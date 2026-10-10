#!/usr/bin/env python3
"""Build data/starters-sentences.json from tools/sentences/starters.txt.

Each line of starters.txt:
    id|sentence|highlight|中文|picture caption|中文|false caption
The last three fields are optional (caption + 中文 are needed for 對或錯,
the false caption is optional). Run from the repo root:

    python3 tools/sentences/build_starters.py

Checks before writing:
  * every word in the Starters page has exactly one sentence (matched by id
    and word text, read from starters-vocab.html)
  * the highlight appears in the sentence as a whole word
  * every word in every sentence / caption is a Pre A1 Starters word
    (the page's word list plus the basic grammar words and numbers listed
    in EXTRA below) — anything else is reported and nothing is written
Audio paths point to audio/{uk,us}/st/{s,p,q}/<slug>.mp3. Until those MP3s
exist each entry carries "tts": true and the page reads it with the device
voice; tools/sentences/make_audio_starters.py creates the MP3s and clears the flag.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = Path(__file__).with_name("starters.txt")
PAGE = ROOT / "starters-vocab.html"
OUT = ROOT / "data" / "starters-sentences.json"

# Basic words that are on the Pre A1 Starters list but are not separate
# entries in the page's word list (articles, be, possessives, numbers...).
EXTRA = set("""
the is are am isn't aren't my your our their at up down has does doesn't don't
can't do were here's there's it's that's what's where's who's let's i'm i've you've
you're we're they're he's she's hello goodbye please thank thanks
one two three four five six seven eight nine ten eleven twelve thirteen fourteen
fifteen sixteen seventeen eighteen nineteen twenty
""".split())

IRREGULAR = {"mice": "mouse", "feet": "foot", "men": "man", "women": "woman",
             "children": "child", "people": "person", "has": "have", "does": "do",
             "is": "be", "are": "be", "am": "be"}


def page_words():
    h = PAGE.read_text(encoding="utf-8")
    raw = h[h.index("const RAW_WORDS = ["):h.index("const WORDS =")]
    rows = re.findall(r'\["((?:[^"\\]|\\.)*)", "([^"]+)", "([^"]+)", "([^"]+)"\]', raw)
    return [r[0].replace('\\"', '"') for r in rows]


def vocab(words):
    v = set(EXTRA)
    for w in words:
        for part in re.split(r"[\s/()]+", w.lower()):
            part = part.strip()
            if part:
                v.add(part)
                v.add(part.replace("-", ""))
    return v


def lemmas(tok):
    out = {tok}
    if tok in IRREGULAR:
        out.add(IRREGULAR[tok])
    if tok.endswith("ies"):
        out.add(tok[:-3] + "y")
    if tok.endswith("es"):
        out.add(tok[:-2])
    if tok.endswith("s"):
        out.add(tok[:-1])
    if tok.endswith("ing"):
        b = tok[:-3]
        out |= {b, b + "e"}
        if len(b) > 2 and b[-1] == b[-2]:
            out.add(b[:-1])
    return out


def unknown_words(text, v):
    bad = []
    for tok in re.findall(r"[A-Za-z][A-Za-z'\-]*", text):
        t = tok.lower().strip("'")
        if t in v:
            continue
        if t.endswith("'s") and t[:-2] in v | EXTRA:
            continue
        t2 = t[:-2] if t.endswith("'s") else t
        if any(l in v for l in lemmas(t2)) or len(t2) == 1:
            continue
        bad.append(tok)
    return bad


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def main():
    words = page_words()
    v = vocab(words)
    items, errors = {}, []
    for n, line in enumerate(SRC.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        f = line.split("|")
        wid, en, hl, zh = f[0], f[1], f[2], f[3]
        i = int(wid[1:])
        if i >= len(words):
            errors.append(f"line {n}: {wid} is not in the word list")
            continue
        m = re.search(r"(?<![A-Za-z])" + re.escape(hl) + r"(?![A-Za-z])", en)
        if not m or en.find(hl) != m.start():
            errors.append(f"line {n}: highlight '{hl}' is not the first whole-word match in '{en}'")
        texts = [en] + ([f[4]] if len(f) > 4 else []) + ([f[6]] if len(f) > 6 else [])
        for t in texts:
            for b in unknown_words(t, v):
                errors.append(f"line {n} ({words[i]}): '{b}' is not a Starters word — {t}")
        items[wid] = f
    for i, w in enumerate(words):
        if f"w{i}" not in items:
            errors.append(f"missing sentence for w{i} {w}")
    if errors:
        print("\n".join(errors))
        sys.exit(1)

    # one slug per word; words listed twice (orange, clean, colour) get the id appended
    base = {}
    for i, w in enumerate(words):
        base.setdefault(slug(w), []).append(i)
    out = {}
    for i, w in enumerate(words):
        f = items[f"w{i}"]
        sg = slug(w) if len(base[slug(w)]) == 1 else f"{slug(w)}_{i}"
        e = {"word": w, "en": f[1], "hl": f[2], "zh": f[3], "audio": f"st/s/{sg}"}
        if len(f) > 5:
            e.update(pic=f[4], pzh=f[5], paudio=f"st/p/{sg}")
        if len(f) > 6:
            e.update(pfalse=f[6], pfaudio=f"st/q/{sg}")
        for d in ("uk", "us"):
            have = all((ROOT / "audio" / d / f"{p}.mp3").exists()
                       for p in (e["audio"], e.get("paudio"), e.get("pfaudio")) if p)
            if not have:
                e["tts"] = True
        out[f"w{i}"] = e
    doc = {
        "version": 1,
        "level": "starters",
        "note": "Example sentences written for this project; vocabulary limited to the Cambridge Pre A1 Starters wordlist. "
                "Entries with tts:true have no MP3 yet and are read with the device voice.",
        "sentences": out,
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    pics = sum(1 for e in out.values() if "pic" in e)
    fals = sum(1 for e in out.values() if "pfalse" in e)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out)} sentences, {pics} picture captions, {fals} false captions, "
          f"{sum(1 for e in out.values() if e.get('tts'))} without MP3")


if __name__ == "__main__":
    main()
