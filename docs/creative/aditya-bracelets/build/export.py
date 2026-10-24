# Exports approved shots to the live listing size (1288x1600 JPEG) as exports/<handle>-NN.jpg in listing.json order.
# Every frame gets a 1.5% inset crop first: some worn frames carry a thin white "paper edge" down the sides.
# Heroes that were reshot export from their approved take: A5_H2 and A9_H2, and A6_Hc (A6_H2 with the royal-blue correction from colour.py).
import json, os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports")
SRC = {"A5_H": "A5_H2", "A6_H": "A6_Hc", "A9_H": "A9_H2"}
INSET = 0.015
def export(key, dst):
    im = Image.open(f"{H}/out/{SRC.get(key, key)}.png").convert("RGB"); w, h = im.size
    dx, dy = round(w * INSET), round(h * INSET)
    im = im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS)
    im.save(dst, quality=92, optimize=True, progressive=True)
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    L = json.load(open(f"{H}/../shopify/listing.json")); A = json.load(open(f"{H}/approved.json"))
    emap, missing = {}, []
    for p in L:
        for n, (k, _) in enumerate(p["images"], 1):
            if k not in A: missing.append(k); continue
            fn = f"{p['handle']}-{n:02d}.jpg"; export(k, f"{OUT}/{fn}"); emap[k] = fn
    json.dump(emap, open(f"{H}/export_map.json", "w"), indent=1)
    print(len(emap), "exported; missing:", missing)
