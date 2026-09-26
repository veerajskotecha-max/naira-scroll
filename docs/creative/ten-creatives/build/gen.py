# -*- coding: utf-8 -*-
"""Ten creatives, two sets, two formats. Names and prices come from live Shopify data; nothing is typed by hand."""
import json, os, sys, asyncio, html
from playwright.async_api import async_playwright

ROOT=os.path.dirname(os.path.abspath(__file__))
ROWS={r["sku"]:r for r in json.load(open(f"{ROOT}/inventory_rows.json"))}
DET=json.load(open(f"{ROOT}/details.json"))
CUT=json.load(open(f"{ROOT}/cut/info.json"))
FRAMES="/home/user/naira-scroll/docs/creative/frames"
KEEP="/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/keep"
FORMATS={"feed":(1080,1350),"story":(1080,1920)}
PX_PER_MM=1080/68.0   # 1:1 on a 68mm-wide display (most 6.5-6.7in phones); a 6.1in iPhone is 65mm

def rupees(p): return "₹"+f"{int(round(p)):,}"
def name(sku): return html.escape(ROWS[sku]["title"])
def price(sku): return rupees(ROWS[sku]["price"])
def esc(s): return html.escape(s)

# ---------------------------------------------------------------- the ten
CREATIVES=[
 dict(id="A1",set="A",kind="grid",h1="STEEL.",h2="NOT SILVER.",
      aside="(surgical grade, rhodium plated. that's why it survives the shower.)",
      cta="SHOP THE STEEL →", tok_feed=dict(HL="90px",ASIDE="27px",GGAP="20px",NAME="19px",PRICE="25px",MONO="13px",GAP3="18px"), tok_story=dict(NAME="23px",PRICE="30px",MONO="16px"), gridw="700px",
      items=[("B00681C","WRIST","RHODIUM · 5MM CUSHION CZ"),
             ("YF5215","WRIST","6MM STEEL SPHERES · GOLD TOGGLE"),
             ("WR23569K8","FINGER","RHODIUM · 8×6MM OVAL · US 7"),
             ("E20997C","EAR","RHODIUM · 9MM SHELL PEARL")]),
 dict(id="A2",set="A",kind="actual",h1="ACTUAL SIZE.",h2="HOLD IT UP.",
      aside="(1:1 on a 6.6-inch phone. three hoops, to the millimetre.)",
      cta="SHOP EARRINGS →", tok_feed=dict(NAME="20px",PRICE="26px",MONO="14px",AGAP="30px"), tok_story=dict(PAD="58px",AGAP="26px",NAME="24px",MONO="17px"),
      items=[("E14776S","12MM · BRUSHED SATIN · NO STONES"),("WE14387B","20MM · BAGUETTE CHANNEL SET"),("E20267O","25MM · BRAIDED · NO STONES")]),
 dict(id="A3",set="A",kind="spec",h1="THE SPEC.",h2="ALL OF IT.",
      aside="(read it like a watch. every number is from the listing.)",
      cta="SHOP NECKLACES →", sku="YF5143", tok_feed=dict(MONO="18px",NAME="26px",PRICE="34px",SPECIMG="520px"), tok_story=dict(MONO="20px",NAME="30px",PRICE="40px",SPECIMG="520px"),
      spec=[("CHAIN","4MM PAPERCLIP LINK"),("LENGTH","50CM"),("CLOSURE","TOGGLE BAR THROUGH RING · 15MM"),
            ("WEIGHT","12G"),("PLATING","18K PVD GOLD TONE"),("METAL","SURGICAL STAINLESS STEEL"),
            ("STONES","NONE"),("FINISH","NON TARNISH")],
      care=[("SHOWER",True),("SWIM",True),("SWEAT",True),("SLEEP",True),("PERFUME",False)]),
 dict(id="A4",set="A",kind="plain",h1="SWEAT",h2="IN IT.",
      aside="(then wear it to dinner. surgical steel, 18k pvd gold.)",
      cta="SHOP NECKLACES →", sku="YF5143", image=f"{KEEP}/K7b.png", pos="50% 60%", light=True),
 dict(id="A5",set="A",kind="plain",h1="GOLD",h2="THAT STAYS.",
      aside="(18k gold tone over surgical steel. tarnish free, water fine.)",
      cta="SHOP EARRINGS →", sku="E20267O", image=f"{FRAMES}/04-on-indian-skin.jpg", pos="60% 50%", light=True),
 dict(id="B1",set="B",kind="list",h1="WHAT I WEAR",h2="TO THE SANGEET.",aside="(all sparkle.)",
      cta="SHOP THIS LOOK →", tok_feed=dict(THUMB="186px",RGAP="20px",MONO="15px"), tok_story=dict(HL="108px"),
      items=[("YF3952","NECK","HEART-CUT CZ STATIONS · PAPERCLIP"),
             ("WE14387B","EAR","20MM · BAGUETTE CHANNEL SET"),
             ("YF3925","WRIST","BAROQUE SHELL PEARL · GOLD TOGGLE"),
             ("JDR0303312-7","FINGER","DOUBLE-V PAVÉ · US 7")]),
 dict(id="B2",set="B",kind="list",h1="WHAT I WEAR",h2="TO WORK.",aside="(all quiet.)",
      cta="SHOP THIS LOOK →", tok_feed=dict(THUMB="186px",RGAP="20px",MONO="15px"),
      items=[("E14776S","EAR","12MM · BRUSHED SATIN · NO STONES"),
             ("YF5143","NECK","4MM PAPERCLIP · 50CM · TOGGLE"),
             ("YF5215","WRIST","6MM STEEL SPHERES · GOLD HEART"),
             ("YF5214","FINGER","ENGRAVED STARS · ONE CZ EACH")]),
 dict(id="B3",set="B",kind="receipt",h1="WHAT I WEAR",h2="ON ONE HAND.",
      aside="(three rings. no occasion required.)",
      cta="SHOP RINGS →", tok_feed=dict(MONO="18px"), tok_story=dict(MONO="22px"),
      items=[("WR12518B","US 6–8 · OPEN BACK"),("JDR0303312-7","US 7 · FIXED"),("WR23569K8","US 7 · FIXED")]),
 dict(id="B4",set="B",kind="card",h1="WHAT I WEAR",h2="TO THE AIRPORT.",aside="(one chain. that's it.)",
      cta="SHOP NECKLACES →", sku="YF5143", image=f"{ROOT}/prod/YF5143_0.jpg", pos="50% 30%", tok_story=dict(HL="108px",CARDH="1120px")),
 dict(id="B5",set="B",kind="card",h1="WHAT I WEAR",h2="TO BRUNCH.",aside="(the loud one.)",
      cta="SHOP BRACELETS →", sku="B00681C", image=f"{ROOT}/prod/B00681C_0.jpg", pos="50% 78%", tok_story=dict(CARDH="1120px"), zoom_story="transform:scale(1.28);transform-origin:35% 72%"),
]

