"""Builds the Naira Ten review page from deck.json."""
import base64, html, json
from pathlib import Path
T = Path(__file__).resolve().parent.parent
S = T.parent
deck = json.load(open(T / 'out' / 'deck.json'))
E = lambda s: html.escape(str(s), quote=False)
velista = base64.b64encode((S / 'labels' / 'fonts' / 'Velista.ttf').read_bytes()).decode()
TOKEN = {'EARRINGS': 'haldi', 'RINGS': 'sindoor', 'NECKLACES': 'neelam', 'BRACELETS': 'rani', 'SHOP ALL': 'mehendi'}


def inr(n):
    s = str(int(round(n)))
    if len(s) <= 3: return '₹' + s
    head, tail = s[:-3], s[-3:]; parts = []
    while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
    return '₹' + ','.join([head] + parts) + ',' + tail


def chip(label):
    return f"<span class='chip c-{TOKEN[label]}'><i></i>{E(label)}</span>"


def pics(a):
    feeds = [f for f in a['files'] if f.endswith('_feed.jpg')]
    story = [f for f in a['files'] if f.endswith('_story.jpg')]
    cap = ['card 1', 'card 2', 'card 3'] if len(feeds) > 1 else ['feed 4:5']
    out = ''.join(f"<figure class='feed'><img src='ads/{f}' alt='{E(a['hook'])}, {c}' width='720' height='900'><figcaption>{c}</figcaption></figure>" for f, c in zip(feeds, cap))
    out += ''.join(f"<figure class='story'><img src='ads/{f}' alt='{E(a['hook'])}, story' width='720' height='1280'><figcaption>story 9:16</figcaption></figure>" for f in story)
    return f"<div class='pics{' carousel' if len(feeds) > 1 else ''}'>{out}</div>"


def section(n, a):
    piece = (f"<b>{E(a['piece_title'])}</b> · {inr(a['price'])} · {a['stock']} in stock" if a['piece_title'] else '<b>Ten pieces, four collections</b> · 121 in stock')
    prim = E(a['primary']).replace('\n', '<br>')
    return f"""
<section class='ad' id='a{n:02d}'>
  <header class='adh'>
    <span class='no'>{n:02d}</span>
    <div class='adt'>
      <p class='meta'>{chip(a['collection'])}<span class='tech'>{E(a['technique'])}</span><span class='layer'>{E(a['layer'])}</span></p>
      <h2>{E(a['hook'])}</h2>
      <p class='piece'>{piece}</p>
    </div>
  </header>
  {pics(a)}
  <div class='cols'>
    <div>
      <h3>The idea</h3><p>{E(a['lineage'])}</p>
      <h3>The edit</h3><p>{E(a['edit'])}</p>
      <h3>Why this one</h3><p>{E(a['why'])}</p>
    </div>
    <div class='copy'>
      <h3>For Ads Manager</h3>
      <dl>
        <dt>Headline</dt><dd>{E(a['headline'])}</dd>
        <dt>Primary text</dt><dd>{prim}</dd>
        <dt>Description</dt><dd>{E(a['description'])}</dd>
        <dt>Button</dt><dd>Shop now</dd>
        <dt>Link</dt><dd><code>{E(a['link'])}</code></dd>
      </dl>
    </div>
  </div>
</section>"""


ads = deck['ads']; plan = deck['plan']
index = ''.join(f"<a class='thumb' href='#a{i:02d}'><img src='ads/{[f for f in a['files'] if f.endswith('_feed.jpg')][0]}' alt='' width='720' height='900'>"
                f"<span><b>{i:02d}</b> {E(a['technique'])}</span></a>" for i, a in enumerate(ads, 1))
