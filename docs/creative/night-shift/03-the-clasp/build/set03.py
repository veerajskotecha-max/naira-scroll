# -*- coding: utf-8 -*-
"""SET 03 — THE CLASP. Five closures drawn up like patent sheets: the mechanism photographed open, numbered
callouts on leader lines, a parts list and one line of action. The closure is the design; nobody photographs it."""
from core import *
SET=dict(slug="03-the-clasp",title="The Clasp",n=3)
S3=f"{ROOT}/s03"
TOK={"feed":dict(FIGH="640px",HEAD="118px",CALL="34px"),"story":dict(FIGH="1010px",HEAD="140px",CALL="38px")}
CSS="""
.sheet{position:absolute;inset:0;background:var(--bg)}
.fig{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--pad) + 52px);height:var(--FIGH);border:1.5px solid var(--ink);overflow:hidden;background:#E9E2D6}
.fig img{width:100%;height:100%;object-fit:cover;display:block}
.fig svg{position:absolute;inset:0;width:100%;height:100%}
.fig .cap{position:absolute;left:0;bottom:0;background:var(--bg);border-top:1.5px solid var(--ink);border-right:1.5px solid var(--ink);padding:8px 14px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.14em;text-transform:uppercase}
.corner{position:absolute;width:18px;height:18px;border-color:var(--ink);border-style:solid;border-width:0}
.title{position:absolute;left:var(--pad);right:var(--pad);top:calc(var(--pad) + 52px + var(--FIGH) + 26px)}
.title .h{font-family:'Velista';font-weight:500;font-size:var(--HEAD);line-height:.9;letter-spacing:-.01em;text-transform:uppercase}
.title .sub{font-family:'Cormorant Garamond';font-style:italic;font-size:var(--ASIDE);margin-top:8px}
.parts{display:grid;grid-template-columns:1fr 1fr;gap:10px 30px;margin-top:18px;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;max-width:640px}
.parts div{display:flex;gap:12px;align-items:center;border-bottom:1px dotted rgba(27,21,18,.35);padding-bottom:6px}
.parts i{display:inline-flex;width:24px;height:24px;border:1.5px solid var(--ink);border-radius:50%;align-items:center;justify-content:center;font-style:normal;font-size:13px;flex:none}
.act{margin-top:16px;font-family:'Jost';font-weight:500;font-size:calc(var(--MONO)*1.35);letter-spacing:.02em;max-width:36ch}
.act b{font-family:'JetBrains Mono';font-weight:500;font-size:var(--MONO);letter-spacing:.12em;color:var(--mute);margin-right:10px}
.foot .see{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-bottom:6px}
"""
def callouts(c,fmt):
    W,H=FORMATS[fmt]; pad=int(TOK.get(fmt,{}).get("pad","0").replace("px","") or (52 if fmt=="feed" else 64))
    fw=W-2*pad; fh=int(TOK[fmt]["FIGH"].replace("px",""))
    pts=c["calls_"+fmt] if "calls_"+fmt in c else c["calls"]
    out=[]
    for n,(tx,ty,lx,ly) in enumerate(pts,1):
        x1,y1=tx*fw,ty*fh; x2,y2=lx*fw,ly*fh
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#1B1512" stroke-width="1.6"/><circle cx="{x1:.0f}" cy="{y1:.0f}" r="4" fill="#1B1512"/>'
                   f'<circle cx="{x2:.0f}" cy="{y2:.0f}" r="17" fill="#F1EBE1" stroke="#1B1512" stroke-width="1.6"/><text x="{x2:.0f}" y="{y2+5:.0f}" text-anchor="middle" font-family="JetBrains Mono" font-size="15" fill="#1B1512">{n}</text>')
    return f'<svg viewBox="0 0 {fw} {fh}">{"".join(out)}</svg>'