# ---------------------------------------------------------------- css
CSS="""
@font-face{font-family:'Velista';src:url('FONTS/Velista.ttf') format('truetype');font-weight:400 600;}
FONTFACES
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:WIDTHpx;height:HEIGHTpx;overflow:hidden}
body{background:var(--bg);color:var(--ink);font-family:'Jost',sans-serif;-webkit-font-smoothing:antialiased}
:root{
 --bg:#F1EBE1;--ink:#1B1512;--ac:#6E1E2A;--mute:#7A6E66;--hair:rgba(27,21,18,.22);--tile:#F1EBE1;
 --pad:var(--PAD);
}
body.night{--bg:#2A0D14;--ink:#F1EBE1;--ac:#F2C4BD;--mute:#C9AEB0;--hair:rgba(241,235,225,.28);--tile:#F1EBE1}
.ad{position:relative;width:WIDTHpx;height:HEIGHTpx;padding:var(--pad);display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;height:36px;margin-bottom:var(--GAP1)}
.top img{height:26px}
.top .setlab{font-family:'JetBrains Mono';font-size:16px;letter-spacing:.14em;color:var(--mute)}
h1{font-family:'Velista';font-weight:500;font-size:var(--HL);line-height:.92;letter-spacing:-.005em;text-transform:uppercase}
h1 .ac{color:var(--ac)}
.aside{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--ASIDE);line-height:1.15;margin-top:var(--GAP2);color:var(--ink);max-width:92%}
.body{flex:1;display:flex;flex-direction:column;justify-content:center}
.foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:var(--GAP3)}
.cta{display:inline-block;background:var(--ac);color:var(--bg);font-family:'Jost';font-weight:600;font-size:var(--CTA);letter-spacing:.14em;text-transform:uppercase;padding:calc(var(--CTA)*.85) calc(var(--CTA)*1.8);white-space:nowrap}
body.night .cta{color:#2A0D14}
.fn{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);text-align:right;line-height:1.5}
.mono{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;color:var(--mute);line-height:1.35}
.name{font-family:'Jost';font-weight:600;font-size:var(--NAME);letter-spacing:.06em;text-transform:uppercase;line-height:1.1}
.price{font-family:'Jost';font-weight:600;font-size:var(--PRICE);letter-spacing:.01em;white-space:nowrap}
/* grid */
.grid{display:grid;grid-template-columns:1fr 1fr;gap:var(--GGAP) var(--GGAP);width:100%}
.cell .tile{width:100%;aspect-ratio:1/1;background:var(--tile);overflow:hidden}
.cell .tile img{width:100%;height:100%;object-fit:cover;display:block}
.cell .cap{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-top:14px}
.cell .mono{margin-top:4px}
/* list */
.rows{display:flex;flex-direction:column;gap:var(--RGAP)}
.row{display:grid;grid-template-columns:var(--THUMB) 1fr auto;gap:0 28px;align-items:center}
.row .thumb{width:var(--THUMB);height:var(--THUMB);background:var(--tile);overflow:hidden}
.row .thumb img{width:100%;height:100%;object-fit:cover;display:block}
.row .mid .mono{margin-bottom:8px}
.row .mid .name{display:flex;align-items:center;gap:16px}
.chk{display:inline-block;width:.9em;height:.9em;border:2px solid var(--ac);position:relative;flex:none}
.chk:after{content:'';position:absolute;left:28%;top:6%;width:26%;height:56%;border:solid var(--ac);border-width:0 2px 2px 0;transform:rotate(45deg)}
.row .price{text-align:right}
.total{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--hair);padding-top:16px;margin-top:6px}
/* receipt */
.rrow3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--GGAP)}
.rrow3 .tile{aspect-ratio:1/1;background:var(--tile);overflow:hidden}
.rrow3 .tile img{width:100%;height:100%;object-fit:cover;display:block}
.receipt{background:var(--tile);color:#1B1512;padding:34px 40px;margin-top:var(--GGAP);font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase}
.receipt .l{display:flex;justify-content:space-between;gap:16px;padding:9px 0;border-bottom:1px dashed rgba(27,21,18,.25)}
.receipt .l span:first-child{color:#1B1512}
.receipt .l small{display:block;color:#7A6E66;font-size:.8em;margin-top:3px;letter-spacing:.06em}
.receipt .tot{display:flex;justify-content:space-between;padding-top:16px;font-family:'Jost';font-weight:600;font-size:calc(var(--PRICE)*1.1);letter-spacing:.06em}
.receipt .hd{display:flex;justify-content:space-between;color:#7A6E66;padding-bottom:10px;border-bottom:1px solid #1B1512;margin-bottom:6px}
/* spec */
.spec{display:grid;grid-template-columns:var(--SPECIMG) 1fr;gap:36px;align-items:start}
.spec .tile{width:var(--SPECIMG);height:var(--SPECIMG);background:var(--tile);overflow:hidden}
.spec .tile img{width:100%;height:100%;object-fit:cover;display:block}
.spec table,.body>table{width:100%;border-collapse:collapse;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase}
.spec td,.body>table td{padding:11px 0;border-bottom:1px solid var(--hair);vertical-align:top;font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase}
.spec td:first-child,.body>table td:first-child{color:var(--mute);width:30%}
.spec .nm{margin-bottom:14px}
.care{display:flex;gap:10px;margin-top:var(--GGAP)}
.care div{flex:1;border:1px solid var(--hair);padding:14px 10px;text-align:center;font-family:'JetBrains Mono';font-size:calc(var(--MONO)*.92);letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}
.care div b{display:block;font-size:1.6em;line-height:1;margin-bottom:8px;color:var(--ink);font-weight:400}
.care div.no b{color:var(--ac)}
/* actual size */
.actual{position:relative}
.arow{display:flex;align-items:flex-end;gap:var(--AGAP);margin-bottom:var(--AROW);padding-bottom:150px}
.hoop{text-align:left;position:relative}
.hoop img{display:block}
.hoop .cap{position:absolute;left:0;top:100%;margin-top:14px}
.ruler{position:relative;height:30px;border-bottom:1px solid var(--ink);margin-top:10px}
.ruler i{position:absolute;bottom:0;width:1px;background:var(--ink)}
.ruler b{position:absolute;bottom:8px;font-family:'JetBrains Mono';font-weight:400;font-size:14px;letter-spacing:.08em;color:var(--mute);transform:translateX(-50%)}
/* plain */
.plain{position:absolute;inset:0}
.plain img{width:100%;height:100%;object-fit:cover;display:block}
.plain .veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(241,235,225,.92) 0%,rgba(241,235,225,.55) 30%,rgba(241,235,225,0) 52%)}
.plain .veil.bottom{background:linear-gradient(0deg,rgba(241,235,225,.85) 0%,rgba(241,235,225,0) 28%)}
.over{position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:space-between}
.over .pr{display:flex;gap:18px;align-items:baseline;margin-top:var(--GAP2)}
/* card */
.card{width:100%;height:var(--CARDH);background:var(--tile);overflow:hidden}
.card img{width:100%;height:100%;object-fit:cover;display:block}
.cardcap{display:flex;justify-content:space-between;align-items:baseline;margin-top:16px}
"""

