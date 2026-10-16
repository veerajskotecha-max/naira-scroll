# Desaturates leftover stone-colour fringes on the silver halo around each recoloured stone (a colour that is not the new stone's).
import cv2, json, sys, numpy as np
cur, spec, out = sys.argv[1:4]; S=json.load(open(spec)); a=cv2.imread(cur)
hsv=cv2.cvtColor(a,cv2.COLOR_BGR2HSV).astype(np.float32); H,Sa=hsv[...,0],hsv[...,1]
yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]; half=S.get("half",38)
band={"A":(H>78)&(H<110),"P":(H>150)|(H<8),"Y":(H>14)&(H<40)}
m=np.zeros(a.shape[:2],bool)
for i,(cx,cy) in enumerate(S["stones"]):
    t=S["tgt"][i]
    if S["cur"][i]==t: continue
    r=np.sqrt((xx-cx)**2+(yy-cy)**2); ring=(r>half*0.92)&(r<half*S.get("fr_out",1.52))
    for c in S.get("fringe","AP"):
        if c!=t: m|=ring&band[c]&(Sa>30)
mm=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.0)
hsv[...,1]=Sa*(1-0.85*mm)
cv2.imwrite(out,cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR)); print("fringe px",int(m.sum()))
