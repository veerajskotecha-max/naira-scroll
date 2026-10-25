# Exports approved shots to the live listing size (1288x1600 JPEG) as exports/<handle>-NN.jpg in listing.json order.
# Every frame gets a 1.5% inset crop first: some worn frames carry a thin white "paper edge" down the sides.
# Heroes that were reshot export from their approved take: A5_H2 and A9_H2, and A6_Hc (A6_H2 with the royal-blue correction from colour.py).
# The Bougainvillea photos export from the 25 Oct size fix (retouch.py): A8_Hs, A8_W1s, A8_W2s, A8_Ms, A9_Hs (made from
# A9_H2), A9_W1s and A9_Ms.
# Usage: export.py [handle ...] (no handles: every product)
import json, os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports")
SRC = {"A5_H": "A5_H2", "A6_H": "A6_Hc",
       "A8_H": "A8_Hs", "A8_W1": "A8_W1s", "A8_W2": "A8_W2s", "A8_M": "A8_Ms", "A9_H": "A9_Hs", "A9_W1": "A9_W1s", "A9_M": "A9_Ms"}
INSET = 0.015
def export(key, dst):
    im = Image.open(f"{H}/out/{SRC.get(key, key)}.png").convert("RGB"); w, h = im.size
    dx, dy = round(w * INSET), round(h * INSET)
    im = im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS)
    im.save(dst, quality=92, optimize=True, progressive=True)
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True); only = set(sys.argv[1:])
    L = json.load(open(f"{H}/../shopify/listing.json")); A = json.load(open(f"{H}/approved.json"))
    emap = json.load(open(f"{H}/export_map.json")) if only else {}; missing = []
    for p in L:
        if only and p["handle"] not in only: continue
        for n, (k, _) in enumerate(p["images"], 1):
            if k not in A: missing.append(k); continue
            fn = f"{p['handle']}-{n:02d}.jpg"; export(k, f"{OUT}/{fn}"); emap[k] = fn
    json.dump(emap, open(f"{H}/export_map.json", "w"), indent=1)
    print(len(emap), "exported; missing:", missing)
