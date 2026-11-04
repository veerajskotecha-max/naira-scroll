# Builds the review page for the ten Toggle hook tests: the clasp findings first, then each ad (Feed beside Story) with its
# hook, format, the judge's verdict and the caption, then the fifteen that wait for credits.
# Usage: crazy_board.py judge_crazy.json out_dir   (writes out_dir/index.html; images are referenced as ads/ and proof/)
import html, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
esc = lambda s: html.escape(s or "", quote=True)
META = [
 ("X01_kabhi_front", "Kabhi front. Kabhi side.", "The clever one", "A Bollywood title turned into a product truth: the clasp sits at the front or the side."),
 ("X02_sticky_note", "Note to self: the clasp goes in FRONT.", "Lo-fi", "A sticky note and a marker arrow on a polished photo: the pattern interrupt."),
 ("X03_unpopular_opinion", "Unpopular opinion: the clasp is the best part of a necklace.", "Platform-native", "A plain post from Naira, the way a feed looks, not the way an ad looks."),
 ("X04_looks_expensive", "Looks expensive. Isn&rsquo;t.", "Price reveal", "The jewellery price-reveal hook, said dry, on the darkest, richest photo."),
 ("X05_gem_clip", "Gem clip, promoted.", "Look-alike", "What India calls a paperclip; the best Toggle number came from paperclips."),
 ("X06_tap_the_link", "Tap the link.", "Platform-native", "The chain's links, the web's links: the call to action is the joke."),
 ("X07_anatomy", "Anatomy of a show-off clasp", "Lo-fi", "Marker scribbles that name each part, with only what the listing says."),
 ("X08_goes_with", "Goes with:", "Platform-native", "A checklist note of Indian necklines, ending on a wink."),
 ("X09_checkerboard", "The clasp is the point.", "The checkerboard", "Four panels: line, worn, detail, price and promises. More time on the ad."),
 ("X10_hook_laga_do", "No more &lsquo;hook laga do&rsquo;.", "Problem, solved", "What everyone says to whoever is nearest, made unnecessary by a front clasp."),
]

def main():
    jpath, out = sys.argv[1], sys.argv[2]
    judge = json.load(open(jpath)) if os.path.exists(jpath) else {"ads": []}
    by = {a["key"]: a for a in judge.get("ads", [])}
    caps = {a["key"]: a["text"] for a in json.load(open(os.path.join(HERE, "..", "captions.json")))["ads"]}
    plan = json.load(open(os.path.join(HERE, "plan.json")))["ads"]
    cards = []
    for k, line, fam, why in META:
        j = by.get(k, {}); v = j.get("verdict", "")
        badge = {"pass": "Passes", "fix": "Passes after a fix", "fail": "Cut"}.get(v, "")
        cards.append(
            '<article class="ad" id="%s"><div class="pics"><img src="ads/%s_feed.jpg" alt="%s, Feed 4:5" loading="lazy" width="1080" height="1350">'
            '<img src="ads/%s_story.jpg" alt="%s, Story 9:16" loading="lazy" width="1080" height="1920"></div>'
            '<div class="meta"><div class="row"><span class="no">%s · %s</span><span class="score">%s</span></div><h3>%s</h3><p class="why">%s</p>'
            '%s<p class="cap"><span>Caption</span> %s</p></div></article>'
            % (k[:3].lower(), k, line, k, line, k[:3], esc(fam), ("%s · %.1f" % (badge, j["overall"])) if j.get("overall") is not None else "", line, esc(why),
               ('<p class="j"><span>Judge</span> %s</p>' % esc("; ".join(j.get("defects", [])) or "No defects named.")) if j else "", esc(caps.get(k))))
    picks = judge.get("budget_first", [])
    pick_html = "".join('<li><b>%s</b> (%s): %s</li>' % (esc(p.get("key")), esc(p.get("format")), esc(p.get("why"))) for p in picks)
    rows = "".join('<li><span class="n">%s</span> %s</li>' % (esc(a["no"]), esc(a["line"])) for a in plan)
    page = TEMPLATE % {"cards": "".join(cards), "picks": pick_html or "<li>The judge's picks appear here once it has scored the set.</li>", "plan": rows}
    os.makedirs(out, exist_ok=True); open(os.path.join(out, "index.html"), "w").write(page); print(os.path.join(out, "index.html"), len(page))

