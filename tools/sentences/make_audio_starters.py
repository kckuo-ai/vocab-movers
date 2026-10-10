#!/usr/bin/env python3
"""Generate MP3s for data/starters-sentences.json with Kokoro-82M.

Same voices as the Movers sentences: UK = bm_fable, US = af_heart, speed 0.95,
pronunciation from Kokoro's own G2P "misaki" (it tells apart words such as
"live" / "lives" by part of speech). Runs the ONNX build of Kokoro, so no GPU
or PyTorch model download is needed.

Setup (once):
    pip install kokoro-onnx misaki num2words spacy soundfile
    python3 -m spacy download en_core_web_sm
    # model files (from github.com/thewh1teagle/kokoro-onnx releases, model-files-v1.0):
    #   kokoro-v1.0.onnx  voices-v1.0.bin   -> put them in tools/sentences/model/ (not committed)
    # ffmpeg must be on the PATH

Run from the repo root, then rebuild the JSON so the "tts" flags are cleared:
    python3 tools/sentences/make_audio_starters.py           # only missing files
    python3 tools/sentences/make_audio_starters.py --force   # regenerate everything
    python3 tools/sentences/build_starters.py

Files: audio/{uk,us}/st/s/<slug>.mp3 (example sentence),
       audio/{uk,us}/st/p/<slug>.mp3 (picture caption),
       audio/{uk,us}/st/q/<slug>.mp3 (false caption).
Sentences made of two parts ("I'm tired. I want to go to bed.") are spoken
part by part in the US voice and joined with a 0.35 s pause, as for Movers,
so a question keeps a natural tone; the UK voice reads them in one go.
Long silences at the start and end are trimmed.
"""
import json, os, re, subprocess, sys, tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from misaki import en, espeak

# words misaki doesn't know (names such as Kim, Hugo, Eva) fall back to the
# espeak-ng library that ships with kokoro-onnx
try:
    import espeakng_loader
    from phonemizer.backend.espeak.wrapper import EspeakWrapper
    EspeakWrapper.set_library(espeakng_loader.get_library_path())
    EspeakWrapper.set_data_path(espeakng_loader.get_data_path())
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "starters-sentences.json"
MODEL_DIR = Path(os.environ.get("KOKORO_DIR", Path(__file__).with_name("model")))
VOICES = {"uk": ("bm_fable", True, "en-gb"), "us": ("af_heart", False, "en-us")}
SPEED = 0.95
SR = 24000
FORCE = "--force" in sys.argv
# files that Whisper misheard with the default voice and that came out clearly
# with another voice / speed: {"uk/st/s/you": ["bm_george", 0.95], ...}
OVERRIDES_FILE = Path(__file__).with_name("starters_voice_overrides.json")
OVERRIDES = json.loads(OVERRIDES_FILE.read_text()) if OVERRIDES_FILE.exists() else {}


def trim(a, keep=0.08, thr=0.01):
    idx = np.where(np.abs(a) > thr)[0]
    if not len(idx):
        return a
    k = int(keep * SR)
    return a[max(0, idx[0] - k): min(len(a), idx[-1] + k)]


def speak(kok, g2p, voice, lang, text, speed=SPEED):
    ph, _ = g2p(text)
    a, sr = kok.create(ph, voice=voice, speed=speed, lang=lang, is_phonemes=True)
    assert sr == SR
    return trim(a)


def make(kok, g2p, voice, lang, split, text, speed=SPEED):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z'])", text) if split else [text]
    pause = np.zeros(int(0.35 * SR), dtype=np.float32)
    out = []
    for i, p in enumerate(parts):
        if i:
            out.append(pause)
        out.append(speak(kok, g2p, voice, lang, p, speed))
    return np.concatenate(out)


def to_mp3(audio, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        sf.write(tmp.name, audio, SR)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp.name,
                        "-ac", "1", "-ar", str(SR), "-b:a", "64k", str(out)], check=True)


def main():
    kok = Kokoro(str(MODEL_DIR / "kokoro-v1.0.onnx"), str(MODEL_DIR / "voices-v1.0.bin"))
    items = list(json.loads(DATA.read_text(encoding="utf-8"))["sentences"].values())
    for accent, (voice, british, lang) in VOICES.items():
        g2p = en.G2P(trf=False, british=british, fallback=espeak.EspeakFallback(british=british))
        n = 0
        for e in items:
            for text_key, path_key in (("en", "audio"), ("pic", "paudio"), ("pfalse", "pfaudio")):
                if text_key not in e:
                    continue
                out = ROOT / "audio" / accent / f"{e[path_key]}.mp3"
                if out.exists() and not FORCE:
                    continue
                v, sp = OVERRIDES.get(f"{accent}/{e[path_key]}", (voice, SPEED))
                to_mp3(make(kok, g2p, v, lang, accent == "us", e[text_key], sp), out)
                n += 1
        print(accent, "files written:", n)


if __name__ == "__main__":
    main()
