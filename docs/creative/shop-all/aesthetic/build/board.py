# Builds the review board for the aesthetic Shop All ads: the ten to run (Feed beside Story, scores, exact Meta copy and
# link, what changed after review), how to run them beside the first ten, where the photos came from, the ones not picked,
# and the things to know. Usage: board.py <out_dir>   (reads ../research/*.json and ../plan.json; images in ads/ and thumbs/)
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
esc = lambda s: html.escape(str(s if s is not None else ""), quote=True)
J = lambda p: json.load(open(os.path.join(ROOT, p)))


def fill(t, vals):
    # %(key)s placeholders only, so the CSS can use plain % signs
    return re.sub(r"%\((\w+)\)s", lambda m: str(vals[m.group(1)]), t)


def score(v):
    return "–" if v is None else ("%.1f" % v)


def main():
    out = sys.argv[1]
    judging, plan, specs = J("research/judging.json"), J("plan.json"), {s["no"]: s for s in J("research/specs.json")}
    caps = {c["no"]: c for c in J("research/captions.json")}
    notes = {c["no"]: c for c in J("research/changes.json")} if os.path.exists(os.path.join(ROOT, "research/changes.json")) else {}
    table = {t["no"]: t for t in judging["table"]}
    fixed = {f["no"]: f for f in judging["fixed"] if f}
    picks = judging["pick"]["picks"]

    cards = []
    for i, p in enumerate(picks, 1):
        no, sp, t, cp, f, n = p["no"], specs[p["no"]], table[p["no"]], caps.get(p["no"], {}), fixed.get(p["no"], {}), notes.get(p["no"], {})
        v = f.get("verify") or {}
        link = plan["link_base"] + "&utm_content=" + no.lower() + "_" + plan["slugs"][no]
        changed = n.get("changes") or []
        still = n.get("still") or []
        vline = ""
        if v:
            vline = ("Checked again by a reviewer who had not seen it: passes, %s/10 for cold-scroll clicks." % score(v.get("score"))) if v.get("pass") \
                else ("Checked again: still has notes: " + "; ".join(v.get("defects", [])))
        cards.append(fill("""<article class="ad" id="%(id)s">
<div class="pics"><figure><img src="ads/%(no)s_feed.jpg" alt="%(name)s, Feed 4:5" loading="lazy" width="1080" height="1350"><figcaption>Feed 4:5</figcaption></figure><figure><img src="ads/%(no)s_story.jpg" alt="%(name)s, Story 9:16" loading="lazy" width="1080" height="1920"><figcaption>Story 9:16</figcaption></figure></div>
<div class="meta"><p class="folio"><span>%(i)s</span><span class="sc" title="Art director · media buyer · checker, out of 10">%(a)s · %(b)s · %(k)s</span></p>
<h3>%(name)s</h3><p class="role">%(role)s</p>
<dl class="copy"><dt>Primary text</dt><dd><span class="t">%(pt)s</span><button type="button" class="cp" data-copy="%(pt)s">Copy</button></dd>
<dt>Headline</dt><dd><span class="t">%(hl)s</span><button type="button" class="cp" data-copy="%(hl)s">Copy</button></dd>
<dt>Description</dt><dd><span class="t">%(ds)s</span></dd>
<dt>Link</dt><dd><span class="t url">%(link)s</span><button type="button" class="cp" data-copy="%(link)s">Copy</button></dd></dl>
<details><summary>Why it is in, and what changed after review</summary><p>%(why)s</p>%(changed)s<p class="v">%(vline)s</p>%(still)s</details>
</div></article>""", {
            "id": no.lower(), "no": no, "i": "%02d" % i, "name": esc(sp["name"]), "role": esc(p["role"]),
            "a": score(t.get("art")), "b": score(t.get("buyer")), "k": score(t.get("check")),
            "pt": esc(cp.get("primary_text", "")), "hl": esc(cp.get("headline", "")), "ds": esc(cp.get("description", "")),
            "link": esc(link), "why": esc(p["why"]),
            "changed": ("<ul>" + "".join("<li>%s</li>" % esc(x) for x in changed) + "</ul>") if changed else "",
            "vline": esc(vline), "still": ("<p class='still'>Still worth knowing: " + esc(" ".join(still)) + "</p>") if still else ""}))

    order = [p["no"] for p in picks]
    why_not = {w["no"]: w["why"] for w in judging["pick"]["why_not"]}
    rest = "".join(fill('<figure class="th"><div class="pp"><img src="thumbs/%(no)s_feed.jpg" alt="%(name)s, Feed" loading="lazy"><img src="thumbs/%(no)s_story.jpg" alt="%(name)s, Story" loading="lazy"></div><figcaption><b>%(name)s</b> <span class="sc">%(s)s</span><br>%(why)s</figcaption></figure>',
                        {"no": no, "name": esc(specs[no]["name"]), "s": "%.2f" % table[no]["score"], "why": esc(why_not.get(no, ""))})
                   for no in sorted(table, key=lambda n: -table[n]["score"]) if no not in order)
    rows = lambda pairs: "".join("<tr><th scope='row'>%s</th><td>%s</td></tr>" % (esc(k), esc(v)) for k, v in pairs)
    page = fill(TEMPLATE, {
        "title": esc(plan["title"]), "idea": esc(plan["idea"]), "cards": "".join(cards), "rest": rest or "<p class='note'>All the ads built were picked.</p>",
        "n_built": len(table), "n_concepts": plan.get("n_concepts", ""), "setup": rows(plan["setup"]),
        "rules": "".join("<li>%s</li>" % esc(r) for r in plan["rules"]),
        "src": "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (esc(s["ad"]), esc(s["result"]), esc(s["used"])) for s in plan["sources"]),
        "flags": "".join("<li>%s</li>" % esc(x) for x in plan["flags"]), "link": esc(plan["link_base"].split("?")[0]),
        "first": esc(plan["first_board"])})
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w").write(page)
    print(os.path.join(out, "index.html"), len(page))


