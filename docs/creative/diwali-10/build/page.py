# Diwali 10 (25 Oct 2026): the review page and README.md, both from notes.py, manifest.json, ledger.json and meta.csv.
# The page shows every ad (Feed, Story, Story with no text), the winners it copies, the thinking, the Meta copy and a Keep / Rework
# verdict per ad, saved to the artifact's shared database (collection "verdicts", one document per ad number).
# Images go to the page at web size (Feed 720x900, Story 540x960) with a link to the full 1080 file.
# Usage: page.py -> <scratchpad>/diwali10/artifact/ (index.html, web/, full/, win/, logo.png) and ../README.md
import html, json, os, shutil, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); CREATIVE = os.path.dirname(ROOT)
sys.path.insert(0, HERE); sys.path.insert(0, f"{CREATIVE}/finished-ads")
import notes as N
import build_ads as B

ART, REF = f"{B.SPB}/diwali10/artifact", f"{B.SPB}/diwali10/ref"
E = lambda s: html.escape(str(s), quote=True)
WIN = {w["id"]: w for w in N.WINNERS + N.REELS}

def pct(x): return f"{x:.2f}%"
def num(x): return f"{x:,}"

def images(M):
    """web-size copies for the page, the full files beside them, winner thumbnails and the wordmark"""
    for d in ("web", "full", "win"): os.makedirs(f"{ART}/{d}", exist_ok=True)
    for m in M:
        for fmt in ("feed", "story") + (() if m["variant_of"] else ("story-clean",)):
            name = f"{m['base']}-{fmt}.jpg"; src = f"{ROOT}/ads/{name}"
            shutil.copyfile(src, f"{ART}/full/{name}")
            size = (720, 900) if fmt == "feed" else (540, 960)
            Image.open(src).convert("RGB").resize(size, Image.LANCZOS).save(f"{ART}/web/{name}", quality=82, optimize=True, progressive=True)
    for w in N.WINNERS:
        if w["img"]:
            im = Image.open(f"{REF}/{w['img']}").convert("RGB"); h = round(im.height * 240 / im.width)
            im.resize((240, h), Image.LANCZOS).save(f"{ART}/win/{w['img']}", quality=80, optimize=True, progressive=True)
    a = Image.open(f"{B.BRAND}/logo_ink.png").convert("RGBA").getchannel("A")   # the wordmark in cream, for the night band
    logo = Image.new("RGBA", a.size, (243, 231, 207, 0)); logo.putalpha(a)
    logo.resize((600, round(a.height * 600 / a.width)), Image.LANCZOS).save(f"{ART}/logo.png", optimize=True)

def shot(m, fmt, cap):
    name = f"{m['base']}-{fmt}.jpg"; w, h = (720, 900) if fmt == "feed" else (540, 960)
    alt = f"{cap} for ad {m['n']}" + ("" if fmt == "story-clean" else f": “{m['line']}”")
    return (f'<figure class="{ "f" if fmt == "feed" else "s"}"><a href="full/{name}" target="_blank" rel="noopener">'
            f'<img src="web/{name}" width="{w}" height="{h}" alt="{E(alt)}" loading="lazy"></a><figcaption>{E(cap)}</figcaption></figure>')

def chip(wid):
    w = WIN[wid]
    if w.get("img"): img = f'<img src="win/{w["img"]}" alt="" loading="lazy">'
    else: img = '<span class="noimg">' + ("Reel" if wid.startswith("reel") else "Carousel") + "</span>"
    sales = f" · {w['sales']} sales" if w.get("sales", 0) > 1 else (" · 1 sale" if w.get("sales") == 1 else "")
    line, place = (w["caption"], f"{w['place']} with no text, line in the caption") if w.get("caption") else (w["line"], w.get("place", "Reel"))
    return (f'<li>{img}<span><i class="sl">{E(line)}</i><small>{E(place)} · {pct(w["ctr"])} CTR · '
            f'{pct(w["octr"])} outbound{sales}</small></span></li>')

