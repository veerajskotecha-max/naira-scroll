# -*- coding: utf-8 -*-
"""SET 05 — THE LAYER. Stacking arithmetic in millimetres. Every stack is drawn with engineering dimension
lines pulled from the listing's own figures; the headline is the sum. Basket size is the lever."""
from core import *
SET=dict(slug="05-the-layer",title="The Layer",n=5)
S5=f"{ROOT}/s05"
TOK={"feed":dict(PLATE="820px",HEAD="150px",SUMW="700px"),"story":dict(PLATE="1240px",HEAD="176px",SUMW="900px")}
CSS="""
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.plate svg{position:absolute;inset:0;width:100%;height:100%}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 26px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:-.005em;text-transform:uppercase;white-space:nowrap}
.h em{font-style:normal;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:6px}
.sum{display:grid;grid-template-columns:auto 1fr auto;gap:8px 18px;margin-top:18px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;max-width:var(--SUMW)}
.sum span:nth-child(3n+1){color:var(--ac);font-weight:500;white-space:nowrap}
.sum span:nth-child(3n+3){text-align:right;white-space:nowrap;font-family:'Jost';font-weight:600;font-size:calc(var(--MONO)*1.25);letter-spacing:.02em}
.sum .tot{border-top:1px solid var(--ink);padding-top:8px;margin-top:2px}
.foot{grid-template-columns:1fr auto}
.foot .tot{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.foot .tot b{font-family:'Jost';font-weight:600;font-size:var(--PRICE);letter-spacing:.01em;color:var(--ink);display:block;margin-top:4px}
"""
def dims(c,fmt):
    """engineering dimension lines: (x, y0, y1, label, side) in plate fractions; vertical measure with extension ticks"""
    W,H=FORMATS[fmt]; ph=int(TOK[fmt]["PLATE"].replace("px",""))
    pts=c.get("dims_"+fmt,c["dims"]); out=[]
    col="#F1EBE1" if c.get("dark") else "#1B1512"; halo="#1B1512" if c.get("dark") else "#F1EBE1"
    for (x,y0,y1,label,side) in pts:
        X=x*W; Y0=y0*ph; Y1=y1*ph; tick=14 if side=="r" else -14
        out.append(f'<line x1="{X:.0f}" y1="{Y0:.0f}" x2="{X:.0f}" y2="{Y1:.0f}" stroke="{col}" stroke-width="1.5"/>'
                   f'<line x1="{X-8:.0f}" y1="{Y0:.0f}" x2="{X+8:.0f}" y2="{Y0:.0f}" stroke="{col}" stroke-width="1.5"/><line x1="{X-8:.0f}" y1="{Y1:.0f}" x2="{X+8:.0f}" y2="{Y1:.0f}" stroke="{col}" stroke-width="1.5"/>'
                   f'<text x="{X+tick:.0f}" y="{(Y0+Y1)/2+5:.0f}" text-anchor="{"start" if side=="r" else "end"}" font-family="JetBrains Mono" font-size="15" letter-spacing="1.5" fill="{col}" stroke="{halo}" stroke-width="3" stroke-opacity=".5" stroke-linejoin="round" paint-order="stroke">{E(label)}</text>')
    return f'<svg viewBox="0 0 {W} {ph}">{"".join(out)}</svg>'
def render(c,fmt):
    plate=f'{S5}/plate_{c["plate"]}_{fmt}.jpg'
    rows="".join(f'<span>{E(a)}</span><span>{name(s)}</span><span>{price(s)}</span>' for a,s in c["rows"])
    total=sum(ROWS[s]["price"] for _,s in c["rows"])
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}">{dims(c,fmt)}</div>'
            f'{top("NAIRA PETITE · THE LAYER",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="h">{c["head"]}</div><div class="sub">{E(c["sub"])}</div><div class="sum">{rows}</div></div>'
            f'<div class="foot"><div class="tot">the stack · {len(c["rows"])} pieces<b>{rupees(total)}</b></div><span class="cta solid">{E(c["cta"])}</span></div>')
