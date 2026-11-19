# Contact sheet for a batch review: python3 -I sheet.py out.jpg a.jpg b.jpg ...  (labels are the file names)
import os, sys
from PIL import Image, ImageDraw, ImageFont
out, files = sys.argv[1], sys.argv[2:]
W, H, G = 540, 675, 16
F = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Medium.otf", 20)
cols = min(5, len(files)); rows = -(-len(files) // cols)
sheet = Image.new("RGB", (cols * (W + G) + G, rows * (H + 44 + G) + G), "white"); d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    x, y = G + (i % cols) * (W + G), G + (i // cols) * (H + 44 + G)
    im = Image.open(f).convert("RGB"); im.thumbnail((W, H)); sheet.paste(im, (x, y))
    d.text((x, y + H + 10), os.path.basename(f), fill="black", font=F)
sheet.save(out, quality=88); print(out, sheet.size)
