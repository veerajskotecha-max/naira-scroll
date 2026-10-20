# Catalogue cards for every in-stock product, three per product, at 1080×1080 (the Meta catalogue and carousel size):
#   A "worn"    the on-model photo cropped round the piece; NAIRA on top, name and price below (the Palmonas look)
#   B "detail"  worn and close-up side by side, labelled, with a cream name plate
#   C "loupe"   a second on-model photo (or a wider crop) with the close-up in a magnifier pointing at the piece
# Products with no on-model photo use their product shots in the same layouts (C becomes the close-up, full bleed).
# Inputs: <scratchpad>/cat/src/products_pick.json and full/ (fetch_full.py, alts.py, variants.py), boxes.txt here.
# Usage: cards.py [handle ...]   (default: all) -> <scratchpad>/cat/out/cards/<handle>-<A|B|C>.jpg and cards.json
import html, json, math, os, subprocess, sys
from PIL import Image, ImageFilter, ImageStat

HERE = os.path.dirname(os.path.abspath(__file__))
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/cat"
SRC, WORK, OUT, FONTS = f"{SP}/src", f"{SP}/work/cards", f"{SP}/out/cards", f"{SP}/fonts"
BRAND = os.path.normpath(f"{HERE}/../finished-ads/brand")
N, GUT = 1080, 6
INK, PAPER, CORAL, PILL = "#1A1614", "#FFF8F5", "#B4513B", "#F0A08F"
FILL = {"Ring": .30, "Earrings": .28, "Bracelet": .58, "Necklace": .76, "Jewellery": .6}   # share of the crop the piece fills
TONE = {"Gold": "gold tone", "Silver": "silver tone", "Ruby": "ruby red", "Emerald": "emerald green", "Crystal": "crystal clear",
        "Amethyst": "amethyst"}

def load_boxes():
    d = {}
    for line in open(f"{HERE}/boxes.txt"):
        if not line.strip() or line.startswith("#"): continue
        k, *v = line.split(); v = [float(x) for x in v]
        d[k] = dict(box=v[:4], focus=v[4:8] if len(v) >= 8 else v[:4])
    return d

def crop(W, H, focus, aspect, fill, ycen, smin):
    """Crop (x0, y0, w, h) of aspect w/h round the focus box (fractions): the box fills `fill` of the crop, the crop
    is at least `smin` of the photo's width, and the box centre sits `ycen` of the way down where the photo allows."""
    fx0, fy0, fx1, fy1 = focus[0] * W, focus[1] * H, focus[2] * W, focus[3] * H
    cw = max((fx1 - fx0) / fill, (fy1 - fy0) / fill * aspect, smin * W)
    cw = min(cw, W, H * aspect); ch = cw / aspect
    x0 = min(max((fx0 + fx1) / 2 - cw / 2, 0), W - cw); y0 = min(max((fy0 + fy1) / 2 - ycen * ch, 0), H - ch)
    return x0, y0, cw, ch

def cut(src, rect, size, name):
    """Cuts rect from the photo, resizes it to size and saves it; returns its path and scale (above 1 means enlarged)."""
    im = Image.open(src).convert("RGB"); x0, y0, w, h = rect
    out = im.crop((round(x0), round(y0), round(x0 + w), round(y0 + h))).resize(size, Image.LANCZOS)
    scale = size[0] / w
    if scale > 1.05: out = out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=55, threshold=2))
    path = f"{WORK}/{name}.jpg"; out.save(path, quality=94); return path, scale

def to_card(box, W, H, rect, size):
    """The piece's box in output pixels, given the photo size, crop rect and output size."""
    x0, y0, w, h = rect; sx, sy = size[0] / w, size[1] / h
    return [(box[0] * W - x0) * sx, (box[1] * H - y0) * sy, (box[2] * W - x0) * sx, (box[3] * H - y0) * sy]

def lum(path, rect):
    im = Image.open(path).convert("L").crop(tuple(round(v) for v in rect)); return ImageStat.Stat(im).mean[0] / 255

def hit(a, b, m=0):
    return not (a[2] + m <= b[0] or b[2] + m <= a[0] or a[3] + m <= b[1] or b[3] + m <= a[1])

