"""plan.json + template.html -> site/index.html (the artifact page) and site/files.json (the publish map)."""
import json, base64, re, sys, html
from pathlib import Path
D = Path(sys.argv[1]); SITE = D / "site"; SITE.mkdir(exist_ok=True)
plan = json.load(open(D / "plan.json")); P = json.load(open(D / "products.json"))["products"]
REPO = Path("/home/user/naira-scroll")
LOGO = json.load(open(REPO / "creative/naira-bag/build/assets/naira-logo-vector.json"))
velista = base64.b64encode((REPO / "public/fonts/Velista.ttf").read_bytes()).decode()
nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", LOGO["flower"])]; xs, ys = nums[0::2], nums[1::2]
fvb = f"{min(xs)-6:.0f} {min(ys)-6:.0f} {max(xs)-min(xs)+12:.0f} {max(ys)-min(ys)+12:.0f}"

# compact library
lib = plan["library"]
for x in lib:
    if not isinstance(x["p"], str): x["p"] = (x["p"][0] if x["p"] else "cream")
def table(vals):
    seen = {}; out = []
    for v in vals:
        if v not in seen: seen[v] = len(out); out.append(v)
    return out, seen
kinds, ki = table([x["k"] for x in lib]); cats, ci = table([x["c"] for x in lib]); pals, pi = table([x["p"] for x in lib])
ars, ai = table([x["a"] for x in lib]); days, di = table([x["d"] for x in lib]); roles, ri = table([x["r"] for x in lib])
prods, pri = table([x["n"] for x in lib if x["n"]]); excl, ei = table([r for x in lib for r in x["x"]]); series, si = table([x["s"] for x in lib])
rows = [[x["id"], x["ti"], -1 if x["si"] is None else x["si"], -1 if x["mi"] is None else x["mi"], -1 if x["sti"] is None else x["sti"],
         ki[x["k"]], ci[x["c"]], pi[x["p"]], ai[x["a"]], di[x["d"]], pri[x["n"]] if x["n"] else -1, ri[x["r"]], [ei[r] for r in x["x"]], si[x["s"]]] for x in lib]
C = plan["counts"]; R = plan["roles"]
def n(k): return f"{R.get(k, 0):,}"
cnt_excl = {}
for x in lib:
    for r in x["x"]: cnt_excl[r.split(":")[0]] = cnt_excl.get(r.split(":")[0], 0) + 1

