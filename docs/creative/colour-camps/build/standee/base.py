# -*- coding: utf-8 -*-
"""Shared print scaffolding for the exhibition roll-up standees.
Pages are laid out in CSS px at 96 px/inch, so the PDF comes out at exact physical size; photographs are
embedded at their own resolution (JPEG for plates, PNG only where the cut-out needs alpha)."""
import os, sys, json, math, html, asyncio, re
import numpy as np
from PIL import Image, ImageFont

SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
sys.path.insert(0, f"{SP}/sets2")
from core import fontfaces, ROWS, VEL            # local webfonts + live price rows
from campcopy import COPY, ORDER

CM = 96 / 2.54                                    # CSS px per centimetre
SIZES = [("2x5ft", 61.0, 152.4), ("2.5x6ft", 76.2, 182.6), ("3x6ft", 91.4, 182.6), ("4x6ft", 122.0, 182.6)]
ROOT = f"{SP}/standee"; AS = f"{ROOT}/assets"; OUT = f"{ROOT}/out"
os.makedirs(AS, exist_ok=True); os.makedirs(OUT, exist_ok=True)
PLATES = f"{SP}/cc/shoot/plates"; CUTS = f"{SP}/cc/cutouts"
FINAL = json.load(open(f"{SP}/cc/shoot/final_v2.json"))
URL = "nairaflore.com"


def E(s): return html.escape(str(s))
def price(sku): return "₹" + f"{int(round(ROWS[sku]['price'])):,}"
def title(sku): return ROWS[sku]["title"]


def fit(text, target_px, track=-0.01, font=VEL):
    f = ImageFont.truetype(font, 400); w = f.getlength(text) + track * 400 * (len(text) - 1)
    return target_px * 400 / w


# ------------------------------------------------------------------ images
_A = {}
def asset_plate(path, key, box=None, q=90):
    """plate (or a region of it) as JPEG; returns a record in ORIGINAL plate pixel coordinates"""
    k = (path, key, box)
    if k in _A: return _A[k]
    im = Image.open(path).convert("RGB"); PW, PH = im.size
    if box:
        box = tuple(int(round(v)) for v in (max(0, box[0]), max(0, box[1]), min(PW, box[2]), min(PH, box[3])))
        im = im.crop(box); ox, oy = box[0], box[1]
    else:
        ox = oy = 0
    if box: key = f"{key}_{abs(hash(box)) % 99991}"
    out = f"{AS}/{key}.jpg"; im.save(out, quality=q, optimize=True, subsampling=0)
    r = dict(path=out, ox=ox, oy=oy, w=im.size[0], h=im.size[1], PW=PW, PH=PH); _A[k] = r; return r


def asset_cut(path, key, pad=6, shadow=(0.0, 0.006, 0.012, 0.20)):
    """background-removed cut-out cropped to its alpha box, PNG, with a soft drop shadow BAKED into it (CSS filters make
    Chromium rasterise the element at ~2.4x in the PDF). shadow = (dx, dy, blur, opacity) as fractions of the cut width."""
    from PIL import ImageFilter
    k = (path, key, shadow)
    if k in _A: return _A[k]
    im = Image.open(path).convert("RGBA"); PW, PH = im.size
    a = np.asarray(im)[..., 3]; ys, xs = np.where(a > 8)
    cw = int(xs.max() - xs.min())
    extra = int(cw * (shadow[2] * 3 + abs(shadow[1]) + abs(shadow[0]))) + pad if shadow else pad
    box = (max(0, xs.min() - extra), max(0, ys.min() - extra), min(PW, xs.max() + extra + 1), min(PH, ys.max() + extra + 1))
    c = im.crop(box)
    if shadow:
        dx, dy, bl, op = shadow
        al = c.split()[3]
        sh = Image.new("L", c.size, 0); sh.paste(al, (int(dx * cw), int(dy * cw)))
        sh = sh.filter(ImageFilter.GaussianBlur(float(max(1.0, bl * float(cw))))).point(lambda v: int(v * op))
        base_ = Image.new("RGBA", c.size, (25, 15, 30, 0)); base_.putalpha(sh)
        c = Image.alpha_composite(base_, c)
    out = f"{AS}/{key}{'_sh' if shadow else ''}.png"; c.save(out, optimize=True)
    ys2, xs2 = np.where(a > 128)
    r = dict(path=out, ox=box[0], oy=box[1], w=c.size[0], h=c.size[1], PW=PW, PH=PH,
             bbox=(xs2.min(), ys2.min(), xs2.max(), ys2.max())); _A[k] = r; return r