def ad_card(m, V):
    n, a = m["n"], N.ADS[m["n"]]; score = N.SCORES[n]
    var = f" · {m['variant']}" if m.get("variant") else ""
    flights = E(m["flight"])
    killed = "".join(f'<li><i class="sl">{E(l)}</i> {E(r)}</li>' for l, r in a["killed"]) or ""
    killed_block = (f'<section><h4>Lines it beat</h4><ul class="killed">{killed}</ul></section>' if killed else
                    f'<section><h4>Kept from draft one</h4><p>{E(a["kept"])}</p></section>')
    extras = ""
    if a.get("alt"): extras += f'<p class="aside"><b>Test against it:</b> <i class="sl">{E(a["alt"])}</i></p>'
    if a.get("extra"): extras += f'<p class="aside">{E(a["extra"])}</p>'
    regional = ""
    if V:
        regional = ('<div class="regional"><h4>Regional wordings, same photograph</h4><p>' + E(a["regional"]) + '</p><div class="shots small">' +
                    "".join(shot(v, "feed", f"Feed · {v['line'].split('.')[0]}") + shot(v, "story", f"Story · {v['line'].split('.')[0]}")
                            for v in V) + '</div></div>')
    flags = "".join(f"<li>{E(f)}</li>" for f in a["flags"])
    flags = f'<ul class="flags">{flags}</ul>' if flags else ""
    pid = f"pt-{n}"
    return f'''
<article class="ad" id="ad-{n}" data-n="{n}">
  <header class="adhead">
    <span class="num">{n}</span>
    <div class="adtitle">
      <h3 class="line">{E(m["line"])}</h3>
      <p class="admeta">{E(m["title"])}{E(var)} · {E(m["price"])} · <b>{m["stock"]} in stock</b> · {E(m["adset"])} · {flights}</p>
    </div>
    <span class="score" title="My score out of 10 for the finished ad"><b>{score:.1f}</b><small>of 10</small></span>
  </header>
  <div class="shots">{shot(m, "feed", "Feed 4:5")}{shot(m, "story", "Story 9:16")}{shot(m, "story-clean", "Story, no text")}</div>
  {regional}
  <div class="why">
    <div class="col">
      <section><h4>The Diwali truth</h4><p>{E(a["truth"])}</p><p class="where">{E(a["where"])}</p></section>
      <section><h4>The picture</h4><p>{E(a["picture"])}</p></section>
      <section><h4>Why the line works</h4><p>{E(a["turn"])}</p>{extras}</section>
    </div>
    <div class="col">
      <section><h4>Built on</h4><ul class="built">{"".join(chip(w) for w in a["built"])}</ul><p>{E(a["built_note"])}</p></section>
      {killed_block}
      <section class="next"><h4>What it changed for the next ad</h4><p>{E(a["next"])}</p></section>
    </div>
  </div>
  <div class="shoot"><p><b>Shoot.</b> {E(a["shoot"])}</p>{flags}</div>
  <details class="copy">
    <summary>Copy for Meta</summary>
    <div class="copygrid">
      <div class="cp"><span class="lbl">Primary text</span><div class="txt pre" id="{pid}">{E(m["primary_text"])}</div>
        <button type="button" class="cbtn" data-copy="{pid}">Copy</button></div>
      <div class="cp"><span class="lbl">Headline</span><div class="txt" id="hl-{n}">{E(m["headline"])}</div>
        <button type="button" class="cbtn" data-copy="hl-{n}">Copy</button></div>
      <div class="cp"><span class="lbl">Link · Shop now</span><div class="txt url" id="url-{n}">{E(m["url"])}</div>
        <button type="button" class="cbtn" data-copy="url-{n}">Copy</button></div>
    </div>
  </details>
  <form class="verdict" data-n="{n}" onsubmit="return false">
    <div class="seg" role="group" aria-label="Verdict for ad {n}">
      <button type="button" data-v="keep" aria-pressed="false">Keep</button>
      <button type="button" data-v="rework" aria-pressed="false">Rework</button>
    </div>
    <label class="note"><span class="lbl">Note</span><textarea id="note-{n}" rows="2" placeholder="What to change, or why it works"></textarea></label>
    <span class="saved" id="saved-{n}" aria-live="polite"></span>
  </form>
</article>'''

