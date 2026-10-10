"""Write data/flyers-sentences.json from flyers_ex*.py and flyers_pic.py."""
import json, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[1]
import vocab_check
from flyers_ex1 import EX as A
from flyers_ex2 import EX as B
from flyers_ex3 import EX as C
from flyers_pic import PIC

words = vocab_check.list_words("flyers-vocab.html")
ex = {wid: (en, hl, zh) for wid, en, hl, zh in A + B + C}
pic = {wid: (p, pz, pf) for wid, p, pz, pf in PIC}
assert len(ex) == len(words), (len(ex), len(words))


def slug(t):
    return re.sub(r"[^a-z0-9]+", "_", t.lower()).strip("_")


used = set()
out = {}
for i, (en, pos, zh, cat) in enumerate(words):
    wid = f"w{i}"
    s_en, hl, s_zh = ex[wid]
    assert hl in s_en, wid
    bad = vocab_check.unknown_words(s_en)
    assert not bad, (wid, bad)
    name = slug(re.sub(r"\s*\(.*?\)", "", en)) or wid
    if name in used:
        name = f"{name}_{wid}"
    used.add(name)
    item = {"word": en, "en": s_en, "hl": hl, "zh": s_zh, "audio": f"flyers/s/{name}"}
    if wid in pic:
        p, pz, pf = pic[wid]
        assert not vocab_check.unknown_words(p), (wid, p)
        item.update({"pic": p, "pzh": pz, "paudio": f"flyers/p/{name}"})
        if pf:
            assert not vocab_check.unknown_words(pf), (wid, pf)
            item.update({"pfalse": pf, "pfaudio": f"flyers/q/{name}"})
    out[wid] = item

doc = {
    "version": 1,
    "level": "flyers",
    "note": "Example sentences written for this project; vocabulary limited to the Cambridge Pre A1 Starters, A1 Movers and A2 Flyers wordlists. Audio: Kokoro-82M (Apache-2.0), voices bm_lewis (UK) / af_heart (US).",
    "sentences": out,
}
(ROOT / "data" / "flyers-sentences.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
print(len(out), "sentences,", sum(1 for v in out.values() if "pic" in v), "pictures,", sum(1 for v in out.values() if "pfalse" in v), "changed-detail")
