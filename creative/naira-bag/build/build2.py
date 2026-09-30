#!/usr/bin/env python3
"""
NAIRA print artwork, version 2: bag front, bag back, full bag sheet, and the floral card.

  bag face   6 x 9.5 in  (+0.125 bleed -> 6.25 x 9.75 in, 1875 x 2925 px @ 300 dpi)
  bag sheet  16.75 x 11.2 in trim (+bleed -> 17 x 11.45 in), for reference / single-image upload
  card       2.77 x 2.76 in (+0.125 bleed -> 3.02 x 3.01 in, 906 x 903 px @ 300 dpi)

Layers, bottom to top:
  1. ground: cream, with the website's own watercolour leaf sprigs (upscaled from the site
     assets) laid as a quiet half-drop repeat - rasterised once in PIL at 300 dpi and embedded
  2. corner clusters: the card's tulips, redrawn (five petals, buds, tulip blades)
  3. the lockup: NAIRA in its own colours (sage-blue letters, blush flower), the eyebrow
     "[ 18k gold coated · rhodium coated ]", a short sage rule, "made to stay gold."
  4. back face only: a QR to nairaflore.com/jewellery with its caption
"""
import base64, io, pathlib, sys, segno
import numpy as np
from PIL import Image
from motifs import *

ROOT = pathlib.Path(__file__).parent
FONTS = ROOT.parent / "fonts"
OUT = ROOT / "out2"; OUT.mkdir(exist_ok=True)
DPI = 300
BLEED = 0.125
FACE_W, FACE_H = 6.0, 9.5
SHEET_W, SHEET_H = 16.75, 11.2
CARD_W, CARD_H = 2.77, 2.76
FRONT_X, BACK_X = 2.0, 10.0                  # face origins on the sheet (trim coords)
GLUE_X = 16.0
HANDLE_W, HANDLE_H, HANDLE_TOP, HANDLE_ARC = 2.3, 1.0, 1.05, 0.6
QR_URL = "https://nairaflore.com/jewellery"
EYEBROW = "[ 18k gold coated · rhodium coated ]"
TAG = "made to stay gold."
PATTERN_OP = 0.34                            # strength of the leaf repeat
Image.MAX_IMAGE_PIXELS = None


def b64(p):
    return base64.b64encode(pathlib.Path(p).read_bytes()).decode()


def b64img(im, fmt="PNG", **kw):
    buf = io.BytesIO(); im.save(buf, fmt, **kw)
    return base64.b64encode(buf.getvalue()).decode()


# ---------------------------------------------------------------- ground: cream + the site's leaves
_SPRIGS = None


def sprigs():
    """The upscaled site sprigs as float multiply-masks (1 = paper, <1 = pigment), RGB."""
    global _SPRIGS
    if _SPRIGS is None:
        out = []
        for name in ("sprig1", "sprig2"):
            im = Image.open(ROOT / "up" / f"{name}_4k.png").convert("RGB")
            out.append(im)
        _SPRIGS = out
    return _SPRIGS


