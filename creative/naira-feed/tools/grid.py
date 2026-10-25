# Usage: python3 grid.py out.png img1 img2 ... (newest first = top-left, Instagram order)
# Builds the profile-grid view: 3 columns, each tile centre-cropped to 3:4 like the 2025 grid,
# 2px gutters, at phone width 1170 (iPhone 3x) so it can be read at real thumbnail size too.
import sys
from PIL import Image, ImageDraw
out, files = sys.argv[1], sys.argv[2:]
W = 1170; gap = 3; cols = 3
tw = (W - gap * (cols - 1)) // cols; th = round(tw * 4 / 3)
rows = (len(files) + cols - 1) // cols
canvas = Image.new('RGB', (W, rows * th + (rows - 1) * gap), (255, 255, 255))
for i, f in enumerate(files):
    im = Image.open(f).convert('RGB')
    w, h = im.size
    target = 3 / 4
    if w / h > target:  # too wide -> crop sides
        nw = round(h * target); x0 = (w - nw) // 2; im = im.crop((x0, 0, x0 + nw, h))
    else:
        nh = round(w / target); y0 = (h - nh) // 2; im = im.crop((0, y0, w, y0 + nh))
    im = im.resize((tw, th), Image.LANCZOS)
    r, c = divmod(i, cols)
    canvas.paste(im, (c * (tw + gap), r * (th + gap)))
canvas.save(out, quality=92)
small = canvas.resize((390, round(canvas.height * 390 / W)), Image.LANCZOS)
small.save(out.replace('.png', '-phone1x.png'))
print(out, canvas.size)
