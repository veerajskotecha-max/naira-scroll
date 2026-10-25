"""plan.json + thumbs -> site/{t,s,m,st}/NN.webp sprite sheets.
t: every library image, 80x100 (10x10 per sheet)      s: every image in the plan, 240x300 (6x5)
m: grid covers and carousel slides, 720x900 (2x2)      st: story frames, 405x720 (3x2)"""
import json, sys, concurrent.futures as cf
from pathlib import Path
from PIL import Image
D = Path(sys.argv[1]); SITE = D / "site"; plan = json.load(open(D / "plan.json")); L = plan["library"]
TIERS = {"t": ("ti", 80, 100, 10, 10, 68), "s": ("si", 240, 300, 6, 5, 76), "m": ("mi", 600, 750, 2, 2, 78), "st": ("sti", 405, 720, 3, 2, 76)}
only = sys.argv[2:] or list(TIERS)

def cover(iid, w, h):
    im = Image.open(D / "thumbs" / (iid + ".webp")).convert("RGB")
    s = max(w / im.width, h / im.height); im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    x0, y0 = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x0, y0, x0 + w, y0 + h))

def build(tier):
    key, w, h, cols, rows, q = TIERS[tier]; out = SITE / tier; out.mkdir(parents=True, exist_ok=True)
    items = sorted([x for x in L if x.get(key) is not None], key=lambda x: x[key]); per = cols * rows
    sheets = (len(items) + per - 1) // per
    def one(n):
        path = out / f"{n}.webp"
        if path.exists() and tier == "t": return 0
        sh = Image.new("RGB", (cols * w, rows * h), (246, 240, 232))
        for x in items[n * per:(n + 1) * per]:
            i = x[key] - n * per
            try: sh.paste(cover(x["id"], w, h), ((i % cols) * w, (i // cols) * h))
            except Exception as e: print("miss", x["id"], e)
        sh.save(path, "WEBP", quality=q, method=4); return 1
    with cf.ThreadPoolExecutor(6) as ex: made = sum(ex.map(one, range(sheets)))
    size = sum(p.stat().st_size for p in out.glob("*.webp"))
    print(tier, len(items), "images,", sheets, "sheets,", made, "written,", round(size / 1e6, 1), "MB")

for t in only: build(t)
