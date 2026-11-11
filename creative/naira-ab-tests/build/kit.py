"""Shared kit for the Naira Ten: fonts, logo, the collection colour code, tabs, and the renderer.

Colour code (every ad carries a tab in its collection's colour, named after an Indian colour):
  EARRINGS  Haldi    #F2B705   RINGS      Sindoor #C1272D   NECKLACES Neelam #1D3C8F
  BRACELETS Rani     #C2185B   SHOP ALL   Mehendi #2F6B3A
"""
import asyncio, base64, json, re, html as H
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright

S = Path('/tmp/claude-0/-home-user-naira-scroll/3afe135e-ba9d-5fe5-a4de-8088e2e02a7f/scratchpad')
T = S / 'ab2'; F1 = S / 'labels' / 'fonts'; F2 = S / 'ten' / 'fonts'
OUT = T / 'out'; OUT.mkdir(exist_ok=True); (T / 'html').mkdir(exist_ok=True)
LIVE = json.load(open(S / 'camp' / 'data' / 'live.json')); STOCK = json.load(open(S / 'camp' / 'data' / 'inventory.json'))
LOGO = json.load(open('/home/user/naira-scroll/creative/naira-bag/build/assets/naira-logo-vector.json'))
CHROME = '/opt/pw-browsers/chromium'
FEED, STORY = (1080, 1350), (1080, 1920)
INK, CREAM = '#1F1A14', '#FBF5EA'
COLL = {
    'earrings': dict(label='EARRINGS', hex='#F2B705', ink=INK, name='Haldi'),
    'rings': dict(label='RINGS', hex='#C1272D', ink=CREAM, name='Sindoor'),
    'necklaces': dict(label='NECKLACES', hex='#1D3C8F', ink=CREAM, name='Neelam'),
    'bracelets': dict(label='BRACELETS', hex='#C2185B', ink=CREAM, name='Rani'),
    'all': dict(label='SHOP ALL', hex='#2F6B3A', ink=CREAM, name='Mehendi'),
}
LINK = {'earrings': 'https://nairaflore.com/collections/earrings', 'rings': 'https://nairaflore.com/collections/rings',
        'necklaces': 'https://nairaflore.com/collections/necklaces', 'bracelets': 'https://nairaflore.com/collections/bracelets',
        'all': 'https://nairaflore.com/collections/shop-all'}
UTM = 'utm_source=meta&utm_medium=paid&utm_campaign=naira-ten-nov26&utm_content={id}'
OFFER = 'Buy 2, 10% off · Buy 3, 20% off'
TRUST = 'Free insured shipping · Cash on delivery'


def b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def uri(p):
    p = Path(p); mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp'}[p.suffix.lower()]
    return f'data:{mime};base64,{b64(p)}'


def face(fam, path, weight=400, style='normal', rng=None):
    fmt = 'truetype' if str(path).endswith('.ttf') else 'woff2'
    r = f'unicode-range:{rng};' if rng else ''
    return (f"@font-face{{font-family:'{fam}';src:url(data:font/{fmt};base64,{b64(path)}) format('{fmt}');"
            f"font-weight:{weight};font-style:{style};font-display:block;{r}}}")


