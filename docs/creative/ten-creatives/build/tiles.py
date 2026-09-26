# square tile crops from the plinth photos. (sku, img index, cx, cy, size) as fractions of the source
import json,sys
from PIL import Image
SPEC={
 "YF5143":      (1, .50,.50,.58),   # Toggle Link Chain
 "B00681C":     (3, .50,.50,.80),   # Prism Riviere
 "E20267O":     (1, .50,.50,.80),   # Woven Gold Hoops
 "YF5215":      (5, .50,.48,.62),   # Heartbead
 "E14776S":     (0, .52,.46,.62),   # Brushed Gold Huggies
 "YF3925":      (0, .50,.52,.80),   # Baroque Shell
 "JDR0303312-7":(0, .50,.50,.72),   # Chevron Whisper
 "YF8453":      (2, .50,.50,.72),   # Halo Curve
 "YF3952":      (0, .50,.44,.62),   # Heartline Paperclip
 "E20997C":     (0, .50,.50,.72),   # Pearl Blossom
 "FR03136B":    (0, .50,.50,.72),   # Pearl Ribbon Ring
 "FE02847B":    (0, .50,.50,.72),   # Verdant Circlet
 "WR23569K8":   (1, .50,.50,.72),   # Vintage Halo
 "WE14387B":    (0, .50,.50,.72),   # Baguette Arc Hoops
 "YF5144":      (5, .50,.50,.80),   # Bold Nocturne Chain
 "JDR0104337-S":(0, .50,.50,.72),   # Pave Dome
 "WR12518B":    (0, .50,.50,.72),   # Petite Pave Band
 "E16075B":     (1, .50,.50,.72),   # Ribbon Bow
 "FE03586B":    (0, .50,.50,.72),   # Textured Gold Hoops
 "E16676C":     (1, .50,.50,.72),   # Trio Oval Drop
 "JDE0201327":  (1, .50,.50,.80),   # Clover Trio
 "YF8156":      (0, .50,.47,.62),   # Ribbon Bead
 "YF5214":      (2, .50,.50,.72),   # Star Point Band
 "WR10170K7":   (0, .50,.50,.72),   # Whisper Pave
 "YF8439-SLV":  (0, .50,.50,.80),   # Serpentine Silver
 "E19263B":     (0, .50,.50,.72),   # Pearl Point
 "YF8147":      (0, .50,.50,.72),   # Filigree Bloom
}
def tile(sku,out=800):
    i,cx,cy,s=SPEC[sku]
    im=Image.open(f"prod/{sku}_{i}.jpg").convert("RGB"); W,H=im.size
    side=int(min(W,H)*s); x0=int(cx*W-side/2); y0=int(cy*H-side/2)
    x0=max(0,min(W-side,x0)); y0=max(0,min(H-side,y0))
    t=im.crop((x0,y0,x0+side,y0+side)).resize((out,out),Image.LANCZOS)
    t.save(f"tiles/{sku}.jpg",quality=92); return t
if __name__=="__main__":
    from PIL import ImageDraw
    keys=list(SPEC); n=len(keys); cols=6; CW=300
    sheet=Image.new("RGB",(cols*(CW+6)+6,((n+cols-1)//cols)*(CW+24)+6),(241,235,225)); d=ImageDraw.Draw(sheet)
    for k,sku in enumerate(keys):
        t=tile(sku).resize((CW,CW)); x=6+(k%cols)*(CW+6); y=6+(k//cols)*(CW+24)
        sheet.paste(t,(x,y)); d.text((x+2,y+CW+4),sku,fill=(0,0,0))
    sheet.save("tiles_sheet.jpg",quality=82); print("tiles",n,sheet.size)
