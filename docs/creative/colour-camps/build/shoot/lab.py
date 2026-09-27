import numpy as np
M=np.array([[0.4124,0.3576,0.1805],[0.2126,0.7152,0.0722],[0.0193,0.1192,0.9505]]); Mi=np.linalg.inv(M); WP=np.array([0.95047,1,1.08883])
def rgb2lab(rgb):
    r=np.where(rgb>0.04045,((rgb+0.055)/1.055)**2.4,rgb/12.92)
    xyz=r@M.T/WP; f=np.where(xyz>0.008856,np.cbrt(xyz),7.787*xyz+16/116)
    return np.stack([116*f[...,1]-16,500*(f[...,0]-f[...,1]),200*(f[...,1]-f[...,2])],-1)
def lab2rgb(lab):
    fy=(lab[...,0]+16)/116; fx=fy+lab[...,1]/500; fz=fy-lab[...,2]/200
    f=np.stack([fx,fy,fz],-1); xyz=np.where(f**3>0.008856,f**3,(f-16/116)/7.787)*WP
    r=xyz@Mi.T; r=np.clip(r,0,1)
    return np.where(r>0.0031308,1.055*r**(1/2.4)-0.055,12.92*r)
