"""Ad 5 · The dance floor is 18cm long — a miniature sangeet (tabletop miniature photography, Tatsuya Tanaka lineage)
dancing on the Prism Rivière Bracelet. Generated from the product photo; the bracelet is the set."""
from PIL import Image
from kit import *

IMG = T / 'img'
src = Image.open(IMG / 'n04.png').convert('RGB')
src.resize((1080 * 2, 1350 * 2), Image.LANCZOS).save(IMG / 'a5_feed.jpg', quality=92)
CSS = f"""
.card{{background:linear-gradient(#962449 0%, #B12460 18%, #E0549A 82%, #EB54A0 100%)}}
.ph{{position:absolute;left:0;width:1080px;height:1350px;background-size:cover}}
.ph.ext{{-webkit-mask-image:linear-gradient(transparent 0, #000 70px, #000 1280px, transparent 1350px)}}
.floor{{position:absolute;left:0;right:0;bottom:0;mix-blend-mode:multiply;background:linear-gradient(to top, rgba(120,0,45,.62) 0%, rgba(120,0,45,.42) 38%, rgba(120,0,45,0) 72%)}}
.eb{{position:absolute;left:64px;font-size:19px;color:{CREAM}}}
.copy{{position:absolute;left:64px;right:64px;color:{CREAM}}}
.copy h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:86px;line-height:.98;letter-spacing:.01em}}
.copy .sub{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:28px;line-height:1.38;margin-top:20px;max-width:900px}}
.copy .row{{display:flex;align-items:center;gap:22px;margin-top:22px}}
.copy .price{{font-family:'RupeeV','Velista',serif;font-size:58px;line-height:1}}
.copy .chip{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px;letter-spacing:.16em;text-transform:uppercase;border:1.5px solid rgba(251,245,234,.85);padding:11px 14px}}
"""


def body(story):
    if story:
        ph = f"<div class='ph ext' style='top:150px;background-image:url({uri(IMG / 'a5_feed.jpg')})'></div><div class='floor' style='height:980px'></div>"
        copy_top, eb_top, tab_y, rad = 1112, 318, 'top:300px', '29px'
    else:
        ph = f"<div class='ph' style='top:0;background-image:url({uri(IMG / 'a5_feed.jpg')})'></div><div class='floor' style='height:620px'></div>"
        copy_top, eb_top, tab_y, rad = 900, 76, 'top:0', '0 0 14px 14px'
    return ''.join([
        ph, tab('bracelets', y=tab_y, radius=rad, invert=True),
        f"<div class='eb eyebrow safe' style='top:{eb_top}px'>THE SANGEET · BRACELETS</div>",
        f"<div class='copy safe' style='top:{copy_top}px'><h1>THE DANCE FLOOR<br>IS 18 CM LONG.</h1>"
        f"<div class='sub'>Prism Rivière Bracelet: 5mm cushion-cut stones in aqua, pink and yellow, each in its own pavé halo. Rhodium PVD.</div>"
        f"<div class='row'><span class='price'>₹2,399</span><span class='chip'>{OFFER}</span></div></div>",
        f"<div class='safe' style='position:absolute;right:64px;{'top:1478px' if story else 'bottom:48px'}'>{logo(86, CREAM, '#FFBDA8')}</div>",
    ])


render([('A05_dance-floor_feed', doc(*FEED, CSS, body(False)), FEED), ('A05_dance-floor_story', doc(*STORY, CSS, body(True)), STORY)])
