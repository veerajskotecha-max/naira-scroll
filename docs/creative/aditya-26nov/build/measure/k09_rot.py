import math, sys
from PIL import Image, ImageDraw, ImageEnhance
SRC='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
OUT='/home/user/naira-scroll/docs/creative/aditya-26nov/build/measure/'
TH=33.5
C=(826,1070)
im=Image.open(SRC).convert('RGB')
rot=im.rotate(TH, resample=Image.BICUBIC, center=C)
th=math.radians(TH); U=(math.cos(th),math.sin(th)); N=(-math.sin(th),math.cos(th))
def to_orig(a,b): return (C[0]+a*U[0]+b*N[0], C[1]+a*U[1]+b*N[1])
def to_ab(x,y):
    dx,dy=x-C[0],y-C[1]; return (dx*U[0]+dy*U[1], dx*N[0]+dy*N[1])
def crop(a0,a1,b0,b1,s,step,name,lab=20,enh=1.0,img=None):
    img=img or rot
    c=img.crop((C[0]+a0,C[1]+b0,C[0]+a1,C[1]+b1))
    if enh!=1.0: c=ImageEnhance.Contrast(c).enhance(enh)
    W,H=(a1-a0)*s,(b1-b0)*s
    c=c.resize((W,H),Image.LANCZOS); d=ImageDraw.Draw(c)
    for a in range(((a0+step-1)//step)*step,a1+1,step):
        X=(a-a0)*s; col=(255,0,0) if a%lab==0 else (0,220,255)
        d.line([(X,0),(X,H)],fill=col)
        if a%lab==0: d.text((X+2,2),'a%d'%a,fill=(255,255,0)); d.text((X+2,H-12),'a%d'%a,fill=(255,255,0))
    for b in range(((b0+step-1)//step)*step,b1+1,step):
        Y=(b-b0)*s; col=(255,0,0) if b%lab==0 else (0,220,255)
        d.line([(0,Y),(W,Y)],fill=col)
        if b%lab==0: d.text((2,Y+2),'b%d'%b,fill=(255,255,0)); d.text((W-40,Y+2),'b%d'%b,fill=(255,255,0))
    c.save(OUT+name); return c.size
if __name__=='__main__':
    a0,a1,b0,b1,s,step=[int(v) for v in sys.argv[1:7]]
    print(crop(a0,a1,b0,b1,s,step,sys.argv[7], lab=int(sys.argv[8]) if len(sys.argv)>8 else 20))
