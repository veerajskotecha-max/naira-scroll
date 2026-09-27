# -*- coding: utf-8 -*-
"""OPTION A — APRICOT. THE FRUIT STALL.
The camp word is split around the jewellery: APRI above the woven hoops, COT. below, both set in the calm silk the
photograph left for them, so the piece sits inside its own colour name. The price is a fruit-stall PLU sticker slapped
across the edge of the photograph; below, the rest of the camp is laid out like a stall — each piece rising out of its
own crate-photo with its own sticker — and a taped strip carries the three facts that are true of every piece."""
from base import *

K = dict(paper="#F7DCCB", band="#F3C2A6", coral="#E0795A", ink="#2F4A42", dot="#C4513A", ivory="#FFF8F5", brown="#3B2A22")
HERO = "E20267O"
TAGS = {"E20267O": ("WOVEN HOOPS · 25MM", "20267"), "E14776S": ("BRUSHED HUGGIES · 12MM", "14776"),
        "YF3952": ("HEARTLINE · PAPERCLIP", "3952"), "E16075B": ("RIBBON BOWS · 15MM", "16075"),
        "YF8156": ("RIBBON BEAD · 16–19CM", "8156")}
UP = f"{ROOT}/up"
CAP = 0.709          # Velista cap height / em


def word_svg(W, H, lines, z=2):
    """lines: [(text, x_center, baseline, fs, fill, dot_fill)] as one full-page SVG layer"""
    t = []
    for text, xc, bl, fs, fill, dot in lines:
        tail = f'<tspan fill="{dot}">.</tspan>' if dot else ""
        t.append(f'<text x="{xc:.1f}" y="{bl:.1f}" text-anchor="middle" font-family="Velista" font-size="{fs:.1f}" fill="{fill}" letter-spacing="{-0.01*fs:.1f}">{E(text)}{tail}</text>')
    return f'<svg class="abs" style="left:0;top:0;overflow:visible;z-index:{z}" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(t)}</svg>'


