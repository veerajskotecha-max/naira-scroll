# -*- coding: utf-8 -*-
"""SET 11 — SUGARPLAY, RE-DRESSED. Five verified Sugarplay plates with overlays that play: a sweet-shop ticket, a
screenplay page, conversation hearts, a chalk hopscotch, a paper fortune teller. Every figure is the listing's."""
from core import *
import re
SET=dict(slug="11-sugarplay",title="Sugarplay",n=5)
S11=f"{ROOT}/s11"
TOK={"feed":dict(PLATE="760px",HEAD="132px",DEV="330px"),"story":dict(PLATE="1200px",HEAD="156px",DEV="400px")}
CSS="""
.ad{background:var(--bg)}
.plate{position:absolute;left:0;right:0;top:0;height:var(--PLATE);overflow:hidden;background:#f6e6dc}
.plate img{width:100%;height:100%;object-fit:cover;display:block}
.block{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--PLATE) + 22px)}
.h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.92;letter-spacing:.005em;text-transform:uppercase;white-space:nowrap}
.h em{font-style:normal;color:var(--ac)}
.sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:4px;text-wrap:pretty;max-width:36ch}
.dev{position:relative;height:var(--DEV);margin-top:12px}
.foot{grid-template-columns:1fr auto}
/* S1 candy stripe + stickers */
.stripe{position:absolute;left:calc(-1 * var(--pad));right:calc(-1 * var(--pad));top:0;height:54px;background:repeating-linear-gradient(-45deg,var(--ac) 0 22px,var(--bg) 22px 44px);opacity:.9}
.stripe span{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--bg);padding:6px 22px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.2em;text-transform:uppercase}
.stk{position:absolute;width:172px;height:172px;border-radius:50%;background:var(--ac);color:var(--bg);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:'Jost';font-weight:600;letter-spacing:.04em;transform:rotate(-8deg);box-shadow:0 6px 14px rgba(27,21,18,.15)}
.stk.ivory{background:var(--ink);color:var(--bg)}
.stk.line{background:transparent;color:var(--ink);border:1.5px solid var(--ink);transform:rotate(6deg)}
.stk b{font-size:38px;line-height:1}
.stk small{font-family:'JetBrains Mono';font-weight:400;font-size:12px;letter-spacing:.14em;margin-top:6px}
/* S2 screenplay */
.script{font-family:'JetBrains Mono';font-size:calc(var(--MONO)*1.2);letter-spacing:.02em;line-height:1.5;color:var(--ink);max-width:640px}
.script .who{text-align:center;text-transform:uppercase;letter-spacing:.22em;margin-top:10px;color:var(--ac)}
.script .par{text-align:center;font-style:italic;font-family:'Cormorant Garamond';font-size:calc(var(--MONO)*1.3);color:var(--mute)}
.script .say{padding:0 60px;font-size:calc(var(--MONO)*1.32)}
.script .slug{letter-spacing:.18em;text-transform:uppercase;border-bottom:1px solid var(--ink);padding-bottom:6px;margin-bottom:4px}
/* S3 hearts */
.heart{position:absolute;width:215px;height:192px;isolation:isolate;display:flex;align-items:center;justify-content:center;text-align:center;font-family:'JetBrains Mono';font-size:14px;letter-spacing:.12em;text-transform:uppercase;line-height:1.35;padding:0 30px;color:rgba(27,21,18,.78)}
.heart svg{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.heart span{position:relative;z-index:1}
/* S4 hopscotch */
.hop{position:absolute;inset:0}
/* S5 fortune */
.fort{position:absolute;inset:0}
"""
def heart_svg(fill): return f'<svg viewBox="0 0 190 170"><path d="M95 160 C 20 105, 0 70, 0 45 C 0 18, 24 2, 50 2 C 72 2, 88 16, 95 30 C 102 16, 118 2, 140 2 C 166 2, 190 18, 190 45 C 190 70, 170 105, 95 160 Z" fill="{fill}" stroke="#6E1E2A" stroke-width="1.2" stroke-opacity=".35"/></svg>'
def hop_svg(c,fmt):
    W=FORMATS[fmt][0]; w=W-2*(52 if fmt=="feed" else 64); h=int(TOK[fmt]["DEV"].replace("px",""))
    sq=int(min(h/3.4,w/6.2)); g=10; out=[]; x0=0; y=int((h-sq*3-2*g)/2)
    # classic hopscotch laid sideways: 1,2 | 3 | 4,5 | 6 | 7,8 (6-7-8 in oxblood = the sizes)
    cols=[[1,2],[3],[4,5],[6],[7,8]]
    for col in cols:
        n=len(col); tot=n*sq+(n-1)*g; yy=int((h-tot)/2)
        for k in col:
            hot=k in (6,7,8)
            out.append(f'<rect x="{x0}" y="{yy}" width="{sq}" height="{sq}" fill="{"#6E1E2A" if hot else "none"}" stroke="{"#6E1E2A" if hot else "#1B1512"}" stroke-width="2" stroke-dasharray="{"none" if hot else "6 5"}"/>'
                       f'<text x="{x0+sq/2:.0f}" y="{yy+sq*0.68:.0f}" text-anchor="middle" font-family="Velista" font-size="{int(sq*0.62)}" fill="{"#F1EBE1" if hot else "#1B1512"}">{k}</text>')
            yy+=sq+g
        x0+=sq+g*2
    out.append(f'<text x="{x0+10}" y="{h/2+6:.0f}" font-family="JetBrains Mono" font-size="14" letter-spacing="2" fill="#6E1E2A">US 6 · 7 · 8</text>')
    return f'<svg class="hop" viewBox="0 0 {w} {h}">{"".join(out)}</svg>'
