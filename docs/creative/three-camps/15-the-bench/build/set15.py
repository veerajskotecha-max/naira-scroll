# -*- coding: utf-8 -*-
"""SET 15 — THE BENCH, on the brand system. The bench photograph above; below it the deck's sage tile: the watercolour
tulips grow up out of the panel as sage paper silhouettes across the seam and become watercolour inside it, the white
wordmark sits over them exactly as on the box, and the tool's name is the headline. No dahlia, no embroidery, no petals."""
from core import *
import re, flora
SET=dict(slug="15-the-bench",title="The Bench",n=5)
S15=f"{ROOT}/s15"
TOK={"feed":dict(PLATE="700px",HEAD="132px",RISE="150px"),"story":dict(PLATE="1110px",HEAD="156px",RISE="180px")}
_mask=f"-webkit-mask-image:url({flora.uri(flora.ASSET['tulips_sage'])});mask-image:url({flora.uri(flora.ASSET['tulips_sage'])});-webkit-mask-size:100% auto;mask-size:100% auto;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;-webkit-mask-position:top;mask-position:top;"
CSS=f"""
.ad{{background:{flora.SAGE};color:#fff}}
.plate{{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#222}}
.plate img{{width:100%;height:100%;object-fit:cover;display:block}}
.panel{{position:absolute;left:0;right:0;top:var(--PLATE);bottom:0;background:{flora.SAGE}}}
.sil{{position:absolute;background:{flora.SAGE};{_mask}pointer-events:none}}
.wc{{position:absolute;pointer-events:none;clip-path:inset(var(--RISE) 0 0 0)}}
.wm{{position:absolute;pointer-events:none}}
.block{{position:absolute;left:var(--pad);top:calc(var(--PLATE) + 44px);width:56%}}
.h{{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;color:#fff}}
.sub{{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:8px;text-wrap:pretty;color:#fff;opacity:.95}}
.fig{{display:flex;gap:26px;margin-top:16px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.85)}}
.fig span b{{display:block;font-family:'Jost';font-weight:600;font-size:calc(var(--MONO)*2.1);letter-spacing:.01em;color:#fff;text-transform:none;margin-top:2px}}
.foot{{grid-template-columns:1fr auto;color:#fff}}
.foot .spec{{color:rgba(255,255,255,.85);opacity:1}}
.cta.solid{{background:#fff;border-color:#fff;color:{flora.SAGE_TXT}}}
.top{{color:#fff}}
"""
def render(c,fmt):
    W,H=FORMATS[fmt]; pad=52 if fmt=="feed" else 64; plate=f'{S15}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    ph=int(TOK[fmt]["PLATE"].replace("px","")); rise=int(TOK[fmt]["RISE"].replace("px","")); plain=re.sub('<[^>]+>','',c['head']); fs=min(int(TOK[fmt]['HEAD'].replace('px','')),int(fit(plain,(W-2*pad)*0.62,0.005)))
    tw=c.get("tw",{"feed":620,"story":760})[fmt]; th=int(tw*1417/2160); tx=W-tw+c.get("tdx",90); ty=ph-rise
    sil=f'<div class="sil" style="left:{tx}px;top:{ty}px;width:{tw}px;height:{th}px"></div>'
    wc=flora.img("tulips_sage",f"left:{tx}px;top:{ty}px;width:{tw}px;").replace('style="position:absolute;','class="wc" style="position:absolute;')
    lv=flora.img("leaves_sage",f"right:-40px;bottom:{170 if fmt=='feed' else 200}px;width:{int(tw*0.62)}px;opacity:.95;").replace('style="position:absolute;','class="wm" style="position:absolute;')
    wm=f'<img class="wm" src="{ADS}/logo_white.png" style="right:{pad}px;bottom:{(250 if fmt=="feed" else 300)}px;width:{280 if fmt=="feed" else 320}px" alt="">'
    figs="".join(f'<span>{E(k)}<b>{E(v)}</b></span>' for k,v in c["figs"])
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div><div class="panel"></div>{lv}{sil}{wc}{wm}'
            f'{top("THE BENCH",IVORY,logo="logo_white.png")}'
            f'<div class="block"><div class="h" style="font-size:{fs}px">{c["head"]}</div><div class="sub">{E(c["sub"])}</div><div class="fig">{figs}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="B1",file="calliper",head="THE CALLIPER.",sub="(a reading, not a promise. twenty-five across.)",figs=[("across","25 mm"),("stones","none"),("pair","one")],skus=["E20267O"],hero=True,spec="BRAIDED HOOPS · 25MM · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,claims=[("E20267O","25mm")]),
 dict(id="B2",file="mandrel",head="THE MANDREL.",sub="(a fixed size is a single number. this is the number.)",figs=[("size","US 7"),("inside","17.3 mm"),("chevron","9.5 mm")],skus=["JDR0303312-7"],spec="US 7 · 17.3MM INSIDE · 9.5MM AT THE CHEVRON · 18K",cta="SHOP THE RING →",render=render,claims=[("JDR0303312-7","17.3mm · 9.5mm · US 7")]),
 dict(id="B3",file="loupe",head="THE LOUPE.",sub="(an eight-millimetre stone in a twelve-millimetre halo. the loupe is for you.)",figs=[("stone","8 mm"),("halo","12 mm"),("size","US 7")],skus=["WR10170K7"],spec="8MM ROUND · 12MM CUSHION HALO · US 7 · RHODIUM",cta="SHOP THE RING →",render=render,claims=[("WR10170K7","8mm · 12mm · US 7")]),
 dict(id="B4",file="ear",head="THE EAR.",sub="(the only bench tool that comes with a pulse. twenty-two across.)",figs=[("across","22 mm"),("discs","6 mm"),("post","straight")],skus=["FE03586B"],spec="FLUTED DISCS · 22MM · CZ CLUSTERS · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,claims=[("FE03586B","22mm · 6mm")]),
 dict(id="B5",file="grid",head="THE GRID.",sub="(engineering paper does not round up. a clover on an eight-and-a-half-millimetre drop.)",figs=[("drop","8.5 mm"),("huggie","10.2 mm"),("pairs","three")],skus=["JDE0201327"],spec="HUGGIE 10.2MM · DROP 8.5MM · THREE PAIRS · 18K",cta="SHOP THE SET →",render=render,claims=[("JDE0201327","8.5mm · 10.2mm")]),
]
