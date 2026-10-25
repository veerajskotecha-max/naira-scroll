# Exports approved shots to the live listing size (1288x1600 JPEG) as exports/<handle>-NN.jpg in listing.json order.
# Every frame gets a 1.5% inset crop first, as in aditya-bracelets: some worn frames carry a thin paper edge down the sides.
# Frames that were reshot or edited export from their approved take: the full J09 hero is J09_H2 and the first, closer
# J09 hero becomes the detail image (J09_D). The 25 Oct reshoot at true size (the heart and pear sets 30% smaller) and the
# zigzag fix export from their own takes: J05_Hf, J05_W1e2, J06_He, J06_W1e2, J14_Hn, J14_W1z, J14_Mn, J16_Hg1, J16_W1r2,
# J17_Hs and J17_W1h2. The 25 Oct sizing check brought seven worn photos to the listed size (retouch.py): the pinched
# J01_W1p, J03_W1p, J05_W1p, J07_W1p, J08_W1p and J11_W1qp (the ear cuff on the rim), and J02_W1c (a Higgsfield blend
# of the cut-and-scaled earring). The owner kept the 25 Oct takes for the twin heart studs (J06_W1e2, over the swapped
# J06_W1s) and the prism pair (J16_W1r2 and J17_W1h2, over the cut-and-scaled J16_W1d and J17_W1d).
# The watch link piece is a rigid bangle (the owner's KAVNAR photo, 25 Oct): J10_Hb, J10_W2c and J10_Mc replace the strap frames.
import json, os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "../exports")
SRC = {"J09_H": "J09_H2", "J09_D": "J09_H", "J05_H": "J05_Hf", "J06_H": "J06_He", "J06_W1": "J06_W1e2",
       "J14_H": "J14_Hn", "J14_W1": "J14_W1z", "J14_M": "J14_Mn", "J16_H": "J16_Hg1", "J16_W1": "J16_W1r2",
       "J17_H": "J17_Hs", "J17_W1": "J17_W1h2", "J01_W1": "J01_W1p", "J02_W1": "J02_W1c", "J03_W1": "J03_W1p",
       "J05_W1": "J05_W1p", "J07_W1": "J07_W1p", "J08_W1": "J08_W1p", "J11_W1": "J11_W1qp",
       "J10_H": "J10_Hb", "J10_W1": "J10_W2c", "J10_M": "J10_Mc"}
INSET = 0.015
def export(key, dst):
    im = Image.open(f"{H}/out/{SRC.get(key, key)}.png").convert("RGB"); w, h = im.size
    dx, dy = round(w * INSET), round(h * INSET)
    im = im.crop((dx, dy, w - dx, h - dy)).resize((1288, 1600), Image.LANCZOS)
    im.save(dst, quality=92, optimize=True, progressive=True)
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True); only = set(sys.argv[1:])   # optional handles: export just those products
    L = json.load(open(f"{H}/../shopify/listing.json")); A = json.load(open(f"{H}/approved.json"))
    missing = []
    emap = json.load(open(f"{H}/export_map.json")) if only else {}
    for p in L:
        if only and p["handle"] not in only: continue
        for n, (k, _) in enumerate(p["images"], 1):
            if k not in A: missing.append(k); continue
            fn = f"{p['handle']}-{n:02d}.jpg"; export(k, f"{OUT}/{fn}"); emap[k] = fn
    json.dump(emap, open(f"{H}/export_map.json", "w"), indent=1)
    print(len(emap), "exported; missing:", missing)
