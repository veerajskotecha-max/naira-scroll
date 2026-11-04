"""Builds the campaign page (artifact) from deck.json, analysis.json, live.json and the stock snapshot."""
import base64, html, json, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D / "build")); import spec
deck = json.load(open(D / "out" / "deck.json"))
an = json.load(open(D / "data" / "analysis.json"))
live = json.load(open(D / "data" / "live.json")); stock = json.load(open(D / "data" / "inventory.json"))
velista = base64.b64encode((D.parent / "labels" / "fonts" / "Velista.ttf").read_bytes()).decode()
E = lambda s: html.escape(str(s), quote=False)

def inr(n):
    s = str(int(round(n)))
    if len(s) <= 3: return "₹" + s
    head, tail = s[:-3], s[-3:]
    out = []
    while len(head) > 2: out.insert(0, head[-2:]); head = head[:-2]
    return "₹" + ",".join([head] + out) + "," + tail

ads = {a["id"]: a for a in deck["ads"]}
plan = deck["plan"]
heroes = [(a["piece"], a["price"], a["stock"], a["id"], a["collection"]) for a in deck["ads"] if a["piece"]]
top = sorted(((stock[h], h, v["type"], v["price"]) for h, v in live.items()), reverse=True)[:16]
under = [(stock[h], h, v["price"]) for h, v in live.items() if v["price"] < 1000]
cols = {}
for h, v in live.items(): cols.setdefault(v["type"], []).append(v["price"])

def img(f, alt):
    return f"<img src='ads/{f}' alt='{E(alt)}' loading='lazy'>"

def ad_block(a):
    band, on, _ = spec.COL[a["colour"]]
    feed = [f for f in a["files"] if f.endswith("_feed.jpg")]; story = [f for f in a["files"] if f.endswith("_story.jpg")]
    if a["kind"] == "carousel":
        pics = "".join(f"<figure>{img(f, f)}<figcaption>{E(f.split('_')[1] + ' · ' + f.split('_')[2])}</figcaption></figure>" for f in feed)
        pics += f"<figure class='tall'>{img(story[0], 'story cover')}<figcaption>story cover</figcaption></figure>"
    else:
        pics = f"<figure>{img(feed[0], a['hook'])}<figcaption>feed 4:5</figcaption></figure><figure class='tall'>{img(story[0], a['hook'])}<figcaption>story 9:16</figcaption></figure>"
    piece = f"<p class='piece'><b>{E(a['piece'])}</b> · {inr(a['price'])} · <b>{a['stock']} in stock</b></p>" if a["piece"] else ""
    drafts = "".join(f"<li{' class=chosen' if i == 0 else ''}>{E(d)}</li>" for i, d in enumerate(a["drafts"]))
    return f"""
<article class='ad' id='{a['id']}'>
  <header class='adhead'>
    <span class='swatch' style='background:{band};color:{on}'>{a['id']}</span>
    <div>
      <p class='eyebrow'>{E(a['layer'])} · {E(a['kind'])} · links to <a href='{E(a['link'])}'>{E(a['collection'])}</a></p>
      <h3>{E(a['hook'])}</h3>
      {piece}
    </div>
  </header>
  <div class='pics'>{pics}</div>
  <div class='copy'>
    <dl>
      <dt>Band</dt><dd>{E(a['eyebrow'])}{(' · <b>' + E(a['title']) + '</b>') if a['title'] else ''}<br><i>{E(a['hook'])}</i><br>{E(a['sub'])}</dd>
      <dt>Headline</dt><dd>{E(a['headline'])}</dd>
      <dt>Primary text</dt><dd class='primary'>{E(a['primary']).replace(chr(10), '<br>')}</dd>
      <dt>Description</dt><dd>{E(a['description'])}</dd>
      <dt>Button</dt><dd>Shop now → <code>{E(a['link'])}</code></dd>
      <dt>Why this card</dt><dd>{E(a['why'])}</dd>
      <dt>Hook drafts</dt><dd><ol class='drafts'>{drafts}</ol></dd>
    </dl>
  </div>
</article>"""

