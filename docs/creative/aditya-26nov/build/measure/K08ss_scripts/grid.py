import sys
from PIL import Image, ImageDraw, ImageFont
src, out, x0, y0, x1, y1, scale, step = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:9])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
W, H = im.size
im = im.resize((W*scale, H*scale), Image.LANCZOS)
d = ImageDraw.Draw(im)
try:
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
except Exception:
    f = ImageFont.load_default()
for x in range((x0//step+1)*step, x1, step):
    X = (x-x0)*scale
    major = x % (step*5) == 0
    d.line([(X,0),(X,H*scale)], fill=(255,0,0) if major else (255,255,0), width=1)
    d.text((X+2, 2), str(x), fill=(255,0,0), font=f)
    d.text((X+2, H*scale-14), str(x), fill=(255,0,0), font=f)
for y in range((y0//step+1)*step, y1, step):
    Y = (y-y0)*scale
    major = y % (step*5) == 0
    d.line([(0,Y),(W*scale,Y)], fill=(255,0,0) if major else (0,255,255), width=1)
    d.text((2, Y+2), str(y), fill=(0,0,255), font=f)
    d.text((W*scale-30, Y+2), str(y), fill=(0,0,255), font=f)
im.save(out)
print(out, im.size)
