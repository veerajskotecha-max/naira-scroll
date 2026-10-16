# Builds finished ads from the keepers: each keeper photograph cropped to its exact Meta size (Feed 4:5 at 1080×1350, Stories 9:16
# at 1080×1920) with the copy from ads.json set in the Naira typefaces, rendered by Chromium. Output: <scratchpad>/ads/out/<id>.jpg
# and a contact sheet. Usage: build_ads.py [--cfg controls.json] [id ...]   (no ids = all; ads.json by default)
# An entry with "path" uses that photo (relative to docs/creative) instead of a keeper plate, as the plain controls do; "box"
# ([x0, y0, x1, y1] in plate pixels) frames a plate before it is fitted to the format, as the composites need.
import json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
OUT, WORK, FONTS = f"{SPB}/ads/out", f"{SPB}/ads/work", f"{SPB}/c4/fonts"
SIZE = {"4:5": (1080, 1350), "9:16": (1080, 1920)}
SAFE = {"4:5": (72, 72), "9:16": (290, 380)}            # clear space from the top and bottom edges (Stories keep clear of the UI)
INK, CREAM = "#1C1C1C", "#FBF8F3"

CSS = """
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative}
.t{position:absolute;display:flex;flex-direction:column;gap:%(gap)dpx;color:var(--tone);isolation:isolate}
.h{font-family:CGI;font-weight:500;font-size:%(hs)dpx;line-height:.98;letter-spacing:-.005em;text-wrap:balance}
.c{font-family:CG;font-weight:500;font-size:%(cs)dpx;line-height:1.2;text-wrap:balance}
.n{font-family:Jost;font-weight:500;font-size:%(ns)dpx;letter-spacing:.2em;text-transform:uppercase;margin-top:8px;line-height:1.5}
.scrim::before{content:"";position:absolute;inset:-70px -90px;z-index:-1;
  background:radial-gradient(closest-side,var(--glow) 0%%,var(--glow) 45%%,transparent 100%%)}
.card{background:rgba(251,248,243,.94);padding:30px 34px 26px}
"""

# The brand layout ("deck", the default): the system of the account's best ad, "Almost edible.", with the Naira deck's wordmark.
# Headline in Velista capitals (the brand serif), the correction in lowercase Cormorant italic, then a short rule, a spec line of
# listing facts in tracked Jost capitals, an ink CTA and the price, and the NAIRA wordmark (the deck's tulip I) signed off above
# the price with its own height of clear space: the deck's black on light grounds, white on dark (the deck's sage, #99B4AE, reads
# about 2:1 on these photos, so it is only an option). Ink #1A1614 and paper #FBF8F3 are the site's own.
BRAND = f"{HERE}/brand"
DECK_INK, DECK_PAPER = "#1A1614", "#FBF8F3"
DECK_CSS = """
@font-face{font-family:Velista;src:url("file://%(b)s/Velista.ttf");font-weight:400 600}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
*{box-sizing:border-box}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative;color:var(--tone)}
.blk{position:absolute;display:flex;flex-direction:column;isolation:isolate}
.h{font-family:Velista;font-weight:500;font-size:%(hs)dpx;line-height:.9;letter-spacing:-.005em;text-transform:uppercase;text-wrap:balance;margin:0}
.c{font-family:CGI;font-weight:500;font-size:%(cs)dpx;line-height:1.16;text-wrap:balance;margin:%(gap)dpx 0 0}
.ft{position:absolute;left:%(side)dpx;right:%(side)dpx;bottom:%(bot)dpx;display:flex;justify-content:space-between;align-items:flex-end;isolation:isolate}
.ft .l{display:flex;flex-direction:column;align-items:flex-start}
.rule{width:64px;height:2px;background:var(--tone);margin-bottom:16px}
.spec{font-family:Jost;font-weight:500;font-size:%(ss)dpx;letter-spacing:.24em;text-transform:uppercase;line-height:1.45;max-width:%(sw)dpx}
.cta{margin-top:22px;background:var(--btn);color:var(--btnt);font-family:Jost;font-weight:600;font-size:%(bs)dpx;letter-spacing:.22em;
  text-transform:uppercase;padding:%(bp)dpx %(bpx)dpx;line-height:1;white-space:nowrap}
.price{font-family:Jost;font-weight:500;font-size:%(ps)dpx;letter-spacing:.2em;text-transform:uppercase;white-space:nowrap;line-height:1;padding-bottom:%(pp)dpx}
.wm{position:absolute;height:%(wh)dpx}
.ft .r{display:flex;flex-direction:column;align-items:flex-end;gap:40px}
.wmf{height:%(wh)dpx;display:block}
.band,.tband{position:absolute;left:0;right:0;pointer-events:none}
.band{bottom:0;height:%(bh)dpx;background:linear-gradient(to top,rgba(255,248,245,.93) 0,rgba(255,248,245,.93) %(bsd)dpx,rgba(255,248,245,0) 100%%)}
.tband{top:0;height:%(th)dpx;background:linear-gradient(to bottom,rgba(255,248,245,.93) 0,rgba(255,248,245,.93) %(ts)dpx,rgba(255,248,245,0) 100%%)}
.glow::before{content:"";position:absolute;inset:-80px -100px;z-index:-1;
  background:radial-gradient(closest-side,var(--glow) 0%%,var(--glow) 42%%,transparent 100%%)}
"""

