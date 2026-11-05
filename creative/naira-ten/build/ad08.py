"""Ad 8 · Hugs and kisses, on one wrist — the Kiss Knot Bangle on a chalk tic-tac-toe board: it is the O (the hug) and the
X (the kiss) at once, so the O's diagonal wins straight through it. Chalk annotations drawn over the library photograph."""
from kit import *

IMG = T / 'img'
SRC = IMG / 'lib' / 'a2592241.png'                  # 1536 x 2752
CHALK = '#FBFAF6'
FILTER = ("<filter id='chalk' x='-10%' y='-10%' width='120%' height='120%'>"
          "<feTurbulence type='fractalNoise' baseFrequency='1.3' numOctaves='2' seed='4' result='n'/>"
          "<feColorMatrix in='n' type='matrix' values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  3.8 0 0 0 -0.78' result='m'/>"
          "<feComposite in='SourceGraphic' in2='m' operator='in' result='s'/>"
          "<feTurbulence type='turbulence' baseFrequency='0.03' numOctaves='2' seed='9' result='w'/>"
          "<feDisplacementMap in='s' in2='w' scale='5' xChannelSelector='R' yChannelSelector='G'/></filter>"
          "<filter id='dust'><feGaussianBlur stdDeviation='7'/></filter>")


def strokes(w):
    line = f"<path d='M149,793 L566,1178 M976,1557 L1447,1992' fill='none' stroke='{CHALK}' stroke-width='{w + 6}' stroke-linecap='round'/>"
    kiss = (f"<text x='773' y='1915' text-anchor='middle' font-family='Kalam' font-weight='700' font-size='118' fill='{CHALK}'>kiss</text>"
            f"<path d='M773,1800 C 768,1730 778,1660 776,1600' fill='none' stroke='{CHALK}' stroke-width='{w}' stroke-linecap='round'/>"
            f"<path d='M742,1642 L776,1594 L808,1644' fill='none' stroke='{CHALK}' stroke-width='{w}' stroke-linecap='round' stroke-linejoin='round'/>")
    hug = (f"<text x='1262' y='940' text-anchor='middle' font-family='Kalam' font-weight='700' font-size='118' fill='{CHALK}'>hug</text>"
           f"<path d='M1200,996 C 1140,1080 1080,1150 1022,1222' fill='none' stroke='{CHALK}' stroke-width='{w}' stroke-linecap='round'/>"
           f"<path d='M1018,1166 L1016,1228 L1076,1214' fill='none' stroke='{CHALK}' stroke-width='{w}' stroke-linecap='round' stroke-linejoin='round'/>")
    return line + kiss + hug


def marks():
    return (f"<g filter='url(#dust)' opacity='.20'>{strokes(16)}</g>"
            f"<g filter='url(#chalk)'>{strokes(12)}</g>")


CSS = f"""
.card{{background:#1E1E1E}}
.fill{{position:absolute;inset:0;background-size:cover;background-position:center}}
.slate{{position:absolute;background-size:100% 100%}}
.slate.fade{{-webkit-mask-image:linear-gradient(90deg, transparent 0, #000 40px, #000 calc(100% - 40px), transparent 100%)}}
.hd{{position:absolute;left:64px;right:64px;color:{CREAM}}}
.hd .eb{{font-size:19px;opacity:.85}}
.hd h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:76px;line-height:.98;margin-top:12px;letter-spacing:.01em}}
.ft{{position:absolute;left:64px;color:{CREAM};width:560px}}
.ft .nm{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:25px;line-height:1.35}}
.ft .nm b{{font-weight:500}}
.ft .price{{font-family:'RupeeV','Velista',serif;font-size:62px;line-height:1;margin-top:10px}}
.ft .row{{display:flex;align-items:center;gap:26px;margin-top:16px}}
.ft .chip{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:15px;letter-spacing:.16em;text-transform:uppercase;border:1.5px solid rgba(251,245,234,.8);padding:10px 12px;white-space:nowrap}}
"""


def body(story):
    if story:
        sc = 0.62; ox = 64; oy = 540 - 755 * sc
        hd_top, ft_top = 318, 1360
        fill = f"<div class='fill' style='background-image:url({uri(IMG / 'a8_fill.jpg')})'></div>"
        fade = ' fade'
    else:
        sc = 1080 / 1536; ox = 0; oy = 255 - 755 * sc
        hd_top, ft_top = 66, 1184
        fill, fade = '', ''
    w, h = 1536 * sc, 2752 * sc
    svg = (f"<svg style='position:absolute;left:{ox:.1f}px;top:{oy:.1f}px' width='{w:.1f}' height='{h:.1f}' viewBox='0 0 1536 2752'>"
           f"<defs>{FILTER}</defs>{marks()}</svg>")
    return ''.join([
        fill,
        f"<div class='slate{fade}' style='left:{ox:.1f}px;top:{oy:.1f}px;width:{w:.1f}px;height:{h:.1f}px;background-image:url({uri(SRC)})'></div>",
        svg,
        tab('bracelets', y='top:300px' if story else 'top:0', radius='29px' if story else '0 0 14px 14px'),
        f"<div class='hd safe' style='top:{hd_top}px'><div class='eb eyebrow'>BRACELETS · KISS KNOT BANGLE</div>"
        f"<h1>HUGS AND KISSES,<br>ON ONE WRIST.</h1></div>",
        f"<div class='ft safe' style='top:{ft_top}px'>"
        f"<div class='row' style='margin-top:0'><span class='price' style='margin-top:0'>₹1,199</span><span class='nm'>Gold or silver · 18k PVD</span></div>"
        f"<div class='row' style='margin-top:16px'><span class='chip'>{OFFER}</span>{logo(86, CREAM, '#FFBDA8')}</div></div>",
    ])


render([('A08_hugs-and-kisses_feed', doc(*FEED, CSS, body(False)), FEED), ('A08_hugs-and-kisses_story', doc(*STORY, CSS, body(True)), STORY)])
