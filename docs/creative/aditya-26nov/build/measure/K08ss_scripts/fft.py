import numpy as np, sys, math
from PIL import Image
im=np.asarray(Image.open('/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K08_src.jpg').convert('L'),dtype=float)
def period(cx,cy,N=64):
    a=im[cy-N//2:cy+N//2, cx-N//2:cx+N//2].copy()
    # remove low-frequency by subtracting a box blur
    k=9
    from numpy.lib.stride_tricks import sliding_window_view
    pad=np.pad(a,k//2,mode='reflect'); blur=sliding_window_view(pad,(k,k)).mean(axis=(2,3))
    a=a-blur
    w=np.hanning(N); a=a*np.outer(w,w)
    F=np.abs(np.fft.fftshift(np.fft.fft2(a,s=(4*N,4*N))))**2
    M=4*N; yy,xx=np.mgrid[0:M,0:M]; fx=(xx-M//2)/M; fy=(yy-M//2)/M; fr=np.hypot(fx,fy)
    mask=(fr>1/13)&(fr<1/4.5)
    Fm=np.where(mask,F,0); i=np.unravel_index(np.argmax(Fm),F.shape)
    f=fr[i]; ang=math.degrees(math.atan2(fy[i],fx[i]))
    # radial profile peak sharpness
    bins=np.linspace(1/13,1/4.5,40); prof=[F[(fr>=bins[j])&(fr<bins[j+1])].mean() for j in range(len(bins)-1)]
    j=int(np.argmax(prof)); fpk=(bins[j]+bins[j+1])/2
    snr=max(prof)/np.median(prof)
    return 1/f, ang, 1/fpk, snr
pts=[tuple(map(int,s.split(','))) for s in sys.argv[1:]]
for (x,y) in pts:
    P,ang,Pr,snr=period(x,y)
    print('patch centre (%d,%d): peak period %.2f px (wavevector angle %.0f deg); radial-profile peak %.2f px; peak/median %.1f'%(x,y,P,ang,Pr,snr))
