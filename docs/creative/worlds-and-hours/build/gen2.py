# -*- coding: utf-8 -*-
"""Ten creatives, volume two: themed Higgsfield imagery with typography integrated into the picture.
Set C 'Worlds'  — one word, one colour world, the word passes BEHIND the subject (cutout layer).
Set D 'Hours'   — same piece at two hours (split frame, numerals straddling the seam) + one three-hour strip.
Names and prices come from live Shopify data; nothing is typed by hand."""
import json, os, sys, asyncio, html
from PIL import ImageFont
from playwright.async_api import async_playwright

ROOT=os.path.dirname(os.path.abspath(__file__))
H="/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/hist"
ROWS={r["sku"]:r for r in json.load(open(f"{ROOT}/inventory_rows.json"))}
DET=json.load(open(f"{ROOT}/details.json"))
FORMATS={"feed":(1080,1350),"story":(1080,1920)}
VEL=f"{ROOT}/fonts/Velista.ttf"

def rupees(p): return "₹"+f"{int(round(p)):,}"
def name(sku): return html.escape(ROWS[sku]["title"])
def price(sku): return rupees(ROWS[sku]["price"])
def esc(s): return html.escape(s)
def pick(n): return f"{H}/pick/{n:04d}.png"
def cut(n): return f"{H}/cut/{n:04d}.png"
def fit(text,target_px):
    """font-size (px) at which Velista renders `text` `target_px` wide, tracking -0.02em accounted for."""
    f=ImageFont.truetype(VEL,200); w=f.getlength(text)-0.02*200*(len(text)-1)
    return target_px*200/w

IVORY="#F1EBE1"; INK="#1B1512"; OX="#6E1E2A"; BLUSH="#F2C4BD"

CREATIVES=[
 # ---------------- SET C — WORLDS
 dict(id="C1",set="C",kind="world",sku="YF5215",bg=677,cutout=677,word="HEART.",
      aside="(steel beads. one gold heart. survives the shower.)",
      spec="6MM POLISHED STEEL SPHERES · GOLD TOGGLE · 15MM HEART",
      wordcolor=IVORY,ink=IVORY,scrim="dark",pos="50% 50%",wordy=0.098,bleed=1.06,cta="SHOP BRACELETS →",logo="ivory",wordy_story=0.076),
 dict(id="C2",set="C",kind="world",sku="B00681C",bg=699,cutout=699,word="LIGHT.",
      aside="(pastel cz, rhodium over steel. the bracelet is the prism.)",
      spec="5MM CUSHION CZ · PAVÉ HALOS · FOLD-OVER CLASP",
      wordcolor=INK,ink=INK,scrim="light",pos="50% 50%",wordy=0.40,bleed=1.06,cta="SHOP BRACELETS →",logo="ink",fill=f"{H}/pick/0699_fill.jpg"),
 dict(id="C3",set="C",kind="world",sku="E20267O",bg=1041,cutout=1041,word="LOUD.",
      aside="(25mm of braided gold. no stones. no apology.)",
      spec="25MM · BRAIDED ROPE · 18K GOLD TONE · NO STONES",
      wordcolor=OX,ink=INK,scrim="light",pos="50% 62%",wordy=0.22,bleed=1.04,cta="SHOP EARRINGS →",logo="ink",
      pos_story="50% 55%"),
 dict(id="C4",set="C",kind="world",sku="E14776S",bg=1517,cutout=1517,word="QUIET.",
      aside="(12mm. brushed satin. nothing else.)",
      spec="12MM HUGGIE · 6MM FLAT BAND · BRUSHED SATIN · NO STONES",
      wordcolor="rgba(241,235,225,.44)",ink=IVORY,scrim="none",pos="50% 42%",wordy=0.30,bleed=1.06,cta="SHOP EARRINGS →",logo="ivory"),
 dict(id="C5",set="C",kind="world",sku="YF5143",bg=630,cutout=630,word="LINK.",
      aside="(4mm paperclip. toggle bar through ring. fifty centimetres.)",
      spec="4MM PAPERCLIP · 50CM · TOGGLE 15MM · 12G",
      wordcolor="#B9746B",ink=INK,scrim="light",pos="50% 50%",wordy=0.33,bleed=1.02,cta="SHOP NECKLACES →",logo="ink",rot=-24,rotw=1.10),
 # ---------------- SET D — HOURS
 dict(id="D1",set="D",kind="hours",sku="YF5215",top=(2464,"10:00","DESK","50% 42%"),bot=(693,"22:00","BAR","50% 55%"),
      line="SAME BRACELET. DIFFERENT HOUR.",cta="SHOP BRACELETS →",cols=(INK,IVORY)),
 dict(id="D2",set="D",kind="hours",sku="YF5143",top=(709,"07:30","AFTER THE RUN","50% 52%"),bot=(963,"20:00","DINNER","50% 42%"),
      line="SAME CHAIN. DIFFERENT HOUR.",cta="SHOP NECKLACES →",cols=(IVORY,INK)),
 dict(id="D3",set="D",kind="hours",sku="B00681C",top=(2219,"11:00","BRUNCH","50% 45%"),bot=(1045,"23:00","ICE","50% 48%"),
      line="SAME BRACELET. DIFFERENT HOUR.",cta="SHOP BRACELETS →",cols=(INK,IVORY)),
 dict(id="D4",set="D",kind="hours",sku="E20267O",top=(1023,"07:15","MIRROR","50% 22%"),bot=(1536,"23:30","LAST DRINK","50% 45%"),
      line="SAME HOOPS. DIFFERENT HOUR.",cta="SHOP EARRINGS →",cols=(INK,IVORY)),
 dict(id="D5",set="D",kind="day",cta="SHOP THE DAY →",line="ONE DAY. SIX PIECES.",
      frames=[(1017,"06:40","SILENCE THE PHONE","40% 50%",["WR12518B","YF8156"]),
              (1030,"10:15","LAPTOP","45% 40%",["WR10170K7","YF5214"]),
              (1024,"17:00","RAIN","38% 50%",["B00681C","JDE0201327"])]),
]