def html_deck(ad, bg):
    W, H = SIZE[ad["fmt"]]; story = ad["fmt"] == "9:16"
    side = ad.get("x", 64); top, bot = ((340 if ad.get("ext") else 300), 392) if story else (64, 60)
    cream = ad.get("tone") == "cream"; tone = DECK_PAPER if cream else DECK_INK
    glow = "rgba(28,22,18,.42)" if cream else "rgba(251,246,240,.80)"
    btn, btnt = (DECK_PAPER, DECK_INK) if cream else (DECK_INK, DECK_PAPER)
    if story and not ad.get("story_cta"): ad = dict(ad, cta=None)   # Stories carry Meta's own CTA sticker; one is enough
    at = ad.get("at", "tl"); foot_h = 150 if ad.get("cta") else 70
    y = ad.get("y", top if at[0] == "t" else bot + foot_h + 46)
    pos = {"tl": f"left:{side}px;top:{y}px", "tr": f"right:{side}px;top:{y}px;text-align:right;align-items:flex-end",
           "bl": f"left:{side}px;bottom:{y}px", "br": f"right:{side}px;bottom:{y}px;text-align:right;align-items:flex-end"}[at]
    wm_file = {"ink": "logo_ink.png", "white": "logo_white.png", "sage": "logo_sage.png"}[ad.get("wm", "white" if cream else "ink")]
    wh = ad.get("wh", 40); wm_corner = "left" if at in ("tr",) else "right"
    wm_y = ad.get("wy", top + 8)
    foot_wm = ad.get("wmpos", "foot") == "foot"            # default: the wordmark signs off above the price
    css = DECK_CSS % dict(b=BRAND, f=FONTS, w=W, h=H, bg="file://" + bg, hs=ad.get("hs", 100), cs=ad.get("cs", 40), gap=ad.get("gap", 18),
                          side=side, bot=bot, ss=ad.get("ss", 18), sw=ad.get("sw", 620), bs=19, bp=21, bpx=32, ps=22, pp=21, wh=wh,
                          bh=bot + foot_h + 130, bsd=bot + foot_h + 20, th=ad.get("th", y + 330 if at[0] == "t" else 0), ts=ad.get("ts", (y + 330) * .62 if at[0] == "t" else 0))
    bands = ('<div class="band"></div>' if ad.get("band") else "") + ('<div class="tband"></div>' if ad.get("tband") else "")
    cls = "blk" + (" glow" if ad.get("scrim") else "")
    fcls = "ft" + (" glow" if ad.get("fscrim") else "")
    spec = f'<div class="rule"></div><div class="spec">{glue(ad["spec"])}</div>' if ad.get("spec") else ""
    cta = f'<div class="cta">{ad["cta"]}</div>' if ad.get("cta") else ""
    return (f'<meta charset="utf-8"><style>{css}</style><body style="--tone:{tone};--glow:{glow};--btn:{btn};--btnt:{btnt}">' + bands
            + ("" if foot_wm else f'<img class="wm" src="file://{BRAND}/{wm_file}" style="{wm_corner}:{side}px;top:{wm_y}px">') +
            f'<div class="{cls}" style="{pos};width:{ad["w"]}px"><h1 class="h">{glue(ad["h"])}</h1>'
            + (f'<p class="c">{glue(ad["c"])}</p>' if ad.get("c") else "") + '</div>'
            f'<div class="{fcls}"><div class="l">{spec}{cta}</div><div class="r">'
            + (f'<img class="wmf" src="file://{BRAND}/{wm_file}">' if foot_wm else "") +
            f'<div class="price">{glue(ad.get("price", ""))}</div></div></div></body>')

