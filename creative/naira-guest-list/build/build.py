"""Composes the Guest List cards: Feed 1080x1350 and Story 1080x1920 for every ad in spec.py, plus the five carousel
cards. HTML laid out in pixels, screenshotted with Chromium, saved as JPEG 92 with no chroma subsampling.

The invitation-card system: a coloured band carries the function name in Velista capitals and the line in Cormorant
italic; the photograph fills the rest, cropped so the piece sits in the upper part of the window, clear of the caption.
Stories keep every word between 14% and 80% of the height (Meta's safe zone).
Checks: every font loaded, no line longer than three rows, caption and chip never overlap, every featured piece has
the stock the spec demands."""
import asyncio, base64, html, json, re, sys
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright
sys.path.insert(0, str(Path(__file__).resolve().parent))
import spec

D = Path(__file__).resolve().parent.parent            # scratchpad/camp
S = D.parent
FONTS = S / "labels" / "fonts"
OUT = D / "out"; OUT.mkdir(exist_ok=True)
LIVE = json.load(open(D / "data" / "live.json"))
STOCK = json.load(open(D / "data" / "inventory.json"))
LOGO = json.load(open("/home/user/naira-scroll/creative/naira-bag/build/assets/naira-logo-vector.json"))
CHROME = "/opt/pw-browsers/chromium"
INK, CREAM = "#1F1A14", "#F7F1E6"
FEED, STORY = (1080, 1350), (1080, 1920)


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def face(fam, file, weight=400, style="normal", rng=None):
    fmt = "truetype" if file.endswith(".ttf") else "woff2"
    r = f"unicode-range:{rng};" if rng else ""
    return (f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(FONTS / file)}) format('{fmt}');"
            f"font-weight:{weight};font-style:{style};font-display:block;{r}}}")


FONT_CSS = "".join([
    face("Velista", "Velista.ttf"), face("RupeeV", "Laila-300-r.woff2", 400, rng="U+20B9"),
    face("JostF", "Jost-300.woff2", 300), face("JostF", "Jost-400.woff2", 400), face("JostF", "Jost-500.woff2", 500),
    face("Rupee", "Poppins-400-deva.woff2", 300, rng="U+20B9"), face("Rupee", "Poppins-400-deva.woff2", 400, rng="U+20B9"),
    face("Rupee", "Poppins-500-deva.woff2", 500, rng="U+20B9"),
    face("CormI", "CormorantGaramond-300i.woff2", 400, "italic"), face("CormR", "CormorantGaramond-300-r.woff2", 400, "italic", rng="U+20B9"),
    face("Corm", "CormorantGaramond-500-latin.woff2", 500), face("CormRu", "CormorantGaramond-500-r.woff2", 500, rng="U+20B9"),
])


def inr(n):
    s = str(int(round(n)))
    if len(s) <= 3: return "₹" + s
    head, tail = s[:-3], s[-3:]
    return "₹" + re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head) + "," + tail


def logo(w, letters, flower):
    px = py = 65
    vw, vh = LOGO["width"] - 2 * px, LOGO["height"] - 2 * py
    return (f"<svg class='logo' style='width:{w}px;height:{w * vh / vw:.1f}px' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{LOGO['letters']}' fill='{letters}' fill-rule='evenodd'/><path d='{LOGO['flower']}' fill='{flower}' fill-rule='evenodd'/></svg>")


def esc(t):
    return html.escape(t, quote=False)


def photo_css(pid, fx, fy, box_w, box_h, at=0.42):
    """Cover-crop the photo into a box of box_w x box_h so the focus point lands at `at` of the box height."""
    p = D / "img" / "raw" / f"{pid}.png"
    W, H = Image.open(p).size
    scale = max(box_w / W, box_h / H)
    sw, sh = W * scale, H * scale
    x = min(max(fx * sw - box_w / 2, 0), sw - box_w)
    y = min(max(fy * sh - box_h * at, 0), sh - box_h)
    return (f"background-image:url('{p.as_uri()}');background-size:{sw:.0f}px {sh:.0f}px;background-position:{-x:.0f}px {-y:.0f}px;"
            f"height:{box_h}px")


def shop(handle):
    v = LIVE[handle]
    return v, (D / "img" / "shop" / f"{handle}.jpg").as_uri()


def tile(handle, h, caption=True):
    v, src = shop(handle)
    cap = f"<div class='tn'>{esc(v['title'])}</div><div class='tp'>{inr(v['price'])}</div>" if caption else ""
    return f"<div class='tile'><div class='tph' style=\"background-image:url('{src}')\"></div>{cap}</div>"


