# -*- coding: utf-8 -*-
"""SET 12 — THE RED ROOM, RE-DRESSED. Oxblood, wet lacquer, red glass. Five overlays that behave like the room: water-drop
loupes, a headline that reflects, a cloakroom ticket numbered with the price, a wine list, a darkroom contact sheet."""
from core import *
import re, base64
SET=dict(slug="12-red-room",title="The Red Room",n=5)
S12=f"{ROOT}/s12"
RED="#B3122E"; ROOM="#1A0508"
TOK={"feed":dict(PLATE="790px",HEAD="150px",DEV="250px"),"story":dict(PLATE="1230px",HEAD="176px",DEV="330px")}
CSS="""
.ad{background:var(--bg);color:var(--ink)}
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#2a0a0f}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.plate:after{content:"";position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(180deg,rgba(26,5,8,0),var(--bg))}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) - 30px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap}
.h em{font-style:normal;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:6px;text-wrap:pretty;max-width:36ch}
.dev{position:relative;height:var(--DEV);margin-top:10px}
.foot{grid-template-columns:1fr auto}
.foot .spec{opacity:.8}
.cta.solid{background:var(--ac);border-color:var(--ac);color:#fff}
/* R1 lenses */
.lens{position:absolute;border-radius:50%;border:1.5px solid rgba(241,235,225,.85);box-shadow:0 10px 30px rgba(0,0,0,.45), inset 0 0 0 6px rgba(255,255,255,.06);overflow:hidden;background-repeat:no-repeat}
.lens:after{content:"";position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 30% 25%, rgba(255,255,255,.35), rgba(255,255,255,0) 38%)}
.lens i{position:absolute;left:8px;bottom:8px;font-style:normal;font-family:'JetBrains Mono';font-size:12px;letter-spacing:.14em;color:#F1EBE1;background:rgba(26,5,8,.55);padding:2px 6px}
.lz{position:absolute;inset:0}
/* R2 mirror */
.mir{position:relative;margin-top:-6px}
.mir .h2{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap;transform:scaleY(-1);-webkit-mask-image:linear-gradient(180deg,rgba(0,0,0,.75),rgba(0,0,0,0) 90%);mask-image:linear-gradient(180deg,rgba(0,0,0,.75),rgba(0,0,0,0) 90%);color:var(--ac)}
.mir .rule{height:1px;background:rgba(241,235,225,.35);margin:2px 0 0}
/* R3 ticket */
.tix{position:absolute;left:0;top:0;width:760px;height:100%;border:1.5px dashed rgba(241,235,225,.7);display:grid;grid-template-columns:1fr auto;align-items:center;padding:16px 24px;gap:18px}
.tix .l .k{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.2em;text-transform:uppercase;color:var(--ac)}
.tix .l .n{font-family:'Velista';font-size:136px;line-height:.9;margin-top:6px}
.tix .l .n small{font-family:'Jost';font-weight:400;font-size:38px;vertical-align:.55em;margin-right:8px;color:var(--ac)}
.tix .l .m{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.14em;text-transform:uppercase;margin-top:10px;opacity:.85}
.tix .r{writing-mode:vertical-rl;transform:rotate(180deg);font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.3em;text-transform:uppercase;border-left:1.5px dashed rgba(241,235,225,.7);padding-left:14px;opacity:.85}
/* R4 wine list */
.list{font-family:'JetBrains Mono';font-size:calc(var(--MONO)*1.1);letter-spacing:.06em;max-width:720px}
.list .row{display:grid;grid-template-columns:auto 1fr auto;gap:0 12px;align-items:baseline;margin-bottom:7px}
.list .row.big{font-family:'Jost';font-weight:600;font-size:calc(var(--MONO)*1.6);letter-spacing:.06em;text-transform:uppercase;margin-bottom:14px}
.list .dots{border-bottom:1px dotted rgba(241,235,225,.45);transform:translateY(-5px)}
.list .k{text-transform:uppercase;letter-spacing:.14em;color:var(--ac)}
.list .v{font-family:'Cormorant Garamond';font-style:italic;font-size:calc(var(--MONO)*1.75);letter-spacing:0}
/* R5 contact sheet */
.sheet{position:absolute;left:calc(-1 * var(--pad));right:calc(-1 * var(--pad));top:0;height:100%;background:#0e0304;display:flex;align-items:center;gap:0;padding:0 var(--pad);overflow:hidden}
.sheet .fr{position:relative;height:calc(100% - 44px);aspect-ratio:4/5;background:#000;border-left:2px solid #2b0d10;flex:none;overflow:hidden}
.sheet .fr img{width:100%;height:100%;object-fit:cover;display:block;filter:contrast(1.05)}
.sheet .fr:before,.sheet .fr:after{content:"";position:absolute;left:0;right:0;height:10px;background:repeating-linear-gradient(90deg,#f1ebe1 0 8px,transparent 8px 22px);opacity:.55}
.sheet .fr:before{top:-14px}.sheet .fr:after{bottom:-14px}
.sheet .fr span{position:absolute;left:6px;top:6px;font-family:'JetBrains Mono';font-size:11px;letter-spacing:.14em;color:#F1EBE1;opacity:.8}
.sheet svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.sheet .lab{position:absolute;right:var(--pad);bottom:10px;font-family:'JetBrains Mono';font-size:12px;letter-spacing:.2em;color:#F1EBE1;opacity:.75;text-transform:uppercase}
"""
def lenses(c,fmt):
    W=FORMATS[fmt][0]; ph=int(TOK[fmt]["PLATE"].replace("px","")); plate=f'{S12}/plate_{c["file"]}_{fmt}.jpg'
    out=[]; z=c.get("zoom",2.1)
    for (tx,ty,lx,ly,d,label) in c.get("lens_"+fmt,c["lens"]):
        TX,TY=tx*W,ty*ph; LX,LY=lx*W,ly*ph
        bw,bh=W*z,ph*z; bx=-(TX*z-d/2); by=-(TY*z-d/2)
        out.append(f'<line x1="{TX:.0f}" y1="{TY:.0f}" x2="{LX:.0f}" y2="{LY:.0f}" stroke="rgba(241,235,225,.8)" stroke-width="1.5"/><circle cx="{TX:.0f}" cy="{TY:.0f}" r="4" fill="#F1EBE1"/>')
        out.append(f'</svg><div class="lens" style="left:{LX-d/2:.0f}px;top:{LY-d/2:.0f}px;width:{d}px;height:{d}px;background-image:url({plate});background-size:{bw:.0f}px {bh:.0f}px;background-position:{bx:.0f}px {by:.0f}px"><i>{E(label)}</i></div><svg class="lz" viewBox="0 0 {W} {ph}">')
    return f'<svg class="lz" viewBox="0 0 {W} {ph}">{"".join(out)}</svg>'
