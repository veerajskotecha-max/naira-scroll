import sys, math
sys.path.insert(0,'/home/user/naira-scroll/docs/creative/aditya-26nov/build/measure')
import k09_rot as R
from PIL import Image, ImageFilter, ImageDraw
rot=R.rot
def segment(a0,a1,b0,b1,smax=85,vmin=100,close=5,openk=3,name=None):
    box=(R.C[0]+a0,R.C[1]+b0,R.C[0]+a1,R.C[1]+b1)
    hsv=rot.crop(box).convert('HSV'); px=hsv.load(); W,H=hsv.size
    m=Image.new('L',(W,H),0); mp=m.load()
    for y in range(H):
        for x in range(W):
            h,s,v=px[x,y]
            if s<smax and v>vmin: mp[x,y]=255
    if close: m=m.filter(ImageFilter.MaxFilter(close)).filter(ImageFilter.MinFilter(close))
    # fill holes: pad with a 0 border, floodfill from corner
    pad=Image.new('L',(W+2,H+2),0); pad.paste(m,(1,1)); ImageDraw.floodfill(pad,(0,0),128)
    pp=pad.load(); out=Image.new('L',(W,H),0); op=out.load()
    for y in range(H):
        for x in range(W):
            op[x,y]=0 if pp[x+1,y+1]==128 else 255
    if openk: out=out.filter(ImageFilter.MinFilter(openk)).filter(ImageFilter.MaxFilter(openk))
    if name: out.save('/home/user/naira-scroll/docs/creative/aditya-26nov/build/measure/'+name)
    lp=out.load(); seen=set(); res=[]
    for y in range(H):
        for x in range(W):
            if lp[x,y]==255 and (x,y) not in seen:
                st=[(x,y)]; seen.add((x,y)); pts=[]
                while st:
                    p=st.pop(); pts.append(p)
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        q=(p[0]+dx,p[1]+dy)
                        if 0<=q[0]<W and 0<=q[1]<H and q not in seen and lp[q]==255:
                            seen.add(q); st.append(q)
                if len(pts)>600:
                    A=[p[0]+a0 for p in pts]; B=[p[1]+b0 for p in pts]
                    n=len(pts); ma=sum(A)/n; mb=sum(B)/n
                    saa=sum((a-ma)**2 for a in A)/n; sbb=sum((b-mb)**2 for b in B)/n; sab=sum((a-ma)*(b-mb) for a,b in zip(A,B))/n
                    tr=saa+sbb; det=saa*sbb-sab*sab; d=math.sqrt(max(tr*tr/4-det,0)); l1=tr/2+d; l2=tr/2-d
                    ang=0.5*math.degrees(math.atan2(2*sab,saa-sbb))
                    xo,yo=R.to_orig(ma,mb)
                    res.append(dict(area=n,ca=ma,cb=mb,orig=(round(xo),round(yo)),a=(min(A),max(A)),b=(min(B),max(B)),ell=(4*math.sqrt(l1),4*math.sqrt(l2)),rect=(math.sqrt(12*l1),math.sqrt(12*l2)),ang=ang))
    return res
if __name__=='__main__':
    for r in segment(*[int(v) for v in sys.argv[1:5]], name=sys.argv[5] if len(sys.argv)>5 else None):
        print('area %(area)5d centre a%(ca).0f b%(cb).0f orig%(orig)s a%(a)s b%(b)s ell %(ell)s rect %(rect)s ang %(ang).1f'%r)