def render(c,fmt):
    sk=c["sku"]; plate=f'{S3}/plate_{c["plate"]}_{fmt}.jpg'
    parts="".join(f'<div><i>{i}</i><span>{E(p)}</span></div>' for i,p in enumerate(c["parts"],1))
    return (f'<div class="sheet"></div>{top(f"closures · sheet {c[chr(110)]} of 5",INK)}'
            f'<div class="fig"><img src="{plate}" style="object-position:{c.get("pos","50% 50%")}">{callouts(c,fmt)}<div class="cap">fig. {c["n"]} · {E(c["figcap"])}</div></div>'
            f'<div class="title"><div class="h">{E(c["head"])}</div><div class="sub">{E(c["sub"])}</div><div class="parts">{parts}</div>'
            f'<div class="act"><b>ACTION</b>{E(c["action"])}</div></div>'
            f'<div class="foot"><div><div class="see">on:</div><div class="name">{name(sk)}</div><div class="spec">{E(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sk)}</div><span class="cta solid">{E(c["cta"])}</span></div></div>')
CREATIVES=[
 dict(id="K1",n=1,file="toggle",plate="toggle",sku="YF5143",hero=True,head="Toggle.",sub="(closes with a turn, not a catch.)",figcap="the bar, mid-turn",
      parts=["bar · about 15mm","ring","paperclip link · 4mm","chain · 50cm"],action="pass the bar through the ring and turn it flat. worn at the front, on purpose.",
      calls=[(0.40,0.50,0.22,0.22),(0.31,0.72,0.12,0.88),(0.80,0.58,0.90,0.26),(0.14,0.40,0.06,0.62)],calls_story=[(0.44,0.44,0.24,0.18),(0.33,0.56,0.10,0.84),(0.80,0.52,0.90,0.24),(0.10,0.47,0.08,0.12)],
      spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM",cta="SHOP NECKLACES →",render=render,claims=[("YF5143","bar about 15mm · 4mm · 50cm")]),
 dict(id="K2",n=2,file="fold-over",plate="fold",sku="B00681C",hero=True,head="Fold-over.",sub="(a tongue that clicks into a box.)",figcap="the clasp, open",
      parts=["tongue, hinged","box","cushion cz · 5mm","pavé halo"],action="fold the tongue down over the box until it clicks. it will not open on its own.",
      calls=[(0.30,0.40,0.12,0.18),(0.36,0.60,0.14,0.82),(0.60,0.40,0.80,0.16),(0.66,0.50,0.88,0.72)],
      spec="5MM CUSHION CZ · PAVÉ HALOS · FOLD-OVER CLASP",cta="SHOP BRACELETS →",render=render,claims=[("B00681C","5mm cushion")]),
 dict(id="K3",n=3,file="latch",plate="latch",sku="E20267O",hero=True,head="Latch.",sub="(a post that swings out, a tab that holds it.)",figcap="the hoop, open",
      parts=["post","hinge","flat tab","braided rope · 25mm"],action="swing the post through, close it under the tab. the tab is the lock.",
      calls=[(0.30,0.58,0.12,0.80),(0.44,0.62,0.30,0.86),(0.52,0.30,0.68,0.14),(0.66,0.45,0.88,0.40)],
      spec="25MM · BRAIDED ROPE · NO STONES",cta="SHOP EARRINGS →",render=render,claims=[("E20267O","25mm")]),
 dict(id="K4",n=4,file="snap",plate="snap",sku="E14776S",hero=True,head="Snap.",sub="(a hinge on one side, a snap on the other.)",figcap="the huggie, open",
      parts=["hinge pin","snap post","band · 6mm deep","brushed satin"],action="open on the hinge, close with a snap. it hugs the lobe; that is the name.",
      calls=[(0.42,0.58,0.22,0.84),(0.66,0.62,0.86,0.84),(0.58,0.44,0.80,0.20),(0.40,0.50,0.14,0.16)],
      spec="12MM · 6MM FLAT BAND · BRUSHED SATIN",cta="SHOP EARRINGS →",render=render,claims=[("E14776S","12mm · 6mm")]),
 dict(id="K5",n=5,file="open-back",plate="open",sku="JDR0104337-S",head="Open back.",sub="(no clasp at all. the band is the fitting.)",figcap="the shank, from behind",
      parts=["shank end","gap","shank end","pavé dome · 17mm"],action="ease the ends apart or together to fit. one size that becomes yours.",
      calls=[(0.40,0.60,0.18,0.84),(0.50,0.66,0.50,0.88),(0.60,0.60,0.82,0.84),(0.50,0.30,0.80,0.16)],
      spec="PAVÉ DOME · US 7 OPEN BACK · RHODIUM",cta="SHOP RINGS →",render=render,claims=[("JDR0104337-S","US 7 open back")]),
]
