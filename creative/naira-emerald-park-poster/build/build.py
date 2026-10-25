"""NAIRA PETITE · thank-you poster for the Emerald Park pop-up (Nashik, October 2026).
4:5 feed (1080 x 1350 CSS px) and 9:16 Status (1080 x 1920), rendered at 2x with Chromium."""
import asyncio, json, re, sys, math
from pathlib import Path
from playwright.async_api import async_playwright

P = Path(__file__).resolve().parent
REPO = Path("/home/user/naira-scroll")
sys.path.insert(0, str(REPO / "creative" / "naira-bag" / "build"))
import motifs as M

CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
LOGO = json.load(open(REPO / "creative" / "naira-bag" / "build" / "assets" / "naira-logo-vector.json"))
SRC_W, SRC_Y0 = 1512, 640          # display.png = source x 0..1512, y 640..2016, at 2x

CREAM, BLUSH, GOLD, GOLD_LT, INK_SOFT = "#F6EFE6", "#F2CFC4", "#D6B26A", "#EBD39C", "#E9D9C6"


def logo_svg(h, letters=CREAM, flower=M.LOGO_BLUSH):
    px = py = 65
    vw, vh = LOGO["width"] - 2 * px, LOGO["height"] - 2 * py
    return (f"<svg viewBox='{px} {py} {vw} {vh}' style='height:{h}px;display:block;margin:0 auto' role='img' aria-label='NAIRA'>"
            f"<path d='{LOGO['letters']}' fill='{letters}' fill-rule='evenodd'/>"
            f"<path d='{LOGO['flower']}' fill='{flower}' fill-rule='evenodd'/></svg>")


def flower_bbox():
    nums = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", LOGO["flower"])]
    xs, ys = nums[0::2], nums[1::2]
    return min(xs), min(ys), max(xs), max(ys)


def stamp(cx, cy, size, colour=GOLD, rot=-11, n=6):
    """Round postmark centred on (cx, cy): double ring, the pop-up's name set around the edge, the NAIRA
    flower in the middle, and n wave segments of cancellation lines running off to the left."""
    fx0, fy0, fx1, fy1 = flower_bbox()
    fw, fh = fx1 - fx0, fy1 - fy0
    fs = 60 / fh
    ring = "THE EMERALD PARK POP-UP \u00b7 NASHIK \u00b7 OCTOBER 2026 \u00b7"
    x0 = 6 - n * 25 - 6
    waves = "".join(
        f"<path d='M{6 - n * 25},{y} " + " ".join(f"q12.5,{-7 if i % 2 == 0 else 7} 25,0" for i in range(n)) +
        f"' stroke='{colour}' stroke-width='2.2' fill='none' opacity='.75'/>" for y in (72, 88, 104, 120)) if n else ""
    sc = size / 200
    w = (200 - x0) * sc
    ox, oy = (100 - x0) * sc, 100 * sc
    return f"""
<svg viewBox='{x0} 0 {200 - x0} 200' style='position:absolute;left:{cx - ox:.1f}px;top:{cy - oy:.1f}px;width:{w:.1f}px;height:{size}px;
  transform-origin:{ox:.1f}px {oy:.1f}px;transform:rotate({rot}deg)' aria-hidden='true'>
  {waves}
  <circle cx='100' cy='100' r='94' fill='none' stroke='{colour}' stroke-width='2.6'/>
  <circle cx='100' cy='100' r='86' fill='none' stroke='{colour}' stroke-width='1.2'/>
  <circle cx='100' cy='100' r='52' fill='none' stroke='{colour}' stroke-width='1.2'/>
  <defs><path id='rp{cx:.0f}' d='M100,100 m-69,0 a69,69 0 1,1 138,0 a69,69 0 1,1 -138,0'/></defs>
  <text font-family='JostF' font-weight='500' font-size='12.4' fill='{colour}'>
    <textPath href='#rp{cx:.0f}' startOffset='0' textLength='428' lengthAdjust='spacing'>{ring}</textPath></text>
  <g transform='translate({100 - fw * fs / 2 - fx0 * fs:.2f},{100 - fh * fs / 2 - fy0 * fs - 7:.2f}) scale({fs:.5f})'>
    <path d='{LOGO["flower"]}' fill='{colour}' fill-rule='evenodd'/></g>
  <text x='100' y='138' text-anchor='middle' font-family='JostF' font-weight='500' font-size='10' letter-spacing='3' fill='{colour}'>POP-UP</text>
</svg>"""


