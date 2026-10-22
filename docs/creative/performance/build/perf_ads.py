# Performance ads (Oct 2026): every passed frame from the performance shoot, set in one of the four overlays that have sold:
#   deck   "Almost edible." / "Sweet On You.": Velista capitals, italic correction, rule + spec, ink CTA, price (build_ads.html_deck)
#   note   "The gold note.": italic headline, two roman lines, tracked name · price (build_ads.html, layout v1)
#   quiet  the Apricot camp (1.72×): NAIRA wordmark at the top, name and price centred at the foot
#   plain  the fruit-plate Story (2.94×): the photograph alone; the words live in the primary text
# Frames are 1080×1920 (9:16). Each copy entry makes a Story (the frame as shot) and a Feed post (a 1080×1350 window centred on
# the jewellery, `cy` = its centre as a fraction of the frame height). A rhyme frame's Story is plain unless "story": "deck".
# Usage: perf_ads.py [--copy copy.json] [id-prefix ...] -> <scratchpad>/perf/ads/out/<id>.jpg, copied to ../ads/<id>.jpg
import json, os, re, shutil, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE)
sys.path.insert(0, os.path.normpath(f"{PERF}/../finished-ads"))
import build_ads as B

SPB = B.SPB; OUT, WORK = f"{SPB}/perf/ads/out", f"{SPB}/perf/ads/work"

QUIET_CSS = """
@font-face{font-family:Velista;src:url("file://%(b)s/Velista.ttf")}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative;color:%(ink)s}
.ft{color:var(--tone,%(ink)s);isolation:isolate}
.qglow::before{content:"";position:absolute;inset:-40px 18%%;z-index:-1;background:radial-gradient(closest-side,var(--glow) 0%%,var(--glow) 45%%,transparent 100%%)}
.wm{position:absolute;left:50%%;transform:translateX(-50%%);top:%(top)dpx;height:%(wh)dpx}
.ft{position:absolute;left:0;right:0;bottom:%(bot)dpx;text-align:center}
.nm{font-family:Velista;font-size:%(ns)dpx;letter-spacing:.14em;line-height:1;margin-left:.14em}
.pr{font-family:Jost;font-weight:500;font-size:%(ps)dpx;letter-spacing:.22em;margin-top:18px;margin-left:.22em}
"""

def html_quiet(ad, bg):
    W, H = B.SIZE[ad["fmt"]]; story = ad["fmt"] == "9:16"
    top, bot = (300, 400) if story else (70, 76)
    ink = B.DECK_PAPER if ad.get("tone") == "cream" else "#2B2622"
    logo = "logo_white.png" if ad.get("tone") == "cream" else "logo_ink.png"
    css = QUIET_CSS % dict(b=B.BRAND, f=B.FONTS, w=W, h=H, bg="file://" + bg, ink=ink, top=ad.get("wy", top), wh=ad.get("wh", 44),
                           bot=ad.get("fy", bot), ns=ad.get("ns", 40), ps=ad.get("ps", 22))
    return (f'<meta charset="utf-8"><style>{css}</style><body><img class="wm" src="file://{B.BRAND}/{logo}">'
            f'<div class="ft"><div class="nm">{B.glue(ad["name"].upper())}</div><div class="pr">{ad["price"]}</div></div></body>')

