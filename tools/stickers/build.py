"""Write img/t_<name>.svg for every sticker.  Run: python3 tools/stickers/build.py [series...]"""
import sys, pathlib, importlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
OUT = HERE.parent.parent / "img"
SERIES = ["zoo", "sea", "magic", "sweet", "play"]
names = []
for s in (sys.argv[1:] or SERIES):
    if not (HERE / f"{s}.py").exists():
        continue
    mod = importlib.import_module(s)
    for name, fn in mod.STICKERS.items():
        (OUT / f"t_{name}.svg").write_text(fn())
        names.append(name)
print(" ".join(names))