def tulips_svg(kind, size, flip=False):
    """The gift bag's tulip corner, drawn from the bag's own motif code."""
    parts = "".join(M.cluster(kind, 0, 0, 2.2, 2.2, 1.0))
    t = " transform='translate(2.2,0) scale(-1,1)'" if flip else ""
    return (f"<svg viewBox='-0.3 -0.1 2.5 2.1' style='width:{size}px;height:{size * 2.1 / 2.5}px;display:block' aria-hidden='true'>"
            f"<g{t}>{parts}</g></svg>")


def glint(x, y, s, op=.9):
    return (f"<svg class='glint' style='left:{x - s / 2}px;top:{y - s / 2}px;width:{s}px;height:{s}px;opacity:{op}' viewBox='-50 -50 100 100' aria-hidden='true'>"
            f"<path d='M0,-50 C4,-8 8,-4 50,0 C8,4 4,8 0,50 C-4,8 -8,4 -50,0 C-8,-4 -4,-8 0,-50 Z' fill='#FFF6DE'/>"
            f"<circle r='9' fill='#FFFFFF'/></svg>")


def fonts_css():
    f = "url(fonts/{}) format('{}')"
    return "".join([
        f"@font-face{{font-family:'Velista';src:{f.format('Velista.ttf', 'truetype')}}}",
        f"@font-face{{font-family:'JostF';src:{f.format('Jost-300.woff2', 'woff2')};font-weight:300}}",
        f"@font-face{{font-family:'JostF';src:{f.format('Jost-400-full.woff2', 'woff2')};font-weight:400}}",
        f"@font-face{{font-family:'JostF';src:{f.format('Jost-500-full.woff2', 'woff2')};font-weight:500}}",
        f"@font-face{{font-family:'CormI';src:{f.format('CormorantGaramond-italic-var.woff2', 'woff2')};font-style:italic;font-weight:300 700}}",
    ])


CSS = """
* { margin:0; padding:0; box-sizing:border-box }
html, body { background:#0B2A20 }
.canvas { position:relative; overflow:hidden; width:1080px; color:#F6EFE6;
  background: radial-gradient(ellipse 75% 55% at 50% 58%, #1D5240 0%, #163F31 38%, #102F24 70%, #0A231B 100%) }
.abs { position:absolute }
.center { left:50%; transform:translateX(-50%); text-align:center }
.grain { position:absolute; inset:0; opacity:.10; mix-blend-mode:overlay; pointer-events:none }
.frame { position:absolute; border:1.2px solid rgba(214,178,106,.55) }
.frame::after { content:''; position:absolute; inset:5px; border:.8px solid rgba(214,178,106,.32) }
.kick { font-family:'JostF',sans-serif; font-weight:500; letter-spacing:.34em; text-transform:uppercase; color:#E9D9C6; white-space:nowrap }
.head { font-family:'Velista',Georgia,serif; white-space:nowrap; line-height:1; letter-spacing:.015em;
  background: linear-gradient(176deg, #FBEFC9 0%, #E9CC8A 28%, #C99B4E 52%, #F1DCA2 70%, #B98A43 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
  filter: drop-shadow(0 2px 0 rgba(0,0,0,.18)) drop-shadow(0 10px 24px rgba(0,0,0,.30)) }
.it { font-family:'CormI',Georgia,serif; font-style:italic; font-weight:400; color:#F2CFC4; white-space:nowrap; line-height:1.1 }
.glow { position:absolute; border-radius:50%; background: radial-gradient(closest-side, rgba(120,190,160,.30), rgba(120,190,160,.10) 55%, rgba(120,190,160,0)) }
.disp { position:absolute; display:block; filter: drop-shadow(0 26px 40px rgba(2,12,8,.55)) }
.glint { position:absolute; pointer-events:none; mix-blend-mode:screen }
.fade { position:absolute; left:0; width:1080px; background:linear-gradient(to bottom, rgba(11,36,28,0) 0%, rgba(11,36,28,.82) 48%, rgba(10,34,26,.96) 100%) }
.foot { font-family:'JostF',sans-serif; font-weight:400; letter-spacing:.14em; color:#F6EFE6; white-space:nowrap }
.foot2 { font-family:'JostF',sans-serif; font-weight:300; letter-spacing:.08em; color:#E9D9C6; white-space:nowrap }
.rule { height:0; border-top:1px solid rgba(214,178,106,.6) }
"""

GRAIN = ("<svg class='grain' xmlns='http://www.w3.org/2000/svg' width='100%' height='100%'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 1 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(#n)'/></svg>")


def place(left, top, width):
    k = width / SRC_W
    return k, (lambda sx, sy: (left + sx * k, top + (sy - SRC_Y0) * k))