def fort_svg(c,fmt):
    W=FORMATS[fmt][0]; w=W-2*(52 if fmt=="feed" else 64); h=int(TOK[fmt]["DEV"].replace("px",""))
    s=min(h,w*0.6); cx=w/2; cy=h/2; r=s/2
    flaps=c["flaps"]; out=[]
    pts=[((cx,cy-r),(cx+r,cy)),((cx+r,cy),(cx,cy+r)),((cx,cy+r),(cx-r,cy)),((cx-r,cy),(cx,cy-r))]
    cols=["#F2C4BD","#F1EBE1","#F2C4BD","#F1EBE1"]
    for i,((ax,ay),(bx,by)) in enumerate(pts):
        out.append(f'<polygon points="{cx:.0f},{cy:.0f} {ax:.0f},{ay:.0f} {bx:.0f},{by:.0f}" fill="{cols[i]}" stroke="#1B1512" stroke-width="1.5"/>')
        mx=(cx+ax+bx)/3; my=(cy+ay+by)/3; mx=cx+(mx-cx)*1.35; my=cy+(my-cy)*1.35
        out.append(f'<text x="{mx:.0f}" y="{my+5:.0f}" text-anchor="middle" font-family="JetBrains Mono" font-size="17" letter-spacing="1.5" fill="#1B1512">{E(flaps[i])}</text>')
    out.append(f'<line x1="{cx-r:.0f}" y1="{cy:.0f}" x2="{cx+r:.0f}" y2="{cy:.0f}" stroke="#1B1512" stroke-width="1" stroke-dasharray="4 4"/><line x1="{cx:.0f}" y1="{cy-r:.0f}" x2="{cx:.0f}" y2="{cy+r:.0f}" stroke="#1B1512" stroke-width="1" stroke-dasharray="4 4"/>')
    out.append(f'<text x="{cx+r+26:.0f}" y="{cy-10:.0f}" font-family="Cormorant Garamond" font-style="italic" font-size="28" fill="#1B1512">pick a number.</text><text x="{cx+r+26:.0f}" y="{cy+22:.0f}" font-family="Cormorant Garamond" font-style="italic" font-size="28" fill="#6E1E2A">every flap is true.</text>')
    return f'<svg class="fort" viewBox="0 0 {w} {h}">{"".join(out)}</svg>'
def device(c,fmt):
    k=c["dev"]
    if k=="stickers":
        return (f'<div class="stripe"><span>{E(c["band"])}</span></div>'
                f'<div class="stk" style="left:0;top:66px"><b>{E(c["stk"][0][0])}</b><small>{E(c["stk"][0][1])}</small></div>'
                f'<div class="stk line" style="left:200px;top:96px"><b>{E(c["stk"][1][0])}</b><small>{E(c["stk"][1][1])}</small></div>'
                f'<div class="stk ivory" style="left:400px;top:60px"><b>{E(c["stk"][2][0])}</b><small>{E(c["stk"][2][1])}</small></div>'
                f'<div class="stk" style="left:600px;top:100px;transform:rotate(4deg)"><b>{E(c["stk"][3][0])}</b><small>{E(c["stk"][3][1])}</small></div>')
    if k=="script":
        lines="".join(f'<div class="who">{E(w)}</div>'+(f'<div class="par">({E(p)})</div>' if p else '')+f'<div class="say">{E(s)}</div>' for w,p,s in c["script"])
        return f'<div class="script"><div class="slug">{E(c["slug"])}</div>{lines}</div>'
    if k=="hearts":
        pos=[(0,14,"#F2C4BD"),(240,70,"#E8A79E"),(480,4,"#F2C4BD"),(720,74,"#E8A79E")]
        return "".join(f'<div class="heart" style="left:{x}px;top:{y}px">{heart_svg(f)}<span>{E(t)}</span></div>' for (x,y,f),t in zip(pos,c["hearts"]))
    if k=="hop": return hop_svg(c,fmt)
    if k=="fort": return fort_svg(c,fmt)
    return ""
