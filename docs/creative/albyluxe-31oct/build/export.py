# Exports the approved frames at the live listing size (1288x1600 JPEG) after the house 1.5% inset crop, as
# ../../clover-garland/build/export.py does. frames.json maps each listing id to {variant name: [frame keys]} (out/<key>.png);
# the files go to ../exports/<handle>-NN.jpg, variant by variant in that order, the handle made from the listing's title.
# Usage: python3 -I export.py [id ...]   (no id: every listing in frames.json)
import json, os, re, sys, unicodedata
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports"); os.makedirs(OUT, exist_ok=True)

def export(src, dst, inset=0.015):
    im = Image.open(src).convert("RGB"); w, h = im.size; dx, dy = round(w * inset), round(h * inset)
    im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS).save(dst, quality=92, optimize=True, progressive=True)

def handle(title):
    t = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower(); return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

if __name__ == "__main__":
    F = json.load(open(os.path.join(H, "frames.json"))); T = {x["id"]: x["title"] for x in json.load(open(os.path.join(H, "listings.json")))}
    for i in sys.argv[1:] or F:
        keys = [k for ks in F[i].values() for k in ks]; h = handle(T[i])
        for n, key in enumerate(keys, 1):
            export(os.path.join(H, "out", f"{key}.png"), os.path.join(OUT, f"{h}-{n:02d}.jpg"))
        print(i, h, len(keys), "exported")
