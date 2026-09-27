# -*- coding: utf-8 -*-
"""OPTION C — LILAC. THE STAMP SHEET.
The stand is a philatelic souvenir sheet: a bordered lilac sheet with its inscription, one giant perforated stamp whose
picture is the Prism Rivière bracelet with LILAC. behind it — the bracelet climbing out over the perforations — and a
round NAIRAFLORE.COM postmark cancelling its corner, its wavy lines running off the sheet. Below it, the rest of the
issue as a block of stamps (the price is the denomination), a stamp you scan, and an airmail border at the foot."""
from base import *
from apricot import CAP

K = dict(sheet="#E9DDEF", ink="#3B2D52", dot="#DD7F68", paper="#FBF8F4", band="#D6C3DA", muted="#6B5C80")
HERO = "B00681C"
UP = f"{ROOT}/up"


def rot_wrap(inner, cx, cy, deg, W, H, z):
    return (f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;transform-origin:{cx:.1f}px {cy:.1f}px;'
            f'transform:rotate({deg}deg);z-index:{z};pointer-events:none">{inner}</div>')


def stamp(sku, x, y, w, h, u, W, H, rot=0.0, hero=False, uid="s", z=3):
    out = []
    pad = w * (0.055 if not hero else 0.045)
    bm = h * (0.15 if not hero else 0.105)                       # paper margin under the picture
    out.append(stamp_paper(x, y, w, h, K["paper"], uid, z=1))
    wx, wy, ww, wh = x + pad, y + pad, w - 2 * pad, h - pad - bm
    if hero:
        P = asset_plate(f"{UP}/{HERO}_S1.png", "lil_hero_plate")
        C = asset_cut(f"{UP}/{HERO}_S1_cut.png", "lil_hero_cut")
        bx0, by0, bx1, by1 = C["bbox"]
        s = max(ww / (bx1 - bx0) * 0.98, ww / P["PW"])
        tx = wx + ww / 2 - s * (bx0 + bx1) / 2
        ty = (wy - 0.20 * s * (by1 - by0)) - s * by0              # the top of the bracelet climbs out over the perforations
        s, tx, ty = cover(P, wx, wy, ww, wh, s, tx, ty)
        out.append(clipbox(wx, wy, ww, wh, img(P, s, tx, ty), z=2))
        fs = fit("LILAC.", 0.96 * ww); ch = CAP * fs
        capt = ty + s * (by0 + (by1 - by0) * 0.52)
        t = (f'<text x="{wx + ww/2:.1f}" y="{capt + ch:.1f}" text-anchor="middle" font-family="Velista" font-size="{fs:.1f}" fill="{K["ink"]}" '
             f'letter-spacing="{-0.01*fs:.1f}">LILAC<tspan fill="{K["dot"]}">.</tspan></text>')
        out.append(clipbox(wx, wy, ww, wh, f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="10" height="10">{t}</svg>', z=3))
        top_room = max(0, wy - (ty + s * by0)) + 8
        out.append(clipbox(wx, wy - top_room, ww, wh + top_room, img(C, s, tx, ty,
                           extra="filter:drop-shadow(0 %.0fpx %.0fpx rgba(40,20,60,.22))" % (u * 0.25, u * 0.7)), z=4))
        den = price(HERO); nm = title(HERO); sp = COPY[HERO]["spec"]
    else:
        out.append(pop_tile(sku, wx, wy, ww, wh, fill=0.84, pop=0.20, z=2, side=0.0))
        den = price(sku); nm = title(sku); sp = COPY[sku]["spec"]
    # denomination, white, in the picture's lower-left corner
    ds = (w * 0.085 if not hero else w * 0.060)
    out.append(f'<div class="abs jost" style="left:{wx + ww*0.04:.1f}px;top:{wy + wh - ds*1.35:.1f}px;font-size:{ds:.1f}px;color:#fff;'
               f'text-shadow:0 {ds*0.04:.1f}px {ds*0.25:.1f}px rgba(30,15,45,.45);z-index:6;text-transform:none">{den}</div>')
    # the paper margin: name left, issue right
    ns = bm * (0.27 if not hero else 0.28)
    out.append(f'<div class="abs jost" style="left:{wx:.1f}px;top:{wy + wh + bm*0.20:.1f}px;width:{ww*0.66:.0f}px;font-size:{ns:.1f}px;letter-spacing:.05em;line-height:1.05;color:{K["ink"]};z-index:6">{E(nm)}</div>')
    ms = ns * 0.42
    if hero:
        out.append(f'<div class="abs mono" style="left:{wx:.1f}px;top:{wy + wh + bm*0.20 + ns*1.25:.1f}px;width:{ww*0.70:.0f}px;font-size:{ms:.1f}px;letter-spacing:.06em;line-height:1.35;color:{K["ink"]};opacity:.85;z-index:6">{E(sp)}</div>')
    if not hero: out.append(f'<div class="abs mono" style="left:{wx + ww*0.70:.1f}px;width:{ww*0.30:.0f}px;text-align:right;top:{wy + wh + bm*0.24:.1f}px;font-size:{ms:.1f}px;letter-spacing:.14em;line-height:1.5;color:{K["ink"]};opacity:.8;z-index:6">NAIRA PETITE<br>THE LILAC ISSUE</div>')
    cx, cy = x + w / 2, y + h / 2
    return rot_wrap("".join(out), cx, cy, rot, W, H, z) if rot else f'<div class="abs" style="left:0;top:0;width:{W}px;height:{H}px;z-index:{z}">{"".join(out)}</div>'


def qr_stamp(x, y, w, h, u, W, H, uid, rot=0.0, z=3):
    out = [stamp_paper(x, y, w, h, K["paper"], uid, z=1)]
    pad = w * 0.10
    q = w - 2 * pad
    out.append(f'<div class="abs" style="left:{x+pad:.1f}px;top:{y+pad:.1f}px;width:{q:.1f}px;height:{q:.1f}px;z-index:3">{qr_svg("https://nairaflore.com/?utm_source=standee&utm_medium=print&utm_campaign=lilac", K["ink"])}</div>')
    out.append(f'<div class="abs jost" style="left:{x+pad:.1f}px;top:{y + pad + q + (h - pad - q - pad)*0.10:.1f}px;width:{q:.1f}px;text-align:center;font-size:{w*0.085:.1f}px;letter-spacing:.16em;color:{K["ink"]};z-index:3">SCAN</div>')
    return rot_wrap("".join(out), x + w / 2, y + h / 2, rot, W, H, z)


def build(wcm, hcm):
    W, H = int(wcm * CM), int(hcm * CM); u = W / 100
    wide = wcm / hcm > 0.6
    m = max(2.5 * CM, 0.05 * W); body = []
    rest = [s for s in ORDER["lilac"] if s != HERO and FINAL.get(f"{s}|S1")]
    base_h = 12 * CM
    # ---------------- souvenir-sheet border + inscription
    bi = m * 0.45
    body.append(f'<div class="abs" style="left:{bi:.1f}px;right:{bi:.1f}px;top:{3.0*CM:.1f}px;bottom:{base_h + 3.2*CM:.1f}px;border:{max(2,u*0.09):.1f}px solid {K["ink"]};opacity:.55"></div>')
    ins = "NAIRA PETITE POST · THE LILAC ISSUE · SOUVENIR SHEET"
    isz = (1.0 if not wide else 0.8) * u
    body.append(f'<div class="abs mono" style="left:0;right:0;top:{3.0*CM - isz*0.72:.1f}px;text-align:center;z-index:2"><span style="background:{K["sheet"]};padding:0 {1.2*u:.1f}px;font-size:{isz:.1f}px;letter-spacing:.34em;color:{K["ink"]}">{ins}</span></div>')
    # ---------------- header
    y = 3.0 * CM + 2.4 * u
    lw = (0.20 if wide else 0.30) * W; lh = lw * 368 / 1642
    body.append(f'<img src="{logo(K["ink"], "ink_lil")}" class="abs" style="left:{(W-lw)/2:.1f}px;top:{y:.1f}px;width:{lw:.1f}px;height:{lh:.1f}px;z-index:3">')
    y += lh + 3.2 * u
    # ---------------- vertical budget: hero stamp (square-ish), then the block of stamps takes what is left
    air_h = (1.8 if not wide else 1.3) * u
    scan_h = (15 if not wide else 16) * CM
    cols = 2 if not wide else 4
    rows = math.ceil(len(rest) / cols)
    gap = 2.6 * u if not wide else 2.0 * u
    hw = {61.0: W - 2 * m - 3.0 * u, 76.2: W - 2 * m - 3.0 * u, 91.4: 0.76 * W}.get(wcm, 0.64 * W)
    hh = hw * (1.02 if not wide else 1.00)
    hx = (W - hw) / 2 - (0 if not wide else 0.09 * W)
    hy = y + 3.4 * u
    body.append(stamp(HERO, hx, hy, hw, hh, u, W, H, rot=-1.2, hero=True, uid="hero", z=4))
    # postmark cancelling the lower-right corner (over paper, never over the piece); waves run off the sheet
    D = (0.34 if not wide else 0.22) * W
    body.append(f'<div class="abs" style="left:{hx + hw - D*0.58:.1f}px;top:{hy + hh - D*0.78:.1f}px;z-index:9;transform:rotate(-8deg);transform-origin:{D/2:.0f}px {D/2:.0f}px">'
                f'{postmark_svg(D, K["ink"], "LILAC", W, "hero")}</div>')
    if wide:   # the right margin: the line and the facts
        fx = hx + hw + 5 * u; fwid = W - m - fx
        body.append(f'<div class="abs" style="left:{fx:.1f}px;top:{hy + hh*0.22:.1f}px;width:{fwid:.0f}px;z-index:5">'
                    f'<div class="ital" style="font-size:{2.8*u:.1f}px;line-height:1.1;color:{K["ink"]};margin-bottom:{1.6*u:.1f}px">{E(COPY[HERO]["sub"])}</div>'
                    f'<div class="mono" style="font-size:{0.95*u:.1f}px;letter-spacing:.2em;line-height:1.8;color:{K["ink"]}">WATERPROOF<br>SURGICAL STAINLESS STEEL<br>RHODIUM PLATED</div></div>')
        yb = hy + hh + 3.0 * u
    else:
        body.append(f'<div class="abs ital" style="left:{hx + 1.0*u:.1f}px;top:{hy + hh + 1.6*u:.1f}px;font-size:{2.5*u:.1f}px;color:{K["ink"]};z-index:5">{E(COPY[HERO]["sub"])}</div>')
        yb = hy + hh + 6.6 * u
    # ---------------- the rest of the issue
    tsz = (1.15 if not wide else 0.9) * u
    gbot = H - base_h - air_h - 2.6 * u - scan_h - 2.0 * u
    gw = W - 2 * m - 2 * u
    sw_ = (gw - (cols - 1) * gap) / cols
    top_g = yb + tsz * 3.2
    sh_ = min(sw_ * (1.05 if not wide else 1.28), (gbot - top_g - (rows - 1) * gap * 1.2) / rows)
    sw_ = min(sw_, sh_ / (0.80 if not wide else 1.0))
    blk = rows * sh_ + (rows - 1) * gap * 1.2
    by = top_g + (gbot - top_g - blk) * 0.45
    body.append(f'<div class="abs mono" style="left:{m + u:.1f}px;top:{by - tsz*3.0:.1f}px;font-size:{tsz:.1f}px;letter-spacing:.3em;color:{K["ink"]}">THE REST OF THE ISSUE — {len(rest)} STAMPS</div>')
    rots = [-2.0, 1.6, 1.2, -1.4]
    for i, sku in enumerate(rest):
        r_, c_ = divmod(i, cols)
        n_in = min(cols, len(rest) - r_ * cols)
        tot = cols * sw_ + (cols - 1) * gap
        x = (W - tot) / 2 + c_ * (sw_ + gap) + (cols - n_in) * (sw_ + gap) / 2
        yy = by + r_ * (sh_ + gap * 1.2)
        body.append(stamp(sku, x, yy, sw_, sh_, u, W, H, rot=rots[i % 4], uid=f"g{i}", z=4 + i))
    # ---------------- scan row
    sy = H - base_h - air_h - 2.6 * u - scan_h
    qsw = scan_h * 0.80
    body.append(qr_stamp(m + u, sy + (scan_h - qsw * 1.18) / 2, qsw, qsw * 1.18, u, W, H, "qr", rot=-2.5, z=5))
    tx0 = m + u + qsw + 3.0 * u
    body.append(f'<div class="abs jost" style="left:{tx0:.1f}px;top:{sy + scan_h*0.18:.1f}px;font-size:{scan_h*0.075:.1f}px;letter-spacing:.14em;color:{K["ink"]}">SCAN · SHOP THE ISSUE</div>')
    fsu = min(fit("nairaflore.com", W - m - tx0, track=0), scan_h * 0.30)
    body.append(f'<div class="abs vel" style="left:{tx0 - 0.2*u:.1f}px;top:{sy + scan_h*0.34:.1f}px;font-size:{fsu:.1f}px;color:{K["ink"]}">nairaflore.com</div>')
    body.append(f'<div class="abs mono" style="left:{tx0:.1f}px;top:{sy + scan_h*0.68:.1f}px;font-size:{max(scan_h*0.042, 0.9*u):.1f}px;letter-spacing:.2em;line-height:1.6;color:{K["ink"]};opacity:.85">WATERPROOF · SURGICAL STAINLESS STEEL<br>RHODIUM PLATED</div>')
    # ---------------- airmail border + base
    ay = H - base_h - air_h
    stripe = air_h * 1.6
    body.append(f'<div class="abs" style="left:0;right:0;top:{ay:.1f}px;height:{air_h:.1f}px;background:repeating-linear-gradient(-45deg,{K["ink"]} 0 {stripe:.1f}px,{K["sheet"]} {stripe:.1f}px {stripe*1.5:.1f}px,{K["dot"]} {stripe*1.5:.1f}px {stripe*2.5:.1f}px,{K["sheet"]} {stripe*2.5:.1f}px {stripe*3:.1f}px)"></div>')
    body.append(f'<div class="abs" style="left:0;right:0;bottom:0;height:{base_h:.1f}px;background:{K["ink"]}"></div>')
    return page_html(wcm, hcm, "".join(body), K["sheet"])


if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if not a.startswith("--")] or [s[0] for s in SIZES]
    jobs = [(f"C-lilac-{t}", w, h, build(w, h)) for t, w, h in SIZES if t in only]
    asyncio.run(render_all(jobs, pdf="--nopdf" not in sys.argv))
    print("rendered", [j[0] for j in jobs])
