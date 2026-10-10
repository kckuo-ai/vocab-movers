#!/usr/bin/env python3
"""Check the Starters sentence MP3s with Whisper small.en (via sherpa-onnx).

Every file is transcribed and compared with its sentence after removing
case and punctuation; numbers written as digits are spelled out first.
Prints the files whose transcript differs, so they can be listened to and,
if needed, regenerated (delete the MP3 and run make_audio_starters.py again).

    pip install sherpa-onnx
    # model: sherpa-onnx-whisper-small.en from github.com/k2-fsa/sherpa-onnx releases (asr-models)
    WHISPER_DIR=/path/to/sherpa-onnx-whisper-small.en python3 tools/sentences/check_audio_starters.py
"""
import json, os, re, subprocess, sys
from pathlib import Path

import numpy as np
import sherpa_onnx

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "starters-sentences.json"
WD = Path(os.environ.get("WHISPER_DIR", Path(__file__).with_name("whisper")))
NUM = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
       "8": "eight", "9": "nine", "10": "ten", "20": "twenty"}
# spellings Whisper may use for the same spoken words
SAME = {"mum": "mom", "colour": "color", "favourite": "favorite", "grey": "gray", "ok": "okay",
        "teddy": "teddy", "t shirt": "tshirt"}


def norm(s):
    s = s.lower().replace("-", " ").replace("’", "'")
    s = re.sub(r"\d+", lambda m: NUM.get(m.group(0), m.group(0)), s)
    for a, b in (("we're", "we are"), ("you're", "you are"), ("they're", "they are"), ("i'm", "i am"),
                 ("it's", "it is"), ("there's", "there is"), ("that's", "that is"), ("i've", "i have"),
                 ("you've", "you have"), ("she's", "she is"), ("he's", "he is"), ("what's", "what is"),
                 ("where's", "where is"), ("here's", "here is"), ("let's", "let us"), ("isn't", "is not"),
                 ("don't", "do not"), ("can't", "cannot"), ("can not", "cannot")):
        s = s.replace(a, b)
    s = re.sub(r"[^a-z' ]+", " ", s).replace("'", "")
    s = " ".join(s.split())
    for a, b in SAME.items():
        s = re.sub(rf"\b{a}\b", b, s)
    return s.replace("t shirt", "tshirt")


def load(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(path), "-f", "s16le", "-ac", "1",
                          "-ar", "16000", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768


def main():
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=str(WD / "small.en-encoder.int8.onnx"), decoder=str(WD / "small.en-decoder.int8.onnx"),
        tokens=str(WD / "small.en-tokens.txt"), language="en", task="transcribe", num_threads=4)
    items = json.loads(DATA.read_text(encoding="utf-8"))["sentences"].values()
    bad = total = 0
    only = sys.argv[1:]  # optional: uk / us
    for accent in only or ["uk", "us"]:
        for e in items:
            for tk, pk in (("en", "audio"), ("pic", "paudio"), ("pfalse", "pfaudio")):
                if tk not in e:
                    continue
                f = ROOT / "audio" / accent / f"{e[pk]}.mp3"
                if not f.exists():
                    continue
                st = rec.create_stream()
                st.accept_waveform(16000, load(f))
                rec.decode_stream(st)
                got = st.result.text.strip()
                total += 1
                if norm(got) != norm(e[tk]):
                    bad += 1
                    print(f"{accent}\t{e[pk]}\t{e[tk]}\t=> {got}")
    print(f"checked {total}, different {bad}")


if __name__ == "__main__":
    main()
