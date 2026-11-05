"""Ad 7 · This is 50cm — a seamless three-card carousel: one photograph of the Toggle Link Chain laid straight across all
three cards, with a tailor's tape drawn beneath it from 0 at the T-bar to 50 at the ring. Swipe to measure it.
The story runs the same idea vertically."""
from PIL import Image
from kit import *

IMG = T / 'img'
PW, PH = 3240, 1350
# panorama: n07 scaled 1.10, cropped so the chain sits at y≈618
SC, OX, OY = 1.10, 142, 40
src = Image.open(IMG / 'n07.png').convert('RGB')
big = src.resize((round(3168 * SC), round(1344 * SC)), Image.LANCZOS).crop((OX, OY, OX + PW, OY + PH))
big.save(IMG / 'a7_pano.jpg', quality=92)
X0, X1 = 183 * SC - OX, 3018 * SC - OX          # 0 cm at the T-bar, 50 cm at the ring
CY = 678 * SC - OY
PXCM = (X1 - X0) / 50
# story: n09 scaled to cover 1080x1920
SS = 1080 / 1536
st = Image.open(IMG / 'n09.png').convert('RGB')
stb = st.resize((1080, round(2752 * SS)), Image.LANCZOS)
SOY = (stb.size[1] - 1920) // 2
stb.crop((0, SOY, 1080, SOY + 1920)).save(IMG / 'a7_story.jpg', quality=92)
Y0, Y1 = 220 * SS - SOY, 2565 * SS - SOY
SX = 775 * SS
NEEL = COLL['necklaces']['hex']


def tape_h(x0, x1, y, h=64, start=-1, end=52):
    """A cream tailor's tape lying horizontally, 0 at x0, 50 at x1."""
    pxcm = (x1 - x0) / 50
    left, right = x0 + start * pxcm, x0 + end * pxcm
    p = [f"<rect x='{left:.1f}' y='{y}' width='{right - left:.1f}' height='{h}' rx='3' fill='#FBF7EE'/>",
         f"<rect x='{left:.1f}' y='{y}' width='{right - left:.1f}' height='{h}' rx='3' fill='none' stroke='rgba(31,26,20,.18)'/>"]
    for mm in range(start * 10, end * 10 + 1):
        x = x0 + mm * pxcm / 10
        if mm % 10 == 0:
            p.append(f"<line x1='{x:.1f}' y1='{y}' x2='{x:.1f}' y2='{y + 24}' stroke='#1F1A14' stroke-width='1.6'/>")
            cm = mm // 10
            if 0 <= cm <= 50:
                red = cm % 10 == 0
                p.append(f"<text x='{x:.1f}' y='{y + 50}' text-anchor='middle' font-family='JostF' font-weight='500' font-size='{22 if red else 16}' fill='{'#C1272D' if red else '#1F1A14'}'>{cm}</text>")
        elif mm % 5 == 0:
            p.append(f"<line x1='{x:.1f}' y1='{y}' x2='{x:.1f}' y2='{y + 15}' stroke='#1F1A14' stroke-width='1.1'/>")
        else:
            p.append(f"<line x1='{x:.1f}' y1='{y}' x2='{x:.1f}' y2='{y + 8}' stroke='#1F1A14' stroke-width='.7'/>")
    # brass end cap at the left
    p.append(f"<rect x='{left - 18:.1f}' y='{y - 3}' width='22' height='{h + 6}' rx='3' fill='url(#brass)'/>")
    return ''.join(p)


def tape_v(y0, y1, x, w=58, start=-1, end=51):
    pxcm = (y1 - y0) / 50
    top, bot = y0 + start * pxcm, y0 + end * pxcm
    p = [f"<rect x='{x}' y='{top:.1f}' width='{w}' height='{bot - top:.1f}' rx='3' fill='#FBF7EE'/>"]
    for mm in range(start * 10, end * 10 + 1):
        y = y0 + mm * pxcm / 10
        if mm % 10 == 0:
            cm = mm // 10
            p.append(f"<line x1='{x + w}' y1='{y:.1f}' x2='{x + w - 22}' y2='{y:.1f}' stroke='#1F1A14' stroke-width='1.5'/>")
            if 0 <= cm <= 50 and cm % 5 == 0:
                red = cm % 10 == 0
                p.append(f"<text x='{x + 6}' y='{y + 6:.1f}' font-family='JostF' font-weight='500' font-size='{19 if red else 15}' fill='{'#C1272D' if red else '#1F1A14'}'>{cm}</text>")
        elif mm % 5 == 0:
            p.append(f"<line x1='{x + w}' y1='{y:.1f}' x2='{x + w - 13}' y2='{y:.1f}' stroke='#1F1A14' stroke-width='1'/>")
    p.append(f"<rect x='{x - 3}' y='{top - 18:.1f}' width='{w + 6}' height='22' rx='3' fill='url(#brass)'/>")
    return ''.join(p)


DEFS = ("<defs><linearGradient id='brass' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#FFF0B8'/>"
        "<stop offset='.45' stop-color='#D9A93E'/><stop offset='1' stop-color='#8C6420'/></linearGradient>"
        "<filter id='sh' x='-5%' y='-50%' width='110%' height='200%'><feDropShadow dx='0' dy='6' stdDeviation='6' flood-color='#5A4632' flood-opacity='.28'/></filter></defs>")