def device(c,fmt):
    k=c["dev"]
    if k=="mirror": return f'<div class="mir"><div class="rule"></div><div class="h2" style="font-size:{c.get("_fs",150)}px">{c["head"]}</div></div>'
    if k=="ticket":
        return (f'<div class="tix"><div class="l"><div class="k">{E(c["tk"])}</div><div class="n"><small>№</small>{E(c["tn"])}</div><div class="m">{E(c["tm"])}</div></div><div class="r">{E(c["tr"])}</div></div>')
    if k=="list":
        rows="".join(f'<div class="row{" big" if i==0 else ""}"><span class="k">{E(a)}</span><span class="dots"></span><span class="v">{E(b)}</span></div>' for i,(a,b) in enumerate(c["rows"]))
        return f'<div class="list">{rows}</div>'
    if k=="sheet":
        plate=f'{S12}/plate_{c["file"]}_sheet.jpg'
        frs="".join(f'<div class="fr"><img src="{plate}" style="object-position:{p}"><span>{n}</span></div>' for n,p in c["frames"])
        return (f'<div class="sheet">{frs}<svg viewBox="0 0 1080 250" preserveAspectRatio="none"><ellipse cx="{c["circle"][0]}" cy="125" rx="{c["circle"][1]}" ry="112" fill="none" stroke="#F1EBE1" stroke-width="4" stroke-linecap="round" stroke-dasharray="520 40" transform="rotate(-6 {c["circle"][0]} 125)" opacity=".92"/></svg><div class="lab">{E(c["lab"])}</div></div>')
    return ""