# Placement: the copy block goes where the photograph is calmest and its tone reads. Python scores the background on a 24 px grid
# (detail = blurred gradient; ink type is penalised on dark cells, cream type on light ones), and a script in the page tries every
# corner, width, offset and a slightly smaller type size, measures the real text box and keeps the cheapest. The deck footer picks
# ink or cream the same way and gains a soft paper band when neither reads.
CELL = 24
PLACE_JS = """<script>(function(){const P=%s;
function cost(r,a){const p=16,v=[];const x0=Math.max(0,Math.floor((r.left-p)/P.cw)),x1=Math.min(P.cols-1,Math.floor((r.right+p)/P.cw)),
 y0=Math.max(0,Math.floor((r.top-p)/P.cw)),y1=Math.min(P.rows-1,Math.floor((r.bottom+p)/P.cw));
 for(let y=y0;y<=y1;y++)for(let x=x0;x<=x1;x++)v.push(a[y*P.cols+x]);if(!v.length)return 9;v.sort((m,n)=>m-n);
 return v.reduce((m,n)=>m+n,0)/v.length+.6*v[Math.floor(v.length*.9)];}
function lines(el,sel,lh){const h=el.querySelector(sel);if(!h)return 1;const fs=parseFloat(getComputedStyle(h).fontSize);return Math.round(h.getBoundingClientRect().height/(fs*lh));}
function hit(a,b){return!(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom);}
function put(el,at,w,off,k){const s=el.style;s.left=s.right=s.top=s.bottom=s.transform='';s.width=w+'px';
 if(at[1]=='c'||at=='bc'){s.left='50%%';s.transform='translateX(-50%%)';s.textAlign='center';s.alignItems='center';}
 else if(at[1]=='l'){s.left=P.side+'px';s.textAlign='left';s.alignItems='flex-start';}else{s.right=P.side+'px';s.textAlign='right';s.alignItems='flex-end';}
 if(at[0]=='t')s.top=off+'px';else s.bottom=off+'px';
 el.querySelectorAll('.h').forEach(h=>h.style.fontSize=(P.hs*k)+'px');el.querySelectorAll('.c').forEach(c=>c.style.fontSize=(P.cs*k)+'px');}
function tone(el,t){const ink=t=='ink';el.style.setProperty('--tone',ink?P.INK:P.PAPER);el.style.setProperty('--glow',ink?'rgba(251,246,240,.80)':'rgba(28,22,18,.42)');
 el.style.setProperty('--btn',ink?P.INK:P.PAPER);el.style.setProperty('--btnt',ink?P.PAPER:P.INK);
 el.querySelectorAll('img.wmf').forEach(i=>i.src=i.src.replace(/logo_(ink|white)/,ink?'logo_ink':'logo_white'));}
function go(){const el=document.querySelector(P.sel);const ft=P.foot?document.querySelector('.ft'):null;const fr=ft?ft.getBoundingClientRect():null;let best=null;
 for(const at of P.ats)for(const w of P.ws)for(const k of[1,.86])for(let i=0;i<P.n;i++){const off=(at[0]=='t'?P.top:P.bot)+i*36;put(el,at,w,off,k);
  const r=el.getBoundingClientRect();if(r.top<P.top-1||r.bottom>P.H-P.bot+1||r.left<0||r.right>P.W)continue;if(fr&&hit(r,{left:fr.left,right:fr.right,top:fr.top-28,bottom:fr.bottom}))continue;
  const band=(P.sy&&Math.min(r.bottom,P.sy[1])-Math.max(r.top,P.sy[0])>12?.9:0)+(P.quiet&&P.sy&&r.bottom<P.sy[0]?.25:0);const hl=lines(el,'.h',P.lh),xs=Math.max(0,hl-P.hl)*.09;
  for(const t of['ink','cream']){let c=cost(r,P[t])+band+xs+(k<1?.05:0)+(t!=P.tone0?.06:0)+(at!=P.pref?.04:0)+i*.004;if(!best||c<best.c)best={c,at,w,off,k,t};}}
 if(best){put(el,best.at,best.w,best.off,best.k);tone(el,best.t);if(best.c>.42)el.classList.add(P.quiet?'qglow':'glow');}
 if(ft){const parts=[...ft.children].map(e=>e.getBoundingClientRect());let ci=0,cc=0;for(const r of parts){ci+=cost(r,P.ink);cc+=cost(r,P.cream);}
  if(Math.min(ci,cc)/parts.length>.5){const b=document.createElement('div');b.className='band';document.body.insertBefore(b,document.body.firstChild);tone(ft,'ink');}
  else tone(ft,ci<=cc?'ink':'cream');}
 window.__placed=JSON.stringify(best);}
document.fonts.ready.then(()=>setTimeout(go,30));})();</script>"""

