# Review sheet: one row per product, its listing images in order, labelled with SKU and title -> board.jpg
import json, os
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(f"{H}/../shopify/listing.json")); E = json.load(open(f"{H}/export_map.json"))
TW, TH, LAB = 322, 400, 30
F = ImageFont.truetype(os.path.join(H, "../../aditya-bracelets/build/fonts/Jost-500.ttf"), 20)
rows = [(p, [E[k] for k, _ in p["images"]]) for p in L]
cols = max(len(r[1]) for r in rows)
pairs = [rows[i:i + 2] for i in range(0, len(rows), 2)]
sheet = Image.new("RGB", (2 * cols * TW + 20, len(pairs) * (TH + LAB)), (244, 235, 226)); d = ImageDraw.Draw(sheet)
for r, pr in enumerate(pairs):
    for c, (p, files) in enumerate(pr):
        x0, y0 = c * (cols * TW + 20), r * (TH + LAB)
        d.text((x0 + 6, y0 + 5), f"{p['sku']}  {p['title']}", font=F, fill=(28, 23, 18))
        for i, fn in enumerate(files):
            im = Image.open(f"{H}/../exports/{fn}").convert("RGB").resize((TW - 4, TH - 4))
            sheet.paste(im, (x0 + i * TW, y0 + LAB))
sheet.save(f"{H}/../board.jpg", quality=86); print(sheet.size)
