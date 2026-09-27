# -*- coding: utf-8 -*-
"""SET 14 — THE LONG AFTERNOON, on the brand system. Blush ground from the deck, the deck's watercolour tulips rising
from the corner and printed across the seam, a herbarium label ruled in sage, the sage-and-coral wordmark."""
from core import *
import re, flora
SET=dict(slug="14-long-afternoon",title="The Long Afternoon",n=5)
S14=f"{ROOT}/s14"
TOK={"feed":dict(PLATE="720px",HEADL="66px"),"story":dict(PLATE="1120px",HEADL="76px")}
CSS=f"""
.ad{{background:{flora.BLUSH};color:var(--ink)}}
.plate{{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#eee}}
.plate img{{width:100%;height:100%;object-fit:cover;display:block}}
.tul{{position:absolute;pointer-events:none}}
.lead{{position:absolute;pointer-events:none}}
.label{{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 34px);border-top:1.5px solid {flora.SAGE};padding-top:14px;display:grid;grid-template-columns:minmax(0,62%) auto;gap:8px 24px}}
.label .t{{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.18em;text-transform:uppercase;color:{flora.SAGE_TXT};grid-column:1/3}}
.label .h{{font-family:'Velista';font-weight:500;font-size:var(--HEADL);line-height:.95;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;margin-top:8px}}
.label .rows{{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);line-height:1.25;margin-top:6px}}
.label .rows b{{font-family:'JetBrains Mono';font-style:normal;font-weight:400;font-size:calc(var(--MONO)*.92);letter-spacing:.14em;text-transform:uppercase;color:{flora.SAGE_TXT};margin-right:8px}}
.label .stamp{{align-self:start;justify-self:end;width:118px;height:118px;border-radius:50%;background:{flora.CORAL};display:flex;align-items:center;justify-content:center;transform:rotate(-10deg);margin-top:10px;box-shadow:0 6px 14px rgba(27,21,18,.12)}}
.label .stamp img{{width:64px;height:64px;object-fit:contain;filter:brightness(0) invert(1)}}
.foot{{grid-template-columns:1fr auto}}
.foot .spec{{color:{flora.SAGE_TXT};opacity:1}}
.cta.solid{{background:{flora.SAGE};border-color:{flora.SAGE};color:#fff}}
.top{{color:{flora.SAGE_TXT}}}
.top img{{height:48px}}
"""
def leader(c,fmt):
    W=FORMATS[fmt][0]; ph=int(TOK[fmt]["PLATE"].replace("px",""))
    (tx,ty,lx,ly)=c.get("ref_"+fmt,c["ref"]); X=tx*W; Y=ty*ph; LX=lx*W; LY=ly*ph; anchor="end" if lx<tx else "start"
    return (f'<svg class="lead" style="left:0;top:0;width:{W}px;height:{ph}px" viewBox="0 0 {W} {ph}">'
            f'<path d="M{X:.0f} {Y:.0f} Q {(X+LX)/2:.0f} {min(Y,LY)-40:.0f} {LX:.0f} {LY:.0f}" fill="none" stroke="{flora.SAGE}" stroke-width="1.6" stroke-dasharray="3 4"/>'
            f'<circle cx="{X:.0f}" cy="{Y:.0f}" r="4.5" fill="none" stroke="{flora.SAGE}" stroke-width="1.6"/>'
            f'<text x="{LX+(8 if anchor=="start" else -8):.0f}" y="{LY+5:.0f}" text-anchor="{anchor}" font-family="Cormorant Garamond" font-style="italic" font-size="32" fill="{flora.SAGE_TXT}" stroke="{flora.BLUSH}" stroke-width="5" paint-order="stroke" stroke-linejoin="round">{E(c["refname"])}</text></svg>')
