# Review grid: grid.py OUT.jpg KEY... -> each row = supplier ref | approved hero | KEY image (macro/worn), labelled.
import sys, os, json
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); S = json.load(open(f"{H}/skus.json"))
out, keys = sys.argv[1], sys.argv[2:]; h = 420; rows = []
for k in keys:
    base = k.rsplit("_", 1)[0]; ref = S[base]["ref"] if base in S else "C_src"
    files = [f"{H}/refs/{ref}.jpg", f"{H}/out/{base}_H.png", f"{H}/out/{k}.png"]
    ims = [Image.open(f).convert("RGB") for f in files if os.path.exists(f)]
    ims = [i.resize((int(i.width * h / i.height), h)) for i in ims]
    r = Image.new("RGB", (sum(i.width for i in ims) + 8 * len(ims), h + 26), "white"); x = 0
    for i in ims: r.paste(i, (x, 26)); x += i.width + 8
    ImageDraw.Draw(r).text((4, 6), k, fill="black"); rows.append(r)
W = max(r.width for r in rows); s = Image.new("RGB", (W, sum(r.height for r in rows)), "white"); y = 0
for r in rows: s.paste(r, (0, y)); y += r.height
s.thumbnail((2000, 3000)); s.save(out, quality=86)
