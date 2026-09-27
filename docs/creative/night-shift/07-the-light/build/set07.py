# -*- coding: utf-8 -*-
"""SET 07 — THE LIGHT. Festive without a discount. Every jewellery brand runs Diwali on a countdown and a code; this set
runs it on a single diya. Dark ground, one flame, the offer block every festive ad carries — filled in honestly with NONE."""
from core import *
SET=dict(slug="07-the-light",title="The Light",n=5)
S7=f"{ROOT}/s07"
TOK={"feed":dict(PLATE="880px",HEAD="150px",FORM="17px"),"story":dict(PLATE="1320px",HEAD="176px",FORM="20px")}
CSS="""
.ad{background:var(--bg);color:var(--ink)}
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#150608}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.plate:after{content:"";position:absolute;left:0;right:0;bottom:0;height:140px;background:linear-gradient(180deg,rgba(42,13,20,0),var(--bg))}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) - 40px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap}
.h em{font-style:normal;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:6px;text-wrap:pretty;max-width:34ch}
.form{display:grid;grid-template-columns:auto 1fr auto;gap:9px 14px;margin-top:22px;font-family:'JetBrains Mono';font-size:var(--FORM);letter-spacing:.1em;text-transform:uppercase;max-width:560px}
.form .k{color:rgba(241,235,225,.55)}
.form .dots{border-bottom:1px dotted rgba(241,235,225,.35);transform:translateY(-5px)}
.form .v{text-align:right}
.form .v.ac{color:var(--ac)}
.foot{grid-template-columns:1fr auto}
.cta.solid{background:var(--ac);border-color:var(--ac);color:var(--bg)}
"""
def render(c,fmt):
    plate=f'{S7}/plate_{c["file"]}_{fmt}.jpg'
    rows=[("offer","none",False),("code","none",False),("ends","never",False),("light",c["light"],True)]
    form="".join(f'<span class="k">{E(k)}</span><span class="dots"></span><span class="v{" ac" if a else ""}">{E(v)}</span>' for k,v,a in rows)
    sku=c["skus"][0]
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · THE LIGHT",IVORY,logo="logo_ivory.png")}'
            f'<div class="block"><div class="h">{c["head"]}</div><div class="sub">{E(c["sub"])}</div><div class="form">{form}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
COMMON=dict(render=render,ink=IVORY,bg=WINE,ac=BLUSH,hero=True)
CREATIVES=[
 dict(id="F1",file="chain",head="NO <em>CODE.</em>",sub="(the light is the offer. this diwali, and after it.)",light="one diya",skus=["YF5143"],spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM · 18K PVD",cta="SHOP THE CHAIN →",claims=[("YF5143","4mm · 50cm · 15mm")],**COMMON),
 dict(id="F2",file="hoops",head="NO <em>TIMER.</em>",sub="(nothing here ends at midnight. we lit a lamp instead.)",light="one diya",skus=["E20267O"],spec="BRAIDED HOOP · 25MM · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("E20267O","25mm")],**COMMON),
 dict(id="F3",file="prism",head="NO <em>SALE.</em>",sub="(it costs what it costs. the stones do the celebrating.)",light="one diya",skus=["B00681C"],spec="CUSHION CZ · 5MM · RHODIUM PLATED",cta="SHOP THE BRACELET →",claims=[("B00681C","5mm")],**COMMON),
 dict(id="F4",file="heart",head="NO <em>RUSH.</em>",sub="(diwali is not a deadline. the heart is not a hint.)",light="one diya",skus=["YF5215"],spec="STEEL SPHERES · 6MM · 18K GOLD TONE CLASP",cta="SHOP THE BRACELET →",claims=[("YF5215","6mm")],**COMMON),
 dict(id="F5",file="huggies",head="NO <em>CATCH.</em>",sub="(one lamp, one pair, one price. that is the whole offer.)",light="one diya",skus=["E14776S"],spec="BRUSHED SATIN · 12MM · 6MM DEEP · 18K",cta="SHOP THE HUGGIES →",claims=[("E14776S","12mm · 6mm")],**COMMON),
]
