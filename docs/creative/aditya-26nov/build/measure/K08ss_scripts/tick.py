import sys
from PIL import Image, ImageDraw
src, out, x0, y0, x1, y1, z, step = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:9])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
im = im.resize(((x1-x0)*z, (y1-y0)*z), Image.BICUBIC)
M=40
can = Image.new('RGB',(im.width+2*M, im.height+2*M),(255,255,255))
can.paste(im,(M,M))
d = ImageDraw.Draw(can)
for x in range((x0//step+1)*step, x1, step):
    X = (x-x0)*z+M
    L = 12 if x%(step*2)==0 else 6
    d.line([(X,M-L),(X,M)],fill=(0,0,0)); d.line([(X,M+im.height),(X,M+im.height+L)],fill=(0,0,0))
    if x%(step*2)==0:
        d.text((X-8,2),str(x),fill=(200,0,0)); d.text((X-8,M+im.height+14),str(x),fill=(200,0,0))
for y in range((y0//step+1)*step, y1, step):
    Y = (y-y0)*z+M
    L = 12 if y%(step*2)==0 else 6
    d.line([(M-L,Y),(M,Y)],fill=(0,0,0)); d.line([(M+im.width,Y),(M+im.width+L,Y)],fill=(0,0,0))
    if y%(step*2)==0:
        d.text((2,Y-5),str(y),fill=(0,0,200)); d.text((M+im.width+14,Y-5),str(y),fill=(0,0,200))
can.save(out)