TEMPLATE = """<title>Toggle Ten</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500&family=Kalam:wght@700&display=swap">
<style>
/* A lookbook for ten hook tests: the clasp proof first (what was wrong, what is right), then each ad, then what waits. */
:root{--bg:#FBF8F3;--paper:#F3EDE4;--ink:#1A1614;--mute:#6E645E;--line:#E2D8CC;--gold:#9A6B2F;--ok:#2F5D50;--red:#B3362A;
 --display:"Cormorant Garamond",Georgia,"Times New Roman",serif;--body:"Jost","Helvetica Neue",Arial,sans-serif;--hand:"Kalam","Comic Sans MS",cursive}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#15110F;--paper:#1E1916;--ink:#F3EDE4;--mute:#A99D94;--line:#352C27;--gold:#D4A764;--ok:#7FB8A6;--red:#E98A7E;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#15110F;--paper:#1E1916;--ink:#F3EDE4;--mute:#A99D94;--line:#352C27;--gold:#D4A764;--ok:#7FB8A6;--red:#E98A7E;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:40px 72px}
h1,h2,h3{font-family:var(--display);font-weight:500;text-wrap:balance;margin:0}
h1{font-size:clamp(40px,6vw,64px);line-height:1.02;letter-spacing:-.01em}
h2{font-size:clamp(30px,4vw,42px);line-height:1.05}
.lede{max-width:62ch;color:var(--mute);margin:14px 0 0}
.eyebrow{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin:0 0 8px}
section{margin-top:64px} section>header{max-width:70ch}
.proof{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:22px}
.proof figure{margin:0;min-width:0} .proof img{display:block;width:100%%;height:auto;background:var(--line)}
.proof figcaption{font-size:13px;color:var(--mute);margin-top:8px} .proof b{color:var(--ink);font-weight:500}
.tag{font-size:11px;letter-spacing:.14em;text-transform:uppercase;padding:2px 8px;border:1px solid currentColor;margin-right:6px}
.tag.bad{color:var(--red)} .tag.good{color:var(--ok)}
.flags{margin:18px 0 0;padding-left:18px;max-width:80ch} .flags li{margin:6px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:28px;margin-top:26px}
.ad{min-width:0} .pics{display:grid;grid-template-columns:5fr 2.81fr;gap:8px;align-items:end}
.pics img{display:block;width:100%%;height:auto;background:var(--line)}
.meta{margin-top:12px} .row{display:flex;justify-content:space-between;align-items:baseline;gap:12px;border-top:1px solid var(--line);padding-top:8px}
.no{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)} .score{font-size:13px;color:var(--ok);font-weight:500;text-align:right}
h3{font-size:24px;line-height:1.12;margin-top:6px;font-style:italic}
.why{font-size:14px;margin:6px 0 0} .j,.cap{font-size:13px;color:var(--mute);margin:8px 0 0}
.j span,.cap span{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-right:6px}
.picks{margin:14px 0 0;padding-left:18px;max-width:80ch} .picks li{margin:6px 0}
.plan{columns:2 260px;margin:18px 0 0;padding:0;list-style:none} .plan li{break-inside:avoid;padding:6px 0;border-bottom:1px solid var(--line);font-family:var(--display);font-size:19px;font-style:italic}
.plan .n{font-family:var(--body);font-style:normal;font-size:12px;letter-spacing:.12em;color:var(--mute);margin-right:10px}
.hand{font-family:var(--hand);color:var(--red)}
footer{margin-top:72px;border-top:1px solid var(--line);padding-top:18px;font-size:13px;color:var(--mute);max-width:90ch}
</style>
<div class="wrap">
<p class="eyebrow">Naira · Toggle Link Chain · 4 Nov 2026</p>
<h1>Ten crazy hooks, one <span class="hand">checked</span> clasp</h1>
<p class="lede">Ten hook tests for the Toggle Link Chain, each on a format the research backs (lo-fi notes, platform-native posts, the clever line, the checkerboard), all built on photos whose clasp was checked part by part against the listing. An independent judge scored them; the ones it would not run are marked.</p>

<section id="proof"><header><p class="eyebrow">First, the toggle</p><h2>What was wrong, and what is right</h2>
<p class="lede">The real clasp: a thick spring-gate ring with a gate and a push-pin nub at three o'clock, and a short bar with one line of tiny clear stones through it. Several photos in use draw something else.</p></header>
<div class="proof">
<figure><img src="proof/real_clasp.jpg" alt="The clasp in the listing's worn photo, enlarged" loading="lazy"><figcaption><span class="tag good">Right</span><b>The listing's worn photo.</b> Gate, collars and push-pin on the ring; a straight single-row bar on a jump ring.</figcaption></figure>
<figure><img src="proof/live_product_photo.jpg" alt="The clasp in the generated worn photo on the product page" loading="lazy"><figcaption><span class="tag bad">Wrong</span><b>On the product page now</b> (third photo, added 21 Oct): a plain closed ring, no gate or push-pin, and a wide curved hoop of stones instead of the bar.</figcaption></figure>
<figure><img src="proof/live_ads.jpg" alt="The clasp in the five Toggle ads live on Meta" loading="lazy"><figcaption><span class="tag bad">Wrong</span><b>Four of the five live Toggle ads</b> (plate, fork, spool, Story): plain rings, or a hoop with black stones. The hook ad is closest. All five still say ₹1,099 and "anti-tarnish".</figcaption></figure>
</div>
<ul class="flags"><li>Nothing has been changed on Shopify or Meta. Replacing the product photo and pausing the four ads wait for the owner.</li>
<li>Of 19 earlier Toggle photos, 4 pass, 4 have small defects and 11 fail. These ten ads use only the 4 that pass.</li>
<li>One question for a physical piece: the cube listing photo shows the stone piece as a hoop; the worn and velvet photos and the description say bar.</li></ul>
</section>

<section id="ads"><header><p class="eyebrow">The ten</p><h2>Hook tests, Feed beside Story</h2>
<p class="lede">Five share one photo on purpose, so they test the hook alone. Every claim is on the product page today; the offer lives in the caption.</p></header>
<div class="grid">%(cards)s</div>
<p class="eyebrow" style="margin-top:34px">Where the judge would spend first</p><ul class="picks">%(picks)s</ul>
</section>

<section id="next"><header><p class="eyebrow">Next, with credits</p><h2>The fifteen with new photos</h2>
<p class="lede">Planned and independently judged, with shot briefs written; they need about 50 Higgsfield credits (1.71 left).</p></header>
<ul class="plan">%(plan)s</ul>
</section>
<footer>Prices are the live Shopify price on 4 November (₹1,199). Free insured shipping, the Naira gift box and the Buy 2 · 10%% / Buy 3 · 20%% offer applied in the bag are as the storefront states them. The metal is named gold tone. Research links are in the README.</footer>
</div>
"""

if __name__ == "__main__":
    main()
