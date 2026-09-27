# -*- coding: utf-8 -*-
"""SET 10 — THE ANSWER. Improvised from what the first nine taught: the cards that work are the ones where the device is the
truth. So the last set is five real questions people ask before they buy, answered in one word, with the listing quoted as
evidence. Three of the answers are NO. That is the brand."""
from core import *
SET=dict(slug="10-the-answer",title="The Answer",n=5)
S10=f"{ROOT}/s10"
TOK={"feed":dict(PLATE="720px",ANS="210px",Q="42px",EV="17px"),"story":dict(PLATE="1170px",ANS="250px",Q="50px",EV="20px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 26px)}
.q{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--Q);line-height:1.1}
.q b{font-family:'JetBrains Mono';font-style:normal;font-weight:400;font-size:var(--MONO);letter-spacing:.14em;color:var(--ac);margin-right:14px;vertical-align:.35em}
.a{font-family:'Velista';font-weight:500;font-size:var(--ANS);line-height:.88;letter-spacing:-.005em;text-transform:uppercase;white-space:nowrap;margin-top:6px}
.a em{font-style:normal;color:var(--ac)}
.ev{display:grid;grid-template-columns:auto 1fr;gap:12px;margin-top:16px;font-family:'JetBrains Mono';font-size:var(--EV);letter-spacing:.04em;line-height:1.45;max-width:62ch}
.ev b{font-weight:400;color:var(--ac);letter-spacing:.14em;text-transform:uppercase;font-size:var(--MONO)}
.ev i{font-family:'Cormorant Garamond';font-style:italic;font-size:calc(var(--EV)*1.35);color:var(--mute);display:block;margin-top:2px}
.foot{grid-template-columns:1fr auto}
"""
def render(c,fmt):
    plate=f'{S10}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · THE ANSWER",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="q"><b>Q.</b>{E(c["q"])}</div><div class="a">{c["a"]}</div>'
            f'<div class="ev"><b>A.</b><div>“{E(c["ev"])}”<i>{E(c["src"])}</i></div></div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="A1",file="shower",q="can i shower in it?",a="YES<em>.</em>",ev="Waterproof and tarnish free, so daily wear and water are fine.",src="— the care line on the listing",
      skus=["YF5215"],water=True,hero=True,spec="6MM STEEL SPHERES · GOLD TOGGLE · SURGICAL STEEL",cta="SHOP THE BRACELET →",render=render,claims=[("YF5215","6mm")]),
 dict(id="A2",file="tarnish",q="will it tarnish?",a="NO<em>.</em>",ev="Waterproof and tarnish free, so daily wear and water are fine.",src="— the care line on the listing",
      skus=["E20267O"],water=True,hero=True,spec="BRAIDED HOOPS · 25MM · 18K GOLD TONE · SURGICAL STEEL",cta="SHOP THE HOOPS →",render=render,claims=[("E20267O","25mm")]),
 dict(id="A3",file="gold",q="is it real gold?",a="NO<em>.</em>",ev="18k PVD gold tone plated. Surgical stainless steel.",src="— the listing. which is why it is ₹1,499, not ₹49,000.",
      skus=["YF5143"],hero=True,spec="4MM PAPERCLIP · 50CM · 18K PVD · SURGICAL STEEL",cta="SHOP THE CHAIN →",render=render,claims=[("YF5143","4mm · 50cm")]),
 dict(id="A4",file="perfume",q="and perfume?",a="NO<em>.</em>",ev="Keep it away from perfume and harsh chemicals.",src="— the care line on the listing. spray first, then dress.",
      skus=["B00681C"],hero=True,spec="CUSHION CZ · 5MM · RHODIUM PLATED · SURGICAL STEEL",cta="SHOP THE BRACELET →",render=render,claims=[("B00681C","5mm")]),
 dict(id="A5",file="fit",q="will it fit my wrist?",a="15 <em>TO</em> 19<em>.</em>",ev="15-19cm adjustable links.",src="— the listing. that is a small wrist to a large one.",
      skus=["B00681C"],hero=True,spec="CUSHION CZ · 5MM · 15–19CM ADJUSTABLE · RHODIUM",cta="SHOP THE BRACELET →",render=render,claims=[("B00681C","15-19cm · 5mm")]),
]
