"""Ad 2 · Repeat the hoops. Not the outfit. — one portrait screenprinted in the colours of the wedding's functions (Warhol
repetition), the Woven Gold Hoops left as the only photograph in every panel."""
import pop
from kit import *

IMG = T / 'img'
FEED_ORDER = ['MEHENDI', 'HALDI', 'SANGEET', 'COCKTAIL', 'PHERAS', 'RECEPTION']
STORY_ORDER = ['ROKA', 'SAGAI', 'MEHENDI', 'HALDI', 'SANGEET', 'COCKTAIL', 'PHERAS', 'VIDAAI', 'RECEPTION']
for n in pop.PAL:
    pop.screenprint(n, (380, 330, 1430, 1642), (720, 900)).save(IMG / f'pop45_{n}.jpg', quality=93)
    pop.screenprint(n, (380, 300, 1430, 1700), (720, 960)).save(IMG / f'pop34_{n}.jpg', quality=93)

c = COLL['earrings']
CSS = f"""
.panel{{position:absolute;background-size:cover}}
.lbl{{position:absolute;left:14px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:14px;letter-spacing:.22em;background:{CREAM};color:{INK};padding:7px 10px 6px;border-radius:4px}}
.band{{position:absolute;left:0;right:0;background:{CREAM};color:{INK};padding:0 64px}}
.band .eb{{font-size:18px;color:{INK};opacity:.75}}
.band h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:76px;line-height:.98;letter-spacing:.01em;margin-top:14px}}
.band h1 span{{color:{COLL['rings']['hex']}}}
.band .sub{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:27px;line-height:1.35;margin-top:16px;max-width:900px}}
.band .row{{display:flex;align-items:center;gap:22px;margin-top:20px}}
.band .price{{font-family:'RupeeV','Velista',serif;font-size:54px;line-height:1}}
.band .chip{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px;letter-spacing:.16em;text-transform:uppercase;border:1.5px solid {INK};padding:11px 14px}}
"""


def panels(order, cols, cw, ch, rows_y, label_at):
    out = []
    for k, n in enumerate(order):
        r, cidx = divmod(k, cols)
        x, y = cidx * cw, rows_y[r]
        f = IMG / (f'pop45_{n}.jpg' if ch / cw == 1.25 else f'pop34_{n}.jpg')
        lab_y = f'top:{14}px' if label_at[r] == 'top' else f'bottom:{14}px'
        out.append(f"<div class='panel' style='left:{x}px;top:{y}px;width:{cw}px;height:{ch}px;background-image:url({uri(f)})'>"
                   f"<span class='lbl safe' style='{lab_y}'>{n}</span></div>")
    return ''.join(out)


def band(story):
    return (f"<div class='band' style='top:{960 if story else 450}px;height:{480 if story else 450}px;padding-top:{52 if story else 46}px'>"
            f"{tab('earrings', y='top:0')}"
            f"<div class='eb eyebrow safe'>{'NINE' if story else 'SIX'} FUNCTIONS · ONE PAIR OF HOOPS</div>"
            f"<h1 class='safe'>REPEAT THE HOOPS.<br><span>NOT THE OUTFIT.</span></h1>"
            f"<div class='sub safe'>Woven Gold Hoops: 25mm of braided gold, 18k PVD on surgical steel. Waterproof, so they last the whole week.</div>"
            f"<div class='row safe'><span class='price'>₹1,199</span><span class='chip'>{OFFER}</span></div></div>")


feed = (panels(FEED_ORDER, 3, 360, 450, [0, 900], ['top', 'bottom']) + band(False)
        + f"<div style='position:absolute;right:64px;top:{450 + 450 - 74}px'>{logo(86, INK, '#C86F58')}</div>")
story = (panels(STORY_ORDER, 3, 360, 480, [0, 480, 1440], ['bottom', 'bottom', 'top']) + band(True)
         + f"<div class='safe' style='position:absolute;right:64px;top:{960 + 480 - 70}px'>{logo(86, INK, '#C86F58')}</div>")
render([('A02_repeat-the-hoops_feed', doc(*FEED, CSS, feed), FEED), ('A02_repeat-the-hoops_story', doc(*STORY, CSS, story), STORY)])
