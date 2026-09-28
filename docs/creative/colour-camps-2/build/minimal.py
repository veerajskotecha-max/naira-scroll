# -*- coding: utf-8 -*-
"""COLOUR CAMPS 2.0 — the quiet edition.
The verified photograph carries the ad. On it: the Naira wordmark, the product's name in the brand serif, and its price.
Nothing else — no camp word, no stickers, chips or stamps, no buttons (Meta adds its own), no scrims.
Type is the website's own: Velista for the name, Jost tracked capitals for the price, Cormorant italic for the one line
a card may carry. Ink is tone-on-tone per camp. Stories keep the top 250px and the bottom 340px clear of all text."""
import os, sys, json, html
import numpy as np
from PIL import Image
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
sys.path.insert(0, f"{SP}/sets3"); sys.path.insert(0, f"{SP}/sets2")
from core import *                      # FORMATS, ROWS, E, price, fontfaces, render, gate, audit
from campcopy import COPY, ORDER

CC = f"{SP}/cc"; CUT = f"{CC}/cutouts"; FINAL = f"{CC}/shoot/final_v2.json"
F = json.load(open(FINAL))
INKS = {"peach": "#3A2520", "sage": "#1F3A31", "lilac": "#33274A"}
IVORY = "#FBF6F0"
MAT = {"peach": "#EFD7C8", "sage": "#D9E6DE", "lilac": "#E2D6E6"}      # one mat tone per camp
LOGO_SRC = f"{SP}/standee/assets/logo_src.png"
OUTA = f"{SP}/sets3/assets"; os.makedirs(OUTA, exist_ok=True)


def logo(col):
    p = f"{OUTA}/logo_{col.strip('#')}.png"
    if not os.path.exists(p):
        im = Image.open(LOGO_SRC).convert("RGBA"); c = Image.new("RGBA", im.size, col); c.putalpha(im.split()[3]); c.save(p)
    return p


def cut_of(plate):
    b = os.path.basename(plate)[:-4]
    for cand in (b, b[:-1] if b.endswith("g") else b, b.rstrip("cgr"), b.rstrip("g").rstrip("c")):
        p = f"{CUT}/{cand}.png"
        if os.path.exists(p): return p
    return None


def alpha_bbox(cut):
    a = np.asarray(Image.open(cut).convert('RGBA'))[..., 3]; ys, xs = np.where(a > 128)
    return xs.min() / a.shape[1], ys.min() / a.shape[0], xs.max() / a.shape[1], ys.max() / a.shape[0]


def lum_region(plate, box):
    """mean relative luminance of a region (fractions of the plate)"""
    im = Image.open(plate).convert("RGB"); w, h = im.size
    x0, y0, x1, y1 = [int(v) for v in (box[0] * w, box[1] * h, box[2] * w, box[3] * h)]
    a = np.asarray(im.crop((max(0, x0), max(0, y0), min(w, x1), min(h, y1))).resize((64, 32))).astype(float) / 255
    a = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    return float((0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]).mean())


def contrast(l1, l2):
    a, b = max(l1, l2), min(l1, l2); return (a + 0.05) / (b + 0.05)