CSS = """
* { margin:0; padding:0; box-sizing:border-box }
body { width:1080px; background:#000; font-family:'Rupee','JostF',sans-serif; -webkit-font-smoothing:antialiased }
.card { position:relative; width:1080px; overflow:hidden; display:flex; flex-direction:column; background:var(--band); color:var(--on) }
.band { padding:60px 64px 48px; display:flex; flex-direction:column; gap:14px }
.story .band { padding-top:290px }
.eyebrow { font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:20px; letter-spacing:.26em; text-transform:uppercase; opacity:.9 }
.story .eyebrow { font-size:22px }
.title { font-family:'RupeeV','Velista',serif; font-size:104px; line-height:.98; letter-spacing:.01em; margin-top:4px }
.story .title { font-size:112px }
.title.small { font-size:84px } .story .title.small { font-size:92px }
.hook { font-family:'CormR','CormI',serif; font-style:italic; font-size:62px; line-height:1.08; text-wrap:balance; max-width:940px; margin-top:2px }
.story .hook { font-size:66px }
.hook.solo { font-size:80px; line-height:1.05 } .story .hook.solo { font-size:84px }
.sub { font-family:'Rupee','JostF',sans-serif; font-weight:300; font-size:28px; line-height:1.35; opacity:.95; max-width:900px }
.story .sub { font-size:31px }
.ph { position:relative; width:1080px; background-repeat:no-repeat }
.ph::after { content:''; position:absolute; left:0; right:0; bottom:0; height:44%; background:linear-gradient(to top, rgba(0,0,0,.55), rgba(0,0,0,0)) }
.cap { position:absolute; left:64px; bottom:52px; z-index:2; color:#F7F1E6; display:flex; flex-direction:column; gap:8px }
.pn { font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:28px; letter-spacing:.03em }
.pp { font-family:'RupeeV','Velista',serif; font-size:60px; line-height:1 }
.chip { position:absolute; right:64px; bottom:60px; z-index:2; font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:18px; letter-spacing:.18em; text-transform:uppercase; color:#F7F1E6; border:1.5px solid rgba(247,241,230,.85); padding:14px 18px; white-space:nowrap }
.story .cap { bottom:400px } .story .chip { bottom:408px }
.logo { display:block; margin-bottom:4px }
.wrap { flex:1; display:flex; flex-direction:column; padding:8px 64px 56px; gap:26px }
.story .wrap { padding-bottom:400px }
.grid { display:grid; gap:14px; flex:1; min-height:0; grid-auto-rows:1fr }
.g3 { grid-template-columns:repeat(3,1fr) } .g2 { grid-template-columns:repeat(2,1fr) }
.tile { display:flex; flex-direction:column; gap:6px; min-height:0 }
.tph { width:100%; flex:1; min-height:0; background-size:cover; background-position:center; border:1px solid rgba(31,26,20,.10) }
.tn { font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:22px; line-height:1.2; margin-top:6px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis }
.tp { font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:24px; letter-spacing:.02em }
.foot { display:flex; justify-content:space-between; align-items:center; margin-top:auto }
.foot .chip { position:static; color:var(--on); border-color:rgba(31,26,20,.5) }
.go { font-family:'Rupee','JostF',sans-serif; font-weight:500; font-size:20px; letter-spacing:.18em; text-transform:uppercase; padding:16px 22px; background:#1F1A14; color:#F7F1E6; white-space:nowrap }
.maths { display:flex; align-items:baseline; gap:26px; flex-wrap:wrap }
.maths .was { font-family:'RupeeV','Velista',serif; font-size:56px; text-decoration:line-through; text-decoration-thickness:2px; opacity:.5 }
.maths .now { font-family:'RupeeV','Velista',serif; font-size:100px; line-height:1 }
.maths .lbl { font-family:'Rupee','JostF',sans-serif; font-weight:400; font-size:23px; letter-spacing:.03em; max-width:320px; line-height:1.3 }
.rule { height:0; border-top:1.5px solid currentColor; opacity:.3 }
"""


def doc(colour, story, inner):
    band, on, flower = spec.COL[colour]
    h = STORY[1] if story else FEED[1]
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}{CSS}:root{{--band:{band};--on:{on}}}</style></head>"
            f"<body><div class='card{' story' if story else ''}' style='height:{h}px'>{inner}</div></body></html>")


def band(ad, extra=""):
    t = ad.get("title", "")
    parts = [f"<div class='eyebrow'>{esc(ad['eyebrow'])}</div>"]
    if t: parts.append(f"<div class='title{' small' if len(t) > 9 else ''}'>{esc(t)}</div>")
    parts.append(f"<div class='hook{'' if t else ' solo'}'>{esc(ad['hook'])}</div>")
    if ad.get("sub"): parts.append(f"<div class='sub'>{esc(ad['sub'])}</div>")
    return f"<div class='band'>{''.join(parts)}{extra}</div>"