CSS="""
@font-face{font-family:'Velista';src:url('FONTS/Velista.ttf') format('truetype');font-weight:400 600;}
FONTFACES
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:WIDTHpx;height:HEIGHTpx;overflow:hidden;background:#000}
body{font-family:'Jost',sans-serif;-webkit-font-smoothing:antialiased}
.ad{position:relative;width:WIDTHpx;height:HEIGHTpx;overflow:hidden;background:#111}
.ad img.layer{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.word{position:absolute;left:50%;transform:translateX(-50%);font-family:'Velista';font-weight:500;line-height:.85;letter-spacing:-.02em;white-space:nowrap;text-transform:uppercase}
.scrim{position:absolute;left:0;right:0;bottom:0;height:34%;pointer-events:none}
.scrim.dark{background:linear-gradient(0deg,rgba(20,10,8,.62) 0%,rgba(20,10,8,.28) 55%,rgba(20,10,8,0) 100%)}
.scrim.light{background:linear-gradient(0deg,rgba(241,235,225,.78) 0%,rgba(241,235,225,.35) 55%,rgba(241,235,225,0) 100%)}
.top{position:absolute;left:var(--pad);right:var(--pad);top:var(--pad);display:flex;justify-content:space-between;align-items:center}
.top img{height:24px}
.lab{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.14em;text-transform:uppercase;opacity:.85}
.foot{position:absolute;left:var(--pad);right:var(--pad);bottom:var(--pad);display:grid;grid-template-columns:1fr auto;gap:18px 28px;align-items:end}
.name{font-family:'Jost';font-weight:600;font-size:var(--NAME);letter-spacing:.06em;text-transform:uppercase;line-height:1.05}
.spec{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;line-height:1.4;margin-top:8px;opacity:.9}
.aside{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--ASIDE);line-height:1.12;margin-bottom:14px;max-width:34ch}
.price{font-family:'Jost';font-weight:600;font-size:var(--PRICE);letter-spacing:.01em;white-space:nowrap;text-align:right}
.cta{display:inline-block;border:2px solid currentColor;font-family:'Jost';font-weight:600;font-size:var(--CTA);letter-spacing:.14em;text-transform:uppercase;padding:calc(var(--CTA)*.7) calc(var(--CTA)*1.4);white-space:nowrap;margin-top:14px}
/* hours */
.half{position:absolute;left:0;right:0;overflow:hidden}
.half img{width:100%;height:100%;object-fit:cover;display:block}
.seam{position:absolute;left:0;right:0;height:6px;background:#F1EBE1}
.num{position:absolute;font-family:'Velista';font-weight:500;font-size:var(--NUM);line-height:1;letter-spacing:-.01em;white-space:nowrap}
.num.a{color:#F1EBE1}.num.b{color:#1B1512}
.tag{position:absolute;font-family:'JetBrains Mono';font-size:calc(var(--MONO)*1.1);letter-spacing:.16em;text-transform:uppercase;font-weight:500}
.hscrim{position:absolute;left:0;right:0;pointer-events:none}
/* day */
.strip{position:absolute;left:var(--pad);right:var(--pad);display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.fr{position:relative;overflow:hidden;background:#222}
.fr img{width:100%;height:100%;object-fit:cover;display:block}
.fr .t{position:absolute;left:14px;top:12px;font-family:'Velista';font-weight:500;font-size:var(--DAYNUM);line-height:1;color:#F1EBE1;text-shadow:0 1px 14px rgba(0,0,0,.35)}
.fr .s{position:absolute;left:14px;bottom:12px;font-family:'JetBrains Mono';font-size:calc(var(--MONO)*.9);letter-spacing:.12em;text-transform:uppercase;color:#F1EBE1;text-shadow:0 1px 10px rgba(0,0,0,.5)}
.list{position:absolute;left:var(--pad);right:var(--pad);display:grid;grid-template-columns:1fr auto;gap:8px 24px;font-family:'Jost';color:#F1EBE1}
.list .n{font-weight:600;font-size:var(--NAME);letter-spacing:.06em;text-transform:uppercase}
.list .m{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;opacity:.8;margin-top:2px}
.list .p{font-weight:600;font-size:var(--NAME);text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.list .tot{border-top:1px solid rgba(241,235,225,.35);padding-top:12px;margin-top:6px}
"""
TOK={"feed":dict(pad="52px",NAME="24px",MONO="15px",ASIDE="30px",PRICE="34px",CTA="20px",NUM="150px",DAYNUM="46px"),
     "story":dict(pad="64px",NAME="28px",MONO="18px",ASIDE="36px",PRICE="40px",CTA="24px",NUM="176px",DAYNUM="54px")}

