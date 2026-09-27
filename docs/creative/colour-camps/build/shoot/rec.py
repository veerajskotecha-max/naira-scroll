"""rec.py q.json j.json idx:job_id ... | rec.py q.json j.json --url job_id url ...  — record submissions / results; downloads when url given"""
import json,sys,os,subprocess
Q=json.load(open(sys.argv[1])); jf=sys.argv[2]
J=json.load(open(jf)) if os.path.exists(jf) else {}
a=sys.argv[3:]
if a and a[0]=='--url':
    a=a[1:]
    for jid,url in zip(a[::2],a[1::2]):
        m=J[jid]; m['url']=url; fn=f"plates/{m['key']}.png"
        if not os.path.exists(fn): subprocess.run(['curl','-sS','-L','--max-time','120','-o',fn,url])
        print(fn, os.path.getsize(fn))
else:
    for x in a:
        i,jid=x.split(':'); q=Q[int(i)]; J[jid]={k:q[k] for k in ('key','camp','sku','shot','attempt')}
json.dump(J,open(jf,'w'),indent=1)
