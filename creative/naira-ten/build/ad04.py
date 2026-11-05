"""Ad 4 · Anatomy of a compliment — the Verdant Circlet Stud as an engineering drawing on cyanotype blue: callouts from
the listing, a 16.8mm dimension line, construction lines, and a title block where the price sits like a part number."""
from kit import *

IMG = T / 'img'
SW, SH = 899, 1050                        # stud_tight.png
BLUE, LINE, PALE = '#173A7A', '#DCE8F7', 'rgba(220,232,247,.55)'
PARTS = [   # anchor in the cut-out (px), number, title, spec
    ((690, 140), '01', 'FINISH', '18k gold PVD'),
    ((470, 250), '02', 'STONE', 'Green CZ, cushion cut, 10mm'),
    ((770, 480), '03', 'CIRCLET', 'Open ring of clear CZ'),
    ((770, 740), '04', 'SHELL PEARL', 'White, 6mm'),
    ((330, 925), '05', 'STAR POINTS', 'Gold, set in the circlet'),
]

CSS = f"""
.card{{background:{BLUE}}}
.grid{{position:absolute;inset:0;background-image:linear-gradient({'rgba(220,232,247,.07)'} 1px, transparent 1px),linear-gradient(90deg, rgba(220,232,247,.07) 1px, transparent 1px),linear-gradient(rgba(220,232,247,.12) 1px, transparent 1px),linear-gradient(90deg, rgba(220,232,247,.12) 1px, transparent 1px);background-size:27px 27px,27px 27px,135px 135px,135px 135px}}
.frame{{position:absolute;inset:28px;border:1.5px solid {PALE}}}
.mono{{font-family:'Plex',ui-monospace,monospace;color:{LINE}}}
.top{{position:absolute;left:64px;right:64px;color:{LINE}}}
.top .m{{font-size:17px;letter-spacing:.08em;opacity:.85}}
.top h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:62px;line-height:1;margin-top:12px;color:#FFFFFF;letter-spacing:.01em}}
.stud{{position:absolute;filter:drop-shadow(0 14px 22px rgba(0,8,30,.45))}}
.lab{{position:absolute;width:252px;color:{LINE}}}
.lab .n{{font-family:'Plex',monospace;font-size:16px;letter-spacing:.06em;opacity:.8}}
.lab .t{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:23px;letter-spacing:.14em;color:#FFFFFF;margin-top:2px}}
.lab .s{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:22px;line-height:1.25;margin-top:4px}}
.tb{{position:absolute;left:64px;right:64px;display:grid;grid-template-columns:1.25fr 1fr .8fr;border:1.5px solid {LINE};color:{LINE}}}
.tb div{{border-right:1.5px solid {PALE};border-bottom:1.5px solid {PALE};padding:10px 14px 12px}}
.tb div:nth-child(3n){{border-right:0}}
.tb div:nth-last-child(-n+3){{border-bottom:0}}
.tb .k{{font-family:'Plex',monospace;font-size:13px;letter-spacing:.1em;opacity:.75;display:block}}
.tb .v{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:21px;letter-spacing:.06em;color:#FFFFFF;display:block;margin-top:4px}}
.tb .v.big{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:44px;letter-spacing:0;line-height:1}}
"""


