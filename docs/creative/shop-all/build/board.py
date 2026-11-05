# Builds the Shop All review board: the ten ads to run (Feed beside Story, scores, the exact Meta copy and link), the campaign
# plan, where the photos came from, the other ten, and the ratings of the competitor screenshots, the Naira Twenty ads and the
# captions. Usage: board.py <out_dir>   (reads ../research/*.json and ../plan.json; images are referenced as ads/ and thumbs/)
import html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
esc = lambda s: html.escape(str(s if s is not None else ""), quote=True)
J = lambda p: json.load(open(os.path.join(ROOT, p)))


def score(v):
    return "–" if v is None else ("%.1f" % v)


def main():
    out = sys.argv[1]
    judging, plan = J("research/judging.json"), J("plan.json")
    comp, naira, caps = J("research/competitor_ratings.json"), J("research/naira_twenty_ratings.json"), J("research/captions_comparison.json")
    concepts = {c["no"]: c for c in J("research/concepts.json")["final"]}
    table = {t["no"]: t for t in judging["table"]}
    copy = {c["no"]: c for c in judging["caps"]["ads"]}
    fixed = {f["no"]: f for f in judging["fixed"]}
    picks = judging["pick"]["picks"]
    order = [p["no"] for p in picks]

    cards = []
    for i, p in enumerate(picks, 1):
        no, c, t, cp, f = p["no"], concepts[p["no"]], table[p["no"]], copy.get(p["no"], {}), fixed.get(p["no"], {})
        v = f.get("verify") or {}
        link = plan["link_base"] + "&utm_content=" + no.lower() + "_" + plan["slugs"][no]
        cards.append("""<article class="ad" id="%(id)s">
<div class="pics"><img src="ads/%(no)s_feed.jpg" alt="%(name)s, Feed 4:5" loading="lazy" width="1080" height="1350"><img src="ads/%(no)s_story.jpg" alt="%(name)s, Story 9:16" loading="lazy" width="1080" height="1920"></div>
<div class="meta"><div class="row"><span class="no">%(i)02d · %(no)s · %(fam)s</span><span class="sc" title="Media buyer · creative director · checker">%(b)s · %(d)s · %(k)s</span></div>
<h3>%(name)s</h3><p class="role">%(role)s</p>
<dl class="copy"><dt>Primary text</dt><dd><span class="t">%(pt)s</span><button type="button" class="cp" data-copy="%(pt)s">Copy</button></dd>
<dt>Headline</dt><dd><span class="t">%(hl)s</span><button type="button" class="cp" data-copy="%(hl)s">Copy</button></dd>
<dt>Description</dt><dd><span class="t">%(ds)s</span></dd>
<dt>Link</dt><dd><span class="t url">%(link)s</span><button type="button" class="cp" data-copy="%(link)s">Copy</button></dd></dl>
<details><summary>Why it is in, and what was fixed</summary><p>%(why)s</p><ul>%(fixes)s</ul><p class="v">%(vline)s</p></details>
</div></article>""" % {
            "id": no.lower(), "no": no, "i": i, "fam": esc(c["family"]), "name": esc(c["name"]), "role": esc(p["role"]),
            "b": score(t["buyer"]), "d": score(t["director"]), "k": score(t["checker"]),
            "pt": esc(cp.get("primary_text", c["caption"])), "hl": esc(cp.get("headline", c["headline"])), "ds": esc(cp.get("description", "")),
            "link": esc(link), "why": esc(p["why"]), "fixes": "".join("<li>%s</li>" % esc(x) for x in (f.get("done") or p["fixes"])),
            "vline": esc(("Independent re-check: %s, %s/10." % ("passes" if v.get("pass") else "still has notes: " + "; ".join(v.get("defects", [])), score(v.get("score")))) if v else "")})

    rest = []
    why_not = {w["no"]: w["why"] for w in judging["pick"]["why_not"]}
    for no in sorted(table, key=lambda n: -table[n]["score"]):
        if no in order:
            continue
        t, c = table[no], concepts[no]
        rest.append('<figure class="th"><div class="pp"><img src="thumbs/%s_feed.jpg" alt="%s, Feed" loading="lazy"><img src="thumbs/%s_story.jpg" alt="%s, Story" loading="lazy"></div><figcaption><b>%s · %s</b> <span class="sc">%s</span><br>%s</figcaption></figure>'
                    % (no, esc(c["name"]), no, esc(c["name"]), no, esc(c["name"]), "%.2f" % t["score"], esc(why_not.get(no, ""))))

    comp_rows = "".join('<figure class="cmp"><img src="screens/%s" alt="%s ad screenshot" loading="lazy"><figcaption><b>%s</b> <span class="big">%s</span><br><span class="hook">%s</span><br>%s</figcaption></figure>'
                        % (os.path.basename(a["file"]), esc(a["brand"]), esc(a["brand"]), score(a["overall"]), esc(a["hook_text"][:120]), esc(a["steal"][:260]))
                        for a in sorted(comp["ads"], key=lambda a: -a["overall"]))
    naira_rows = "".join("<tr><td>%s</td><td>%s</td><td class='n'>%s</td><td class='n'>%s</td><td class='n'><b>%s</b></td><td>%s</td></tr>"
                         % (esc(a["key"].replace("_", " ")), esc(a["hook"][:70]), score(a["feed"]), score(a["story"]), score(a["overall"]), esc(a["weaknesses"][:170]))
                         for a in sorted(naira["ads"], key=lambda a: -a["overall"]))
    cap_rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (esc(x["dimension"]), esc(x["verdict"])) for x in caps["comparison"])
    rules = "".join("<li>%s</li>" % esc(r) for r in caps["rules"])
    src_rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (esc(s["ad"]), esc(s["result"]), esc(s["used"])) for s in plan["sources"])
    live_rows = "".join("<tr><td>%s</td><td class='n'>%s</td><td class='n'>%s</td><td class='n'>%s</td><td class='n'>%s</td></tr>" % tuple(esc(x) for x in r) for r in plan["live"])
    plan_rows = "".join("<tr><th scope='row'>%s</th><td>%s</td></tr>" % (esc(k), esc(v)) for k, v in plan["setup"])
    rules_rows = "".join("<li>%s</li>" % esc(r) for r in plan["rules"])
    flags = "".join("<li>%s</li>" % esc(f) for f in plan["flags"])
    page = TEMPLATE % {"cards": "".join(cards), "rest": "".join(rest), "comp": comp_rows, "naira": naira_rows, "caprows": cap_rows,
                       "rules": rules, "src": src_rows, "live": live_rows, "plan": plan_rows, "prules": rules_rows, "flags": flags,
                       "idea": esc(plan["idea"]), "capsg": score(caps["scores"]["giva"]), "capsp": score(caps["scores"]["palmonas"]),
                       "capsn": score(caps["scores"]["naira"]), "capnote": esc(caps["source_note"]), "link": esc(plan["link_base"])}
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(page)
    print(os.path.join(out, "index.html"), len(page))


