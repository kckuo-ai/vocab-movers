"""Build offline-manifest.json: a fingerprint for every file the offline mode can store.

The level pages compare these fingerprints with the ones they saved when they
downloaded each file, so 設定 → 離線使用 only fetches files that are new or
changed instead of downloading the whole level again.

Run after changing any picture, sound, sentence file or page:
    python3 tools/offline/build_manifest.py           # write the file
    python3 tools/offline/build_manifest.py --check   # exit 1 if it is out of date

Three files, so a page only fetches what it can use:
    offline-manifest.json      pages, data, pictures
    offline-manifest-uk.json   British sounds (audio/uk/...)
    offline-manifest-us.json   American sounds (audio/us/...)
Format (grouped by folder to keep it small):
    {"v": 1, "files": {"img/": {"c_road.svg": "<10 hex sha1>:<bytes>", ...}, "": {"index.html": ...}}}
"""
import hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PARTS = {"offline-manifest.json": lambda f: not f.startswith("audio/"),
         "offline-manifest-uk.json": lambda f: f.startswith("audio/uk/"),
         "offline-manifest-us.json": lambda f: f.startswith("audio/us/")}
PATTERNS = ["*.html", "manifest.webmanifest", "data/*.json", "img/*", "audio/**/*.mp3"]


def build():
    groups = {}
    seen = set()
    for pat in PATTERNS:
        for p in sorted(ROOT.glob(pat)):
            if not p.is_file() or p in seen:
                continue
            seen.add(p)
            rel = p.relative_to(ROOT).as_posix()
            folder, _, name = rel.rpartition("/")
            data = p.read_bytes()
            groups.setdefault(folder + "/" if folder else "", {})[name] = f"{hashlib.sha1(data).hexdigest()[:10]}:{len(data)}"
    return {name: {"v": 1, "files": {k: groups[k] for k in sorted(groups) if keep(k)}} for name, keep in PARTS.items()}


def dump(m):
    return json.dumps(m, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n"


if __name__ == "__main__":
    stale = []
    for name, m in build().items():
        out, text = ROOT / name, dump(m)
        if "--check" in sys.argv:
            if not out.exists() or out.read_text() != text:
                stale.append(name)
        else:
            out.write_text(text)
            n = sum(len(v) for v in m["files"].values())
            print(f"wrote {name}: {n} files, {len(text) // 1024} KB")
    if "--check" in sys.argv:
        if stale:
            print("out of date: " + ", ".join(stale) + " (run python3 tools/offline/build_manifest.py)")
            sys.exit(1)
        print("offline manifests are up to date")