CSS = f"""
.card{{background:#EFE3D6}}
.ph{{position:absolute;inset:0;background-size:cover}}
.eb{{position:absolute;font-size:19px;color:{INK};opacity:.8}}
.h{{position:absolute;color:{INK};font-family:'RupeeV','Velista',serif;font-weight:400;line-height:.96;letter-spacing:.01em}}
.p{{position:absolute;color:{INK};font-family:'Rupee','JostF',sans-serif;font-weight:300;font-size:30px;line-height:1.38}}
.p b{{font-weight:500}}
.price{{font-family:'RupeeV','Velista',serif;font-size:62px;line-height:1}}
.chip{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:17px;letter-spacing:.16em;text-transform:uppercase;border:1.5px solid {INK};padding:11px 14px;color:{INK}}}
.swipe{{position:absolute;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:19px;letter-spacing:.2em;color:{INK}}}
"""

pano = ''.join([
    f"<div class='ph' style='background-image:url({uri(IMG / 'a7_pano.jpg')})'></div>",
    f"<svg style='position:absolute;inset:0' width='{PW}' height='{PH}'>{DEFS}<g filter='url(#sh)'>{tape_h(X0, X1, round(CY + 130))}</g></svg>",
    tab('necklaces', x=f'left:{1080 - 56 - 236}px', y='top:0'),
    # card 1
    "<div class='eb eyebrow' style='left:64px;top:76px'>NECKLACES · ACTUAL LENGTH</div>",
    "<div class='h fit' style='left:64px;top:122px;width:960px;font-size:124px'>THIS IS<br>50 CM.</div>",
    f"<div class='p' style='left:64px;top:{round(CY + 250)}px;width:800px'>Laid flat next to a tailor's tape, T-bar to ring.</div>",
    f"<div class='swipe' style='left:{1080 - 64 - 330}px;bottom:58px;display:flex;align-items:center;gap:14px'>SWIPE ALONG IT"
    f"<svg width='46' height='16' viewBox='0 0 46 16'><path d='M0 8 H42 M34 1 L43 8 L34 15' fill='none' stroke='{INK}' stroke-width='2'/></svg></div>",
    f"<div style='position:absolute;left:54px;bottom:50px'>{logo(86, INK, '#C86F58')}</div>",
    # card 2
    "<div class='h fit' style='left:1144px;top:122px;width:960px;font-size:96px'>OF PAPERCLIP<br>CHAIN,</div>",
    f"<div class='p' style='left:1144px;top:{round(CY + 250)}px;width:900px'><b>Long flat links, 4mm wide.</b> 18k gold PVD on surgical steel, so it holds its colour through sweat, water and a five-day wedding.</div>",
    # card 3
    "<div class='h fit' style='left:2224px;top:122px;width:960px;font-size:96px'>AND ONE<br>TOGGLE.</div>",
    f"<div class='p' style='left:2224px;top:{round(CY + 250)}px;width:900px'>A 15mm bar and ring you wear at the front, or turned to the side. <b>Toggle Link Chain.</b></div>",
    f"<div style='position:absolute;left:2224px;bottom:58px;display:flex;align-items:center;gap:22px'><span class='price'>₹1,199</span><span class='chip'>{OFFER}</span></div>",
])

story = ''.join([
    f"<div class='ph' style='background-image:url({uri(IMG / 'a7_story.jpg')})'></div>",
    f"<svg style='position:absolute;inset:0' width='1080' height='1920'>{DEFS}<g filter='url(#sh)'>{tape_v(Y0, Y1, round(SX - 150))}</g></svg>",
    tab('necklaces', y='top:300px', radius='29px'),
    f"<div class='eb eyebrow safe' style='left:{round(SX + 70)}px;top:372px'>ACTUAL LENGTH</div>",
    f"<div class='h safe' style='left:{round(SX + 70)}px;top:410px;font-size:100px'>THIS<br>IS<br>50 CM.</div>",
    f"<div class='p safe' style='left:{round(SX + 70)}px;top:760px;width:{1080 - round(SX + 70) - 56}px;font-size:28px'><b>Toggle Link Chain.</b> Paperclip links 4mm wide, a 15mm toggle at the front. 18k gold PVD on surgical steel.</div>",
    f"<div class='safe' style='position:absolute;left:{round(SX + 70)}px;top:1130px'><div class='price'>₹1,199</div></div>",
    f"<div class='chip safe' style='position:absolute;left:{round(SX + 70)}px;top:1222px;font-size:15px;line-height:1.7;width:{1080 - round(SX + 70) - 56}px'>Buy 2, 10% off<br>Buy 3, 20% off</div>",
    f"<div class='safe' style='position:absolute;left:64px;top:1470px'>{logo(86, INK, '#C86F58')}</div>",
])

res = render([('A07_pano', doc(PW, PH, CSS, pano), (PW, PH)), ('A07_fifty-cm_story', doc(*STORY, CSS, story), STORY)])
full = Image.open(OUT / 'A07_pano.jpg')
for k in range(3):
    full.crop((k * 1080, 0, (k + 1) * 1080, PH)).save(OUT / f'A07_fifty-cm_card{k + 1}_feed.jpg', 'JPEG', quality=92, subsampling=0, optimize=True)
print('pxcm', round(PXCM, 1), 'chain y', round(CY), 'story chain', round(Y0), round(Y1), 'x', round(SX))
