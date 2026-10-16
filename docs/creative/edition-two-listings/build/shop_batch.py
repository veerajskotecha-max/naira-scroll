import json, sys, os
b = json.load(open('shop/batches.json'))
done = {'silk-mesh-cuff'}
rest = [h for g in b for h in g if h not in done]
B = [rest[i:i+5] for i in range(0, len(rest), 5)]
json.dump(B, open('shop/batches2.json', 'w'), indent=1)
n = int(sys.argv[1])
hs = B[n]
letters = 'abcdefgh'
vars_ = {letters[i]: json.load(open(f'shop/{h}.json')) for i, h in enumerate(hs)}
decl = ', '.join(f'${l}: ProductSetInput!' for l in vars_)
sel = ' '.join(f'{l}: productSet(input: ${l}, synchronous: true) {{ product {{ id handle status variants(first: 20) {{ nodes {{ sku media(first: 1) {{ nodes {{ id }} }} }} }} }} userErrors {{ field message code }} }}' for l in vars_)
q = f'mutation({decl}) {{ {sel} }}'
open(f'shop/b{n}.q', 'w').write(q)
open(f'shop/b{n}.json', 'w').write(json.dumps(vars_, ensure_ascii=False, separators=(',', ':')))
print(len(B), 'batches;', hs, os.path.getsize(f'shop/b{n}.json'), 'bytes')
