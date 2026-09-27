# -*- coding: utf-8 -*-
"""SET 08 — THE MEASURE. Five figures from the listings, each photographed with the bench tool that takes it, each
printed on a ruler. The card is a reading, not a promise: size, width, stone, weight, drop."""
from core import *
SET=dict(slug="08-the-measure",title="The Measure",n=5)
S8=f"{ROOT}/s08"
TOK={"feed":dict(PLATE="790px",HEAD="132px",RULE="118px"),"story":dict(PLATE="1230px",HEAD="156px",RULE="140px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 24px)}
.lbl{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.14em;text-transform:uppercase;color:var(--ac)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;margin-top:6px}
.rule{display:block;width:100%;height:var(--RULE);margin-top:10px}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:8px;text-wrap:pretty;max-width:38ch}
.foot{grid-template-columns:1fr auto}
"""
def ruler(c,fmt):
    """SVG ruler: range (lo,hi) in units, ticks every 1, numbers every 5, markers at the values with the figure printed"""
    W=FORMATS[fmt][0]; pad=int(TOK.get(fmt,{}).get("pad","52px").replace("px","")) if False else (52 if fmt=="feed" else 64)
    w=W-2*pad; h=int(TOK[fmt]["RULE"].replace("px","")); lo,hi=c["range"]; unit=c["unit"]
    x=lambda v: (v-lo)/(hi-lo)*w
    base=h-36; out=[f'<line x1="0" y1="{base}" x2="{w}" y2="{base}" stroke="#1B1512" stroke-width="1.5"/>']
    v=lo
    while v<=hi+1e-9:
        major=abs(v/5-round(v/5))<1e-9; t=22 if major else 11
        out.append(f'<line x1="{x(v):.1f}" y1="{base}" x2="{x(v):.1f}" y2="{base-t}" stroke="#1B1512" stroke-width="{1.5 if major else 1}"/>')
        if major: out.append(f'<text x="{x(v):.1f}" y="{base+24}" text-anchor="middle" font-family="JetBrains Mono" font-size="13" letter-spacing="1" fill="#7A6E66">{int(v)}</text>')
        v+=1
    for val,label in c["marks"]:
        X=x(val)
        out.append(f'<line x1="{X:.1f}" y1="{base}" x2="{X:.1f}" y2="{base-46}" stroke="#6E1E2A" stroke-width="2.5"/>'
                   f'<polygon points="{X-7:.1f},{base-46} {X+7:.1f},{base-46} {X:.1f},{base-36}" fill="#6E1E2A"/>'
                   f'<text x="{X:.1f}" y="{base-56}" text-anchor="middle" font-family="Jost" font-weight="600" font-size="30" letter-spacing="0.5" fill="#6E1E2A">{E(label)}</text>')
    out.append(f'<text x="{w}" y="{base+24}" text-anchor="end" font-family="JetBrains Mono" font-size="13" letter-spacing="2" fill="#7A6E66">{E(unit)}</text>')
    return f'<svg class="rule" viewBox="0 0 {w} {h}">{"".join(out)}</svg>'
def render(c,fmt):
    plate=f'{S8}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · THE MEASURE",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="lbl">{E(c["lab"])}</div><div class="h">{c["head"]}</div>{ruler(c,fmt)}<div class="sub">{E(c["sub"])}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="M1",file="size",dark=True,lab="the size · inner diameter · us 7",head="THE SIZE.",range=(10,25),unit="MM",marks=[(17.3,"17.3")],
      sub="(fixed size, so the number is the whole story. seventeen point three, inside.)",skus=["JDR0303312-7"],spec="US 7 · 17.3MM INSIDE · 9.5MM AT THE CHEVRON · 18K",cta="SHOP THE RING →",render=render,claims=[("JDR0303312-7","17.3mm · US 7 · 9.5mm")]),
 dict(id="M2",file="width",dark=True,lab="the width · across the hoop",head="THE WIDTH.",range=(0,40),unit="MM",marks=[(25,"25")],
      sub="(twenty-five millimetres across. one pair, no stones, all braid.)",skus=["E20267O"],spec="BRAIDED HOOP · 25MM · ONE PAIR · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,hero=True,claims=[("E20267O","25mm")]),
 dict(id="M3",file="stone",lab="the stone · and its halo",head="THE STONE.",range=(0,20),unit="MM",marks=[(8,"8"),(12,"12")],
      sub="(an eight-millimetre stone inside a twelve-millimetre halo. the loupe is for you.)",skus=["WR10170K7"],spec="8MM ROUND · 12MM CUSHION HALO · US 7 · RHODIUM",cta="SHOP THE RING →",render=render,claims=[("WR10170K7","8mm · 12mm · US 7")]),
 dict(id="M4",file="weight",lab="the weight · on the bench scale",head="THE WEIGHT.",range=(0,20),unit="G",marks=[(12,"12")],
      sub="(twelve grams. enough to leave a mark in wax.)",skus=["YF5143"],spec="4MM PAPERCLIP · 50CM · 12G · 18K PVD",cta="SHOP THE CHAIN →",render=render,hero=True,claims=[("YF5143","4mm · 50cm · 12g")]),
 dict(id="M5",file="drop",lab="the drop · below the huggie",head="THE DROP.",range=(0,15),unit="MM",marks=[(8.5,"8.5"),(10.2,"10.2")],
      sub="(a clover on an eight-and-a-half-millimetre drop, on the paper that measures it.)",skus=["JDE0201327"],spec="HUGGIE 10.2MM · DROP 8.5MM · THREE PAIRS · 18K",cta="SHOP THE SET →",render=render,claims=[("JDE0201327","10.2mm · 8.5mm")]),
]