TOKENS={
 "feed": dict(PAD="56px",GAP1="22px",GAP2="18px",GAP3="26px",HL="104px",ASIDE="30px",CTA="24px",MONO="16px",NAME="24px",PRICE="30px",
              GGAP="22px",RGAP="18px",THUMB="168px",SPECIMG="500px",AGAP="60px",AROW="26px",CARDH="800px"),
 "story":dict(PAD="72px",GAP1="30px",GAP2="24px",GAP3="40px",HL="140px",ASIDE="38px",CTA="28px",MONO="19px",NAME="28px",PRICE="36px",
              GGAP="26px",RGAP="26px",THUMB="220px",SPECIMG="640px",AGAP="80px",AROW="40px",CARDH="1150px"),
}

def fontfaces():
    out=[]
    for f in ["Inter.local.css","JetBrains_Mono.local.css","Cormorant_Garamond.local.css","Jost.local.css"]:
        out.append(open(f"{ROOT}/fonts/{f}").read().replace("url(","url(FONTS/"))
    return "\n".join(out)

def top(c):
    logo="logo_ivory.png" if c["set"]=="B" else "logo_ink.png"
    lab={"A":"NAIRA PETITE · THE SPEC SHEET","B":"NAIRA PETITE · WHAT I WEAR"}[c["set"]]
    return f'<div class="top"><img src="{ROOT}/{logo}"><span class="setlab">{lab}</span></div>'

