import sys, math
from PIL import Image
im=Image.open('/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg').convert('L')
p=im.load()
def bil(x,y):
    x0=int(math.floor(x)); y0=int(math.floor(y)); fx=x-x0; fy=y-y0
    return (p[x0,y0]*(1-fx)*(1-fy)+p[x0+1,y0]*fx*(1-fy)+p[x0,y0+1]*(1-fx)*fy+p[x0+1,y0+1]*fx*fy)
def profile(x0,y0,x1,y1,halfw=3):
    L=math.hypot(x1-x0,y1-y0); n=int(L)
    ux,uy=(x1-x0)/L,(y1-y0)/L; nx,ny=-uy,ux
    out=[]
    for i in range(n):
        s=0
        for k in range(-halfw,halfw+1):
            s+=bil(x0+ux*i+nx*k,y0+uy*i+ny*k)
        out.append(s/(2*halfw+1))
    return out
def detrend(a,w=15):
    o=[]
    for i in range(len(a)):
        lo=max(0,i-w); hi=min(len(a),i+w+1); o.append(a[i]-sum(a[lo:hi])/(hi-lo))
    return o
def acorr(a,maxlag=20):
    m=sum(a)/len(a); a=[x-m for x in a]; d=sum(x*x for x in a)
    return [sum(a[i]*a[i+l] for i in range(len(a)-l))/d for l in range(maxlag+1)]
def peaks(a):
    return [i for i in range(1,len(a)-1) if a[i]>a[i-1] and a[i]>=a[i+1] and a[i]>0]
for line in [tuple(map(float,s.split(','))) for s in sys.argv[1:]]:
    pr=detrend(profile(*line))
    ac=acorr(pr,25)
    pk=peaks(pr)
    # first acorr peak after lag 3
    best=max(range(4,25),key=lambda l:ac[l])
    # refine parabolic
    l=best; 
    if 1<=l<len(ac)-1:
        den=ac[l-1]-2*ac[l]+ac[l+1]; off=0.5*(ac[l-1]-ac[l+1])/den if den!=0 else 0
    else: off=0
    gaps=[b-a for a,b in zip(pk,pk[1:])]
    print('line',line,'len',len(pr),'acorr peak lag %.2f (r=%.2f)'%(l+off,ac[l]),'npeaks',len(pk),'mean gap %.2f'%((pk[-1]-pk[0])/(len(pk)-1)) if len(pk)>1 else '', 'gaps',gaps)
