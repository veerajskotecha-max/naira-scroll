# -*- coding: utf-8 -*-
"""Builds index.html for the colour-camps delivery artifact from manifest.json."""
import json, base64, html, os, sys
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
ART = f"{SP}/art_cc"
M = json.load(open(f"{ART}/manifest.json"))
F = json.load(open(f"{SP}/cc/shoot/final_v2.json"))
E = lambda s: html.escape(str(s))
vel = base64.b64encode(open(f"{SP}/ads/fonts/Velista.ttf", "rb").read()).decode()
logo = base64.b64encode(open(f"{SP}/standee/assets/logo_src.png", "rb").read()).decode()

CAMP_COPY = {
 "peach": ("APRICOT", "The fruit stall", "Gold pieces photographed on apricot silk. Each price is a fruit-stall PLU sticker; the camp word sits behind the piece."),
 "sage": ("SAGE", "The colour card", "Gold and steel on celadon glaze. Each ad carries a paint-chip card whose chips are sampled from that photograph."),
 "lilac": ("LILAC", "The stamp sheet", "Rhodium pieces on lilac paper. Each ad carries a perforated stamp of the piece, cancelled by a NAIRAFLORE.COM postmark."),
}
SHOTS = {"S1": "Hero", "S2": "Worn", "S3": "Macro", "S4": "Flat lay"}


def pill(stock):
    if stock >= 20: return f'<span class="pill ok">{stock} in stock</span>'
    if stock >= 4: return f'<span class="pill mid">{stock} in stock</span>'
    return f'<span class="pill low">{stock} in stock · cap spend</span>'


def product(p, camp):
    car = p["carousel"]
    cards = "".join(f'<button class="card" data-full="{E(c["file"])}" aria-label="Carousel card {i+1}"><img loading="lazy" src="{E(c["thumb"])}" alt=""><span>{i+1}</span></button>' for i, c in enumerate(car))
    car_paths = json.dumps([c["file"] for c in car])
    shots = " · ".join(v for k, v in SHOTS.items() if F.get(f'{p["sku"]}|{k}'))
    return f'''
<article class="prod" id="{E(p["sku"])}">
  <div class="info">
    <p class="eyebrow">{E(p["id"])} · {E(p["sku"])}</p>
    <h3>{E(p["title"])}</h3>
    <p class="price">₹{p["price"]:,} {pill(p["stock"])}</p>
    <p class="sub">{E(p["sub"])}</p>
    <p class="spec">{E(p["spec"])}</p>
    <p class="url"><span>{E(p["url"])}</span><button class="copy" data-copy="{E(p["url"])}">Copy link</button></p>
    <p class="shots">Verified frames in this set: {E(shots)}</p>
  </div>
  <div class="formats">
    <figure class="story"><button class="thumb" data-full="{E(p["ads"]["story"]["file"])}"><img loading="lazy" src="{E(p["ads"]["story"]["thumb"])}" alt="{E(p["title"])} story ad"></button>
      <figcaption>Story 1080×1920 <button class="dl" data-path="{E(p["ads"]["story"]["file"])}">Save</button></figcaption></figure>
    <figure class="feed"><button class="thumb" data-full="{E(p["ads"]["feed"]["file"])}"><img loading="lazy" src="{E(p["ads"]["feed"]["thumb"])}" alt="{E(p["title"])} feed ad"></button>
      <figcaption>Feed 1080×1350 <button class="dl" data-path="{E(p["ads"]["feed"]["file"])}">Save</button></figcaption></figure>
    <div class="carousel"><div class="cards">{cards}</div>
      <p class="cap">Carousel · {len(car)} cards <button class="dlzip" data-paths='{E(car_paths)}' data-name="{E(p["id"] + "-" + p["sku"])}-carousel.zip">Save carousel .zip</button></p></div>
  </div>
</article>'''


def camp_section(c):
    name, device, blurb = CAMP_COPY[c["key"]]
    allp = []
    for p in c["products"]:
        allp += [p["ads"]["story"]["file"], p["ads"]["feed"]["file"]] + [x["file"] for x in p["carousel"][1:]]
    prods = "".join(product(p, c["key"]) for p in c["products"])
    return f'''
<section class="camp {c["key"]}" id="{c["key"]}">
  <header class="band">
    <div><p class="eyebrow">Camp · {E(device)}</p><h2>{name}<em>.</em></h2></div>
    <div class="bandside"><p>{E(blurb)}</p>
      <button class="dlzip big" data-paths='{E(json.dumps(allp))}' data-name="naira-{name.lower()}-ads.zip">Save all {name} ads .zip</button></div>
  </header>
  {prods}
</section>'''


