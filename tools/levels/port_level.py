"""Rebuild a level page (Starters / Flyers) from the Movers page (index.html).

index.html is the template: it has every feature. This script copies it and
puts back the parts that belong to the target level, taken from the target's
current page: word list + categories, picture map, colours, titles, storage
keys, settings links, credits. Level settings that the old page does not have
(sentence file, 對或錯 categories / look-alike groups) come from LEVELS below.

Usage:  python3 tools/levels/port_level.py flyers
The old page is overwritten; git keeps the previous version.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]

LEVELS = {
    "flyers": {
        "file": "flyers-vocab.html",
        "prefix": "flyers-vocab-",
        "sentences": "data/flyers-sentences.json",
        "sent_scope": "Starters + Movers + Flyers",
        "tf_cats": ["animals", "body", "clothes", "colours", "food", "health", "home", "places", "school",
                    "sports", "time", "transport", "weather", "work", "world"],
        # pictures that look alike when small never stand in for each other
        "tf_confusable": [
            ["cooker", "oven", "fridge"], ["envelope", "letter (mail)", "invitation", "stamp", "post office"],
            ["a.m.", "p.m.", "midday", "midnight", "time", "hour", "minute", "quarter"],
            ["tyre (tire)", "wheel", "bicycle"], ["fog", "foggy", "storm", "winter"],
            ["college", "university", "student"], ["rocket", "spaceship", "astronaut", "space", "planet", "Earth"],
            ["snowboard", "snowboarding", "ski", "sledge"], ["airport", "land", "pilot"],
            ["police officer", "police station"], ["fire engine (fire truck)", "fire station", "fire fighter", "fire", "ambulance"],
            ["concert", "singer", "stage (theatre)", "pop music", "theatre (theater)"], ["prize", "winner", "competition", "race"],
            ["stream", "path", "railway"], ["crown", "queen"], ["spot", "spotted", "stripe", "striped", "beetle", "insect"],
            ["knife", "fork", "spoon", "meal", "chopsticks"], ["flour", "sugar", "salt"], ["museum", "bank", "theatre (theater)", "hotel", "post office"],
            ["autumn (fall)", "spring", "summer", "winter"], ["hill", "desert", "view"], ["diary", "dictionary", "magazine"],
            ["engineer", "mechanic", "fire fighter"], ["drum", "violin", "instrument"],
            ["artist", "pilot", "student", "photographer", "journalist"], ["mechanic", "police officer", "pilot", "waiter"],
            ["spot", "pizza", "strawberry"],
        ],
    },
}


def grab(pattern, text, what):
    m = re.search(pattern, text, re.S | re.M)
    if not m:
        raise SystemExit(f"cannot find {what}")
    return m.group(0)


def swap(pattern, new, text, what, count=1):
    rx = re.compile(pattern, re.S | re.M)
    found = len(rx.findall(text))
    if found != count:
        raise SystemExit(f"{what}: expected {count} match, found {found}")
    return rx.sub(lambda m: new, text)


def js_list(items):
    import json
    return json.dumps(items, ensure_ascii=False)


def port(level):
    cfg = LEVELS[level]
    tpl = (ROOT / "index.html").read_text()
    old = (ROOT / cfg["file"]).read_text()
    out = tpl

    # head: colour + title
    for pat, what in ((r'^<meta name="theme-color" content="[^"]*" />$', "theme colour"),
                      (r'^<title>[^\n]*</title>$', "title"),
                      (r'^  --hdrA:[^\n]*$', "header colours")):
        out = swap(pat, grab(pat, old, what), out, what)

    # word data comment + RAW_WORDS + CATEGORIES (everything up to CAT_MAP)
    pat = r'^/\* =+\n   劍橋 .*?(?=^const CAT_MAP)'
    out = swap(pat, grab(pat, old, "word data"), out, "word data")

    # picture map
    pat = r'^const IMG = \{[^\n]*\};$'
    out = swap(pat, grab(pat, old, "IMG"), out, "IMG")

    # storage keys (progress, scores, daily, voice, sound effects)
    out = re.sub(r'"movers-vocab-(progress|hiscore|daily|voice|fx)-v1"', lambda m: f'"{cfg["prefix"]}{m.group(1)}-v1"', out)

    # titles, header tag, credits, settings links
    for pat, what in ((r'^  home: \["單字護照", [^\n]*$', "home title"),
                      (r'^    <div class="htagRow"><div class="htag">[^\n]*$', "header tag"),
                      (r'^      <div>單字範圍參考 [^\n]*$', "credits"),
                      (r'(?:^    <a class="appLink" href="[^"]*">[^\n]*\n)+', "level links")):
        out = swap(pat, grab(pat, old, what), out, what)

    # sentences + 對或錯 settings
    out = out.replace("EXAMPLE SENTENCES (data/movers-sentences.json)", f"EXAMPLE SENTENCES ({cfg['sentences']})")
    out = out.replace("One sentence per word, vocabulary limited to Starters + Movers.",
                      f"One sentence per word, vocabulary limited to {cfg['sent_scope']}.")
    out = swap(r'^const SENT_URL = "[^"\n]*";$', f'const SENT_URL = "{cfg["sentences"]}";', out, "SENT_URL")
    out = swap(r'^const TF_CATS = \[[^\n]*\];$', f'const TF_CATS = {js_list(cfg["tf_cats"])};', out, "TF_CATS")
    groups = ",\n".join("  " + js_list(g) for g in cfg["tf_confusable"])
    out = swap(r'^const TF_CONFUSABLE = \[\n.*?\n\];$', f'const TF_CONFUSABLE = [\n{groups},\n];', out, "TF_CONFUSABLE")

    leftover = [l for l in out.splitlines() if re.search(r'movers', l, re.I)
                and "RAW_WORDS" not in l and '["movers-vocab", "Movers"]' not in l and 'href="index.html"' not in l]
    if leftover:
        print("check these lines that still mention Movers:")
        for l in leftover:
            print("  ", l.strip()[:140])
    (ROOT / cfg["file"]).write_text(out)
    print(f"wrote {cfg['file']} ({len(out)} bytes)")


if __name__ == "__main__":
    port(sys.argv[1] if len(sys.argv) > 1 else "flyers")
