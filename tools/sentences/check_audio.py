"""Listen to every sentence MP3 with Whisper small.en (sherpa-onnx) and list the
ones whose transcript does not match the text.

    python3 tools/sentences/check_audio.py data/flyers-sentences.json WHISPER_DIR [uk|us]
"""
import json, sys, subprocess, pathlib, re, difflib
import numpy as np
import sherpa_onnx

ROOT = pathlib.Path(__file__).resolve().parents[2]
NUM = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
       "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "twenty": "20", "thirty": "30", "fifty": "50",
       "hundred": "100", "first": "1st"}


def norm(t):
    t = t.lower().replace("’", "'").replace("–", " ").replace("-", " ")
    t = t.replace("a.m.", "am").replace("p.m.", "pm")
    t = re.sub(r"\ba m\b", "am", t)
    t = re.sub(r"\bp m\b", "pm", t)
    t = t.replace("mr ", "mister ").replace("mr. ", "mister ")
    t = re.sub(r"(\d)([a-z])", r"\1 \2", t)  # 8pm -> 8 pm
    t = re.sub(r"\ba\.?m\b\.?", "am", t)
    t = re.sub(r"\bp\.?m\b\.?", "pm", t)
    words = re.findall(r"[a-z0-9']+", t)
    return [NUM.get(w, w) for w in words]


def load(path):
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(pcm, dtype=np.int16).astype(np.float32) / 32768


def main():
    doc = json.loads(pathlib.Path(sys.argv[1]).read_text())
    wd = pathlib.Path(sys.argv[2])
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    accents = [a for a in sys.argv[3:] if a in ("uk", "us")] or ["uk", "us"]
    rec = sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=str(wd / "small.en-encoder.int8.onnx"), decoder=str(wd / "small.en-decoder.int8.onnx"),
        tokens=str(wd / "small.en-tokens.txt"), num_threads=4)
    bad = []
    n = 0
    for acc in accents:
        for wid, s in doc["sentences"].items():
            if only and wid not in only:
                continue
            for tkey, akey in (("en", "audio"), ("pic", "paudio"), ("pfalse", "pfaudio")):
                if not s.get(tkey):
                    continue
                f = ROOT / "audio" / acc / f"{s[akey]}.mp3"
                if not f.exists():
                    continue
                st = rec.create_stream()
                st.accept_waveform(16000, load(f))
                rec.decode_stream(st)
                heard = st.result.text.strip()
                a, b = norm(s[tkey]), norm(heard)
                ratio = difflib.SequenceMatcher(None, a, b).ratio()
                n += 1
                # the target word itself must be heard, and the rest nearly so
                key = norm(s["hl"]) if tkey == "en" else []
                missing_key = key and not all(k in b for k in key)
                if ratio < 0.85 or missing_key:
                    bad.append((acc, wid, akey, round(ratio, 2), s[tkey], heard))
    for x in bad:
        print("\t".join(map(str, x)))
    print(f"checked {n}, flagged {len(bad)}", file=sys.stderr)


if __name__ == "__main__":
    main()
