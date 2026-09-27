# -*- coding: utf-8 -*-
"""Shared build system for the overnight sets. Each set is a module exposing SET (meta) and CREATIVES (list of dicts
with a `render(c, fmt, ctx)` callable). core renders both formats, audits copy numbers against listings, gates stock,
exports delivery JPEGs, contact sheets and artifact thumbnails."""
import json, os, sys, asyncio, html, re, importlib
from PIL import Image, ImageDraw, ImageFont
from playwright.async_api import async_playwright

SP="/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
ADS=f"{SP}/ads"; HIST=f"{SP}/hist"; ROOT=f"{SP}/sets"
REPO=os.environ.get("NS_REPO","/home/user/naira-scroll/docs/creative/night-shift")
ROWS={r["sku"]:r for r in json.load(open(f"{ADS}/inventory_rows.json"))}
DET=json.load(open(f"{ADS}/details.json"))
FORMATS={"feed":(1080,1350),"story":(1080,1920)}
VEL=f"{ADS}/fonts/Velista.ttf"
IVORY="#F1EBE1"; INK="#1B1512"; OX="#6E1E2A"; BLUSH="#F2C4BD"; WINE="#2A0D14"; SAGE="#9AA793"; MUTE="#7A6E66"

def rupees(p): return "₹"+f"{int(round(p)):,}"
def name(sku): return html.escape(ROWS[sku]["title"])
def price(sku): return rupees(ROWS[sku]["price"])
def E(s): return html.escape(str(s))
def prod(sku,i=0): return f"{ADS}/prod/{sku}_{i}.jpg"
def pick(n): return f"{HIST}/pick/{n:04d}.png"
def cut(n): return f"{HIST}/cut/{n:04d}.png"
def fit(text,target_px,track=-0.02):
    f=ImageFont.truetype(VEL,200); w=f.getlength(text)+track*200*(len(text)-1)
    return target_px*200/w

def fontfaces():
    out=[f"@font-face{{font-family:'Velista';src:url('{VEL}') format('truetype');font-weight:400 600;}}"]
    for f in ["Inter.local.css","JetBrains_Mono.local.css","Cormorant_Garamond.local.css","Jost.local.css"]:
        out.append(open(f"{ADS}/fonts/{f}").read().replace("url(",f"url({ADS}/fonts/"))
    return "\n".join(out)

BASE_CSS="""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:WIDTHpx;height:HEIGHTpx;overflow:hidden;background:#000}
body{font-family:'Jost',sans-serif;-webkit-font-smoothing:antialiased;color:var(--ink)}
.ad{position:relative;width:WIDTHpx;height:HEIGHTpx;overflow:hidden;background:var(--bg)}
.ad img.layer{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.top{position:absolute;left:var(--pad);right:var(--pad);top:var(--pad);display:flex;justify-content:space-between;align-items:center;z-index:5}
.top img{height:24px}
.lab{font-family:'JetBrains Mono';font-size:15px;letter-spacing:.14em;text-transform:uppercase;opacity:.85}
.foot{position:absolute;left:var(--pad);right:var(--pad);bottom:var(--pad);display:grid;grid-template-columns:1fr auto;gap:18px 28px;align-items:end;z-index:5}
.name{font-family:'Jost';font-weight:600;font-size:var(--NAME);letter-spacing:.06em;text-transform:uppercase;line-height:1.05}
.spec{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;line-height:1.4;margin-top:8px;opacity:.9}
.aside{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:var(--ASIDE);line-height:1.12;margin-bottom:14px;max-width:34ch}
.price{font-family:'Jost';font-weight:600;font-size:var(--PRICE);letter-spacing:.01em;white-space:nowrap;text-align:right}
.cta{display:inline-block;border:2px solid currentColor;font-family:'Jost';font-weight:600;font-size:var(--CTA);letter-spacing:.14em;text-transform:uppercase;padding:calc(var(--CTA)*.7) calc(var(--CTA)*1.4);white-space:nowrap;margin-top:14px}
.cta.solid{background:var(--ac);border-color:var(--ac);color:var(--bg)}
.mono{font-family:'JetBrains Mono';font-size:var(--MONO);letter-spacing:.06em;text-transform:uppercase;line-height:1.4}
.vel{font-family:'Velista';font-weight:500;line-height:.9;letter-spacing:-.01em;text-transform:uppercase}
.ital{font-family:'Cormorant Garamond';font-style:italic;font-weight:500}
"""
TOK={"feed":dict(pad="52px",NAME="24px",MONO="15px",ASIDE="30px",PRICE="34px",CTA="20px"),
     "story":dict(pad="64px",NAME="28px",MONO="18px",ASIDE="36px",PRICE="40px",CTA="24px")}

def top(label,color=INK,logo=None):
    logo=logo or ("logo_ivory.png" if color==IVORY else "logo_ink.png")
    return f'<div class="top" style="color:{color}"><img src="{ADS}/{logo}"><span class="lab">{E(label)} · NAIRAFLORE.COM</span></div>'

def page(c,fmt,mod):
    W,H=FORMATS[fmt]; tk=dict(TOK[fmt]); tk.update(getattr(mod,"TOK",{}).get(fmt,{})); tk.update(c.get("tok_"+fmt,{}))
    vars_=":root{"+";".join(f"--{k}:{v}" for k,v in tk.items())+f";--ink:{c.get('ink',INK)};--bg:{c.get('bg',IVORY)};--ac:{c.get('ac',OX)};--mute:{MUTE}"+"}\n"
    css=vars_+fontfaces()+BASE_CSS.replace("WIDTH",str(W)).replace("HEIGHT",str(H))+getattr(mod,"CSS","")
    body=c["render"](c,fmt)
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="ad">{body}</div></body></html>'