def fontfaces():
    out=[]
    for f in ["Inter.local.css","JetBrains_Mono.local.css","Cormorant_Garamond.local.css","Jost.local.css"]:
        out.append(open(f"{ROOT}/fonts/{f}").read().replace("url(","url(FONTS/"))
    return "\n".join(out)

def top(c,color,label):
    logo="logo_ivory.png" if color==IVORY else "logo_ink.png"
    return f'<div class="top" style="color:{color}"><img src="{ROOT}/{logo}"><span class="lab">{label}</span></div>'

def world(c,fmt):
    W,H=FORMATS[fmt]; pos=c.get("pos_story",c["pos"]) if fmt=="story" else c["pos"]
    rot=c.get("rot",0)
    target=W*c["bleed"] if not rot else W*c.get("rotw",1.25)
    fs=fit(c["word"],target)
    wy=int(H*(c.get("wordy_story",c["wordy"]) if fmt=="story" else c["wordy"]))
    tr=f"translateX(-50%) rotate({rot}deg)" if rot else "translateX(-50%)"
    sk=c["sku"]
    scrim=f'<div class="scrim {c["scrim"]}"></div>' if c["scrim"]!="none" else ""
    word=(f'<div class="word" style="top:{wy}px;font-size:{fs:.0f}px;color:transparent;background:url({c["fill"]}) center/cover fixed;-webkit-background-clip:text;background-clip:text;transform:{tr}">{esc(c["word"])}</div>' if c.get("fill") else
          f'<div class="word" style="top:{wy}px;font-size:{fs:.0f}px;color:{c["wordcolor"]};transform:{tr}">{esc(c["word"])}</div>')
    return (f'<img class="layer" src="{pick(c["bg"])}" style="object-position:{pos}">'
            f'{word}'
            f'<img class="layer" src="{cut(c["cutout"])}" style="object-position:{pos}">'
            f'{scrim}'
            f'{top(c,c["ink"],"NAIRA PETITE · WORLDS")}'
            f'<div class="foot" style="color:{c["ink"]}"><div><div class="aside">{esc(c["aside"])}</div><div class="name">{name(sk)}</div><div class="spec">{esc(c["spec"])}</div></div>'
            f'<div><div class="price">{price(sk)}</div><span class="cta">{esc(c["cta"])}</span></div></div>')

