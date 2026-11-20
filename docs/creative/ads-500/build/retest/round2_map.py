"""Map round 2 (blind sheets t1-t4 and the coded audit) back to ids and apply PLAYBOOK §7.
Usage: python3 -I round2_map.py <workflow_output.json> <key3.json> <out.json>"""
import json, sys

res = json.load(open(sys.argv[1]))
res = res.get('result', res)
key = json.load(open(sys.argv[2]))
W = dict(stop=.15, message=.10, truth=.15, layout=.10, brand=.05, copy=.10, fit=.05, desire=.15, cues=.15)
D = list(W)
NAME = {'win_static_hoops_apricot': 'apricot', 'win_twenty_f2_tennis_ruby': 'F2', 'lose_p2_proof_parody': 'p2', 'lose_sa08_walls': 'sa08'}
problems = []

# blind
blind, anchors = {}, {}
for sid, k in key['blind'].items():
    r = res['thumbs'].get(sid)
    if not r:
        problems.append(sid + ': no result'); continue
    sc = {t['code'].strip().upper(): t for t in r['tiles']}
    if set(sc) != set(k['tiles']):
        problems.append('%s: code mismatch %s' % (sid, sorted(set(sc) ^ set(k['tiles']))))
    rank = [c.strip().upper() for c in r['ranking']]
    by = {it: dict(sc[c], rank=rank.index(c) + 1 if c in rank else None) for c, it in k['tiles'].items() if c in sc}
    for a in k['anchors']:
        anchors.setdefault(NAME[a], {})[k['critic']] = by[a]['score']
    for it, v in by.items():
        if it in NAME:
            continue
        d = blind.setdefault(it, {'A': {}, 'B': {}, 'thumbs': {'A': [], 'B': []}, 'notes': []})
        d['thumbs'][k['critic']].append(v['score'])
        d['notes'].append('%s %s: %s (%s)' % (sid, k['critic'], v['landsFirst'], v['note']))
        for a in k['anchors']:
            av = by[a]['score']
            d[k['critic']][NAME[a]] = 'beats' if v['score'] > av else ('ties' if v['score'] == av else 'loses')
for it, d in blind.items():
    d['beatsWinnerBy'] = {n: [c for c in 'AB' if d[c].get(n) == 'beats'] for n in ('apricot', 'F2')}
    d['beatsLoserBy'] = {n: [c for c in 'AB' if d[c].get(n) == 'beats'] for n in ('p2', 'sa08')}
    d['beatsWinner'] = any(len(v) == 2 for v in d['beatsWinnerBy'].values())
    d['beatsLoser'] = any(len(v) == 2 for v in d['beatsLoserBy'].values())
    allt = d['thumbs']['A'] + d['thumbs']['B']
    d['thumbMean'] = round(sum(allt) / len(allt), 2) if allt else None

# audit
runs = {}
for n, run in enumerate(res['runs']):
    r = run.get('result')
    if not r:
        problems.append('audit run %d: no result' % n); continue
    got = set()
    for ad in r['ads']:
        c = ad['code'].strip().upper()
        if c not in key['audit']:
            problems.append('run %d unknown code %s' % (n, c)); continue
        got.add(c)
        runs.setdefault(key['audit'][c], {'A': [], 'B': []})[run['critic']].append(dict(ad, run=n))
    if set(key['audit']) - got:
        problems.append('run %d missing %s' % (n, sorted(set(key['audit']) - got)))
rows = {}
for i, d in runs.items():
    m = {c: {k: round(sum(x[k] for x in d[c]) / len(d[c]), 3) for k in D} for c in 'AB' if d[c]}
    wA = round(sum(m['A'][k] * W[k] for k in D), 4)
    wB = round(sum(m['B'][k] * W[k] for k in D), 4)
    comp = all(x['compliancePass'] for c in 'AB' for x in d[c])
    under6 = ['%s %s %.2f' % (c, k, m[c][k]) for c in 'AB' for k in D if m[c][k] < 6]
    truth_ok = m['A']['truth'] >= 8 and m['B']['truth'] >= 8
    bl = blind.get(i, {})
    rows[i] = dict(A=wA, B=wB, mean=round((wA + wB) / 2, 4), dimsA=m['A'], dimsB=m['B'], compliance=comp, truthOk=truth_ok,
                   under6=under6, beatsLoser=bool(bl.get('beatsLoser')), beatsWinner=bool(bl.get('beatsWinner')),
                   passes=comp and truth_ok and not under6 and bool(bl.get('beatsLoser')),
                   runs={c: [{k: x[k] for k in D + ['compliancePass', 'complianceNotes', 'worstIssue', 'zeroCreditFix', 'run']} for x in d[c]] for c in 'AB'})

json.dump({'audit': rows, 'blind': blind, 'anchors': anchors, 'problems': problems,
           'auditMethod': [(r.get('result') or {}).get('method') for r in res['runs']],
           'blindMethod': {s: (res['thumbs'].get(s) or {}).get('method') for s in res['thumbs']}},
          open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
print('problems:', problems)
print('anchors:', anchors)
print('%-7s %-6s %-6s %-6s %-5s %-5s %-6s %-6s %-6s %-22s %s' % ('id', 'A', 'B', 'mean', 'comp', 'trth', 'loser', 'winner', 'PASS', 'thumbs', 'under6'))
for i in sorted(rows, key=lambda i: -rows[i]['mean']):
    r, b = rows[i], blind.get(i, {})
    print('%-7s %-6.3f %-6.3f %-6.3f %-5s %-5s %-6s %-6s %-6s %-22s %s' % (i, r['A'], r['B'], r['mean'], r['compliance'], r['truthOk'], r['beatsLoser'],
          r['beatsWinner'], r['passes'], json.dumps(b.get('thumbs')), r['under6']))
    print('        wins:', json.dumps(b.get('beatsWinnerBy')), 'losers:', json.dumps(b.get('beatsLoserBy')),
          '| truth A %.2f B %.2f copy A %.2f B %.2f' % (r['dimsA']['truth'], r['dimsB']['truth'], r['dimsA']['copy'], r['dimsB']['copy']))
    for c in 'AB':
        for x in r['runs'][c]:
            if not x['compliancePass'] or min(x[k] for k in D) < 6.5:
                print('        %s%d low/flag: %s%s' % (c, x['run'], x['worstIssue'][:200], '' if x['compliancePass'] else ' | COMPLIANCE: ' + x['complianceNotes'][:200]))
