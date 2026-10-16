# After a stone recolour: restore the original pixels wherever strongly coloured cloth or halo around a changed stone shifted hue.
import cv2, json, sys, numpy as np
cur, orig, spec, out = sys.argv[1:5]
a=cv2.imread(cur); o=cv2.imread(orig); S=json.load(open(spec))
hsv=cv2.cvtColor(a,cv2.COLOR_BGR2HSV).astype(np.float32); ho=cv2.cvtColor(o,cv2.COLOR_BGR2HSV).astype(np.float32)
dh=np.abs(((hsv[...,0]-ho[...,0]+90)%180)-90)
yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]; near=np.zeros(a.shape[:2],bool)
r0,r1=S.get("ring",[40,64])
for i,(cx,cy) in enumerate(S["stones"]):
    if S["cur"][i]!=S["tgt"][i]: near|=((xx-cx)**2+(yy-cy)**2<r1**2)&((xx-cx)**2+(yy-cy)**2>r0**2)
spill=near&(dh>20)&(ho[...,1]>45)
m=cv2.GaussianBlur(spill.astype(np.float32),(0,0),1.2)[...,None]
cv2.imwrite(out,(a*(1-m)+o*m).astype(np.uint8)); print("restored",int(spill.sum()))
