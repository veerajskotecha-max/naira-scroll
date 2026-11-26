# zoomed crop with ticks only on the margins (no grid over the piece)
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
x0,y0,x1,y1,z,step=map(int,sys.argv[1:7]); out=sys.argv[7]
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
if len(sys.argv)>8: im=ImageEnhance.Contrast(im).enhance(float(sys.argv[8]))
im=im.resize(((x1-x0)*z,(y1-y0)*z),Image.LANCZOS)
M=40
c=Image.new('RGB',(im.width+2*M,im.height+2*M),(255,255,255)); c.paste(im,(M,M))
d=ImageDraw.Draw(c); f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
for x in range((x0//step+1)*step,x1,step):
    X=M+(x-x0)*z
    d.line([(X,M-10),(X,M)],fill=(255,0,0),width=1); d.line([(X,M+im.height),(X,M+im.height+10)],fill=(255,0,0))
    d.text((X-10,5),str(x),fill=(0,0,0),font=f); d.text((X-10,M+im.height+14),str(x),fill=(0,0,0),font=f)
for y in range((y0//step+1)*step,y1,step):
    Y=M+(y-y0)*z
    d.line([(M-10,Y),(M,Y)],fill=(255,0,0)); d.line([(M+im.width,Y),(M+im.width+10,Y)],fill=(255,0,0))
    d.text((2,Y-6),str(y),fill=(0,0,0),font=f); d.text((M+im.width+2,Y-6),str(y),fill=(0,0,0),font=f)
c.save(out); print(out,c.size)