def build(wcm, hcm):
    W, H = int(wcm * CM), int(hcm * CM); u = W / 100
    wide = wcm / hcm > 0.6
    m = max(2.5 * CM, 0.05 * W); body = []
    grid = [s for s in ORDER["peach"] if s != HERO and FINAL.get(f"{s}|S1")]
    base_h = 12 * CM
    # ---------------- the print (full-bleed on narrow stands, a centred print on the 4 ft stand)
    P = asset_plate(f"{UP}/{HERO}_S1.png", "apr_hero_plate")
    Cc = asset_cut(f"{UP}/{HERO}_S1_cut.png", "apr_hero_cut")
    bx0, by0, bx1, by1 = Cc["bbox"]
    pw = {61.0: 1.0, 76.2: 1.0, 91.4: 0.72, 122.0: 0.52}.get(wcm, 1.0) * W; px = (W - pw) / 2
    s = pw / P["PW"]; ph = s * (by1 - by0)
    # header
    y = 3.5 * CM
    lw = (0.20 if wide else 0.30) * W; lh = lw * 368 / 1642
    ts = (0.95 if wide else 1.25) * u
    head_h = lh + 1.1 * u + ts * 1.4
    cap1 = y + head_h + (2.2 if not wide else 1.6) * u          # top of APRI capitals
    # height the rest of the stand needs (from the floor up), so the hero gets whatever is left
    cols = max(1, len(ORDER["peach"]) - 1); gap = 1.6 * u
    tw_ = (W - 2 * m - (cols - 1) * gap) / cols
    th_ = tw_ * (1.18 if not wide else 0.85)
    nm = (2.5 if not wide else 1.7) * u
    need = (12 * CM + min(max(0.15 * W, 8 * CM), 12 * CM) + 2.4 * u + (2.5 if not wide else 1.8) * u + 1.2 * u
            + (1.2 if not wide else 0.9) * u * 1.8 + 1.4 * u + th_ * (1 + 0.22 * 0.95) + (4.6 if not wide else 3.6) * u + 1.6 * u
            + (nm * 4.3 + 2.6 * u if not wide else 2.0 * u))
    budget = H - need
    ww = {61.0: 0.93, 76.2: 0.93, 91.4: 0.90, 122.0: 0.80}.get(wcm, 0.9) * W
    ch_max = (budget - cap1 - ph) / 2.0
    fs = min(fit("APRI", ww), fit("COT.", ww), ch_max / CAP); ch = CAP * fs
    b1 = cap1 + ch
    pt = b1 - 0.10 * ch                                           # hoops overlap the foot of APRI a little
    pb = pt + ph
    cap2 = pb - 0.20 * ch                                         # ...and the head of COT.
    b2 = cap2 + ch
    print_top = 0 if pw >= W else max(cap1 - 0.14 * ch, y + head_h + 0.8 * u)
    print_bot = b2 + 0.30 * ch
    tx = px + pw / 2 - s * (bx0 + bx1) / 2
    ty = pt - s * by0
    # keep the plate covering the print (vertical)
    if ty > print_top: ty = print_top
    if ty + s * P["PH"] < print_bot: print_bot = ty + s * P["PH"]
    ph_print = print_bot - print_top
    centred = pw < W
    shadow = "" if not centred else "box-shadow:0 %.0fpx %.0fpx rgba(80,40,20,.20)" % (u * 0.5, u * 1.8)
    body.append(clipbox(px, print_top, pw, ph_print, img(P, s, tx, ty), z=1, radius=(u * 0.6 if centred else 0), extra=shadow))
    body.append(f'<img src="{logo(K["ink"], "ink_apr")}" class="abs" style="left:{(W-lw)/2:.1f}px;top:{y:.1f}px;width:{lw:.1f}px;height:{lh:.1f}px;z-index:4">')
    body.append(f'<div class="abs mono" style="left:0;right:0;top:{y + lh + 1.1*u:.1f}px;text-align:center;font-size:{ts:.1f}px;letter-spacing:.34em;color:{K["ink"]};z-index:4">NAIRA PETITE — THE APRICOT CAMP</div>')
    body.append(word_svg(W, H, [("APRI", W / 2, b1, fs, K["ink"], None), ("COT", W / 2 - fs * 0.03, b2, fs, K["ink"], K["dot"])], z=2))
    # the cut-out may leave the print (on the wide stand) — clip only to the page
    body.append(clipbox(0, 0, W, H, img(Cc, s, tx, ty, extra="filter:drop-shadow(0 %.0fpx %.0fpx rgba(60,30,10,.20))" % (u * 0.3, u * 0.9)), z=3))
    # ---------------- caption row + sticker
    nm = (2.5 if not wide else 1.55) * u
    if not wide:
        yb = print_bot + 1.8 * u; cx_, cw_ = m, 0.55 * W
    else:
        cw_ = px - m - 2.0 * u; cx_ = m; yb = pt + ph * 0.42
    body.append(f'<div class="abs ital" style="left:{cx_:.1f}px;top:{yb:.1f}px;width:{cw_:.0f}px;font-size:{nm*1.05:.1f}px;line-height:1.05;color:{K["brown"]}">(texture does the talking here.)</div>')
    nl = 1.45 if not wide else 2.5
    body.append(f'<div class="abs jost" style="left:{cx_:.1f}px;top:{yb + nm*nl:.1f}px;width:{cw_:.0f}px;font-size:{nm:.1f}px;letter-spacing:.07em;color:{K["ink"]};line-height:1.05">{E(title(HERO))}</div>')
    ns = 2.75 if not wide else 4.95
    body.append(f'<div class="abs mono" style="left:{cx_:.1f}px;top:{yb + nm*ns:.1f}px;width:{cw_:.0f}px;font-size:{nm*0.44:.1f}px;letter-spacing:.08em;color:{K["ink"]};opacity:.9;line-height:1.45">{E(COPY[HERO]["spec"])}</div>')
    if not centred:      # slapped across the bottom edge of the photograph, under the baseline of COT.
        sw = 0.36 * W; sx = W - m - sw * 0.98; sy = b2 + 0.02 * ch
    else:                # stuck on the right edge of the print, beside the hoops
        sw = (0.27 if not wide else 0.20) * W
        sx = px + pw - sw * (0.42 if not wide else 0.30); sy = pt + ph * (0.30 if not wide else 0.12)
    body.append(f'<div class="abs" style="left:{sx:.1f}px;top:{sy:.1f}px;transform:rotate(-9deg);z-index:6">'
                f'{plu_svg(sw, price(HERO), "NAIRA PETITE · APRICOT", TAGS[HERO][0], TAGS[HERO][1], K["coral"], K["ivory"])}</div>')
    yg = (yb + nm * 2.75 + nm * 0.44 * 1.45 * 2 + 2.6 * u) if not wide else print_bot + 2.4 * u
    # ---------------- bottom stack (from the floor up)
    qr = min(max(0.15 * W, 8 * CM), 12 * CM)
    qr_row = qr + 2.4 * u
    tick_h = (2.5 if not wide else 1.8) * u
    tyk = H - base_h - qr_row - tick_h - 1.2 * u
    # ---------------- the stall: one row
    gt = (1.2 if not wide else 0.9) * u
    body.append(f'<div class="abs mono" style="left:{m:.1f}px;top:{yg:.1f}px;font-size:{gt:.1f}px;letter-spacing:.3em;color:{K["ink"]}">FROM THE SAME STALL</div>')
    body.append(f'<div class="abs" style="left:{m:.1f}px;right:{m:.1f}px;top:{yg + gt*1.8:.1f}px;height:{max(2,u*0.08):.1f}px;background:{K["ink"]};opacity:.45"></div>')
    cols = max(1, len(grid)); gap = 1.6 * u
    tw = (W - 2 * m - (cols - 1) * gap) / cols
    lab_h = (4.6 if not wide else 3.6) * u
    pop = 0.22
    top_room = gt * 1.8 + 1.4 * u
    avail = tyk - 1.6 * u - (yg + top_room) - lab_h
    th = min(tw * 1.30, avail / (1 + pop * 0.95))
    ty_ = yg + top_room + th * pop * 0.95 + (avail - th * (1 + pop * 0.95)) * 0.35
    for i, sku in enumerate(grid):
        x = m + i * (tw + gap)
        body.append(pop_tile(sku, x, ty_, tw, th, fill=0.84, pop=pop, z=3, radius=u * 0.6,
                             frame_extra="box-shadow:0 %.0fpx %.0fpx rgba(80,40,20,.15)" % (u * 0.25, u * 0.9)))
        ssw = tw * 0.56
        body.append(f'<div class="abs" style="left:{x + tw - ssw*0.80:.1f}px;top:{ty_ + th - ssw*0.46:.1f}px;transform:rotate(-8deg);z-index:7">'
                    f'{plu_svg(ssw, price(sku), "NAIRA PETITE · APRICOT", TAGS[sku][0], TAGS[sku][1], K["coral"], K["ivory"])}</div>')
        ly = ty_ + th + 0.9 * u + ssw * 0.18
        body.append(f'<div class="abs jost" style="left:{x:.1f}px;top:{ly:.1f}px;width:{tw*0.98:.0f}px;font-size:{(1.35 if not wide else 1.05)*u:.1f}px;letter-spacing:.05em;color:{K["ink"]};line-height:1.08">{E(title(sku))}</div>')
    # ---------------- taped strip
    fact = "WATERPROOF · SURGICAL STAINLESS STEEL · 18K GOLD TONE · "
    body.append(f'<div class="abs mono" style="left:{-0.1*W:.0f}px;width:{1.2*W:.0f}px;top:{tyk:.1f}px;height:{tick_h:.1f}px;line-height:{tick_h:.1f}px;'
                f'background:{K["coral"]};color:{K["ivory"]};font-size:{tick_h*0.40:.1f}px;letter-spacing:.24em;white-space:nowrap;overflow:hidden;'
                f'transform:rotate(-1.6deg);z-index:8;box-shadow:0 {u*0.2:.0f}px {u*0.6:.0f}px rgba(80,30,10,.18)">{fact * 8}</div>')
    # ---------------- scan row
    qy = H - base_h - qr_row + 0.8 * u
    body.append(f'<div class="abs" style="left:{m:.1f}px;top:{qy:.1f}px;width:{qr:.1f}px;height:{qr:.1f}px;background:{K["ivory"]};padding:{qr*0.07:.1f}px;border-radius:{qr*0.05:.1f}px;z-index:5">'
                f'{qr_svg("https://nairaflore.com/?utm_source=standee&utm_medium=print&utm_campaign=apricot", K["ink"])}</div>')
    tx0 = m + qr + 2.2 * u
    body.append(f'<div class="abs jost" style="left:{tx0:.1f}px;top:{qy + qr*0.08:.1f}px;font-size:{qr*0.10:.1f}px;letter-spacing:.14em;color:{K["ink"]}">SCAN · SHOP THE CAMP</div>')
    fsu = min(fit("nairaflore.com", W - m - tx0, track=0), qr * 0.46)
    body.append(f'<div class="abs vel" style="left:{tx0 - 0.2*u:.1f}px;top:{qy + qr*0.30:.1f}px;font-size:{fsu:.1f}px;color:{K["ink"]}">nairaflore.com</div>')
    body.append(f'<div class="abs mono" style="left:{tx0:.1f}px;top:{qy + qr*0.82:.1f}px;font-size:{qr*0.056:.1f}px;letter-spacing:.22em;color:{K["ink"]};opacity:.85">NAIRA PETITE · APRICOT · SAGE · LILAC</div>')
    # ---------------- base (goes into the stand)
    body.append(f'<div class="abs" style="left:0;right:0;bottom:0;height:{base_h:.1f}px;background:{K["ink"]}"></div>')
    return page_html(wcm, hcm, "".join(body), K["paper"])


if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if not a.startswith("--")] or [s[0] for s in SIZES]
    jobs = [(f"A-apricot-{t}", w, h, build(w, h)) for t, w, h in SIZES if t in only]
    asyncio.run(render_all(jobs, pdf="--nopdf" not in sys.argv))
    print("rendered", [j[0] for j in jobs])
