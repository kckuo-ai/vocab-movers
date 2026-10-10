"""Check that example sentences only use words from the YLE word lists.

Allowed = every word in starters-vocab.html, index.html (Movers) and
flyers-vocab.html, with simple inflections (plural, -ing, -ed, comparatives,
possessive 's) and a short table of irregular forms. Words that are not
allowed are printed so the sentence can be rewritten.
"""
import re, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]


def list_words(fname):
    s = (ROOT / fname).read_text()
    m = re.search(r'const RAW_WORDS = \[(.*?)\n\];', s, re.S)
    return [json.loads('[' + x + ']') for x in re.findall(r'^\s*\[(".*?)\],?\s*$', m.group(1), re.M)]


def base_forms(en):
    """'pajamas (pyjamas)' -> pajamas, pyjamas; 'businessman/woman' -> ...; multiword split."""
    out = set()
    en = en.replace("…", " ")
    for part in re.split(r"[()/]", en):
        for t in re.findall(r"[A-Za-z][A-Za-z'.-]*", part):
            out.add(t.lower().strip(".'"))
    if "businessman/woman" in en:
        out.update({"businessman", "businesswoman", "businesswomen", "businessmen"})
    return out


IRREG = {
    "am": "be", "is": "be", "are": "be", "was": "be", "were": "be", "been": "be", "being": "be",
    "has": "have", "had": "have", "does": "do", "did": "do", "done": "do", "doing": "do",
    "went": "go", "gone": "go", "goes": "go", "made": "make", "came": "come", "saw": "see", "seen": "see",
    "took": "take", "taken": "take", "gave": "give", "given": "give", "got": "get", "gotten": "get",
    "ate": "eat", "eaten": "eat", "drank": "drink", "drunk": "drink", "ran": "run", "swam": "swim",
    "sang": "sing", "sung": "sing", "wrote": "write", "written": "write", "read": "read", "said": "say",
    "told": "tell", "thought": "think", "bought": "buy", "brought": "bring", "caught": "catch",
    "taught": "teach", "found": "find", "knew": "know", "known": "know", "left": "leave", "felt": "feel",
    "kept": "keep", "slept": "sleep", "met": "meet", "sat": "sit", "stood": "stand", "lost": "lose",
    "won": "win", "began": "begin", "begun": "begin", "broke": "break", "broken": "break", "fell": "fall",
    "fallen": "fall", "flew": "fly", "flown": "fly", "forgot": "forget", "forgotten": "forget",
    "heard": "hear", "lay": "lie", "lain": "lie", "let": "let", "put": "put", "cut": "cut", "hit": "hit",
    "rode": "ride", "ridden": "ride", "sold": "sell", "spoke": "speak", "spoken": "speak", "spent": "spend",
    "threw": "throw", "thrown": "throw", "woke": "wake", "wore": "wear", "worn": "wear", "burnt": "burn",
    "drew": "draw", "drawn": "draw", "drove": "drive", "driven": "drive", "hid": "hide", "hidden": "hide",
    "built": "build", "sent": "send", "meant": "mean", "paid": "pay", "understood": "understand",
    "children": "child", "men": "man", "women": "woman", "people": "person", "feet": "foot", "teeth": "tooth",
    "mice": "mouse", "geese": "goose", "sheep": "sheep", "fish": "fish", "knives": "knife", "shelves": "shelf",
    "leaves": "leaf", "wives": "wife", "lives": "life", "better": "good", "best": "good", "worse": "bad",
    "worst": "bad", "more": "more", "most": "most", "less": "less", "further": "far", "farther": "far",
    "i": "i", "me": "i", "my": "my", "mine": "mine", "us": "we", "our": "our", "him": "he", "his": "his",
    "her": "her", "hers": "hers", "them": "they", "their": "their", "its": "its", "it's": "it",
    "can't": "can", "don't": "do", "doesn't": "do", "didn't": "do", "isn't": "be", "aren't": "be",
    "wasn't": "be", "weren't": "be", "won't": "will", "haven't": "have", "hasn't": "have", "shouldn't": "should",
    "couldn't": "could", "i'm": "i", "you're": "you", "we're": "we", "they're": "they", "he's": "he",
    "she's": "she", "that's": "that", "there's": "there", "let's": "let", "what's": "what", "i've": "i",
    "we've": "we", "i'll": "will", "we'll": "will", "you'll": "will", "it'll": "will", "they'll": "will",
    "he'll": "will", "she'll": "will", "i'd": "would", "where's": "where", "who's": "who", "here's": "here",
    "mustn't": "must", "you've": "you", "they've": "they",
}

# grammar words that are in the lists but written differently there, plus
# numbers and a few unavoidable ones
EXTRA = set("""a an the and but or to of in on at for with from by about as than then so
is be am are this that these those there here it you he she we they i who what where when why how which
not no yes very too all some any every each one two three four five six seven eight nine ten eleven twelve
thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty
ninety hundred thousand first second third fourth fifth o'clock mr mrs miss ok okay
shall could would my your his her its our their me him us them mine yours hers ours theirs myself yourself himself herself itself ourselves themselves""".split())


def build_allowed():
    allowed = set(EXTRA)
    names = set()
    for f in ("starters-vocab.html", "index.html", "flyers-vocab.html"):
        for en, pos, zh, cat in list_words(f):
            for b in base_forms(en):
                allowed.add(b)
                if cat == "names" or en[:1].isupper():
                    names.add(b)
    return allowed, names


ALLOWED, NAMES = build_allowed()


def candidates(t):
    """Possible dictionary forms of an inflected token."""
    c = {t}
    if t in IRREG:
        c.add(IRREG[t])
    if t.endswith("'s"):
        c.add(t[:-2])
    for suf, rep in (("ies", "y"), ("es", ""), ("s", ""), ("ied", "y"), ("ed", ""), ("ed", "e"), ("d", ""),
                     ("ing", ""), ("ing", "e"), ("ier", "y"), ("iest", "y"), ("er", ""), ("er", "e"),
                     ("est", ""), ("est", "e"), ("ly", ""), ("ily", "y"), ("'s", "")):
        if t.endswith(suf) and len(t) - len(suf) >= 2:
            stem = t[: len(t) - len(suf)] + rep
            c.add(stem)
            if len(stem) > 2 and stem[-1] == stem[-2]:
                c.add(stem[:-1])  # running -> run, bigger -> big
    return c


SOCIAL = {"please", "hello", "sorry", "wow", "ok", "oh", "t"}  # t = T-shirt


def unknown_words(sentence):
    bad = []
    text = sentence.replace("’", "'")
    # hyphenated list words (x-ray, T-shirt) count as one word
    for raw in re.findall(r"[A-Za-z]+(?:[-.][A-Za-z]+)+\.?", text):
        if raw.lower().strip(".") in ALLOWED or raw.lower() == "t-shirt":
            text = text.replace(raw, " ")
    for raw in re.findall(r"[A-Za-z][A-Za-z']*", text):
        if raw.lower() in SOCIAL:
            continue
        t = raw.lower().strip("'")
        if any(x in ALLOWED for x in candidates(t)):
            continue
        bad.append(raw)
    return bad


if __name__ == "__main__":
    import sys
    for line in sys.argv[1:]:
        print(line, "->", unknown_words(line))
