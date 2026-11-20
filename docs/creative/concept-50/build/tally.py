"""Map coded ratings back to ads and variants, apply the concept-50 pick rule (PLAN §6 step 7) and write results.
Usage: python3 -I tally.py <ratings.json> <key_path> <out.json>
ratings.json: {"experts": [{"critic": "perf|craft|truth", "run": 1|2, "result": {...expert schema...}}],
               "customers": [{"persona": "Meera", "run": 1|2, "result": {...customer schema...}}]}"""
import sys, json
R = json.load(open(sys.argv[1])); K = json.load(open(sys.argv[2]))
import os
if os.environ.get('C50_RUBRIC', 'crazy') == 'crazy':
    W = dict(stop=.15, message=.08, truth=.15, layout=.08, brand=.05, copy=.08, fit=.03, desire=.13, cues=.10, crazy=.15)
else:
    W = dict(stop=.15, message=.10, truth=.15, layout=.10, brand=.05, copy=.10, fit=.05, desire=.15, cues=.15)
D = list(W); var = K['variants']; problems = []
ex = {c: {} for c in var}; th = {c: {} for c in var}; cu = {c: [] for c in var}; baskets = []
anchors = {}
for e in R['experts']:
    r = e.get('result') or {}
    crit, run = e['critic'], e['run']
    for v in r.get('variants', []):
        c = v['code'].strip().upper()
        if c not in var: problems.append(f'{crit}{run}: unknown code {c}'); continue
        ex[c].setdefault(crit, []).append(v)
    sid = f'{crit}{run}'; sk = K['sheets'].get(sid)
    tiles = {t['code'].strip().upper(): t for t in (r.get('thumbs') or {}).get('tiles', [])}
    if not sk: problems.append(f'no sheet {sid}'); continue
    for ac, name in sk['anchors'].items():
        if ac in tiles: anchors.setdefault(name, {})[sid] = tiles[ac]['score']
        else: problems.append(f'{sid}: anchor tile {ac} not scored')
    for c in var:
        if c in tiles: th[c][sid] = tiles[c]['score']
        else: problems.append(f'{sid}: tile {c} not scored')
for cr in R['customers']:
    r = cr.get('result') or {}
    for v in r.get('variants', []):
        c = v['code'].strip().upper()
        if c in var: cu[c].append(dict(v, persona=cr['persona'], run=cr['run']))
    b = r.get('basket') or []
    baskets.append({'persona': cr['persona'], 'run': cr['run'], 'basket': b, 'size': len(b), 'favourite': r.get('favouriteCode')})
rows = {}
for c, (ad, vn) in var.items():
    per = {}
    for crit, lst in ex[c].items():
        dm = {k: sum(x[k] for x in lst) / len(lst) for k in D}
        per[crit] = {'dims': dm, 'weighted': sum(dm[k] * W[k] for k in D), 'compliance': all(x.get('compliancePass', True) for x in lst),
                     'worst': [x.get('worstIssue', '') for x in lst]}
    if not per: problems.append(f'{c}: no expert scores'); continue
    dims = {k: sum(p['dims'][k] for p in per.values()) / len(per) for k in D}
    em = sum(p['weighted'] for p in per.values()) / len(per)
    comp = all(p['compliance'] for p in per.values())
    truth_ok = dims['truth'] >= 8 and per.get('truth', {'dims': {'truth': 10}})['dims']['truth'] >= 8
    under6 = [k for k in D if dims[k] < 6]
    t = th[c]; thumbs = list(t.values())
    def beats(run, loser):
        return all(t.get(f'{cr}{run}', -1) > anchors.get(loser, {}).get(f'{cr}{run}', 99) for cr in ('perf', 'craft'))
    def beats_w(run, win):
        return all(t.get(f'{cr}{run}', -1) > anchors.get(win, {}).get(f'{cr}{run}', 99) for cr in ('perf', 'craft'))
    bl = beats(1, 'p2') or beats(2, 'sa08'); bw = beats_w(1, 'apricot') or beats_w(2, 'F2')
    cl = cu[c]
    wb = sum(x['wouldBuy'] for x in cl) / len(cl) if cl else 0
    cm = sum((x['stop'] + x['want'] + x['trust'] + x['wouldBuy']) / 4 for x in cl) / len(cl) if cl else 0
    yes = sum(1 for x in cl if x.get('buyYes')) / len(cl) if cl else 0
    tm = sum(thumbs) / len(thumbs) if thumbs else 0
    gate = comp and truth_ok and not under6 and bl
    rows[c] = dict(ad=ad, variant=vn, expertMean=round(em, 3), dims={k: round(v, 2) for k, v in dims.items()},
                   perCritic={k: round(p['weighted'], 3) for k, p in per.items()}, compliance=comp, truthOk=truth_ok, under6=under6,
                   thumbs=t, thumbMean=round(tm, 2), beatsLoser=bl, beatsWinner=bw, customerMean=round(cm, 3), wouldBuy=round(wb, 3),
                   buyYesShare=round(yes, 2), gate=gate, score=round(0.5 * em + 0.3 * wb + 0.2 * tm, 3),
                   worst={k: p['worst'] for k, p in per.items()}, customerLines=[f"{x['persona']}{x['run']}: {x.get('line', '')}" for x in cl])
pick = {}
for c, r in rows.items():
    a = r['ad']; cand = pick.get(a)
    key = (r['gate'], r['score'])
    if cand is None or key > (rows[cand]['gate'], rows[cand]['score']): pick[a] = c
ads = sorted(set(r['ad'] for r in rows.values()))
summary = {}
for a in ads:
    c = pick[a]; r = rows[c]
    summary[a] = {'chosen': r['variant'], 'code': c, 'gate': r['gate'], 'score': r['score'], 'expertMean': r['expertMean'],
                  'customerMean': r['customerMean'], 'wouldBuy': r['wouldBuy'], 'thumbMean': r['thumbMean'],
                  'others': {rows[x]['variant']: {'score': rows[x]['score'], 'gate': rows[x]['gate']} for x in rows if rows[x]['ad'] == a and x != c}}
ch = [rows[pick[a]] for a in ads]
batch = {'expertMean': round(sum(r['expertMean'] for r in ch) / len(ch), 3), 'customerMean': round(sum(r['customerMean'] for r in ch) / len(ch), 3),
         'basketRate': round(sum(1 for b in baskets if b['size'] >= 3) / len(baskets), 2) if baskets else None,
         'shipped': sum(1 for r in ch if r['gate']), 'anchors': anchors}
json.dump({'rows': rows, 'pick': summary, 'batch': batch, 'baskets': baskets, 'problems': problems}, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
print('problems:', problems)
print('batch:', json.dumps(batch))
for a in ads:
    print(a, json.dumps(summary[a]))
