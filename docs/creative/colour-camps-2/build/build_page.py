# -*- coding: utf-8 -*-
"""Builds index.html for Colour Camps 2.0 from manifest.json."""
import json, base64, html
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
ART = f"{SP}/art_v2"
M = json.load(open(f"{ART}/manifest.json"))
E = lambda s: html.escape(str(s))
vel = base64.b64encode(open(f"{SP}/ads/fonts/Velista.ttf", "rb").read()).decode()
logo = base64.b64encode(open(f"{SP}/standee/assets/logo_src.png", "rb").read()).decode()
V1_URL = "https://claude.ai/artifact/16NXisPUtfeiZFjV5XNNgy"
CAMP_LINE = {"peach": "Gold on apricot silk.", "sage": "Gold and steel on celadon glaze.", "lilac": "Rhodium on lilac paper."}


def pill(n):
    if n >= 20: return f'<span class="stock ok">{n} in stock</span>'
    if n >= 4: return f'<span class="stock mid">{n} in stock</span>'
    return f'<span class="stock low">{n} in stock · cap spend</span>'


def product(p, d):
    cards = "".join(f'<button class="card" data-full="{E(c["file"])}" aria-label="Card {i+1}"><img loading="lazy" src="{E(c["thumb"])}" alt=""><span>{i+1}</span></button>'
                    for i, c in enumerate(p["cards"]))
    paths = json.dumps([p["story"]["file"], p["feed"]["file"]] + [c["file"] for c in p["cards"][1:]])
    return f'''
<article class="prod">
  <div class="info">
    <p class="eyebrow">{E(p["id"])} · {E(p["sku"])}</p>
    <h3>{E(p["title"])}</h3>
    <p class="line">{E(p["line"])}</p>
    <p class="price">₹{p["price"]:,} {pill(p["stock"])}</p>
    <p class="url"><span>{E(p["url"])}</span> <button class="copy" data-copy="{E(p["url"])}">Copy link</button></p>
    <p><button class="dlzip" data-paths='{E(paths)}' data-name="{E(d + '-' + p['id'] + '-' + p['sku'])}.zip">Save all {len(p["cards"]) + 1} files</button></p>
  </div>
  <div class="imgs">
    <figure><button class="thumb" data-full="{E(p["story"]["file"])}"><img loading="lazy" src="{E(p["story"]["thumb"])}" alt="{E(p["title"])}, story ad"></button>
      <figcaption>Story <button class="dl" data-path="{E(p["story"]["file"])}">Save</button></figcaption></figure>
    <figure><button class="thumb" data-full="{E(p["feed"]["file"])}"><img loading="lazy" src="{E(p["feed"]["thumb"])}" alt="{E(p["title"])}, feed ad"></button>
      <figcaption>Feed <button class="dl" data-path="{E(p["feed"]["file"])}">Save</button></figcaption></figure>
    <div class="car"><div class="cards">{cards}</div><p class="cap">Carousel · {len(p["cards"])} cards</p></div>
  </div>
</article>'''


def direction(d, label):
    out = [f'<div class="dir" data-dir="{d}"{" hidden" if d != "framed" else ""}>']
    for c in M["directions"][d]:
        allp = []
        for p in c["products"]:
            allp += [p["story"]["file"], p["feed"]["file"]] + [x["file"] for x in p["cards"][1:]]
        out.append(f'''<section class="camp {c["key"]}" id="{d}-{c["key"]}">
  <header class="band"><div><p class="eyebrow">{E(label)}</p><h2>{c["name"].capitalize()}</h2><p>{E(CAMP_LINE[c["key"]])}</p></div>
  <button class="dlzip" data-paths='{E(json.dumps(allp))}' data-name="naira-2.0-{d}-{c["name"].lower()}.zip">Save all {c["name"].capitalize()} ({len(allp)})</button></header>
  {"".join(product(p, d) for p in c["products"])}
</section>''')
    out.append("</div>")
    return "".join(out)