R = 'U+20B9'
FONT_CSS = ''.join([
    face('Velista', F1 / 'Velista.ttf'), face('RupeeV', F1 / 'Laila-300-r.woff2', 400, rng=R),
    face('JostF', F1 / 'Jost-300.woff2', 300), face('JostF', F1 / 'Jost-400.woff2', 400), face('JostF', F1 / 'Jost-500.woff2', 500),
    face('Rupee', F1 / 'Poppins-400-deva.woff2', 300, rng=R), face('Rupee', F1 / 'Poppins-400-deva.woff2', 400, rng=R), face('Rupee', F1 / 'Poppins-500-deva.woff2', 500, rng=R),
    face('CormI', F1 / 'CormorantGaramond-300i.woff2', 400, 'italic'), face('CormR', F1 / 'CormorantGaramond-300-r.woff2', 400, 'italic', rng=R),
    face('Corm', F1 / 'CormorantGaramond-500-latin.woff2', 500), face('Corm', F1 / 'CormorantGaramond-400-latin.woff2', 400),
    face('Kalam', F2 / 'Kalam-400-latin.woff2', 400), face('Kalam', F2 / 'Kalam-700-latin.woff2', 700),
    face('KalamR', F2 / 'Kalam-400-devanagari.woff2', 400, rng=R), face('KalamR', F2 / 'Kalam-700-devanagari.woff2', 700, rng=R),
    face('Plex', F2 / 'IBMPlexMono-400-latin.woff2', 400), face('Plex', F2 / 'IBMPlexMono-500-latin.woff2', 500),
    face('Rozha', F2 / 'RozhaOne-400-latin.woff2', 400), face('RozhaR', F2 / 'RozhaOne-400-devanagari.woff2', 400, rng=R),
])

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#000}
body{-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}
.card{position:relative;overflow:hidden}
.display{font-family:'RupeeV','Velista',serif;font-weight:400;letter-spacing:.01em;line-height:.95}
.sans{font-family:'Rupee','JostF',sans-serif}
.serif-i{font-family:'CormR','CormI',serif;font-style:italic}
.hand{font-family:'KalamR','Kalam',cursive}
.mono{font-family:'Plex',ui-monospace,monospace}
.fat{font-family:'RozhaR','Rozha',serif}
.eyebrow{font-family:'Rupee','JostF',sans-serif;font-weight:500;letter-spacing:.24em;text-transform:uppercase}
.tab{position:absolute;display:flex;align-items:center;gap:12px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:19px;letter-spacing:.24em;padding:0 22px;height:58px}
.tab i{display:block;width:12px;height:12px;border-radius:50%;border:2px solid currentColor}
"""


def esc(t):
    return H.escape(t, quote=False)


def inr(n):
    s = str(int(round(n)))
    if len(s) <= 3: return '₹' + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2: parts.insert(0, head[-2:]); head = head[:-2]
    return '₹' + ','.join([head] + parts) + ',' + tail


def logo(w, letters=CREAM, flower='#FFBDA8', style=''):
    px = py = 65
    vw, vh = LOGO['width'] - 2 * px, LOGO['height'] - 2 * py
    return (f"<svg class='logo' style='width:{w}px;height:{w * vh / vw:.1f}px;{style}' viewBox='{px} {py} {vw} {vh}'>"
            f"<path d='{LOGO['letters']}' fill='{letters}' fill-rule='evenodd'/><path d='{LOGO['flower']}' fill='{flower}' fill-rule='evenodd'/></svg>")


def tab(coll, x='right:56px', y='top:0', radius='0 0 14px 14px', extra='', invert=False):
    """The collection tab. invert=True when the ground is already the collection colour: cream tab, colour text."""
    c = COLL[coll]
    bg, fg = (CREAM, c['hex']) if invert else (c['hex'], c['ink'])
    return (f"<div class='tab' style='{x};{y};background:{bg};color:{fg};border-radius:{radius};{extra}'>"
            f"<i></i>{c['label']}</div>")


def doc(w, h, css, body):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS}{BASE_CSS}{css}</style></head>"
            f"<body><div class='card' style='width:{w}px;height:{h}px'>{body}</div></body></html>")


CHECK = """(story) => {
  const bad = [];
  const card = document.querySelector('.card');
  document.querySelectorAll('.fit').forEach(e => { if (e.scrollWidth > e.clientWidth + 1 || e.scrollHeight > e.clientHeight + 1) bad.push('overflow: ' + (e.id || e.className)); });
  if (story) document.querySelectorAll('.safe').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && (r.top < 269 || r.bottom > 1536)) bad.push('outside story safe zone: ' + (e.id || e.className) + ' ' + Math.round(r.top) + '-' + Math.round(r.bottom)); });
  const fonts = [...document.fonts].filter(f => f.status === 'error').map(f => f.family + ' ' + f.weight);
  return {bad, fonts};
}"""


async def _render(jobs):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        res = {}
        for name, html_doc, (w, h) in jobs:
            f = T / 'html' / f'{name}.html'; f.write_text(html_doc)
            pg = await b.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            await pg.goto(f.as_uri(), wait_until='networkidle')
            await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(250)
            res[name] = await pg.evaluate(CHECK, h > w * 1.5)
            png = OUT / f'{name}.png'
            await pg.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            await pg.close()
            Image.open(png).convert('RGB').save(OUT / f'{name}.jpg', 'JPEG', quality=92, subsampling=0, optimize=True)
            png.unlink()
        await b.close()
    for k, v in res.items():
        print(f"{k:34s} {'OK' if not (v['bad'] or v['fonts']) else v}")
    return res


def render(jobs):
    return asyncio.run(_render(jobs))


def fit_cover(img, w, h, fx=0.5, fy=0.5):
    """Crop a PIL image to w x h around focus (fx, fy), scaling to cover."""
    W, Hh = img.size
    s = max(w / W, h / Hh)
    img = img.resize((max(w, round(W * s)), max(h, round(Hh * s))), Image.LANCZOS)
    W, Hh = img.size
    x = min(max(round(fx * W - w / 2), 0), W - w); y = min(max(round(fy * Hh - h / 2), 0), Hh - h)
    return img.crop((x, y, x + w, y + h))