def head(c):
    return f'<h1>{esc(c["h1"])}<br><span class="ac">{esc(c["h2"])}</span></h1><p class="aside">{esc(c["aside"])}</p>'

def foot(c,fn="NAIRAFLORE.COM"):
    return f'<div class="foot"><span class="cta">{esc(c["cta"])}</span><span class="fn">{fn}</span></div>'

def tile(sku): return f'{ROOT}/tiles/{sku}.jpg'

def body_grid(c):
    cells=[]
    for i,(sku,part,spec) in enumerate(c["items"],1):
        cells.append(f'<div class="cell"><div class="tile"><img src="{tile(sku)}"></div>'
                     f'<div class="cap"><span class="name">{name(sku)}</span><span class="price">{price(sku)}</span></div>'
                     f'<div class="mono">{i:02d} // {part} · {esc(spec)}</div></div>')
    gw=c.get("gridw","100%")
    return f'<div class="grid" style="max-width:{gw}">{"".join(cells)}</div>'

def body_list(c):
    rows=[]; tot=0
    for i,(sku,part,spec) in enumerate(c["items"],1):
        tot+=ROWS[sku]["price"]
        rows.append(f'<div class="row"><div class="thumb"><img src="{tile(sku)}"></div>'
                    f'<div class="mid"><div class="mono">{i:02d} // {part} · {esc(spec)}</div>'
                    f'<div class="name"><span class="chk"></span><span>{name(sku)}</span></div></div>'
                    f'<div class="price">{price(sku)}</div></div>')
    rows.append(f'<div class="total"><span class="mono">THE WHOLE LOOK · {len(c["items"])} PIECES</span><span class="price">{rupees(tot)}</span></div>')
    return f'<div class="rows">{"".join(rows)}</div>'