RULES = f"""
<h2>One row, one product, three ways</h2>
<p>Every row of three is one family of jewellery seen left to right as <b>the object</b> (a still life or a plinth shot), <b>worn</b> (on a person, for scale) and <b>the detail</b> (a macro, for the setting and the finish). The grid is read like a page, so the eye gets the thing, its size and its quality in one line. Rows one to four in a chapter are earrings, rings, necklaces and bracelets in rotation; the fifth row is the chapter's mixed hero row.</p>
<p class="q">The object. The scale. The finish. Then the next row.</p>
<h2>Six colour chapters, two weeks each</h2>
<ol>
{''.join(f"<li><b>{c['num']} {html.escape(c['name'])}</b> · {c['start']} to {c['end']} · <span class='it'>{html.escape(c['line'])}</span> {html.escape(c['about'])}</li>" for c in plan['chapters'])}
</ol>
<p>Each chapter is fifteen posts: seven singles, four carousels and four reels. The pinned row on top is evergreen and states the thesis: the index packshot carousel, one worn frame, one macro.</p>
<h2>Order and timing</h2>
<p>A chapter is published bottom-right to top-left, so the finished grid reads as designed with the newest row on top. Two posts on a chapter's first day (the 12:30 reel, then the 19:30 post), then one a day. Reels go up at 12:30 IST, posts at 19:30 IST. The season opens Monday 2 November 2026 with The Red Room, four days before Dhanteras, and closes on 24 January 2027.</p>
<h3>Reel recipes</h3>
<ul>
<li><b>The Index</b> · up to 30 packshots of one family, one frame per beat at 120 bpm, about 10 seconds. The piece stays centred; the plaster never moves. Metronomic audio, no vocals.</li>
<li><b>Worn</b> · 8 frames on a person, slow dissolves at 1.5 seconds each, about 12 seconds, end on the ear or the wrist. Soft piano, cut on the phrase.</li>
<li><b>Up close</b> · 8 to 10 macro frames, a 10 percent push-in over each, cut on the stone. Room tone with a quiet string pad, no beat.</li>
</ul>
<p>Frames and covers for all {len([t for t in plan['tiles'] if t['type']=='reel'])} reels are chosen in this plan; the video files still need cutting.</p>
<h3>Stories, three a day</h3>
<ul>
<li><b>09:00</b> a texture or still life frame with a poll, a question box or a slider.</li>
<li><b>13:00</b> a macro with a tap-through, a countdown or a site link.</li>
<li><b>21:00</b> a worn or packshot frame with the link sticker and the price.</li>
</ul>
<p>Festival days open with a plain greeting frame before the jewellery. Eight highlight covers are chosen so the chapters survive on the profile after their fortnight.</p>
<h2>Copy rules</h2>
<ul>
<li>No exclamation marks, anywhere.</li>
<li>The material line on every post: [ 18k gold coated · rhodium coated ]. Hypoallergenic on every post. Tarnish-free and waterproof only where it is true of the piece.</li>
<li>Price when the piece is live on nairaflore.com, <span class="it">waitlist open</span> when it is sold out. A named piece links to its product page; an unnamed frame links to its family collection.</li>
<li>Four brand tags on everything, two chapter tags on top. Alt text on every post.</li>
<li>Prices and stock were read from the live store on the day this plan was built and should be checked on the day of posting.</li>
</ul>
<h2>What stayed out, and where the rest went</h2>
<p>{C['library']:,} completed generations were reviewed, every one given a role. {C['plan_images']:,} are placed in the plan: {R.get('cover',0)} covers, {R.get('slide',0)} carousel slides, {R.get('reel',0)} reel frames, {R.get('story',0)} story frames and {R.get('highlight',0)} highlight covers. The rest are sorted, not lost: an <b>ads bank</b> of {n('ads')} finished 4:5 and 9:16 frames for paid, a <b>catalogue bank</b> of {n('catalogue')} packshots for the site, {n('variant')} near-duplicates of placed frames, {n('bank')} usable frames held for next season, and {n('excluded')} excluded with a reason each: {', '.join(f"{html.escape(k)} ({v})" for k, v in sorted(cnt_excl.items(), key=lambda kv: -kv[1]))}. Every image and its reason is in the Library tab.</p>
<h2>Open questions</h2>
<ul>
<li>Dates assume Dhanteras on 6 November and Diwali on 8 November 2026; confirm against the panchang you follow.</li>
<li>One model (the orange camisole series) carries most of the worn frames across chapters. Decide whether she is the house face for the season or whether the Sage and Lilac chapters should use the other sittings.</li>
<li>The Index reels need cutting; the Apricot index has 15 necklace packshots, the others 30.</li>
</ul>
"""

