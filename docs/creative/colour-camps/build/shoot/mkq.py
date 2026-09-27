"""mkq.py out.json SKU:S1,S2 ... — queue with fresh prompts from ladder.json; attempt = next free (plates on disk + any job json keys)"""
import json,os,sys,glob
L=json.load(open('ladder.json')); M=json.load(open('media.json'))
from ladder import P
taken=set(os.path.basename(f)[:-4] for f in glob.glob('plates/*.png'))
for jf in glob.glob('j*.json'):
    try: taken|={m['key'] for m in json.load(open(jf)).values()}
    except Exception: pass
Q=[]
for arg in sys.argv[2:]:
    sku,shots=arg.split(':'); camp=P[sku]['camp']
    for sh in shots.split(','):
        n=1
        while f'{camp}_{sku}_{sh}_a{n}' in taken: n+=1
        key=f'{camp}_{sku}_{sh}_a{n}'; taken.add(key)
        Q.append(dict(key=key,camp=camp,sku=sku,shot=sh,attempt=n,aspect='9:16' if sh=='S1' else '4:5',media=M.get(f'{sku}|{sh}',M[sku]),prompt=L[sku][sh]))
json.dump(Q,open(sys.argv[1],'w'),indent=1); print(len(Q),[q['key'] for q in Q])
