"""plan.json -> preview_grid.jpg: the finished profile grid (newest at top, pinned row first), 3:4 tiles like Instagram,
with chapter labels in the margin, plus preview_stories.jpg (one week of story frames per chapter)."""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw
D = Path(sys.argv[1]); plan = json.load(open(D / "plan.json")); lib = {x["id"]: x for x in plan["library"]}
TW, TH, GAP, M = 200, 267, 3, 150

def tile(iid, w, h, ar="4:5"):
    im = Image.open(D / "thumbs" / (iid + ".webp")).convert("RGB")
    s = max(w / im.width, h / im.height); im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    x0, y0 = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x0, y0, x0 + w, y0 + h))

rows = [plan["pinned"]]
chapters = plan["chapters"]
for ci in reversed(range(len(chapters))):
    ct = [t for t in plan["tiles"] if t["chapter"] == ci]
    for r in range(5):
        rows.append([next(t for t in ct if t["row"] == r and t["col"] == c) for c in ("object", "worn", "detail")])
H = len(rows) * (TH + GAP) + 40
sheet = Image.new("RGB", (M + 3 * (TW + GAP) + 20, H), "white"); d = ImageDraw.Draw(sheet)
y = 20
for ri, row in enumerate(rows):
    for ci, t in enumerate(row):
        x = M + ci * (TW + GAP)
        try: sheet.paste(tile(t["cover"], TW, TH), (x, y))
        except Exception as e: d.rectangle([x, y, x + TW, y + TH], fill="#ddd")
        tag = {"carousel": f"carousel {len(t['slides'])}", "reel": f"REEL {t.get('reel','')} {len(t.get('frames', []))}f", "single": ""}[t["type"]]
        lab = f"{t['date'][5:]} {tag}".strip(); d.rectangle([x, y + TH - 16, x + TW, y + TH], fill=(255, 255, 255))
        d.text((x + 3, y + TH - 15), (lab + " · " + (lib[t["cover"]]["n"] or lib[t["cover"]]["c"] or ""))[:38], fill="black")
    if ri == 0: d.text((6, y + 4), "PINNED (evergreen)", fill="black")
    elif (ri - 1) % 5 == 0:
        c = chapters[len(chapters) - 1 - (ri - 1) // 5]
        d.text((6, y + 4), f"{c['num']} {c['name']}", fill="black"); d.text((6, y + 18), f"{c['start']} to {c['end']}", fill="black")
        d.text((6, y + 32), "row: " + ", ".join(c["pal"][:3]), fill="black")
    y += TH + GAP
sheet.save(D / "preview_grid.jpg", quality=82)

# stories: first 7 days of each chapter
cols = 21; cw, chh = 90, 160
st = Image.new("RGB", (cols * (cw + 2) + 10, 6 * (chh + 30)), "white"); d = ImageDraw.Draw(st)
for ci, c in enumerate(chapters):
    days = [s for s in plan["stories"] if s["chapter"] == ci][:7]
    d.text((4, ci * (chh + 30) + 2), f"{c['num']} {c['name']} - stories, first week (3 a day)", fill="black")
    k = 0
    for s in days:
        for f in s["frames"]:
            try: st.paste(tile(f["id"], cw, chh), (4 + k * (cw + 2), ci * (chh + 30) + 16))
            except Exception: pass
            k += 1
st.save(D / "preview_stories.jpg", quality=80)
print("ok", len(rows), "rows")

# per-chapter sheets, readable size
TW2, TH2 = 300, 400
for ci, c in enumerate(chapters + [None]):
    rws = rows[1 + 5 * (len(chapters) - 1 - ci): 1 + 5 * (len(chapters) - ci)] if c else rows[:1]
    sh = Image.new("RGB", (3 * (TW2 + GAP), len(rws) * (TH2 + GAP) + 24), "white"); d = ImageDraw.Draw(sh)
    d.text((4, 4), (f"{c['num']} {c['name']} {c['start']}..{c['end']}" if c else "PINNED"), fill="black")
    for ri, row in enumerate(rws):
        for cj, t in enumerate(row):
            x, yy = cj * (TW2 + GAP), 24 + ri * (TH2 + GAP)
            try: sh.paste(tile(t["cover"], TW2, TH2), (x, yy))
            except Exception: pass
            tag = {"carousel": f"carousel {len(t['slides'])}", "reel": f"REEL {t.get('reel','')} {len(t.get('frames', []))}f", "single": "single"}[t["type"]]
            L = lib[t["cover"]]; d.rectangle([x, yy + TH2 - 30, x + TW2, yy + TH2], fill=(255, 255, 255))
            d.text((x + 4, yy + TH2 - 28), f"{t['date'][5:]} {t['time']} {tag}"[:46], fill="black")
            d.text((x + 4, yy + TH2 - 14), f"{L['k']} · {L['p']} · {(L['n'] or L['c'] or '')}"[:46], fill="black")
    sh.save(D / f"preview_ch{ci if c else 'pin'}.jpg", quality=82)