EDITS = f"""
<p class="q">The grid was built, looked at, and rebuilt three times. Each pass is recorded here with what it found and what it changed.</p>
<div class="edit"><div class="num">0</div><h3>First build</h3><p>The planner read each image's prompt to decide what it showed. It got the colour chapters right and the row logic wrong: seventeen of the thirty <span class="it">worn</span> tiles were plinth shots, four of the five in The Index. A text filter meant to drop images with rendered headlines matched the phrase <span class="it">No lettering, no watermark</span> in the briefs and threw out 1,159 clean frames.</p><div class="res"><span>excluded <b>1,727</b></span><span>worn tiles on a person <b>13 of 30</b></span></div></div>
<div class="edit"><div class="num">1</div><h3>Sorting the library</h3><p>A body-word classifier (ear, wrist, collarbone, her neck) decides what is worn. Background plates with no jewellery in the brief are out, 194 of them. The Red Room keyword list dropped <span class="it">night, dark, black</span>, which had let any dark frame in, and the palette now outweighs the keywords. The family order rotates every chapter so the six index reels cover all four families instead of starting on earrings each time.</p><div class="res"><span>excluded <b>793</b></span><span>placed <b>758</b></span><span>worn tiles on a person, by eye <b>26 of 30</b></span></div></div>
<div class="edit"><div class="num">2</div><h3>Reading the shot, not the brief</h3><p>The briefs describe their reference photographs too (<span class="it">ignore the hands… the model and her warm skin belong to those photographs alone</span>), and the classifier was reading those lines as a person in frame. It now reads only the paragraph that describes the shot. Dark saturated grounds keep their hue, so green velvet no longer counts as charcoal in the Red Room. Poster backgrounds and <span class="it">remove the necklace</span> plates are out, and a style veto keeps crushed cans and black nails off the grid.</p><div class="res"><span>excluded <b>1,179</b></span><span>placed <b>777</b></span><span>worn tiles on a person, by eye <b>25 of 30</b></span></div></div>
<div class="edit"><div class="num">3</div><h3>Pale hours and product trios</h3><p>The parser now handles briefs that open with the supplier note (<span class="it">IMAGE 1 is a supplier photo worn on a wrist</span>) and strips negations before it looks for a person, so <span class="it">no hands</span> no longer reads as hands. Brightness floors keep the pale chapters pale: The Index above 0.50, Lilac above 0.42. The object tile of each row prefers a product that also has a worn frame and a macro in the chapter's palette, so more rows read as one piece three ways. Handwritten notes join the text exclusion, highlight covers are made distinct, and three Lilac covers were vetoed by hand (a locker full of mixed pieces, a surgical tray, shattered glass). All 93 covers were then checked by eye.</p><div class="res"><span>excluded <b>{R.get('excluded',0):,}</b></span><span>placed <b>{C['plan_images']:,}</b></span><span>worn tiles on a person, by eye <b>30 of 30</b></span><span>object tiles that are objects <b>30 of 30</b></span></div></div>
<p>Built {plan['built']}. Rebuild from <code>creative/naira-feed/build/</code> in the repository: <code>tag.py</code>, <code>colors.py</code>, <code>quality.py</code>, <code>plan.py</code>, <code>sprites.py</code>, <code>site.py</code>.</p>
"""

data = {"season": plan["season"], "chapters": plan["chapters"], "events": plan["events"], "pinned": plan["pinned"], "tiles": plan["tiles"], "stories": plan["stories"],
        "highlights": plan["highlights"], "counts": C, "roles": R, "rules": RULES, "edits": EDITS,
        "lib": {"kinds": kinds, "cats": cats, "pals": pals, "ars": ars, "days": days, "roles": roles, "prods": prods, "excl": excl, "series": series, "rows": rows}}
blob = json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
tpl = (D / "tools/template.html").read_text()
out = tpl.replace("__DATA__", blob).replace("__VELISTA__", velista).replace("__LOGO_L__", LOGO["letters"]).replace("__LOGO_F__", LOGO["flower"]).replace("__FLOWER_VB__", fvb)
(SITE / "index.html").write_text(out)
files = sorted(str(p.relative_to(SITE)) for p in SITE.rglob("*.webp"))
json.dump(files, open(SITE / "files.json", "w"))
print("index.html", round(len(out.encode()) / 1e6, 2), "MB; data", round(len(blob) / 1e6, 2), "MB;", len(files), "sprite files,", round(sum((SITE / f).stat().st_size for f in files) / 1e6, 1), "MB")