def render(c,fmt):
    plate=f'{S12}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; plain=re.sub('<[^>]+>','',c['head']); fs=min(int(TOK[fmt]['HEAD'].replace('px','')),int(fit(plain,W-2*pad,0.005)))
    over=lenses(c,fmt) if c["dev"]=="lens" else ""
    c["_fs"]=fs; mir=device(c,fmt) if c["dev"]=="mirror" else ""
    dev_html="" if c["dev"] in ("mirror","lens") else '<div class="dev">'+device(c,fmt)+'</div>'
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}">{over}</div>'
            f'{top("NAIRA PETITE · THE RED ROOM",IVORY,logo="logo_ivory.png")}'
            f'<div class="block"><div class="h" style="font-size:{fs}px">{c["head"]}</div>{mir}<div class="sub">{E(c["sub"])}</div>{dev_html}</div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
COMMON=dict(render=render,ink=IVORY,bg=ROOM,ac=RED,hero=True)
CREATIVES=[
 dict(id="R1",file="dome",head="LOOK <em>CLOSER.</em>",sub="(three drops, three loupes. the braid holds up under all of them.)",dev="lens",zoom=2.2,
      lens=[(0.35,0.55,0.17,0.27,230,"×2 · the plait"),(0.66,0.42,0.85,0.22,190,"×2 · no stones"),(0.10,0.60,0.13,0.82,170,"×2 · the drop")],
      lens_story=[(0.36,0.52,0.16,0.22,260,"×2 · the plait"),(0.66,0.44,0.84,0.20,220,"×2 · no stones"),(0.12,0.70,0.14,0.90,200,"×2 · the drop")],
      skus=["E20267O"],water=True,spec="BRAIDED HOOPS · 25MM · WATERPROOF · 18K GOLD TONE",cta="SHOP THE HOOPS →",claims=[("E20267O","25mm")],**COMMON),
 dict(id="R2",file="lacquer",head="TWICE.",sub="(one bracelet, two of everything. the lacquer does the second.)",dev="mirror",
      skus=["B00681C"],water=True,spec="CUSHION CZ · 5MM · PAVÉ HALOS · RHODIUM · WATERPROOF",cta="SHOP THE BRACELET →",claims=[("B00681C","5mm")],**COMMON),
 dict(id="R3",file="velvet",head="CLOAK<em>ROOM.</em>",sub="(hand this in at the end of the night. or don't.)",dev="ticket",tk="the red room · cloakroom",tn="1,299",tm="redeem for: one heartbead bracelet",tr="keep this ticket",
      skus=["YF5215"],spec="6MM MIRROR STEEL · GOLD TOGGLE · ONE GOLD HEART",cta="SHOP THE BRACELET →",claims=[("YF5215","6mm")],**COMMON),
 dict(id="R4",file="pour",head="THE <em>LIST.</em>",sub="(by the glass. no vintage, no tannin, no tarnish.)",dev="list",
      rows=[("toggle link chain","₹1,499"),("body","12g"),("length","50cm, 4mm"),("nose","none"),("finish","non tarnish"),("served","at the front or the side")],
      skus=["YF5143"],spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM · 18K PVD",cta="SHOP THE CHAIN →",claims=[("YF5143","12g · 50cm · 4mm · 15mm")],**COMMON),
 dict(id="R5",file="glass",head="RED <em>LIGHT.</em>",sub="(from the contact sheet. frame seven, print this one.)",dev="sheet",
      frames=[("F5","20% 50%"),("F6","40% 50%"),("F7","50% 50%"),("F8","60% 50%"),("F9","80% 50%")],circle=(540,120),lab="contact · 27 sep 2026 · safelight",
      skus=["E14776S"],spec="BRUSHED SATIN HUGGIES · 12MM · 6MM DEEP · 18K",cta="SHOP THE HUGGIES →",claims=[("E14776S","12mm · 6mm")],**COMMON),
]
