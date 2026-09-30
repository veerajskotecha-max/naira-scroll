#!/usr/bin/env python3
"""Page 2 of the editable master: a reference sheet for the manufacturer (not for print)."""
import asyncio, base64, io, json, pathlib
import fitz
from playwright.async_api import async_playwright
import build2 as B
import motifs as m

fitz.TOOLS.set_icc(True)
ROOT = pathlib.Path(__file__).parent
M = ROOT / "master"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 17.0, 11.45
LOGO = json.load(open(ROOT / "assets" / "naira-logo-vector.json"))


def cmyk(hexs):
    r, g, b = (int(hexs[i:i + 2], 16) for i in (1, 3, 5))
    pix = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 1, 1), False)
    pix.set_pixel(0, 0, (r, g, b))
    c = fitz.Pixmap(fitz.csCMYK, pix).pixel(0, 0)
    return " ".join(f"{k}{round(v / 255 * 100)}" for k, v in zip("CMYK", c)), (r, g, b)


COLOURS = [("Cream · background", m.CREAM), ("Sage · logo letters", m.LOGO_SAGE), ("Blush · logo flower", m.LOGO_BLUSH),
           ("Coral · tulip", m.CORAL), ("Coral deep · tulip", m.CORAL_DEEP), ("Coral light · tulip", m.CORAL_LIGHT),
           ("Coral back petals", m.CORAL_BACK), ("Leaf sage", m.SAGE), ("Leaf sage deep", m.SAGE_DEEP),
           ("Leaf sage light", m.SAGE_LIGHT), ("Ink · text and QR", m.INK)]


def preview_png():
    """Page 1 of the editable master, dieline visible, as the picture on this sheet."""
    d = fitz.open(M / "Naira-DCut-Bag-6x9.5x2-EDITABLE.pdf")
    pix = d[0].get_pixmap(dpi=150)
    return base64.b64encode(pix.tobytes("png")).decode()


