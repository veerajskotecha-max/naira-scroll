import sys, math
from PIL import Image, ImageDraw, ImageFont
src,out=sys.argv[1],sys.argv[2]
cx,cy,ang,half,scale=float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7])
im=Image.open(src).convert('RGB')
# rotate counterclockwise by ang around (cx,cy): a vector at ang deg clockwise from vertical becomes vertical
r=im.rotate(ang,resample=Image.BICUBIC,center=(cx,cy))
c=r.crop((int(cx-half),int(cy-half),int(cx+half),int(cy+half)))
c=c.resize((c.width*scale,c.height*scale),Image.LANCZOS)
d=ImageDraw.Draw(c); f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',11)
for v in range(-half,half+1,5):
    X=(v+half)*scale
    col=(255,0,0) if v%25==0 else (255,255,0)
    d.line([(X,0),(X,c.height)],fill=col); d.text((X+2,2),str(v),fill=(255,0,0),font=f)
    d.line([(0,X),(c.width,X)],fill=(255,0,0) if v%25==0 else (0,255,255)); d.text((2,X+1),str(v),fill=(0,0,255),font=f)
c.save(out)
# map rotated-frame (u,v) back to original: inverse rotate
def back(u,v):
    a=math.radians(ang)
    # PIL rotate ccw by a: original point p -> rotated point. inverse: rotate cw
    x=cx+u*math.cos(a)-v*math.sin(a); y=cy+u*math.sin(a)+v*math.cos(a)
    return round(x,1),round(y,1)
print(out, 'u,v grid units = original px; (0,0)=',(cx,cy))
for uv in [(0,-40),(0,40),(-20,0),(20,0)]:
    print(uv,'->',back(*uv))
