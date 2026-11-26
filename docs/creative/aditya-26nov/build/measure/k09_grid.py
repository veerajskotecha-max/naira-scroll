import sys
from PIL import Image, ImageDraw, ImageEnhance
im=Image.open('refs/K09_src.jpg').convert('RGB')
def grid(box, scale, step, name, major=100, enh=None, lw=1, alpha=True):
    c=im.crop(box)
    if enh: c=ImageEnhance.Contrast(c).enhance(enh)
    c=c.resize(((box[2]-box[0])*scale,(box[3]-box[1])*scale), Image.LANCZOS)
    d=ImageDraw.Draw(c)
    for x in range(((box[0]+step-1)//step)*step, box[2]+1, step):
        X=(x-box[0])*scale; d.line([(X,0),(X,c.size[1])], fill=(255,0,0) if x%major==0 else (0,255,255), width=lw)
        d.text((X+2,2), str(x), fill=(255,255,0)); d.text((X+2,c.size[1]-12), str(x), fill=(255,255,0))
    for y in range(((box[1]+step-1)//step)*step, box[3]+1, step):
        Y=(y-box[1])*scale; d.line([(0,Y),(c.size[0],Y)], fill=(255,0,0) if y%major==0 else (0,255,255), width=lw)
        d.text((2,Y+2), str(y), fill=(255,255,0)); d.text((c.size[0]-30,Y+2), str(y), fill=(255,255,0))
    c.save('build/measure/'+name)
if __name__=='__main__':
    b=tuple(int(v) for v in sys.argv[1].split(','))
    grid(b, int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], major=int(sys.argv[5]) if len(sys.argv)>5 else 100)
