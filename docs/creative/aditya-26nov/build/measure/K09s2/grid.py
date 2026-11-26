# usage: python3 -I grid.py x0 y0 x1 y1 zoom step out.png [enhance]
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
x0,y0,x1,y1,z,step=map(int,sys.argv[1:7]); out=sys.argv[7]
enh = len(sys.argv)>8 and sys.argv[8]=='e'
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
if enh:
    im=ImageEnhance.Contrast(im).enhance(1.6)
im=im.resize(((x1-x0)*z,(y1-y0)*z),Image.LANCZOS)
d=ImageDraw.Draw(im)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',max(10,min(14,z*5)))
except Exception: f=ImageFont.load_default()
for x in range((x0//step+1)*step, x1, step):
    X=(x-x0)*z; c=(255,0,0) if x%100==0 else (0,255,255)
    d.line([(X,0),(X,im.height)],fill=c,width=1)
    d.text((X+2,2),str(x),fill=c,font=f); d.text((X+2,im.height-16),str(x),fill=c,font=f)
for y in range((y0//step+1)*step, y1, step):
    Y=(y-y0)*z; c=(255,0,0) if y%100==0 else (0,255,255)
    d.line([(0,Y),(im.width,Y)],fill=c,width=1)
    d.text((2,Y+2),str(y),fill=c,font=f); d.text((im.width-40,Y+2),str(y),fill=c,font=f)
im.save(out); print(out, im.size)