compare = "".join(f'''<figure class="cmp"><figcaption>{E(r["title"])}</figcaption><div class="trio">
<div><button class="thumb" data-full="{E(r["v1"])}"><img loading="lazy" src="{E(r["v1"])}" alt="version 1"></button><span>1.0</span></div>
<div><button class="thumb" data-full="{E(r["framed"])}"><img loading="lazy" src="{E(r["framed"])}" alt="2.0 framed"></button><span>2.0 · Framed</span></div>
<div><button class="thumb" data-full="{E(r["quiet"])}"><img loading="lazy" src="{E(r["quiet"])}" alt="2.0 full-bleed"></button><span>2.0 · Full-bleed</span></div>
</div></figure>''' for r in M["compare"])

page = f'''<title>Colour Camps 2.0</title>
<style>@font-face{{font-family:"Velista";src:url(data:font/ttf;base64,{vel}) format("truetype");font-display:swap}}</style>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&family=Cormorant+Garamond:ital,wght@1,500&display=swap">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
<style>
:root{{--ground:#F4F2EE;--panel:#FCFBF9;--ink:#1A1614;--muted:#6F6862;--line:#DDD8D1;--gold:#9A7432;
--peach:#EFD7C8;--peach-ink:#3A2520;--sage:#D9E6DE;--sage-ink:#1F3A31;--lilac:#E2D6E6;--lilac-ink:#33274A;--ok:#2F6B4F;--mid:#86661E;--low:#A33D2B;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--ground:#141211;--panel:#1C1A18;--ink:#ECE7E1;--muted:#A39B93;--line:#34302C;--gold:#D2A95E;
--peach:#3A2A23;--peach-ink:#F3DDD0;--sage:#1F2E28;--sage-ink:#D9E6DE;--lilac:#2B2433;--lilac-ink:#E6DCEA;--ok:#7CC4A0;--mid:#E0B85A;--low:#F08A74;color-scheme:dark}}}}
:root[data-theme="dark"]{{--ground:#141211;--panel:#1C1A18;--ink:#ECE7E1;--muted:#A39B93;--line:#34302C;--gold:#D2A95E;
--peach:#3A2A23;--peach-ink:#F3DDD0;--sage:#1F2E28;--sage-ink:#D9E6DE;--lilac:#2B2433;--lilac-ink:#E6DCEA;--ok:#7CC4A0;--mid:#E0B85A;--low:#F08A74;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ground);color:var(--ink);font:400 15px/1.6 Jost,"Helvetica Neue",Arial,sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding-inline:20px;padding-block:0 72px}}
h1,h2{{font-family:Velista,"Cormorant Garamond",Georgia,serif;font-weight:500;margin:0;line-height:1;text-wrap:balance;letter-spacing:.02em}}
h1{{font-size:clamp(44px,8vw,96px)}} h2{{font-size:clamp(34px,5vw,56px)}}
h3{{font:500 15px/1.3 Jost,sans-serif;letter-spacing:.2em;text-transform:uppercase;margin:0 0 6px}}
.eyebrow,.lbl,figcaption,.cap,nav button,.seg button,.stock{{font-family:Jost,sans-serif;font-weight:500;letter-spacing:.24em;text-transform:uppercase;font-size:11px}}
.eyebrow{{color:var(--gold);margin:0 0 10px}}
.line,.ital{{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:500}}
.top{{display:grid;justify-items:center;text-align:center;gap:16px;padding-block:44px 30px}}
.logo{{width:120px;height:27px;background:var(--ink);-webkit-mask:url(data:image/png;base64,{logo}) center/contain no-repeat;mask:url(data:image/png;base64,{logo}) center/contain no-repeat}}
.lede{{max-width:58ch;font-size:17px;margin:0;color:var(--ink)}}
.lede a{{color:inherit}}
.dlnote{{display:none;font-size:13px;color:var(--muted)}} .no-dl .dlnote{{display:block}}
.changes{{display:grid;grid-template-columns:1fr;gap:22px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding-block:26px;margin-block:10px 34px}}
@media (min-width:820px){{.changes{{grid-template-columns:repeat(3,1fr)}}}}
.changes h4{{font:500 11px/1.4 Jost,sans-serif;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}}
.changes ul{{margin:0;padding-left:18px}} .changes li{{margin-bottom:6px;max-width:44ch}}
.cmpwrap{{display:grid;gap:28px;margin-bottom:40px}}
.cmp{{margin:0}} .cmp>figcaption{{margin-bottom:10px;color:var(--muted)}}
.trio{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.trio span{{display:block;margin-top:6px;font:500 10.5px/1.3 Jost,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}}
.pick{{display:grid;gap:14px;justify-items:center;text-align:center;padding-block:10px 22px}}
.seg{{display:inline-flex;border:1px solid var(--ink);border-radius:999px;padding:3px;gap:3px}}
.seg button{{border:0;background:none;color:var(--ink);padding:10px 16px;border-radius:999px;cursor:pointer}}
.seg button[aria-pressed="true"]{{background:var(--ink);color:var(--panel)}}
.why{{max-width:60ch;margin:0;color:var(--muted);font-size:14px}}
nav{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--ground);display:flex;justify-content:center;flex-wrap:wrap;gap:4px 22px;padding-block:12px;border-bottom:1px solid var(--line)}}
nav a{{color:var(--ink);text-decoration:none;font:500 11px/1 Jost,sans-serif;letter-spacing:.24em;text-transform:uppercase}}
nav a:hover,nav a:focus-visible{{color:var(--gold)}}
.camp{{margin-top:44px}}
.band{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:14px;padding:26px 24px;border-radius:2px}}
.band p{{margin:6px 0 0}} .band .eyebrow{{color:inherit;opacity:.7}}
.peach .band{{background:var(--peach);color:var(--peach-ink)}} .sage .band{{background:var(--sage);color:var(--sage-ink)}} .lilac .band{{background:var(--lilac);color:var(--lilac-ink)}}
.prod{{display:grid;grid-template-columns:1fr;gap:18px;padding-block:26px;border-bottom:1px solid var(--line)}}
@media (min-width:900px){{.prod{{grid-template-columns:270px 1fr}}}}
.info p{{margin:0 0 8px}}
.line{{font-size:20px;line-height:1.2}}
.price{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font:500 16px/1 Jost,sans-serif;letter-spacing:.12em;font-variant-numeric:tabular-nums}}
.stock{{font-size:10px;letter-spacing:.14em;padding:5px 8px;border:1px solid currentColor;border-radius:99px}}
.stock.ok{{color:var(--ok)}} .stock.mid{{color:var(--mid)}} .stock.low{{color:var(--low)}}
.url{{font-size:12.5px;word-break:break-all;color:var(--muted)}}
.imgs{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}}
@media (min-width:720px){{.imgs{{grid-template-columns:minmax(0,.72fr) minmax(0,1fr) minmax(0,1.3fr)}}}}
.car{{grid-column:1/-1;min-width:0}} @media (min-width:720px){{.car{{grid-column:auto}}}}
figure{{margin:0;min-width:0}}
.thumb,.card{{display:block;padding:0;border:0;background:none;cursor:zoom-in;width:100%}}
.thumb img,.card img{{display:block;width:100%;height:auto;border-radius:1px;box-shadow:0 1px 2px rgb(0 0 0 / .10)}}
figcaption,.cap{{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:6px;color:var(--muted);margin-top:8px}}
.cards{{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x mandatory}}
.card{{flex:0 0 46%;max-width:190px;position:relative;scroll-snap-align:start}}
.card span{{position:absolute;left:6px;top:6px;font:500 10px/1 Jost,sans-serif;background:var(--panel);color:var(--ink);padding:4px 6px;border-radius:99px}}
button.dl,button.dlzip,button.copy{{font:500 11px/1 Jost,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:var(--ink);background:none;border:1px solid var(--ink);border-radius:999px;padding:8px 12px;cursor:pointer}}
button.dl:hover,button.dlzip:hover,button.copy:hover{{background:var(--ink);color:var(--panel)}}
button:focus-visible,a:focus-visible{{outline:2px solid var(--gold);outline-offset:2px}}
.no-dl button.dl,.no-dl button.dlzip{{display:none}}
.notes{{margin-top:56px;display:grid;gap:22px}} .notes .cols{{display:grid;grid-template-columns:1fr;gap:22px}} @media (min-width:860px){{.notes .cols{{grid-template-columns:repeat(3,1fr)}}}}
.notes p{{margin:0 0 10px;max-width:60ch}}
#lb{{position:fixed;inset:0;background:rgb(12 10 9 / .94);display:flex;align-items:center;justify-content:center;padding:calc(env(safe-area-inset-top,0px) + 48px) 16px 16px;z-index:20}}
#lb img{{max-width:100%;max-height:100%;object-fit:contain}}
#lb[hidden],#toast[hidden],.dir[hidden]{{display:none!important}}
#lb button{{position:absolute;top:calc(env(safe-area-inset-top,0px) + 10px);right:14px;font:500 11px Jost,sans-serif;letter-spacing:.18em;text-transform:uppercase;background:#fff;color:#111;border:0;padding:9px 13px;border-radius:99px;cursor:pointer}}
#toast{{position:fixed;left:50%;bottom:calc(env(safe-area-inset-bottom,0px) + 18px);transform:translateX(-50%);background:var(--ink);color:var(--panel);font:500 13px Jost,sans-serif;padding:10px 16px;border-radius:99px;z-index:30;max-width:calc(100% - 32px)}}
</style>
<div class="wrap">
  <header class="top">
    <div class="logo" role="img" aria-label="Naira"></div>
    <p class="eyebrow">Naira Petite · Apricot · Sage · Lilac</p>
    <h1>Colour Camps 2.0</h1>
    <p class="lede">The same fifteen verified photographs, with everything that competed with them taken away. Two quiet directions are below; flip between them and pick one. The first version is still <a href="{V1_URL}" target="_blank" rel="noopener">here</a> for reference.</p>
    <p class="dlnote">Saving files isn't available in this view. Open the page on claude.ai to save the ads.</p>
  </header>

  <section class="changes" aria-label="What changed">
    <div><h4>Taken away</h4><ul>
      <li>The giant camp word laid across every piece</li>
      <li>Price stickers, paint chips, stamps and postmarks</li>
      <li>The Shop button. Meta adds its own under every ad</li>
      <li>The second price, the spec line and the page counters</li>
      <li>Two of the four typefaces, and the tint behind the text</li></ul></div>
    <div><h4>Kept</h4><ul>
      <li>Every photograph exactly as verified against its listing</li>
      <li>The three colour worlds, carried by the photographs</li>
      <li>Names, prices and stock from Shopify</li>
      <li>One verified fact per carousel card, in the listing's own words</li></ul></div>
    <div><h4>Added</h4><ul>
      <li>The website's own type: Velista for names, Jost for prices</li>
      <li>The listing's opening line in italic, as the brand's voice</li>
      <li>One ink per camp, tone on tone, and one mat colour per camp</li>
      <li>Stories kept clear of the top 250 px and the reply bar at the bottom</li></ul></div>
  </section>

  <section class="cmpwrap" aria-label="Before and after">{compare}</section>

  <section class="pick" id="pick">
    <p class="eyebrow">Choose a direction</p>
    <div class="seg" role="group" aria-label="Direction">
      <button type="button" data-d="framed" aria-pressed="true">Framed · recommended</button>
      <button type="button" data-d="quiet" aria-pressed="false">Full-bleed</button>
    </div>
    <p class="why" id="why">Framed sets each photograph on a mat in its camp colour, like a page from a lookbook. It reads as one campaign, and the words always sit on a clean ground.</p>
  </section>
  <nav aria-label="Camps"><a href="#" data-cam="peach">Apricot</a><a href="#" data-cam="sage">Sage</a><a href="#" data-cam="lilac">Lilac</a><a href="#notes">Notes</a></nav>
  {direction("framed", "2.0 · Framed")}
  {direction("quiet", "2.0 · Full-bleed")}

  <section class="notes" id="notes">
    <h2>Notes</h2>
    <div class="cols">
      <div><h3>Why framed</h3><p>The mat does three jobs: it carries the camp colour, keeps every line of type on a clean ground, and gives all fifteen products one shape in the feed. It costs a little photo size, which small, precious pieces can afford.</p></div>
      <div><h3>When full-bleed wins</h3><p>Full-bleed shows the photograph at its biggest and stops the thumb faster, especially in Stories. Where a caption falls on texture, a soft haze sits behind the words so they stay readable without a visible box.</p></div>
      <div><h3>Running it</h3><p>Upload the story and feed versions as one ad and let Meta place them. Use the carousel for pieces with 3–5 units and cap spend. Pause any ad at 2 units. Woven Gold Hoops, Toggle Link Chain and Prism Rivière (77–80 units) can run always-on.</p></div>
    </div>
  </section>
</div>
<div id="lb" hidden><button type="button" id="lbx">Close</button><img alt=""></div>
<div id="toast" hidden role="status"></div>
<script>
(function(){{
  var DL=null,busy=false;
  var WHY={{framed:"Framed sets each photograph on a mat in its camp colour, like a page from a lookbook. It reads as one campaign, and the words always sit on a clean ground.",
            quiet:"Full-bleed lets the photograph fill the frame, with only the wordmark, the name and the price on it. It is the most immersive, and strongest in Stories."}};
  function toast(t){{var e=document.getElementById('toast');e.textContent=t;e.hidden=false;clearTimeout(e._t);e._t=setTimeout(function(){{e.hidden=true}},3200)}}
  function why(e){{var c=e&&e.code;if(c==='declined')return null;if(c==='rate_limited')return 'Another save is waiting for you. Finish it, then try again.';
    if(c==='extension_not_enabled'||c==='rejected_extension')return 'This file type cannot be saved from this view.';if(c==='too_large')return 'That file is too large for this view.';return 'Saving is not available right now.'}}
  if(window.claude&&window.claude.use){{window.claude.use('downloads').then(function(d){{DL=d;if(!d)document.body.classList.add('no-dl')}}).catch(function(){{document.body.classList.add('no-dl')}})}}else{{document.body.classList.add('no-dl')}}
  async function saveBlob(n,b){{try{{await DL.save({{filename:n,data:b}});toast('Saved '+n)}}catch(e){{var m=why(e);if(m)toast(m)}}}}
  async function savePath(p){{if(!DL||busy)return;busy=true;try{{var r=await fetch(p);if(!r.ok)throw 0;await saveBlob(p.split('/').pop(),await r.blob())}}catch(e){{toast('Could not load that file. Reload the page and try again.')}}finally{{busy=false}}}}
  async function saveZip(paths,name){{if(!DL||busy)return;if(!window.JSZip){{toast('The zip tool did not load. Save files one by one.');return}}busy=true;toast('Packing '+paths.length+' files…');
    try{{var z=new JSZip();for(var i=0;i<paths.length;i++){{var r=await fetch(paths[i]);if(!r.ok)throw 0;z.file(paths[i].split('/').pop(),await r.blob())}}
    await saveBlob(name,await z.generateAsync({{type:'blob',compression:'STORE'}}))}}catch(e){{toast('Could not pack those files. Try saving them one by one.')}}finally{{busy=false}}}}
  function setDir(d){{document.querySelectorAll('.dir').forEach(function(x){{x.hidden=x.dataset.dir!==d}});
    document.querySelectorAll('.seg button').forEach(function(b){{b.setAttribute('aria-pressed',String(b.dataset.d===d))}});
    document.getElementById('why').textContent=WHY[d];try{{localStorage.setItem('cc2dir',d)}}catch(e){{}}}}
  try{{var s=localStorage.getItem('cc2dir');if(s==='quiet'||s==='framed')setDir(s)}}catch(e){{}}
  document.addEventListener('click',function(ev){{
    var a=ev.target.closest('a[data-cam]');if(a){{ev.preventDefault();var cur=document.querySelector('.dir:not([hidden])').dataset.dir;var el=document.getElementById(cur+'-'+a.dataset.cam);if(el)el.scrollIntoView({{behavior:'smooth'}});return}}
    var t=ev.target.closest('button');if(!t)return;
    if(t.dataset.d){{setDir(t.dataset.d);return}}
    if(t.classList.contains('dl')){{savePath(t.dataset.path);return}}
    if(t.classList.contains('dlzip')){{saveZip(JSON.parse(t.dataset.paths),t.dataset.name);return}}
    if(t.classList.contains('copy')){{var v=t.dataset.copy;if(navigator.clipboard)navigator.clipboard.writeText(v).then(function(){{toast('Link copied')}},function(){{toast(v)}});else toast(v);return}}
    if(t.dataset.full){{var lb=document.getElementById('lb');lb.querySelector('img').src=t.dataset.full;lb.hidden=false;document.getElementById('lbx').focus();return}}
    if(t.id==='lbx'){{document.getElementById('lb').hidden=true}}
  }});
  document.getElementById('lb').addEventListener('click',function(e){{if(e.target.id==='lb')e.currentTarget.hidden=true}});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')document.getElementById('lb').hidden=true}});
}})();
</script>'''
open(f"{ART}/index.html", "w").write(page)
print("index.html", round(len(page) / 1e3), "KB")
