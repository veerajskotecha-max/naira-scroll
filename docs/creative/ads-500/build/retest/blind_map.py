"""Map the clean blind re-test back to ad ids. Usage: python3 -I blind_map.py <workflow_output.json> <key.json> <out.json>"""
import json, sys

out = json.load(open(sys.argv[1]))
res = out['result'] if 'result' in out else out
key = json.load(open(sys.argv[2]))
W = {'win_static_hoops_apricot': 'apricot', 'win_twenty_f2_tennis_ruby': 'F2'}
Lz = {'lose_p2_proof_parody': 'p2', 'lose_sa08_walls': 'sa08'}

per = {}          # id -> {'A': {...}, 'B': {...}}
anchors = {}
problems = []
for sid in ('s1', 's2', 's3', 's4'):
    k = key[sid]; crit = k['critic']; r = res['thumbs'].get(sid)
    if not r:
        problems.append(sid + ': no result'); continue
    sc = {t['code'].strip().upper(): t for t in r['tiles']}
    if set(sc) != set(k['tiles']):
        problems.append('%s: codes differ: missing %s extra %s' % (sid, sorted(set(k['tiles']) - set(sc)), sorted(set(sc) - set(k['tiles']))))
    rank = [c.strip().upper() for c in r['ranking']]
    by_id = {}
    for code, item in k['tiles'].items():
        t = sc.get(code)
        if t is None:
            continue
        by_id[item] = dict(score=t['score'], rank=rank.index(code) + 1 if code in rank else None, lands=t['landsFirst'],
                           productReads=t['productReads'], priceReads=t['priceReads'], note=t['note'], code=code)
    for a in k['anchors']:
        anchors.setdefault(a, {})[crit] = by_id.get(a)
    for item, v in by_id.items():
        if item in W or item in Lz:
            continue
        d = per.setdefault(item, {}).setdefault(crit, {'sheets': {}})
        d['sheets'][sid] = v
        for a in k['anchors']:
            av = by_id[a]['score']
            rel = 'beats' if v['score'] > av else ('ties' if v['score'] == av else 'loses')
            d[(W.get(a) or Lz.get(a))] = rel

rows = {}
for item, d in per.items():
    bw = {n: [c for c in 'AB' if d.get(c, {}).get(n) == 'beats'] for n in ('apricot', 'F2')}
    bl = {n: [c for c in 'AB' if d.get(c, {}).get(n) == 'beats'] for n in ('p2', 'sa08')}
    thumbs = {c: [v['score'] for v in d.get(c, {}).get('sheets', {}).values()] for c in 'AB'}
    rows[item] = dict(
        beatsWinnerBy=bw, beatsLoserBy=bl,
        beatsWinner=any(len(v) == 2 for v in bw.values()), beatsLoser=any(len(v) == 2 for v in bl.values()),
        rel={c: {n: d.get(c, {}).get(n) for n in ('apricot', 'F2', 'p2', 'sa08')} for c in 'AB'},
        thumbs=thumbs, thumbMean=round(sum(thumbs['A'] + thumbs['B']) / max(1, len(thumbs['A'] + thumbs['B'])), 2),
        sheets={c: d.get(c, {}).get('sheets', {}) for c in 'AB'})

WEIGHTS = dict(stop=.15, message=.10, truth=.15, layout=.10, brand=.05, copy=.10, fit=.05, desire=.15, cues=.15)
pair = {}
for c in 'AB':
    p = res['pair'].get(c)
    if not p:
        problems.append('pair %s: no result' % c); continue
    for lab in 'XY':
        x = p[lab]; ident = key['pair'][lab]
        w = round(sum(x[k] * v for k, v in WEIGHTS.items()), 4)
        pair.setdefault(ident, {})[c] = dict({k: x[k] for k in WEIGHTS}, weighted=w, compliancePass=x['compliancePass'],
                                             complianceNotes=x['complianceNotes'], notes=x['notes'], label=lab)
    pair.setdefault('_prefer', {})[c] = {'prefer': key['pair'].get(p['prefer'], 'tie'), 'why': p['why']}

json.dump({'rows': rows, 'anchors': anchors, 'pair': pair, 'problems': problems,
           'method': {s: (res['thumbs'].get(s) or {}).get('method') for s in ('s1', 's2', 's3', 's4')}},
          open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)

print('problems:', problems)
print('anchors:', {a: {c: (v or {}).get('score') for c, v in x.items()} for a, x in anchors.items()})
order = sorted(rows, key=lambda i: -rows[i]['thumbMean'])
print('%-7s %-5s %-11s %-11s %-11s %-11s %-6s %-6s %s' % ('id', 'mean', 'A apr/F2', 'B apr/F2', 'A p2/sa08', 'B p2/sa08', 'winr', 'losr', 'thumbs'))
s = lambda r, c, a, b: '%s/%s' % (r['rel'][c][a][0] if r['rel'][c][a] else '-', r['rel'][c][b][0] if r['rel'][c][b] else '-')
for i in order:
    r = rows[i]
    print('%-7s %-5s %-11s %-11s %-11s %-11s %-6s %-6s %s' % (i, r['thumbMean'], s(r, 'A', 'apricot', 'F2'), s(r, 'B', 'apricot', 'F2'),
          s(r, 'A', 'p2', 'sa08'), s(r, 'B', 'p2', 'sa08'), r['beatsWinner'], r['beatsLoser'], r['thumbs']))
for ident in ('b04-3', 'b04-3h'):
    for c in 'AB':
        x = pair.get(ident, {}).get(c)
        if x:
            print(ident, c, x['label'], 'w=%.4f' % x['weighted'], {k: x[k] for k in WEIGHTS}, 'compliance', x['compliancePass'])
print('prefer', pair.get('_prefer'))
