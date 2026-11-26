# Exports the chosen frame of every listing photo at the live listing size (1288x1600 JPEG) after the house 1.5% inset
# crop (as ../../aditya-jewellery/build/export.py), as ../exports/<handle>-NN.jpg in ../shopify/listing.json order.
# chosen.json maps each listing slot (K01_W1 ...) to the frame that fills it: the take itself, its redo (…r) or a
# size-corrected retouch (…p, retouch.py). Usage: python3 -I export.py [handle ...]
import json, os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports"); os.makedirs(OUT, exist_ok=True)
INSET = 0.015
def export(src, dst):
    im = Image.open(src).convert("RGB"); w, h = im.size; dx, dy = round(w * INSET), round(h * INSET)
    im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS).save(dst, quality=92, optimize=True, progressive=True)
if __name__ == "__main__":
    L = json.load(open(f"{H}/../shopify/listing.json")); C = json.load(open(f"{H}/chosen.json")); only = set(sys.argv[1:])
    emap = json.load(open(f"{H}/export_map.json")) if os.path.exists(f"{H}/export_map.json") else {}
    for p in L:
        if only and p["handle"] not in only: continue
        done = []
        for n, (slot, _) in enumerate(p["images"], 1):        # a slot with no approved frame yet is skipped (shot later)
            if slot not in C or not os.path.exists(f"{H}/out/{C[slot]}.png"): continue
            fn = f"{p['handle']}-{n:02d}.jpg"; export(f"{H}/out/{C[slot]}.png", f"{OUT}/{fn}"); emap[slot] = fn; done.append(slot)
        print(p["sku"], p["handle"], len(done), "of", len(p["images"]), "exported", done)
    json.dump(emap, open(f"{H}/export_map.json", "w"), indent=1)