TEMPLATE = """<title>Never Just One</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600&display=swap">
<style>
/* A campaign book for Naira's Shop All ads: the ten to run first (each with its exact Meta copy), then the plan, then the evidence. */
:root{--bg:#FBF8F3;--paper:#F3EDE4;--ink:#1A1614;--mute:#6B615B;--line:#E2D8CC;--gold:#8E6229;--sage:#2F5D50;--red:#A8332A;
 --display:"Cormorant Garamond",Georgia,"Times New Roman",serif;--body:"Jost","Helvetica Neue",Arial,sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15110F;--paper:#1F1A17;--ink:#F3EDE4;--mute:#AA9F96;--line:#372E29;--gold:#D9AC69;--sage:#86BCA9;--red:#EA8D80;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15110F;--paper:#1F1A17;--ink:#F3EDE4;--mute:#AA9F96;--line:#372E29;--gold:#D9AC69;--sage:#86BCA9;--red:#EA8D80;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1200px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:40px 80px}
h1,h2,h3{font-family:var(--display);font-weight:500;text-wrap:balance;margin:0}
h1{font-size:clamp(48px,8vw,92px);line-height:.95;letter-spacing:-.01em;font-style:italic}
h2{font-size:clamp(30px,4vw,44px);line-height:1.05}
h3{font-size:25px;line-height:1.1;font-style:italic;margin-top:6px}
p{margin:0}
.eyebrow{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.lede{max-width:66ch;color:var(--mute);margin-top:16px;font-size:16px}
.facts{display:flex;flex-wrap:wrap;gap:10px 28px;margin-top:24px;padding-top:16px;border-top:1px solid var(--line)}
.facts div{min-width:0} .facts b{display:block;font-family:var(--display);font-size:30px;font-weight:600;line-height:1}
.facts span{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
section{margin-top:72px} section>header{max-width:72ch}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:36px 28px;margin-top:28px}
.ad{min-width:0}
.pics{display:grid;grid-template-columns:5fr 2.81fr;gap:8px;align-items:end}
.pics img,.pp img{display:block;width:100%;height:auto;background:var(--line)}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:10px;border-top:1px solid var(--line);padding-top:8px;margin-top:12px}
.no{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)} .sc{font-size:13px;color:var(--sage);font-weight:500;font-variant-numeric:tabular-nums;white-space:nowrap}
.role{font-size:14px;margin-top:4px}
.copy{margin:12px 0 0;display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:13.5px}
.copy dt{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);padding-top:3px}
.copy dd{margin:0;display:flex;gap:8px;align-items:flex-start;min-width:0}
.copy .t{flex:1;min-width:0;overflow-wrap:anywhere} .url{font-size:12px;color:var(--mute)}
.cp{font:500 11px var(--body);letter-spacing:.12em;text-transform:uppercase;border:1px solid var(--line);background:transparent;color:var(--ink);padding:4px 8px;cursor:pointer;flex:none}
.cp:hover,.cp:focus-visible{border-color:var(--ink)} .cp.ok{color:var(--sage);border-color:var(--sage)}
details{margin-top:12px;font-size:13.5px;color:var(--mute)} summary{cursor:pointer;color:var(--ink)} details ul{padding-left:18px;margin:8px 0} details p{margin-top:6px}
.v{color:var(--sage)}
table{border-collapse:collapse;width:100%;font-size:14px;margin-top:18px}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}
thead th{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute);font-weight:500}
tbody th{font-weight:500;width:28%} td.n{font-variant-numeric:tabular-nums;white-space:nowrap}
.tw{overflow-x:auto}
ul.list{padding-left:18px;max-width:84ch;margin:14px 0 0} ul.list li{margin:6px 0}
.rest{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:22px;margin-top:22px}
.th{margin:0;min-width:0} .pp{display:grid;grid-template-columns:5fr 2.81fr;gap:5px;align-items:end}
.th figcaption{font-size:12.5px;color:var(--mute);margin-top:8px} .th b{color:var(--ink);font-weight:500}
.cmps{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:20px;margin-top:22px}
.cmp{margin:0;min-width:0} .cmp img{display:block;width:100%;height:auto;background:var(--line)}
.cmp figcaption{font-size:12.5px;color:var(--mute);margin-top:8px} .cmp b{color:var(--ink);font-weight:500}
.cmp .big{font-family:var(--display);font-size:22px;color:var(--ink);font-weight:600;float:right;line-height:1}
.hook{font-style:italic;color:var(--ink)}
.scores{display:flex;flex-wrap:wrap;gap:12px 32px;margin-top:18px}
.scores div b{font-family:var(--display);font-size:38px;font-weight:600;line-height:1;display:block} .scores span{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}
.note{font-size:13px;color:var(--mute);max-width:84ch;margin-top:12px}
footer{margin-top:80px;border-top:1px solid var(--line);padding-top:18px;font-size:13px;color:var(--mute);max-width:90ch}
@media (prefers-reduced-motion: reduce){*{scroll-behavior:auto}}
</style>
<div class="wrap">
<p class="eyebrow">Naira · Shop All · ₹1,000 a day</p>
<h1>Never just one</h1>
<p class="lede">%(idea)s</p>
<div class="facts"><div><b>40</b><span>creatives made</span></div><div><b>10</b><span>to run</span></div><div><b>₹1,000</b><span>a day</span></div><div><b>130+</b><span>pieces, from ₹599</span></div><div><b>0</b><span>new photos</span></div></div>

<section id="ten"><header><p class="eyebrow">Run these</p><h2>The ten, Feed beside Story</h2>
<p class="lede">Picked from 20 concepts (40 images) by three independent judges: a media buyer, a creative director and a fact checker (their scores, out of 10, in that order). Every pick was then fixed and checked again by someone who had not seen it. The copy beside each is ready to paste into Ads Manager; the button is Shop now.</p></header>
<div class="grid">%(cards)s</div></section>

<section id="plan"><header><p class="eyebrow">How to run it</p><h2>The campaign</h2></header>
<div class="tw"><table><tbody>%(plan)s</tbody></table></div>
<h3 style="margin-top:28px">Rules for the first two weeks</h3><ul class="list">%(prules)s</ul>
<h3 style="margin-top:28px">What is live now (last 7 days)</h3>
<div class="tw"><table><thead><tr><th>Campaign</th><th>Spend</th><th>CTR</th><th>Purchases</th><th>ROAS</th></tr></thead><tbody>%(live)s</tbody></table></div>
<p class="note">Nothing has been created or changed on Meta. The campaign above is built only when you say so.</p></section>

<section id="sources"><header><p class="eyebrow">Built on what clicked</p><h2>Where the photos come from</h2>
<p class="lede">Every photo in these ads is one Naira has already run or listed; no new photos were made. These are the ads that earned the clicks.</p></header>
<div class="tw"><table><thead><tr><th>Ad</th><th>Result on Meta</th><th>Used in</th></tr></thead><tbody>%(src)s</tbody></table></div></section>

<section id="rest"><header><p class="eyebrow">Made, not picked</p><h2>The other ten</h2><p class="lede">With the panel's combined score and why each sat out. Any of them can replace a tired ad later.</p></header>
<div class="rest">%(rest)s</div></section>

<section id="ratings"><header><p class="eyebrow">Out of 10</p><h2>The screenshots you sent</h2>
<p class="lede">GIVA, Palmonas, Snitch and Lenskart, rated by an independent strategist for clicks from a cold scroll. Under each: what Naira should take from it.</p></header>
<div class="cmps">%(comp)s</div>
<h3 style="margin-top:40px">The Naira Twenty ads, rated again</h3>
<p class="note">Rated without seeing the earlier scores. Feed, Story and overall, out of 10.</p>
<div class="tw"><table><thead><tr><th>Ad</th><th>Hook</th><th>Feed</th><th>Story</th><th>Overall</th><th>Weakest point</th></tr></thead><tbody>%(naira)s</tbody></table></div></section>

<section id="captions"><header><p class="eyebrow">Captions</p><h2>GIVA and Palmonas against Naira</h2></header>
<div class="scores"><div><b>%(capsn)s</b><span>Naira</span></div><div><b>%(capsg)s</b><span>GIVA</span></div><div><b>%(capsp)s</b><span>Palmonas</span></div></div>
<p class="note">%(capnote)s</p>
<div class="tw"><table><thead><tr><th>What was compared</th><th>Verdict</th></tr></thead><tbody>%(caprows)s</tbody></table></div>
<h3 style="margin-top:28px">The rules the ten captions follow</h3><ul class="list">%(rules)s</ul></section>

<section id="flags"><header><p class="eyebrow">Before you spend</p><h2>Things to know</h2></header><ul class="list">%(flags)s</ul></section>
<footer>Prices, stock and the offer were read from Shopify and the live store on 4 November 2026; Meta results from the account's own reporting. Shop All link: %(link)s</footer>
</div>
<script>
document.addEventListener('click', function (e) {
  var b = e.target.closest('.cp'); if (!b) return;
  var t = b.getAttribute('data-copy');
  function done(ok) { b.textContent = ok ? 'Copied' : 'Select'; b.classList.toggle('ok', ok); setTimeout(function () { b.textContent = 'Copy'; b.classList.remove('ok'); }, 1600); }
  function sel() { var s = b.parentNode.querySelector('.t'); var r = document.createRange(); r.selectNodeContents(s); var w = window.getSelection(); w.removeAllRanges(); w.addRange(r); done(false); }
  try { navigator.clipboard.writeText(t).then(function () { done(true); }, sel); } catch (err) { sel(); }
});
</script>
"""

if __name__ == "__main__":
    main()