BAND_H = {}      # measured on the first pass so the photo box can be sized exactly


def card_photo(ad, story, band_h):
    _, on, flower = spec.COL[ad["colour"]]
    pid, fx, fy = ad["story" if story else "feed"]
    v = LIVE[ad["piece"]]
    box_h = (STORY[1] if story else FEED[1]) - band_h
    at = 0.38 if story else 0.42
    inner = "".join([band(ad), f"<div class='ph' style=\"{photo_css(pid, fx, fy, 1080, box_h, at)}\"></div>",
        f"<div class='cap'>{logo(126, CREAM, '#FFBDA8')}<div class='pn'>{esc(v['title'])}</div><div class='pp'>{inr(v['price'])}</div></div>",
        f"<div class='chip'>{esc(spec.OFFER)}</div>"])
    return doc(ad["colour"], story, inner)


def card_grid(ad, story):
    _, on, flower = spec.COL[ad["colour"]]
    tiles = "".join(tile(x, 0) for x in (ad["grid"][:6] if story else ad["grid"]))
    inner = band(ad) + f"<div class='wrap'><div class='grid g3'>{tiles}</div><div class='foot'>{logo(150, on, flower)}<div class='chip'>{esc(spec.OFFER)}</div></div></div>"
    return doc(ad["colour"], story, inner)


def card_trio(ad, story):
    _, on, flower = spec.COL[ad["colour"]]
    total = sum(LIVE[x]["price"] for x in ad["trio"])
    tiles = "".join(tile(x, 380 if story else 290) for x in ad["trio"])
    inner = band(ad) + ("<div class='wrap'>" f"<div class='grid g3'>{tiles}</div><div class='rule'></div>"
        f"<div class='maths'><span class='was'>{inr(total)}</span><span class='now'>{inr(total * 0.8)}</span><span class='lbl'>for all three with code BUY3 at checkout</span></div>"
        f"<div class='foot'>{logo(150, on, flower)}<div class='go'>Shop all</div></div></div>")
    return doc(ad["colour"], story, inner)


def carousel(ad):
    _, on, flower = spec.COL[ad["colour"]]
    out = []
    cover = "".join(tile(x, 232, caption=False) for x in ad["cover"])
    out.append(("I1_card1_cover_feed", doc(ad["colour"], False, band(ad) + f"<div class='wrap'><div class='grid g3'>{cover}</div><div class='foot'>{logo(150, on, flower)}<div class='chip'>{esc(spec.OFFER)}</div></div></div>")))
    for n, (name, key, hs) in enumerate(ad["cards"], start=2):
        t = name.lower().rstrip("s")
        cnt = sum(1 for v in LIVE.values() if v["type"].lower().rstrip("s") == t)
        low = min(v["price"] for v in LIVE.values() if v["type"].lower().rstrip("s") == t)
        a = dict(eyebrow=f"THE GUEST LIST · {n - 1} OF 4", title=name, hook=f"{cnt} pieces in stock, from {inr(low)}.")
        tiles = "".join(tile(x, 326) for x in hs)
        out.append((f"I1_card{n}_{key}_feed", doc(ad["colour"], False, band(a) + f"<div class='wrap'><div class='grid g2'>{tiles}</div><div class='foot'>{logo(150, on, flower)}<div class='go'>Shop {key}</div></div></div>")))
    hs = ad["cover"] + ad["cover_extra"]
    tiles = "".join(tile(x, 232, caption=False) for x in hs)
    out.append(("I1_cover_story", doc(ad["colour"], True, band(ad) + f"<div class='wrap'><div class='grid g3'>{tiles}</div><div class='foot'>{logo(150, on, flower)}<div class='chip'>{esc(spec.OFFER)}</div></div></div>")))
    return out