def standees():
    out = []
    for s in M["standees"]:
        if not s["sizes"]: continue
        chips = "".join(f'<button class="size{" on" if i == 0 else ""}" data-i="{i}">{E(z["ft"])}<small>{E(z["cm"])}</small></button>' for i, z in enumerate(s["sizes"]))
        data = json.dumps(s["sizes"])
        z0 = s["sizes"][0]
        out.append(f'''
<article class="stand" data-sizes='{E(data)}'>
  <div class="stview"><button class="thumb stthumb" data-full="{E(z0["preview"])}"><img loading="lazy" src="{E(z0["thumb"])}" alt="{E(s["name"])} standee preview"></button></div>
  <div class="stinfo"><p class="eyebrow">Exhibition roll-up standee</p><h3>{E(s["name"])}</h3>
    <div class="sizes">{chips}</div>
    <p class="stmeta"><span class="stcm">{E(z0["cm"])}</span> · print PDF at exact size, <span class="stmb">{z0.get("pdf_mb","–")} MB</span></p>
    <p><button class="dl big stpdf" data-path="{E(z0.get("pdf",""))}">Save print PDF</button> <button class="dl stprev" data-path="{E(z0["preview"])}">Save preview JPG</button></p>
  </div>
</article>''')
    return "".join(out)


def notes():
    return '''
<section id="notes" class="notes">
  <h2>How this set was made and checked</h2>
  <div class="cols">
    <div><h3>Photographs</h3>
      <p>Every image was generated in Higgsfield from the product's own listing photo, one product per frame, inside its camp colour. Each frame was then checked against the live listing by an independent reviewer: stone and link counts, construction and clasps, metal colour, finish, scale against a known object or the body, and no face features in worn shots.</p>
      <p>Frames that failed were reshot or left out. None were used on trust. Examples: the huggie and bow earrings were reshot without a size prop after reading oversized next to fruit; the Toggle Link Chain clasp was corrected to the real spring-gate ring; worn shots showing an eye, lip or chin were dropped.</p></div>
    <div><h3>Edits after the shoot</h3>
      <p>Sage frames had their green backgrounds pulled toward the brand sage. On the heroes the piece was masked out entirely, and on the other frames the reviewers checked the metal for any colour shift. Worn shots were cropped to remove face edges. On the Trio Oval Drop hero, the cream table behind the torn paper was recoloured lilac with the earrings masked out.</p>
      <p>Every claim on the ads comes from the listing: prices and stock are live Shopify figures, and every piece is waterproof surgical stainless steel.</p></div>
    <div><h3>Running it</h3>
      <p>Always-on: Woven Gold Hoops, Toggle Link Chain and Prism Rivière (77–80 units each). Secondary: Heartbead Bracelet and Brushed Gold Huggies.</p>
      <p>Pieces with 3–5 units should run in carousels or with capped budgets, and should be paused at 2 units so an ad never sells something that is gone.</p>
      <p>Standee QR codes open nairaflore.com tagged utm_source=standee, utm_medium=print, utm_campaign=&lt;camp&gt;, so fair traffic shows up separately in analytics.</p></div>
  </div>
  <h3>Printing the standees</h3>
  <p class="print">Each PDF is set at the exact roll-up size (61 × 152.4, 76.2 × 182.6, 91.4 × 182.6 and 122 × 182.6 cm), with images and colours running to every edge. The bottom 12 cm is a plain band because it sits inside the stand's base, and nothing important sits in the top 3 cm under the rail. Files are RGB and the printer converts them. If the print shop asks for bleed, let them extend the edges; the backgrounds already run off the page.</p>
</section>'''


n_story = sum(1 for c in M["camps"] for p in c["products"])
n_card = sum(len(p["carousel"]) for c in M["camps"] for p in c["products"])
n_pdf = sum(1 for s in M["standees"] for z in s["sizes"] if z.get("pdf"))

