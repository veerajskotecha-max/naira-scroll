# -*- coding: utf-8 -*-
"""SET 15 — THE BENCH, IN BLOOM. The bench stills with the brand's painted bloom laid on the bench like a flower someone
brought in, petals fallen across the plate with the bench's own shadow, the embroidered floral cloth as the table's edge,
and the tool's name as the headline. Nothing here claims the piece was made by hand; the bench measures, it does not make."""
from core import *
import re, flora
SET=dict(slug="15-the-bench",title="The Bench",n=5)
S15=f"{ROOT}/s15"
TOK={"feed":dict(PLATE="760px",HEAD="150px",CLOTH="64px"),"story":dict(PLATE="1200px",HEAD="176px",CLOTH="80px")}
CSS="""
.ad{background:var(--bg);color:var(--ink)}
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}
.plate img.pl{width:100%;height:100%;object-fit:cover;display:block}
.pet{position:absolute;inset:0;pointer-events:none}
.bloom{position:absolute;pointer-events:none;filter:drop-shadow(0 14px 18px rgba(27,21,18,.35))}
.cloth{position:absolute;left:0;right:0;top:calc(var(--PLATE) - 6px);height:var(--CLOTH);background:url(/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/sets/floral/embroidery.jpg) center/cover;box-shadow:0 8px 20px rgba(27,21,18,.18)}
.cloth:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(241,235,225,0),rgba(241,235,225,.15))}
.wm{position:absolute;right:-120px;bottom:60px;width:620px;opacity:.10;pointer-events:none;filter:grayscale(1) brightness(.4)}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + var(--CLOTH) + 18px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap}
.h em{font-style:normal;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:6px;text-wrap:pretty;max-width:36ch}
.fig{display:flex;gap:26px;margin-top:16px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.12em;text-transform:uppercase}
.fig span b{display:block;font-family:'Jost';font-weight:600;font-size:calc(var(--MONO)*2.1);letter-spacing:.01em;color:var(--ac);text-transform:none;margin-top:2px}
.foot{grid-template-columns:1fr auto}
"""
def render(c,fmt):
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; plate=f'{S15}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    ph=int(TOK[fmt]["PLATE"].replace("px","")); plain=re.sub('<[^>]+>','',c['head']); fs=min(int(TOK[fmt]['HEAD'].replace('px','')),int(fit(plain,W-2*pad,0.005)))
    bx,by,bw,br=c.get("bloom_"+fmt,c["bloom"])
    bloom=flora.img("bloom",f"left:{bx}px;top:{by}px;width:{bw}px;transform:rotate({br}deg);").replace('style="position:absolute;','class="bloom" style="position:absolute;')
    pet=flora.scatter(c.get("n",6),(0,int(ph*0.35),W,ph-40),seed=c.get("seed",4),sizes=(36,90),colours=[0,4,2],opacity=(0.92,1.0))
    figs="".join(f'<span>{E(k)}<b>{E(v)}</b></span>' for k,v in c["figs"])
    return (f'<div class="plate"><img class="pl" src="{plate}" style="object-position:{c.get("pos","50% 50%")}"><div class="pet">{pet}</div>{bloom}</div>'
            f'<div class="cloth"></div><img class="wm" src="{flora.uri(flora.ASSET["flower"])}" alt="">'
            f'{top("NAIRA PETITE · THE BENCH",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="h" style="font-size:{fs}px">{c["head"]}</div><div class="sub">{E(c["sub"])}</div><div class="fig">{figs}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="B1",file="calliper",head="THE <em>CALLIPER.</em>",sub="(a reading, not a promise. twenty-five across, and a flower on the bench for luck.)",bloom=(690,70,380,18),bloom_story=(700,140,440,18),dark=True,
      figs=[("across","25 mm"),("stones","none"),("pair","one")],skus=["E20267O"],hero=True,spec="BRAIDED HOOPS · 25MM · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,claims=[("E20267O","25mm")],seed=4),
 dict(id="B2",file="mandrel",head="THE <em>MANDREL.</em>",sub="(a fixed size is a single number. this is the number.)",bloom=(-120,380,420,-24),bloom_story=(-120,720,470,-24),dark=True,
      figs=[("size","US 7"),("inside","17.3 mm"),("chevron","9.5 mm")],skus=["JDR0303312-7"],spec="US 7 · 17.3MM INSIDE · 9.5MM AT THE CHEVRON · 18K",cta="SHOP THE RING →",render=render,claims=[("JDR0303312-7","17.3mm · 9.5mm · US 7")],seed=8),
 dict(id="B3",file="loupe",head="THE <em>LOUPE.</em>",sub="(an eight-millimetre stone in a twelve-millimetre halo. the loupe is for you, not us.)",bloom=(680,360,400,30),bloom_story=(700,720,460,30),
      figs=[("stone","8 mm"),("halo","12 mm"),("size","US 7")],skus=["WR10170K7"],spec="8MM ROUND · 12MM CUSHION HALO · US 7 · RHODIUM",cta="SHOP THE RING →",render=render,claims=[("WR10170K7","8mm · 12mm · US 7")],seed=2),
 dict(id="B4",file="ear",head="THE <em>EAR.</em>",sub="(the only bench tool that comes with a pulse. twenty-two across, discs and clusters.)",bloom=(-90,90,380,22),bloom_story=(-90,160,440,22),dark=True,
      figs=[("across","22 mm"),("discs","6 mm"),("post","straight")],skus=["FE03586B"],spec="FLUTED DISCS · 22MM · CZ CLUSTERS · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,claims=[("FE03586B","22mm · 6mm")],seed=6),
 dict(id="B5",file="grid",head="THE <em>GRID.</em>",sub="(engineering paper does not round up. a clover on an eight-and-a-half-millimetre drop.)",bloom=(670,80,380,-16),bloom_story=(690,150,440,-16),
      figs=[("drop","8.5 mm"),("huggie","10.2 mm"),("pairs","three")],skus=["JDE0201327"],spec="HUGGIE 10.2MM · DROP 8.5MM · THREE PAIRS · 18K",cta="SHOP THE SET →",render=render,claims=[("JDE0201327","8.5mm · 10.2mm")],seed=3),
]