_DS = {}
def _scaled(path, f):
    """a copy of `path` at factor f (only ever smaller) so the PDF never carries more than ~1.5x the printed pixels"""
    f = round(f, 2)
    if f >= 0.95: return path
    k = (path, f)
    if k in _DS: return _DS[k]
    im = Image.open(path); nw, nh = max(1, int(im.size[0] * f)), max(1, int(im.size[1] * f))
    out = path[:-4] + f"_x{int(f*100)}" + path[-4:]
    im = im.resize((nw, nh), Image.LANCZOS)
    if out.endswith(".jpg"): im.convert("RGB").save(out, quality=90, optimize=True, subsampling=0)
    else: im.save(out, optimize=True)
    _DS[k] = out; return out


def img(rec, s, tx, ty, z=1, extra=""):
    """absolute <img> for a record under the mapping page = t + s*plate"""
    src = _scaled(rec["path"], min(1.0, s * 1.5))
    extra = re.sub(r"filter:\s*drop-shadow\([^;]*\)\)?;?", "", extra)
    return (f'<img src="{src}" style="position:absolute;left:{tx + s * rec["ox"]:.2f}px;top:{ty + s * rec["oy"]:.2f}px;'
            f'width:{s * rec["w"]:.2f}px;height:{s * rec["h"]:.2f}px;z-index:{z};{extra}">')


def cover(rec_region, x, y, w, h, s, tx, ty):
    """clamp the translation so the plate region covers the rect (x,y,w,h) entirely"""
    L = rec_region["ox"]; T = rec_region["oy"]; R = L + rec_region["w"]; B = T + rec_region["h"]
    s = max(s, w / (R - L), h / (B - T))
    tx = min(max(tx, x + w - s * R), x - s * L)
    ty = min(max(ty, y + h - s * B), y - s * T)
    return s, tx, ty


def clipbox(x, y, w, h, inner, z=1, radius=0, extra=""):
    """a clipping window at page (x,y,w,h); `inner` is html positioned in PAGE coordinates"""
    return (f'<div style="position:absolute;left:{x:.2f}px;top:{y:.2f}px;width:{w:.2f}px;height:{h:.2f}px;overflow:hidden;'
            f'border-radius:{radius}px;z-index:{z};{extra}"><div style="position:absolute;left:{-x:.2f}px;top:{-y:.2f}px">{inner}</div></div>')


def pop_tile(sku, x, y, w, h, fill=0.74, pop=0.16, z=3, radius=0, frame_extra="", cut_z=None, shadow=True, plate=None, cutp=None, side=0.02, anchor_y=None):
    """product window: the plate is clipped to the window, the cut-out rises `pop` of its height above the top edge.
    Returns html. fill = product width as a fraction of the window width (height-limited too)."""
    plate = plate or FINAL[f"{sku}|S1"]
    cutp = cutp or cut_for(plate)
    C = asset_cut(cutp, f"cut_{os.path.basename(cutp)[:-4]}")
    bx0, by0, bx1, by1 = C["bbox"]; bw, bh = bx1 - bx0, by1 - by0
    s = min(fill * w / bw, 0.88 * h / ((1 - pop) * bh))
    ph = s * bh
    tx = x + w / 2 - s * (bx0 + bx1) / 2
    ty = (y - pop * ph) - s * by0
    # plate region around the product (generous), as JPEG
    ex = 0.9
    R = asset_plate(plate, f"pl_{os.path.basename(plate)[:-4]}", (bx0 - ex * bw, by0 - ex * bh, bx1 + ex * bw, by1 + ex * bh))
    s2, tx2, ty2 = cover(R, x, y, w, h, s, tx, ty)
    if abs(s2 - s) > 1e-6 or abs(ty2 - ty) > 0.5 or abs(tx2 - tx) > 0.5:
        s, tx, ty = s2, tx2, ty2
    plate_html = img(R, s, tx, ty, z=1)
    top_room = max(0.0, y - (ty + s * by0)) + 4
    cz = cut_z if cut_z is not None else z + 1
    sh = ""
    cut_html = img(C, s, tx, ty, z=1, extra=sh)
    return (clipbox(x, y, w, h, plate_html, z=z, radius=radius, extra=frame_extra) +
            clipbox(x - w * side, y - top_room, w * (1 + 2 * side), h + top_room, cut_html, z=cz))


