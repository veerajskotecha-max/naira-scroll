# -*- coding: utf-8 -*-
"""SET 13 — PIGMENT, IN BLOOM. Each colour field becomes the card; the photograph is seen through a window cut in the
shape of the brand flower; the brand's rose petals, tinted from the pigment itself, drift across the cut edge."""
from core import *
import re, flora
SET=dict(slug="13-pigment",title="Pigment",n=5)
PIG="/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/pig"
TOK={"feed":dict(WIN="1000px",WW="900px",WT="-60px",HEAD="168px"),"story":dict(WIN="1300px",WW="1170px",WT="-40px",HEAD="196px")}
CSS="""
.ad{background:var(--bg);color:var(--ink)}
.win,.rim{position:absolute;left:50%;top:var(--WT);width:var(--WW);height:var(--WIN);transform:translateX(-50%);-webkit-mask-image:url("data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2036%2040%22%3E%3Cpath%20d%3D%22M18%203%20C8%204%202%2014%204%2024%20C6%2033%2014%2039%2018%2038%20C22%2039%2030%2033%2032%2024%20C34%2014%2028%204%2018%203%20Z%22%20fill%3D%22black%22/%3E%3C/svg%3E");mask-image:url("data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20viewBox%3D%220%200%2036%2040%22%3E%3Cpath%20d%3D%22M18%203%20C8%204%202%2014%204%2024%20C6%2033%2014%2039%2018%2038%20C22%2039%2030%2033%2032%2024%20C34%2014%2028%204%2018%203%20Z%22%20fill%3D%22black%22/%3E%3C/svg%3E");-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat}
.rim{background:var(--rim);transform:translateX(-50%) scale(1.012);opacity:.9}
.win{background-size:cover;background-repeat:no-repeat}
.pet{position:absolute;inset:0;pointer-events:none}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--WIN) + var(--WT) - 90px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:8px;text-wrap:pretty;max-width:38ch}
.foot{grid-template-columns:1fr auto}
.cta.solid{background:var(--ink);border-color:var(--ink);color:var(--bg)}
"""
def render(c,fmt):
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; plain=re.sub('<[^>]+>','',c['head']); fs=min(int(TOK[fmt]['HEAD'].replace('px','')),int(fit(plain,W-2*pad,0.005)))
    plate=f'{PIG}/{c["file"]}.png'; sku=c["skus"][0]; winh=int(TOK[fmt]["WIN"].replace("px",""))
    tints=[flora.tint_from(h) for h in c["tints"]]
    pet=flora.scatter(c.get("n",9),(0,int(winh*0.30),W,int(winh*0.98)),seed=c.get("seed",1),sizes=(50,150),colours=tints,opacity=(0.9,1.0))
    return (f'<div class="rim"></div><div class="win" style="background-image:url({plate});background-position:{c.get("pos_"+fmt,c.get("pos","50% 50%"))}"></div><div class="pet">{pet}</div>'
            f'{top("NAIRA PETITE · PIGMENT",c["ink"],logo=("logo_ivory.png" if c["ink"]==IVORY else "logo_ink.png"))}'
            f'<div class="block"><div class="h" style="font-size:{fs}px">{c["head"]}</div><div class="sub">{E(c["sub"])}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
def card(**k):
    d=dict(render=render); d.update(k); d["rim"]=d.get("rim","rgba(241,235,225,.85)"); return d
CREATIVES=[
 card(id="G1",file="P08",head="LILAC.",sub="(the pearl is champagne, the powder is lilac. neither is trying to match.)",bg="#C8B1C6",ink=INK,tints=["#A98CB0","#8E6BB0","#D9C3D8"],pos="50% 45%",
      skus=["E20997C"],spec="PAVÉ BOW · 9MM SHELL PEARL · 18MM TALL · RHODIUM",cta="SHOP THE STUDS →",claims=[("E20997C","9mm · 18mm")],seed=5),
 card(id="G2",file="P01",head="PASTEL.",sub="(three powders, three stones, one straight line.)",bg="#346254",ink=IVORY,tints=["#8FD2C7","#E9D46C","#F0A6B6"],pos="50% 40%",
      skus=["B00681C"],hero=True,spec="CUSHION CZ · 5MM · AQUA, PINK, YELLOW · RHODIUM",cta="SHOP THE BRACELET →",claims=[("B00681C","5mm")],seed=11,n=12),
 card(id="G3",file="P10",head="CORNFLOWER.",sub="(because steel wanted a cold blue, and the heart wanted the opposite.)",bg="#6A91CB",ink=IVORY,tints=["#8FB0E0","#4E77B8","#C7D7F0"],pos="50% 50%",
      skus=["YF5215"],hero=True,spec="6MM MIRROR STEEL · GOLD TOGGLE · ONE GOLD HEART",cta="SHOP THE BRACELET →",claims=[("YF5215","6mm")],seed=7),
 card(id="G4",file="P06",head="GREEN.",sub="(green cubic zirconia. not emerald, and the listing says so.)",bg="#285849",ink=IVORY,tints=["#4E8A72","#9CC7B0","#2F6B55"],pos="38% 55%",
      skus=["FE02847B"],spec="10MM GREEN CZ · 6MM PEARL · 20MM TALL · 18K GOLD TONE",cta="SHOP THE STUDS →",claims=[("FE02847B","10mm · 6mm · 20mm")],seed=3),
 card(id="G5",file="P04",head="CORAL.",sub="(for a bow that never comes undone.)",bg="#D95E5E",ink=IVORY,tints=["#F2A38F","#B8443F","#F7C8B8"],pos="58% 45%",
      skus=["E16075B"],spec="BOW STUDS · 15MM WIDE · PEAR-CUT CZ · 18K GOLD TONE",cta="SHOP THE STUDS →",claims=[("E16075B","15mm")],seed=9),
]