def html():
    rows = []
    for name, hx in COLOURS:
        c, (r, g, b) = cmyk(hx)
        rows.append(f'<tr><td><i style="background:{hx}"></i></td><td>{name}</td><td>{hx}</td><td>{r} {g} {b}</td><td>{c}</td></tr>')
    logo = (f'<svg viewBox="0 0 {LOGO["width"]} {LOGO["height"]}" style="height:.62in;display:block;margin-left:-.06in">'
            f'<path d="{LOGO["letters"]}" fill="{m.LOGO_SAGE}" fill-rule="evenodd"/><path d="{LOGO["flower"]}" fill="{m.LOGO_BLUSH}" fill-rule="evenodd"/></svg>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:18in 12in;margin:0}}
@font-face{{font-family:"Jost";src:url(data:font/woff2;base64,{B.b64(B.FONTS/'Jost-400.woff2')}) format("woff2");font-weight:400}}
@font-face{{font-family:"Jost";src:url(data:font/woff2;base64,{B.b64(B.FONTS/'Jost-500.woff2')}) format("woff2");font-weight:500}}
@font-face{{font-family:"Corm";src:url(data:font/woff2;base64,{B.b64(B.FONTS/'Cormorant-400-italic.woff2')}) format("woff2");font-style:italic}}
html{{margin:0;padding:0;background:transparent}}
body{{margin:0;background:#fff;width:{W}in;height:{H}in;box-sizing:border-box;overflow:hidden;padding:.55in .6in;font-family:"Jost",sans-serif;color:{m.INK};
     display:grid;grid-template-columns:10.35in 1fr;grid-template-rows:auto 1fr;column-gap:.5in;row-gap:.3in;-webkit-font-smoothing:antialiased}}
header{{grid-column:1/3;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:1px solid #D9CFC6;padding-bottom:.18in}}
header .t{{font-family:"Corm";font-style:italic;font-size:26pt;line-height:1;margin-top:.06in}}
header .r{{text-align:right;font-size:9.5pt;letter-spacing:.14em;text-transform:uppercase;color:#8B7E74;line-height:1.7}}
header .r b{{color:#C4006A;font-weight:500}}
figure{{margin:0}}
figure img{{width:10.35in;display:block;border:1px solid #E6DDD5}}
figcaption{{font-size:8.5pt;color:#8B7E74;margin-top:.1in;letter-spacing:.02em}}
aside{{font-size:9pt;line-height:1.5}}
h3{{font-size:8pt;font-weight:500;letter-spacing:.2em;text-transform:uppercase;color:#6C8A7C;margin:.2in 0 .06in}}
h3:first-child{{margin-top:0}}
dl{{display:grid;grid-template-columns:1.25in 1fr;gap:.03in .12in;margin:0}}
dt{{color:#8B7E74}} dd{{margin:0}}
table{{border-collapse:collapse;width:100%;font-size:8.2pt}}
td{{padding:.022in .05in .022in 0;border-bottom:1px solid #EFE8E2;white-space:nowrap}}
td i{{display:inline-block;width:.16in;height:.16in;border-radius:50%;border:1px solid #D9CFC6;vertical-align:middle}}
ul{{margin:0;padding-left:.16in}} li{{margin:.02in 0}}
</style></head><body>
<header><div>{logo}<div class="t">D-cut handle bag · 6 × 9.5 × 2 in</div></div>
<div class="r">Print specification · page 2 of 2<br><b>Reference only · do not print this page</b><br>Artwork is page 1</div></header>
<figure><img src="data:image/png;base64,{preview_png()}">
<figcaption>Page 1 with the dieline layer switched on. Magenta = cut, cyan dashed = fold. The dieline layer is set to not print.</figcaption></figure>
<aside>
<h3>Size</h3>
<dl><dt>Bag</dt><dd>6 in wide × 9.5 in tall × 2 in gusset</dd>
<dt>Flat artwork</dt><dd>16.75 × 11.2 in trim, 0.125 in bleed on every side (page 17 × 11.45 in)</dd>
<dt>Panels, left to right</dt><dd>gusset 2 · front 6 · gusset 2 · back 6 · glue 0.75 in. Each gusset folds on its centre line.</dd>
<dt>Base</dt><dd>base fold at 9.5 in, gusset fold 1 in above it, bottom flap 1.7 in</dd>
<dt>Handle</dt><dd>D-cut 2.3 × 1.0 in, 1.05 in below the top edge, centred on front and back</dd></dl>
<h3>Colours · document is sRGB</h3>
<table><tr><td></td><td></td><td>HEX</td><td>RGB</td><td>CMYK approx.</td></tr>{''.join(rows)}</table>
<h3>Type</h3>
<dl><dt>Eyebrow, QR line</dt><dd>Jost Regular and Medium</dd><dt>Tagline</dt><dd>Cormorant Garamond Light Italic</dd>
<dt>Logo</dt><dd>vector paths, not a font</dd></dl>
<h3>Notes for production</h3>
<ul><li>Layers: background, leaf pattern, florals, logo, QR, text, dieline. Everything is vector except the leaf pattern (2048 px images, above 850 ppi at size).</li>
<li>Print as sRGB on digital, or convert to your press profile. CMYK values above are a guide for matching.</li>
<li>The glue flap carries plain cream only. Keep it free of lamination or varnish.</li>
<li>QR (0.85 in) opens nairaflore.com/jewellery. Keep its cream quiet zone and do not scale it below 0.75 in.</li>
<li>The dieline is reconstructed from the Kraftix 6 × 9.5 × 2 template. Align the artwork to your own die before cutting.</li>
<li>Need to retype text? Install Jost and Cormorant Garamond (free, Google Fonts), or use the PRINT-READY file where text is already outlined.</li></ul>
</aside></body></html>"""


async def main():
    f = M / "spec.html"
    f.write_text(html(), encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        pg = await b.new_page()
        await pg.goto(f.as_uri())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.pdf(path=str(M / "spec.pdf"), width="18in", height="12in",
                     margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}, print_background=True)
        await b.close()
    d = fitz.open(M / "spec.pdf")
    print("spec pages", len(d), f"{d[0].rect.width/72:.2f} x {d[0].rect.height/72:.2f} in",
          "fonts", [x[3] for x in d[0].get_fonts(full=True)])


if __name__ == "__main__":
    asyncio.run(main())