def cut_for(plate):
    b = os.path.basename(plate)[:-4]
    for cand in (b, b[:-1] if b.endswith("g") else b, b.rstrip("cg")):
        p = f"{CUTS}/{cand}.png"
        if os.path.exists(p): return p
    raise FileNotFoundError(plate)


def logo(color, key):
    """brand wordmark (from the site's footer asset, 1642 px) recoloured"""
    out = f"{AS}/logo_{key}.png"
    if not os.path.exists(out):
        im = Image.open(f"{AS}/logo_src.png").convert("RGBA"); a = im.split()[3]
        c = Image.new("RGBA", im.size, color); c.putalpha(a); c.save(out, optimize=True)
    return out


def qr_svg(url, ink):
    import segno
    q = segno.make(url, error="m")
    return q.svg_inline(scale=1, border=0, dark=ink, light=None, omitsize=True)


# ------------------------------------------------------------------ devices (scalable versions of the ad devices)
def plu_svg(w, price_txt, top_txt, bot_txt, code, col, ink):
    k = w / 260; h = w * 0.72; rx, ry = w / 2 - 4 * k, h / 2 - 4 * k; cx, cy = w / 2, h / 2; u = f"{code}{int(w)}"
    return f'''<svg width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {w:.1f} {h:.1f}" style="overflow:visible;display:block">
<defs><path id="pt{u}" d="M {cx-rx*0.78:.1f},{cy+2*k:.1f} A {rx*0.78:.1f},{ry*0.74:.1f} 0 0,1 {cx+rx*0.78:.1f},{cy+2*k:.1f}"/>
<path id="pb{u}" d="M {cx-rx*0.80:.1f},{cy-4*k:.1f} A {rx*0.80:.1f},{ry*0.80:.1f} 0 0,0 {cx+rx*0.80:.1f},{cy-4*k:.1f}"/>
<linearGradient id="gl{u}" x1="0" y1="0" x2="0.6" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".30"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<ellipse cx="{cx+3*k:.1f}" cy="{cy+5*k:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#000" fill-opacity=".10"/>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{col}"/>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx-9*k:.1f}" ry="{ry-9*k:.1f}" fill="none" stroke="{ink}" stroke-width="{1.6*k:.2f}" stroke-opacity=".85"/>
<text font-family="JetBrains Mono" font-size="{w*0.052:.1f}" letter-spacing="{2.4*k:.1f}" fill="{ink}"><textPath href="#pt{u}" startOffset="50%" text-anchor="middle">{E(top_txt)}</textPath></text>
<text x="{cx:.1f}" y="{cy+w*0.07:.1f}" text-anchor="middle" font-family="Jost" font-weight="600" font-size="{w*0.20:.1f}" fill="{ink}">{E(price_txt)}</text>
<text font-family="JetBrains Mono" font-size="{w*0.046:.1f}" letter-spacing="{1.8*k:.1f}" fill="{ink}"><textPath href="#pb{u}" startOffset="50%" text-anchor="middle">{E(bot_txt)}</textPath></text>
<text x="{cx:.1f}" y="{cy+ry*0.58:.1f}" text-anchor="middle" font-family="JetBrains Mono" font-size="{w*0.040:.1f}" letter-spacing="{1.5*k:.1f}" fill="{ink}" fill-opacity=".8">PLU {E(code)}</text>
<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="url(#gl{u})"/>
</svg>'''


def perf_mask(uid, w, h, r, step):
    holes = []
    n = max(2, int(round(w / step)))
    for i in range(n + 1): x = i * w / n; holes += [(x, 0), (x, h)]
    m = max(2, int(round(h / step)))
    for j in range(m + 1): y = j * h / m; holes += [(0, y), (w, y)]
    hs = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#000"/>' for x, y in holes)
    return f'<mask id="perf{uid}"><rect x="0" y="0" width="{w:.1f}" height="{h:.1f}" fill="#fff"/>{hs}</mask>'


