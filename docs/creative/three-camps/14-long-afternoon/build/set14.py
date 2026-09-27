# -*- coding: utf-8 -*-
"""SET 14 — THE LONG AFTERNOON, PRESSED. The khadi stills become herbarium sheets: the photograph mounted with paper
corners, the brand's watercolour sprig and line vine laid across the mount, a specimen label with the listing's figures,
the referent (a shirt button, a cardamom pod) named like a botanist would."""
from core import *
import re, flora
SET=dict(slug="14-long-afternoon",title="The Long Afternoon",n=5)
S14=f"{ROOT}/s14"
TOK={"feed":dict(PLATE="700px",PT="120px",LAB="240px"),"story":dict(PLATE="1080px",PT="150px",LAB="300px")}
CSS="""
.ad{background:#F4EEE4;color:var(--ink)}
.paper{position:absolute;inset:0;background:url(/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/sets/floral/wallpaper.png) center/cover;opacity:.55;mix-blend-mode:multiply}
.mount{position:absolute;left:var(--pad);right:var(--pad);top:var(--PT);height:var(--PLATE);background:#fff;padding:14px;box-shadow:0 10px 30px rgba(27,21,18,.14)}
.mount img.pl{width:100%;height:100%;object-fit:cover;display:block}
.corner{position:absolute;width:44px;height:44px;background:#1B1512;opacity:.85}
.corner.tl{left:-6px;top:-6px;clip-path:polygon(0 0,100% 0,0 100%)}.corner.tr{right:-6px;top:-6px;clip-path:polygon(0 0,100% 0,100% 100%)}
.corner.bl{left:-6px;bottom:-6px;clip-path:polygon(0 0,0 100%,100% 100%)}.corner.br{right:-6px;bottom:-6px;clip-path:polygon(100% 0,100% 100%,0 100%)}
.flora{position:absolute;pointer-events:none;filter:contrast(1.3) saturate(1.25) drop-shadow(0 10px 14px rgba(27,21,18,.25))}
.pet{position:absolute;inset:0;pointer-events:none}
.label{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PT) + var(--PLATE) + 30px);height:var(--LAB);border:1.5px solid var(--ink);padding:16px 22px;display:grid;grid-template-columns:1fr auto;gap:8px 24px;background:rgba(255,255,255,.55)}
.label .t{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.18em;text-transform:uppercase;color:var(--ac);grid-column:1/3;border-bottom:1px solid var(--ink);padding-bottom:8px}
.label .h{font-family:'Velista';font-weight:500;font-size:var(--HEADL);line-height:.95;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;margin-top:6px}
.label .rows{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);line-height:1.25}
.label .rows b{font-family:'JetBrains Mono';font-style:normal;font-weight:400;font-size:calc(var(--MONO)*.92);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);margin-right:8px}
.label .stamp{align-self:end;justify-self:end;width:112px;height:112px;border:1.5px solid var(--ac);border-radius:50%;display:flex;align-items:center;justify-content:center;transform:rotate(-12deg);color:var(--ac);position:relative}
.label .stamp img{width:66px;height:66px;object-fit:contain}
.label .stamp span{position:absolute;inset:0;font-family:'JetBrains Mono';font-size:10px;letter-spacing:.16em;text-transform:uppercase;text-align:center;top:6px}
.lead{position:absolute;pointer-events:none}
.foot{grid-template-columns:1fr auto}
"""
def leader(c,fmt):
    """a hand-drawn leader from the referent to its label, drawn over the mount: (x,y) target in plate fractions"""
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; pt=int(TOK[fmt]["PT"].replace("px","")); ph=int(TOK[fmt]["PLATE"].replace("px",""))
    (tx,ty,lx,ly)=c.get("ref_"+fmt,c["ref"]); mw=W-2*pad-28; mh=ph-28
    X=pad+14+tx*mw; Y=pt+14+ty*mh; LX=pad+14+lx*mw; LY=pt+14+ly*mh
    anchor="end" if lx<tx else "start"
    return (f'<svg class="lead" style="left:0;top:0;width:{W}px;height:{pt+ph+40}px" viewBox="0 0 {W} {pt+ph+40}">'
            f'<path d="M{X:.0f} {Y:.0f} Q {(X+LX)/2:.0f} {min(Y,LY)-40:.0f} {LX:.0f} {LY:.0f}" fill="none" stroke="#6E1E2A" stroke-width="1.3" stroke-dasharray="3 4"/>'
            f'<circle cx="{X:.0f}" cy="{Y:.0f}" r="4" fill="none" stroke="#6E1E2A" stroke-width="1.3"/>'
            f'<text x="{LX+(8 if anchor=="start" else -8):.0f}" y="{LY+5:.0f}" text-anchor="{anchor}" font-family="Cormorant Garamond" font-style="italic" font-size="28" fill="#6E1E2A" stroke="#F4EEE4" stroke-width="5" paint-order="stroke" stroke-linejoin="round">{E(c["refname"])}</text></svg>')
