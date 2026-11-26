import sys, math, colorsys
from PIL import Image
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg'
cx,cy,ang=map(float,sys.argv[1:4]); mode=sys.argv[4]; fixed=float(sys.argv[5]); a,b=int(sys.argv[6]),int(sys.argv[7])
im=Image.open(src).convert('RGB')
r=im.rotate(ang,resample=Image.BICUBIC,center=(cx,cy)); p=r.load()
# map rotated (u,v) back to original coords for reporting
th=math.radians(ang)
def orig(u,v):
    # PIL rotate CCW by ang: rotated pixel at (cx+u,cy+v) came from original at rotation by -ang (in image coords, y down)
    x=cx+u*math.cos(th)-v*math.sin(th); y=cy+u*math.sin(th)+v*math.cos(th)
    return x,y
for k in range(a,b+1):
    u,v=(k,fixed) if mode=='row' else (fixed,k)
    R,G,B=p[int(round(cx+u)),int(round(cy+v))]
    h,s,vv=colorsys.rgb_to_hsv(R/255,G/255,B/255)
    ox,oy=orig(u,v)
    print('%s=%4d  rgb=(%3d,%3d,%3d) h=%3.0f s=%.2f v=%.2f  orig=(%.0f,%.0f) %s'%('u' if mode=='row' else 'v',k,R,G,B,h*360,s,vv,ox,oy,'#'*int(s*30)))