def skus_of(c):
    s=c.get("skus") or ([c["sku"]] if "sku" in c else [])
    return list(dict.fromkeys(s))

def gate(mod):
    bad=[]
    for c in mod.CREATIVES:
        for s in skus_of(c):
            r=ROWS.get(s)
            if not r: bad.append((c["id"],s,"NOT ACTIVE")); continue
            if r["inv"]<=0 or not r["avail"]: bad.append((c["id"],s,"OUT OF STOCK"))
            elif c.get("hero") and r["inv"]<13: bad.append((c["id"],s,f"HERO WITH {r['inv']} UNITS"))
            elif r["inv"]<3: bad.append((c["id"],s,f"ONLY {r['inv']} UNITS"))
            if c.get("water") and not DET[s]["waterproof"]: bad.append((c["id"],s,"WATER CLAIM ON NON-WATERPROOF SKU"))
    return bad

def nums(t): return set(re.findall(r'\d+(?:\.\d+)?',t))
def audit(mod):
    """every figure in a creative's `claims` strings must exist in that SKU's listing Details/intro"""
    out=[]
    for c in mod.CREATIVES:
        for sku,text in c.get("claims",[]):
            src=" ".join(DET[sku]["details"].values())+" "+DET[sku]["intro"]
            missing=[n for n in nums(text) if n not in nums(src) and not re.fullmatch(r'0?[1-9]|1[0-9]|20',n)]
            out.append((c["id"],sku,text[:60],"ok" if not missing else "MISSING "+str(missing)))
    return out

async def render(mod,only=None,fmts=("feed","story")):
    od=f"{ROOT}/{mod.SET['slug']}/out"; os.makedirs(od,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome",args=["--no-sandbox"])
        for c in mod.CREATIVES:
            if only and c["id"] not in only: continue
            for fmt in fmts:
                W,H=FORMATS[fmt]; fn=f"{od}/{c['id']}_{fmt}.html"; open(fn,"w").write(page(c,fmt,mod))
                pg=await b.new_page(viewport={"width":W,"height":H},device_scale_factor=1)
                await pg.goto("file://"+fn); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(350)
                await pg.screenshot(path=f"{od}/{c['id']}_{fmt}.png"); await pg.close()
        await b.close()

def review(mod,fmts=("feed","story"),tag=""):
    od=f"{ROOT}/{mod.SET['slug']}/out"; ids=[c["id"] for c in mod.CREATIVES]
    outs=[]
    for fmt in fmts:
        w,h=(520,650) if fmt=="feed" else (400,711)
        W=len(ids)*(w+12)+12; H=h+40
        sh=Image.new("RGB",(W,H),(40,40,40)); d=ImageDraw.Draw(sh)
        for i,k in enumerate(ids):
            x=12+i*(w+12)
            if not os.path.exists(f"{od}/{k}_{fmt}.png"): d.text((x,h+18),k+" (missing)",fill=(255,120,120)); continue
            im=Image.open(f"{od}/{k}_{fmt}.png").convert("RGB").resize((w,h),Image.LANCZOS); sh.paste(im,(x,12)); d.text((x,h+18),k,fill=(255,255,255))
        fn=f"{od}/review_{fmt}{tag}.jpg"; sh.save(fn,quality=84); outs.append(fn)
    return outs

def export(mod):
    slug=mod.SET["slug"]; od=f"{ROOT}/{slug}/out"
    dst=f"{REPO}/{slug}"; os.makedirs(f"{dst}/feed",exist_ok=True); os.makedirs(f"{dst}/story",exist_ok=True); os.makedirs(f"{ROOT}/{slug}/art",exist_ok=True)
    ids=[c["id"] for c in mod.CREATIVES]
    for c in mod.CREATIVES:
        k=c["id"]
        for fmt in ["feed","story"]:
            im=Image.open(f"{od}/{k}_{fmt}.png").convert("RGB")
            im.save(f"{dst}/{fmt}/{k}-{c['file']}-{'1080x1350' if fmt=='feed' else '1080x1920'}.jpg",quality=92,optimize=True,progressive=True)
            sm=im.copy(); sm.thumbnail((720,1280),Image.LANCZOS); sm.save(f"{ROOT}/{slug}/art/{k}_{fmt}.jpg",quality=80,optimize=True)
    for fmt,(w,h) in {"feed":(520,650),"story":(400,711)}.items():
        W=len(ids)*(w+16)+16; H=h+44+70
        sh=Image.new("RGB",(W,H),(20,18,18)); d=ImageDraw.Draw(sh)
        d.text((16,22),f"NAIRA PETITE · {mod.SET['title'].upper()} · {fmt.upper()} {'1080×1350' if fmt=='feed' else '1080×1920'}",fill=(235,230,222))
        for i,c in enumerate(mod.CREATIVES):
            im=Image.open(f"{od}/{c['id']}_{fmt}.png").convert("RGB").resize((w,h),Image.LANCZOS); x=16+i*(w+16); sh.paste(im,(x,70)); d.text((x,70+h+8),f"{c['id']}  {c['file']}",fill=(200,195,188))
        sh.save(f"{dst}/00-contact-{fmt}.jpg",quality=86)
    return dst

if __name__=="__main__":
    modname=sys.argv[1]; mod=importlib.import_module(modname)
    cmd=sys.argv[2] if len(sys.argv)>2 else "render"
    if cmd in ("render","all"):
        bad=gate(mod); print("stock gate:","PASS" if not bad else bad)
        for a in audit(mod): print("  audit",a)
        only=sys.argv[3].split(",") if len(sys.argv)>3 and sys.argv[3] else None
        asyncio.run(render(mod,only)); print("rendered")
        print(review(mod))
    if cmd in ("export","all"):
        print("exported to",export(mod))