CREATIVES=[
 dict(id="L1",file="neck",plate="neck",head="2 <em>+</em> 4.",sub="(six millimetres of chain. the silver at 40cm, the gold at 50cm.)",rows=[("2mm snake · 40cm","YF8439-SLV"),("4mm paperclip · 50cm","YF5143")],skus=["YF8439-SLV","YF5143"],
      dims=[(0.83,0.10,0.42,"2MM · 40CM","r"),(0.14,0.10,0.70,"4MM · 50CM","r")],dims_story=[(0.83,0.15,0.48,"2MM · 40CM","r"),(0.14,0.15,0.67,"4MM · 50CM","r")],cta="SHOP NECKLACES →",render=render,pos="50% 55%",
      claims=[("YF8439-SLV","2mm · 40cm"),("YF5143","4mm · 50cm")]),
 dict(id="L2",file="wrist",plate="wrist",head="5 <em>+</em> 6.",sub="(eleven millimetres of wrist. pastel stones beside steel spheres.)",
      rows=[("5mm cushion cz","B00681C"),("6mm steel spheres","YF5215")],skus=["B00681C","YF5215"],hero=True,
      dims=[(0.30,0.36,0.44,"5MM","l"),(0.68,0.25,0.31,"6MM","r")],dims_story=[(0.32,0.39,0.45,"5MM","l"),(0.72,0.28,0.33,"6MM","r")],cta="SHOP BRACELETS →",render=render,pos="50% 50%",
      claims=[("B00681C","5mm"),("YF5215","6mm")]),
 dict(id="L3",file="hand",plate="hand",head="4 <em>+</em> 12.",sub="(four fine bands beside a twelve-millimetre halo.)",
      rows=[("4 bands · 2 pavé, 2 plain","WR12518B"),("12mm halo · 8mm stone","WR10170K7")],skus=["WR12518B","WR10170K7"],
      dims=[(0.17,0.40,0.55,"4 BANDS","l"),(0.66,0.50,0.63,"12MM","r")],dims_story=[(0.18,0.39,0.48,"4 BANDS","l"),(0.70,0.47,0.57,"12MM","r")],cta="SHOP RINGS →",render=render,pos="50% 45%",
      claims=[("WR10170K7","12mm · 8mm")]),
 dict(id="L4",file="ear",plate="ear",head="12 <em>+</em> 25.",sub="(the huggie above, the hoop below. two piercings, one ear.)",
      rows=[("12mm huggie","E14776S"),("25mm hoop","E20267O")],skus=["E14776S","E20267O"],hero=True,
      dark=True,logo_feed="logo_ink.png",dims=[(0.22,0.44,0.72,"12MM","l"),(0.70,0.40,0.80,"25MM","r")],dims_story=[(0.22,0.56,0.75,"12MM","l"),(0.68,0.53,0.82,"25MM","r")],cta="SHOP EARRINGS →",render=render,pos="50% 50%",
      claims=[("E14776S","12mm"),("E20267O","25mm")]),
 dict(id="L5",file="nest",plate="nest",head="9.5 <em>+</em> 12.",sub="(the chevron is cut to nest against a solitaire. the listing says so.)",
      rows=[("9.5mm at the chevron","JDR0303312-7"),("12mm halo · 8mm stone","WR10170K7")],skus=["JDR0303312-7","WR10170K7"],
      dark=True,dims=[(0.26,0.29,0.44,"9.5MM","l"),(0.74,0.47,0.68,"12MM","r")],dims_story=[(0.12,0.32,0.43,"9.5MM","r"),(0.86,0.43,0.63,"12MM","r")],cta="SHOP RINGS →",render=render,pos="50% 50%",
      claims=[("JDR0303312-7","9.5mm"),("WR10170K7","12mm · 8mm")]),
]
