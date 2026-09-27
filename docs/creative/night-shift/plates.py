"""cover-fit plate cutter: plates.cut(src, box, (w,h), out) — box is a fractional focus region; the crop is expanded to the target ratio around it."""
from PIL import Image
def cut(src,box,size,out,q=93):
    im=Image.open(src).convert("RGB"); W,H=im.size; tw,th=size; tr=tw/th
    x0,y0,x1,y1=W*box[0],H*box[1],W*box[2],H*box[3]; cw,ch=x1-x0,y1-y0; cx,cy=(x0+x1)/2,(y0+y1)/2
    if cw/ch<tr: cw=ch*tr
    else: ch=cw/tr
    cw=min(cw,W); ch=min(ch,H)
    if cw/ch<tr: ch=cw/tr
    else: cw=ch*tr
    x0=max(0,min(W-cw,cx-cw/2)); y0=max(0,min(H-ch,cy-ch/2))
    c=im.crop((int(x0),int(y0),int(x0+cw),int(y0+ch))).resize((tw,th),Image.LANCZOS); c.save(out,quality=q); return c
