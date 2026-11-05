"""Ad 6 · Pick your shade — the Baguette Tennis Necklace as three paint chips dropped on the desk: a colour band, the
stone on the same model, and a label. Ruby, crystal, emerald; one price."""
from PIL import Image
from kit import *

IMG = T / 'img'
SHADES = [   # library id, shade, chip colour, chip ink, code, rotation, lift, crop centre y
    ('4577f059', 'RUBY', '#9B1B30', CREAM, '01', -3.2, 0, .36),
    ('1851cd8f', 'CRYSTAL', '#E3E9EE', INK, '02', 1.4, -22, .36),
    ('5f16bd83', 'EMERALD', '#0F6B3F', CREAM, '03', 3.0, 6, .34),
]


def chip_photo(i, w, h, cy):
    im = Image.open(IMG / 'lib' / f'{i}.png').convert('RGB'); W, H = im.size
    ch = H * 0.60; cw = ch * w / h
    x0, y0 = W * 0.5 - cw / 2, min(max(H * cy - ch / 2, 0), H - ch)
    out = IMG / f'a6_{i}_{w}x{h}.jpg'
    im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((w * 2, h * 2), Image.LANCZOS).save(out, quality=92)
    return out


NEEL = COLL['necklaces']['hex']
CSS = f"""
.card{{background:radial-gradient(110% 70% at 50% 60%, #2A4FA8 0%, {NEEL} 50%, #142A66 100%)}}
.title{{position:absolute;left:64px;right:64px;color:{CREAM}}}
.title .eb{{font-size:19px;opacity:.9}}
.title h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:84px;line-height:.98;margin-top:12px;letter-spacing:.01em}}
.title p{{font-size:40px;line-height:1.1;margin-top:10px}}
.chips{{position:absolute;left:46px;right:46px;display:flex;justify-content:space-between}}
.ch{{width:312px;background:#FBF8F2;border-radius:6px;overflow:hidden;box-shadow:0 26px 40px rgba(5,12,40,.42),0 3px 8px rgba(5,12,40,.3)}}
.ch .band{{height:96px;padding:14px 18px;display:flex;flex-direction:column;justify-content:space-between}}
.ch .band .code{{font-family:'Plex',monospace;font-size:15px;letter-spacing:.1em}}
.ch .band .sw{{font-family:'Plex',monospace;font-size:13px;letter-spacing:.08em;opacity:.8}}
.ch .ph{{background-size:cover;background-position:center}}
.ch .lab{{padding:16px 18px 18px;color:{INK}}}
.ch .lab .nm{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:31px;letter-spacing:.16em}}
.ch .lab .pr{{display:flex;justify-content:space-between;align-items:baseline;margin-top:6px;font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:21px;letter-spacing:.04em;color:#5A5148}}
.ch .lab .pr b{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:34px;color:{INK};letter-spacing:0}}
.foot2{{position:absolute;left:64px;right:64px;display:flex;justify-content:space-between;align-items:flex-end;color:{CREAM}}}
.foot2 .t{{font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:19px;letter-spacing:.16em;text-transform:uppercase;text-align:right;line-height:1.6}}
"""


def body(story):
    ph_h = 560 if story else 540
    chips = []
    for i, nm, col, ink, code, rot, lift, cy in SHADES:
        f = chip_photo(i, 312, ph_h, cy)
        chips.append(f"<div class='ch' style='transform:translateY({lift}px) rotate({rot}deg)'>"
                     f"<div class='band' style='background:{col};color:{ink}'><span class='code'>SHADE {code}</span><span class='sw'>BAGUETTE TENNIS NECKLACE</span></div>"
                     f"<div class='ph' style='height:{ph_h}px;background-image:url({uri(f)})'></div>"
                     f"<div class='lab'><div class='nm'>{nm}</div><div class='pr'><span>36cm · 6mm</span><b>₹2,099</b></div></div></div>")
    top = 300 if story else 0
    return ''.join([
        tab('necklaces', y=f'top:{top}px', radius='29px' if story else '0 0 14px 14px', invert=True),
        f"<div class='title safe' style='top:{top + (70 if story else 76)}px'><div class='eb eyebrow'>NECKLACES · THREE SHADES</div>"
        f"<h1>PICK YOUR SHADE.</h1><p class='serif-i'>Same necklace, same ₹2,099, three stones.</p></div>",
        f"<div class='chips' style='top:{top + 330 if story else 368}px'>{''.join(chips)}</div>",
        f"<div class='foot2 safe' style='{'top:1470px' if story else 'bottom:46px'}'>{logo(86, CREAM, '#FFBDA8')}"
        f"<span class='t'>Crosswise baguettes in gold claws · 18k gold PVD</span></div>",
    ])


render([('A06_pick-your-shade_feed', doc(*FEED, CSS, body(False)), FEED), ('A06_pick-your-shade_story', doc(*STORY, CSS, body(True)), STORY)])