TEMPLATE = """<title>%(title)s</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@400;500&display=swap">
<style>
/* A quiet gallery catalogue for Naira's aesthetic Shop All ads: each ad hangs like a print, with its label and copy beside it. */
:root{--bg:#F6F1EA;--paper:#EFE7DC;--ink:#1C1714;--mute:#6D625A;--line:#DDD2C4;--gold:#8A5E26;--sage:#2F5D50;
 --display:"Cormorant Garamond",Georgia,"Times New Roman",serif;--body:"Jost","Helvetica Neue",Arial,sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#14100E;--paper:#1D1815;--ink:#F1E9DE;--mute:#A99D93;--line:#3A312B;--gold:#D6A962;--sage:#8CC1AE;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14100E;--paper:#1D1815;--ink:#F1E9DE;--mute:#A99D93;--line:#3A312B;--gold:#D6A962;--sage:#8CC1AE;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.6;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:48px 88px}
h1,h2,h3{font-family:var(--display);font-weight:400;text-wrap:balance;margin:0}
h1{font-size:clamp(52px,9vw,104px);line-height:.92;letter-spacing:-.015em}
h1 em{font-style:italic;color:var(--gold)}
h2{font-size:clamp(32px,4.4vw,48px);line-height:1.05}
h3{font-size:28px;line-height:1.1;font-style:italic}
p{margin:0}
.eyebrow{font-size:11.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);margin:0 0 14px}
.lede{max-width:64ch;color:var(--mute);margin-top:20px;font-size:16.5px}
.facts{display:flex;flex-wrap:wrap;gap:12px 40px;margin-top:30px;padding-top:18px;border-top:1px solid var(--line)}
.facts div{min-width:0}.facts b{display:block;font-family:var(--display);font-size:34px;font-weight:500;line-height:1}
.facts span{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute)}
section{margin-top:84px} section>header{max-width:70ch}
.ad{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:40px;padding:44px 0;border-top:1px solid var(--line)}
.ad:first-of-type{border-top:0}
@media (max-width:860px){.ad{grid-template-columns:1fr;gap:22px}}
.pics{display:grid;grid-template-columns:5fr 2.81fr;gap:14px;align-items:end;min-width:0}
.pics figure{margin:0;min-width:0}
.pics img,.pp img{display:block;width:100%;height:auto;background:var(--paper);box-shadow:0 1px 2px rgba(0,0,0,.06),0 10px 28px -14px rgba(60,40,20,.35)}
.pics figcaption{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--mute);margin-top:8px}
.meta{min-width:0;align-self:center}
.folio{display:flex;justify-content:space-between;align-items:baseline;gap:12px;font-size:12px;letter-spacing:.2em;color:var(--mute)}
.folio span:first-child{font-family:var(--display);font-size:22px;letter-spacing:0;color:var(--gold)}
.sc{font-size:12.5px;letter-spacing:.04em;color:var(--sage);font-variant-numeric:tabular-nums;white-space:nowrap}
.meta h3{margin-top:8px}
.role{margin-top:6px;color:var(--mute);max-width:52ch}
.copy{margin:20px 0 0;display:grid;grid-template-columns:auto 1fr;gap:9px 14px;font-size:14px}
.copy dt{font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);padding-top:3px}
.copy dd{margin:0;display:flex;gap:10px;align-items:flex-start;min-width:0}
.copy .t{flex:1;min-width:0;overflow-wrap:anywhere}.url{font-size:12px;color:var(--mute)}
.cp{font:500 10.5px var(--body);letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--line);background:transparent;color:var(--ink);padding:5px 9px;cursor:pointer;flex:none}
.cp:hover,.cp:focus-visible{border-color:var(--ink);outline:none}.cp.ok{color:var(--sage);border-color:var(--sage)}
details{margin-top:18px;font-size:14px;color:var(--mute)} summary{cursor:pointer;color:var(--ink)} summary:focus-visible{outline:1px solid var(--gold)}
details ul{padding-left:18px;margin:10px 0} details p{margin-top:8px} .v{color:var(--sage)} .still{font-style:italic}
table{border-collapse:collapse;width:100%;font-size:14px;margin-top:20px}
th,td{text-align:left;vertical-align:top;padding:10px 12px;border-bottom:1px solid var(--line)}
thead th{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--mute);font-weight:500}
tbody th{font-weight:500;width:26%}
.tw{overflow-x:auto}
ul.list{padding-left:18px;max-width:84ch;margin:16px 0 0} ul.list li{margin:7px 0}
.rest{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:26px;margin-top:24px}
.th{margin:0;min-width:0}.pp{display:grid;grid-template-columns:5fr 2.81fr;gap:6px;align-items:end}
.th figcaption{font-size:12.5px;color:var(--mute);margin-top:10px}.th b{color:var(--ink);font-weight:500}
.note{font-size:13.5px;color:var(--mute);max-width:84ch;margin-top:14px}
footer{margin-top:88px;border-top:1px solid var(--line);padding-top:20px;font-size:13px;color:var(--mute);max-width:90ch;overflow-wrap:anywhere}
a{color:var(--gold)}
</style>
<div class="wrap">
<p class="eyebrow">Naira · Shop All · the aesthetic ten</p>
<h1>%(title)s</h1>
<p class="lede">%(idea)s</p>
<div class="facts"><div><b>%(n_concepts)s</b><span>concepts written</span></div><div><b>%(n_built)s</b><span>built</span></div><div><b>10</b><span>to run</span></div><div><b>₹599–₹2,399</b><span>the whole collection</span></div><div><b>0</b><span>new photos</span></div></div>

<section id="ten"><header><p class="eyebrow">Hang these</p><h2>The ten, Feed beside Story</h2>
<p class="lede">Chosen from the ads built by three independent judges: an art director, a media buyer and a fact checker (their scores, out of 10, in that order). Each was then fixed and checked again by someone who had not seen it. The copy beside each is ready to paste into Ads Manager; the button is Shop now.</p></header>
%(cards)s</section>

<section id="run"><header><p class="eyebrow">How to run them</p><h2>Beside the first ten</h2></header>
<div class="tw"><table><tbody>%(setup)s</tbody></table></div>
<h3 style="margin-top:30px">Rules for the first two weeks</h3><ul class="list">%(rules)s</ul>
<p class="note">Nothing has been created or changed on Meta. The first ten: <a href="%(first)s">%(first)s</a></p></section>

<section id="sources"><header><p class="eyebrow">Built on what clicked</p><h2>Where the photos come from</h2>
<p class="lede">Every photo is one Naira has already run or listed; nothing new was generated.</p></header>
<div class="tw"><table><thead><tr><th>Photo</th><th>Result on Meta</th><th>Used in</th></tr></thead><tbody>%(src)s</tbody></table></div></section>

<section id="rest"><header><p class="eyebrow">Made, not picked</p><h2>The others</h2><p class="lede">With the panel's combined score and why each sat out.</p></header>
<div class="rest">%(rest)s</div></section>

<section id="flags"><header><p class="eyebrow">Before you spend</p><h2>Things to know</h2></header><ul class="list">%(flags)s</ul></section>
<footer>Prices and stock were read from Shopify on 7 November 2026; Meta results from the account's own reporting. Shop All: %(link)s</footer>
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