HEAD = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1080px;overflow:hidden;background:#1A1614}
img{display:block}.abs{position:absolute}
.ph{position:absolute;left:0;top:0}
.gt{position:absolute;left:0;right:0;top:0;height:250px}
.gb{position:absolute;left:0;right:0;bottom:0;height:420px}
.nm{position:absolute;font:300 41px/1.12 Jost;letter-spacing:.035em;text-wrap:balance}
.pr{position:absolute;font:400 24px/1 Jost;letter-spacing:.16em;text-transform:uppercase}
.pill{position:absolute;font:600 19px/1 Jost;letter-spacing:.2em;text-transform:uppercase;padding:13px 20px 12px;border-radius:999px;
  background:rgba(255,248,245,.9);color:#1A1614}
.plate{position:absolute;left:50%%;transform:translateX(-50%%);bottom:46px;width:640px;background:#FFF8F5;padding:24px 30px 24px;
  text-align:center;box-shadow:0 14px 40px rgba(20,12,8,.28)}
.plate .lg{width:150px;margin:0 auto 14px}.plate .n{font:400 31px/1.15 Jost;color:#1A1614;letter-spacing:.02em}
.plate .p{font:500 21px/1 Jost;color:#B4513B;letter-spacing:.18em;margin-top:12px;text-transform:uppercase}
.loupe{position:absolute;border-radius:50%%;overflow:hidden;border:9px solid #FFF8F5;
  box-shadow:0 22px 50px rgba(15,9,6,.42),0 0 0 2px rgba(255,248,245,.55)}
.loupe img{width:100%%;height:100%%}
.ltag{position:absolute;font:600 19px/1 Jost;letter-spacing:.2em;text-transform:uppercase;padding:13px 20px 12px;border-radius:999px;
  background:#F0A08F;color:#1A1614;transform:translateX(-50%%);box-shadow:0 6px 16px rgba(0,0,0,.18)}
</style></head><body>
"""

def overlay_colours(dark):
    """Dark photo region: white type on a soft dark gradient. Light region: ink type on a soft paper gradient."""
    if dark: return "#FFFFFF", "logo_white.png", "rgba(18,12,9,%s)", "0 2px 16px rgba(0,0,0,.38)"
    return INK, "logo_ink.png", "rgba(255,248,245,%s)", "none"

def card_a(p, photo, rect, scale, jbox):
    """Full-bleed worn crop. Logo top (centre unless the piece is under it), name and price at the bottom."""
    cands = [(390, 44, 690, 111), (56, 44, 356, 111), (724, 44, 1024, 111)]
    j = [jbox[0] - 26, jbox[1] - 26, jbox[2] + 26, jbox[3] + 26]
    logo = next((c for c in cands if not hit(c, j)), max(cands, key=lambda c: abs((c[0] + c[2]) / 2 - (j[0] + j[2]) / 2)))
    name_r = (70, 890, 1010, 1040); name_top = hit(name_r, j)
    dark_top = lum(photo, logo) < .6; dark_bot = lum(photo, (70, 760, 1010, 1060) if not name_top else (70, 120, 1010, 330)) < .62
    tc, lg, grad, sh = overlay_colours(dark_top); bc, _, gradb, shb = overlay_colours(dark_bot)
    x = f'<img class="ph" src="file://{photo}" width="1080" height="1080">'
    x += f'<div class="gt" style="background:linear-gradient({grad % ".46"},{grad % "0"})"></div>'
    if not name_top:
        x += f'<div class="gb" style="background:linear-gradient(to top,{gradb % ".66"},{gradb % ".26"} 48%,{gradb % "0"})"></div>'
    x += f'<img class="abs" src="file://{BRAND}/{lg}" style="left:{logo[0]}px;top:{logo[1]}px;width:300px;filter:drop-shadow({sh})">'
    nm, pr = html.escape(p["title"]), price_line(p, "worn")
    if name_top:
        x += f'<div class="nm" style="left:80px;right:80px;top:150px;text-align:center;color:{bc};text-shadow:{shb}">{nm}</div>'
        x += f'<div class="pr" style="left:80px;right:80px;top:{150 + 64}px;text-align:center;color:{bc}">{pr}</div>'
    else:
        x += f'<div class="nm" style="left:80px;right:80px;bottom:112px;text-align:center;color:{bc};text-shadow:{shb}">{nm}</div>'
        x += f'<div class="pr" style="left:80px;right:80px;bottom:64px;text-align:center;color:{bc};opacity:.94">{pr}</div>'
    return x, dict(logo=logo, name_top=name_top)

def card_b(p, left, right):
    x = f'<img class="ph" src="file://{left}" width="{(N - GUT) // 2}" height="1080">'
    x += f'<div class="abs" style="left:{(N - GUT) // 2}px;top:0;width:{GUT}px;height:1080px;background:{PAPER}"></div>'
    x += f'<img class="ph" src="file://{right}" style="left:{(N + GUT) // 2}px" width="{(N - GUT) // 2}" height="1080">'
    lt = "Worn" if p["worn"] else "The piece"
    x += f'<div class="pill" style="left:30px;top:30px">{lt}</div><div class="pill" style="right:30px;top:30px">Up close</div>'
    x += (f'<div class="plate"><img class="lg" src="file://{BRAND}/logo_ink.png"><div class="n">{html.escape(p["title"])}</div>'
          f'<div class="p">{price_line(p, "worn")}</div></div>')
    return x

def card_c(p, photo, jbox, loupe_img, alt):
    """Worn photo with the close-up in a magnifier on the side away from the piece, a thin line pointing at it."""
    cx, cy = (jbox[0] + jbox[2]) / 2, (jbox[1] + jbox[3]) / 2; R = 205
    spots = [(262, 318), (818, 318), (262, 742), (818, 742)]
    order = sorted(spots, key=lambda s: -math.hypot(s[0] - cx, s[1] - cy))
    j = [jbox[0] - 30, jbox[1] - 30, jbox[2] + 30, jbox[3] + 30]
    def clear(s): return not hit((s[0] - R - 10, s[1] - R - 10, s[0] + R + 10, s[1] + R + 10), j)
    L = next((s for s in order if clear(s)), order[0])
    top = L[1] < 540; leftside = L[0] < 540
    logo = (724, 44, 1024, 111) if (top and leftside) else (56, 44, 356, 111) if top else (390, 44, 690, 111)
    if top: name = dict(style="left:80px;right:80px;bottom:112px;text-align:center", pr="left:80px;right:80px;bottom:64px;text-align:center", zone=(70, 860, 1010, 1060))
    elif leftside: name = dict(style="left:520px;right:56px;bottom:112px;text-align:right", pr="left:520px;right:56px;bottom:64px;text-align:right", zone=(520, 860, 1024, 1060))
    else: name = dict(style="left:56px;right:520px;bottom:112px;text-align:left", pr="left:56px;right:520px;bottom:64px;text-align:left", zone=(56, 860, 560, 1060))
    tc, lg, grad, sh = overlay_colours(lum(photo, logo) < .6); bc, _, gradb, shb = overlay_colours(lum(photo, name["zone"]) < .62)
    x = f'<img class="ph" src="file://{photo}" width="1080" height="1080">'
    x += f'<div class="gt" style="background:linear-gradient({grad % ".42"},{grad % "0"})"></div>'
    x += f'<div class="gb" style="background:linear-gradient(to top,{gradb % ".62"},{gradb % ".22"} 48%,{gradb % "0"})"></div>'
    d = math.hypot(cx - L[0], cy - L[1]); rj = max(jbox[2] - jbox[0], jbox[3] - jbox[1]) / 2 + 16
    svg = ""
    if d > R + rj + 46:
        ux, uy = (cx - L[0]) / d, (cy - L[1]) / d
        x1, y1, x2, y2 = L[0] + ux * (R + 12), L[1] + uy * (R + 12), cx - ux * (rj + 6), cy - uy * (rj + 6)
        svg = (f'<svg class="abs" style="left:0;top:0" width="1080" height="1080"><g fill="none" stroke="#FFF8F5" stroke-width="3" '
               f'style="filter:drop-shadow(0 1px 3px rgba(0,0,0,.45))"><line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}"/>'
               f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{rj:.0f}"/></g></svg>')
    x += svg
    x += f'<div class="loupe" style="left:{L[0] - R}px;top:{L[1] - R}px;width:{2 * R}px;height:{2 * R}px"><img src="file://{loupe_img}"></div>'
    x += f'<div class="ltag" style="left:{L[0]}px;top:{L[1] + R - 16}px">Up close</div>'
    x += f'<img class="abs" src="file://{BRAND}/{lg}" style="left:{logo[0]}px;top:{logo[1]}px;width:300px;filter:drop-shadow({sh})">'
    x += f'<div class="nm" style="{name["style"]};color:{bc};text-shadow:{shb}">{html.escape(p["title"])}</div>'
    x += f'<div class="pr" style="{name["pr"]};color:{bc};opacity:.94">{price_line(p, "alt" if alt else "worn")}</div>'
    return x, dict(loupe=L)

def price_line(p, kind):
    pr = p.get(f"{kind}_price") or p["price"]; c = p.get(f"{kind}_colour")
    s = f"₹{pr:,}"
    return s + (f" · {TONE.get(c, c)}" if c else "")

def build(rows, boxes):
    os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    jobs, meta = [], []
    for p in rows:
        h = p["handle"]; fill = FILL.get(p["type"], .6)
        worn, close = f"{SRC}/full/{h}-worn.jpg", f"{SRC}/full/{h}-close.jpg"
        W, H = Image.open(worn).size; CW, CH = Image.open(close).size
        has = bool(p["worn"]); b = boxes.get(f'{p["n"]}w') if has else None
        bx = b["box"] if b else [.2, .2, .8, .8]; fo = b["focus"] if b else [.25, .25, .75, .75]
        # A: tight worn crop (product shot when there is no worn photo)
        ra = crop(W, H, fo if p["type"] in ("Earrings", "Ring") else bx, 1, fill, .47, .56)
        pa, sa = cut(worn, ra, (N, N), f"{h}-Aph"); ja = to_card(bx, W, H, ra, (N, N)) if has else [9999] * 4
        xa, la = card_a(p, pa, ra, sa, ja)
        # B: worn panel and close-up panel
        pw = (N - GUT) // 2
        rbl = crop(W, H, fo, pw / N, min(.8, fill * 1.25), .46, .34)
        pl, sl = cut(worn, rbl, (pw, N), f"{h}-B1")
        rbr = crop(CW, CH, [.3, .3, .7, .7], pw / N, .7, .5, .42)
        prr, sr = cut(close, rbr, (pw, N), f"{h}-B2")
        xb = card_b(p, pl, prr)
        # C: second photo or a wide crop, with the close-up in the loupe
        if has:
            alt = bool(p.get("alt")) and f'{p["n"]}a' in boxes
            src = f"{SRC}/full/{h}-alt.jpg" if alt else worn
            bc = boxes[f'{p["n"]}a'] if alt else b
            AW, AH = Image.open(src).size
            rc = crop(AW, AH, bc["box"], 1, fill * (.8 if alt else .62), .5, .7 if not alt else .56)
            pc, sc = cut(src, rc, (N, N), f"{h}-Cph"); jc = to_card(bc["box"], AW, AH, rc, (N, N))
            lsrc = f"{SRC}/full/{h}-altclose.jpg" if alt and p.get("alt_close") else close
            LW, LH = Image.open(lsrc).size; rl = crop(LW, LH, [.3, .3, .7, .7], 1, .62, .5, .5)
            lp, _ = cut(lsrc, rl, (410, 410), f"{h}-L")
            xc, lc = card_c(p, pc, jc, lp, alt)
        else:
            rc = crop(CW, CH, [.15, .15, .85, .85], 1, .9, .5, .8)
            pc, sc = cut(close, rc, (N, N), f"{h}-Cph")
            xc, lc = card_a(p, pc, rc, sc, [9999, 9999, 9999, 9999]); alt = False
        for k, body in (("A", xa), ("B", xb), ("C", xc)):
            open(f"{WORK}/{h}-{k}.html", "w").write(HEAD % dict(f=FONTS) + body + "</body></html>")
            jobs.append(f"{h}-{k}:{N}:{N}")
        meta.append(dict(handle=h, title=p["title"], type=p["type"], n=p["n"], worn=has, alt=alt, price=p["price"], url=p["url"],
                         alt_url=p.get("alt_url"), scale_a=round(sa, 2), scale_c=round(sc, 2), jbox_a=[round(v) for v in ja]))
    env = dict(os.environ, NODE_PATH="/opt/node-tools/node_modules")
    for i in range(0, len(jobs), 60):
        subprocess.run(["node", f"{HERE}/render.cjs", WORK, *jobs[i:i + 60]], check=True, env=env)
    for j in jobs:
        k = j.split(":")[0]; os.replace(f"{WORK}/{k}.jpg", f"{OUT}/{k}.jpg")
    return meta

if __name__ == "__main__":
    rows = json.load(open(f"{SRC}/products_pick.json")); want = set(sys.argv[1:])
    if want: rows = [r for r in rows if r["handle"] in want]
    meta = build(rows, load_boxes())
    old = {m["handle"]: m for m in (json.load(open(f"{OUT}/cards.json")) if os.path.exists(f"{OUT}/cards.json") else [])}
    old.update({m["handle"]: m for m in meta})
    json.dump(sorted(old.values(), key=lambda m: m["n"]), open(f"{OUT}/cards.json", "w"), indent=1, ensure_ascii=False)
    print(len(meta), "products,", 3 * len(meta), "cards ->", OUT)
