"""grade.py <in.png> <out.png> [target_h] [strength] — HSL-secondary style grade for sage plates:
pulls the hue of low-chroma green background pixels (h 90-185, C 3-30) toward the brand sage hue; product colours
(gold h<85 or C>30, silver C<3, skin h<75, emerald C>30) are untouched. Smooth weights, no hard edges."""
import sys, numpy as np
from PIL import Image
from lab import rgb2lab, lab2rgb
src,dst=sys.argv[1],sys.argv[2]; T=float(sys.argv[3]) if len(sys.argv)>3 else 165.0; S=float(sys.argv[4]) if len(sys.argv)>4 else 0.75
PROT=sys.argv[5] if len(sys.argv)>5 else None
im=Image.open(src); a=np.asarray(im.convert('RGB')).astype(np.float64)/255
lab=rgb2lab(a); L,A,B=lab[...,0],lab[...,1],lab[...,2]
C=np.hypot(A,B); h=(np.degrees(np.arctan2(B,A))+360)%360
def ss(x,e0,e1): t=np.clip((x-e0)/(e1-e0),0,1); return t*t*(3-2*t)
w=ss(h,88,102)*(1-ss(h,178,192))*ss(C,2.5,5)*(1-ss(C,24,32))
if PROT:   # never touch the product: zero the weight wherever the background-removed cut-out has the piece
    from PIL import ImageFilter
    pa=Image.open(PROT).convert('RGBA').split()[3].resize(im.size).filter(ImageFilter.MaxFilter(5))
    w=w*(1-np.asarray(pa).astype(float)/255)
nh=h+(T-h)*S*w
lab2=np.stack([L,C*np.cos(np.radians(nh)),C*np.sin(np.radians(nh))],-1)
out=np.clip(lab2rgb(lab2),0,1)
Image.fromarray((out*255+0.5).astype(np.uint8)).save(dst); print(dst, 'weighted px %.1f%%'%(100*(w>0.5).mean()))
