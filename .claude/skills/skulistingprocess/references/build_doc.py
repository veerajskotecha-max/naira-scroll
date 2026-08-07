#!/usr/bin/env python3
"""Build the Lovable top-50 listing pack.

Emits:
  Naira_Petite_Top50_Listing.html   self-contained review doc (target <=10MB)
  assets/<SKU>_<n>_<slot>.jpg       full-res images, named for upload
  products.json / products.csv      structured feed for Lovable
"""
import json, os, base64, html, io, csv, shutil, sys
from urllib.parse import quote
from PIL import Image

BASE = '/tmp/naira_work/listing'
WA = '919561557935'
TARGET_MB = 9.5

man = json.load(open(f'{BASE}/MANIFEST.json'))
raw = json.load(open(f'{BASE}/verdicts.json'))
ver = raw if isinstance(raw, list) else raw.get('images', [])
audit = open(f'{BASE}/AUDIT.md').read()
renames = json.load(open(f'{BASE}/RENAMES.json')) if os.path.exists(f'{BASE}/RENAMES.json') else {}
copy = json.load(open(f'{BASE}/COPY.json')) if os.path.exists(f'{BASE}/COPY.json') else {}
order = json.load(open(f'{BASE}/ORDER.json')) if os.path.exists(f'{BASE}/ORDER.json') else {}
notes = open(f'{BASE}/PLANNER_NOTES.md').read() if os.path.exists(f'{BASE}/PLANNER_NOTES.md') else ''
MAN = {m['sku']: m for m in man['skus']}
SECTIONS = order.get('sections') or [{'title': 'All products', 'blurb': '', 'skus': [m['sku'] for m in man['skus']]}]

by_sku = {}
for v in ver:
    if v.get('score', 0) <= 0 or not v.get('slot') or not os.path.exists(v.get('file', '')):
        continue
    by_sku.setdefault(v['sku'], []).append(v)
for s in by_sku:
    by_sku[s].sort(key=lambda x: (x['slot'], -x.get('score', 0)))
    by_sku[s] = by_sku[s][:6]

# ---------- assets + feed ----------
ASSETS = f'{BASE}/assets'
shutil.rmtree(ASSETS, ignore_errors=True)
os.makedirs(ASSETS)
feed = []
for m in man['skus']:
    sku = m['sku']
    imgs = by_sku.get(sku, [])
    disp = renames.get(sku, {}).get('name', m['name'])
    files = []
    for n, v in enumerate(imgs, 1):
        if v['slot'] == 1:
            kind = 'main'
        elif '/worn' in v['file']:
            kind = 'worn'
        elif v['file'].startswith('/tmp/naira_work/') and '/out/' in v['file']:
            kind = 'editorial'
        else:
            kind = 'alt'
        dst = f'{sku}_{n}_{kind}.jpg'
        im = Image.open(v['file']).convert('RGB')
        if im.width > 1600:
            im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        im.save(f'{ASSETS}/{dst}', 'JPEG', quality=90, optimize=True, progressive=True)
        files.append(dst)
        v['asset'] = dst
    feed.append(dict(sku=sku, name=disp, previous_name=(m['name'] if disp != m['name'] else ''),
                     category=renames.get(sku, {}).get('category', m['cat']),
                     price_inr=m['our'], mrp_inr=m['mrp'], discount_pct=round(100 * (1 - m['our'] / m['mrp'])),
                     competitor_price_inr=m['pal'], qty=5, design_score=m['score'],
                     material='18K gold-plated 316L stainless steel',
                     short_description=m['desc'], images=files,
                     headline=copy.get(sku, {}).get('headline', ''),
                     long_description=copy.get(sku, {}).get('description', ''),
                     details=copy.get(sku, {}).get('details', []),
                     care=copy.get(sku, {}).get('care', ''),
                     occasion=copy.get(sku, {}).get('occasion', ''),
                     whatsapp_url=f"https://wa.me/{WA}?text=" + quote(
                         f"Hi Naira Petite — I'd like to order {disp} ({sku}), Rs {m['our']:,}."),
                     audit_note=renames.get(sku, {}).get('note', '')))
json.dump(feed, open(f'{BASE}/products.json', 'w'), indent=1, ensure_ascii=False)
with open(f'{BASE}/products.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['sku', 'name', 'previous_name', 'category', 'price_inr', 'mrp_inr', 'discount_pct',
                'competitor_price_inr', 'qty', 'material', 'short_description', 'image_1', 'image_2',
                'image_3', 'image_4', 'image_5', 'image_6', 'whatsapp_url', 'audit_note'])
    for p in feed:
        im = p['images'] + [''] * 6
        w.writerow([p['sku'], p['name'], p['previous_name'], p['category'], p['price_inr'], p['mrp_inr'],
                    p['discount_pct'], p['competitor_price_inr'], p['qty'], p['material'],
                    p['short_description'], *im[:6], p['whatsapp_url'], p['audit_note']])

