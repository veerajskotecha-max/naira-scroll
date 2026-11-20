"""Build coded rating packs and blind 200 px sheets for one concept-50 batch.
Usage: python3 -I build_sheets.py <batch_dir> <variants.json> <out_dir> <key_path> <seed>
variants.json: [{"ad": "c01-1", "variant": "V1", "feed": "<abs jpg>", "story": "<abs jpg>",
                 "meta": {"primaryText": "", "headline": "", "description": ""}}]
Writes <out_dir>/packs/<CODE>/{feed.jpg, story.jpg, info.md}, <out_dir>/sheets/<sid>.png and the key (never printed).
Expert sheets: 3 experts x 2 runs; run 1 carries anchors apricot (winner) + p2 (loser), run 2 F2 (winner) + sa08 (loser)."""
import sys, os, json, random, shutil, re
from PIL import Image, ImageDraw, ImageFont
bdir, vpath, out, keyp, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
C = '/home/user/naira-scroll/docs/creative'
V = json.load(open(vpath))
plan = json.load(open(C + '/concept-50/plan.json'))
ads = {a['id']: a for c in plan['camps'] for a in c['ads']}
camps = {a['id']: c for c in plan['camps'] for a in c['ads']}
locks = plan.get('locks', {})
prod_lines = open(C + '/ads-500/build/study/products.md', encoding='utf-8').read().split('\n')
starts = [(i, l) for i, l in enumerate(prod_lines) if l.startswith('== ')]
sec = {}
for n, (i, l) in enumerate(starts):
    m = re.match(r'== \d+\. ([a-z0-9-]+):', l)
    if m:
        sec[m.group(1)] = '\n'.join(prod_lines[i:starts[n + 1][0] if n + 1 < len(starts) else len(prod_lines)])
shutil.rmtree(out, ignore_errors=True); os.makedirs(out + '/packs'); os.makedirs(out + '/sheets')
rng = random.Random(seed)
alpha = 'ACDEFHJKLMNPRTUVWXY'
codes = set()
while len(codes) < len(V) + 20:
    codes.add(rng.choice(alpha) + rng.choice('23456789'))
codes = list(codes); rng.shuffle(codes)
vcodes, spare = codes[:len(V)], codes[len(V):]
key = {'variants': {}, 'sheets': {}}
order = list(range(len(V))); rng.shuffle(order)
for code, idx in zip(vcodes, order):
    v = V[idx]; a = ads[v['ad']]; camp = camps[v['ad']]
    d = f'{out}/packs/{code}'; os.makedirs(d)
    shutil.copyfile(v['feed'], d + '/feed.jpg'); shutil.copyfile(v['story'], d + '/story.jpg')
    lk = locks.get(a['handle'], '')
    lk = lk if isinstance(lk, str) else json.dumps(lk, ensure_ascii=False)
    refs = [f"{C}/{a['refs'][s].split('docs/creative/')[-1]}" for s in ('slot1', 'slot2') if a.get('refs', {}).get(s)]
    m = v.get('meta', {})
    info = [f'# Ad {code}', '', f"- Camp idea: {camp.get('name')}. {camp.get('insight', '')}",
            f"- Product: {a['product']}, ₹{a['price']:,} (live price, stock 20+ read on the day).",
            f"- Reference photos of the real piece (the authority on construction, colour and size): {', '.join(refs)}",
            f"- Construction facts the picture must match: {lk}",
            f"- Meta primary text: \"{m.get('primaryText', '')}\"", f"- Meta headline: \"{m.get('headline', '')}\"",
            f"- Meta description: \"{m.get('description', '')}\"", '- CTA: Shop Now; landing page: the product page.',
            f'- Feed: {d}/feed.jpg (1080 x 1350). Story: {d}/story.jpg (1080 x 1920).', '',
            '## Listing facts (from the store listing)', '', sec.get(a['handle'], '(see the reference photos)')]
    open(d + '/info.md', 'w', encoding='utf-8').write('\n'.join(info) + '\n')
    key['variants'][code] = [v['ad'], v['variant']]
anch = {'apricot': 'win_static_hoops_apricot', 'F2': 'win_twenty_f2_tennis_ruby', 'p2': 'lose_p2_proof_parody', 'sa08': 'lose_sa08_walls'}
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
TW, TH, G, LH, COLS = 200, 250, 24, 30, 5
for critic in ('perf', 'craft', 'truth'):
    for run, an in ((1, ['apricot', 'p2']), (2, ['F2', 'sa08'])):
        sid = f'{critic}{run}'
        items = [(c, f'{out}/packs/{c}/feed.jpg') for c in vcodes]
        ac = {}
        for a_ in an:
            c = spare.pop(); ac[c] = a_
            items.append((c, f'{C}/ads-500/build/anchors/{anch[a_]}.jpg'))
        rng.shuffle(items)
        rows = (len(items) + COLS - 1) // COLS
        sh = Image.new('RGB', (COLS * TW + (COLS + 1) * G, rows * (TH + LH) + (rows + 1) * G), (237, 237, 237)); dr = ImageDraw.Draw(sh)
        for i, (c, p) in enumerate(items):
            r_, k = divmod(i, COLS); x = G + k * (TW + G); y = G + r_ * (TH + LH + G)
            sh.paste(Image.open(p).convert('RGB').resize((TW, TH), Image.LANCZOS), (x, y))
            dr.text((x + TW // 2, y + TH + 4), c, fill=(30, 30, 30), font=font, anchor='ma')
        sh.save(f'{out}/sheets/{sid}.png')
        key['sheets'][sid] = {'critic': critic, 'run': run, 'anchors': ac}
json.dump(key, open(keyp, 'w'), indent=1)
print(json.dumps({'packs': sorted(vcodes), 'sheets': sorted(key['sheets'])}))