layers = {"Inform": [], "Desire": [], "Convert": []}
for a in deck["ads"]: layers[a["layer"]].append(a)
layer_text = {
 "Inform": "The customer learns what Naira is: 121 pieces in stock from ₹599, four collections, 18k gold PVD on surgical steel, waterproof. The carousel shows the range; the Waterproof card explains the craft in one line.",
 "Desire": "Five wedding functions, five dress-code colours, five deepest-stocked pieces. Each card tells the customer which function the piece is for and gives one fact (fit, length, stone, coating) so the purchase feels informed, not impulsive.",
 "Convert": "The reasons to order now: any three pieces at 20% off with the maths shown, insured delivery in 3 to 5 days with pay on delivery and the gift box, and 42 pieces under ₹1,000 for the plus-one budget.",
}

def table(head, rows, cls=""):
    th = "".join(f"<th>{E(h)}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<div class='tbl'><table class='{cls}'><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>"

comp_rows = [(c["n"], E(c["brand"]), E(c["what"]), c["hook"], c["offer"], c["product"], c["brand_"], c["cta"], f"<b>{c['score']:.1f}</b>", E(c["note"])) for c in an["competitors"]]
meta_w = [(E(r[0]), r[1], r[2], r[3], r[4]) for r in an["meta"]["winners"]]
meta_l = [(E(r[0]), r[1], r[2], r[3], r[4]) for r in an["meta"]["losers"]]
twenty = [(E(t[0]), f"{t[1]:.2f}", E(t[2])) for t in an["twenty"]]
stock_rows = [(E(live[h]["title"]), E(t), inr(p), s, "hero" if any(h == x[0] for x in heroes) else ("tile" if any(h in (ad.get("grid", []) + ad.get("trio", []) + ad.get("cover", []) + ad.get("cover_extra", []) + sum([c[2] for c in ad.get("cards", [])], [])) for ad in spec.ADS) else "")) for s, h, t, p in top]
gen_rows = [
 ("D1 feed", "g01", "Verdant Circlet Studs on an open palm in fresh green mehendi, cone at the edge", "used"),
 ("D1 alternate", "g02", "The studs on the knuckles of a mehendi hand", "held"),
 ("D1 story", "g03", "Ear crop, green raw-silk blouse, a mehendi hand tucking the hair", "used"),
 ("D2 feed", "g04", "Woven Gold Hoop on the ear with haldi smeared on the cheek and jaw", "used"),
 ("D2 story, take 1", "g05", "Hoops in a brass thali of turmeric: rendered three hoops, so it was redone", "redone"),
 ("D2 story", "g11", "The same scene with exactly two hoops", "used"),
 ("D3 feed, take 1", "g06", "Prism Rivière on a wrist mid-dance: glass bangles crept onto the other wrist, so it was redone", "redone"),
 ("D3 alternate", "g12", "The redo with one hand only; the feed card uses the brand's prism-and-rainbow still life instead", "held"),
 ("D3 story", "g13", "The bracelet on magenta raw silk with marigolds and fairy-light bokeh", "used"),
 ("D4 feed", "g09", "Cushion Halo Ring on a hand on red silk, kumkum and rice at the fingertips", "used"),
 ("D5 feed", "g07", "Baguette Tennis Necklace across the keys of a grand piano, two coupes behind", "used"),
 ("D5 story", "g08", "The necklace at the base of the neck over a black halter", "used"),
 ("I2 feed", "g10", "Brushed Gold Huggie under the shower, one drop hanging from the band", "used"),
]
steps = [
 "Ads Manager → Create → Sales. Name it exactly as the plan: <b>Naira · The Guest List · Shop All + collections · ₹1,000/day · Nov 2026</b>. Campaign budget on, ₹1,000 a day.",
 "Schedule: start at <b>10:10 IST</b> on launch day, no end date. Conversion event Purchase on the nairaflore.com pixel; check the event fires on a test order first.",
 "Ad set 1, Cold: all India, women 22 to 45, Advantage+ audience on, Advantage+ placements on, minimum ₹600 a day. Ad set 2, Warm: website visitors 30 days, Instagram engagers 60 days, add to cart 14 days, purchasers 180 days excluded, frequency cap 2 per 7 days.",
 "Upload the 24 files from the ads folder. For each ad, put the 4:5 file on Feed placements and the 9:16 file on Stories and Reels (Advantage+ creative → placement customisation). The carousel takes the five feed cards in order, each card with its own collection link.",
 "Paste the headline, primary text and description from the ad blocks above. Website URL is the collection link with the UTM string appended; the UTM content is the ad ID, so Shopify reports read I1, D1 and so on.",
 "Check the discount codes BUY2 (10%) and BUY3 (20%) are live in Shopify before 10:10, with no minimum that excludes the ₹599 pieces.",
 "Day 2: nothing. Day 3: read link CTR per ad; anything under 1.2% at 1,500 impressions goes off. Day 7: keep the top five by cost per purchase, swap the bottom three for the reserve hooks. Day 14: full review against the KPIs, then decide on a second carousel.",
 "Every Monday: check the stock of the seven heroes in Shopify. Under 15 units, swap the piece for the next one in its carousel card and keep the hook.",
]
nav = "".join(f"<a href='#{k}'>{v}</a>" for k, v in [("plan", "Plan"), ("ads", "The ten ads"), ("stock", "Stock"), ("meta", "Meta data"), ("competitors", "Competitors"), ("photos", "Photography"), ("launch", "Launch"), ("brief", "Brief")])

page = f"""<title>The Guest List</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap">
<style>
/* layout: a cream invitation card on a long scroll, each function card shown as the suite it belongs to */
@font-face {{ font-family:'Velista'; src:url(data:font/truetype;base64,{velista}) format('truetype'); font-display:swap }}
:root {{ --bg:#FBF7F1; --card:#FFFFFF; --fg:#1F1A14; --mute:#6B6259; --line:#E6DED2; --sage:#CFDFD9; --sage-ink:#2F5D4C; --coral:#C86F58; --marigold:#E9B414; --ink:#16213B;
  --display:'Velista','Cormorant Garamond',Georgia,serif; --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif; --sans:'Jost','Helvetica Neue',Arial,sans-serif; color-scheme:light }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#15120F; --card:#1F1A16; --fg:#F3EBDF; --mute:#B5A999; --line:#3A322B; --sage:#2A4A41; --sage-ink:#BFD9CF; --coral:#E09A86; --marigold:#E9B414; --ink:#F3EBDF; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#15120F; --card:#1F1A16; --fg:#F3EBDF; --mute:#B5A999; --line:#3A322B; --sage:#2A4A41; --sage-ink:#BFD9CF; --coral:#E09A86; --marigold:#E9B414; --ink:#F3EBDF; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--sans); font-weight:300; font-size:17px; line-height:1.5; margin:0 }}
.wrap {{ max-width:1180px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:0 }}
a {{ color:var(--sage-ink); text-decoration-thickness:1px; text-underline-offset:3px }}
h1,h2,h3 {{ text-wrap:balance; margin:0 }}
h1 {{ font-family:var(--display); font-weight:400; font-size:clamp(56px, 11vw, 136px); line-height:.95; letter-spacing:.01em }}
h2 {{ font-family:var(--display); font-weight:400; font-size:clamp(34px, 5vw, 56px); line-height:1; margin-bottom:18px }}
h3 {{ font-family:var(--serif); font-style:italic; font-weight:500; font-size:clamp(28px, 3.4vw, 40px); line-height:1.1 }}
p {{ margin:0 }}
.eyebrow {{ font-family:var(--sans); font-weight:500; font-size:12px; letter-spacing:.24em; text-transform:uppercase; color:var(--mute) }}
.lede {{ font-family:var(--serif); font-size:clamp(22px, 2.6vw, 30px); line-height:1.3; max-width:34em }}
nav.top {{ position:sticky; top:env(safe-area-inset-top, 0px); z-index:5; background:var(--bg); border-bottom:1px solid var(--line) }}
nav.top .wrap {{ display:flex; gap:22px; overflow-x:auto; padding-block:12px; font-size:13px; letter-spacing:.14em; text-transform:uppercase; font-weight:500; white-space:nowrap }}
nav.top a {{ color:var(--fg); text-decoration:none }}
body::before {{ content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top, 0px); z-index:10; background:var(--bg) }}
header.hero {{ padding-block:56px 40px; display:grid; gap:22px }}
.facts {{ display:flex; flex-wrap:wrap; gap:14px 36px; padding-block:18px; border-top:1px solid var(--line); border-bottom:1px solid var(--line) }}
.facts div {{ display:grid; gap:2px }} .facts b {{ font-family:var(--serif); font-weight:600; font-size:30px; line-height:1; font-variant-numeric:tabular-nums }}
.facts span {{ font-size:12px; letter-spacing:.18em; text-transform:uppercase; color:var(--mute) }}
section {{ padding-block:48px; border-top:1px solid var(--line) }}
.layers {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:18px; margin-top:12px }}
.layer {{ background:var(--card); border:1px solid var(--line); padding:22px; display:grid; gap:12px; align-content:start; min-width:0 }}
.layer h4 {{ font-family:var(--display); font-weight:400; font-size:30px; margin:0; line-height:1 }}
.layer ul {{ margin:0; padding-left:18px; display:grid; gap:4px }}
.chips {{ display:flex; flex-wrap:wrap; gap:8px }}
.chip {{ display:inline-block; font-size:12px; letter-spacing:.12em; text-transform:uppercase; padding:6px 10px; border:1px solid var(--line); color:var(--fg) }}
.plan {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:18px }}
.plan div {{ min-width:0 }} .plan ul {{ padding-left:18px; margin:6px 0 0; display:grid; gap:6px }}
.ad {{ background:var(--card); border:1px solid var(--line); margin-top:26px; display:grid; gap:18px; padding:22px }}
.adhead {{ display:flex; gap:16px; align-items:flex-start }}
.swatch {{ flex:none; width:58px; height:58px; display:grid; place-items:center; font-family:var(--display); font-size:24px }}
.piece {{ margin-top:6px; color:var(--mute) }} .piece b {{ color:var(--fg); font-weight:500 }}
.pics {{ display:flex; gap:14px; overflow-x:auto; padding-bottom:6px }}
.pics figure {{ margin:0; flex:none; width:min(300px, 70vw) }} .pics figure.tall {{ width:min(240px, 56vw) }}
.pics img {{ width:100%; height:auto; display:block; border:1px solid var(--line) }}
figcaption {{ font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--mute); margin-top:6px }}
dl {{ display:grid; grid-template-columns:150px 1fr; gap:10px 18px; margin:0 }}
dt {{ font-size:12px; letter-spacing:.18em; text-transform:uppercase; color:var(--mute); padding-top:4px }} dd {{ margin:0; min-width:0 }}
dd i {{ font-family:var(--serif); font-size:24px; font-weight:500 }}
code {{ font-family:ui-monospace, SFMono-Regular, Menlo, monospace; font-size:13px; word-break:break-all; background:var(--bg); padding:2px 5px }}
.drafts {{ margin:0; padding-left:20px; display:grid; gap:2px }} .drafts .chosen {{ font-weight:500 }}
.tbl {{ overflow-x:auto; margin-top:14px; border:1px solid var(--line); background:var(--card) }}
table {{ border-collapse:collapse; width:100%; font-size:15px; min-width:640px }}
th, td {{ text-align:left; vertical-align:top; padding:10px 12px; border-bottom:1px solid var(--line) }} th {{ font-size:12px; letter-spacing:.16em; text-transform:uppercase; color:var(--mute); font-weight:500 }}
td {{ font-variant-numeric:tabular-nums }} tbody tr:last-child td {{ border-bottom:0 }}
.comp td:nth-child(3), .comp td:nth-child(10) {{ min-width:260px }}
.notes {{ display:grid; gap:12px; margin-top:16px; max-width:70ch }}
.notes p {{ padding-left:16px; border-left:3px solid var(--sage) }}
ol.steps {{ padding-left:22px; display:grid; gap:12px; max-width:70ch; margin:14px 0 0 }}
.twocol {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:28px }} .twocol > div {{ min-width:0 }}
.brief p {{ max-width:70ch; margin-top:12px }}
footer {{ padding-block:40px; color:var(--mute); font-size:14px; border-top:1px solid var(--line) }}
@media (max-width:640px) {{ dl {{ grid-template-columns:1fr }} .adhead {{ flex-direction:column }} }}
@media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior:smooth }} }}
</style>

<nav class='top'><div class='wrap'>{nav}</div></nav>
<div class='wrap'>
<header class='hero'>
  <p class='eyebrow'>Naira · Meta campaign · wedding season · November 2026</p>
  <h1>THE GUEST LIST</h1>
  <p class='lede'>One invitation suite, ten ads, three layers. Every card is a wedding function in its dress-code colour, carrying the deepest-stocked piece in its collection and linking to that collection. ₹1,000 a day, campaign budget, launch at 10:10 IST.</p>
  <div class='facts'>
    <div><b>10</b><span>ads, 24 files</span></div><div><b>7</b><span>heroes, 30 to 80 units each</span></div><div><b>121</b><span>pieces in stock, from ₹599</span></div><div><b>₹1,000</b><span>per day, CBO</span></div><div><b>10:10</b><span>IST launch</span></div><div><b>13</b><span>new photographs</span></div>
  </div>
</header>

<section id='plan'>
  <h2>THE PLAN</h2>
  <p class='lede'>Inform, then desire, then convert. The customer meets the range, then a function she is dressing for, then a reason to order this week.</p>
  <div class='layers'>
    {"".join(f"<div class='layer'><h4>{E(k.upper())}</h4><p>{E(layer_text[k])}</p><div class='chips'>{''.join(f'<a class=chip href=#{a[chr(105)+chr(100)]}>{a[chr(105)+chr(100)]} · {E(a[chr(104)+chr(111)+chr(111)+chr(107)])}</a>' for a in v)}</div></div>" for k, v in layers.items())}
  </div>
  <div class='plan' style='margin-top:28px'>
    <div><p class='eyebrow'>Campaign</p><p><b>{E(plan['name'])}</b></p><p>{E(plan['objective'])}</p><p>{E(plan['budget'])}</p><p>{E(plan['launch'])}</p></div>
    <div><p class='eyebrow'>Ad sets</p>{"".join(f"<p style='margin-top:8px'><b>{E(s['name'])}</b> · {E(s['budget'])}<br>{' · '.join(s['ads'])}<br><span style='color:var(--mute)'>{E(s['placements'])}</span></p>" for s in plan['adsets'])}</div>
    <div><p class='eyebrow'>KPIs</p><ul>{"".join(f'<li>{E(k)}</li>' for k in plan['kpis'])}</ul></div>
    <div><p class='eyebrow'>Rules</p><ul>{"".join(f'<li>{E(r)}</li>' for r in plan['rules'])}</ul></div>
  </div>
</section>

<section id='ads'>
  <h2>THE TEN ADS</h2>
  <p class='lede'>Each block is one ad as it goes into Ads Manager: the files, the band copy on the card, the headline, primary text, description, button link and the four hooks it was chosen from. Offer on every card: {E(deck['offer'])}.</p>
  {"".join(ad_block(ads[i]) for i in ["I1", "I2", "D1", "D2", "D3", "D4", "D5", "C1", "C2", "C3"])}
</section>

<section id='stock'>
  <h2>STOCK</h2>
  <p class='lede'>Read from Shopify on 4 November 2026: 121 in-stock pieces, none on pre-order. A hero needs at least {spec.MIN_HERO} units; a tile in a grid or carousel at least {spec.MIN_GRID}. The sixteen deepest-stocked pieces and where they appear:</p>
  {table(["Piece", "Collection", "Price", "Units", "In the campaign"], stock_rows)}
  <div class='twocol' style='margin-top:22px'>
    <div><p class='eyebrow'>By collection</p><ul style='padding-left:18px;margin:8px 0 0'>{"".join(f"<li>{E(t)}: {len(ps)} pieces in stock, from {inr(min(ps))}</li>" for t, ps in sorted(cols.items()))}</ul></div>
    <div><p class='eyebrow'>Under ₹1,000</p><p style='margin-top:8px'>{len(under)} pieces, {sum(s for s, _, _ in under)} units. The nine deepest-stocked carry the plus-one grid: {", ".join(E(live[h]['title']) + f" ({s})" for s, h, _ in sorted(under, reverse=True)[:9])}.</p></div>
  </div>
  <div class='notes'><p>Pieces that looked like heroes but are not: Emerald Carré Bracelet (4 units), Heartline Paperclip Necklace (2), Dewdrop Bezel Necklace (5), Pearl Blossom Earrings (5), Petite Pavé Band (4). All were in the first draft and all are out. Baguette Huggies show 46 units but 4 of them are the ruby pictured on the site, so they sit out of the earrings card.</p></div>
</section>

<section id='meta'>
  <h2>WHAT THE ACCOUNT ALREADY KNOWS</h2>
  <p class='lede'>{E(an['meta']['totals'])}</p>
  <div class='twocol'>
    <div><p class='eyebrow' style='margin-top:18px'>What paid</p>{table(["Ad", "Link CTR", "ROAS", "Cost per purchase", "Spend"], meta_w)}</div>
    <div><p class='eyebrow' style='margin-top:18px'>What did not</p>{table(["Campaign", "Link CTR", "ROAS", "Cost per purchase", "Spend"], meta_l)}</div>
  </div>
  <div class='notes'>{"".join(f'<p>{E(l)}</p>' for l in an['meta']['lessons'])}</div>
  <p class='eyebrow' style='margin-top:26px'>Kept from the Naira Twenty (the judge's scores out of 10)</p>
  {table(["Hook", "Score", "What happened to it"], twenty)}
</section>

<section id='competitors'>
  <h2>THE COMPETITION, RATED</h2>
  <p class='lede'>Ten ads from the client's feed, scored out of 10 on five things: the hook (does it stop a thumb), the offer (is the reason to buy clear), the product (can you see what you would get), the brand (would you know whose ad it is with the logo covered) and the button (is the next step obvious). The overall is a weighted read, not an average.</p>
  {table(["#", "Brand", "The ad", "Hook", "Offer", "Product", "Brand", "Button", "Overall", "Reading"], comp_rows, "comp")}
  <div class='notes'>{"".join(f'<p>{E(p)}</p>' for p in an['patterns'])}</div>
</section>

<section id='photos'>
  <h2>PHOTOGRAPHY</h2>
  <p class='lede'>Thirteen new images from Higgsfield, each locked to the product photograph of the piece it sells (one product per frame, countable facts in the prompt, two light sources, real scale). Two were redone. The rest of the cards use the brand's existing library and the shop's plinth photographs for the tiles.</p>
  {table(["Card", "Image", "What it shows", "Status"], [(E(a), E(b), E(c), E(d)) for a, b, c, d in gen_rows])}
  <div class='notes'><p>Library images carried over: the prism-and-rainbow still life (D3 feed), the ring on linen (D4 story), the huggie ear crop (I2 story), the chain in the pink box (C2 feed) and the chain in the train window (C2 story). The prompts for all thirteen generations are in the repo under creative/naira-guest-list/build/prompts.md, ready to re-run for new pieces.</p></div>
</section>

<section id='launch'>
  <h2>LAUNCH</h2>
  <p class='lede'>In order, from Ads Manager to the first review.</p>
  <ol class='steps'>{"".join(f'<li>{s}</li>' for s in steps)}</ol>
</section>

<section id='brief' class='brief'>
  <h2>THE BRIEF FOR THE CLIENT</h2>
  <p class='lede'>What to tell the team, in the words a customer will meet.</p>
  <p><b>The idea.</b> A wedding has five functions and a dress code for each. The Guest List is Naira's invitation suite: one card per function, in that function's colour, with one piece and one fact. It is themed without being a sale, so it can run through the season without a discount war.</p>
  <p><b>Why these pieces.</b> Every hero has between 30 and 80 units in the warehouse, so a good week cannot sell the campaign out, and every tile has at least ten. The pieces were chosen from the stock sheet first and the pictures made second.</p>
  <p><b>What the customer is told.</b> First that Naira has 121 pieces in stock from ₹599 and that the gold is PVD-bonded, waterproof and anti-tarnish. Then which piece suits which function, with one fact she can check on the product page (the 10mm stone, the 36cm length, the adjustable band). Then how to order: any three pieces at 20% off, insured delivery in 3 to 5 days, pay on delivery, the pink box.</p>
  <p><b>What the customer is not told.</b> No countdowns, no "only 3 left", no exclamation marks, no emojis. Every number on a card is true on the day it runs, and the stock rule keeps it that way.</p>
  <p><b>What to watch.</b> Link CTR above 2.5%, cost per purchase under ₹600 and ROAS above 2.0 are the bars; the catalogue campaigns have cleared them before. If the carousel wins, build the second one from the week's sellers. If a hero drops under 15 units, swap it for the next piece on its collection card and keep the hook.</p>
</section>

<footer>Built on 4 November 2026 from the live nairaflore.com prices, the Shopify stock sheet and the Meta ad account. Files, spec and build scripts: creative/naira-guest-list in the naira-scroll repository.</footer>
</div>
"""
(D / "page" / "index.html").write_text(page)
print("page", len(page) // 1000, "KB")
