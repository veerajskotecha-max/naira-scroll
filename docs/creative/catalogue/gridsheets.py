# Annotation sheets: every on-model photo (main "w" and second "a") with a 10% grid, so the piece's box can be read off.
import json, sys, os
from PIL import Image, ImageDraw, ImageFont
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
rows = json.load(open(f"{SRC}/products_pick.json"))
items = []
for r in rows:
    if r["worn"]: items.append((f"{r['n']}w", f"{SRC}/full/{r['handle']}-worn.jpg", r["title"]))
    if r.get("alt"): items.append((f"{r['n']}a", f"{SRC}/full/{r['handle']}-alt.jpg", r["title"]))
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16); f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
W, PER, COLS = 300, 15, 5
for s in range(0, len(items), PER):
    chunk = items[s:s + PER]; cells = []
    for key, path, title in chunk:
        im = Image.open(path).convert("RGB"); h = round(W * im.height / im.width); im = im.resize((W, h), Image.LANCZOS)
        d = ImageDraw.Draw(im)
        for i in range(1, 10):
            x = round(W * i / 10); y = round(h * i / 10)
            d.line([(x, 0), (x, h)], fill=(0, 255, 255), width=1); d.line([(0, y), (W, y)], fill=(0, 255, 255), width=1)
            d.text((x + 2, 2), str(i), fill=(255, 255, 0), font=f2); d.text((2, y + 1), str(i), fill=(255, 255, 0), font=f2)
        cells.append((key, title, im))
    rowsn = (len(cells) + COLS - 1) // COLS; ch = max(c[2].height for c in cells) + 24
    sheet = Image.new("RGB", (COLS * (W + 8), rowsn * ch), "white"); d = ImageDraw.Draw(sheet)
    for i, (key, title, im) in enumerate(cells):
        x = (i % COLS) * (W + 8); y = (i // COLS) * ch
        d.text((x + 2, y + 2), f"{key} {title[:24]}", fill="black", font=F); sheet.paste(im, (x, y + 22))
    sheet.save(f"{OUT}/grid_{s // PER + 1:02d}.jpg", quality=82)
print(len(items), "photos on", (len(items) + PER - 1) // PER, "sheets")
