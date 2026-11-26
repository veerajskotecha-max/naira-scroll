import sys, math, colorsys
from PIL import Image
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg'
cx,cy,ang=map(float,sys.argv[1:4]); u0=int(sys.argv[4]) if len(sys.argv)>4 else 0
im=Image.open(src).convert('RGB')
r=im.rotate(ang,resample=Image.BICUBIC,center=(cx,cy)); p=r.load()
th=math.radians(ang)
def orig(u,v): return cx+u*math.cos(th)-v*math.sin(th), cy+u*math.sin(th)+v*math.cos(th)
def isskin(u,v):
    R,G,B=p[int(round(cx+u)),int(round(cy+v))]
    h,s,vv=colorsys.rgb_to_hsv(R/255,G/255,B/255); h*=360
    return (h<=25 and s>=0.30)
for v in range(-50,51,2):
    if isskin(u0,v):
        print('%4d skin at centre'%v); continue
    l=u0
    while l>-40 and not isskin(l-1,v): l-=1
    rr=u0
    while rr<40 and not isskin(rr+1,v): rr+=1
    s=''.join('.' if isskin(u,v) else '#' for u in range(-30,31))
    lo=orig(l,v); ro=orig(rr,v)
    print('%4d %s  L=%3d R=%3d W=%2d   Lorig=(%.0f,%.0f) Rorig=(%.0f,%.0f)'%(v,s,l,rr,rr-l+1,*lo,*ro))