def smooth1d(row, sigma):
    r = int(sigma * 3); x = np.arange(-r, r + 1); k = np.exp(-x ** 2 / (2 * sigma ** 2)); k /= k.sum()
    pad = np.pad(row, ((r, r), (0, 0)), mode="edge")
    return np.stack([np.convolve(pad[:, c], k, mode="valid") for c in range(3)], 1)

def extend916(im):
    # A 4:5 photo set in a 9:16 frame: above and below, its own backdrop continues from the edge rows and drifts to their mean
    # colour, with the seams softened and a fine grain to match. The extension sits mostly under the Stories interface.
    a = np.asarray(im.resize((1080, 1350), Image.LANCZOS)).astype(np.float32); H, off = 1920, 285
    can = np.zeros((H, 1080, 3), np.float32); can[off:off + 1350] = a
    for rows, rng in ((a[:30], range(off - 1, -1, -1)), (a[-30:], range(off + 1350, H))):
        row = smooth1d(rows.mean(0), 25); flat = rows.reshape(-1, 3).mean(0); n = len(rng)
        for i, y in enumerate(rng):
            t = min(1, (i / n) ** 0.8); can[y] = row * (1 - t) + flat * t
    img = Image.fromarray(np.clip(can, 0, 255).astype(np.uint8))
    blur = img.filter(ImageFilter.GaussianBlur(10)); mp = np.zeros((H, 1080), np.float32)
    for seam in (off, off + 1350):
        for d in range(-40, 41):
            if 0 <= seam + d < H: mp[seam + d] = np.maximum(mp[seam + d], 1 - abs(d) / 40)
    img = Image.composite(blur, img, Image.fromarray((mp * 255).astype(np.uint8)))
    g = np.random.default_rng(7).normal(0, 2.2, (H, 1080, 1)).astype(np.float32)
    mask = np.ones((H, 1, 1), np.float32); mask[off:off + 1350] = 0
    return Image.fromarray(np.clip(np.asarray(img).astype(np.float32) + g * mask, 0, 255).astype(np.uint8))

def extend_mirror(im, off=285, H=1920, max_blur=18, grain=2.2):
    # For frames whose texture runs to the edge (the ECG grid): mirror the photo's edge band across each seam, sharp at the seam
    # and blurring progressively away from it, then drift the outer 40% toward the edge colour under the Stories interface.
    a = np.asarray(im.resize((1080, 1350), Image.LANCZOS)).astype(np.float32)
    can = np.zeros((H, 1080, 3), np.float32); can[off:off + 1350] = a
    n_top, n_bot = off, H - off - 1350
    for d in range(n_top): can[off - 1 - d] = a[min(d, 1349)]
    for d in range(n_bot): can[off + 1350 + d] = a[max(1349 - d, 0)]
    base = Image.fromarray(np.clip(can, 0, 255).astype(np.uint8))
    L = [np.asarray(x).astype(np.float32) for x in [base] + [base.filter(ImageFilter.GaussianBlur(r)) for r in (3, 7, 12, max_blur)]]
    out = can.copy()
    for d in range(max(n_top, n_bot)):
        t = (d / max(n_top, n_bot)) ** 0.75 * (len(L) - 1); i = min(int(t), len(L) - 2); f = t - i
        for y in ([off - 1 - d] if d < n_top else []) + ([off + 1350 + d] if d < n_bot else []):
            out[y] = L[i][y] * (1 - f) + L[i + 1][y] * f
    for rng, band in ((range(0, off), a[:40]), (range(off + 1350, H), a[-40:])):
        flat = band.reshape(-1, 3).mean(0)
        for y in rng:
            d = (off - 1 - y) if y < off else (y - off - 1350); n = n_top if y < off else n_bot
            w = max(0.0, (d / n - 0.6) / 0.4) * 0.7; out[y] = out[y] * (1 - w) + flat * w
    g = np.random.default_rng(7).normal(0, grain, (H, 1080, 1)).astype(np.float32)
    mask = np.ones((H, 1, 1), np.float32); mask[off:off + 1350] = 0
    return Image.fromarray(np.clip(out + g * mask, 0, 255).astype(np.uint8))