def body_receipt(c):
    tiles="".join(f'<div class="tile"><img src="{tile(s)}"></div>' for s,_ in c["items"])
    lines=[]; tot=0
    for sku,sz in c["items"]:
        tot+=ROWS[sku]["price"]
        lines.append(f'<div class="l"><span>{name(sku)}<small>{esc(sz)}</small></span><span>{price(sku)}</span></div>')
    rec=(f'<div class="receipt"><div class="hd"><span>NAIRA PETITE · RINGS</span><span>3 ITEMS</span></div>{"".join(lines)}'
         f'<div class="tot"><span>TOTAL</span><span>{rupees(tot)}</span></div></div>')
    return f'<div class="rrow3">{tiles}</div>{rec}'

def body_spec(c,fmt="feed"):
    sku=c["sku"]
    trs="".join(f'<tr><td>{esc(k)}</td><td>{esc(v)}</td></tr>' for k,v in c["spec"])
    care="".join(f'<div class="{"" if ok else "no"}"><b>{"✓" if ok else "✗"}</b>{esc(k)}</div>' for k,ok in c["care"])
    if fmt=="story":
        return (f'<div class="spec"><div class="tile"><img src="{tile(sku)}"></div>'
                f'<div style="align-self:end"><div class="nm"><div class="name">{name(sku)}</div><div class="price" style="margin-top:6px">{price(sku)}</div></div>'
                f'<div class="mono">{esc(". ".join(DET[sku]["intro"].split(". ")[:2]).rstrip(".")+".")}</div></div></div>'
                f'<table style="margin-top:28px">{trs}</table><div class="care">{care}</div>')
    return (f'<div class="spec"><div class="tile"><img src="{tile(sku)}"></div>'
            f'<div><div class="nm"><div class="name">{name(sku)}</div><div class="price" style="margin-top:6px">{price(sku)}</div></div>'
            f'<table>{trs}</table></div></div><div class="care">{care}</div>')

def body_actual(c,fmt):
    hoops=[]
    for sku,spec in c["items"]:
        w_px=CUT[sku]["mm"]*PX_PER_MM
        bw=CUT[sku]["bbox_w"]; scale=w_px/bw
        h_px=CUT[sku]["bbox_h"]*scale
        hoops.append((sku,spec,round(w_px),round(h_px)))
    r1=hoops; r2=[]
    gap=int(TOKENS[fmt]["AGAP"].replace("px","")) if "AGAP" not in c.get("tok_"+fmt,{}) else int(c["tok_"+fmt]["AGAP"].replace("px",""))
    def row(hs):
        if not hs: return ""
        return '<div class="arow">'+"".join(
            f'<div class="hoop"><img src="{ROOT}/cut/{s}_c.png" style="width:{w}px;height:{h}px">'
            f'<div class="cap" style="width:{w+gap-12}px"><div class="name">{name(s)}</div><div class="mono">{esc(sp)}</div><div class="price" style="margin-top:4px">{price(s)}</div></div></div>'
            for s,sp,w,h in hs)+'</div>'
    ticks="".join(f'<i style="left:{i*PX_PER_MM:.1f}px;height:{18 if i%10==0 else (11 if i%5==0 else 6)}px"></i>'+(f'<b style="left:{i*PX_PER_MM:.1f}px">{i}</b>' if i%10==0 else "") for i in range(0,61))
    ruler=f'<div class="ruler" style="width:{60*PX_PER_MM:.0f}px">{ticks}</div><div class="mono" style="margin-top:10px">MILLIMETRES · TRUE SIZE ON A 68MM-WIDE DISPLAY (MOST 6.5–6.7IN PHONES) · A 6.1IN IPHONE SHOWS THEM ABOUT 5% SMALLER</div>'
    return f'<div class="actual">{row(r1)}{row(r2)}{ruler}</div>'

