"""Generate sentence MP3s for a level with Kokoro-82M (kokoro-onnx), using the
same settings as the Movers sentences (see README):

  - voices: bm_fable (UK), af_heart (US); speed 0.95
  - pronunciation from misaki (Kokoro's own G2P, picks the right reading of
    words like "lives" / "read" from the part of speech), espeak as fallback
  - long pauses shortened; US two-sentence examples are made one sentence at a
    time and joined with a 0.35 s pause (keeps question intonation natural)
  - 24 kHz mono 64 kb/s MP3, leading / trailing silence trimmed

    python3 tools/sentences/make_audio.py data/flyers-sentences.json MODEL_DIR [--redo id,id] [--accent uk|us]

Existing files are skipped unless their word id is listed in --redo.
"""
import json, sys, subprocess, pathlib, re, tempfile
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from misaki import en, espeak

ROOT = pathlib.Path(__file__).resolve().parents[2]
VOICES = {"uk": ("bm_fable", True), "us": ("af_heart", False)}
# a few words misaki gets wrong (British phonemes)
PHONEME_FIX = {"kˈɒmz": "kˈQmz"}  # combs
# sentences that the main voice says unclearly (found with check_audio.py):
# file path -> other voice. Kept in a JSON file next to the sentence data.
SPEED = 0.95
SR = 24000


def spoken(text):
    """Text as it should be read aloud."""
    t = text.replace("–", "-")
    t = re.sub(r"\b(\w+) - (\w+)\b", r"\1, \2", t)  # score "two - one"
    t = t.replace("a.m.", "A M").replace("p.m.", "P M")
    return t


def split_sentences(text):
    parts = re.findall(r"[^.!?]+[.!?]+(?:\s|$)", text + " ")
    parts = [p.strip() for p in parts if p.strip()]
    return parts if len(parts) > 1 else [text]


def main():
    doc = json.loads(pathlib.Path(sys.argv[1]).read_text())
    model = pathlib.Path(sys.argv[2])
    redo = set(sys.argv[sys.argv.index("--redo") + 1].split(",")) if "--redo" in sys.argv else set()
    accents = [sys.argv[sys.argv.index("--accent") + 1]] if "--accent" in sys.argv else list(VOICES)
    vfile = pathlib.Path(sys.argv[1]).with_name(pathlib.Path(sys.argv[1]).stem + "-voices.json")
    override = json.loads(vfile.read_text()) if vfile.exists() else {}
    k = Kokoro(str(model / "kokoro-v1.0.onnx"), str(model / "voices-v1.0.bin"))
    jobs = []
    for wid, s in doc["sentences"].items():
        for tkey, akey in (("en", "audio"), ("pic", "paudio"), ("pfalse", "pfaudio")):
            if s.get(tkey):
                jobs.append((wid, s[tkey], s[akey]))
    done = 0
    for acc in accents:
        voice, british = VOICES[acc]
        g2p = en.G2P(trf=False, british=british, fallback=espeak.EspeakFallback(british=british))

        def say(text, v):
            ph, _ = g2p(spoken(text))
            for bad, good in PHONEME_FIX.items():
                ph = ph.replace(bad, good)
            samples, sr = k.create(ph, voice=v, speed=SPEED, is_phonemes=True)
            assert sr == SR
            return samples

        for wid, text, path in jobs:
            out = ROOT / "audio" / acc / f"{path}.mp3"
            if out.exists() and wid not in redo:
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            v = override.get(f"{acc}/{path}", voice)
            parts = split_sentences(spoken(text)) if acc == "us" else [text]
            if len(parts) > 1:
                gap = np.zeros(int(SR * 0.35), dtype=np.float32)
                pieces = []
                for i, p in enumerate(parts):
                    pieces.append(np.trim_zeros(say(p, v).astype(np.float32)))
                    if i < len(parts) - 1:
                        pieces.append(gap)
                samples = np.concatenate(pieces)
            else:
                samples = say(text, v)
            with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
                sf.write(tmp.name, samples, SR)
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp.name, "-af",
                                # shorten pauses longer than 0.45 s, then trim both ends
                                "silenceremove=stop_periods=-1:stop_duration=0.45:stop_threshold=-45dB:stop_silence=0.45,"
                                "silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.05,"
                                "areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.1,areverse",
                                "-ar", str(SR), "-ac", "1", "-b:a", "64k", str(out)], check=True)
            done += 1
            if done % 50 == 0:
                print(acc, done, "files", flush=True)
    print("done", done)


if __name__ == "__main__":
    main()
