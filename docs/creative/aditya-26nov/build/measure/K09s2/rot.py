# rotated zoom: long axis horizontal. usage: rot.py cx cy angle half zoom out [contrast]
# frame: u to the right, v down, origin at (cx,cy); source = (cx + u cos a - v sin a, cy + u sin a + v cos a)
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
cx,cy,ang=float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]); half=int(sys.argv[4]); z=int(sys.argv[5]); out=sys.argv[6]
con=float(sys.argv[7]) if len(sys.argv)>7 else 1.0
im=Image.open(src).convert('RGB')
big=im.resize((1600*z,1600*z),Image.BICUBIC) if False else None
r=im.rotate(ang,resample=Image.BICUBIC,center=(cx,cy))
c=r.crop((int(cx-half),int(cy-half),int(cx+half),int(cy+half)))
if con!=1: c=ImageEnhance.Contrast(c).enhance(con)
c=c.resize((2*half*z,2*half*z),Image.LANCZOS)
M=40
can=Image.new('RGB',(c.width+2*M,c.height+2*M),(255,255,255)); can.paste(c,(M,M))
d=ImageDraw.Draw(can); f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
ox=M+(cx-int(cx-half))*z; oy=M+(cy-int(cy-half))*z
for u in range(-half//5*5,half+1,5):
    X=ox+u*z
    if M<=X<=M+c.width:
        L=12 if u%10==0 else 6
        d.line([(X,M-L),(X,M)],fill=(255,0,0)); d.line([(X,M+c.height),(X,M+c.height+L)],fill=(255,0,0))
        if u%10==0: d.text((X-8,4),str(u),fill=(0,0,0),font=f); d.text((X-8,M+c.height+16),str(u),fill=(0,0,0),font=f)
for v in range(-half//5*5,half+1,5):
    Y=oy+v*z
    if M<=Y<=M+c.height:
        L=12 if v%10==0 else 6
        d.line([(M-L,Y),(M,Y)],fill=(255,0,0)); d.line([(M+c.width,Y),(M+c.width+L,Y)],fill=(255,0,0))
        if v%10==0: d.text((2,Y-6),str(v),fill=(0,0,0),font=f); d.text((M+c.width+2,Y-6),str(v),fill=(0,0,0),font=f)
# faint crosshair through centre
d.line([(ox,M),(ox,M+c.height)],fill=(0,255,255)); d.line([(M,oy),(M+c.width,oy)],fill=(0,255,255))
can.save(out); print(out,can.size)
