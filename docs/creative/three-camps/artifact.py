# -*- coding: utf-8 -*-
"""The Night Shift — one page that grows a section per set. Each set module supplies SET meta + CREATIVES; a
sets/<slug>/notes.json supplies the design plan, the review score and the ledger for that set."""
import json,base64,html,os,sys,importlib,glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from core import ROWS,DET,rupees,ROOT,ADS,skus_of
E=html.escape
def b64(p,mime="image/jpeg"): return f"data:{mime};base64,"+base64.b64encode(open(p,"rb").read()).decode()
def section(mod):
    slug=mod.SET["slug"]; notes=json.load(open(f"{ROOT}/{slug}/notes.json"))
    cards=[]
    for c in mod.CREATIVES:
        k=c["id"]; skus=skus_of(c)
        pcs="".join(f'<li><span>{E(ROWS[s]["title"])}</span><span class="m">{s} · {rupees(ROWS[s]["price"])} · {ROWS[s]["inv"]} in stock</span></li>' for s in skus)
        cards.append(f'''<article class="cr"><div class="imgs"><figure><img src="{b64(f'{ROOT}/{slug}/art/{k}_feed.jpg')}" alt="{k} feed"><figcaption>Feed · 1080×1350 <button class="dl" type="button" data-src="png/{slug}/{k}_feed.png" data-name="naira-{slug}-{k}-feed-1080x1350.png">↓ Download PNG</button></figcaption></figure>
<figure><img src="{b64(f'{ROOT}/{slug}/art/{k}_story.jpg')}" alt="{k} story"><figcaption>Story · 1080×1920 <button class="dl" type="button" data-src="png/{slug}/{k}_story.png" data-name="naira-{slug}-{k}-story-1080x1920.png">↓ Download PNG</button></figcaption></figure></div>
<div class="txt"><div class="eb">{k}</div><h3>{E(notes["cards"][k]["title"])}</h3><p>{notes["cards"][k]["why"]}</p><ul class="pc">{pcs}</ul>
<div class="m">Source <b>{E(notes["cards"][k]["source"])}</b> · Checked: {E(notes["cards"][k]["check"])}</div></div></article>''')
    score=notes["score"]
    return f'''<section class="set" id="{slug}"><div class="eb">Set {int(slug[:2]):02d} · {E(notes["device"])}</div><h2>{E(mod.SET["title"])}</h2>
<p class="lede">{E(notes["lede"])}</p>
<div class="plan"><div><span class="m">Idea</span><p>{notes["idea"]}</p></div><div><span class="m">Type</span><p>{notes["type"]}</p></div><div><span class="m">Review</span><p>{notes["review"]}</p></div></div>
<div class="score"><b>{score}</b><span>/10 after {notes["passes"]} pass{"es" if notes["passes"]!=1 else ""} — {E(notes["verdict"])}</span></div>
{"".join(cards)}</section>'''
def build(slugs,out):
    velista=b64(f"{ADS}/fonts/Velista.ttf","font/ttf")
    secs=[]; total=0
    for slug in slugs:
        mod=importlib.import_module(slug.split("-")[0].replace("0","set0") if False else f"set{slug[:2]}"); secs.append(section(mod)); total+=len(mod.CREATIVES)
    page=f'''<title>Three Camps in Bloom</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500&family=Jost:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
@font-face{{font-family:'Velista';src:url('{velista}') format('truetype');font-weight:400 600;font-display:swap}}
:root{{--bg:#F1EBE1;--ink:#1B1512;--ac:#6E1E2A;--mute:#7A6E66;--hair:rgba(27,21,18,.18);--tile:#FBF8F2}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#1E0A10;--ink:#F1EBE1;--ac:#F2C4BD;--mute:#C9AEB0;--hair:rgba(241,235,225,.22);--tile:#2E1218;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#1E0A10;--ink:#F1EBE1;--ac:#F2C4BD;--mute:#C9AEB0;--hair:rgba(241,235,225,.22);--tile:#2E1218;color-scheme:dark}}
body{{background:var(--bg);color:var(--ink);font-family:'Jost',system-ui,sans-serif;font-size:17px;line-height:1.55;padding-block:0 4rem;padding-inline:clamp(16px,4vw,48px)}}
.wrap{{max-width:1120px;margin:0 auto}}
header{{padding-block:3rem 2rem;border-bottom:1px solid var(--hair)}}
h1{{font-family:'Velista','Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(52px,9vw,112px);line-height:.92;letter-spacing:-.005em;text-transform:uppercase;text-wrap:balance}}
h1 .ac{{color:var(--ac)}}
.lede{{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(22px,2.6vw,30px);margin-top:.6rem;max-width:44ch}}
h2{{font-family:'Velista','Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(34px,4.5vw,56px);line-height:1;text-transform:uppercase;margin:0 0 .4rem;text-wrap:balance}}
h3{{font-family:'Velista','Cormorant Garamond',Georgia,serif;font-weight:500;font-size:clamp(24px,3vw,34px);line-height:1;text-transform:uppercase;margin:.3rem 0 .6rem}}
.eb,.m{{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute)}}
.m b{{color:var(--ink);font-weight:500}}
section{{padding-block:2.6rem;border-bottom:1px solid var(--hair)}}
p{{max-width:68ch}}
.plan{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.2rem 2rem;margin-top:1.4rem}} .plan p{{margin-top:.3rem;font-size:16px}}
.score{{display:flex;align-items:baseline;gap:.8rem;margin:1.6rem 0 .4rem;border-top:2px solid var(--ac);padding-top:.6rem;max-width:60ch}}
.score b{{font-family:'Velista','Cormorant Garamond',serif;font-weight:500;font-size:48px;line-height:1}} .score span{{color:var(--mute);font-size:15px}}
.cr{{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:1.4rem 2.4rem;padding-block:2rem;border-top:1px solid var(--hair)}}
.cr .imgs{{display:grid;grid-template-columns:1fr .78fr;gap:14px;align-items:start}}
.cr figure{{margin:0}} .dl{{display:none;float:right;font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ac);background:transparent;cursor:pointer;border:1px solid var(--ac);padding:.25rem .55rem;margin-left:.6rem}} .has-dl .dl{{display:inline-block}} .dl:hover{{background:var(--ac);color:var(--bg)}} .dl[disabled]{{opacity:.5;cursor:default}} .dlnote{{display:none;position:fixed;left:50%;bottom:1.2rem;transform:translateX(-50%);background:var(--ink);color:var(--bg);font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.72rem;letter-spacing:.06em;padding:.55rem .9rem;z-index:99}} .dlnote.on{{display:block}} .cr img{{width:100%;height:auto;display:block;background:var(--tile)}}
.cr figcaption{{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--mute);margin-top:8px}}
.pc{{list-style:none;padding:0;margin:1rem 0;display:grid;gap:6px}}
.pc li{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;border-bottom:1px solid var(--hair);padding-bottom:6px;font-weight:500}} .pc li .m{{font-weight:400}}
nav{{display:flex;flex-wrap:wrap;gap:.5rem 1.2rem;margin-top:1.4rem}} nav a{{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--hair);font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.08em;text-transform:uppercase}}
@media (max-width:760px){{.cr{{grid-template-columns:1fr}}}}
</style>
<div class="wrap">
<header><div class="eb">Naira Petite · paid social · the overnight run · 27 Sep 2026</div>
<h1>Three camps<br><span class="ac">in bloom.</span></h1>
<p class="lede">(pigment, the long afternoon and the bench, re-dressed one after another with the brand's own florals: the hero petals, the painted bloom, the watercolour sprig and vine. every plate verified against its listing first. {total} creatives so far.)</p>
<nav>{"".join(f'<a href="#{s}">{s}</a>' for s in slugs)}</nav></header>
{"".join(secs)}
<section><h2>How every set was gated</h2><p>Names and prices are read from Shopify at build time. A set does not render if a piece is inactive, unavailable, under thirteen units as a hero or under three as a listed piece, or if a water claim sits on a piece whose Care block lacks the waterproof line. Every figure in a spec line is checked against that piece's listing Details. Every frame — archive, website or freshly generated — was looked at against the listing before it was kept; rejected frames are named in each set's notes. Nothing here has been tested against live spend.</p></section>
<div class="dlnote" id="dlnote"></div>
<script>
(async()=>{{
  const note=document.getElementById('dlnote'); let t=null;
  const say=(m)=>{{note.textContent=m;note.classList.add('on');clearTimeout(t);t=setTimeout(()=>note.classList.remove('on'),3200);}};
  const dl=(window.claude&&window.claude.use)?await window.claude.use('downloads'):null;
  if(!dl) return;
  document.body.classList.add('has-dl');
  document.querySelectorAll('button.dl').forEach(b=>b.addEventListener('click',async()=>{{
    if(b.disabled) return; b.disabled=true; const was=b.textContent; b.textContent='fetching…';
    try{{
      const r=await fetch(b.dataset.src); if(!r.ok) throw new Error('fetch '+r.status);
      const blob=await r.blob(); b.textContent='saving…';
      await dl.save({{filename:b.dataset.name,data:blob}});
      say('saved '+b.dataset.name);
    }}catch(e){{
      const c=(e&&e.code)||''; if(c!=='declined') say(c==='rate_limited'?'one download at a time — try again in a moment':'could not save this file');
    }}finally{{ b.disabled=false; b.textContent=was; }}
  }}));
}})();
</script>
</div>'''
    open(out,"w").write(page); return len(page)
if __name__=="__main__":
    slugs=sys.argv[1].split(","); out=sys.argv[2]
    print("MB",round(build(slugs,out)/1e6,2))
