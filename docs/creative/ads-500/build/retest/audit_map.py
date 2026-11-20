"""Map the fresh audit back to ids and apply PLAYBOOK §7 with the clean blind result.
Usage: python3 -I audit_map.py <audit_output.json> <key2.json> <blind_result.json> <out.json>"""
import json, sys

out = json.load(open(sys.argv[1]))
res = out['result'] if 'result' in out else out
key = json.load(open(sys.argv[2]))
blind = json.load(open(sys.argv[3]))['rows']
W = dict(stop=.15, message=.10, truth=.15, layout=.10, brand=.05, copy=.10, fit=.05, desire=.15, cues=.15)
D = list(W)

runs = {}          # id -> {'A': [run1, run2], 'B': [...]}
problems = []
for n, run in enumerate(res['runs']):
    r = run.get('result')
    if not r:
        problems.append('run %d (%s): no result' % (n, run['critic'])); continue
    got = set()
    for ad in r['ads']:
        c = ad['code'].strip().upper()
        if c not in key:
            problems.append('run %d: unknown code %s' % (n, c)); continue
        got.add(c)
        runs.setdefault(key[c], {'A': [], 'B': []})[run['critic']].append(dict(ad, run=n))
    miss = set(key) - got
    if miss:
        problems.append('run %d (%s): missing %s' % (n, run['critic'], sorted(miss)))

rows = {}
for i, d in runs.items():
    mean = {}
    for c in 'AB':
        rs = d[c]
        mean[c] = {k: round(sum(x[k] for x in rs) / len(rs), 3) for k in D} if rs else None
    wA = round(sum(mean['A'][k] * W[k] for k in D), 4) if mean['A'] else None
    wB = round(sum(mean['B'][k] * W[k] for k in D), 4) if mean['B'] else None
    comp = all(x['compliancePass'] for c in 'AB' for x in d[c])
    lows = sorted({'%s %s %.2f' % (c, k, mean[c][k]) for c in 'AB' if mean[c] for k in D if mean[c][k] < 6})
    truth_ok = all(mean[c]['truth'] >= 8 for c in 'AB' if mean[c])
    bl = blind.get(i, {})
    ship_ok = comp and truth_ok and not lows and bool(bl.get('beatsLoser'))
    rows[i] = dict(A=wA, B=wB, mean=round((wA + wB) / 2, 4) if wA is not None and wB is not None else None,
                   dimsA=mean['A'], dimsB=mean['B'], compliance=comp, truthOk=truth_ok, under6=lows,
                   beatsLoser=bool(bl.get('beatsLoser')), beatsWinner=bool(bl.get('beatsWinner')), passes=ship_ok,
                   runs={c: [{k: x[k] for k in D + ['compliancePass', 'complianceNotes', 'worstIssue', 'zeroCreditFix', 'run']} for x in d[c]] for c in 'AB'})

json.dump({'rows': rows, 'problems': problems,
           'method': [ (r.get('result') or {}).get('method') for r in res['runs'] ]}, open(sys.argv[4], 'w'), indent=1, ensure_ascii=False)
print('problems:', problems)
print('%-7s %-6s %-6s %-6s %-5s %-5s %-6s %-6s %s' % ('id', 'A', 'B', 'mean', 'comp', 'trth', 'loser', 'PASS', 'under 6'))
for i in sorted(rows, key=lambda i: -(rows[i]['mean'] or 0)):
    r = rows[i]
    print('%-7s %-6.3f %-6.3f %-6.3f %-5s %-5s %-6s %-6s %s' % (i, r['A'], r['B'], r['mean'], r['compliance'], r['truthOk'], r['beatsLoser'], r['passes'], r['under6']))
for i in sorted(rows):
    r = rows[i]
    print('\n' + i, 'truth A %.2f B %.2f | copy A %.2f B %.2f' % (r['dimsA']['truth'], r['dimsB']['truth'], r['dimsA']['copy'], r['dimsB']['copy']))
    for c in 'AB':
        for x in r['runs'][c]:
            print('  %s%d worst: %s | fix: %s%s' % (c, x['run'], x['worstIssue'][:170], x['zeroCreditFix'][:170],
                  '' if x['compliancePass'] else ' | COMPLIANCE FAIL: ' + x['complianceNotes'][:200]))