def hours(c,fmt):
    W,H=FORMATS[fmt]; tk=TOK[fmt]; mid=H//2
    (ti,tn,tt,tp),(bi,bn,bt,bp)=c["top"],c["bot"]; sk=c["sku"]
    ca,cb=c.get("cols",(IVORY,IVORY))
    num=int(tk["NUM"].replace("px",""))
    # numerals straddle the seam; each is drawn twice and clipped at the seam so the colour flips across it
    def split(text,left):
        style=f"left:{tk['pad']}" if left else f"right:{tk['pad']}"
        y=mid-int(num*0.44)
        a=f'<div class="num a" style="{style};top:{y}px;clip-path:inset(0 0 {num-(mid-y)}px 0);color:{ca}">{text}</div>'
        b=f'<div class="num b" style="{style};top:{y}px;clip-path:inset({mid-y}px 0 0 0);color:{cb}">{text}</div>'
        return a+b
    return (f'<div class="half" style="top:0;height:{mid}px"><img src="{pick(ti)}" style="object-position:{tp}"></div>'
            f'<div class="half" style="top:{mid}px;height:{H-mid}px"><img src="{pick(bi)}" style="object-position:{bp}"></div>'
            f'<div class="hscrim" style="top:0;height:26%;background:linear-gradient(180deg,rgba(20,10,8,.45),rgba(20,10,8,0))"></div>'
            f'<div class="hscrim" style="bottom:0;height:30%;background:linear-gradient(0deg,rgba(20,10,8,.62),rgba(20,10,8,0))"></div>'
            f'<div class="seam" style="top:{mid-3}px"></div>'
            f'{split(tn,True)}{split(bn,False)}'
            f'<div class="tag" style="left:{tk["pad"]};top:{mid-int(num*0.44)-34}px;color:{ca}">{esc(tt)}</div>'
            f'<div class="tag" style="right:{tk["pad"]};top:{mid+int(num*0.56)+12}px;color:{cb};text-align:right">{esc(bt)}</div>'
            f'{top(c,IVORY,"NAIRA PETITE · HOURS")}'
            f'<div class="foot" style="color:{IVORY}"><div><div class="aside">{esc(c["line"].lower().replace("same","(same").replace("hour.","hour.)"))}</div><div class="name">{name(sk)}</div><div class="spec">{esc(DET[sk]["details"].get("plating","")).upper()} · {esc(DET[sk]["details"].get("material","")).upper()}</div></div>'
            f'<div><div class="price">{price(sk)}</div><span class="cta">{esc(c["cta"])}</span></div></div>')

SHORT={"WR12518B":"OPEN BACK · US 6–8 · 2 PAVÉ + 2 PLAIN BANDS","YF8156":"1.2MM CABLE · 2 HEART-CUT CZ · 16–19CM",
       "B00681C":"RHODIUM · 5MM CUSHION CZ · PAVÉ HALOS","JDE0201327":"3 PAIRS · HUGGIE 10.2MM · CLOVER 8.5MM","YF5214":"18K GOLD TONE · ENGRAVED STARS · ONE CZ EACH","WR10170K7":"RHODIUM · 8MM ROUND BRILLIANT · CUSHION HALO"}
