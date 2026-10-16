# Picks every Edition One plate that passed verification at the 8.5 run bar (or every pass with --all) and writes final_e1.json
# for pdfs_e1.py and the board page. Verdicts come from verify/*.json; frame facts from frames.json and frames_bold.json.
# Usage: select_e1.py [final_e1.json] [--all]
import json, os, sys, glob
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e1"
BAR = 0 if "--all" in sys.argv else 8.5
frames = {}
for fn in ["frames.json", "frames_bold.json"]:
    p = f"{HERE}/{fn}"
    if os.path.exists(p):
        for f in json.load(open(p))["frames"]: frames[f["id"]] = f
pieces = json.load(open(f"{HERE}/frames.json"))["pieces"]

verdicts = {}
for p in sorted(glob.glob(f"{HERE}/verify/*.json"), key=os.path.getmtime):
    for v in json.load(open(p)):
        verdicts[v["plate"].rsplit(".", 1)[0]] = dict(v, src=os.path.basename(p))

best = {}
for stem, v in verdicts.items():
    if not v.get("pass") or v.get("score") is None or v["score"] < BAR: continue
    fid = stem.split("_")[0]
    if fid not in frames: continue
    if fid not in best or v["score"] > best[fid][1]["score"]: best[fid] = (stem, v)

final = {}
for fid, (stem, v) in sorted(best.items(), key=lambda kv: -kv[1][1]["score"]):
    f = frames[fid]; w, h = Image.open(f"{SP}/plates/{stem}.png").size
    notes = v.get("notes") or []
    final.setdefault(f["camp"], []).append(dict(id=fid, file=f"{stem}.png", score=v["score"], name=f["name"], copy=f["copy"],
        aspect=f["aspect"], w=w, h=h, note=notes[0] if isinstance(notes, list) and notes else ""))
for k in pieces:
    print(f"{k:11} {len(final.get(k, [])):2}  " + ", ".join(f"{i['id']} {i['score']}" for i in final.get(k, [])))
print(sum(len(v) for v in final.values()), "verified plates")
out = [a for a in sys.argv[1:] if not a.startswith("--")]
if out:
    json.dump(final, open(out[0], "w"), indent=1, ensure_ascii=False); print("wrote", out[0])
