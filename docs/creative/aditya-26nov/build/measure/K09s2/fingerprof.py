# luminance profile across the ring finger in the 37 deg frame centred on the round stone (825,1098)
import math
from PIL import Image
im=Image.open('/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg').convert('L')
P=im.load(); cx,cy=825,1098; a=math.radians(37); ca,sa=math.cos(a),math.sin(a)
def L(u,v):
    x=cx+u*ca-v*sa; y=cy+u*sa+v*ca
    return P[int(round(x)),int(round(y))], (round(x),round(y))
for u0 in (-200,-160,-120,100,140,180,220):
    prof=[]
    for v in range(-230,231):
        s=0
        for du in range(-5,6): s+=L(u0+du,v)[0]
        prof.append((v,s/11))
    # minima in two windows
    up=min((p for p in prof if -200<=p[0]<=-110),key=lambda p:p[1])
    lo=min((p for p in prof if 60<=p[0]<=180),key=lambda p:p[1])
    print(f"u={u0:5d}  upper gap v={up[0]:5d} (lum {up[1]:.0f}) src {L(u0,up[0])[1]}   lower gap v={lo[0]:5d} (lum {lo[1]:.0f}) src {L(u0,lo[0])[1]}   width {lo[0]-up[0]} px")