def hexlum(hx):
    r, g, b = (int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ink_for(camp, plate, box):
    """camp ink where it reads, ivory where the photograph under the words is dark"""
    L = lum_region(plate, box); ink = INKS[camp]
    return ink if contrast(L, hexlum(ink)) >= contrast(L, hexlum(IVORY)) else IVORY


def sample_bg(plate, light=0.0):
    im = np.asarray(Image.open(plate).convert("RGB").resize((96, 172))).astype(float)
    p = np.median(im[4:34].reshape(-1, 3), axis=0)
    p = p + (255 - p) * light
    return "#%02X%02X%02X" % tuple(int(v) for v in p)


def plate_window(plate, W, H, cy_frac=None, target=0.5):
    """cover-fit the plate into W x H, the product centre at `target` of the height"""
    iw, ih = Image.open(plate).size
    s = max(W / iw, H / ih); pw, ph = iw * s, ih * s
    cut = cut_of(plate)
    if cy_frac is None and cut:
        x0, y0, x1, y1 = alpha_bbox(cut); cy_frac = (y0 + y1) / 2
    cy_frac = 0.5 if cy_frac is None else cy_frac
    top = H * target - cy_frac * ph; top = max(min(top, 0), H - ph)
    left = (W - pw) / 2
    return left, top, pw, ph, s


CSS = """
.v2{position:absolute;inset:0;overflow:hidden}
.v2 img.ph{position:absolute;display:block}
.v2 .lg{position:absolute;left:50%;transform:translateX(-50%);display:block}
.v2 .cap{position:absolute;left:0;right:0;text-align:center}
.v2 .nm{font-family:'Velista';font-weight:500;letter-spacing:.05em;line-height:1.05;text-transform:uppercase}
.v2 .pr{font-family:'Jost';font-weight:400;letter-spacing:.24em;text-transform:uppercase}
.v2 .ln{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;line-height:1.15}
.v2 .lb{font-family:'Jost';font-weight:500;letter-spacing:.42em;text-transform:uppercase}
.v2 .rule{display:inline-block;height:1.5px;background:currentColor;opacity:.55}
"""


def haze(x, y, w, h, col, strength=0.30):
    """a feathered patch that softens the photograph under a caption: backdrop blur plus a faint wash of the local colour"""
    r, g, b = (int(col[i:i + 2], 16) for i in (1, 3, 5))
    m = "radial-gradient(ellipse 50% 50% at 50% 50%, #000 42%, transparent 100%)"
    return (f'<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;height:{h:.0f}px;'
            f'backdrop-filter:blur(9px);-webkit-backdrop-filter:blur(9px);background:rgba({r},{g},{b},{strength});'
            f'-webkit-mask-image:{m};mask-image:{m};z-index:1"></div>')


def local_col(plate, box):
    im = Image.open(plate).convert("RGB"); w, h = im.size
    x0, y0, x1, y1 = [int(v) for v in (box[0] * w, box[1] * h, box[2] * w, box[3] * h)]
    a = np.asarray(im.crop((max(0, x0), max(0, y0), min(w, x1), min(h, y1))).resize((32, 16))).reshape(-1, 3)
    return "#%02X%02X%02X" % tuple(int(v) for v in np.median(a, axis=0))


def price_txt(sku):
    return "₹" + f"{int(round(ROWS[sku]['price'])):,}"


import re
def fact(sku, shot):
    """the verified listing line for a detail card, in sentence case: 'Worn · about 25mm across'"""
    c = COPY[sku]; raw = c["worn"] if shot == "S2" else c["close"]
    raw = re.sub(r"<[^>]+>", "", raw)
    lab, _, txt = raw.partition(" · ")
    t = txt.lower()
    for a, b in ((r"\bcz\b", "CZ"), (r"\bus\b", "US"), (r"(\d)mm", r"\1 mm"), (r"(\d)cm", r"\1 cm")):
        t = re.sub(a, b, t)
    return lab.capitalize(), t


def product_box(plate, left, top, pw, ph):
    cut = cut_of(plate)
    if not cut: return None
    x0, y0, x1, y1 = alpha_bbox(cut)
    return left + x0 * pw, top + y0 * ph, left + x1 * pw, top + y1 * ph


def place_feed(plate, W, H, lo=150, hi=1110):
    """4:5 window: the product centred between the logo and the caption band"""
    iw, ih = Image.open(plate).size
    s = max(W / iw, H / ih); pw, ph = iw * s, ih * s
    cut = cut_of(plate); cy = 0.5
    if cut:
        x0, y0, x1, y1 = alpha_bbox(cut); cy = (y0 + y1) / 2
    top = (lo + hi) / 2 - cy * ph; top = max(min(top, 0), H - ph)
    return (W - pw) / 2, top, pw, ph


# ------------------------------------------------------------------ direction A · QUIET (full-bleed)
def render_quiet(c, fmt):
    W, H = FORMATS[fmt]; camp, sku, plate = c["camp"], c["sku"], c["plate"]
    if fmt == "story":
        iw, ih = Image.open(plate).size; s = max(W / iw, H / ih); pw, ph = iw * s, ih * s
        l, t = (W - pw) / 2, (H - ph) / 2
        logo_top, logo_w = 262, 170
        pb = product_box(plate, l, t, pw, ph)
        cap_top = 1452 if (pb is None or pb[3] < 1415) else 360      # under the piece, or up under the wordmark
    else:
        l, t, pw, ph = place_feed(plate, W, H)
        logo_top, logo_w = 64, 146
        cap_top = 1158
    ink_top = ink_for(camp, plate, ((-l) / pw, (logo_top - t) / ph, (W - l) / pw, (logo_top + 60 - t) / ph))
    ink_cap = ink_for(camp, plate, ((W * 0.2 - l) / pw, (cap_top - t) / ph, (W * 0.8 - l) / pw, (cap_top + 110 - t) / ph))
    box = ((W * 0.12 - l) / pw, (cap_top - 20 - t) / ph, (W * 0.88 - l) / pw, (cap_top + 120 - t) / ph)
    hz = haze(W * 0.08, cap_top - 70, W * 0.84, 250, local_col(plate, box))
    return (f'<div class="v2"><img class="ph" src="{plate}" style="left:{l:.1f}px;top:{t:.1f}px;width:{pw:.1f}px;height:{ph:.1f}px">{hz}'
            f'<img class="lg" src="{logo(ink_top)}" style="top:{logo_top}px;width:{logo_w}px;z-index:2">'
            f'<div class="cap" style="top:{cap_top}px;color:{ink_cap};z-index:2">'
            f'<div class="nm" style="font-size:{44 if fmt=="feed" else 48}px;padding:0 96px">{E(ROWS[sku]["title"])}</div>'
            f'<div class="pr" style="font-size:{22 if fmt=="feed" else 24}px;margin-top:{16 if fmt=="feed" else 20}px">{price_txt(sku)}</div></div></div>')


def quiet_card(c, fmt="feed"):
    """carousel detail card: the photograph, and one quiet line; the last card carries name and price"""
    W, H = FORMATS["feed"]; camp, sku, plate = c["camp"], c["sku"], c["plate"]
    iw, ih = Image.open(plate).size; s = max(W / iw, H / ih); pw, ph = iw * s, ih * s
    l, t = (W - pw) / 2, (H - ph) / 2
    if c.get("last"):
        cap_top = 1158
        ink = ink_for(camp, plate, ((W * 0.2 - l) / pw, (cap_top - t) / ph, (W * 0.8 - l) / pw, (cap_top + 110 - t) / ph))
        cap = (f'<div class="cap" style="top:{cap_top}px;color:{ink}"><div class="nm" style="font-size:44px;padding:0 96px">{E(ROWS[sku]["title"])}</div>'
               f'<div class="pr" style="font-size:22px;margin-top:16px">{price_txt(sku)}</div></div>')
    else:
        lab, txt = fact(sku, c["shot"])
        ink = ink_for(camp, plate, ((64 - l) / pw, (1210 - t) / ph, (760 - l) / pw, (1290 - t) / ph))
        cap = (f'<div style="position:absolute;left:64px;bottom:60px;right:64px;color:{ink}">'
               f'<div class="lb" style="font-size:17px;opacity:.85">{E(lab)}</div>'
               f'<div class="ln" style="font-size:36px;margin-top:6px">{E(txt[0].upper() + txt[1:])}</div></div>')
    if c.get("last"):
        hz = haze(W * 0.08, 1158 - 70, W * 0.84, 250, local_col(plate, ((W * 0.12 - l) / pw, (1138 - t) / ph, (W * 0.88 - l) / pw, (1278 - t) / ph)))
    else:
        hz = haze(10, 1150, 880, 230, local_col(plate, ((40 - l) / pw, (1190 - t) / ph, (800 - l) / pw, (1300 - t) / ph)))
    return f'<div class="v2"><img class="ph" src="{plate}" style="left:{l:.1f}px;top:{t:.1f}px;width:{pw:.1f}px;height:{ph:.1f}px">{hz}<div style="position:absolute;inset:0;z-index:2">{cap}</div></div>'


# ------------------------------------------------------------------ direction B · FRAMED (passe-partout)
def framed_shell(c, fmt, win, logo_top, logo_w, cap_html, target=0.5):
    W, H = FORMATS[fmt]; camp, sku, plate = c["camp"], c["sku"], c["plate"]
    mat = MAT[camp]
    wx, wy, ww, wh = win
    l, t, pw, ph, s = plate_window(plate, ww, wh, target=target)
    return (f'<div class="v2" style="background:{mat}">'
            f'<div style="position:absolute;left:{wx}px;top:{wy}px;width:{ww}px;height:{wh}px;overflow:hidden">'
            f'<img class="ph" src="{plate}" style="left:{l:.1f}px;top:{t:.1f}px;width:{pw:.1f}px;height:{ph:.1f}px"></div>'
            f'<img class="lg" src="{logo(INKS[camp])}" style="top:{logo_top}px;width:{logo_w}px">{cap_html}</div>')


def render_framed(c, fmt):
    camp, sku = c["camp"], c["sku"]; ink = INKS[camp]
    name = E(ROWS[sku]["title"]); line = E(COPY[sku]["sub"].strip("()").rstrip(".").capitalize() + ".")
    if fmt == "story":      # block centred in the visible band: 250px clear at the top, ~320px at the bottom
        win = (84, 360, 1080 - 168, 1060); cap_top = 360 + 1060 + 44
        cap = (f'<div class="cap" style="top:{cap_top}px;color:{ink}"><div class="nm" style="font-size:44px;padding:0 90px">{name}</div>'
               f'<div class="ln" style="font-size:32px;margin-top:10px;opacity:.92">{line}</div>'
               f'<div class="pr" style="font-size:23px;margin-top:14px">{price_txt(sku)}</div></div>')
        return framed_shell(c, fmt, win, 290, 150, cap)
    win = (64, 132, 1080 - 128, 996); cap_top = 132 + 996 + 34
    cap = (f'<div class="cap" style="top:{cap_top}px;color:{ink}"><div class="nm" style="font-size:38px;padding:0 80px">{name}</div>'
           f'<div class="ln" style="font-size:28px;margin-top:6px;opacity:.92">{line}</div>'
           f'<div class="pr" style="font-size:20px;margin-top:10px">{price_txt(sku)}</div></div>')
    return framed_shell(c, fmt, win, 50, 136, cap)


def framed_card(c, fmt="feed"):
    camp, sku = c["camp"], c["sku"]; ink = INKS[camp]
    win = (64, 132, 1080 - 128, 996); cap_top = 132 + 996 + 40
    if c.get("last"):
        cap = (f'<div class="cap" style="top:{cap_top}px;color:{ink}"><div class="nm" style="font-size:38px;padding:0 80px">{E(ROWS[sku]["title"])}</div>'
               f'<div class="pr" style="font-size:20px;margin-top:12px">{price_txt(sku)}</div></div>')
    else:
        lab, txt = fact(sku, c["shot"])
        cap = (f'<div class="cap" style="top:{cap_top - 4}px;color:{ink}"><div class="lb" style="font-size:16px;opacity:.8">{E(lab)}</div>'
               f'<div class="ln" style="font-size:36px;margin-top:8px;padding:0 90px">{E(txt[0].upper() + txt[1:])}</div></div>')
    return framed_shell(c, "feed", win, 50, 136, cap)


PRE = {"peach": "A", "sage": "S", "lilac": "L"}


def creatives(direction, skus=None):
    out = []
    for camp, lst in ORDER.items():
        for i, sku in enumerate(lst, 1):
            if skus and sku not in skus: continue
            p = F.get(f"{sku}|S1")
            if not p: continue
            out.append(dict(render=render_quiet if direction == "quiet" else render_framed, camp=camp, id=f"{PRE[camp]}{i}",
                            sku=sku, skus=[sku], plate=p, claims=[], file=re.sub(r"[^a-z0-9]+", "-", ROWS[sku]["title"].lower().replace("é", "e").replace("è", "e")).strip("-")))
    return out


def cards(direction, skus=None):
    out = []
    for camp, lst in ORDER.items():
        for i, sku in enumerate(lst, 1):
            if skus and sku not in skus: continue
            if not F.get(f"{sku}|S1"): continue
            shots = [sh for sh in ("S2", "S3", "S4") if F.get(f"{sku}|{sh}")]
            for j, sh in enumerate(shots, 2):
                out.append(dict(render=quiet_card if direction == "quiet" else framed_card, camp=camp, id=f"{PRE[camp]}{i}{chr(96 + j)}",
                                sku=sku, skus=[sku], plate=F[f"{sku}|{sh}"], shot=sh, last=(j == len(shots) + 1), claims=[],
                                file=re.sub(r"[^a-z0-9]+", "-", ROWS[sku]["title"].lower().replace("é", "e").replace("è", "e")).strip("-")))
    return out
