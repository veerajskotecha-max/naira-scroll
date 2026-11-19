"""Build the Ads 500 review board and the Meta upload sheet from build/ledger.json and each ad's copy.json.

Usage: python3 -I make_board.py <out_dir>
  <out_dir>/index.html   the board page (published as an Artifact; images beside it in img/)
  <out_dir>/img/         web copies of every shipped Feed (540 px wide) and Story (405 px wide) JPG
  ../meta_upload.csv     one row per shipped ad, the fields Meta asks for (nothing is uploaded); a headline variant's
                         row names its ad in variant_of (upload it as a second creative in that ad, not as a new ad)
Only ledger rows whose verdict starts with "ship" go on the board. Pictures are never edited; the web copies are
plain downscales of the finished ad JPGs.
"""
import base64, csv, glob, html, json, os, re, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # docs/creative/ads-500
OUT = os.path.abspath(sys.argv[1])
os.makedirs(os.path.join(OUT, 'img'), exist_ok=True)

ledger = json.load(open(os.path.join(ROOT, 'build', 'ledger.json')))


def price_text(p):
    if isinstance(p, (int, float)):
        return '₹{:,}'.format(int(p))
    s = str(p or '').strip()
    return s if s.startswith('₹') or not s else '₹' + s


def short(s, n):
    s = re.sub(r'\s+', ' ', str(s or '')).strip()
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(' ', 1)[0]
    return cut.rstrip(',;:(') + '…'


def web_copy(src, dst, width):
    im = Image.open(src).convert('RGB')
    h = round(im.height * width / im.width)
    im.resize((width, h), Image.LANCZOS).save(dst, 'JPEG', quality=84, optimize=True, progressive=True)


ANCHOR_NAMES = {'win_static_hoops_apricot': 'apricot hoops', 'win_twenty_f2_tennis_ruby': 'F2 tennis',
                'win_vkf18_prism_cluster': 'vkf18 Prism'}
ads, held = [], []
for r in ledger:
    v = str(r.get('verdict', ''))
    if not v.startswith('ship'):
        held.append({'id': r['id'], 'batch': r.get('batch') or r['id'][:3], 'handle': r.get('handle', ''),
                     'why': short(v, 150)})
        continue
    cp = json.load(open(os.path.join(ROOT, r['copy'])))
    on, meta = cp.get('onImage') or {}, cp.get('meta') or {}
    a, b = r.get('weightedA'), r.get('weightedB')
    wb = r.get('beatsWinnerBy')
    if isinstance(wb, dict):      # zero-credit pass: one winner per sheet, keyed by anchor file
        wb = '; '.join('{}: {}'.format(ANCHOR_NAMES.get(k, k), ', '.join(v) if v else 'neither critic')
                       for k, v in wb.items())
    elif isinstance(wb, list):
        wb = ', '.join(wb)
    mean = round((a + b) / 2, 2) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else None
    feed_src, story_src = os.path.join(ROOT, r['feed']), os.path.join(ROOT, r['story'])
    web_copy(feed_src, os.path.join(OUT, 'img', r['id'] + '_feed.jpg'), 540)
    web_copy(story_src, os.path.join(OUT, 'img', r['id'] + '_story.jpg'), 405)
    head = on.get('headline')
    if isinstance(head, list):
        head = ' / '.join(head)
    ads.append({
        'id': r['id'], 'batch': r.get('batch') or r['id'][:3], 'handle': cp.get('handle', r.get('handle', '')),
        'product': cp.get('product', ''), 'price': price_text(cp.get('price')),
        'archetype': short(re.split(r' \(', str(cp.get('archetype') or r.get('archetype') or ''))[0], 40),
        'headline': head or '', 'beat': on.get('beat') or '', 'cardLine': on.get('cardLine') or '',
        'offer': on.get('offer') or '', 'sizeTag': short(on.get('sizeTag') or '', 70),
        'A': a, 'B': b, 'mean': mean, 'beatsLoser': bool(r.get('beatsLoser')),
        'beatsWinner': bool(r.get('beatsWinner')), 'beatsWinnerBy': wb or '',
        'variantOf': r.get('variantOf') or '',
        'verdict': short(v, 160),
        'primaryText': meta.get('primaryText', ''), 'metaHeadline': meta.get('headline', ''),
        'description': meta.get('description', ''), 'cta': meta.get('cta', 'Shop Now'), 'url': meta.get('url', ''),
        'feedFile': r['feed'], 'storyFile': r['story'],
        'feed': 'img/' + r['id'] + '_feed.jpg', 'story': 'img/' + r['id'] + '_story.jpg',
    })

# Meta upload sheet (repo copy)
csv_path = os.path.join(ROOT, 'build', 'meta_upload.csv')
cols = ['ad_name', 'feed_image_1080x1350', 'story_image_1080x1920', 'primary_text', 'headline', 'description',
        'call_to_action', 'website_url', 'product', 'price', 'score_mean', 'variant_of']
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(cols)
    for x in ads:
        w.writerow(['NAIRA_ads500_' + x['id'] + '_' + x['handle'], 'docs/creative/ads-500/' + x['feedFile'],
                    'docs/creative/ads-500/' + x['storyFile'], x['primaryText'], x['metaHeadline'], x['description'],
                    x['cta'], x['url'], x['product'], x['price'], x['mean'], x['variantOf']])

pictures = len(glob.glob(os.path.join(ROOT, 'batches', 'b0*', 'pics', 'b0*.png')))
batches = sorted({x['batch'] for x in ads} | {h['batch'] for h in held})
main = [x for x in ads if not x['variantOf']]        # a headline variant is a second creative of its ad (RULINGS §1.3)
means = [x['mean'] for x in main if x['mean'] is not None]
best = max(main, key=lambda x: x['mean'] or 0) if main else None
stats = {'ads': len(main), 'variants': len(ads) - len(main), 'pictures': pictures, 'credits': pictures * 2,
         'batches': len(batches),
         'mean': round(sum(means) / len(means), 2) if means else None,
         'best': best and {'id': best['id'], 'product': best['product'], 'mean': best['mean']},
         'batchList': batches}

velista = base64.b64encode(open(os.path.join(ROOT, 'kit', 'fonts', 'Velista.ttf'), 'rb').read()).decode()
tpl = open(os.path.join(HERE, 'board_template.html'), encoding='utf-8').read()
data = json.dumps({'ads': ads, 'held': held, 'stats': stats}, ensure_ascii=False).replace('</', '<\\/')
page = tpl.replace('__VELISTA__', velista).replace('__DATA__', data)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
print(json.dumps({'ads': len(main), 'variants': len(ads) - len(main), 'held': len(held), 'pictures': pictures, 'csv': os.path.relpath(csv_path, ROOT),
                  'page_kb': round(os.path.getsize(os.path.join(OUT, 'index.html')) / 1024)}))
