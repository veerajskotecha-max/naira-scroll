"""Ad 1 · I D◯ — the Cushion Halo Ring stands in for the O. Typographic swap (KFC 'FCK' lineage: the product rewrites the word)."""
import numpy as np
from PIL import Image
from kit import *

IMG = T / 'img'
ring = Image.open(IMG / 'ring_cut_tight.png').convert('RGBA')
a = np.array(ring)
a[:90, 600:, 3] = 0                                   # drop the lens-flare star above the stone
ys, xs = np.where(a[:, :, 3] > 40); ring = Image.fromarray(a).crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
ring.save(IMG / 'a1_ring.png'); RW, RH = ring.size
BAND = 1011                                            # outer diameter of the band in the cut-out, px
F = 470                                                # Velista size: cap height .698em, O height .718em
O_H = 0.718 * F                                        # the ring's band matches the height of a Velista O
ring_h = O_H * RH / BAND; ring_w = O_H * RW / BAND
c = COLL['rings']
RED, DEEP = c['hex'], '#8E1219'

CSS = f"""
.card{{background:{RED}}}
.grain{{position:absolute;inset:0;opacity:.20;mix-blend-mode:multiply;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .35  0 0 0 0 .02  0 0 0 0 .04  0 0 0 .9 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}}
.vig{{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 38%, rgba(0,0,0,0) 55%, rgba(60,0,6,.38) 100%)}}
.eyebrow{{position:absolute;left:64px;font-size:20px;color:{CREAM};opacity:.92}}
.word{{position:absolute;left:0;right:0;display:flex;justify-content:center;align-items:flex-end;color:{CREAM};font-size:{F}px;line-height:1}}
.word .lt{{position:relative;display:block;height:{F * .75:.0f}px;line-height:{F * .98:.0f}px;margin-bottom:-{F * .02:.0f}px;filter:drop-shadow(0 18px 16px rgba(70,0,8,.30)) drop-shadow(0 2px 2px rgba(40,0,4,.35))}}
.word .lt::after{{content:'';position:absolute;left:6%;right:6%;bottom:{F * .005:.0f}px;height:22px;border-radius:50%;background:radial-gradient(closest-side, rgba(55,0,6,.50), rgba(55,0,6,0));filter:blur(4px);z-index:-1}}
.word .gap{{width:{F * .26:.0f}px}}
.word .o{{position:relative;width:{ring_w:.0f}px;height:{ring_h:.0f}px;margin-left:{F * .03:.0f}px;margin-bottom:-{F * .012:.0f}px}}
.word .o img{{position:absolute;inset:0;width:100%;height:100%;filter:drop-shadow(0 18px 18px rgba(70,0,8,.35)) drop-shadow(0 3px 3px rgba(40,0,4,.45))}}
.word .o .shadow{{position:absolute;left:12%;right:12%;bottom:-14px;height:28px;border-radius:50%;background:radial-gradient(closest-side, rgba(55,0,6,.55), rgba(55,0,6,0));filter:blur(4px)}}
.say{{position:absolute;left:64px;right:64px;color:{CREAM};font-size:66px;line-height:1.05}}
.facts{{position:absolute;left:64px;right:64px;color:{CREAM};font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:29px;line-height:1.45;letter-spacing:.01em;opacity:.95}}
.facts b{{font-weight:500}}
.price{{position:absolute;left:64px;color:{CREAM};font-size:76px;line-height:1}}
.foot{{position:absolute;left:54px;right:56px;display:flex;justify-content:space-between;align-items:flex-end;color:{CREAM}}}
.foot .t{{font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:19px;letter-spacing:.16em;text-transform:uppercase;opacity:.9}}
"""


def body(story):
    top = 300 if story else 0
    base = 905 if story else 700                       # baseline of the giant word
    word_top = base - ring_h - F * .012
    return ''.join([
        "<div class='grain'></div><div class='vig'></div>",
        tab('rings', y=f'top:{top}px', radius='0 0 14px 14px' if not story else '29px', invert=True),
        f"<div class='eyebrow safe' style='top:{top + (76 if not story else 18)}px'>ENGAGEMENT SEASON · NOV 2026</div>",
        f"<div class='word display safe' style='top:{word_top:.0f}px;height:{ring_h:.0f}px'>"
        f"<span class='lt'>I</span><span class='gap'></span><span class='lt'>D</span>"
        f"<span class='o'><span class='shadow'></span><img src='{uri(IMG / 'a1_ring.png')}'></span></div>",
        f"<div class='say serif-i safe' style='top:{base + 60}px'>Say it with a ring that adjusts.</div>",
        f"<div class='facts safe' style='top:{base + 160}px'><b>Cushion Halo Ring.</b> An 8mm stone in four claws, a 12mm pavé halo, "
        f"rhodium PVD on surgical steel. Open at the back, so it fits US 5 to 9.</div>",
        f"<div class='price display safe' style='top:{base + (330 if story else 318)}px'>₹1,099</div>",
        f"<div class='foot safe' style='bottom:{(1920 - 1500) if story else 50}px'>{logo(86, CREAM, '#FFBDA8')}<span class='t'>{TRUST}</span></div>",
    ])


render([('A01_i-do_feed', doc(*FEED, CSS, body(False)), FEED), ('A01_i-do_story', doc(*STORY, CSS, body(True)), STORY)])
