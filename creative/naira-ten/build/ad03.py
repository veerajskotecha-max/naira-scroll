"""Ad 3 · The Periodic Table of Naira — a catalogue grid (the account's best format) set as the periodic table: each
column a collection in its colour, like the table's groups, and the two real elements every piece is coated in."""
from PIL import Image
from kit import *

IMG = T / 'img'
SHOP = S / 'camp' / 'img' / 'shop'
GROUPS = [   # (collection, [(handle, symbol, focus x, focus y, zoom)])
    ('earrings', [('verdant-circlet-studs', 'Vc', .50, .42, 1.5), ('woven-gold-hoops', 'Wg', .52, .45, 1.45), ('brushed-gold-huggies', 'Bh', .55, .42, 1.8)]),
    ('rings', [('cushion-halo-ring', 'Ch', .50, .33, 1.9), ('verdant-eternity-band', 'Ve', .44, .36, 1.35)]),
    ('necklaces', [('toggle-link-chain', 'Tl', .42, .45, 1.5), ('baguette-tennis-necklace', 'Bt', .45, .40, 1.4)]),
    ('bracelets', [('prism-riviere-bracelet', 'Pr', .55, .32, 1.35), ('kiss-knot-bangle', 'Kk', .50, .44, 1.3), ('baguette-tennis-bracelet', 'Tb', .56, .66, 2.4)]),
]
ELEMENTS = {'rings': ('79', 'Au', 'Gold', '196.97', 'gold'), 'necklaces': ('45', 'Rh', 'Rhodium', '102.91', 'rh')}


def crop(handle, fx, fy, zoom, w, h):
    im = Image.open(SHOP / f'{handle}.jpg').convert('RGB'); W, H = im.size
    cw = W / zoom; ch = cw * h / w
    if ch > H: ch = H; cw = ch * w / h
    x = min(max(fx * W - cw / 2, 0), W - cw); y = min(max(fy * H - ch / 2, 0), H - ch)
    out = IMG / f'pt_{handle}.jpg'
    im.crop((round(x), round(y), round(x + cw), round(y + ch))).resize((w * 2, h * 2), Image.LANCZOS).save(out, quality=92)
    return out


CSS = f"""
.card{{background:#F8F2E7}}
.paper{{position:absolute;inset:0;opacity:.5;background-image:linear-gradient(rgba(31,26,20,.045) 1px, transparent 1px),linear-gradient(90deg, rgba(31,26,20,.045) 1px, transparent 1px);background-size:27px 27px}}
.head{{position:absolute;left:56px;right:56px;color:{INK}}}
.head .eb{{font-size:18px;opacity:.75}}
.head h1{{font-family:'RupeeV','Velista',serif;font-weight:400;font-size:62px;line-height:1;margin-top:12px;letter-spacing:.01em}}
.head p{{font-size:40px;line-height:1.12;margin-top:10px}}
.grid{{position:absolute;left:56px;right:56px;display:grid;grid-template-columns:repeat(4,1fr);column-gap:14px}}
.col{{display:flex;flex-direction:column;gap:12px}}
.gh{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:15px;letter-spacing:.2em;padding-bottom:8px;border-bottom:5px solid;color:{INK}}}
.el{{position:relative;display:flex;flex-direction:column;overflow:hidden;border-radius:3px}}
.el .ph{{background-size:cover;background-position:center}}
.el .bd{{flex:1;position:relative;padding:8px 12px 10px}}
.el .num{{position:absolute;left:12px;top:8px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px}}
.el .pr{{position:absolute;right:12px;top:8px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:19px}}
.el .sym{{position:absolute;left:12px;bottom:4px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:62px;line-height:1;letter-spacing:-.01em}}
.el.real{{justify-content:space-between;padding:12px 14px}}
.el.real .num{{position:static;font-size:22px}}
.el.real .sym{{position:static;font-size:96px;line-height:.9}}
.el.real .nm{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:21px;letter-spacing:.04em}}
.el.real .wt{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:18px}}
.el.gold{{background:linear-gradient(135deg,#8C6420 0%,#E9C46A 28%,#FFF0B8 46%,#D9A93E 62%,#9A6F22 100%);color:#2A1C05}}
.el.rh{{background:linear-gradient(135deg,#7E848C 0%,#D9DEE4 30%,#FFFFFF 47%,#BFC5CC 64%,#80868E 100%);color:#1E2328}}
.el.real::after{{content:'';position:absolute;inset:0;mix-blend-mode:overlay;opacity:.35;background-image:repeating-linear-gradient(115deg, rgba(255,255,255,.18) 0 2px, rgba(0,0,0,.06) 2px 5px)}}
.legend{{position:absolute;left:56px;right:56px;display:flex;align-items:flex-end;justify-content:space-between;color:{INK}}}
.legend .t{{font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:22px;line-height:1.4;text-align:right}}
.legend .t b{{font-weight:500}}
"""


def body(story):
    tile_w = 231
    ph_h, bd_h = (160, 96) if story else (190, 100)
    real_h = ph_h + bd_h
    n = 0; cols = []
    for coll, items in GROUPS:
        c = COLL[coll]; tiles = []
        for handle, sym, fx, fy, z in items:
            n += 1
            f = crop(handle, fx, fy, z, tile_w, ph_h)
            tiles.append(f"<div class='el' style='height:{real_h}px'><div class='ph' style='height:{ph_h}px;background-image:url({uri(f)})'></div>"
                         f"<div class='bd' style='background:{c['hex']};color:{c['ink']}'><span class='num'>{n}</span>"
                         f"<span class='pr'>{inr(LIVE[handle]['price'])}</span><span class='sym'>{sym}</span></div></div>")
        if coll in ELEMENTS:
            num, sym, nm, wt, cls = ELEMENTS[coll]
            tiles.append(f"<div class='el real {cls}' style='height:{real_h}px'><span class='num'>{num}</span><span class='sym'>{sym}</span>"
                         f"<span><div class='nm'>{nm}</div><div class='wt'>{wt}</div></span></div>")
        cols.append(f"<div class='col'><div class='gh' style='border-color:{c['hex']}'>{c['label']}</div>{''.join(tiles)}</div>")
    top = 300 if story else 0
    grid_top = 580 if story else 262
    return ''.join([
        "<div class='paper'></div>",
        tab('all', y=f'top:{top}px', radius='0 0 14px 14px' if not story else '29px'),
        f"<div class='head safe' style='top:{372 if story else 74}px'><div class='eb eyebrow'>121 PIECES IN STOCK · FROM ₹599</div>"
        f"<h1>THE PERIODIC TABLE OF NAIRA</h1><p class='serif-i'>Every piece is made of Au or Rh.</p></div>",
        f"<div class='grid safe' style='top:{grid_top}px'>{''.join(cols)}</div>",
        f"<div class='legend safe' style='{'top:1450px' if story else 'bottom:44px'}'>{logo(86, INK, '#C86F58')}"
        f"<div class='t'><b>Au</b> 18k gold or <b>Rh</b> rhodium, PVD-bonded to surgical steel.<br>{OFFER}</div></div>",
    ])


render([('A03_periodic-table_feed', doc(*FEED, CSS, body(False)), FEED), ('A03_periodic-table_story', doc(*STORY, CSS, body(True)), STORY)])
