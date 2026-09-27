# -*- coding: utf-8 -*-
"""OPTION B — SAGE. THE COLOUR CARD.
The stand is a giant paint sample card. The top swatch is the photograph itself — SAGE. set behind the Heartbead
bracelet, which climbs out over the top edge of its swatch. Below it runs a paint strip, lightest to deepest sage,
one chip per piece, each piece stepping up out of its chip over the one above; every chip carries its real hex code.
The deepest chip is the one you scan."""
from base import *
from apricot import word_svg, CAP
from ccads import sample_class

K = dict(card="#F4F1EA", ink="#1F3A31", dot="#DD7F68", ivory="#F7F4EE", muted="#5E6F66")
CHIPS = ["#D5E6DC", "#B3CCBF", "#8DAE9F", "#5F8575"]
HERO = "YF5215"
NUM = {"YF5143": "5143", "YF5215": "5215", "FE02847B": "02847", "JDR0104337": "0104337", "JDR0303312-7": "0303312"}
UP = f"{ROOT}/up"


def lum(hx):
    r, g, b = (int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def hero_swatch(body, x, y, w, h, u, pop=0.10):
    """photograph as the first swatch; SAGE. behind the bracelet; the bracelet climbs out over the top edge"""
    P = asset_plate(f"{UP}/{HERO}_S1.png", "sage_hero_plate")
    Cc = asset_cut(f"{UP}/{HERO}_S1_cut.png", "sage_hero_cut")
    bx0, by0, bx1, by1 = Cc["bbox"]
    s = w / P["PW"]
    tx = x + w / 2 - s * (bx0 + bx1) / 2
    ty = y - pop * s * (by1 - by0) - s * by0
    s, tx, ty = cover(P, x, y, w, h, s, tx, ty)
    body.append(clipbox(x, y, w, h, img(P, s, tx, ty), z=1, extra="box-shadow:0 %.0fpx %.0fpx rgba(20,40,30,.18)" % (u * 0.3, u * 1.2)))
    fs = fit("SAGE.", 0.94 * w); ch = CAP * fs
    # the word sits across the middle of the bead circle (upper ~40% of the product box)
    mid = ty + s * (by0 + (by1 - by0) * 0.40)
    bl = mid + ch / 2
    t = f'<text x="{x + w/2:.1f}" y="{bl:.1f}" text-anchor="middle" font-family="Velista" font-size="{fs:.1f}" fill="{K["ink"]}" letter-spacing="{-0.01*fs:.1f}">SAGE<tspan fill="{K["dot"]}">.</tspan></text>'
    body.append(clipbox(x, y, w, h, f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="10" height="10">{t}</svg>', z=2))
    top_room = max(0, y - (ty + s * by0)) + 6
    body.append(clipbox(x - w * 0.03, y - top_room, w * 1.06, h + top_room, img(Cc, s, tx, ty,
                        extra="filter:drop-shadow(0 %.0fpx %.0fpx rgba(20,40,30,.18))" % (u * 0.25, u * 0.7)), z=3))
    return P, s, tx, ty


def chip(body, sku, x, y, w, h, col, u, first=False, pop=0.18, prod_w=0.40):
    """one paint chip: flat colour, the piece standing on the left and stepping up over the chip above; label right"""
    ink = K["ink"] if lum(col) > 0.28 else K["ivory"]
    body.append(f'<div class="abs" style="left:{x:.1f}px;top:{y:.1f}px;width:{w:.1f}px;height:{h:.1f}px;background:{col};z-index:2"></div>')
    plate = FINAL[f"{sku}|S1"]; cutp = cut_for(plate)
    C = asset_cut(cutp, f"cut_{os.path.basename(cutp)[:-4]}")
    bx0, by0, bx1, by1 = C["bbox"]; bw, bh = bx1 - bx0, by1 - by0
    s = min(prod_w * w / bw, h * (0.90 + pop) / bh)
    cx = x + w * 0.05 + (prod_w * w - s * bw) / 2
    tx = cx - s * bx0
    ty = (y + h - 0.06 * h) - s * by1          # stands on the chip, just above its lower edge
    body.append(clipbox(x, y - h * pop - 4, w, h * (1 + pop) + 4, img(C, s, tx, ty,
                        extra="filter:drop-shadow(0 %.0fpx %.0fpx rgba(10,30,20,.25))" % (u * 0.25, u * 0.6)), z=4))
    lx = x + w * (prod_w + 0.10); lw = x + w - lx - w * 0.04
    n = h / 100
    pw_ = u * 3.2 * 3.6                                   # room kept for the price on the right
    body.append(f'<div class="abs" style="left:{lx:.1f}px;top:{y + h*0.15:.1f}px;width:{lw - pw_:.0f}px;z-index:5;color:{ink}">'
                f'<div class="mono" style="font-size:{u*1.05:.1f}px;letter-spacing:.18em;opacity:.85;margin-bottom:{u*0.6:.1f}px">SAGE Nº {NUM[sku]} · {col}</div>'
                f'<div class="jost" style="font-size:{u*2.3:.1f}px;letter-spacing:.05em;line-height:1.02;margin-bottom:{u*0.7:.1f}px">{E(title(sku))}</div>'
                f'<div class="mono" style="font-size:{u*1.0:.1f}px;letter-spacing:.06em;line-height:1.4;opacity:.9">{E(COPY[sku]["spec"])}</div></div>')
    body.append(f'<div class="abs jost" style="right:{W_[0] - (x + w) + w*0.04:.1f}px;top:{y + h*0.15 + u*1.5:.1f}px;font-size:{u*3.2:.1f}px;letter-spacing:.01em;color:{ink};z-index:5;text-transform:none">{price(sku)}</div>')


W_ = [0]


def chipcard(w, rows, u):
    k = w / 230
    ch = "".join(f'<div style="display:flex;align-items:center;gap:{10*k:.1f}px;margin-bottom:{8*k:.1f}px"><div style="width:{w*0.44:.1f}px;height:{w*0.24:.1f}px;background:{hx}"></div>'
                 f'<div><div class="jost" style="font-size:{13*k:.1f}px;letter-spacing:.1em">{E(nm)}</div><div class="mono" style="font-size:{10.5*k:.1f}px;letter-spacing:.06em;opacity:.8">{hx}</div></div></div>' for hx, nm in rows)
    return (f'<div style="width:{w:.1f}px;background:#FBF9F4;color:{K["ink"]};padding:{14*k:.1f}px {14*k:.1f}px {10*k:.1f}px">'
            f'<div class="mono" style="font-size:{11.5*k:.1f}px;letter-spacing:.16em;margin-bottom:{10*k:.1f}px;opacity:.85">NAIRA PETITE · SAGE</div>{ch}'
            f'<div class="mono" style="font-size:{10.5*k:.1f}px;letter-spacing:.14em;border-top:{max(1,1.2*k):.1f}px solid currentColor;padding-top:{8*k:.1f}px;opacity:.85">Nº 5215 · HEARTBEAD</div></div>')


def build(wcm, hcm, tentative=False):
    W, H = int(wcm * CM), int(hcm * CM); u = W / 100; W_[0] = W
    wide = wcm / hcm > 0.6
    m = max(2.5 * CM, 0.05 * W); body = []
    ff = dict(FINAL)
    if tentative:
        for k, v in {"YF5143|S1": f"{PLATES}/sage_YF5143_S1_a5g.png", "JDR0303312-7|S1": f"{PLATES}/sage_JDR0303312-7_S1_a4.png"}.items():
            ff.setdefault(k, v)
    FINAL.update(ff)
    strip = [s for s in ORDER["sage"] if s != HERO and FINAL.get(f"{s}|S1")]
    base_h = 12 * CM
    # ---------------- header: brand left, card name right (paint-card style)
    y = 3.5 * CM
    lw = (0.18 if wide else 0.30) * W; lh = lw * 368 / 1642
    body.append(f'<img src="{logo(K["ink"], "ink_sage")}" class="abs" style="left:{m:.1f}px;top:{y:.1f}px;width:{lw:.1f}px;height:{lh:.1f}px">')
    ts = (1.05 if wide else 1.45) * u
    body.append(f'<div class="abs mono" style="right:{m:.1f}px;top:{y - lh*0.05:.1f}px;text-align:right;font-size:{ts:.1f}px;letter-spacing:.26em;line-height:1.55;color:{K["ink"]}">COLOUR CARD<br>Nº 05 — SAGE<br><span style="opacity:.7">NAIRA PETITE</span></div>')
    y += lh + 3.2 * u
    qr_h = 13.5 * CM if not wide else 15 * CM          # the deepest chip (above the base)
    sw_ = (W - 2 * m) if not wide else 0.62 * W        # photo swatch width (keeps the photograph >= ~70 dpi)
    x, w = (W - sw_) / 2, sw_
    avail = H - base_h - qr_h - y
    n = max(1, len(strip))
    hero_h = avail * (0.52 if not wide else 0.50)
    lab_h = 10.6 * u if not wide else 8.6 * u
    chip_h = (avail - hero_h - lab_h) / n
    P, s_, tx_, ty_ = hero_swatch(body, x, y + hero_h * 0.08, w, hero_h * 0.92, u)
    # the ads' device: a paint-chip card of colours sampled from this photograph, stuck over the swatch corner
    Cc = asset_cut(f"{UP}/{HERO}_S1_cut.png", "sage_hero_cut")
    rows = [(sample_class(f"{UP}/{HERO}_S1.png", None, "bg"), "SAGE"),
            (sample_class(f"{UP}/{HERO}_S1.png", f"{UP}/{HERO}_S1_cut.png", "silver"), "STEEL"),
            (sample_class(f"{UP}/{HERO}_S1.png", f"{UP}/{HERO}_S1_cut.png", "gold"), "GOLD HEART")]
    cw = (0.21 * W) if not wide else 0.13 * W
    cxx = (x + w - cw * 0.80) if not wide else (x + w + (W - m - (x + w) - cw) / 2)
    cyy = y + hero_h * 0.60 if not wide else y + hero_h * 0.18
    body.append(f'<div class="abs" style="left:{cxx:.1f}px;top:{cyy:.1f}px;transform:rotate(5deg);z-index:6;filter:drop-shadow(0 {u*0.3:.0f}px {u*0.9:.0f}px rgba(20,40,30,.22))">{chipcard(cw, rows, u)}</div>')
    if wide:   # left margin: the card's own spine
        body.append(f'<div class="abs mono" style="left:{m + (x - m) * 0.30:.1f}px;top:{y + hero_h*0.08:.1f}px;writing-mode:vertical-rl;transform:rotate(180deg);font-size:{1.2*u:.1f}px;letter-spacing:.5em;color:{K["ink"]};opacity:.8;height:{hero_h*0.92:.0f}px;text-align:center">COLOUR CARD · Nº 05 · SAGE · NAIRA PETITE</div>')
    ly = y + hero_h + 1.3 * u
    _hero_label(body, x, ly, w, u if not wide else u * 0.8)
    cy = y + hero_h + lab_h
    cx0, cwid = m, W - 2 * m
    for i, sku in enumerate(strip):
        chip(body, sku, cx0, cy + i * chip_h, cwid, chip_h, CHIPS[i % len(CHIPS)], u if not wide else u * 0.8,
             pop=(0.0 if i == 0 else 0.10), prod_w=(0.40 if not wide else 0.26))
    qx, qy, qw = cx0, cy + n * chip_h, cwid
    # ---------------- the deepest chip: scan
    body.append(f'<div class="abs" style="left:{qx:.1f}px;top:{qy:.1f}px;width:{qw:.1f}px;height:{H - qy:.1f}px;background:{K["ink"]};z-index:2"></div>')
    q = min(qr_h * 0.80, 12 * CM)
    qy0 = qy + (qr_h - q) / 2
    body.append(f'<div class="abs" style="left:{qx + qw*0.04:.1f}px;top:{qy0:.1f}px;width:{q:.1f}px;height:{q:.1f}px;z-index:5">'
                f'{qr_svg("https://nairaflore.com/?utm_source=standee&utm_medium=print&utm_campaign=sage", K["ivory"])}</div>')
    tx0 = qx + qw * 0.04 + q + 2.2 * u
    body.append(f'<div class="abs mono" style="left:{tx0:.1f}px;top:{qy0:.1f}px;font-size:{max(q*0.058, 0.95*u):.1f}px;letter-spacing:.2em;color:{K["ivory"]};opacity:.85;z-index:5">SAGE Nº 00 · {K["ink"]} · THE DEEPEST ONE</div>')
    body.append(f'<div class="abs jost" style="left:{tx0:.1f}px;top:{qy0 + q*0.16:.1f}px;font-size:{q*0.10:.1f}px;letter-spacing:.14em;color:{K["ivory"]};z-index:5">SCAN · SHOP THE CAMP</div>')
    fsu = min(fit("nairaflore.com", qx + qw - tx0 - 1.5 * u, track=0), q * 0.40)
    body.append(f'<div class="abs vel" style="left:{tx0 - 0.2*u:.1f}px;top:{qy0 + q*0.36:.1f}px;font-size:{fsu:.1f}px;color:{K["ivory"]};z-index:5">nairaflore.com</div>')
    body.append(f'<div class="abs mono" style="left:{tx0:.1f}px;top:{qy0 + q*0.84:.1f}px;font-size:{max(q*0.056, 0.95*u):.1f}px;letter-spacing:.2em;color:{K["ivory"]};opacity:.85;z-index:5">WATERPROOF · SURGICAL STAINLESS STEEL</div>')
    return page_html(wcm, hcm, "".join(body), K["card"])


def _hero_label(body, x, y, w, u):
    hx = sample_bg()
    body.append(f'<div class="abs mono" style="left:{x:.1f}px;top:{y:.1f}px;font-size:{1.0*u:.1f}px;letter-spacing:.2em;color:{K["ink"]};opacity:.85">SAGE Nº {NUM[HERO]} · {hx} · SAMPLED FROM THE PHOTOGRAPH</div>')
    body.append(f'<div class="abs jost" style="left:{x:.1f}px;top:{y + 1.9*u:.1f}px;font-size:{2.5*u:.1f}px;letter-spacing:.06em;color:{K["ink"]}">{E(title(HERO))}</div>')
    body.append(f'<div class="abs mono" style="left:{x:.1f}px;top:{y + 5.0*u:.1f}px;font-size:{1.05*u:.1f}px;letter-spacing:.08em;color:{K["ink"]};opacity:.9">{E(COPY[HERO]["spec"])}</div>')
    body.append(f'<div class="abs jost" style="left:{x:.1f}px;width:{w:.1f}px;text-align:right;top:{y + 1.2*u:.1f}px;font-size:{3.6*u:.1f}px;color:{K["ink"]};text-transform:none">{price(HERO)}</div>')


def sample_bg():
    im = np.asarray(Image.open(f"{UP}/{HERO}_S1.png").convert("RGB").resize((96, 172)))
    p = im[4:30].reshape(-1, 3); r, g, b = np.median(p, axis=0).astype(int)
    return f"#{r:02X}{g:02X}{b:02X}"


if __name__ == "__main__":
    tent = "--tentative" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")] or [s[0] for s in SIZES]
    jobs = [(f"B-sage-{t}", w, h, build(w, h, tent)) for t, w, h in SIZES if t in only]
    asyncio.run(render_all(jobs, pdf="--nopdf" not in sys.argv))
    print("rendered", [j[0] for j in jobs])