def stamp_paper(x, y, w, h, paper, uid, z=2, shadow=True):
    r = min(w, h) * 0.018 + 3; step = r * 2.9
    o = w * 0.006
    shade = (f'<g transform="translate({o:.1f},{o*1.6:.1f})" opacity=".13"><rect x="0" y="0" width="{w:.1f}" height="{h:.1f}" fill="#2a1840" mask="url(#perf{uid})"/></g>' if shadow else "")
    return (f'<svg style="position:absolute;left:{x:.1f}px;top:{y:.1f}px;overflow:visible;z-index:{z}" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {w:.1f} {h:.1f}">'
            f'<defs>{perf_mask(uid, w, h, r, step)}</defs>{shade}<rect x="0" y="0" width="{w:.1f}" height="{h:.1f}" fill="{paper}" mask="url(#perf{uid})"/></svg>')


def postmark_svg(D, ink, word, waves_len, uid, sw=None):
    """round date-stamp cancellation, diameter D, with wavy lines running `waves_len` px to the right"""
    r = D / 2 - 4; cx = cy = D / 2; sw = sw or D * 0.012
    wl = "".join(f'<path d="M {cx + r*0.55:.1f},{cy - r*0.62 + i*r*0.41:.1f} ' +
                 " ".join(f"q {D*0.09:.1f},{-D*0.05:.1f} {D*0.18:.1f},0 q {D*0.09:.1f},{D*0.05:.1f} {D*0.18:.1f},0" for _ in range(int(waves_len / (D * 0.36)) + 1)) +
                 f'" fill="none" stroke="{ink}" stroke-width="{sw*1.1:.1f}" stroke-linecap="round"/>' for i in range(4))
    return f'''<svg width="{D + waves_len:.1f}" height="{D:.1f}" viewBox="0 0 {D + waves_len:.1f} {D:.1f}" style="overflow:visible;display:block">
<defs><path id="pm{uid}" d="M {cx-r*0.76:.1f},{cy:.1f} a {r*0.76:.1f},{r*0.76:.1f} 0 1,1 {r*1.52:.1f},0 a {r*0.76:.1f},{r*0.76:.1f} 0 1,1 {-r*1.52:.1f},0"/></defs>
<g opacity=".82"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{ink}" stroke-width="{sw*1.4:.1f}"/>
<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*0.56:.1f}" fill="none" stroke="{ink}" stroke-width="{sw*0.8:.1f}"/>
<text font-family="JetBrains Mono" font-size="{r*0.155:.1f}" letter-spacing="{r*0.02:.1f}" fill="{ink}"><textPath href="#pm{uid}" startOffset="0">NAIRAFLORE.COM · NAIRA PETITE · THE LILAC ISSUE ·</textPath></text>
<text x="{cx:.1f}" y="{cy+r*0.13:.1f}" text-anchor="middle" font-family="Velista" font-size="{r*0.36:.1f}" fill="{ink}">{E(word)}</text>
{wl}</g></svg>'''


# ------------------------------------------------------------------ page + render
PAGE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
@page{size:%(wcm).2fcm %(hcm).2fcm;margin:0}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{-webkit-font-smoothing:antialiased;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{position:relative;width:%(W)dpx;height:%(H)dpx;overflow:hidden}
.abs{position:absolute}
.vel{font-family:'Velista';font-weight:500;line-height:.8;white-space:nowrap}
.mono{font-family:'JetBrains Mono';text-transform:uppercase}
.jost{font-family:'Jost';font-weight:600;text-transform:uppercase}
.ital{font-family:'Cormorant Garamond';font-style:italic;font-weight:500}
svg.segno{width:100%%;height:100%%;display:block}
"""


def page_html(wcm, hcm, body, bg):
    W, H = int(wcm * CM), int(hcm * CM)
    css = PAGE_CSS % dict(wcm=wcm, hcm=hcm, W=W, H=H)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{fontfaces()}{css}</style></head>"
            f"<body><div class='pg' style='background:{bg}'>{body}</div></body></html>")


async def render_all(jobs, pdf=True, png=True):
    """jobs: list of (name, wcm, hcm, html). Writes out/<name>.html/.pdf/.png"""
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
        for name, wcm, hcm, doc in jobs:
            W, H = int(wcm * CM), int(hcm * CM)
            fn = f"{OUT}/{name}.html"; open(fn, "w").write(doc)
            pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            await pg.goto("file://" + fn); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(600)
            if png: await pg.screenshot(path=f"{OUT}/{name}.png")
            if pdf: await pg.pdf(path=f"{OUT}/{name}.pdf", width=f"{wcm}cm", height=f"{hcm}cm", print_background=True,
                                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, prefer_css_page_size=True)
            await pg.close()
        await b.close()
