# -*- coding: utf-8 -*-
"""SET 06 — ON EVERY SKIN. One chain, five complexions. The headline on each card is the hex colour sampled from
that woman's collarbone in the picture; the strip beneath shows all five samples with the five crops, the current one marked.
Nothing is named, nothing is graded: the swatch is the data, the chain is the constant."""
from core import *
from PIL import Image
import plates
SET=dict(slug="06-on-every-skin",title="On Every Skin",n=5)
S6=f"{ROOT}/s06"
SKU="YF5143"
TOK={"feed":dict(PLATE="740px",HEAD="150px",TH="118px",SW="20px"),"story":dict(PLATE="1190px",HEAD="176px",TH="150px",SW="26px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 22px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.01em;text-transform:uppercase;white-space:nowrap}
.h .hash{font-family:'Jost';font-weight:400;font-size:.62em;vertical-align:.12em;margin-right:.04em;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:4px;text-wrap:pretty}
.strip{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:18px}
.cell{position:relative;padding:5px}
.cell img{width:100%;height:var(--TH);object-fit:cover;display:block;filter:saturate(.95)}
.cell i{display:block;height:var(--SW);margin-top:6px}
.cell span{display:block;font-family:'JetBrains Mono';font-size:calc(var(--MONO)*.92);letter-spacing:.08em;margin-top:6px;color:var(--mute)}
.cell.cur{outline:1.5px solid var(--ink);outline-offset:0}
.cell.cur span{color:var(--ac);font-weight:600}
.foot{grid-template-columns:1fr auto}
.pc{display:flex;align-items:center;gap:22px}
.pc .cta{margin-top:0}
"""
def sample(path,box):
    im=Image.open(path).convert("RGB"); W,H=im.size
    c=im.crop((int(W*box[0]),int(H*box[1]),int(W*box[2]),int(H*box[3]))).resize((1,1),Image.BOX).getpixel((0,0))
    return "#%02X%02X%02X"%c
def prep():
    """cut plates + thumbs + sample swatches from the five renders (s06/skin_{k}.png)"""
    for c in CREATIVES:
        src=f'{S6}/skin_{c["file"]}.png'
        plates.cut(src,c.get("box_feed",(0.0,0.15,1.0,0.85)),(1080,770),f'{S6}/plate_{c["file"]}_feed.jpg')
        plates.cut(src,c.get("box_story",(0.04,0.04,0.96,0.96)),(1080,1250),f'{S6}/plate_{c["file"]}_story.jpg')
        plates.cut(src,c.get("tbox",(0.25,0.32,0.75,0.72)),(320,320),f'{S6}/th_{c["file"]}.jpg')
        c["hex"]=sample(src,c.get("sbox",(0.06,0.62,0.20,0.80)))
    return [(c["id"],c["hex"]) for c in CREATIVES]
def hexes():
    out={}
    for c in CREATIVES:
        p=f'{S6}/skin_{c["file"]}.png'
        try: out[c["id"]]=sample(p,c.get("sbox",(0.06,0.62,0.20,0.80)))
        except FileNotFoundError: out[c["id"]]="#000000"
    return out
def render(c,fmt):
    HX=hexes(); plate=f'{S6}/plate_{c["file"]}_{fmt}.jpg'
    cells="".join(f'<div class="cell{" cur" if k["id"]==c["id"] else ""}"><img src="{S6}/th_{k["file"]}.jpg"><i style="background:{HX[k["id"]]}"></i><span>{HX[k["id"]]}</span></div>' for k in CREATIVES)
    hx=HX[c["id"]][1:]
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · ON EVERY SKIN",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="h"><span class="hash">#</span>{hx}.</div><div class="sub">{E(c["sub"])}</div><div class="strip">{cells}</div></div>'
            f'<div class="foot"><div><div class="name">{name(SKU)}</div><div class="spec">4MM · 50CM · TOGGLE 15MM · 18K PVD</div></div>'
            f'<div class="pc"><span class="price">{price(SKU)}</span><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="S1",file="one",box_feed=(0.0,0.38,1.0,0.78),box_story=(0.04,0.12,0.96,0.98),tbox=(0.27,0.54,0.67,0.86),sbox=(0.30,0.78,0.44,0.88),sub="(sampled at her collarbone. the same chain on all five.)",dark=True,logo="logo_ink.png",skus=[SKU],hero=True,render=render,cta="SHOP THE CHAIN →",claims=[(SKU,"4mm · 50cm · 15mm")]),
 dict(id="S2",file="two",box_feed=(0.0,0.35,1.0,0.75),box_story=(0.04,0.12,0.96,0.98),tbox=(0.35,0.50,0.75,0.82),sbox=(0.30,0.78,0.44,0.88),sub="(the swatch is her. the gold is 18k pvd on every card.)",skus=[SKU],hero=True,render=render,cta="SHOP THE CHAIN →",claims=[(SKU,"4mm · 50cm · 15mm")]),
 dict(id="S3",file="three",box_feed=(0.0,0.32,1.0,0.72),box_story=(0.04,0.10,0.96,0.96),tbox=(0.35,0.46,0.75,0.78),sbox=(0.30,0.76,0.44,0.86),sub="(one of five. we printed her number, not a name.)",skus=[SKU],hero=True,render=render,cta="SHOP THE CHAIN →",claims=[(SKU,"4mm · 50cm · 15mm")]),
 dict(id="S4",file="four",box_feed=(0.0,0.43,1.0,0.83),box_story=(0.10,0.25,0.90,1.0),tbox=(0.30,0.58,0.70,0.90),sbox=(0.14,0.62,0.26,0.74),sub="(sampled, not named. five colours, one chain.)",skus=[SKU],hero=True,render=render,cta="SHOP THE CHAIN →",claims=[(SKU,"4mm · 50cm · 15mm")]),
 dict(id="S5",file="five",box_feed=(0.0,0.28,1.0,0.68),box_story=(0.04,0.06,0.96,0.94),tbox=(0.34,0.46,0.74,0.78),sbox=(0.30,0.78,0.44,0.88),sub="(five of us, one chain. only the number changes.)",dark=True,logo="logo_ink.png",skus=[SKU],hero=True,render=render,cta="SHOP THE CHAIN →",claims=[(SKU,"4mm · 50cm · 15mm")]),
]
