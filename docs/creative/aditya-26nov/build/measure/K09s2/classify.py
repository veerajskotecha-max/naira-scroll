# class map: stone (low sat, bright) = white, gold (hue 30-55deg, sat high, val high) = yellow, dark = blue, skin = gray
import sys
from PIL import Image, ImageDraw, ImageFont
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
x0,y0,x1,y1,z=map(int,sys.argv[1:6]); out=sys.argv[6]
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
hsv=im.convert('HSV')
W,H=im.size
o=Image.new('RGB',(W,H))
P=im.load(); Q=hsv.load(); O=o.load()
for y in range(H):
    for x in range(W):
        h,s,v=Q[x,y]; r,g,b=P[x,y]
        hd=h*360/255
        if s<70 and v>150: O[x,y]=(255,255,255)
        elif 28<=hd<=60 and s>=110 and v>=120: O[x,y]=(255,200,0)
        elif v<80: O[x,y]=(0,0,160)
        else: O[x,y]=(110,110,110)
o=o.resize((W*z,H*z),Image.NEAREST)
d=ImageDraw.Draw(o)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12)
step=10
for x in range((x0//step+1)*step,x1,step):
    X=(x-x0)*z; c=(255,0,0) if x%50==0 else (0,180,180)
    d.line([(X,0),(X,o.height)],fill=c); 
    if x%20==0: d.text((X+2,2),str(x),fill=(255,0,0),font=f)
for y in range((y0//step+1)*step,y1,step):
    Y=(y-y0)*z; c=(255,0,0) if y%50==0 else (0,180,180)
    d.line([(0,Y),(o.width,Y)],fill=c)
    if y%20==0: d.text((2,Y+2),str(y),fill=(255,0,0),font=f)
o.save(out); print(out,o.size)