# ---------- html ----------
_cache = {}


def embed(path, w, q):
    k = (path, w, q)
    if k in _cache:
        return _cache[k]
    im = Image.open(path).convert('RGB')
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, optimize=True, progressive=True)
    _cache[k] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
    return _cache[k]


try:
    import markdown
    audit_html = markdown.markdown(audit, extensions=['tables'])
    notes_html = markdown.markdown(notes, extensions=['tables'])
except Exception:
    audit_html = '<pre class="raw">' + html.escape(audit) + '</pre>'
    notes_html = '<pre class="raw">' + html.escape(notes) + '</pre>'


def render(hw, aw, q):
    _cache.clear()
    cards = []
    for sec in SECTIONS:
        cards.append(f'<section class="sec"><h2>{html.escape(sec["title"])}</h2>'
                     f'<p class="blurb">{html.escape(sec.get("blurb",""))}</p></section>')
        for sku in sec['skus']:
            m = MAN[sku]
            imgs = by_sku.get(sku, [])
            disp = renames.get(sku, {}).get('name', m['name'])
            old = m['name'] if disp != m['name'] else None
            note = renames.get(sku, {}).get('note', '')
            c = copy.get(sku, {})
            th = []
            for v in imgs:
                if v['slot'] == 1: lbl = 'MAIN · ECOM'
                elif '/worn' in v['file']: lbl = 'WORN'
                elif 'editorial' in v.get('asset', ''): lbl = 'EDITORIAL'
                else: lbl = f"ALT {v['slot']-1}"
                src = embed(v['file'], hw if v['slot'] == 1 else aw, q)
                th.append(f'<figure class="sh{" hero" if v["slot"]==1 else ""}"><img src="{src}" alt="{html.escape(disp)}" loading="lazy">'
                          f'<figcaption><span class="slot s{v["slot"]}">{lbl}</span>{html.escape(v.get("angle",""))}'
                          f'<span class="fn">{v.get("asset","")}</span></figcaption></figure>')
            disc = round(100 * (1 - m['our'] / m['mrp']))
            warn = f'<p class="warn">{html.escape(note)}</p>' if note else ''
            oldl = f'<span class="old">was: {html.escape(old)}</span>' if old else ''
            det = ''.join(f'<li>{html.escape(x)}</li>' for x in c.get('details', []))
            cards.append(f'''<article class="card" id="{sku}">
<header><div><h3>{html.escape(disp)} {oldl}</h3>
<p class="meta"><code>{sku}</code> · {renames.get(sku,{}).get('category',m['cat'])} · design score {m['score']}/10 · qty 5</p></div>
<div class="price"><span class="mrp">₹{m['mrp']:,}</span><span class="sell">₹{m['our']:,}</span><span class="off">{disc}% off · Palmonas ₹{m['pal']:,}</span></div></header>
{warn}<p class="head">{html.escape(c.get('headline',''))}</p>
<p class="desc">{html.escape(c.get('description', m['desc']))}</p>
<div class="shots">{''.join(th)}</div>
<ul class="det">{det}</ul>
<p class="spec"><b>Care.</b> {html.escape(c.get('care',''))}<br><b>Wear it for.</b> {html.escape(c.get('occasion',''))}</p>
<a class="wa" href="https://wa.me/{WA}?text={quote(f'Hi Naira Petite — I would like to order {disp} ({sku}), Rs {m["our"]:,}.')}">Order on WhatsApp</a>
</article>''')

    missing = [(m['sku'], renames.get(m['sku'], {}).get('name', m['name']), len(by_sku.get(m['sku'], [])))
               for m in man['skus'] if len(by_sku.get(m['sku'], [])) < 3]
    short = ('<div class="short"><h3>Below three images</h3><ul>' + ''.join(
        f'<li><code>{s}</code> {html.escape(n)} — {k} usable</li>' for s, n, k in missing) + '</ul></div>') if missing else ''
    total = sum(len(v) for v in by_sku.values())
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Naira Petite — Top 50 SKUs for Lovable</title><style>
:root{{--gold:#B8935A;--bone:#F7F4EE;--ink:#1F1416;--line:#E3DCD1}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bone);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding:40px 20px 80px}}
h1{{font-size:clamp(28px,5vw,44px);margin:0 0 8px;letter-spacing:-.02em}}
.sub{{color:#6b5f57;margin:0 0 28px}}
.legend{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 24px;margin-bottom:36px}}
.legend h2{{margin:0 0 10px;font-size:18px}} .legend ul{{margin:0;padding-left:20px}}
.card{{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:26px}}
.card header{{display:flex;gap:16px;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;border-bottom:1px solid var(--line);padding-bottom:14px;margin-bottom:14px}}
.card h3{{margin:0;font-size:22px;letter-spacing:-.01em}}
.old{{font-size:11px;color:#a08d7d;font-weight:400;letter-spacing:.04em;text-transform:uppercase;margin-left:6px}}
.meta{{margin:4px 0 0;font-size:13px;color:#6b5f57}} .meta code{{background:var(--bone);padding:2px 6px;border-radius:4px}}
.price{{text-align:right;white-space:nowrap}}
.mrp{{text-decoration:line-through;color:#a08d7d;margin-right:8px}}
.sell{{font-size:24px;font-weight:600;color:var(--gold)}}
.off{{display:block;font-size:12px;color:#6b5f57}}
.desc{{margin:0 0 14px;color:#4a3f39}}
.head{{margin:0 0 8px;font-size:17px;color:var(--ink);font-style:italic}}
.det{{margin:14px 0 0;padding-left:20px;font-size:13.5px;color:#4a3f39}}
.det li{{margin-bottom:3px}}
.sec{{margin:44px 0 18px}} .sec h2{{margin:0;font-size:26px;letter-spacing:-.02em}}
.blurb{{margin:6px 0 0;color:#6b5f57}}
.warn{{background:#FFF6E8;border-left:3px solid var(--gold);padding:8px 12px;margin:0 0 12px;font-size:14px;border-radius:0 6px 6px 0}}
.shots{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}}
.sh{{margin:0}} .sh.hero{{grid-column:span 2;grid-row:span 2}}
.shots{{align-items:start}}
.sh img{{width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:8px;background:var(--bone);display:block}}
.sh figcaption{{font-size:11px;color:#6b5f57;margin-top:5px;display:flex;gap:6px;align-items:center;flex-wrap:wrap}}
.slot{{font-size:10px;letter-spacing:.08em;padding:2px 6px;border-radius:3px;background:#EFE8DC;color:#6b5f57}}
.slot.s1{{background:var(--gold);color:#fff}}
.fn{{color:#b6a695;font-family:ui-monospace,Menlo,monospace;font-size:10px}}
.spec{{font-size:12.5px;color:#6b5f57;margin:14px 0 12px}}
.wa{{display:inline-block;background:#25D366;color:#fff;text-decoration:none;padding:9px 18px;border-radius:999px;font-size:14px;font-weight:600}}
.short{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:20px 24px;margin:36px 0}}
.audit{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:24px 28px;margin-top:40px}}
.audit table{{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px;display:block;overflow-x:auto}}
.audit th,.audit td{{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}}
.audit th{{background:var(--bone)}} .raw{{white-space:pre-wrap;font-size:13px}}
@media(max-width:520px){{.price{{text-align:left}}.sh.hero{{grid-column:span 2}}}}
</style></head><body><div class="wrap">
<h1>Naira Petite — Top 50 SKUs</h1>
<p class="sub">Listing pack for the ecom dashboard · {len(man['skus'])} products · {total} images · prices in INR</p>
<div class="legend"><h2>How to read this</h2><ul>
<li><b>MAIN</b> is image 1 — the grid thumbnail and the first PDP image. Every hero shows the piece resting on the plinth with real contact, and the angle varies across SKUs.</li>
<li><b>ALT 1 / ALT 2</b> are further studio shots at deliberately different angles — overhead, profile, macro. Use them in order.</li>
<li><b>EDITORIAL</b> images are campaign photographs. They go last on the PDP and are never the thumbnail.</li>
<li>Full-resolution files are in <code>assets/</code>, named exactly as shown under each image. <code>products.json</code> and <code>products.csv</code> carry the same data as a feed.</li>
<li>Every product is qty 5 and <b>Draft</b> in Shopify. The Palmonas figure is the comparable competitor price, held about 10% above ours.</li>
<li><b>Order on WhatsApp</b> opens <code>wa.me/{WA}</code> with product name, SKU and price pre-filled.</li>
<li>Names marked <span class="old">was:</span> have been corrected. The audit at the end lists every change Shopify needs.</li>
</ul></div>
{''.join(cards)}{short}
<div class="audit">{audit_html}</div>
<div class="audit">{notes_html}</div>
</div></body></html>'''


out = f'{BASE}/Naira_Petite_Top50_Listing.html'
for hw, aw, q in [(760, 460, 80), (660, 400, 76), (560, 340, 72), (480, 300, 68), (420, 260, 62)]:
    doc = render(hw, aw, q)
    open(out, 'w').write(doc)
    mb = os.path.getsize(out) / 1e6
    print(f'  try hero={hw} alt={aw} q={q} -> {mb:.2f} MB', file=sys.stderr)
    if mb <= TARGET_MB:
        break
print(out, round(os.path.getsize(out) / 1e6, 2), 'MB |',
      len(man['skus']), 'skus |', sum(len(v) for v in by_sku.values()), 'images |',
      len(os.listdir(ASSETS)), 'asset files')
