# Picks the best verified plate per frame from every verdict in verify/ and writes final.json for pdfs.py and build_page.py.
# A plate qualifies when its latest verdict passes; among qualifiers the highest ad score wins (8.5+ runs as-is).
# Usage: select.py [final.json]      prints a per-frame table, including frames that still have no passing plate
import json, os, sys, glob
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/c4"
D = json.load(open(f"{HERE}/frames.json"))
BAR = 8.5

verdicts = {}                     # plate stem -> latest verdict (files are read oldest first, so later rounds win)
for p in sorted(glob.glob(f"{HERE}/verify/*.json"), key=os.path.getmtime):
    for v in json.load(open(p)):
        stem = v["plate"].rsplit(".", 1)[0]
        if "_" not in stem: stem += "_a1"          # round-1 prism verdicts name the frame only
        verdicts[stem] = dict(v, src=os.path.basename(p))

final, table = {}, []
for f in D["frames"]:
    cands = [(stem, v) for stem, v in verdicts.items() if stem.split("_")[0] == f["id"] and v.get("pass") and v.get("score") is not None]
    cands.sort(key=lambda sv: (sv[1]["score"], sv[0]), reverse=True)
    if not cands:
        table.append((f["id"], f["name"], "-", "NONE", "")); continue
    stem, v = cands[0]
    w, h = Image.open(f"{SP}/plates/{stem}.png").size
    notes = v.get("notes") or []
    note = notes[0] if isinstance(notes, list) and notes else (notes if isinstance(notes, str) else "")
    if v["score"] >= BAR or "--all" in sys.argv:     # the deliverables carry only frames that run as-is
        final.setdefault(f["camp"], []).append(dict(id=f["id"], file=f"{stem}.png", score=v["score"], note=note, w=w, h=h, src=v["src"]))
    table.append((f["id"], f["name"], stem, f"{v['score']:.1f}", "" if v["score"] >= BAR else "below bar"))

for row in table: print("{:4} {:28} {:10} {:5} {}".format(*row))
ok = sum(1 for r in table if r[3] != "NONE" and r[4] == "")
print(f"{ok}/{len(table)} frames at {BAR}+")
outp = [a for a in sys.argv[1:] if not a.startswith("--")]
if outp:
    json.dump(final, open(outp[0], "w"), indent=1, ensure_ascii=False); print("wrote", outp[0])