def winners_html():
    rows = []
    for i, w in enumerate(N.WINNERS, 1):
        img = f'<img src="win/{w["img"]}" alt="" loading="lazy">' if w["img"] else '<span class="noimg">Carousel</span>'
        line = f'<i class="sl">{E(w["line"])}</i>' + (f' <small>caption: <i>{E(w["caption"])}</i></small>' if w.get("caption") else "")
        feed = f'<span class="feedrun">As a Feed ad: {pct(w["feed"]["ctr"])} CTR on {num(w["feed"]["imp"])} impressions</span>' if w.get("feed") else ""
        sales = (f'{w["sales"]} · {w["roas"]:.2f}×' if w.get("sales") else "–")
        rows.append(f'''<li class="win"><span class="rank">{i}</span>{img}
  <div class="wtext">{line}<span class="wmeta">{E(w["product"])} · {E(w["place"])}</span><p>{E(w["why"])}</p>{feed}</div>
  <dl class="wstats"><div><dt>CTR</dt><dd class="big">{pct(w["ctr"])}</dd></div><div><dt>Outbound</dt><dd>{pct(w["octr"])}</dd></div>
  <div><dt>Impr.</dt><dd>{num(w["imp"])}</dd></div><div><dt>Sales · ROAS</dt><dd>{sales}</dd></div></dl></li>''')
    roas = lambda r: f"{r['roas']:.2f}×" if r["roas"] else "–"
    reels = "".join(f'<tr><td><i class="sl">{E(r["line"])}</i><small>{E(r["who"])}</small></td><td>{pct(r["ctr"])}</td><td>{pct(r["octr"])}</td>'
                    f'<td>{num(r["imp"])}</td><td>{r["sales"] or "–"}</td><td>{roas(r)}</td></tr>' for r in N.REELS)
    pats = "".join(f'<li><b>{E(t)}</b><p>{E(x)}</p></li>' for t, x in N.PATTERNS)
    fails = "".join(f'<li><b>{E(t)}</b><p>{E(x)}</p></li>' for t, x in N.FAILED)
    return f'''<ol class="lb">{"".join(rows)}</ol>
<div class="tablewrap"><table class="reels"><caption>Reels above 4%: they got the clicks, not the sales</caption>
<thead><tr><th>Reel</th><th>CTR</th><th>Outbound</th><th>Impr.</th><th>Sales</th><th>ROAS</th></tr></thead><tbody>{reels}</tbody></table></div>
<h3 class="sub">What the winners share</h3><ol class="pats">{pats}</ol>
<h3 class="sub">What did not work</h3><ul class="pats fails">{fails}</ul>'''

def page(M, csv_text, L):
    base = [m for m in M if not m["variant_of"]]; V = [m for m in M if m["variant_of"]]
    idx = "".join(f'<li><a href="#ad-{m["n"]}"><img src="web/{m["base"]}-feed.jpg" alt="" loading="lazy" width="720" height="900">'
                  f'<span class="ixl"><span class="ixn">{m["n"]}</span>{E(m["line"])}</span><span class="ixs" id="ix-{m["n"]}"></span></a></li>' for m in base)
    cards = "".join(ad_card(m, [v for v in V if v["variant_of"] == m["n"]]) for m in base)
    crit = "".join(f'<tr><td class="n">{n}</td><td><i class="sl">{E(a)}</i></td><td class="sc">{s}</td><td>{E(r)}</td>'
                   f'<td>{"<span class=kept>Kept</span>" if b == "Kept" else f"<i class=sl>{E(b)}</i>"}</td></tr>' for n, a, s, r, b in N.CRITIQUE)
    killed = "".join(f'<li><b>{E(i)}</b><p>{E(w)}</p></li>' for i, w in N.KILLED)
    by_n = {m["n"]: m for m in base}
    sets = "".join(f'<li><b>{E(name)}</b><span>{E(why)}</span><span class="ns">{" · ".join(ns)}</span></li>' for name, ns, why in N.PLAN["adsets"])
    flights = "".join(f'<tr><td class="n"><a href="#ad-{m["n"]}">{m["n"]}</a></td><td><i class="sl">{E(m["line"])}</i></td><td>{E(m["adset"])}</td>'
                      f'<td>{E(m["flight"])}</td><td class="r">{m["stock"]}</td></tr>' for m in base)
    stock = "".join(f'<li><b>{s}</b> {E(t)} <span>(ad {n})</span></li>' for n, t, s in N.PLAN["stock"])
    qs = "".join(f'<li><strong>{E(t)}</strong><p>{E(x)}</p></li>' for t, x in N.QUESTIONS)
    brand = "".join(f"<p>{E(p)}</p>" for p in N.BRAND)
    voice = "".join(f"<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>" for k, v in N.VOICE)
    files = len([1 for m in M for _ in (("feed", "story") if m["variant_of"] else ("feed", "story", "clean"))])
    credits = round(L["credits_before"] - L["credits_after"])
    data = json.dumps({"ads": [m["n"] for m in base]}).replace("</", "<\\/")
    rows = sum(1 for _ in __import__("csv").DictReader(csv_text.splitlines()))
    fill = dict(idx=idx, cards=cards, crit=crit, critic=E(N.CRITIC), killed=killed, sets=sets, flights=flights, stock=stock, qs=qs,
                brand=brand, voice=voice, winners=winners_html(), files=files, credits=credits, left=f"{L['credits_after']:.2f}",
                audience=E(N.PLAN["audience"]), budget=E(N.PLAN["budget"]), ab=E(N.PLAN["ab"]), kill=E(N.PLAN["kill"]), csv=E(csv_text),
                rows=rows, data=data, campaign=E(by_n["01"]["campaign"]))
    out = TEMPLATE
    for k, v in fill.items(): out = out.replace(f"@@{k}@@", str(v))
    assert "@@" not in out, out[out.index("@@") - 40:out.index("@@") + 40]
    return out