legend = ''.join(f"<li>{chip(k)}<span>{v}</span></li>" for k, v in [('EARRINGS', 'Haldi yellow'), ('RINGS', 'Sindoor red'), ('NECKLACES', 'Neelam blue'), ('BRACELETS', 'Rani pink'), ('SHOP ALL', 'Mehendi green')])
refs = [
    ('KFC "FCK", Mother London', 'Cannes Lions Gold, Print & Publishing 2018', 'The brand rewrites its own word. Ad 01 lets the ring rewrite "I do".', 'https://www.campaignlive.co.uk/article/kfcs-were-sorry-mother-wins-cannes-lions-gold-print-publishing/1485469'),
    ('McDonald\'s "Follow the Arches", Cossette', 'Cannes Lions Outdoor Grand Prix 2018', 'A cropped mark is enough when it is iconic. The ring as a letter, the bangle as an X.', 'https://strategyonline.ca/?p=143409'),
    ('Penny "Price Packs", Serviceplan', 'Cannes Lions Print & Publishing Grand Prix 2025', 'The price is the design. Ad 10 makes the price out of the product\'s own surface.', 'https://www.moreaboutadvertising.com/news/press-print-grand-prix-german-store-penny-wins-for-price-packs/'),
    ('Burger King "Moldy Whopper"', 'Cannes Lions Outdoor Grand Prix 2021', 'Show the material truth instead of describing it. The tape measure in ad 07, the drawing in ad 04.', 'https://www.contagious.com/news-and-views/cannes-lions-outdoor-winners-2021'),
    ('Absolut Warhol, 1985', 'Pop-art repetition in advertising', 'Repetition as the message. Ad 02 repeats the outfit and keeps the hoops.', 'https://shots.net/news/view/andy-warhols-absolut-ly-fabulous-alco-pop-art'),
    ('Static ad anatomy, 2026', 'DTC formats that outperform', 'Callouts and comparison carry statics. The anatomy drawing and the shade chips are both.', 'https://segwise.ai/blog/anatomy-high-converting-static-ad'),
]
ref_html = ''.join(f"<li><a href='{u}'>{E(a)}</a><span class='aw'>{E(b)}</span><span>{E(c)}</span></li>" for a, b, c, u in refs)
adsets = ''.join(f"<li><b>{E(s['name'])}</b><br>{E(s['budget'])}<br><span class='mono'>{' · '.join(s['ads'])}</span></li>" for s in plan['adsets'])