def body_card(c,fmt="feed"):
    sku=c["sku"]
    zoom=c.get("zoom_"+fmt,"")
    return (f'<div class="card"><img src="{c["image"]}" style="object-position:{c["pos"]};{zoom}"></div>'
            f'<div class="cardcap"><span class="name">{name(sku)}</span><span class="price">{price(sku)}</span></div>')

def page(c,fmt):
    W,H=FORMATS[fmt]; tk=dict(TOKENS[fmt]); tk.update(c.get("tok_"+fmt,{}))
    css=CSS.replace("WIDTH",str(W)).replace("HEIGHT",str(H)).replace("FONTFACES",fontfaces()).replace("FONTS/",f"{ROOT}/fonts/")
    for k,v in tk.items(): css=css.replace(f"var(--{k})",v)
    night=' class="night"' if c["set"]=="B" else ""
    k=c["kind"]
    if k=="plain":
        sku=c["sku"]
        inner=(f'<div class="plain"><img src="{c["image"]}" style="object-position:{c["pos"]}"><div class="veil"></div></div>'
               f'<div class="over"><div>{top(c)}{head(c)}<div class="pr"><span class="name">{name(sku)}</span><span class="price">{price(sku)}</span></div></div>'
               f'{foot(c)}</div>')
    else:
        body={"grid":body_grid,"list":body_list,"receipt":body_receipt,"spec":body_spec,"card":body_card}.get(k)
        b=body_actual(c,fmt) if k=="actual" else (body_spec(c,fmt) if k=="spec" else (body_card(c,fmt) if k=="card" else body(c)))
        inner=f'{top(c)}{head(c)}<div class="body">{b}</div>{foot(c)}'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body{night}><div class="ad">{inner}</div></body></html>'

def verify():
    bad=[]
    for c in CREATIVES:
        skus=[c["sku"]] if "sku" in c else [it[0] for it in c["items"]]
        for s in skus:
            r=ROWS.get(s)
            if not r: bad.append((c["id"],s,"NOT ACTIVE")); continue
            if r["inv"]<=0: bad.append((c["id"],s,"OUT OF STOCK"))
            if r["inv"]<3: bad.append((c["id"],s,f"ONLY {r['inv']} UNIT(S)"))
            if not r["avail"]: bad.append((c["id"],s,"NOT AVAILABLE FOR SALE"))
    return bad

async def render(only=None,fmts=("feed","story")):
    os.makedirs(f"{ROOT}/out",exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args=["--no-sandbox"])
        for c in CREATIVES:
            if only and c["id"] not in only: continue
            for fmt in fmts:
                W,H=FORMATS[fmt]
                fn=f"{ROOT}/out/{c['id']}_{fmt}.html"; open(fn,"w").write(page(c,fmt))
                pg=await b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
                await pg.goto("file://"+fn); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(250)
                ov=await pg.evaluate("Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)")
                await pg.screenshot(path=f"{ROOT}/out/{c['id']}_{fmt}.png"); await pg.close()
                print(f"{c['id']}_{fmt}: scrollHeight {ov} / {H} {'OVERFLOW' if ov>H else 'ok'}")
        await b.close()

if __name__=="__main__":
    bad=verify()
    print("stock gate:", "PASS" if not bad else bad)
    only=sys.argv[1].split(",") if len(sys.argv)>1 and sys.argv[1] else None
    fmts=tuple(sys.argv[2].split(",")) if len(sys.argv)>2 else ("feed","story")
    asyncio.run(render(only,fmts))
