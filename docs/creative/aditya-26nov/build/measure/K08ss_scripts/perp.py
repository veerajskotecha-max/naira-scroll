import sys, math, colorsys
from PIL import Image
im=Image.open('/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg').convert('RGB'); p=im.load()
def bil(x,y):
    x0=int(math.floor(x)); y0=int(math.floor(y)); fx=x-x0; fy=y-y0
    c=[0,0,0]
    for (xx,yy,w) in ((x0,y0,(1-fx)*(1-fy)),(x0+1,y0,fx*(1-fy)),(x0,y0+1,(1-fx)*fy),(x0+1,y0+1,fx*fy)):
        q=p[xx,yy]; 
        for i in range(3): c[i]+=q[i]*w
    return c
# args: cx cy dirx diry halflen  -> samples along the given direction through (cx,cy)
cx,cy,dx,dy,hl=map(float,sys.argv[1:6])
n=math.hypot(dx,dy); dx/=n; dy/=n
for k in range(-int(hl),int(hl)+1):
    x=cx+dx*k; y=cy+dy*k
    r,g,b=bil(x,y); h,s,v=colorsys.rgb_to_hsv(r/255,g/255,b/255)
    tag='GOLD' if (s>0.5 and 24<=h*360<=50) else ('stone' if s<0.2 and v>0.5 else '')
    print('%4d (%.1f,%.1f) rgb=(%3d,%3d,%3d) h=%3.0f s=%.2f v=%.2f %s'%(k,x,y,r,g,b,h*360,s,v,tag))
