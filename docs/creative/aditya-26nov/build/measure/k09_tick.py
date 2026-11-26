import sys
from PIL import Image, ImageDraw, ImageEnhance, ImageOps
im=Image.open('/home/user/naira-scroll/docs/creative/aditya-26nov/refs/K09_src.jpg').convert('RGB')
def tick(box, s, step, name, gray=False, enh=1.0, lines=False, minor=None):
    c=im.crop(box)
    if gray: c=ImageOps.autocontrast(c.convert('L'),cutoff=1).convert('RGB')
    if enh!=1.0: c=ImageEnhance.Contrast(c).enhance(enh)
    W,H=int(c.size[0]*s),int(c.size[1]*s)
    c=c.resize((W,H),Image.LANCZOS)
    d=ImageDraw.Draw(c)
    if minor:
        for x in range(((box[0]+minor-1)//minor)*minor, box[2]+1, minor):
            X=(x-box[0])*s; d.line([(X,0),(X,6)],fill=(0,255,255)); d.line([(X,H-6),(X,H)],fill=(0,255,255))
        for y in range(((box[1]+minor-1)//minor)*minor, box[3]+1, minor):
            Y=(y-box[1])*s; d.line([(0,Y),(6,Y)],fill=(0,255,255)); d.line([(W-6,Y),(W,Y)],fill=(0,255,255))
    for x in range(((box[0]+step-1)//step)*step, box[2]+1, step):
        X=(x-box[0])*s
        if lines: d.line([(X,0),(X,H)],fill=(255,0,0))
        d.line([(X,0),(X,14)],fill=(255,0,0),width=2); d.line([(X,H-14),(X,H)],fill=(255,0,0),width=2); d.text((X+3,3),str(x),fill=(255,255,0)); d.text((X+3,H-14),str(x),fill=(255,255,0))
    for y in range(((box[1]+step-1)//step)*step, box[3]+1, step):
        Y=(y-box[1])*s
        if lines: d.line([(0,Y),(W,Y)],fill=(255,0,0))
        d.line([(0,Y),(14,Y)],fill=(255,0,0),width=2); d.line([(W-14,Y),(W,Y)],fill=(255,0,0),width=2); d.text((16,Y-6),str(y),fill=(255,255,0)); d.text((W-44,Y-6),str(y),fill=(255,255,0))
    c.save('/home/user/naira-scroll/docs/creative/aditya-26nov/build/measure/'+name)
    return c.size
