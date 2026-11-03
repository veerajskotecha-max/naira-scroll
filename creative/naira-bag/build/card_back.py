#!/usr/bin/env python3
"""The back of the NAIRA floral card (2.77 x 2.76 in + 0.125 in bleed), in the same grammar as the front:
cream ground with the site's leaves, tulips in the two top corners, a thank-you line in Cormorant, a QR to
nairaflore.com/jewellery (as on the bag), the care line from the catalogue, and the WhatsApp number."""
import segno
from build2 import *          # ground, cluster, dots, defs, style, html, LOGO, CREAM, INK, LOGO_SAGE, QR_URL, ...

WHATSAPP = "+91 95615 57935"
CARE = ("Put perfume on before your jewellery, not after,", "and keep each piece in its box between wears.")


def back_layers(x0, y0, k=0.34):
    w, h = CARD_W, CARD_H
    cx = x0 + w / 2
    g = [f'<ellipse cx="{cx}" cy="{y0 + 1.45}" rx="1.25" ry="1.2" fill="url(#halo)"/>']
    for kind in ("tl", "tr"):                                 # tulips on top; the bottom stays clear for the care text
        g += cluster(kind, x0, y0, w, h, k)
    g += [dots([(cx - 1.05, y0 + 1.25), (cx + 1.1, y0 + 1.0), (cx + 1.05, y0 + 1.7), (cx - 1.1, y0 + 1.95)], r=.011)]
    # thank-you line
    g += [f'<text x="{cx}" y="{y0 + .80}" class="ty" text-anchor="middle">thank you</text>',
          f'<text x="{cx}" y="{y0 + 1.0}" class="ty2" text-anchor="middle">for choosing Naira.</text>']
    # QR with its cream quiet zone
    size, top = 0.6, y0 + 1.1
    q = segno.make(QR_URL, error="m")
    n = q.symbol_size(scale=1, border=0)[0]
    d = "".join(f"M{x},{y}h1v1h-1z" for y, row in enumerate(q.matrix_iter(scale=1, border=0)) for x, v in enumerate(row) if v)
    m = size / n
    g += [f'<rect x="{cx - size/2 - 3*m}" y="{top - 3*m}" width="{size + 6*m}" height="{size + 6*m}" fill="{CREAM}"/>',
          f'<g transform="translate({cx - size/2},{top}) scale({m})"><path d="{d}" fill="{INK}"/></g>',
          f'<text x="{cx}" y="{top + size + .13}" class="url" text-anchor="middle">nairaflore.com/jewellery</text>']
    # care and contact
    y = top + size + .29
    g += [f'<rect x="{cx - .17}" y="{y - .06}" width=".34" height=".008" fill="{LOGO_SAGE}"/>',
          f'<text x="{cx}" y="{y + .09}" class="care-h" text-anchor="middle">CARE</text>',
          f'<text x="{cx}" y="{y + .21}" class="care" text-anchor="middle">{CARE[0]}</text>',
          f'<text x="{cx}" y="{y + .315}" class="care" text-anchor="middle">{CARE[1]}</text>',
          f'<text x="{cx}" y="{y + .47}" class="care-h" text-anchor="middle">WHATSAPP {WHATSAPP}</text>']
    return g


def back_page(guides=False):
    W, H = CARD_W + 2 * BLEED, CARD_H + 2 * BLEED
    bg = ground(W, H, 33.5, 31.0, k=0.46, seed=11)           # its own patch of the shared pattern space
    extra = """<style>
  .ty{font-family:"Cormorant",serif;font-style:italic;font-size:.27px;fill:#3D3530}
  .ty2{font-family:"Cormorant",serif;font-style:italic;font-size:.15px;fill:#3D3530}
  .url{font-family:"JostF",sans-serif;font-size:.062px;letter-spacing:.012px;fill:#3D3530}
  .care-h{font-family:"JostM",sans-serif;font-size:.052px;letter-spacing:.022px;fill:#3D3530}
  .care{font-family:"JostF",sans-serif;font-size:.06px;letter-spacing:.004px;fill:#3D3530}
</style>"""
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}in" height="{H}in" viewBox="0 0 {W} {H}">',
             defs(), style(0.46), extra,
             f'<image href="data:image/png;base64,{b64img(bg, "PNG", optimize=True)}" x="0" y="0" width="{W}" height="{H}" preserveAspectRatio="none"/>']
    parts += back_layers(BLEED, BLEED)
    if guides:
        parts.append(f'<rect x="{BLEED}" y="{BLEED}" width="{W-2*BLEED}" height="{H-2*BLEED}" fill="none" stroke="#E0457B" stroke-width=".014"/>')
        parts.append(f'<text x="{W/2}" y="{H - .05}" class="g" text-anchor="middle">pink = cut line · bleed 0.125" · {W:.3g} × {H:.3g} in · back</text>')
    parts.append("</svg>")
    return "\n".join(parts), W, H


if __name__ == "__main__":
    for guides, name in ((False, "card_back"), (True, "card_back_proof")):
        svg, W, H = back_page(guides)
        (OUT / f"{name}.html").write_text(html(svg, W, H).replace("@page{size:3.02in 3.01in;", "@page{size:218pt 217pt;")
                                          .replace("font-size:.11px;fill:#C0392B", "font-size:.045px;fill:#C0392B"), encoding="utf-8")
        print(name, W, H)
