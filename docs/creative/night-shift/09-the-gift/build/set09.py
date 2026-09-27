# -*- coding: utf-8 -*-
"""SET 09 — THE GIFT. The tag is the ad. Every card is the blush drawer box with one piece in it, and beneath it a
gift tag with TO and FROM already filled in — five relationships, five pieces, one honest price each."""
from core import *
SET=dict(slug="09-the-gift",title="The Gift",n=5)
S9=f"{ROOT}/s09"
TOK={"feed":dict(PLATE="770px",TAGH="290px",TO="58px",FROM="40px"),"story":dict(PLATE="1210px",TAGH="340px",TO="68px",FROM="46px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#e9d9cf}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.tagwrap{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 30px);height:var(--TAGH)}
.tag{position:absolute;left:0;right:0;top:0;bottom:0;border:1.5px solid var(--ink);clip-path:polygon(0 0,calc(100% - 34px) 0,100% 34px,100% 100%,0 100%);padding:22px 30px 22px 78px;display:flex;flex-direction:column;justify-content:center;background:rgba(242,196,189,.16)}
.tag:before{content:"";position:absolute;left:28px;top:calc(50% - 9px);width:18px;height:18px;border:1.5px solid var(--ink);border-radius:50%}
.tag .k{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.16em;text-transform:uppercase;color:var(--ac)}
.tag .to{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--TO);line-height:1.05;margin:4px 0 16px;text-wrap:pretty}
.tag .from{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--FROM);line-height:1.1;text-wrap:pretty}
.string{position:absolute;left:36px;top:calc(50% + 6px);width:1.5px;height:calc(var(--TAGH) * .55);background:var(--ink);transform:rotate(28deg);transform-origin:top}
.foot{grid-template-columns:1fr auto}
"""
def render(c,fmt):
    plate=f'{S9}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · THE GIFT",INK)}'
            f'<div class="tagwrap"><div class="tag"><div class="k">to</div><div class="to">{E(c["to"])}</div><div class="k">from</div><div class="from">{E(c["frm"])}</div></div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="G1",file="hoops",to="the sister who borrows everything.",frm="you, so she finally stops.",skus=["E20267O"],spec="BRAIDED HOOPS · 25MM · ONE PAIR · IN THE BOX",cta="GIFT THE HOOPS →",render=render,hero=True,claims=[("E20267O","25mm")]),
 dict(id="G2",file="chain",to="mum, who says she doesn't need anything.",frm="the one who knows better.",skus=["YF5143"],spec="4MM PAPERCLIP · 50CM · TOGGLE · IN THE BOX",cta="GIFT THE CHAIN →",render=render,hero=True,claims=[("YF5143","4mm · 50cm")]),
 dict(id="G3",file="prism",to="the friend who wears colour before noon.",frm="the one in black, with love.",skus=["B00681C"],spec="CUSHION CZ · 5MM · THREE COLOURS · IN THE BOX",cta="GIFT THE BRACELET →",render=render,hero=True,claims=[("B00681C","5mm")]),
 dict(id="G4",file="heart",to="you.",frm="you. nobody has to know.",skus=["YF5215"],spec="6MM STEEL SPHERES · GOLD HEART · IN THE BOX",cta="GIFT THE BRACELET →",render=render,hero=True,claims=[("YF5215","6mm")]),
 dict(id="G5",file="huggies",to="the one who “doesn’t wear jewellery.”",frm="someone who has seen the drawer.",skus=["E14776S"],spec="BRUSHED · 12MM · ONE PAIR · IN THE BOX",cta="GIFT THE HUGGIES →",render=render,hero=True,claims=[("E14776S","12mm")]),
]