def feed():
    H = 1350
    dl, dt, dw = -50, 396, 1180
    k, at = place(dl, dt, dw)
    glints = glint(*at(373, 894), 30) + glint(*at(672, 725), 24, .85) + glint(*at(485, 1028), 22, .75) + glint(*at(1059, 875), 20, .7)
    return H, f"""
<div class='canvas' style='height:{H}px'>
  {GRAIN}
  <div class='frame' style='left:22px;top:22px;right:22px;bottom:22px'></div>
  <div class='abs' style='left:-34px;top:-14px'>{tulips_svg('tl', 250)}</div>
  <div class='abs' style='right:-34px;top:-14px'>{tulips_svg('tl', 250, flip=True)}</div>
  <div class='abs' style='left:0;top:52px;width:1080px'>{logo_svg(44)}</div>
  <div class='abs kick center' style='top:118px;font-size:13px'>Naira Petite &nbsp;·&nbsp; Nashik &nbsp;·&nbsp; October 2026</div>
  <div class='abs head center' id='hd' style='top:146px;font-size:150px'>THANK YOU</div>
  <div class='abs it center' style='top:298px;font-size:40px'>for visiting our Emerald Park pop-up.</div>
  <div class='glow' style='left:60px;top:330px;width:960px;height:620px'></div>
  <img class='disp' src='display.png' style='left:{dl}px;top:{dt}px;width:{dw}px' alt=''>
  {glints}
  {stamp(842, 452, 140, n=4)}
  <div class='fade' style='top:1150px;height:200px'></div>
  <div class='abs it center' style='top:1238px;font-size:24px;color:#F2CFC4'>Missed it? The collection is always online.</div>
  <div class='abs foot center' style='top:1276px;font-size:15px'>NAIRAFLORE.COM &nbsp;·&nbsp; WHATSAPP +91 95615 57935</div>
  <div class='abs foot2 center' style='top:1304px;font-size:12.5px'>Demi-fine jewellery &nbsp;[ 18k gold coated · rhodium coated ]</div>
</div>"""


def story():
    H = 1920
    dl, dt, dw = -80, 842, 1240
    k, at = place(dl, dt, dw)
    glints = glint(*at(373, 894), 34) + glint(*at(672, 725), 27, .85) + glint(*at(485, 1028), 24, .75) + glint(*at(1059, 875), 22, .7)
    return H, f"""
<div class='canvas' style='height:{H}px'>
  {GRAIN}
  <div class='frame' style='left:26px;top:26px;right:26px;bottom:26px'></div>
  <div class='abs' style='left:-40px;top:40px'>{tulips_svg('tl', 300)}</div>
  <div class='abs' style='right:-40px;top:40px'>{tulips_svg('tl', 300, flip=True)}</div>
  <div class='abs' style='left:0;top:150px;width:1080px'>{logo_svg(56)}</div>
  <div class='abs kick center' style='top:236px;font-size:15px'>Naira Petite &nbsp;·&nbsp; Nashik &nbsp;·&nbsp; October 2026</div>
  <div class='abs head center' id='hd' style='top:280px;font-size:176px'>THANK YOU</div>
  <div class='abs it center' style='top:462px;font-size:46px'>for visiting our Emerald Park pop-up.</div>
  {stamp(560, 668, 220, rot=-8, n=7)}
  <div class='glow' style='left:20px;top:760px;width:1040px;height:700px'></div>
  <img class='disp' src='display.png' style='left:{dl}px;top:{dt}px;width:{dw}px' alt=''>
  {glints}
  <div class='fade' style='top:1560px;height:360px'></div>
  <div class='abs it center' style='top:1700px;font-size:28px;color:#F2CFC4'>Missed it? The collection is always online.</div>
  <div class='abs foot center' style='top:1744px;font-size:17px'>NAIRAFLORE.COM &nbsp;·&nbsp; WHATSAPP +91 95615 57935</div>
  <div class='abs foot2 center' style='top:1776px;font-size:15px'>Demi-fine jewellery &nbsp;[ 18k gold coated · rhodium coated ]</div>
</div>"""


def page(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{fonts_css()}{CSS}</style></head><body>{body}</body></html>"


async def main():
    which = sys.argv[1:] or ["feed", "status"]
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for name, fn in (("feed", feed), ("status", story)):
            if name not in which: continue
            H, body = fn()
            (P / f"{name}.html").write_text(page(body))
            pg = await b.new_page(viewport={"width": 1080, "height": H}, device_scale_factor=2)
            await pg.goto((P / f"{name}.html").as_uri(), wait_until="networkidle")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
            info = await pg.evaluate("""() => { const r = document.getElementById('hd').getBoundingClientRect();
                 return {w: Math.round(r.width), top: Math.round(r.top), bottom: Math.round(r.bottom),
                         fonts: [...document.fonts].map(f => f.family + ':' + f.weight + ':' + f.status)} }""")
            print(name, info)
            await pg.screenshot(path=str(P / f"{name}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": H})
        await b.close()

asyncio.run(main())