def render(c,fmt):
    plate=f'{S11}/plate_{c["file"]}_{fmt}.jpg'; sku=c["skus"][0]
    W=FORMATS[fmt][0]; pad=52 if fmt=="feed" else 64; plain=re.sub('<[^>]+>','',c['head']); fs=min(int(TOK[fmt]['HEAD'].replace('px','')),int(fit(plain,W-2*pad,0.005)))
    return (f'<div class="plate"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}"></div>'
            f'{top("NAIRA PETITE · SUGARPLAY",IVORY if c.get("dark") else INK,logo=c.get("logo_"+fmt,c.get("logo")))}'
            f'<div class="block"><div class="h" style="font-size:{fs}px">{c["head"]}</div><div class="sub">{E(c["sub"])}</div><div class="dev">{device(c,fmt)}</div></div>'
            f'<div class="foot"><div><div class="name">{name(sku)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sku)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
BG="#F7E9E2"
CREATIVES=[
 dict(id="S1",file="candy",head="PICK <em>’N’</em> MIX.",sub="(a straight line of sweets that never go stale.)",dev="stickers",band="candy counter · by the piece",
      stk=[("5MM","cushion cz"),("×3","aqua · pink · yellow"),("PAVÉ","halo on each"),("₹2,399","the lot")],
      skus=["B00681C"],hero=True,water=True,bg=BG,spec="CUSHION CZ · 5MM · PAVÉ HALOS · RHODIUM · 15–19CM",cta="SHOP THE BRACELET →",render=render,claims=[("B00681C","5mm · 15-19cm")]),
 dict(id="S2",file="call",head="THE BIG <em>CALL.</em>",sub="(overheard, outside, on a very good hair day.)",dev="script",slug="ext. a street — day",tok_feed=dict(PLATE="680px"),tok_story=dict(PLATE="1100px"),
      script=[("her","touching the hoop","Twenty-five millimetres. A braid. No stones."),("you","","And?"),("her","","And that's the whole call.")],
      skus=["E20267O"],hero=True,bg=BG,spec="BRAIDED HOOPS · 25MM · NO STONES · 18K GOLD TONE",cta="SHOP THE HOOPS →",render=render,claims=[("E20267O","25mm")]),
 dict(id="S3",file="sweetheart",head="SWEET<em>HEART.</em>",sub="(say it with the only warm thing on the piece.)",dev="hearts",
      hearts=["6mm steel spheres","one gold heart","gold toggle bar","₹1,299 · yours"],
      skus=["YF5215"],hero=True,bg=BG,spec="6MM MIRROR STEEL · 18K GOLD TONE HEART · TOGGLE",cta="SHOP THE BRACELET →",render=render,claims=[("YF5215","6mm")]),
 dict(id="S4",file="hopscotch",head="HOP TO <em>YOUR SIZE.</em>",sub="(one ring, sizes six to eight. open back, so it adjusts.)",dev="hop",
      skus=["WR12518B"],bg=BG,spec="FOUR BANDS · 2 PAVÉ, 2 PLAIN · US 6–8 ADJUSTABLE · 18K",cta="SHOP THE RING →",render=render,claims=[("WR12518B","6 · 8")]),
 dict(id="S5",file="fortune",head="PICK A <em>NUMBER.</em>",sub="(a paper fortune teller. every flap says something true.)",dev="fort",
      flaps=["15MM WIDE","PEAR-CUT CZ","GOLD CLAWS","₹1,599"],
      skus=["E16075B"],bg=BG,spec="BOW STUDS · 15MM · PEAR-CUT CZ · 18K GOLD TONE",cta="SHOP THE STUDS →",render=render,claims=[("E16075B","15mm")]),
]
