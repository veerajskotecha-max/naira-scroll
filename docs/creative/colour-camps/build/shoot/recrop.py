"""recrop.py <plate> <x0> <y0> <x1> <y1> [ax ay] — keep the box (fractions), then trim to 4:5 around anchor (fractions of the box, default .5 .5).
Writes <stem>c.png. Refuses if the result is narrower than 1080px."""
import sys
from PIL import Image
p=sys.argv[1]; x0,y0,x1,y1=map(float,sys.argv[2:6]); ax,ay=(map(float,sys.argv[6:8]) if len(sys.argv)>7 else (.5,.5))
im=Image.open(p); W,H=im.size
L,T,R,B=int(W*x0),int(H*y0),int(W*x1),int(H*y1); w,h=R-L,B-T
if w/h>0.8:
    nw=int(h*0.8); cx=L+int(w*ax); L=min(max(L,cx-nw//2),R-nw); R=L+nw
else:
    nh=int(w/0.8); cy=T+int(h*ay); T=min(max(T,cy-nh//2),B-nh); B=T+nh
out=im.crop((L,T,R,B)); fn=p[:-4]+'c.png'
assert out.width>=1080, out.size
out.save(fn); print(fn,out.size)