CHECK = """() => {
  const bad = [];
  for (const sel of ['.hook', '.title']) { const e = document.querySelector(sel); if (e) { const lh = parseFloat(getComputedStyle(e).lineHeight); if (e.getBoundingClientRect().height > lh * 3.2) bad.push(sel + ' over 3 lines'); } }
  const cap = document.querySelector('.cap'), chip = document.querySelector('.card > .chip');
  if (cap && chip) { const a = cap.getBoundingClientRect(), b = chip.getBoundingClientRect(); if (a.right > b.left - 24 && a.bottom > b.top && b.bottom > a.top) bad.push('caption meets chip'); }
  document.querySelectorAll('.tn').forEach(e => { if (e.scrollWidth > e.clientWidth + 1) bad.push('tile name clipped: ' + e.textContent); });
  const card = document.querySelector('.card');
  if (card.scrollHeight > card.clientHeight + 1) bad.push('card overflows by ' + (card.scrollHeight - card.clientHeight) + 'px');
  if (card.classList.contains('story')) document.querySelectorAll('.band *, .cap, .chip, .foot').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && (r.top < 269 || r.bottom > 1536)) bad.push('outside story safe zone: ' + e.className); });
  const fonts = [...document.fonts].filter(f => f.status !== 'loaded' && !/Rupee 500|RupeeV|CormR/.test(f.family + ' ' + f.weight)).map(f => f.family + ' ' + f.weight + ' ' + f.status);
  const bandH = document.querySelector('.band') ? document.querySelector('.band').getBoundingClientRect().height : 0;
  return {bad, fonts, bandH};
}"""


def slug(ad):
    return re.sub(r"[^a-z0-9]+", "-", (ad.get("piece") or ad["kind"]).lower()).strip("-")


def stock_check():
    bad = []
    for ad in spec.ADS:
        need = spec.MIN_HERO if ad["kind"] == "photo" else spec.MIN_GRID
        hs = [ad["piece"]] if ad.get("piece") else []
        for k in ("cover", "cover_extra", "grid", "trio"): hs += ad.get(k, [])
        for c in ad.get("cards", []): hs += c[2]
        for h in hs:
            if STOCK.get(h, 0) < need: bad.append((ad["id"], h, STOCK.get(h)))
    return bad


async def render(b, name, html_doc, story):
    f = D / "html" / f"{name}.html"; f.write_text(html_doc)
    pg = await b.new_page(viewport={"width": 1080, "height": STORY[1] if story else FEED[1]}, device_scale_factor=1)
    await pg.goto(f.as_uri(), wait_until="networkidle")
    await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(200)
    res = await pg.evaluate(CHECK)
    png = OUT / f"{name}.png"
    await pg.screenshot(path=str(png), full_page=False)
    await pg.close()
    Image.open(png).convert("RGB").save(OUT / f"{name}.jpg", "JPEG", quality=92, subsampling=0, optimize=True)
    png.unlink()
    return res


async def main():
    bad = stock_check()
    if bad:
        print("STOCK TOO LOW:", bad); sys.exit(1)
    (D / "html").mkdir(exist_ok=True)
    for f in OUT.glob("*.jpg"): f.unlink()
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for ad in spec.ADS:
            if ad["kind"] == "carousel":
                for name, h in carousel(ad):
                    res = await render(b, name, h, name.endswith("story"))
                    print(f"{name:40s} {res['bad'] or ''} {res['fonts'] or ''}")
                continue
            for story in (False, True):
                name = f"{ad['id']}_{slug(ad)}_{'story' if story else 'feed'}"
                if ad["kind"] == "photo":
                    # pass 1 measures the band, pass 2 sizes the photo box to the remainder
                    res = await render(b, name, card_photo(ad, story, 400), story)
                    res = await render(b, name, card_photo(ad, story, round(res["bandH"])), story)
                else:
                    res = await render(b, name, {"grid": card_grid, "trio": card_trio}[ad["kind"]](ad, story), story)
                print(f"{name:40s} {res['bad'] or ''} {res['fonts'] or ''}")
        await b.close()
    deck = []
    for ad in spec.ADS:
        link = spec.LINKS[ad["link"]] + "?" + spec.UTM.format(id=ad["id"])
        piece = LIVE[ad["piece"]] if ad.get("piece") else None
        deck.append(dict(id=ad["id"], layer=ad["layer"], kind=ad["kind"], colour=ad["colour"], link=link, collection=ad["link"],
                         eyebrow=ad["eyebrow"], title=ad.get("title", ""), hook=ad["hook"], sub=ad.get("sub", ""),
                         piece=piece["title"] if piece else None, price=piece["price"] if piece else None, stock=STOCK.get(ad.get("piece"), None),
                         headline=ad["headline"], primary=ad["primary"], description="Free insured shipping · Cash on delivery", cta="SHOP_NOW",
                         why=ad["why"], drafts=spec.DRAFTS[ad["id"]], files=sorted(p.name for p in OUT.glob(f"{ad['id']}_*.jpg"))))
    json.dump(dict(plan=spec.PLAN, offer=spec.OFFER, ads=deck), open(OUT / "deck.json", "w"), indent=1, ensure_ascii=False)
    print("deck:", len(deck), "ads,", sum(len(a["files"]) for a in deck), "files")


if __name__ == "__main__":
    asyncio.run(main())
