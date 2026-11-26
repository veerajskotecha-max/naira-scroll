import math
from PIL import Image, ImageDraw
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg'
im=Image.open(src).convert('RGB')
def rp(cx,cy,ang,u,v):
    t=math.radians(ang); return (cx+u*math.cos(t)-v*math.sin(t), cy+u*math.sin(t)+v*math.cos(t))
S1=(837,757,30.2); S2=(783,866,35.6)
M={}
M['s1_rim_w']=(rp(*S1,-23.5,0),rp(*S1,17.5,0))
M['s1_stone_w']=(rp(*S1,-21,1.5),rp(*S1,16,1.5))
M['s1_unit']=(rp(*S1,-2,-45),rp(*S1,-2,45.5))
M['s1_pale']=(rp(*S1,-6,-36.5),rp(*S1,-6,18.5))
M['s2_rim_w']=(rp(*S2,-19.5,-4),rp(*S2,18.5,-4))
M['s2_unit']=(rp(*S2,-5,-46),rp(*S2,0,39))
M['s2_pale']=(rp(*S2,6,-18),rp(*S2,6,33))
M['gap']=(rp(*S1,-2,45.5),rp(*S2,-5,-46))
M['finger_inner']=((866,674.6),(745,928.5))
M['band_outer']=((871,662),(742,940))
M['band_w_top']=((859.2,688.2),(876.1,692.9))
M['band_w_bot']=((740.9,920.3),(752.6,928.1))
M['centres']=(rp(*S1,-3,-2),rp(*S2,0,-4))
M['face_span']=(rp(*S1,-2,-45),rp(*S2,0,39))
for k,(a,b) in M.items():
    print('%-13s (%.1f,%.1f) -> (%.1f,%.1f)  %.1f px'%(k,a[0],a[1],b[0],b[1],math.dist(a,b)))
x0,y0,x1,y1=700,640,900,960; z=4
c=im.crop((x0,y0,x1,y1)).resize(((x1-x0)*z,(y1-y0)*z),Image.BICUBIC)
d=ImageDraw.Draw(c)
cols={'s1_rim_w':(0,255,255),'s1_stone_w':(255,0,255),'s1_unit':(0,255,0),'s2_rim_w':(0,255,255),'s2_unit':(0,255,0),'gap':(255,255,0),'finger_inner':(255,80,80),'band_outer':(80,80,255),'band_w_top':(255,0,255),'band_w_bot':(255,0,255)}
for k,(a,b) in M.items():
    if k not in cols: continue
    A=((a[0]-x0)*z,(a[1]-y0)*z); B=((b[0]-x0)*z,(b[1]-y0)*z)
    d.line([A,B],fill=cols[k],width=2)
    for P in (A,B): d.ellipse([P[0]-4,P[1]-4,P[0]+4,P[1]+4],outline=cols[k],width=2)
    d.text((B[0]+6,B[1]-6),k,fill=cols[k])
c.save('K08ss_annot4.png')