def render(c,fmt):
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; plate=f'{S14}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    pt=int(TOK[fmt]["PT"].replace("px","")); ph=int(TOK[fmt]["PLATE"].replace("px",""))
    headl=min(64 if fmt=="feed" else 74,int(fit(c["head"],(W-2*pad)*0.62,0.005)))
    fl=""
    for (name_,x,y,w,rot) in c.get("flora_"+fmt,c["flora"]):
        fl+=flora.img(name_,f"left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);") .replace('style="position:absolute;','class="flora" style="position:absolute;')
    rows="".join(f'<div><b>{E(k)}</b>{E(v)}</div>' for k,v in c["rows"])
    pet=flora.scatter(4,(W-320,pt+ph-60,W-40,pt+ph+60),seed=c.get('seed',2),sizes=(40,80),colours=[0,1,2],opacity=(0.9,1.0))
    return (f'<div class="paper"></div><div class="mount"><img class="pl" src="{plate}" style="object-position:{c.get("pos","50% 50%")}"><div class="corner tl"></div><div class="corner tr"></div><div class="corner bl"></div><div class="corner br"></div></div>'
            f'{fl}<div class="pet">{pet}</div>{leader(c,fmt)}'
            f'{top("NAIRA PETITE · THE LONG AFTERNOON",INK)}'
            f'<div class="label"><div class="t">herbarium · specimen № {c["no"]} · collected on a long afternoon</div>'
            f'<div><div class="h" style="font-size:{headl}px">{E(c["head"])}</div><div class="rows">{rows}</div></div>'
            f'<div class="stamp"><img src="{flora.uri(flora.ASSET["flower"])}"><span>naira petite · verified</span></div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
def card(**k):
    d=dict(render=render,tok_feed=dict(HEADL="64px"),tok_story=dict(HEADL="74px")); d.update(k); return d
CREATIVES=[
 card(id="H1",no="01",file="hoops",head="Woven Gold Hoops",rows=[("size","25mm across, one pair"),("surface","a braid of gold strands, no stones"),("referent","shirt button, 11mm, mother of pearl")],
      ref=(0.74,0.62,0.52,0.86),ref_story=(0.72,0.62,0.50,0.90),refname="Button, 11mm",flora=[("vine",520,-60,700,14)],flora_story=[("vine",520,-30,780,14)],
      skus=["E20267O"],hero=True,spec="BRAIDED HOOPS · 25MM · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("E20267O","25mm")]),
 card(id="H2",no="02",file="clover",head="Clover Trio Edit",rows=[("drop","detachable four-petal clover, 8.5mm"),("huggie","10.2mm across"),("referent","green cardamom pod")],
      ref=(0.62,0.52,0.80,0.20),ref_story=(0.62,0.50,0.80,0.16),refname="Elettaria cardamomum",flora=[("sprig",-140,300,620,-22)],flora_story=[("sprig",-140,640,700,-22)],
      skus=["JDE0201327"],spec="HUGGIE 10.2MM · CLOVER DROP 8.5MM · THREE PAIRS · 18K",cta="SHOP THE SET →",claims=[("JDE0201327","8.5mm · 10.2mm")]),
 card(id="H3",no="03",file="chevron",head="Chevron Whisper Ring",rows=[("profile","a double V, two fine pavé lines"),("size","US 7, 17.3mm inside, 9.5mm at the chevron"),("referent","shirt button, 11mm")],
      ref=(0.30,0.62,0.12,0.24),ref_story=(0.28,0.60,0.12,0.20),refname="Button, 11mm",flora=[("vine",560,-80,700,-10)],flora_story=[("vine",560,-40,780,-10)],
      skus=["JDR0303312-7"],spec="US 7 · 17.3MM INSIDE · 9.5MM AT THE CHEVRON · 18K",cta="SHOP THE RING →",claims=[("JDR0303312-7","17.3mm · 9.5mm")]),
 card(id="H4",no="04",file="textured",head="Textured Gold Hoops",rows=[("detail","alternating fluted gold discs, 6mm each"),("stones","clusters of small clear cz between the discs"),("size","22mm across, open half hoop"),("referent","shirt button, 11mm")],
      ref=(0.72,0.66,0.86,0.30),ref_story=(0.70,0.64,0.86,0.24),refname="Button, 11mm",flora=[("sprig",-150,-40,620,26)],flora_story=[("sprig",-150,20,700,26)],
      skus=["FE03586B"],spec="FLUTED DISCS · 22MM · CZ CLUSTERS · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("FE03586B","22mm · 6mm")]),
 card(id="H5",no="05",file="chain",head="Toggle Link Chain",rows=[("links","4mm paperclip, 50cm"),("closure","toggle bar and ring, about 15mm"),("referent","shirt button, 11mm, mother of pearl")],
      ref=(0.68,0.66,0.86,0.28),ref_story=(0.68,0.66,0.86,0.24),refname="Button, 11mm",flora=[("vine",-160,200,700,-34)],flora_story=[("vine",-160,520,780,-34)],
      skus=["YF5143"],hero=True,spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM · 18K PVD",cta="SHOP THE CHAIN →",claims=[("YF5143","4mm · 50cm · 15mm")]),
]