def render(c,fmt):
    W,H=FORMATS[fmt]; pad=52 if fmt=="feed" else 64; plate=f'{S14}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    ph=int(TOK[fmt]["PLATE"].replace("px","")); headl=min(int(TOK[fmt]["HEADL"].replace("px","")),int(fit(c["head"],(W-2*pad)*0.66,0.005)))
    tw=c.get("tw",{"feed":560,"story":680})[fmt]; lw=int(tw*0.78)
    tul=flora.img("tulips_blush",f"right:-70px;top:{ph-58}px;width:{tw}px;").replace('style="position:absolute;','class="tul" style="position:absolute;')
    lea=flora.img("leaves_blush",f"left:-90px;bottom:-24px;width:{lw}px;opacity:.9;transform:rotate(-6deg);").replace('style="position:absolute;','class="tul" style="position:absolute;')
    rows="".join(f'<div><b>{E(k)}</b>{E(v)}</div>' for k,v in c["rows"])
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>{leader(c,fmt)}{tul}{lea}'
            f'{top("THE LONG AFTERNOON",flora.SAGE_TXT,logo="logo_sage_dark.png")}'
            f'<div class="label"><div class="t">herbarium · specimen № {c["no"]} · collected on a long afternoon</div>'
            f'<div><div class="h" style="font-size:{headl}px">{E(c["head"])}</div><div class="rows">{rows}</div></div>'
            f'<div class="stamp"><img src="{flora.uri(flora.ASSET["flower"])}"></div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
def card(**k):
    d=dict(render=render); d.update(k); return d
CREATIVES=[
 card(id="H1",no="01",file="hoops",head="Woven Gold Hoops",rows=[("size","25mm across, one pair"),("surface","a braid of gold strands, no stones"),("referent","shirt button, 11mm, mother of pearl")],
      ref=(0.74,0.62,0.52,0.90),ref_story=(0.72,0.62,0.50,0.92),refname="Button, 11mm",
      skus=["E20267O"],hero=True,spec="BRAIDED HOOPS · 25MM · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("E20267O","25mm")]),
 card(id="H2",no="02",file="clover",head="Clover Trio Edit",rows=[("drop","detachable four-petal clover, 8.5mm"),("huggie","10.2mm across"),("referent","green cardamom pod")],
      ref=(0.62,0.52,0.82,0.16),ref_story=(0.62,0.50,0.82,0.14),refname="Elettaria cardamomum",
      skus=["JDE0201327"],spec="HUGGIE 10.2MM · CLOVER DROP 8.5MM · THREE PAIRS · 18K",cta="SHOP THE SET →",claims=[("JDE0201327","8.5mm · 10.2mm")]),
 card(id="H3",no="03",file="chevron",head="Chevron Whisper Ring",rows=[("profile","a double V, two fine pavé lines"),("size","US 7, 17.3mm inside, 9.5mm at the chevron"),("referent","shirt button, 11mm")],
      ref=(0.30,0.62,0.14,0.22),ref_story=(0.28,0.60,0.14,0.18),refname="Button, 11mm",
      skus=["JDR0303312-7"],spec="US 7 · 17.3MM INSIDE · 9.5MM AT THE CHEVRON · 18K",cta="SHOP THE RING →",claims=[("JDR0303312-7","17.3mm · 9.5mm")]),
 card(id="H4",no="04",file="textured",head="Textured Gold Hoops",rows=[("detail","alternating fluted gold discs, 6mm each"),("stones","clusters of small clear cz between the discs"),("size","22mm across, open half hoop · referent: button, 11mm")],
      ref=(0.72,0.66,0.86,0.28),ref_story=(0.70,0.64,0.86,0.22),refname="Button, 11mm",
      skus=["FE03586B"],spec="FLUTED DISCS · 22MM · CZ CLUSTERS · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("FE03586B","22mm · 6mm")]),
 card(id="H5",no="05",file="chain",head="Toggle Link Chain",rows=[("links","4mm paperclip, 50cm"),("closure","toggle bar and ring, about 15mm"),("referent","shirt button, 11mm, mother of pearl")],
      ref=(0.68,0.66,0.86,0.26),ref_story=(0.68,0.66,0.86,0.22),refname="Button, 11mm",
      skus=["YF5143"],hero=True,spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM · 18K PVD",cta="SHOP THE CHAIN →",claims=[("YF5143","4mm · 50cm · 15mm")]),
]