page = f'''<title>Naira Colour Camps</title>
<style>
@font-face{{font-family:"Velista";src:url(data:font/ttf;base64,{vel}) format("truetype");font-display:swap}}
</style>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Cormorant+Garamond:ital,wght@1,500&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
<style>
:root{{--ground:#EDF0EC;--panel:#FAFBF9;--ink:#1B2A24;--muted:#5A6B63;--line:#D3DCD6;--accent:#C4513A;
--apricot:#F6D4C0;--apricot-ink:#3B2A22;--sage:#C9DBD1;--sage-ink:#1F3A31;--lilac:#E3D6EA;--lilac-ink:#3B2D52;
--ok:#2F6B4F;--mid:#8A6A1F;--low:#A33D2B;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--ground:#121714;--panel:#1A211D;--ink:#E4EAE6;--muted:#9AABA2;--line:#2D3A33;--accent:#E88A70;
--apricot:#3A2A22;--apricot-ink:#F6D4C0;--sage:#20302A;--sage-ink:#C9DBD1;--lilac:#2C2436;--lilac-ink:#E3D6EA;--ok:#7CC4A0;--mid:#E0B85A;--low:#F08A74;color-scheme:dark}}}}
:root[data-theme="dark"]{{--ground:#121714;--panel:#1A211D;--ink:#E4EAE6;--muted:#9AABA2;--line:#2D3A33;--accent:#E88A70;
--apricot:#3A2A22;--apricot-ink:#F6D4C0;--sage:#20302A;--sage-ink:#C9DBD1;--lilac:#2C2436;--lilac-ink:#E3D6EA;--ok:#7CC4A0;--mid:#E0B85A;--low:#F08A74;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--ground);color:var(--ink);font:400 15px/1.55 Jost,"Helvetica Neue",Arial,sans-serif;margin:0}}
.wrap{{max-width:1240px;margin:0 auto;padding-inline:20px;padding-block:0 64px}}
.mono,.eyebrow,.shots,.spec,figcaption,.cap,.stmeta,nav a{{font-family:"JetBrains Mono",ui-monospace,monospace;letter-spacing:.06em}}
.eyebrow{{text-transform:uppercase;font-size:11px;color:var(--muted);margin:0 0 6px}}
h1,h2{{font-family:Velista,"Cormorant Garamond",Georgia,serif;font-weight:500;line-height:.9;margin:0;text-wrap:balance}}
h1{{font-size:clamp(56px,11vw,150px);letter-spacing:-.01em}}
h1 em,h2 em{{font-style:normal;color:var(--accent)}}
h3{{font:600 17px/1.2 Jost,sans-serif;letter-spacing:.06em;text-transform:uppercase;margin:0 0 6px;text-wrap:balance}}
.top{{display:grid;gap:18px;padding-block:28px 22px}}
.logo{{width:132px;height:30px;background:var(--ink);-webkit-mask:url(data:image/png;base64,{logo}) center/contain no-repeat;mask:url(data:image/png;base64,{logo}) center/contain no-repeat}}
.lede{{max-width:62ch;font-size:17px;margin:0}}
.stats{{display:flex;flex-wrap:wrap;gap:8px 20px;font-family:"JetBrains Mono",monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}
.stats b{{color:var(--ink);font-weight:500}}
nav{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--ground);border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:4px 18px;padding-block:10px}}
nav a{{color:var(--ink);text-decoration:none;font-size:12px;text-transform:uppercase}}
nav a:hover,nav a:focus-visible{{color:var(--accent)}}
.camp{{margin-top:40px}}
.band{{display:grid;grid-template-columns:1fr;gap:14px;padding:22px 22px 20px;border-radius:4px}}
@media (min-width:760px){{.band{{grid-template-columns:auto 1fr;align-items:end;gap:28px}}}}
.band h2{{font-size:clamp(54px,9vw,110px)}}
.band p{{margin:0 0 10px;max-width:56ch}}
.peach .band{{background:var(--apricot);color:var(--apricot-ink)}} .sage .band{{background:var(--sage);color:var(--sage-ink)}} .lilac .band{{background:var(--lilac);color:var(--lilac-ink)}}
.band .eyebrow{{color:inherit;opacity:.75}}
.prod{{display:grid;grid-template-columns:1fr;gap:18px;padding-block:24px;border-bottom:1px solid var(--line)}}
@media (min-width:900px){{.prod{{grid-template-columns:300px 1fr}}}}
.info p{{margin:0 0 8px}}
.price{{font-weight:600;font-size:18px;display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-variant-numeric:tabular-nums}}
.pill{{font:500 11px/1 "JetBrains Mono",monospace;letter-spacing:.06em;padding:5px 8px;border-radius:99px;border:1px solid currentColor}}
.pill.ok{{color:var(--ok)}} .pill.mid{{color:var(--mid)}} .pill.low{{color:var(--low)}}
.sub{{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:19px;line-height:1.2}}
.spec,.shots{{font-size:11.5px;text-transform:uppercase;color:var(--muted)}}
.url{{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:13px;word-break:break-all}}
.formats{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}}
@media (min-width:700px){{.formats{{grid-template-columns:minmax(0,.75fr) minmax(0,1fr) minmax(0,1.35fr)}}}}
.carousel{{grid-column:1/-1;min-width:0}}
@media (min-width:700px){{.carousel{{grid-column:auto}}}}
figure{{margin:0;min-width:0}}
.thumb{{display:block;padding:0;border:0;background:none;cursor:zoom-in;width:100%}}
.thumb img,.card img{{display:block;width:100%;height:auto;border-radius:3px;box-shadow:0 1px 3px rgb(0 0 0 / .12)}}
figcaption,.cap{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:6px;font-size:11px;text-transform:uppercase;color:var(--muted);margin-top:8px}}
.cards{{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x mandatory}}
.card{{flex:0 0 46%;max-width:200px;position:relative;padding:0;border:0;background:none;cursor:zoom-in;scroll-snap-align:start}}
.card span{{position:absolute;left:6px;top:6px;font:500 10px/1 "JetBrains Mono",monospace;background:var(--panel);color:var(--ink);padding:4px 6px;border-radius:99px}}
button.dl,button.dlzip,button.copy,.size{{font:500 12px/1 Jost,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--ink);background:var(--panel);border:1px solid var(--ink);border-radius:2px;padding:7px 10px;cursor:pointer}}
button.big{{padding:11px 14px}}
button:focus-visible,a:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
button.dl:hover,button.dlzip:hover,button.copy:hover{{background:var(--ink);color:var(--panel)}}
.no-dl button.dl,.no-dl button.dlzip{{display:none}}
.dlnote{{display:none;font-size:13px;color:var(--muted)}} .no-dl .dlnote{{display:block}}
.standees{{margin-top:48px}}
.standees>header h2{{font-size:clamp(46px,8vw,96px)}}
.standees>header p{{max-width:62ch}}
.stand{{display:grid;grid-template-columns:1fr;gap:18px;padding-block:22px;border-bottom:1px solid var(--line)}}
@media (min-width:760px){{.stand{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}}}
.stview{{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:14px;display:flex;justify-content:center}}
.stview img{{max-height:640px;width:auto;margin:0 auto;box-shadow:0 4px 16px rgb(0 0 0 / .14)}}
.sizes{{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}}
.size{{display:grid;gap:4px;text-align:left}} .size small{{font:400 10px/1 "JetBrains Mono",monospace;letter-spacing:.04em;text-transform:none;color:var(--muted)}}
.size.on{{background:var(--ink);color:var(--panel)}} .size.on small{{color:inherit;opacity:.8}}
.stmeta{{font-size:12px;color:var(--muted)}}
.notes{{margin-top:48px}} .notes h2{{font-size:clamp(40px,6vw,72px);margin-bottom:18px}}
.cols{{display:grid;grid-template-columns:1fr;gap:22px}} @media (min-width:860px){{.cols{{grid-template-columns:repeat(3,1fr)}}}}
.cols p,.print{{max-width:62ch;margin:0 0 10px}}
#lb{{position:fixed;inset:0;background:rgb(10 14 12 / .92);display:flex;align-items:center;justify-content:center;padding:calc(env(safe-area-inset-top,0px) + 48px) 16px 16px;z-index:20}}
#lb img{{max-width:100%;max-height:100%;object-fit:contain}}
#lb[hidden],#toast[hidden]{{display:none!important}}
#lb button{{position:absolute;top:calc(env(safe-area-inset-top,0px) + 10px);right:14px;font:500 12px Jost,sans-serif;letter-spacing:.08em;text-transform:uppercase;background:#fff;color:#111;border:0;padding:8px 12px;border-radius:2px;cursor:pointer}}
#toast{{position:fixed;left:50%;bottom:calc(env(safe-area-inset-bottom,0px) + 18px);transform:translateX(-50%);background:var(--ink);color:var(--panel);font:500 13px Jost,sans-serif;padding:10px 14px;border-radius:3px;z-index:30;max-width:calc(100% - 32px)}}
@media (prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}
</style>
<div class="wrap">
  <div class="top">
    <div class="logo" role="img" aria-label="Naira"></div>
    <h1>Colour Camps<em>.</em></h1>
    <p class="lede">Ready-to-run ads for Naira Petite in three colour worlds, plus three exhibition standee designs. Every piece was photographed inside its colour and checked against its live listing before it went into an ad.</p>
    <div class="stats"><span><b>{n_story}</b> products</span><span><b>{n_story*2}</b> hero ads, story and feed</span><span><b>{n_story}</b> carousels, <b>{n_card}</b> cards</span><span><b>{n_pdf}</b> print-ready standee PDFs</span></div>
    <p class="dlnote">Saving files isn't available in this view. Open the page on claude.ai to save the ads and print files.</p>
  </div>
  <nav aria-label="Sections"><a href="#peach">Apricot</a><a href="#sage">Sage</a><a href="#lilac">Lilac</a><a href="#standees">Standees</a><a href="#notes">How it was checked</a></nav>
  {"".join(camp_section(c) for c in M["camps"])}
  <section class="standees" id="standees">
    <header><p class="eyebrow">Exhibition roll-ups · three options · four sizes each</p><h2>Standees<em>.</em></h2>
    <p>Each option takes one camp's photographs and its device and makes it big: the fruit stall, the colour card and the stamp sheet. Pick a size to see that layout and save its print file.</p></header>
    {standees()}
  </section>
  {notes()}
</div>
<div id="lb" hidden><button type="button" id="lbx">Close</button><img alt=""></div>
<div id="toast" hidden role="status"></div>
<script>
(function(){{
  var DL=null, busy=false;
  function toast(t){{var e=document.getElementById('toast');e.textContent=t;e.hidden=false;clearTimeout(e._t);e._t=setTimeout(function(){{e.hidden=true}},3200)}}
  function why(e){{var c=e&&e.code;if(c==='declined')return null;if(c==='rate_limited')return 'Another save is waiting for you. Finish it, then try again.';
    if(c==='extension_not_enabled'||c==='rejected_extension')return 'This file type cannot be saved from this view.';if(c==='too_large')return 'That file is too large for this view.';return 'Saving is not available right now.'}}
  var ready=(window.claude&&window.claude.use)?window.claude.use('downloads'):Promise.resolve(null);
  ready.then(function(d){{DL=d;if(!d)document.body.classList.add('no-dl')}}).catch(function(){{document.body.classList.add('no-dl')}});
  if(!(window.claude&&window.claude.use))document.body.classList.add('no-dl');
  async function saveBlob(name,blob){{try{{await DL.save({{filename:name,data:blob}});toast('Saved '+name)}}catch(e){{var m=why(e);if(m)toast(m)}}}}
  async function savePath(p){{if(!DL||busy)return;busy=true;try{{var r=await fetch(p);if(!r.ok)throw 0;await saveBlob(p.split('/').pop(),await r.blob())}}catch(e){{toast('Could not load that file. Reload the page and try again.')}}finally{{busy=false}}}}
  async function saveZip(paths,name){{if(!DL||busy)return;if(!window.JSZip){{toast('The zip tool did not load. Save files one by one.');return}}busy=true;toast('Packing '+paths.length+' files…');
    try{{var z=new JSZip();for(var i=0;i<paths.length;i++){{var r=await fetch(paths[i]);if(!r.ok)throw 0;z.file(paths[i].split('/').pop(),await r.blob())}}
    var b=await z.generateAsync({{type:'blob',compression:'STORE'}});await saveBlob(name,b)}}catch(e){{toast('Could not pack those files. Try saving them one by one.')}}finally{{busy=false}}}}
  document.addEventListener('click',function(ev){{
    var t=ev.target.closest('button');if(!t)return;
    if(t.classList.contains('dl')){{savePath(t.dataset.path);return}}
    if(t.classList.contains('dlzip')){{saveZip(JSON.parse(t.dataset.paths),t.dataset.name);return}}
    if(t.classList.contains('copy')){{var v=t.dataset.copy;if(navigator.clipboard)navigator.clipboard.writeText(v).then(function(){{toast('Link copied')}},function(){{toast(v)}});else toast(v);return}}
    if(t.dataset.full){{var lb=document.getElementById('lb');lb.querySelector('img').src=t.dataset.full;lb.hidden=false;document.getElementById('lbx').focus();return}}
    if(t.id==='lbx'){{document.getElementById('lb').hidden=true;return}}
    if(t.classList.contains('size')){{var a=t.closest('.stand'),S=JSON.parse(a.dataset.sizes),z=S[+t.dataset.i];
      a.querySelectorAll('.size').forEach(function(b){{b.classList.toggle('on',b===t)}});
      var th=a.querySelector('.stthumb');th.dataset.full=z.preview;th.querySelector('img').src=z.thumb;
      a.querySelector('.stcm').textContent=z.cm;a.querySelector('.stmb').textContent=(z.pdf_mb||'–')+' MB';
      a.querySelector('.stpdf').dataset.path=z.pdf||'';a.querySelector('.stprev').dataset.path=z.preview}}
  }});
  document.getElementById('lb').addEventListener('click',function(e){{if(e.target.id==='lb')e.currentTarget.hidden=true}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')document.getElementById('lb').hidden=true}});
}})();
</script>'''
open(f"{ART}/index.html", "w").write(page)
print("index.html", round(len(page) / 1e3), "KB")
