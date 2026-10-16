# Labelled contact sheet: sheet.py OUT.jpg COLS CELL file...
import sys, os
from PIL import Image, ImageDraw
out, cols, cell, files = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4:]
rows = (len(files) + cols - 1) // cols
s = Image.new("RGB", (cols * cell, rows * (cell + 22)), "white"); d = ImageDraw.Draw(s)
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB"); im.thumbnail((cell - 6, cell - 6))
    x, y = (i % cols) * cell, (i // cols) * (cell + 22)
    s.paste(im, (x + 3, y + 3)); d.text((x + 4, y + cell + 4), os.path.basename(f)[:28], fill="black")
s.save(out, quality=88)