def grid(bg):
    """per-cell cost of setting ink or cream type over the background"""
    im = Image.open(bg).convert("L"); W, H = im.size
    L = np.asarray(im.filter(ImageFilter.GaussianBlur(2))).astype(np.float32) / 255
    gy, gx = np.gradient(L); g = np.hypot(gx, gy)
    g = np.asarray(Image.fromarray((np.clip(g / .06, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(7))).astype(np.float32) / 255
    cols, rows = W // CELL, H // CELL
    cell = lambda a: a[:rows * CELL, :cols * CELL].reshape(rows, CELL, cols, CELL).mean((1, 3))
    busy, lum = np.clip(cell(g) * 2.2, 0, 1), cell(L)
    ink = busy + 2.2 * np.clip(.70 - lum, 0, None); cream = busy + 2.2 * np.clip(lum - .42, 0, None)
    return dict(cw=CELL, cols=cols, rows=rows, ink=[round(float(v), 3) for v in ink.ravel()], cream=[round(float(v), 3) for v in cream.ravel()])

def band(ad, y0):
    """the jewellery's vertical extent in page pixels (from the shoot manifest), or None"""
    if not ad.get("sy"): return None
    a, b = ad["sy"]; return [round(a * 1920 - y0), round(b * 1920 - y0)]

def placer(ad, bg, y0):
    W, H = B.SIZE[ad["fmt"]]; story = ad["fmt"] == "9:16"; deck = ad.get("layout", "deck") == "deck"
    top, bot = (300 if story else 60), (392 if story else 60)
    if not deck: bot = 380 if story else 64
    if ad.get("layout") == "quiet": bot = 400 if story else 76
    pref = ad.get("at", "tl"); w0 = ad.get("w", 640)
    quiet = ad.get("layout") == "quiet"
    P = dict(grid(bg), sel=".blk" if deck else ".ft" if quiet else ".t", foot=deck, quiet=quiet, W=W, H=H, top=top, bot=bot, n=(26 if ad.get("layout") == "quiet" else 10) if story else (18 if ad.get("layout") == "quiet" else 8), side=ad.get("x", 64 if deck else 72),
             hs=ad.get("hs", 96 if deck else 78), cs=ad.get("cs", 38 if deck else 34), pref=pref, tone0="cream" if ad.get("tone") == "cream" else "ink",
             ats=["bc"] if quiet else ["tl", "tr", "bl", "br"] + (["tc"] if deck else []), ws=[1000] if quiet else sorted({w0, 380, 460, 560, 680}), INK=B.DECK_INK, PAPER=B.DECK_PAPER,
             sy=band(ad, y0), lh=.9 if deck else .98, hl=2 if deck else 1)
    return PLACE_JS % json.dumps(P)

def prep(ad):
    im = Image.open(f"{PERF}/{ad['plate']}").convert("RGB").resize((1080, 1920), Image.LANCZOS)
    y0 = 0
    if ad["fmt"] == "4:5":
        cy = ad.get("cy", .5); y0 = min(max(round(cy * 1920 - 675), 0), 1920 - 1350); im = im.crop((0, y0, 1080, y0 + 1350))
    path = f"{WORK}/{ad['id']}_bg.jpg"; im.save(path, quality=95); return path, y0

def expand(entries):
    """one copy entry per frame -> a Feed ad and a Story ad"""
    ads = []
    for e in entries:
        base = e.get("id") or re.sub(r"\.jpg$", "", os.path.basename(e["plate"]))
        for fmt, tag in (("4:5", "feed"), ("9:16", "story")):
            ad = dict(e, fmt=fmt, id=f"{base}-{tag}")
            ad.update(e.get(tag, {}) if isinstance(e.get(tag), dict) else {})
            if fmt == "9:16" and e["plate"].endswith("-rhyme.jpg") and e.get("story") != "deck": ad["layout"] = "plain"
            ads.append(ad)
    return ads

def main():
    args = sys.argv[1:]; name = f"{HERE}/copy.json"
    if "--copy" in args: i = args.index("--copy"); name = args[i + 1]; del args[i:i + 2]
    ads = expand(json.load(open(name))["frames"])
    for d in (OUT, WORK, f"{PERF}/ads"): os.makedirs(d, exist_ok=True)
    jobs = []
    for ad in ads:
        if args and not any(ad["id"].startswith(a) for a in args): continue
        bg, y0 = prep(ad); lay = ad.get("layout", "deck")
        if lay == "plain": Image.open(bg).save(f"{WORK}/{ad['id']}.png"); jobs.append((ad["id"], None)); continue
        page = {"deck": B.html_deck, "note": B.html, "quiet": html_quiet}[lay](dict(ad, layout="v1", sb=band(ad, y0)) if lay == "note" else dict(ad, sb=band(ad, y0)), bg)
        if lay in ("deck", "note", "quiet") and not ad.get("fixed"): page = page.replace("</body>", "") + placer(ad, bg, y0) + "</body>"
        open(f"{WORK}/{ad['id']}.html", "w").write(page); W, H = B.SIZE[ad["fmt"]]; jobs.append((ad["id"], f"{ad['id']}:{W}:{H}"))
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    todo = [j for _, j in jobs if j]
    for k in range(0, len(todo), 40): subprocess.run(["node", f"{HERE}/render_perf.cjs", WORK, *todo[k:k + 40]], check=True, env=env)
    for i, _ in jobs:
        Image.open(f"{WORK}/{i}.png").convert("RGB").save(f"{OUT}/{i}.jpg", quality=92, subsampling=0)
        shutil.copy(f"{OUT}/{i}.jpg", f"{PERF}/ads/{i}.jpg"); print("ad", i)

if __name__ == "__main__":
    main()
