# Builds the review board page (index.html) for the 20 ads from the layouts, captions and the judge's round-2 file.
# Usage: board.py judge_r2.json out.html   (the page references ads/<key>_{feed,story}.jpg next to it)
import html, json, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SETS = [
    ("set1", "Set 1", "Studio product cards", "Palmonas's carousel card on a rosewood studio, plus what our own catalogue winners carry and theirs do not: the price and the buy-more chip."),
    ("set2", "Set 2", "Wedding-season moments", "GIVA's grammar: one Indian ritual, one witty serif line. Mehendi, gajra, the gift, the sangeet, the Banarasi."),
    ("set3", "Set 3", "Offer heroes", "The Palmonas '9KT Pendant Free' lockup on a black camisole and a blush set: each card carries one true reason to buy now."),
    ("set4", "Set 4", "Best of, after the judge", "One occasion, one line, one saturated colour behind the piece, four type lines at most, the Story composed first."),
]

def esc(s): return html.escape(s or "", quote=True)

def main():
    judge = json.load(open(sys.argv[1])); out = sys.argv[2]
    by_id = {a["id"]: a for a in judge["ads"]}
    caps = {a["key"]: a for a in json.load(open(os.path.join(HERE, "..", "captions.json")))["ads"]}
    groups = {}
    for a in judge["ads"]: groups.setdefault(a["group"], []).append(a["score"])
    mean = {g: statistics.mean(v) for g, v in groups.items()}
    bench = sorted([a for a in judge["ads"] if a["group"] == "benchmark"], key=lambda a: -a["score"])
    new = [a for a in judge["ads"] if a["group"].startswith("set")]
    top = max(new, key=lambda a: a["score"])
    rows = []
    for g in ("benchmark", "naira_recent", "set1", "set2", "set3", "set4"):
        label = {"benchmark": "GIVA + Palmonas, live ads", "naira_recent": "Naira's recent ads", "set1": "Set 1", "set2": "Set 2", "set3": "Set 3", "set4": "Set 4"}[g]
        v = mean.get(g)
        if v is None: continue
        rows.append('<div class="bar%s"><span class="bl">%s</span><span class="bt"><i style="width:%.1f%%"></i></span><span class="bv">%.2f</span></div>'
                    % (" ours" if g.startswith("set") else "", esc(label), v * 10, v))
    sections = []
    for gid, num, name, about in SETS:
        lay = json.load(open(os.path.join(HERE, "%s_layout.json" % gid.replace("set", "set"))))["ads"]
        cards = []
        for a in lay:
            k = a["key"]; j = by_id.get(k, {}); c = caps.get(k, {})
            line = (a.get("line") or a.get("feed", {}).get("line") or a.get("name", "")).replace("<br>", " ")
            cards.append(
                '<article class="ad" id="%s"><div class="pics"><img class="feed" src="ads/%s_feed.jpg" alt="%s, Feed 4:5" loading="lazy" width="1080" height="1350">'
                '<img class="story" src="ads/%s_story.jpg" alt="%s, Story 9:16" loading="lazy" width="1080" height="1920"></div>'
                '<div class="meta"><div class="row"><span class="no">%s</span><span class="score">%s</span></div>'
                '<h3>%s</h3><p class="cap"><b>%s</b> %s</p><p class="j"><span>Judge</span> %s</p><p class="j fix"><span>Next</span> %s</p></div></article>'
                % (esc(k.split("_")[0].lower()), k, esc(line), k, esc(line), esc(k.split("_")[0]), ("%.2f" % j["score"]) if j else "", esc(line),
                   esc(c.get("headline")), esc(c.get("text")), esc(j.get("best")), esc(j.get("fix"))))
        note = judge.get("set_notes", {}).get(gid, "")
        sections.append('<section class="set" id="%s"><header><p class="eyebrow">%s · mean %.2f</p><h2>%s</h2><p class="about">%s</p><p class="note">%s</p></header><div class="grid">%s</div></section>'
                        % (gid, num, mean.get(gid, 0), esc(name), esc(about), esc(note), "".join(cards)))
    names = {"PAL-9KT-hero": "Palmonas, 9KT Pendant Free", "PAL-9KT-card": "Palmonas, 9KT card", "GIVA-tea": "GIVA, a hot cup of silver",
             "PAL-catalogue": "Palmonas catalogue", "GIVA-catalogue": "GIVA catalogue"}
    top_name = (caps.get(top["id"], {}).get("headline", top["id"]).split(" · ")[0])
    launch = judge.get("launch", "") + " The Story fixes the judge asked for have been made since it scored."
    page = TEMPLATE % {"bars": "".join(rows), "sections": "".join(sections), "launch": esc(launch),
                       "bench": esc(names.get(bench[0]["id"], bench[0]["id"])), "benchv": bench[0]["score"], "top": esc(top_name), "topv": top["score"]}
    open(out, "w").write(page); print(out, len(page))

