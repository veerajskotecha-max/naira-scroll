# Exports approved shots to the live listing size (1288x1600 JPEG) as exports/<handle>-NN.jpg in listing.json order.
# Every frame gets a 1.5% inset crop first, as in aditya-bracelets: some worn frames carry a thin paper edge down the sides.
# Frames that were reshot or edited export from their approved take: the full J09 hero is J09_H2 and the first, closer
# J09 hero becomes the detail image (J09_D). The 25 Oct reshoot at true size (the heart and pear sets 30% smaller) and the
# zigzag fix export from their own takes: J05_Hf, J05_W1e2, J06_He, J06_W1e2, J14_Hn, J14_W1z, J14_Mn, J16_Hg1, J16_W1r2,
# J17_Hs and J17_W1h2.
import json, os
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports")
SRC = {"J09_H": "J09_H2", "J09_D": "J09_H", "J05_H": "J05_Hf", "J05_W1": "J05_W1e2", "J06_H": "J06_He", "J06_W1": "J06_W1e2",
       "J14_H": "J14_Hn", "J14_W1": "J14_W1z", "J14_M": "J14_Mn", "J16_H": "J16_Hg1", "J16_W1": "J16_W1r2",
       "J17_H": "J17_Hs", "J17_W1": "J17_W1h2"}
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
