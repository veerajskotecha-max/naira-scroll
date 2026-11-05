"""Ad 10 · ₹799, the pair — knockout numerals: the price is cut out of the Brushed Gold Huggies' own satin-brushed surface
(a macro of the real piece), with the pair below it. The judge's best entry-price hook, set as material."""
from kit import *

IMG = T / 'img'
CSS = f"""
.card{{background:radial-gradient(90% 60% at 50% 34%, #3A2A1C 0%, #1D1610 55%, #120D09 100%)}}
.eb{{position:absolute;left:64px;font-size:19px;color:{CREAM};opacity:.88}}
.num{{position:absolute;left:0;right:0;display:flex;justify-content:center;white-space:nowrap}}
.num span{{font-family:'RozhaR','Rozha',serif;line-height:1;letter-spacing:-.01em;color:transparent;-webkit-background-clip:text;background-clip:text}}
.num .tex{{background-image:url({uri(IMG / 'a10_brushed.jpg')});background-size:cover;background-position:30% 45%;filter:drop-shadow(0 22px 26px rgba(0,0,0,.55)) drop-shadow(0 2px 2px rgba(0,0,0,.6))}}
.num .gloss{{position:absolute;background-image:linear-gradient(112deg, rgba(255,255,255,0) 30%, rgba(255,248,225,.55) 47%, rgba(255,255,255,0) 60%);mix-blend-mode:soft-light}}
.num .edge{{position:absolute;-webkit-text-stroke:1.4px rgba(255,236,190,.42);color:transparent}}
.pair{{position:absolute;color:{CREAM};font-family:'RupeeV','Velista',serif;font-weight:400;letter-spacing:.01em;line-height:1}}
.hug{{position:absolute;filter:drop-shadow(0 28px 26px rgba(0,0,0,.6)) drop-shadow(0 4px 4px rgba(0,0,0,.5))}}
.spec{{position:absolute;left:64px;color:{CREAM};font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:26px;line-height:1.5}}
.spec b{{font-weight:500;letter-spacing:.02em}}
.foot{{position:absolute;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center}}
.chip{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px;letter-spacing:.16em;text-transform:uppercase;color:{CREAM};border:1.5px solid rgba(251,245,234,.75);padding:12px 14px}}
"""


def numerals(top, size):
    t = '₹799'
    return (f"<div class='num' style='top:{top}px'>"
            f"<span class='tex' style='font-size:{size}px'>{t}</span>"
            f"<span class='gloss' style='font-size:{size}px'>{t}</span>"
            f"<span class='edge' style='font-size:{size}px'>{t}</span></div>")


def body(story):
    if story:
        return ''.join([
            tab('earrings', y='top:300px', radius='29px'),
            f"<div class='eb eyebrow safe' style='top:318px'>EARRINGS · BRUSHED GOLD HUGGIES</div>",
            numerals(352, 470),
            f"<div class='pair safe' style='left:64px;top:872px;font-size:100px'>THE PAIR.</div>",
            f"<img class='hug' src='{uri(IMG / 'a10_pair.png')}' style='left:392px;top:960px;width:640px'>",
            f"<div class='spec safe' style='top:1030px;width:340px'><b>14 × 9.8mm</b> huggies<br>with a <b>6mm</b> band,<br>satin-brushed.<br><br>18k gold PVD on<br>surgical steel.<br>Waterproof.</div>",
            f"<div class='foot safe' style='top:1460px'><span class='chip'>{OFFER}</span>{logo(86, CREAM, '#FFBDA8')}</div>",
        ])
    return ''.join([
        tab('earrings'),
        f"<div class='eb eyebrow' style='top:76px'>EARRINGS · BRUSHED GOLD HUGGIES</div>",
        numerals(104, 470),
        f"<div class='pair' style='left:64px;top:622px;font-size:100px'>THE PAIR.</div>",
        f"<img class='hug' src='{uri(IMG / 'a10_pair.png')}' style='left:392px;top:690px;width:640px'>",
        f"<div class='spec' style='top:770px;width:340px'><b>14 × 9.8mm</b> huggies<br>with a <b>6mm</b> band,<br>satin-brushed.<br><br>18k gold PVD on<br>surgical steel.<br>Waterproof.</div>",
        f"<div class='foot' style='bottom:52px'><span class='chip'>{OFFER}</span>{logo(86, CREAM, '#FFBDA8')}</div>",
    ])


render([('A10_the-799-pair_feed', doc(*FEED, CSS, body(False)), FEED), ('A10_the-799-pair_story', doc(*STORY, CSS, body(True)), STORY)])
