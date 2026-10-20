# Downloads a small copy of every image of every in-stock Naira Petite product, then draws contact sheets
# (one row per product, images numbered by position) so the on-model photo of each product can be picked by eye.
import json, os, sys, urllib.request, concurrent.futures as cf
from PIL import Image, ImageDraw, ImageFont
SRC = sys.argv[1]; OUT = sys.argv[2]
ps = [p for p in json.load(open(f"{SRC}/products.json"))["products"] if p["vendor"] == "Naira Petite" and any(v.get("available") for v in p["variants"])]
ps.sort(key=lambda p: (p["product_type"], p["title"]))
jobs = []
for p in ps:
    for i, im in enumerate(p["images"]):
        u = im["src"] + ("&" if "?" in im["src"] else "?") + "width=260"
        jobs.append((u, f"{SRC}/thumbs/{p['handle']}/{i+1:02d}.jpg"))
def get(j):
    u, f = j
    if os.path.exists(f): return
    os.makedirs(os.path.dirname(f), exist_ok=True)
    with urllib.request.urlopen(u, timeout=60) as r: open(f, "wb").write(r.read())
with cf.ThreadPoolExecutor(16) as ex: list(ex.map(get, jobs))
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 15) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default()
TW, TH, PER = 150, 186, 10
os.makedirs(OUT, exist_ok=True)
for s in range(0, len(ps), PER):
    chunk = ps[s:s+PER]; cols = max(len(p["images"]) for p in chunk)
    sheet = Image.new("RGB", (230 + cols * (TW + 4), len(chunk) * (TH + 6)), "white"); d = ImageDraw.Draw(sheet)
    for r, p in enumerate(chunk):
        y = r * (TH + 6)
        d.text((6, y + 8), f"{s+r+1}. {p['title'][:22]}", fill="black", font=font)
        d.text((6, y + 30), p["product_type"], fill="gray", font=font)
        for i in range(len(p["images"])):
            f = f"{SRC}/thumbs/{p['handle']}/{i+1:02d}.jpg"
            im = Image.open(f).convert("RGB"); im.thumbnail((TW, TH))
            x = 230 + i * (TW + 4); sheet.paste(im, (x, y))
            d.rectangle([x, y, x + 22, y + 20], fill="black"); d.text((x + 4, y + 1), str(i + 1), fill="yellow", font=font)
    sheet.save(f"{OUT}/sheet_{s//PER+1:02d}.jpg", quality=80)
json.dump([dict(n=k+1, handle=p["handle"], title=p["title"], type=p["product_type"], imgs=len(p["images"])) for k, p in enumerate(ps)], open(f"{OUT}/index.json", "w"), indent=0)
print(len(ps), "products,", len(jobs), "images,", (len(ps) + PER - 1) // PER, "sheets")
