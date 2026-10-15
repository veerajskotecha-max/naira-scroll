# Crop a plate to remove a face edge, keeping the frame's aspect ratio (4:5 or 9:16) and the most pixels possible.
# Usage: recrop.py <in.png> <out.png> <aspect w:h> <x0> <y0> [x1 y1]  -- (x0,y0) is the top-left limit that must be excluded
# beyond (face above y0 or left of x0); the crop is the largest box of the given aspect inside [x0,x1]x[y0,y1].
import sys
from PIL import Image
src, dst, ar = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src); W, H = im.size
x0, y0 = int(sys.argv[4]), int(sys.argv[5])
x1 = int(sys.argv[6]) if len(sys.argv) > 6 else W
y1 = int(sys.argv[7]) if len(sys.argv) > 7 else H
aw, ah = map(int, ar.split(":"))
bw, bh = x1 - x0, y1 - y0
if bw / bh > aw / ah:   # box too wide: full height, trim width around the centre
    h = bh; w = int(h * aw / ah); cx = x0 + (bw - w) // 2; box = (cx, y0, cx + w, y0 + h)
else:                   # box too tall: full width, keep the top (y0 is the face line) and trim the bottom
    w = bw; h = int(w * ah / aw); box = (x0, y0, x0 + w, y0 + h)
c = im.crop(box); c.save(dst); print(dst, box, c.size)