def label(w):
    """a winner as the README names it"""
    if w.get("caption"): return f"the ruby anaar Story, no text (caption “{w['caption']}”)"
    if w["id"] == "catalogue": return "the Edition Two carousel"
    if w["id"].startswith("reel"): return f"the {w['line']} reel"
    return f"“{w['line']}”"

def readme(M, L):
    base = [m for m in M if not m["variant_of"]]; V = [m for m in M if m["variant_of"]]
    o = ["# Naira Diwali 10 (25 Oct 2026)", "",
         "Ten Diwali ads for Naira, to run from 29 Oct to 10 Nov 2026 (Dhanteras 6 Nov, Diwali 8 Nov). Each one is built on a Naira ad that "
         "beat 4% CTR, and each line was written, judged by an independent critic, and rewritten before its photograph was made. Every ad "
         "has a Feed and a Story with the line, and a Story with no text to test against it. Nothing has been uploaded to Meta.", "",
         "## What beat 4%", "",
         "Every Naira ad above 4% CTR (all) with 250 or more impressions, from Meta on 25 Oct 2026 (lifetime). The March–May 2026 ads sold "
         "lehengas, a different business, and are left out.", "",
         "| # | Ad | Product · placement | CTR | Outbound | Impr. | Sales · ROAS |", "|---|---|---|---|---|---|---|"]
    for i, w in enumerate(N.WINNERS, 1):
        line = w["line"] + (f" (caption: {w['caption']})" if w.get("caption") else "")
        o.append(f"| {i} | {line} | {w['product']} · {w['place']} | {pct(w['ctr'])} | {pct(w['octr'])} | {num(w['imp'])} | "
                 + (f"{w['sales']} · {w['roas']:.2f}×" if w.get("sales") else "–") + " |")
    o += ["", "Reels above 4% (clicks, not sales):", "", "| Reel | CTR | Outbound | Impr. | Sales · ROAS |", "|---|---|---|---|---|"]
    for r in N.REELS:
        o.append(f"| {r['line']} ({r['who']}) | {pct(r['ctr'])} | {pct(r['octr'])} | {num(r['imp'])} | "
                 + (f"{r['sales']} · {r['roas']:.2f}×" if r["roas"] else "–") + " |")
    o += ["", "**What the winners share**", ""] + [f"{i}. **{t}.** {x}" for i, (t, x) in enumerate(N.PATTERNS, 1)]
    o += ["", "**What did not work**", ""] + [f"- **{t}.** {x}" for t, x in N.FAILED]
    o += ["", "## Naira, at Diwali", ""] + [p + "\n" for p in N.BRAND] + [f"- **{k}:** {v}" for k, v in N.VOICE]
    o += ["", "## The ten ads", ""]
    for m in base:
        a = N.ADS[m["n"]]; var = f", {m['variant']}" if m.get("variant") else ""
        o += [f"### {m['n']} · {m['line']}", "",
              f"{m['title']}{var} · {m['price']} · {m['stock']} in stock · {m['adset']} · {m['flight']} · score {N.SCORES[m['n']]:.1f}/10", "",
              f"- **Truth.** {a['truth']} {a['where']}", f"- **Picture.** {a['picture']}", f"- **Why the line works.** {a['turn']}",
              f"- **Built on.** " + "; ".join(f"{label(WIN[w])} ({pct(WIN[w]['ctr'])})" for w in a["built"]) + f". {a['built_note']}"]
        if a["killed"]: o.append("- **Lines it beat.** " + " ".join(f"“{l}” {r}" for l, r in a["killed"]))
        else: o.append(f"- **Kept from draft one.** {a['kept']}")
        if a.get("alt"): o.append(f"- **Test against it.** {a['alt']}")
        if a.get("regional"): o.append(f"- **Regional.** {a['regional']}")
        o += [f"- **What it changed for the next ad.** {a['next']}", f"- **Shoot.** {a['shoot']}"]
        o += [f"- **Flag.** {f}" for f in a["flags"]]
        o += ["", f"Files: `ads/{m['base']}-feed.jpg`, `-story.jpg`, `-story-clean.jpg`" +
              "".join(f", `ads/{v['base']}-feed.jpg`, `-story.jpg`" for v in V if v["variant_of"] == m["n"]), ""]
    o += ["## Draft one, judged", "", f"The critic’s summary: {N.CRITIC}", "", "| Ad | Draft one | Score | Why | Runs as |", "|---|---|---|---|---|"]
    o += [f"| {n} | {a} | {s} | {r} | {b} |" for n, a, s, r, b in N.CRITIQUE]
    o += ["", "Dropped before draft one:", "", "| Idea | Why it was dropped |", "|---|---|"] + [f"| {i} | {w} |" for i, w in N.KILLED]
    o += ["", "## How to run it", "", f"Campaign: {base[0].get('campaign', '')}", ""]
    o += [f"- **{name}** ({', '.join(ns)}): {why}." for name, ns, why in N.PLAN["adsets"]]
    o += [f"- **Audience.** {N.PLAN['audience']}", f"- **Budget (suggested).** {N.PLAN['budget']}", f"- **Story test.** {N.PLAN['ab']}",
          f"- **Kill rule.** {N.PLAN['kill']}", "- **Stock to watch.** " + "; ".join(f"{t}: {s}" for n, t, s in N.PLAN["stock"]) + ".", "",
          "| Ad | Line | Ad set | Flight | Stock |", "|---|---|---|---|---|"]
    o += [f"| {m['n']} | {m['line']} | {m['adset']} | {m['flight']} | {m['stock']} |" for m in base]
    o += ["", "## Open questions", ""] + [f"{i}. **{t}.** {x}" for i, (t, x) in enumerate(N.QUESTIONS, 1)]
    o += ["", "## Shoot", "",
          f"{len(L['jobs'])} submissions on Higgsfield (nano_banana_pro, 2K, 9:16) for {len(L['kept'])} kept photographs: "
          f"{L['credits_before'] - L['credits_after']:.0f} credits, {L['credits_after']:.2f} left. {L['note']}. Every attempt, its job ID "
          "and why it was redone are in `build/ledger.json`.", "",
          "## Contents", "",
          "- `plates/NN-<handle>.jpg`: the ten verified photographs, 1080×1920, no text.",
          "- `ads/NN-<handle>-feed.jpg` (1080×1350), `-story.jpg` and `-story-clean.jpg` (1080×1920); `07b` and `07c` are the Amma’s and "
          "Ma’s wordings of 07.",
          "- `build/frames.py` and `build/products.json`: the photograph prompts (scene, fidelity and construction lock, scale, composition, "
          "light, absence list) and each product’s references and locks.",
          "- `build/copy.json` and `build/variants.json`: the overlay for each ad. `build/ads.py` renders them in the house overlay "
          "(wordmark, Cormorant italic line, name and price in tracked Jost, in the photograph’s own ink).",
          "- `build/meta.py` writes `build/meta.csv` (the upload sheet, one row per file: primary text, headline, CTA, link with variant "
          "and UTMs, ad set, flight, regions, stock) and `build/manifest.json`.",
          "- `build/notes.py`: the thinking behind every ad; `build/page.py` renders it as this README and as the review page.",
          "- `build/ledger.json`: every Higgsfield job, the kept frame per ad, its retouch, score and flags.", "",
          "## Rebuilding", "", "```",
          "python3 build/frames.py [NN ...]            # print the prompts (--queue writes the batch request)",
          "python3 build/ads.py [NN ...]               # ads/ from copy.json",
          "python3 build/ads.py --copy variants.json   # the regional wordings of 07",
          "python3 build/meta.py                       # meta.csv, manifest.json",
          "python3 build/page.py                       # README.md and the review page in <scratchpad>/diwali10/artifact",
          "```", "",
          "## Product truth", "",
          "Every claim follows the live listings: gold tone or silver tone, cubic zirconia. Never real, diamond, waterproof or tarnish-free. "
          "The bundle offer in the primary text uses the live codes BUY2 and BUY3.", ""]
    return "\n".join(o)

TEMPLATE = open(f"{HERE}/page_template.html").read()

def main():
    M = json.load(open(f"{HERE}/manifest.json")); L = json.load(open(f"{HERE}/ledger.json")); csv_text = open(f"{HERE}/meta.csv").read()
    for m in M:
        m.setdefault("campaign", "Naira · Diwali, as it happens · 10 ads · Nov 2026")
    images(M)
    open(f"{ART}/index.html", "w").write(page(M, csv_text, L))
    open(f"{ROOT}/README.md", "w").write(readme(M, L))
    n = sum(len(fs) for _, _, fs in os.walk(ART)); mb = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(ART) for f in fs) / 1e6
    print(f"page: {n} files, {mb:.1f} MB in {ART}; README.md written")

if __name__ == "__main__":
    main()
