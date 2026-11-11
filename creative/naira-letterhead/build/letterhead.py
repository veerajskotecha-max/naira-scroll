"""NAIRA letterhead, A4 (210 x 297 mm). White paper, nothing within 6 mm of the edge, so it prints on any office printer.
Same grammar as the floral card and the bag: the card's tulips in the corners, the wordmark in its own sage and blush,
the eyebrow line, and a contact footer."""
import asyncio, base64, json, sys
from pathlib import Path
sys.path.insert(0, '/home/user/naira-scroll/creative/naira-bag/build')
from motifs import cluster, dots, CORAL, INK, LOGO_SAGE, LOGO_BLUSH, SAGE
from playwright.async_api import async_playwright

HERE = Path(__file__).resolve().parent
FONTS = Path('/home/user/naira-scroll/creative/naira-bag/fonts')
LOGO = json.load(open('/home/user/naira-scroll/creative/naira-bag/build/assets/naira-logo-vector.json'))
W_MM, H_MM = 210.0, 297.0
IN = 25.4
EYEBROW = '[ 18k gold coated · rhodium coated ]'
CONTACT = ['nairaflore.com', '@nairaflore', 'WhatsApp +91 95615 57935', 'shopatnaira@gmail.com']
TAG = 'made to stay gold.'


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def logo(x, y, w):
    px = py = 65
    vw, vh = LOGO['width'] - 2 * px, LOGO['height'] - 2 * py
    h = w * vh / vw
    return (f"<svg x='{x - w / 2:.3f}' y='{y:.3f}' width='{w:.3f}' height='{h:.3f}' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{LOGO['letters']}' fill='{LOGO_SAGE}' fill-rule='evenodd'/><path d='{LOGO['flower']}' fill='{LOGO_BLUSH}' fill-rule='evenodd'/></svg>"), h


def page(guides=False):
    Wi, Hi = W_MM / IN, H_MM / IN
    ins = 9.5 / IN                                  # motif frames 9.5 mm in: leaves end 6.5 mm or more from the edge
    top = [*cluster('tl', ins, ins + .02, Wi - 2 * ins, Hi, .66), *cluster('tr', ins, ins + .02, Wi - 2 * ins, Hi, .66)]
    bot = [*cluster('bl', ins, 0, Wi - 2 * ins, Hi - ins + .05, .44), *cluster('br', ins, 0, Wi - 2 * ins, Hi - ins + .05, .44)]
    sprinkle = dots([(1.95, .62), (6.35, .55), (2.45, 1.32), (5.85, 1.38)], r=.022)
    lg, lh = logo(W_MM / 2, 17.5, 62)
    eb_y = 17.5 + lh + 7.4
    sep = "\u2002\u2009<tspan fill='#A8957E'>·</tspan>\u2009\u2002"
    contact = sep.join(CONTACT)
    css = f"""
@font-face{{font-family:'JostF';src:url(data:font/woff2;base64,{b64(FONTS / 'Jost-400.woff2')}) format('woff2');font-weight:400}}
@font-face{{font-family:'JostM';src:url(data:font/woff2;base64,{b64(FONTS / 'Jost-500.woff2')}) format('woff2');font-weight:500}}
@font-face{{font-family:'Corm';src:url(data:font/woff2;base64,{b64(FONTS / 'Cormorant-400-italic.woff2')}) format('woff2');font-style:italic}}
.eb{{font-family:'JostF',sans-serif;font-size:2.55px;letter-spacing:.62px;fill:{INK}}}
.ct{{font-family:'JostF',sans-serif;font-size:2.7px;letter-spacing:.15px;fill:{INK}}}
.tg{{font-family:'Corm',serif;font-style:italic;font-size:4.1px;fill:{INK}}}
"""
    parts = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W_MM}mm' height='{H_MM}mm' viewBox='0 0 {W_MM} {H_MM}'>",
             f"<style>{css}</style><rect width='{W_MM}' height='{H_MM}' fill='#FFFFFF'/>",
             f"<g transform='scale({IN})'>{''.join(top)}{''.join(bot)}{sprinkle}</g>",
             lg,
             f"<text x='{W_MM / 2}' y='{eb_y:.2f}' class='eb' text-anchor='middle'>{EYEBROW}</text>",
             f"<rect x='{W_MM / 2 - 9}' y='{eb_y + 4.6:.2f}' width='18' height='.32' fill='{LOGO_SAGE}'/>",
             f"<line x1='40' y1='271.2' x2='170' y2='271.2' stroke='{LOGO_SAGE}' stroke-width='.28'/>",
             f"<text x='{W_MM / 2}' y='278.4' class='ct' text-anchor='middle'>{contact}</text>",
             f"<text x='{W_MM / 2}' y='285.6' class='tg' text-anchor='middle'>{TAG}</text>"]
    if guides:
        parts.append(f"<rect x='20' y='{eb_y + 14:.1f}' width='170' height='{265 - eb_y - 14:.1f}' fill='none' stroke='#2AA6A0' stroke-width='.3' stroke-dasharray='2 1.5'/>")
    parts.append('</svg>')
    return '\n'.join(parts), eb_y


async def to_pdf(svg, pdf, png=None):
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>@page{{size:A4;margin:0}}html,body{{margin:0;padding:0;background:#fff}}"
            f"svg{{display:block}}</style></head><body>{svg}</body></html>")
    f = HERE / (Path(pdf).stem + '.html'); f.write_text(html)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        pg = await b.new_page()
        await pg.goto(f.as_uri(), wait_until='networkidle'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
        await pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
        await b.close()


if __name__ == '__main__':
    svg, eb_y = page()
    asyncio.run(to_pdf(svg, HERE / 'Naira-Letterhead-A4.pdf'))
    svg2, _ = page(guides=True)
    asyncio.run(to_pdf(svg2, HERE / 'guides.pdf'))
    print('eyebrow y', round(eb_y, 1), 'writing area starts ~', round(eb_y + 14, 1), 'mm')
