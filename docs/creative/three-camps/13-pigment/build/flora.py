# -*- coding: utf-8 -*-
"""flora — the brand's floral graphics as overlay helpers: six vector rose petals (from the site's HeroPetals), the painted
bloom, the watercolour sprig, the line vine, the flat brand-flower silhouette, the pattern tile and the embroidery."""
import json, re, random, base64, os
ROOT=os.path.dirname(os.path.abspath(__file__)); FL=f"{ROOT}/floral"
_P=json.load(open(f"{ROOT}/petals.json")); PAL=_P["palettes"]; PET=_P["petals"]
ASSET={k:f"{FL}/{v}" for k,v in dict(bloom="bloom.png",sprig="sprig.png",vine="vine.png",flower="brandflower.png",pattern="pattern.png",wallpaper="wallpaper.png",embroidery="embroidery.jpg").items()}
def uri(path):
    mime="image/png" if path.endswith(".png") else "image/jpeg"
    return f"data:{mime};base64,"+base64.b64encode(open(path,"rb").read()).decode()
_uid=[0]
def petal(variant=0,colours=None,size=80,rot=0,opacity=1.0,shadow=True,style=""):
    """one petal as inline SVG. variant 0..5 (3 is a full rosette built from variant 0). colours: dict c1,c2,c3,vein or a palette index."""
    _uid[0]+=1; u=_uid[0]
    if colours is None: colours=dict(zip(["c1","c2","c3","vein"],PAL[0]))
    elif isinstance(colours,int): colours=dict(zip(["c1","c2","c3","vein"],PAL[colours]))
    if variant==3:  # rosette of five variant-0 petals
        inner="".join(f'<g transform="rotate({d} 20 20) translate(2 -2) scale(0.5)">{_body(0,colours,u*10+i)}</g>' for i,d in enumerate([0,72,144,216,288]))
        vb="0 0 40 40"; w=size; h=size
    else:
        p=PET[variant]; vb=p["viewBox"]; vw,vh=[float(x) for x in vb.split()[2:]]; w=size; h=size*vh/vw; inner=_body(variant,colours,u)
    sh="filter:drop-shadow(0 6px 10px rgba(27,21,18,.22));" if shadow else ""
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="{vb}" fill="none" style="position:absolute;transform:rotate({rot}deg);opacity:{opacity};{sh}{style}">{inner}</svg>'
def _body(variant,colours,u):
    b=PET[variant]["body"]
    for k,v in colours.items(): b=b.replace("@@"+k+"@@",v)
    b=re.sub(r'id="__(\w+)__"',lambda m:f'id="{m.group(1)}{u}"',b)
    b=re.sub(r'url\(#__(\w+)__\)',lambda m:f'url(#{m.group(1)}{u})',b)
    return b
def scatter(n,box,seed=1,sizes=(60,140),colours=0,variants=(0,1,2,4,5),opacity=(0.85,1.0),shadow=True):
    """n petals scattered in box=(x0,y0,x1,y1) px; returns html of absolutely positioned petals"""
    rnd=random.Random(seed); out=[]
    for i in range(n):
        s=rnd.uniform(*sizes); x=rnd.uniform(box[0],box[2]-s); y=rnd.uniform(box[1],box[3]-s); r=rnd.uniform(0,360); v=rnd.choice(variants)
        c=colours if not isinstance(colours,(list,tuple)) else rnd.choice(colours)
        out.append(petal(v,c,s,r,rnd.uniform(*opacity),shadow,style=f"left:{x:.0f}px;top:{y:.0f}px;"))
    return "".join(out)
def img(name,style=""):
    return f'<img src="{uri(ASSET[name])}" style="position:absolute;{style}" alt="">'
def flower_mask_css(): return f"-webkit-mask-image:url({uri(ASSET['flower'])});mask-image:url({uri(ASSET['flower'])});-webkit-mask-size:contain;mask-size:contain;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-position:center;mask-position:center;"
def tint(hexcol): return {"c1":"#ffffff","c2":hexcol,"c3":hexcol,"vein":hexcol}
def mix(a,b,t):
    a=a.lstrip('#'); b=b.lstrip('#'); return '#%02x%02x%02x'%tuple(int(int(a[i:i+2],16)*(1-t)+int(b[i:i+2],16)*t) for i in (0,2,4))
def tint_from(hexcol):
    """petal gradient built from one plate colour: light centre to the colour itself, darker vein"""
    return {"c1":mix(hexcol,"#ffffff",0.75),"c2":mix(hexcol,"#ffffff",0.35),"c3":hexcol,"vein":mix(hexcol,"#1B1512",0.35)}