def prep(ad):
    src = os.path.join(HERE, "..", ad["path"]) if "path" in ad else f"{SPB}/{ad['src']}/plates/{ad.get('plate', ad['id'])}.png"
    W, H = SIZE["4:5" if ad.get("ext") else ad["fmt"]]
    im = Image.open(src).convert("RGB")
    if "box" in ad: im = im.crop(tuple(ad["box"]))                       # a composite's framing, in plate pixels
    w, h = im.size
    if w / h > W / H: nw = round(h * W / H); box = (round((w - nw) * ad.get("cx", .5)), 0, round((w - nw) * ad.get("cx", .5)) + nw, h)
    else: nh = round(w * H / W); box = (0, round((h - nh) * ad.get("cy", .5)), w, round((h - nh) * ad.get("cy", .5)) + nh)
    path = f"{WORK}/{ad['id']}_bg.jpg"; im = im.crop(box)
    ext = ad.get("ext")
    (extend_mirror(im) if ext == "mirror" else extend916(im) if ext else im.resize((W, H), Image.LANCZOS)).save(path, quality=95); return path

def glue(t):
    return re.sub(r"(\d) (mm|cm)\b", "\\1\u00a0\\2", t)                  # never break a number from its unit

def html(ad, bg):
    W, H = SIZE[ad["fmt"]]; top, bottom = (357, 380) if ad.get("ext") else SAFE[ad["fmt"]]; side = ad.get("x", 72)
    pos = {"tl": f"left:{side}px;top:{ad.get('y', top)}px", "tr": f"right:{side}px;top:{ad.get('y', top)}px;text-align:right;align-items:flex-end",
           "bl": f"left:{side}px;bottom:{ad.get('y', bottom if ad['fmt'] == '9:16' else 72)}px",
           "br": f"right:{side}px;bottom:{ad.get('y', bottom if ad['fmt'] == '9:16' else 72)}px;text-align:right;align-items:flex-end"}[ad["at"]]
    tone = CREAM if ad.get("tone") == "cream" else INK
    glow = "rgba(28,22,18,.45)" if ad.get("tone") == "cream" else "rgba(250,243,236,.78)"
    cls = "t" + (" scrim" if ad.get("scrim") else "") + (" card" if ad.get("card") else "")
    css = CSS % dict(f=FONTS, w=W, h=H, bg="file://" + bg, hs=ad.get("hs", 92), cs=ad.get("cs", 42), ns=ad.get("ns", 23), gap=ad.get("gap", 18))
    return (f'<meta charset="utf-8"><style>{css}</style><div class="{cls}" style="{pos};width:{ad["w"]}px;--tone:{tone};--glow:{glow}">'
            f'<div class="h">{glue(ad["h"])}</div><div class="c">{glue(ad["c"])}</div><div class="n">{glue(ad["n"])}</div></div>')

def main():
    args = sys.argv[1:]; name = "ads.json"
    if "--cfg" in args: i = args.index("--cfg"); name = args[i + 1]; del args[i:i + 2]
    cfg = json.load(open(f"{HERE}/{name}"))["ads"]; want = args
    for d in [OUT, WORK]: os.makedirs(d, exist_ok=True)
    jobs = []
    for ad in cfg:
        if want and ad["id"] not in want: continue
        open(f"{WORK}/{ad['id']}.html", "w").write((html if ad.get("layout") == "v1" else html_deck)(ad, prep(ad)))
        W, H = SIZE[ad["fmt"]]; jobs.append(f"{ad['id']}:{W}:{H}")
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", f"{HERE}/render.cjs", WORK, *jobs], check=True, env=env)
    for j in jobs:
        i = j.split(":")[0]; Image.open(f"{WORK}/{i}.png").convert("RGB").save(f"{OUT}/{i}.jpg", quality=92, subsampling=0); print("ad", i)
    ids = [a["id"] for a in cfg if os.path.exists(f"{OUT}/{a['id']}.jpg")]
    tw = 360; ims = [Image.open(f"{OUT}/{i}.jpg") for i in ids]; ims = [im.resize((tw, round(im.height * tw / im.width))) for im in ims]
    cols = 5; rows = [ims[r:r + cols] for r in range(0, len(ims), cols)]
    sheet = Image.new("RGB", (cols * (tw + 12) + 12, sum(max(i.height for i in r) + 12 for r in rows) + 12), (236, 232, 226)); y = 12
    for r in rows:
        for k, im in enumerate(r): sheet.paste(im, (12 + k * (tw + 12), y))
        y += max(i.height for i in r) + 12
    sheet.save(f"{SPB}/ads/sheet_{name.split('.')[0]}.jpg", quality=86); print("sheet", sheet.size)

if __name__ == "__main__":
    main()