page = f"""<title>The Naira Ten</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* layout: a proof sheet. Index of ten thumbnails, then one proof per ad: files, idea, copy */
@font-face {{ font-family:'Velista'; src:url(data:font/truetype;base64,{velista}) format('truetype'); font-display:swap }}
:root {{ --paper:#F6F1E9; --card:#FFFDF9; --ink:#1F1A14; --mute:#6A6157; --line:#E3DACD; --code:#EFE7DB;
  --haldi:#F2B705; --sindoor:#C1272D; --neelam:#1D3C8F; --rani:#C2185B; --mehendi:#2F6B3A; --on-haldi:#1F1A14; --on-dark:#FBF5EA;
  --display:'Velista','Times New Roman',serif; --sans:'Jost','Helvetica Neue',Arial,sans-serif; --mono:'IBM Plex Mono',ui-monospace,Menlo,monospace; color-scheme:light }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --paper:#15120F; --card:#1D1915; --ink:#F2EBE1; --mute:#B2A695; --line:#3A322A; --code:#26211C; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --paper:#15120F; --card:#1D1915; --ink:#F2EBE1; --mute:#B2A695; --line:#3A322A; --code:#26211C; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-weight:300; font-size:17px; line-height:1.55 }}
.wrap {{ max-width:1200px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:0 }}
a {{ color:inherit }}
h1, h2 {{ font-family:var(--display); font-weight:400; text-wrap:balance; margin:0; letter-spacing:.01em }}
h1 {{ font-size:clamp(56px, 10vw, 128px); line-height:.92 }}
h2 {{ font-size:clamp(32px, 4.4vw, 54px); line-height:1 }}
h3 {{ font-family:var(--mono); font-weight:500; font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--mute); margin:22px 0 6px }}
p {{ margin:0 }}
.mono {{ font-family:var(--mono); font-size:13px; letter-spacing:.04em }}
.eyebrow {{ font-family:var(--mono); font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--mute) }}
header.top {{ padding-block:56px 34px; display:grid; gap:22px }}
.lede {{ font-size:clamp(19px, 2vw, 23px); line-height:1.45; max-width:44em }}
.facts {{ display:flex; flex-wrap:wrap; gap:12px 34px; padding-block:18px; border-top:1px solid var(--line); border-bottom:1px solid var(--line) }}
.facts div {{ display:grid }} .facts b {{ font-family:var(--display); font-weight:400; font-size:34px; line-height:1; font-variant-numeric:tabular-nums }}
.facts span {{ font-family:var(--mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--mute); margin-top:6px }}
.legend {{ list-style:none; margin:0; padding:0; display:flex; flex-wrap:wrap; gap:10px 22px; align-items:center }}
.legend li {{ display:flex; align-items:center; gap:10px; font-size:15px }}
.chip {{ display:inline-flex; align-items:center; gap:8px; font-family:var(--sans); font-weight:500; font-size:12px; letter-spacing:.2em; padding:6px 11px; border-radius:0 0 9px 9px; white-space:nowrap }}
.chip i {{ width:9px; height:9px; border-radius:50%; border:1.6px solid currentColor }}
.c-haldi {{ background:var(--haldi); color:var(--on-haldi) }} .c-sindoor {{ background:var(--sindoor); color:var(--on-dark) }}
.c-neelam {{ background:var(--neelam); color:var(--on-dark) }} .c-rani {{ background:var(--rani); color:var(--on-dark) }} .c-mehendi {{ background:var(--mehendi); color:var(--on-dark) }}
.index {{ display:grid; grid-template-columns:repeat(5, minmax(0, 1fr)); gap:14px; padding-block:30px 10px }}
.thumb {{ text-decoration:none; display:grid; gap:8px }}
.thumb img {{ width:100%; height:auto; display:block; border:1px solid var(--line) }}
.thumb span {{ font-family:var(--mono); font-size:12px; letter-spacing:.04em; color:var(--mute); line-height:1.35 }}
.thumb b {{ color:var(--ink); font-weight:500 }}
.thumb:hover img, .thumb:focus-visible img {{ outline:2px solid var(--ink); outline-offset:2px }}
section {{ padding-block:46px; border-top:1px solid var(--line) }}
.adh {{ display:flex; gap:22px; align-items:flex-start }}
.no {{ font-family:var(--display); font-size:clamp(54px, 7vw, 92px); line-height:.8; color:var(--mute) }}
.adt {{ display:grid; gap:12px; min-width:0 }}
.meta {{ display:flex; flex-wrap:wrap; gap:10px 14px; align-items:center }}
.tech {{ font-family:var(--mono); font-size:13px; letter-spacing:.06em }}
.layer {{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; border:1px solid var(--line); padding:4px 8px; color:var(--mute) }}
.piece {{ color:var(--mute) }} .piece b {{ color:var(--ink); font-weight:500 }}
.pics {{ display:flex; gap:16px; align-items:flex-start; margin-top:26px; overflow-x:auto; padding-bottom:6px }}
.pics figure {{ margin:0; flex:none }}
.pics .feed {{ width:min(430px, 78vw) }} .pics .story {{ width:min(250px, 46vw) }}
.pics.carousel .feed {{ width:min(330px, 70vw) }}
.pics img {{ width:100%; height:auto; display:block; border:1px solid var(--line) }}
figcaption {{ font-family:var(--mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--mute); margin-top:6px }}
.cols {{ display:grid; grid-template-columns:minmax(0, 1fr) minmax(0, 1.15fr); gap:34px; margin-top:8px }}
.cols p {{ max-width:62ch }}
.copy {{ background:var(--card); border:1px solid var(--line); padding:4px 22px 20px }}
dl {{ display:grid; grid-template-columns:110px minmax(0, 1fr); gap:10px 16px; margin:12px 0 0 }}
dt {{ font-family:var(--mono); font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--mute); padding-top:4px }}
dd {{ margin:0; min-width:0 }}
code {{ font-family:var(--mono); font-size:12px; background:var(--code); padding:2px 5px; word-break:break-all }}
.plan {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:26px; margin-top:20px }}
.plan > div {{ min-width:0 }}
.plan ul {{ margin:6px 0 0; padding-left:18px; display:grid; gap:8px }}
.refs {{ list-style:none; padding:0; margin:20px 0 0; display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:18px 26px }}
.refs li {{ display:grid; gap:4px; padding-top:12px; border-top:1px solid var(--line); min-width:0 }}
.refs a {{ font-weight:500; text-underline-offset:3px }}
.refs .aw {{ font-family:var(--mono); font-size:12px; color:var(--mute) }}
footer {{ padding-block:40px 60px; color:var(--mute); font-size:14px; border-top:1px solid var(--line) }}
@media (max-width:900px) {{ .index {{ grid-template-columns:repeat(3, minmax(0, 1fr)) }} .cols {{ grid-template-columns:1fr }} }}
@media (max-width:560px) {{ .index {{ grid-template-columns:repeat(2, minmax(0, 1fr)) }} .adh {{ flex-direction:column; gap:8px }} dl {{ grid-template-columns:1fr }} }}
@media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior:smooth }} }}
</style>

<div class='wrap'>
<header class='top'>
  <p class='eyebrow'>Naira · Meta concept set · wedding season · November 2026</p>
  <h1>THE NAIRA TEN</h1>
  <p class='lede'>Ten ads, ten different techniques, each borrowed from award-winning print and outdoor work and each built on a piece with 32 to 80 units in stock. Every card carries a tab in its collection's colour, so the feed reads as one system.</p>
  <div class='facts'>
    <div><b>10</b><span>ads</span></div><div><b>22</b><span>files, feed and story</span></div><div><b>10</b><span>techniques</span></div>
    <div><b>32–80</b><span>units per hero</span></div><div><b>6</b><span>new generations used</span></div><div><b>₹1,000</b><span>per day, 10:10 IST</span></div>
  </div>
  <ul class='legend' aria-label='Collection colour code'>{legend}</ul>
</header>
<nav class='index' aria-label='The ten ads'>{index}</nav>
{''.join(section(i, a) for i, a in enumerate(ads, 1))}
<section id='plan'>
  <h2>THE PLAN</h2>
  <div class='plan'>
    <div><h3>Campaign</h3><p><b>{E(plan['name'])}</b></p><p>{E(plan['objective'])}. {E(plan['budget'])}.</p><p style='margin-top:8px'>{E(plan['launch'])}</p></div>
    <div><h3>Ad sets</h3><ul>{adsets}</ul></div>
    <div><h3>Bars to clear</h3><ul>{''.join(f'<li>{E(k)}</li>' for k in plan['kpis'])}</ul></div>
    <div><h3>Rules</h3><ul>{''.join(f'<li>{E(r)}</li>' for r in plan['rules'])}</ul></div>
  </div>
  <h3 style='margin-top:30px'>What the account already shows</h3>
  <ul style='margin:6px 0 0;padding-left:18px;display:grid;gap:6px;max-width:70ch'>
    <li>Catalogue grids at current prices: ROAS 2.6 to 2.7 and ₹454 to ₹493 per purchase, the best in the account. Ad 03 is that format.</li>
    <li>Saturated 9:16 stills took the highest link CTR, 4.0%. Ads 05 and 09 are built for Stories first.</li>
    <li>Prism and rainbow pieces carry the highest static CTR, 3.1 to 3.2%. Ad 05 puts the Prism Rivière on the dance floor.</li>
    <li>Influencer reels and broad prospecting without product cost ₹3,000 or more per purchase. Nothing here depends on them.</li>
  </ul>
</section>
<section id='research'>
  <h2>WHERE THE IDEAS COME FROM</h2>
  <ul class='refs'>{ref_html}</ul>
</section>
<footer>Built 5 November 2026 from the live nairaflore.com prices and descriptions, the Shopify stock sheet of 4 November and the Naira Higgsfield library. Files, scripts and prompts: creative/naira-ten in the naira-scroll repository. Nothing was created or changed in Meta.</footer>
</div>
"""
(T / 'page').mkdir(exist_ok=True)
(T / 'page' / 'index.html').write_text(page)
print('page', len(page) // 1000, 'KB')
