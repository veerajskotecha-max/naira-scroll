import sys, numpy as np
from PIL import Image
def lab(rgb):
    rgb=np.asarray(rgb,float)/255
    rgb=np.where(rgb>0.04045,((rgb+0.055)/1.055)**2.4,rgb/12.92)
    M=np.array([[0.4124,0.3576,0.1805],[0.2126,0.7152,0.0722],[0.0193,0.1192,0.9505]])
    xyz=rgb@M.T/np.array([0.95047,1,1.08883])
    f=np.where(xyz>0.008856,np.cbrt(xyz),7.787*xyz+16/116)
    return np.stack([116*f[...,1]-16,500*(f[...,0]-f[...,1]),200*(f[...,1]-f[...,2])],-1)
for f in sys.argv[1:]:
    im=np.asarray(Image.open(f).convert('RGB').resize((96,160))).astype(float)
    for name,reg in [('top',im[:40]),('bottom',im[-36:])]:
        med=np.median(reg.reshape(-1,3),axis=0); L,a,b=lab(med); C=np.hypot(a,b); h=(np.degrees(np.arctan2(b,a))+360)%360
        print(f"{f.split('/')[-1]:32s} {name:6s} L{L:5.1f} C{C:5.1f} h{h:5.1f} #{int(med[0]):02X}{int(med[1]):02X}{int(med[2]):02X}")
