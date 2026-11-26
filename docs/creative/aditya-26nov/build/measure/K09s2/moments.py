import math, json
from PIL import Image, ImageDraw, ImageFilter
src='/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg'
im=Image.open(src).convert('RGB'); hsv=im.convert('HSV')
P=im.load(); Q=hsv.load()
ROIS={
 'marquise':[(838,948),(858,930),(930,936),(975,965),(975,998),(950,1004),(900,1003),(870,992),(845,985)],
 'baguette':[(826,1022),(845,994),(870,998),(930,1040),(915,1060),(900,1092),(880,1090),(860,1070),(840,1045)],
 'round':[(775,1090),(790,1058),(815,1046),(845,1050),(870,1075),(880,1100),(870,1130),(840,1150),(800,1148),(778,1125)],
 'oval':[(690,1150),(705,1130),(740,1118),(770,1125),(800,1160),(812,1195),(800,1215),(770,1235),(740,1232),(710,1200)],
}
def stone(x,y):
    h,s,v=Q[x,y]
    return s<75 and v>140
res={}
for name,poly in ROIS.items():
    xs=[p[0] for p in poly]; ys=[p[1] for p in poly]
    x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
    m=Image.new('L',(1600,1600),0); ImageDraw.Draw(m).polygon(poly,fill=255)
    M=m.load()
    mask=Image.new('L',(1600,1600),0); K=mask.load()
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            if M[x,y] and stone(x,y): K[x,y]=255
    # close holes: dilate then erode
    mask=mask.filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.MinFilter(7))
    # restrict to roi again
    K=mask.load()
    pts=[(x,y) for y in range(y0,y1+1) for x in range(x0,x1+1) if K[x,y] and M[x,y]]
    n=len(pts); cx=sum(p[0] for p in pts)/n; cy=sum(p[1] for p in pts)/n
    sxx=sum((p[0]-cx)**2 for p in pts)/n; syy=sum((p[1]-cy)**2 for p in pts)/n; sxy=sum((p[0]-cx)*(p[1]-cy) for p in pts)/n
    th=0.5*math.atan2(2*sxy,sxx-syy)
    l1=(sxx+syy)/2+math.sqrt(((sxx-syy)/2)**2+sxy**2); l2=(sxx+syy)/2-math.sqrt(((sxx-syy)/2)**2+sxy**2)
    ux,uy=math.cos(th),math.sin(th)
    a=[(p[0]-cx)*ux+(p[1]-cy)*uy for p in pts]; b=[-(p[0]-cx)*uy+(p[1]-cy)*ux for p in pts]
    res[name]=dict(n=n,cx=round(cx,1),cy=round(cy,1),angle_deg=round(math.degrees(th),1),
      major_extent=round(max(a)-min(a),1),minor_extent=round(max(b)-min(b),1),
      ellipse_major=round(4*math.sqrt(l1),1),ellipse_minor=round(4*math.sqrt(l2),1),
      rect_major=round(math.sqrt(12*l1),1),rect_minor=round(math.sqrt(12*l2),1),area=n)
    # save mask view
    vis=im.crop((x0-10,y0-10,x1+10,y1+10)).copy(); V=vis.load()
    for (x,y) in pts:
        r,g,bb=V[x-x0+10,y-y0+10]; V[x-x0+10,y-y0+10]=(min(255,r//2+120),g//2,bb//2)
    d=ImageDraw.Draw(vis)
    L=max(a);Lm=min(a);Wd=max(b);Wm=min(b)
    def P2(s,t): return (cx+s*ux-t*uy-x0+10, cy+s*uy+t*ux-y0+10)
    d.line([P2(Lm,0),P2(L,0)],fill=(0,255,0)); d.line([P2(0,Wm),P2(0,Wd)],fill=(0,255,255))
    d.polygon([P2(Lm,Wm),P2(L,Wm),P2(L,Wd),P2(Lm,Wd)],outline=(255,255,0))
    vis.resize((vis.width*4,vis.height*4),Image.NEAREST).save(f'mask_{name}.png')
print(json.dumps(res,indent=1))
json.dump(res,open('moments.json','w'),indent=1)
