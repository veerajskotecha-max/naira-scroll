"""Builds the contact sheets, the Ads Manager copy sheet, the README and the review page for the 14 angle tests."""
import base64, csv, html, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from copy_data import SETS, CTA_GUIDE, TRUST, link, files, ad_name

T = Path(__file__).resolve().parent.parent
S = T.parent
OUT, PAGE = T / 'out', T / 'page'
REPO = Path('/home/user/naira-scroll/creative/naira-ab-tests')
E = lambda s: html.escape(str(s), quote=True)
FONT = '/usr/share/fonts/opentype/inter/Inter-{}.otf'
f = lambda w, s: ImageFont.truetype(FONT.format(w), s)


# ------------------------------------------------------------------ contact sheets
def sheet(st, cw, ch, title, sub):
    pad, gap, lab, head = 44, 26, 96, 150
    W = pad * 2 + cw * 4 + gap * 3; H = head + (ch + lab) * 2 + gap + pad
    im = Image.new('RGB', (W, H), '#F3ECE2'); d = ImageDraw.Draw(im)
    d.text((pad, 40), title, font=f('SemiBold', 40), fill='#1F1A14'); d.text((pad, 96), sub, font=f('Regular', 25), fill='#6A6157')
    for k, ad in enumerate(st['ads']):
        x = pad + (k % 4) * (cw + gap); y = head + (k // 4) * (ch + lab + gap)
        im.paste(Image.open(OUT / files(st, ad)).convert('RGB').resize((cw, ch), Image.LANCZOS), (x, y))
        d.rectangle([x, y, x + cw - 1, y + ch - 1], outline='#D8CCBB')
        d.text((x, y + ch + 14), f"{ad['id']} · {ad['angle']}", font=f('SemiBold', 26), fill='#1F1A14')
        d.text((x, y + ch + 52), f"Button: {ad['cta']}", font=f('Regular', 22), fill='#6A6157')
    # eighth cell: the benchmark to beat
    x = pad + 3 * (cw + gap); y = head + ch + lab + gap
    d.rectangle([x, y, x + cw - 1, y + ch - 1], fill='#FFFDF9', outline='#D8CCBB')
    o = st['original']; ty = y + 30
    d.text((x + 28, ty), 'THE CONTROL', font=f('SemiBold', 20), fill='#6A6157'); ty += 40
    for line in wrap(o['name'], 26):
        d.text((x + 28, ty), line, font=f('SemiBold', 25), fill='#1F1A14'); ty += 34
    d.text((x + 28, ty + 4), o['when'].split(' · ')[0], font=f('Regular', 21), fill='#6A6157'); ty += 56
    colw = (cw - 56) // 2
    for n, (v, k) in enumerate(o['stats']):
        cx = x + 28 + (n % 2) * colw; cy = ty + (n // 2) * 92
        d.text((cx, cy), v, font=f('SemiBold', 31), fill='#1F1A14')
        for j, line in enumerate(wrap(k, 15)[:2]):
            d.text((cx, cy + 40 + j * 22), line, font=f('Regular', 18), fill='#6A6157')
    d.text((x + 28, y + ch - 70), 'Duplicate the original into the', font=f('Regular', 20), fill='#6A6157')
    d.text((x + 28, y + ch - 44), 'test ad set as the benchmark.', font=f('Regular', 20), fill='#6A6157')
    return im


def wrap(t, n):
    out, cur = [], ''
    for w in t.split():
        if len(cur) + len(w) + 1 > n: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    return out + [cur]


# ------------------------------------------------------------------ README + CSV
def write_docs(dst):
    rows = [['ad_name', 'image_file', 'placement', 'primary_text', 'headline', 'description', 'cta_button', 'website_url']]
    md = ['# Same photo, new angle: Naira A/B angle tests', '',
          'Fourteen Meta ads built on the two original winning photos. Seven challengers each for **Sweet On You** (Prism Rivière, Feed) and the **red Woven** story (Woven Gold Hoops, Stories). '
          'The photo is held constant inside each set; every ad changes the angle: the hook, the edit and the CTA button.', '',
          '## How the test works', '',
          '1. **Screen, days 1 to 6.** New Sales campaign, budget at ad-set level. Ad set "AB · Prism sugar": Instagram Feed only, ₹800/day. Ad set "AB · Woven red": Instagram Stories only, ₹1,200/day. Each holds the original ad plus its seven challengers. Audience as the live ads: women 18–65, all India, Advantage+ audience on.',
          '2. **Read, day 6.** Judge only ads with 1,000+ impressions. Shortlist a challenger when its link CTR beats the original by 30% or more and its add-to-cart rate (add-to-carts ÷ landing-page views) is no lower. Ads Meta barely served are untested, not losers.',
          '3. **Confirm, days 7 to 13.** Ads Manager A/B test: the original against the best challenger (two if two cleared the bar), equal split, 7 days, key metric cost per landing-page view. Accept a winner only at 80% confidence or more; otherwise the original stays.',
          '4. **Scale, then iterate.** Move the winner into the Winners campaign and raise its budget about 20% every 2 to 3 days. Then change one thing at a time on it: a reworded hook, then the button.', '',
          'Rules: turn off every Advantage+ creative enhancement on every ad; launch both ad sets together; no edits for 6 days. Feed impressions in this account cost about ₹437 per thousand and Stories about ₹805, which is why the Stories set gets more budget.', '',
          '## CTA buttons', '', '| Button | Used on | Why |', '|---|---|---|']
    md += [f'| {b} | {u} | {w} |' for b, u, w in CTA_GUIDE]
    for st in SETS:
        o = st['original']
        md += ['', f"## {st['key']} · {st['name']}", '',
               f"{st['piece']}, {st['price']}, {st['stock']} in stock. {st['fmt']}. {st['placement']}. Photo: {st['photo']}.", '',
               f"Control: **{o['name']}** ({o['when']}): " + ', '.join(f'{v} {k}' for v, k in o['stats']) + ' (Meta export of 4 Nov).', '',
               '| Ad | Angle | Hook on the image | Button | File |', '|---|---|---|---|---|']
        md += [f"| {a['id']} | {a['angle']} | {a['hook']} | {a['cta']} | `ads/{files(st, a)}` |" for a in st['ads']]
        for a in st['ads']:
            md += ['', f"### {a['id']} · {a['angle']}", '', f"*{a['why']}*", '',
                   f"- **Primary text:** {a['primary']}", f"- **Headline:** {a['headline']}", f'- **Description:** {TRUST}',
                   f"- **Button:** {a['cta']}", f"- **Website URL:** {link(st, a)}", f"- **Ad name:** {ad_name(st, a)}"]
            rows.append([ad_name(st, a), files(st, a), 'Instagram Feed' if st['key'] == 'P' else 'Instagram Stories', a['primary'], a['headline'], TRUST, a['cta'], link(st, a)])
    md += ['', '## Before launch', '',
           '- "WOVEN, not cast." is unverified: the product page describes a braided rope of gold-tone strands, not how it is made. The live W1 ad uses the line; none of the seven new Woven ads does.',
           '- BUY2 expired on 7 Nov. NAIRA10 (10% off any order, no minimum), BUY3 (20% off 3+) and BUY4 (30% off 4+) are active. The Guest List and Naira Ten primary text still mention BUY2.',
           '- The two photos were matched from the Naira image library by date and prompt; the Meta connector was signed out, so the original ad files could not be pulled for a pixel check.',
           '', 'Built 11 November 2026 from the live nairaflore.com product pages and the Shopify discount list. Nothing was created or changed in Meta.']
    (dst / 'README.md').write_text('\n'.join(md) + '\n')
    (dst / 'data').mkdir(exist_ok=True)
    with open(dst / 'data' / 'ads-manager-copy.csv', 'w', newline='', encoding='utf-8-sig') as fh:
        csv.writer(fh).writerows(rows)


# ------------------------------------------------------------------ page
def page():
    velista = base64.b64encode((S / 'labels' / 'fonts' / 'Velista.ttf').read_bytes()).decode()
    def card(st, a):
        i = a['id'].lower(); kind = 'feed' if st['key'] == 'P' else 'story'
        w, h = (1080, 1350) if kind == 'feed' else (1080, 1920)
        return f"""
<article class='ad' id='{i}'>
  <figure class='shot {kind}'><img src='ads/{files(st, a)}' alt='{E(a['id'])}: {E(a['hook'])}' width='{w}' height='{h}'></figure>
  <div class='body'>
    <p class='meta'><span class='id'>{a['id']}</span><span class='angle'>{E(a['angle'])}</span><span class='btn'>{E(a['cta'])}</span></p>
    <h3>{E(a['hook'])}</h3>
    <p class='why'>{E(a['why'])}</p>
    <dl>
      <dt>Primary text</dt><dd><p id='{i}-primary'>{E(a['primary'])}</p><button type='button' data-copy='{i}-primary'>Copy</button></dd>
      <dt>Headline</dt><dd>{E(a['headline'])}</dd>
      <dt>Description</dt><dd>{E(TRUST)}</dd>
      <dt>Button</dt><dd>{E(a['cta'])}</dd>
      <dt>Website URL</dt><dd><code id='{i}-url'>{E(link(st, a))}</code><button type='button' data-copy='{i}-url'>Copy</button></dd>
      <dt>Ad name</dt><dd><code>{E(ad_name(st, a))}</code></dd>
    </dl>
  </div>
</article>"""

    def bench(st):
        o = st['original']
        stats = ''.join(f"<div><b>{E(v)}</b><span>{E(k)}</span></div>" for v, k in o['stats'])
        thumbs = ''.join(f"<a href='#{a['id'].lower()}' class='th {'feed' if st['key'] == 'P' else 'story'}'><img src='ads/{files(st, a)}' alt='' width='540' height='{675 if st['key'] == 'P' else 960}'><span>{a['id']} · {E(a['cta'])}</span></a>" for a in st['ads'])
        return f"""
<section class='set' id='set-{st['key'].lower()}'>
  <header class='seth'>
    <p class='meta'><span class='chip c-{st['token']}'><i></i>{st['chip']}</span><span class='mono'>{E(st['fmt'])}</span></p>
    <h2>{E(st['name'])}</h2>
    <p class='sub'><b>{E(st['piece'])}</b> · {E(st['price'])} · {st['stock']} in stock · {E(st['placement'])}</p>
    <p class='sub'>{E(st['photo'])}</p>
  </header>
  <div class='control'>
    <p class='eyebrow'>The control to beat · {E(o['name'])}</p>
    <p class='when'>{E(o['when'])} · Meta export of 4 Nov</p>
    <div class='stats'>{stats}</div>
  </div>
  <nav class='strip' aria-label='{E(st['piece'])} challengers'>{thumbs}</nav>
  {''.join(card(st, a) for a in st['ads'])}
</section>"""

    steps = [
        ('Screen', 'Days 1 to 6', 'New Sales campaign with budget at ad-set level. <b>AB · Prism sugar</b>: Instagram Feed, ₹800/day. <b>AB · Woven red</b>: Instagram Stories, ₹1,200/day. Each holds the original plus its seven challengers, with the live audience: women 18–65, all India, Advantage+ audience on.'),
        ('Read', 'Day 6', 'Judge only ads with 1,000+ impressions. Shortlist a challenger when its link CTR beats the original by 30% or more and its add-to-cart rate is no lower. Ads Meta barely served are untested, not losers.'),
        ('Confirm', 'Days 7 to 13', 'Ads Manager A/B test: the original against the best challenger, or two if two cleared the bar. Equal split, 7 days, key metric cost per landing-page view. Accept a winner at 80% confidence or more; otherwise the original stays.'),
        ('Scale, then iterate', 'Day 14 on', 'Move the winner into the Winners campaign and raise its budget about 20% every 2 to 3 days. Then change one thing at a time on it: a reworded hook first, then the button.'),
    ]
    step_html = ''.join(f"<li><span class='n'>{k}</span><div><h3>{E(t)}</h3><p class='when'>{E(w)}</p><p>{b}</p></div></li>" for k, (t, w, b) in enumerate(steps, 1))
    cta_rows = ''.join(f"<tr><th scope='row'>{E(b)}</th><td class='mono'>{E(u)}</td><td>{E(w)}</td></tr>" for b, u, w in CTA_GUIDE)
    body = f"""<title>Same Photo, New Angle</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* layout: a test kit. Thesis, the four-step method, then one bench per photo: the control to beat and seven numbered challengers with their Ads Manager fields */
@font-face {{ font-family:'Velista'; src:url(data:font/truetype;base64,{velista}) format('truetype'); font-display:swap }}
:root {{ --paper:#F6F1E9; --card:#FFFDF9; --ink:#1F1A14; --mute:#6A6157; --line:#E3DACD; --code:#EFE7DB; --accent:#8E1238;
  --rani:#C2185B; --haldi:#F2B705; --on-dark:#FBF5EA; --on-haldi:#1F1A14;
  --display:'Velista','Times New Roman',serif; --sans:'Jost','Helvetica Neue',Arial,sans-serif; --mono:'IBM Plex Mono',ui-monospace,Menlo,monospace }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --paper:#15120F; --card:#1D1915; --ink:#F2EBE1; --mute:#B2A695; --line:#3A322A; --code:#26211C; --accent:#F08AAE; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --paper:#15120F; --card:#1D1915; --ink:#F2EBE1; --mute:#B2A695; --line:#3A322A; --code:#26211C; --accent:#F08AAE; color-scheme:dark }}
* {{ box-sizing:border-box }}
body {{ margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-weight:300; font-size:17px; line-height:1.55 }}
.wrap {{ max-width:1180px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:0 }}
h1, h2, h3 {{ font-family:var(--display); font-weight:400; margin:0; text-wrap:balance; letter-spacing:.01em }}
h1 {{ font-size:clamp(54px, 9.5vw, 124px); line-height:.92 }}
h2 {{ font-size:clamp(30px, 4.2vw, 50px); line-height:1.02 }}
h3 {{ font-size:clamp(24px, 2.6vw, 32px); line-height:1.08 }}
p {{ margin:0 }} b {{ font-weight:500 }}
.mono {{ font-family:var(--mono); font-size:13px; letter-spacing:.03em }}
.eyebrow {{ font-family:var(--mono); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--mute) }}
header.top {{ padding-block:54px 30px; display:grid; gap:22px }}
.lede {{ font-size:clamp(19px, 2vw, 22px); line-height:1.45; max-width:44em }}
.facts {{ display:flex; flex-wrap:wrap; gap:12px 36px; padding-block:18px; border-top:1px solid var(--line); border-bottom:1px solid var(--line) }}
.facts div, .stats div {{ display:grid }}
.facts b, .stats b {{ font-family:var(--display); font-weight:400; font-size:34px; line-height:1; font-variant-numeric:tabular-nums }}
.facts span, .stats span {{ font-family:var(--mono); font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--mute); margin-top:6px }}
section {{ padding-block:44px; border-top:1px solid var(--line) }}
.steps {{ list-style:none; margin:24px 0 0; padding:0; display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:26px }}
.steps li {{ display:flex; gap:14px; min-width:0 }}
.steps .n {{ font-family:var(--display); font-size:58px; line-height:.8; color:var(--accent) }}
.steps h3 {{ font-size:26px }}
.when {{ font-family:var(--mono); font-size:12px; letter-spacing:.08em; color:var(--mute); margin:4px 0 8px }}
.twocol {{ display:grid; grid-template-columns:minmax(0, 1fr) minmax(0, 1fr); gap:30px; margin-top:34px }}
.note {{ background:var(--card); border:1px solid var(--line); padding:18px 22px; display:grid; gap:8px }}
.note h3 {{ font-size:24px }}
ul.rules {{ margin:0; padding-left:18px; display:grid; gap:6px }}
.tbl {{ overflow-x:auto; margin-top:14px }}
table {{ border-collapse:collapse; width:100%; min-width:560px }}
th, td {{ text-align:left; vertical-align:top; padding:10px 12px 10px 0; border-top:1px solid var(--line) }}
th {{ font-weight:500; white-space:nowrap }}
.chip {{ display:inline-flex; align-items:center; gap:8px; font-family:var(--sans); font-weight:500; font-size:12px; letter-spacing:.2em; padding:6px 11px; border-radius:0 0 9px 9px; white-space:nowrap }}
.chip i {{ width:9px; height:9px; border-radius:50%; border:1.6px solid currentColor }}
.c-rani {{ background:var(--rani); color:var(--on-dark) }} .c-haldi {{ background:var(--haldi); color:var(--on-haldi) }}
.seth {{ display:grid; gap:10px }}
.meta {{ display:flex; flex-wrap:wrap; align-items:center; gap:8px 14px }}
.sub {{ color:var(--mute); max-width:70ch }} .sub b {{ color:var(--ink) }}
.control {{ margin-top:22px; padding:18px 22px; background:var(--card); border:1px solid var(--line); display:grid; gap:4px }}
.stats {{ display:flex; flex-wrap:wrap; gap:12px 30px; margin-top:10px }}
.stats b {{ font-size:28px }}
.strip {{ display:grid; grid-template-columns:repeat(7, minmax(0, 1fr)); gap:10px; margin-top:24px }}
.th {{ display:grid; gap:6px; text-decoration:none; color:inherit; min-width:0 }}
.th img {{ width:100%; height:auto; display:block; border:1px solid var(--line) }}
.th span {{ font-family:var(--mono); font-size:11px; color:var(--mute); letter-spacing:.04em }}
.th:hover img, .th:focus-visible img {{ outline:2px solid var(--ink); outline-offset:2px }}
.ad {{ display:grid; grid-template-columns:minmax(0, 340px) minmax(0, 1fr); gap:30px; padding-block:34px; border-top:1px solid var(--line); margin-top:30px }}
.ad + .ad {{ margin-top:0 }}
.shot {{ margin:0 }} .shot img {{ width:100%; height:auto; display:block; border:1px solid var(--line) }}
.shot.story {{ max-width:280px }}
.body {{ display:grid; gap:12px; align-content:start; min-width:0 }}
.id {{ font-family:var(--display); font-size:30px; line-height:1 }}
.angle {{ font-family:var(--mono); font-size:13px; letter-spacing:.06em }}
.btn {{ font-family:var(--sans); font-weight:500; font-size:12px; letter-spacing:.16em; text-transform:uppercase; border:1.5px solid var(--ink); padding:5px 10px; border-radius:999px }}
.why {{ color:var(--mute); max-width:62ch }}
dl {{ display:grid; grid-template-columns:120px minmax(0, 1fr); gap:10px 16px; margin:8px 0 0; background:var(--card); border:1px solid var(--line); padding:16px 18px }}
dt {{ font-family:var(--mono); font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--mute); padding-top:4px }}
dd {{ margin:0; min-width:0; display:grid; gap:8px; justify-items:start }}
code {{ font-family:var(--mono); font-size:12px; background:var(--code); padding:2px 6px; word-break:break-all }}
button[data-copy] {{ font:500 12px/1 var(--sans); letter-spacing:.14em; text-transform:uppercase; color:var(--ink); background:transparent; border:1.5px solid var(--ink); border-radius:999px; padding:7px 12px; cursor:pointer }}
button[data-copy]:hover {{ background:var(--ink); color:var(--paper) }}
button[data-copy]:focus-visible, a:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px }}
.flags {{ margin:16px 0 0; padding-left:18px; display:grid; gap:10px; max-width:76ch }}
footer {{ padding-block:36px 60px; color:var(--mute); font-size:14px; border-top:1px solid var(--line) }}
@media (max-width:900px) {{ .twocol {{ grid-template-columns:1fr }} .strip {{ grid-template-columns:repeat(4, minmax(0, 1fr)) }} }}
@media (max-width:640px) {{ .ad {{ grid-template-columns:1fr }} .shot.feed {{ max-width:420px }} dl {{ grid-template-columns:1fr }} .strip {{ grid-template-columns:repeat(3, minmax(0, 1fr)) }} }}
@media (prefers-reduced-motion: no-preference) {{ html {{ scroll-behavior:smooth }} }}
</style>

<div class='wrap'>
<header class='top'>
  <p class='eyebrow'>Naira · Meta A/B test kit · 11 November 2026</p>
  <h1>SAME PHOTO.<br>NEW ANGLE.</h1>
  <p class='lede'>Sweet On You and the red Woven story already won. Each now gets seven challengers built on its exact photo. The photo stays fixed and every ad changes the angle: the words, the edit and the button. When one wins, you know the angle did it.</p>
  <div class='facts'>
    <div><b>14</b><span>ads</span></div><div><b>2</b><span>winning photos</span></div><div><b>5</b><span>CTA buttons</span></div>
    <div><b>₹2,000</b><span>per day, round 1</span></div><div><b>13</b><span>days to a confirmed winner</span></div>
  </div>
</header>

<section id='plan'>
  <h2>How the test works</h2>
  <ol class='steps'>{step_html}</ol>
  <div class='twocol'>
    <div class='note'>
      <h3>Hooks or graphics?</h3>
      <p>In a static ad they are the same thing: the words on the image and the picture are read in the same second. So round 1 tests whole angles, each a hook with its own edit and button. Once an angle wins, change one thing at a time, because a test that changes two things cannot tell you which one worked.</p>
      <p>At about 2.5% link CTR, 1,000 impressions brings roughly 25 clicks. That is enough to see a big difference and not a small one, which is why the bar is 30% and why round 2 confirms it.</p>
    </div>
    <div class='note'>
      <h3>Rules for both rounds</h3>
      <ul class='rules'>
        <li>Turn off every Advantage+ creative enhancement on every ad, so Meta cannot rewrite the angle.</li>
        <li>Duplicate each original into its test ad set as the control and keep the live original running.</li>
        <li>Launch both ad sets at the same moment and edit nothing for 6 days. Any edit restarts learning.</li>
        <li>Feed impressions here cost about ₹437 per thousand and Stories about ₹805, so the Stories set gets the bigger budget.</li>
      </ul>
    </div>
  </div>
  <h3 style='margin-top:34px'>Which button, and why</h3>
  <div class='tbl'><table><thead><tr><th scope='col'>Button</th><th scope='col'>Used on</th><th scope='col'>Why</th></tr></thead><tbody>{cta_rows}</tbody></table></div>
</section>
{''.join(bench(st) for st in SETS)}
<section id='flags'>
  <h2>Before you launch</h2>
  <ul class='flags'>
    <li><b>"WOVEN, not cast." is unverified.</b> The product page describes a braided rope of gold-tone strands, not how it is made. The live W1 ad uses the line; none of the seven new Woven ads does. W3 shows the braid instead of claiming it.</li>
    <li><b>BUY2 expired on 7 November.</b> NAIRA10 (10% off any order, no minimum), BUY3 (20% off 3 or more) and BUY4 (30% off 4 or more) are active. The Guest List and Naira Ten primary text still mention BUY2, so swap that line or reactivate the code before those ads run.</li>
    <li><b>The photos were matched from the Naira image library</b> by date and prompt: 2ebe51f1 (9 Aug) for Sweet On You and 141d0fbd (6 Aug) for the red Woven ad. The Meta connector was signed out, so the original ad files could not be pulled for a pixel check, and the numbers above are from the 4 November export.</li>
  </ul>
</section>
<footer>Built 11 November 2026 from the live nairaflore.com product pages, the Shopify discount list and the Naira image library. Files and scripts are in creative/naira-ab-tests in the naira-scroll repository. Nothing was created or changed in Meta.</footer>
</div>
<script>
document.addEventListener('click', function (e) {{
  var b = e.target.closest('button[data-copy]'); if (!b) return;
  var el = document.getElementById(b.dataset.copy), text = el.innerText;
  function done(ok) {{ b.textContent = ok ? 'Copied' : 'Selected'; setTimeout(function () {{ b.textContent = 'Copy'; }}, 1600); }}
  function select() {{ var r = document.createRange(); r.selectNodeContents(el); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }}
  try {{ navigator.clipboard.writeText(text).then(function () {{ done(true); }}, function () {{ select(); done(false); }}); }}
  catch (err) {{ select(); done(false); }}
}});
</script>
"""
    PAGE.mkdir(exist_ok=True); (PAGE / 'ads').mkdir(exist_ok=True)
    for st in SETS:
        for a in st['ads']:
            shutil.copy(OUT / files(st, a), PAGE / 'ads' / files(st, a))
    (PAGE / 'index.html').write_text(body)
    print('page', len(body) // 1000, 'KB')


if __name__ == '__main__':
    (T / 'sheets').mkdir(exist_ok=True)
    sheet(SETS[0], 540, 675, 'Prism Rivière · the Sweet On You photo · 7 angles', 'Feed 4:5 · photo fixed, each ad changes the hook, the edit and the button').save(T / 'sheets' / 'sheet_prism_sugar_feed.jpg', quality=90)
    sheet(SETS[1], 405, 720, 'Woven Gold Hoops · the red Woven photo · 7 angles', 'Story 9:16 · photo fixed, each ad changes the hook, the edit and the button').save(T / 'sheets' / 'sheet_woven_red_story.jpg', quality=90)
    page()
    # repo folder
    if REPO.exists(): shutil.rmtree(REPO)
    for sub in ['ads', 'sheets', 'build', 'sources', 'data']: (REPO / sub).mkdir(parents=True, exist_ok=True)
    for st in SETS:
        for a in st['ads']: shutil.copy(OUT / files(st, a), REPO / 'ads' / files(st, a))
    for p in (T / 'sheets').glob('*.jpg'): shutil.copy(p, REPO / 'sheets' / p.name)
    for p in ['prep.py', 'ads.py', 'copy_data.py', 'deliver.py', 'kit.py']: shutil.copy(T / 'build' / p, REPO / 'build' / p)
    Image.open(T / 'img' / 'src_sugar.png').convert('RGB').save(REPO / 'sources' / '2ebe51f1_prism-riviere_sugared-sweets.jpg', quality=90)
    Image.open(T / 'img' / 'src_red.png').convert('RGB').save(REPO / 'sources' / '141d0fbd_woven-gold-hoops_oxblood-dome.jpg', quality=90)
    write_docs(REPO)
    print('repo folder ready')