def day(c,fmt):
    W,H=FORMATS[fmt]; tk=TOK[fmt]; pad=int(tk["pad"].replace("px",""))
    fh = 640 if fmt=="feed" else 1040
    frs="".join(f'<div class="fr" style="height:{fh}px"><img src="{pick(n)}" style="object-position:{p}"><div class="t">{t}</div><div class="s">{esc(s)}</div></div>' for n,t,s,p,_ in c["frames"])
    seen=[]; 
    for *_,skus in c["frames"]:
        for s in skus:
            if s not in seen: seen.append(s)
    tot=sum(ROWS[s]["price"] for s in seen)
    rows="".join(f'<div><div class="n">{name(s)}</div><div class="m">{s} · {esc(SHORT.get(s,""))}</div></div><div class="p">{price(s)}</div>' for s in seen)
    top_y=pad+60
    return (f'<div style="position:absolute;inset:0;background:#1B1512"></div>'
            f'{top(c,IVORY,"NAIRA PETITE · HOURS")}'
            f'<div class="strip" style="top:{top_y}px">{frs}</div>'
            f'<div class="list" style="top:{top_y+fh+34}px">{rows}<div class="tot"><div class="n">{esc(c["line"])}</div></div><div class="p tot">{rupees(tot)}</div></div>'
            f'<div class="foot" style="color:{IVORY};grid-template-columns:1fr auto"><div class="aside">(a stack, priced. every piece in stock today.)</div><span class="cta">{esc(c["cta"])}</span></div>')

def page(c,fmt):
    W,H=FORMATS[fmt]; tk=TOK[fmt]
    css=CSS.replace("WIDTH",str(W)).replace("HEIGHT",str(H)).replace("FONTFACES",fontfaces()).replace("FONTS/",f"{ROOT}/fonts/")
    css=":root{"+";".join(f"--{k}:{v}" for k,v in tk.items())+"}\n"+css
    body={"world":world,"hours":hours,"day":day}[c["kind"]](c,fmt)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="ad">{body}</div></body></html>'

def verify():
    bad=[]
    for c in CREATIVES:
        skus=[c["sku"]] if "sku" in c else [s for f in c["frames"] for s in f[4]]
        hero = c["kind"] in ("world","hours")
        for s in skus:
            r=ROWS.get(s)
            if not r: bad.append((c["id"],s,"NOT ACTIVE")); continue
            if r["inv"]<=0 or not r["avail"]: bad.append((c["id"],s,"OUT OF STOCK"))
            elif hero and r["inv"]<13: bad.append((c["id"],s,f"HERO WITH ONLY {r['inv']} UNITS"))
            elif r["inv"]<3: bad.append((c["id"],s,f"ONLY {r['inv']} UNITS"))
    return bad

async def render(only=None,fmts=("feed","story")):
    os.makedirs(f"{ROOT}/out2",exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args=["--no-sandbox"])
        for c in CREATIVES:
            if only and c["id"] not in only: continue
            for fmt in fmts:
                W,H=FORMATS[fmt]; fn=f"{ROOT}/out2/{c['id']}_{fmt}.html"; open(fn,"w").write(page(c,fmt))
                pg=await b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
                await pg.goto("file://"+fn); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
                await pg.screenshot(path=f"{ROOT}/out2/{c['id']}_{fmt}.png"); await pg.close()
                print(f"{c['id']}_{fmt} ok")
        await b.close()

if __name__=="__main__":
    bad=verify(); print("stock gate:","PASS" if not bad else bad)
    only=sys.argv[1].split(",") if len(sys.argv)>1 and sys.argv[1] else None
    fmts=tuple(sys.argv[2].split(",")) if len(sys.argv)>2 else ("feed","story")
    asyncio.run(render(only,fmts))