TEMPLATE = """<title>Naira Twenty</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500&display=swap">
<style>
/* Layout: a jewellery lookbook. Scorecard first, then four sets; each ad is the Feed card with its Story beside it and the judge's note below. */
:root{--bg:#FBF8F3;--paper:#F3EDE4;--ink:#1A1614;--mute:#6E645E;--line:#E2D8CC;--gold:#9A6B2F;--ours:#2F5D50;
 --display:"Cormorant Garamond",Georgia,"Times New Roman",serif;--body:"Jost","Helvetica Neue",Arial,sans-serif}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15110F;--paper:#1E1916;--ink:#F3EDE4;--mute:#A99D94;--line:#352C27;--gold:#D4A764;--ours:#7FB8A6;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15110F;--paper:#1E1916;--ink:#F3EDE4;--mute:#A99D94;--line:#352C27;--gold:#D4A764;--ours:#7FB8A6;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:40px 72px}
h1,h2,h3{font-family:var(--display);font-weight:500;text-wrap:balance;margin:0}
h1{font-size:clamp(40px,6vw,64px);line-height:1.02;letter-spacing:-.01em}
.lede{max-width:62ch;color:var(--mute);margin:14px 0 0}
.eyebrow{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin:0 0 8px}
.card{background:var(--paper);border:1px solid var(--line);padding:22px 22px 18px;margin-top:28px}
.bars{display:grid;gap:10px;margin-top:6px}
.bar{display:grid;grid-template-columns:minmax(0,210px) 1fr 52px;gap:12px;align-items:center;font-size:14px}
.bl{color:var(--mute)} .bt{height:10px;background:var(--line);position:relative}
.bt i{position:absolute;inset:0 auto 0 0;background:var(--mute)} .bar.ours .bt i{background:var(--ours)} .bar.ours .bl{color:var(--ink)}
.bv{font-variant-numeric:tabular-nums;text-align:right}
.facts{display:flex;flex-wrap:wrap;gap:8px 28px;margin-top:16px;font-size:13px;color:var(--mute)}
.facts b{color:var(--ink);font-weight:500}
.launch{margin-top:14px;font-size:14px;max-width:80ch}
.set{margin-top:64px} .set header{max-width:70ch}
h2{font-size:clamp(30px,4vw,42px);line-height:1.05}
.about{margin:8px 0 0} .note{margin:8px 0 0;color:var(--mute);font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:28px;margin-top:26px}
.ad{min-width:0}
.pics{display:grid;grid-template-columns:5fr 2.81fr;gap:8px;align-items:end}
.pics img{display:block;width:100%%;height:auto;background:var(--line)}
.meta{margin-top:12px}
.row{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--line);padding-top:8px}
.no{font-size:12px;letter-spacing:.16em;color:var(--mute)} .score{font-variant-numeric:tabular-nums;font-weight:500;color:var(--ours)}
h3{font-size:24px;line-height:1.12;margin-top:6px;font-style:italic}
.cap{font-size:14px;margin:8px 0 0} .cap b{font-weight:500;display:block}
.j{font-size:13px;color:var(--mute);margin:8px 0 0} .j span{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-right:6px}
footer{margin-top:72px;border-top:1px solid var(--line);padding-top:18px;font-size:13px;color:var(--mute);max-width:90ch}
@media (max-width:520px){.bar{grid-template-columns:minmax(0,1fr) 38%% 44px}}
</style>
<div class="wrap">
<p class="eyebrow">Naira · Meta ads · 4 Nov 2026</p>
<h1>Twenty ads, four sets, one scorecard</h1>
<p class="lede">GIVA's and Palmonas's live ads, our recent ads and the twenty new ones, scored on one ten-point rubric by an independent judge that saw only the images. Each set was made from new Higgsfield photos, checked against the product page for size and detail, and redone where it fell short before the next set began.</p>
<div class="card"><p class="eyebrow">Mean score, round 2</p><div class="bars">%(bars)s</div>
<div class="facts"><span>Best competitor ad: <b>%(bench)s · %(benchv).2f</b></span><span>Best new ad: <b>%(top)s · %(topv).2f</b></span><span>Every Feed card 1080×1350, every Story 1080×1920</span></div>
<p class="launch"><b>Where the judge would spend first.</b> %(launch)s</p></div>
%(sections)s
<footer>Prices are the live Shopify prices on 4 November. The Buy 2 · 10%% off and Buy 3 · 20%% off chip is the site's automatic discount, applied in the bag with no code. Free insured shipping, insured delivery in 3–5 working days, cash on delivery on serviceable pincodes and the Naira gift box are as the storefront states them. Colours are named as colours and metals as gold tone or silver tone. Two frames still read slightly large against the body: the emerald deco hoop (about 1.3×, the same as its live listing photo) and the ribbon bracelet's bow (about 1.3×).</footer>
</div>
"""

if __name__ == "__main__":
    main()
