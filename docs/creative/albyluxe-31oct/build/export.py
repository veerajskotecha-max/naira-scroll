# Exports the approved frames at the live listing size (1288x1600 JPEG) after the house 1.5% inset crop, as
# ../../clover-garland/build/export.py does. frames.json maps each listing's handle to its ordered frame keys (out/<key>.png),
# variant by variant; the files go to ../exports/<handle>-NN.jpg in that order.
# Usage: python3 -I export.py [handle ...]   (no handle: every listing in frames.json)
import json, os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports"); os.makedirs(OUT, exist_ok=True)

def export(src, dst, inset=0.015):
    im = Image.open(src).convert("RGB"); w, h = im.size; dx, dy = round(w * inset), round(h * inset)
    im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS).save(dst, quality=92, optimize=True, progressive=True)

if __name__ == "__main__":
    F = json.load(open(os.path.join(H, "frames.json")))
    for handle in sys.argv[1:] or F:
        for i, key in enumerate(F[handle], 1):
            export(os.path.join(H, "out", f"{key}.png"), os.path.join(OUT, f"{handle}-{i:02d}.jpg"))
        print(handle, len(F[handle]), "exported")