def ground(w_in, h_in, ox=0.0, oy=0.0, k=1.0, seed=7):
    """Cream paper with the leaf repeat. (ox, oy) is where this page sits in the shared pattern
    space (inches), so faces cut from the sheet and the sheet itself carry the same pattern."""
    W, H = int(round(w_in * DPI)), int(round(h_in * DPI))
    cream = np.array([int(CREAM[i:i+2], 16) for i in (1, 3, 5)], dtype=np.float32)
    canvas = np.ones((H, W, 3), dtype=np.float32)            # multiply accumulator, 1 = paper
    rng = np.random.default_rng(seed)
    cell = 2.35 * k                                           # inches
    sizes = (2.0 * k, 1.6 * k)                                # sprig long side, inches
    sp = sprigs()
    # a fixed lattice in pattern space so every page agrees; jitter is a deterministic hash
    def jit(i, j, n):
        return (np.sin(i * 12.9898 + j * 78.233 + n * 37.719) * 43758.5453) % 1.0
    i0, i1 = int((ox - 3) // cell), int((ox + w_in + 3) // cell) + 1
    j0, j1 = int((oy - 3) // cell), int((oy + h_in + 3) // cell) + 1
    for j in range(j0, j1):
        for i in range(i0, i1):
            cx = (i + 0.5 + (0.5 if j % 2 else 0)) * cell + (jit(i, j, 1) - .5) * cell * .35
            cy = (j + 0.5) * cell + (jit(i, j, 2) - .5) * cell * .35
            which = (i + j) % 2
            im = sp[which]
            size = sizes[which] * (0.85 + 0.3 * jit(i, j, 3))
            rot = jit(i, j, 4) * 360
            s = im.resize((int(size * DPI), int(size * DPI)), Image.LANCZOS)
            s = s.rotate(rot, resample=Image.BICUBIC, expand=True, fillcolor=(255, 255, 255))
            a = np.asarray(s).astype(np.float32) / 255.0
            a = 1.0 - PATTERN_OP * (1.0 - a)                    # fade the pigment
            px, py = int((cx - ox) * DPI - s.width / 2), int((cy - oy) * DPI - s.height / 2)
            x0, y0 = max(px, 0), max(py, 0)
            x1, y1 = min(px + s.width, W), min(py + s.height, H)
            if x1 <= x0 or y1 <= y0:
                continue
            canvas[y0:y1, x0:x1] *= a[y0 - py:y1 - py, x0 - px:x1 - px]
    rgb = np.clip(canvas * cream[None, None, :], 0, 255).astype(np.uint8)
    return Image.fromarray(rgb, "RGB")


# ---------------------------------------------------------------- the lockup
LOGO = b64(ROOT / "assets" / "naira-logo-brand.png")
_lg = Image.open(ROOT / "assets" / "naira-logo-brand.png"); LOGO_W, LOGO_H = _lg.size


def lockup(cx, ly, wm_w, k=1.0):
    """Eyebrow, wordmark, rule, tagline centred on cx; ly is the wordmark's top edge."""
    wm_h = wm_w * LOGO_H / LOGO_W
    return [f'<text x="{cx}" y="{ly - .28*k}" class="eyebrow" text-anchor="middle">{EYEBROW}</text>',
            f'<image href="data:image/png;base64,{LOGO}" x="{cx - wm_w/2}" y="{ly}" width="{wm_w}" height="{wm_h}" preserveAspectRatio="xMidYMid meet"/>',
            f'<rect x="{cx - .3*k}" y="{ly + wm_h + .22*k}" width="{.6*k}" height="{.016*k}" fill="{LOGO_SAGE}"/>',
            f'<text x="{cx}" y="{ly + wm_h + .68*k}" class="tag" text-anchor="middle">{TAG}</text>']


def qr_block(cx, top, size=0.85):
    q = segno.make(QR_URL, error="m")
    n = q.symbol_size(scale=1, border=0)[0]
    d = "".join(f"M{x},{y}h1v1h-1z" for y, row in enumerate(q.matrix_iter(scale=1, border=0)) for x, v in enumerate(row) if v)
    m = size / n
    return [f'<ellipse cx="{cx}" cy="{top + size/2 + .1}" rx="1.35" ry="1.05" fill="url(#halo)"/>',
            f'<rect x="{cx - size/2 - 4*m}" y="{top - 4*m}" width="{size + 8*m}" height="{size + 8*m}" fill="{CREAM}"/>',
            f'<g transform="translate({cx - size/2},{top}) scale({m})"><path d="{d}" fill="{INK}"/></g>',
            f'<text x="{cx}" y="{top + size + .3}" class="qr" text-anchor="middle">scan · nairaflore.com/jewellery</text>']


def face_layers(x0, y0, qr=False, k=1.0):
    """Everything drawn on one 6 x 9.5 face whose trim top-left is (x0, y0) in page inches."""
    w, h = FACE_W * k, FACE_H * k
    cx = x0 + w / 2
    ly = y0 + 3.55 * k                                       # wordmark top
    g = [f'<ellipse cx="{cx}" cy="{ly + .3*k}" rx="{2.7*k}" ry="{1.75*k}" fill="url(#halo)"/>']
    for kind in ("tl", "tr", "br", "bl"):
        g += cluster(kind, x0, y0, w, h, k)
    g += [dots([(cx - 1.95*k, y0 + 3.0*k), (cx + 2.15*k, y0 + 2.7*k), (cx - 2.4*k, y0 + 6.2*k), (cx + 2.25*k, y0 + 6.6*k),
                (cx - 1.15*k, y0 + 7.35*k), (cx + .95*k, y0 + 7.65*k), (cx + 2.55*k, y0 + 5.1*k), (cx - 2.6*k, y0 + 4.6*k)], r=.02*k)]
    g += lockup(cx, ly, 3.5 * k, k)
    if qr:
        g += qr_block(cx, y0 + h - 2.4)
    return g


def card_layers(x0, y0):
    """The card: the same grammar, laid out for a 2.77 in square."""
    w, h, k = CARD_W, CARD_H, 0.34
    cx = x0 + w / 2
    wm_w = 1.45
    wm_h = wm_w * LOGO_H / LOGO_W
    top = y0 + .80
    g = [f'<ellipse cx="{cx}" cy="{y0 + 1.2}" rx="1.15" ry=".68" fill="url(#halo)"/>']
    for kind in ("tl", "tr", "br", "bl"):
        g += cluster(kind, x0, y0, w, h, k)
    g += [dots([(cx - .95, y0 + 1.1), (cx + 1.0, y0 + .95), (cx - 1.05, y0 + 1.9), (cx + .55, y0 + 2.05), (cx - .3, y0 + 2.2), (cx + 1.05, y0 + 1.75)], r=.011)]
    g += [f'<text x="{cx}" y="{top - .11}" class="eyebrow" text-anchor="middle">{EYEBROW}</text>',
          f'<image href="data:image/png;base64,{LOGO}" x="{cx - wm_w/2}" y="{top}" width="{wm_w}" height="{wm_h}" preserveAspectRatio="xMidYMid meet"/>',
          f'<rect x="{cx - .2}" y="{top + wm_h + .11}" width=".4" height=".011" fill="{LOGO_SAGE}"/>',
          f'<text x="{cx}" y="{top + wm_h + .43}" class="tag" text-anchor="middle">{TAG}</text>']
    return g


# ---------------------------------------------------------------- pages
def style(k=1.0):
    EB_SIZE, EB_TRACK = (.13, .04) if k == 1.0 else (.07, .016)
    return f"""<style>
  @font-face{{font-family:"Cormorant";src:url(data:font/woff2;base64,{b64(FONTS/'Cormorant-400-italic.woff2')}) format("woff2");font-style:italic;font-weight:400}}
  @font-face{{font-family:"JostF";src:url(data:font/woff2;base64,{b64(FONTS/'Jost-400.woff2')}) format("woff2");font-weight:400}}
  @font-face{{font-family:"JostM";src:url(data:font/woff2;base64,{b64(FONTS/'Jost-500.woff2')}) format("woff2");font-weight:500}}
  .eyebrow{{font-family:"JostF",sans-serif;font-size:{EB_SIZE}px;letter-spacing:{EB_TRACK}px;fill:{INK}}}
  .tag{{font-family:"Cormorant",serif;font-style:italic;font-size:{.42*k if k == 1.0 else .2}px;fill:{INK};letter-spacing:{.006*k}px}}
  .qr{{font-family:"JostM",sans-serif;font-size:.105px;letter-spacing:.028px;fill:{INK}}}
  .g{{font-family:"JostM",sans-serif;font-size:.11px;fill:#C0392B;letter-spacing:.02px}}
</style>"""


def defs():
    return f"""<defs><radialGradient id="halo">
    <stop offset="0" stop-color="{CREAM}" stop-opacity="1"/><stop offset=".6" stop-color="{CREAM}" stop-opacity="1"/><stop offset="1" stop-color="{CREAM}" stop-opacity="0"/>
  </radialGradient></defs>"""


def page(kind, guides=False):
    """Returns (svg, width_in, height_in). kind: front | back | sheet | card."""
    if kind in ("front", "back"):
        W, H = FACE_W + 2 * BLEED, FACE_H + 2 * BLEED
        ox = (FRONT_X if kind == "front" else BACK_X) - BLEED            # pattern-space origin
        bg = ground(W, H, ox, -BLEED)
        body = face_layers(BLEED, BLEED, qr=(kind == "back"))
        k = 1.0
    elif kind == "sheet":
        W, H = SHEET_W + 2 * BLEED, SHEET_H + 2 * BLEED
        bg = ground(W, H, -BLEED, -BLEED)
        body = face_layers(FRONT_X + BLEED, BLEED) + face_layers(BACK_X + BLEED, BLEED, qr=True)
        body.append(f'<rect x="{GLUE_X + BLEED}" y="0" width="{W - GLUE_X - BLEED}" height="{H}" fill="{CREAM}"/>')
        k = 1.0
    elif kind == "card":
        W, H = CARD_W + 2 * BLEED, CARD_H + 2 * BLEED
        bg = ground(W, H, 30.0, 30.0, k=0.46, seed=7)                   # its own patch of pattern space
        body = card_layers(BLEED, BLEED)
        k = 0.46
    else:
        raise ValueError(kind)
    fmt = "JPEG" if kind != "card" else "PNG"
    kw = {"quality": 94, "subsampling": 0} if fmt == "JPEG" else {"optimize": True}
    bgdata = b64img(bg, fmt, **kw)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}in" height="{H}in" viewBox="0 0 {W} {H}">',
             defs(), style(k),
             f'<image href="data:image/{fmt.lower()};base64,{bgdata}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/>']
    parts += body
    if guides:
        pink = '#E0457B'
        parts.append(f'<rect x="{BLEED}" y="{BLEED}" width="{W-2*BLEED}" height="{H-2*BLEED}" fill="none" stroke="{pink}" stroke-width=".014"/>')
        if kind in ("front", "back", "sheet"):
            faces = [BLEED] if kind != "sheet" else [FRONT_X + BLEED, BACK_X + BLEED]
            for fx in faces:
                cx, top, hw = fx + 3, BLEED + HANDLE_TOP, HANDLE_W / 2
                parts.append(f'<path d="M{cx-hw},{top+HANDLE_H} L{cx-hw},{top+HANDLE_ARC} A{hw},{HANDLE_ARC} 0 0 1 {cx+hw},{top+HANDLE_ARC} L{cx+hw},{top+HANDLE_H} Z" fill="none" stroke="{pink}" stroke-width=".014" stroke-dasharray="0.05,0.04"/>')
            if kind == "sheet":
                for x in (1, 2, 8, 9, 10, 16):
                    parts.append(f'<line x1="{x+BLEED}" y1="0" x2="{x+BLEED}" y2="{H}" stroke="#2AA6A0" stroke-width=".012" stroke-dasharray="0.06,0.05"/>')
                for y in (9.5, 8.5):
                    parts.append(f'<line x1="0" y1="{y+BLEED}" x2="{W}" y2="{y+BLEED}" stroke="#2AA6A0" stroke-width=".012" stroke-dasharray="0.06,0.05"/>')
        parts.append(f'<text x="{W/2}" y="{H - .05}" class="g" text-anchor="middle" font-size="{.1 if kind!="card" else .06}">pink = cut line · bleed 0.125" · {W:.3g} × {H:.3g} in · 300 dpi</text>')
    parts.append("</svg>")
    return "\n".join(parts), W, H


def html(svg, W, H):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>@page{{size:{W}in {H}in;margin:0}}"
            f"html,body{{margin:0;padding:0;background:#fff}}svg{{display:block}}</style></head><body>{svg}</body></html>")


if __name__ == "__main__":
    kinds = sys.argv[1:] or ["front", "back", "sheet", "card"]
    for kind in kinds:
        svg, W, H = page(kind)
        (OUT / f"{kind}.html").write_text(html(svg, W, H), encoding="utf-8")
        svg, W, H = page(kind, guides=True)
        (OUT / f"{kind}_proof.html").write_text(html(svg, W, H), encoding="utf-8")
        print(f"{kind}: {W} x {H} in -> {int(round(W*DPI))} x {int(round(H*DPI))} px")