def body(story):
    top = 300 if story else 0
    sh = 640 if story else 630                 # drawn height of the stud
    sc = sh / SH; sw = SW * sc
    sx, sy = (150, top + 262) if story else (150, 284)
    lab_x = 790
    labs, lines, pts = [], [], []
    n = len(PARTS)
    span_top, span_bot = sy + 20, sy + sh - 60
    for i, ((ax, ay), num, t, sp) in enumerate(PARTS):
        X, Y = sx + ax * sc, sy + ay * sc
        ly = span_top + i * (span_bot - span_top) / (n - 1)
        labs.append(f"<div class='lab safe' style='left:{lab_x}px;top:{ly - 18:.0f}px'><div class='n'>{num}</div><div class='t'>{t}</div><div class='s'>{sp}</div></div>")
        lines.append(f"<polyline points='{lab_x - 14},{ly + 4:.0f} {lab_x - 46},{ly + 4:.0f} {X:.0f},{Y:.0f}' fill='none' stroke='{LINE}' stroke-width='1.6'/>")
        pts.append(f"<circle cx='{X:.0f}' cy='{Y:.0f}' r='7' fill='none' stroke='#FFFFFF' stroke-width='2'/><circle cx='{X:.0f}' cy='{Y:.0f}' r='2.5' fill='#FFFFFF'/>")
    # construction lines through the stone centre and a dashed circle round the circlet
    cx, cy = sx + 470 * sc, sy + 290 * sc
    ccx, ccy, cr = sx + 450 * sc, sy + 700 * sc, 360 * sc
    dimx = sx - 54
    cons = (f"<line x1='{sx - 20}' y1='{cy:.0f}' x2='{sx + sw + 20:.0f}' y2='{cy:.0f}' stroke='{PALE}' stroke-width='1.2' stroke-dasharray='22 6 3 6'/>"
            f"<line x1='{cx:.0f}' y1='{sy - 30}' x2='{cx:.0f}' y2='{sy + sh + 30}' stroke='{PALE}' stroke-width='1.2' stroke-dasharray='22 6 3 6'/>"
            f"<circle cx='{ccx:.0f}' cy='{ccy:.0f}' r='{cr:.0f}' fill='none' stroke='{PALE}' stroke-width='1.2' stroke-dasharray='8 8'/>"
            # dimension line: 16.8mm overall height
            f"<line x1='{dimx - 16}' y1='{sy}' x2='{sx - 12}' y2='{sy}' stroke='{LINE}' stroke-width='1.2'/>"
            f"<line x1='{dimx - 16}' y1='{sy + sh}' x2='{sx - 12}' y2='{sy + sh}' stroke='{LINE}' stroke-width='1.2'/>"
            f"<line x1='{dimx}' y1='{sy + 14}' x2='{dimx}' y2='{sy + sh - 14}' stroke='{LINE}' stroke-width='1.6'/>"
            f"<path d='M{dimx},{sy} l-7,18 l14,0 z M{dimx},{sy + sh} l-7,-18 l14,0 z' fill='{LINE}'/>")
    dimlabel = (f"<div class='mono safe' style='position:absolute;left:{dimx - 52}px;top:{sy + sh / 2 - 14:.0f}px;transform:rotate(-90deg);"
                f"transform-origin:center;font-size:20px;letter-spacing:.12em;background:{BLUE};padding:0 8px;color:#FFFFFF'>16.8 MM</div>")
    svg = f"<svg style='position:absolute;inset:0' width='1080' height='{1920 if story else 1350}'>{cons}{''.join(lines)}{''.join(pts)}</svg>"
    tb_top = (sy + sh + 52) if story else 1052
    tb = (f"<div class='tb safe' style='top:{tb_top}px'>"
          f"<div><span class='k'>PART</span><span class='v'>VERDANT CIRCLET STUDS</span></div>"
          f"<div><span class='k'>MATERIAL</span><span class='v'>316L SURGICAL STEEL</span></div>"
          f"<div><span class='k'>PRICE</span><span class='v big'>₹1,099</span></div>"
          f"<div><span class='k'>FINISH</span><span class='v'>18K GOLD PVD · WATERPROOF</span></div>"
          f"<div><span class='k'>SCALE</span><span class='v'>ENLARGED · 16.8MM</span></div>"
          f"<div><span class='k'>DRAWN BY</span><span class='v' style='margin-top:8px'>{logo(92, '#FFFFFF', '#FFBDA8')}</span></div></div>")
    return ''.join([
        "<div class='grid'></div><div class='frame'></div>",
        tab('earrings', y=f'top:{top}px' if story else 'top:0', radius='29px' if story else '0 0 14px 14px'),
        f"<div class='top safe' style='top:{top + (70 if story else 76)}px'><div class='m mono'>DRG NO. VC-01 · EARRINGS · SHEET 1 OF 1</div>"
        f"<h1>ANATOMY OF A COMPLIMENT.</h1></div>",
        f"<img class='stud' src='{uri(IMG / 'stud_tight.png')}' style='left:{sx}px;top:{sy}px;width:{sw:.0f}px;height:{sh}px'>", svg,
        dimlabel, ''.join(labs), tb,
    ])


render([('A04_anatomy_feed', doc(*FEED, CSS, body(False)), FEED), ('A04_anatomy_story', doc(*STORY, CSS, body(True)), STORY)])
