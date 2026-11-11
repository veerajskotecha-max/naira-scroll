"""Naira A/B angle tests on the two original winning photos.

  P · Prism Rivière Bracelet  · the Sweet On You photo (2ebe51f1, sugared jelly sweets)  · Feed 4:5, where it ran
  W · Woven Gold Hoops        · the red Woven photo (141d0fbd, oxblood dome)              · Story 9:16, where it ran

The photo is held constant inside each set; every ad changes the angle: hook, edit and CTA button together."""
import math, random, urllib.parse
from kit import *

IMG = T / 'img'
U = {k: uri(IMG / f) for k, f in [('p_base', 'p_base.jpg'), ('p_win', 'p_win.jpg'), ('p_tex', 'p_tex.jpg'), ('w_full', 'w_full.jpg'),
                                   ('w_push', 'w_push.jpg'), ('w_hoops', 'w_push_hoops.png'), ('w_lens', 'w_lens.jpg')]}

# ------------------------------------------------------------------ tokens
P_INK, RANI, RANI_D, P_CREAM, BLUSH = '#2A1F22', '#C2185B', '#B0164F', '#FBF5EA', '#F6D8DF'
OX, W_CR, GOLD, HALDI = '#2C0305', '#F7EBDD', '#E7C27C', '#F2B705'
ARROW = "<svg width='34' height='16' viewBox='0 0 34 16'><path d='M1 8 H31 M24 1.5 L31.5 8 L24 14.5' stroke='currentColor' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"
CHEV = "<svg width='36' height='20' viewBox='0 0 36 20'><path d='M3 3 L18 17 L33 3' stroke='currentColor' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"
TICK = "<svg width='18' height='14' viewBox='0 0 18 14'><path d='M2 7.5 L7 12 L16 2' stroke='#2C0305' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>"


# ------------------------------------------------------------------ hand-drawn marks
def rough_ellipse(cx, cy, rx, ry, rot=0.0, turns=1.1, seed=3, wob=0.03, steps=160):
    rnd = random.Random(seed); ph = [rnd.uniform(0, 6.28) for _ in range(3)]; a0 = rnd.uniform(0, 6.28); t0 = math.radians(rot)
    pts = []
    for i in range(steps + 1):
        t = i / steps; a = a0 + 2 * math.pi * turns * t
        k = 1 + wob * (math.sin(2 * a + ph[0]) + .6 * math.sin(3 * a + ph[1]) + .4 * math.sin(5 * a + ph[2])) / 2 + .04 * t
        x, y = rx * k * math.cos(a), ry * k * math.sin(a)
        pts.append((cx + x * math.cos(t0) - y * math.sin(t0), cy + x * math.sin(t0) + y * math.cos(t0)))
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)


def arrow(x1, y1, x2, y2, bend=.22, head=22):
    mx, my, dx, dy = (x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1
    cx, cy = mx - dy * bend, my + dx * bend
    a = math.atan2(y2 - cy, x2 - cx)
    h1 = (x2 - head * math.cos(a - .5), y2 - head * math.sin(a - .5)); h2 = (x2 - head * math.cos(a + .5), y2 - head * math.sin(a + .5))
    return f'M{x1} {y1} Q{cx:.1f} {cy:.1f} {x2} {y2} M{h1[0]:.1f} {h1[1]:.1f} L{x2} {y2} L{h2[0]:.1f} {h2[1]:.1f}'


def svg(w, h, paths, extra=''):
    return (f"<svg class='ov' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
            + ''.join(f"<path d='{d}' fill='none' stroke='{c}' stroke-width='{sw}' stroke-linecap='round' stroke-linejoin='round' {ex}/>" for d, c, sw, ex in paths)
            + extra + '</svg>')


def tangents(c1, r1, c2, r2):
    (x1, y1), (x2, y2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1); th = math.atan2(y2 - y1, x2 - x1); ph = math.acos((r1 - r2) / d)
    out = []
    for s in (1, -1):
        a = th + s * ph
        out.append(((x1 + r1 * math.cos(a), y1 + r1 * math.sin(a)), (x2 + r2 * math.cos(a), y2 + r2 * math.sin(a))))
    return out


SMEAR = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 100' preserveAspectRatio='none'>"
         "<path d='M7 40 C 40 16, 118 28, 168 19 S 266 12, 293 29 C 299 47, 289 63, 296 79 C 238 93, 150 83, 92 90 S 22 95, 9 80 C 2 64, 11 53, 7 40 Z' fill='%s'/>"
         "<path d='M18 31 C 86 22, 196 21, 284 27' stroke='#F9CF3F' stroke-width='5' fill='none' opacity='.75'/>"
         "<path d='M24 74 C 98 82, 206 76, 280 70' stroke='#D99A00' stroke-width='4' fill='none' opacity='.5'/></svg>") % HALDI
SMEAR_URI = 'data:image/svg+xml,' + urllib.parse.quote(SMEAR)

# ------------------------------------------------------------------ shared css
BASE = """
.ph{position:absolute;left:0;width:1080px;background-size:100% 100%;background-repeat:no-repeat}
.h{position:absolute;font-family:'RupeeV','Velista',serif;font-weight:400;line-height:1;letter-spacing:.01em;white-space:nowrap}
.t{position:absolute;font-family:'CormR','CormI',serif;font-style:italic;font-weight:400;line-height:1;white-space:nowrap}
.k{position:absolute;font-family:'KalamR','Kalam',cursive;font-weight:400;line-height:1.05;white-space:nowrap}
.ov{position:absolute;left:0;top:0}
.lg{position:absolute}
.ig{position:absolute;left:0;right:0;text-align:center;font-family:'Inter','Rupee',sans-serif}
.ig p{margin:0 0 4px}
.ig span{display:inline;font-weight:600;line-height:1.46;padding:.07em .34em;border-radius:.22em;-webkit-box-decoration-break:clone;box-decoration-break:clone}
"""
FEED_CSS = BASE + f"""
.card{{background:#F3E6D3}}
.fade{{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(rgba(251,245,234,0),rgba(251,245,234,.9) 72%)}}
.fl{{position:absolute;left:56px;bottom:50px;display:flex;flex-direction:column;gap:12px;align-items:flex-start}}
.fl p{{font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:27px;letter-spacing:.02em;color:{P_INK}}}
.fl b{{font-weight:500}}
.cta{{position:absolute;right:56px;bottom:50px;display:flex;align-items:center;gap:14px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:24px;letter-spacing:.22em;color:{P_INK};padding-bottom:8px;border-bottom:2.5px solid currentColor}}
.ink{{color:{P_INK}}} .rani{{color:{RANI_D}}}
"""
STORY_CSS = BASE + f"""
.card{{background:{OX}}}
.seam{{position:absolute;left:0;width:1080px;height:170px;background:linear-gradient({OX},rgba(44,3,5,0))}}
.fade{{position:absolute;left:0;right:0;top:1300px;height:620px;background:linear-gradient(rgba(26,1,3,0),rgba(26,1,3,.74) 40%,rgba(26,1,3,.88))}}
.pl{{position:absolute;left:0;right:0;top:1392px;text-align:center;font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:27px;letter-spacing:.03em;color:{W_CR}}}
.pl b{{font-weight:500}}
.cta{{position:absolute;left:0;right:0;top:1446px;display:flex;flex-direction:column;align-items:center;gap:8px;font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:26px;letter-spacing:.26em;color:{W_CR}}}
.cr{{color:{W_CR}}} .gold{{color:{GOLD}}}
"""


def p_photo(key='p_base', top=0, h=1350):
    return (f"<div class='ph' style=\"top:{top}px;height:{h}px;background-image:url('{U[key]}')\"></div>"
            + ("<div class='fade'></div>" if key == 'p_base' else ''))


def p_tab():
    return tab('bracelets')


def p_foot(cta, product=True, logo_right=False):
    left = (f"<div class='fl'>{logo(118, P_INK, '#C86F58')}<p>Prism Rivière Bracelet · <b>₹2,399</b></p></div>" if product else '')
    if logo_right:
        left += f"<div class='lg' style='right:58px;bottom:112px'>{logo(118, P_INK, '#C86F58')}</div>"
    return left + f"<div class='cta'>{cta}{ARROW}</div>"


def w_photo(mode='push', top=600):
    if mode == 'full':
        return f"<div class='ph' style=\"top:0;height:1920px;background-image:url('{U['w_full']}')\"></div><div class='fade'></div>"
    return (f"<div class='ph' style=\"top:{top}px;height:1320px;background-image:url('{U['w_push']}')\"></div>"
            f"<div class='seam' style='top:{top}px'></div><div class='fade'></div>")


def w_head(chip=True):
    out = f"<div class='lg safe' style='right:64px;top:314px'>{logo(104, W_CR, '#FFBDA8')}</div>"
    if chip:
        out += tab('earrings', x='left:64px', y='top:300px', radius='29px', extra='height:54px').replace("class='tab'", "class='tab safe'")
    return out


def w_foot(cta, line="Woven Gold Hoops · 25mm · 18k gold PVD · <b>₹1,199</b>"):
    return ((f"<div class='pl safe'>{line}</div>" if line else '')
            + f"<div class='cta safe'>{cta}{CHEV}</div>")


# ================================================================== PRISM · feed 1080 x 1350
def p1():
    css = ".big{left:44px;top:30px;font-size:236px;color:%s}" % P_INK
    marks = svg(1080, 1350, [(arrow(880, 392, 800, 468, bend=-.3), RANI, 4.5, '')])
    return css, (p_photo() + p_tab()
                 + "<div class='h big fit' style='width:990px'>TREAT</div>"
                 + f"<div class='t rani' style='left:318px;top:226px;font-size:106px'>yourself.</div>"
                 + f"<div class='k rani' style='left:700px;top:338px;font-size:38px;transform:rotate(-5deg)'>the treat that lasts.</div>"
                 + marks + p_foot('SHOP NOW'))


def p2():
    css = f"""
.nut{{position:absolute;left:40px;top:826px;width:430px;background:#FFFEFA;border:3px solid #141414;padding:12px 16px 12px;font-family:'Inter','Rupee',sans-serif;color:#141414;transform:rotate(-3deg);box-shadow:0 18px 36px rgba(60,30,20,.28)}}
.nut h4{{font-weight:900;font-size:46px;letter-spacing:-.02em;line-height:1;margin-bottom:6px}}
.nut p{{display:flex;justify-content:space-between;align-items:baseline;font-size:18px;line-height:1.18;padding:3px 0;border-top:1.5px solid #141414}}
.nut p.ss{{font-weight:600;border-top:none;padding-top:0}}
.nut p.cal{{font-weight:900;font-size:28px;border-top:none;padding:2px 0}}
.nut p.cal span:last-child{{font-size:38px}}
.nut p.pr{{font-weight:900;font-size:26px;border-top:none}}
.nut i{{display:block;background:#141414}} .nut .r8{{height:10px;margin:3px 0}} .nut .r4{{height:5px;margin-bottom:1px}}
.nut b{{font-weight:800;margin-right:6px}}
.nut small{{display:block;font-size:14px;line-height:1.3;border-top:1.5px solid #141414;padding-top:6px;font-weight:500}}
"""
    rows = [('Sugar', '', '0g'), ('Stones', 'cushion-cut CZ', '~5mm'), ('Halo', 'pavé', 'every stone'), ('Coating', 'PVD rhodium', 'yes'),
            ('Base', 'surgical steel', 'yes'), ('Tarnish', '', '0%'), ('Water', '', 'no problem')]
    label = ("<div class='nut'><h4>Nutrition Facts</h4><p class='ss'><span>Serving size</span><span>1 wrist (15–19cm)</span></p><i class='r8'></i>"
             "<p class='cal'><span>Calories</span><span>0</span></p><i class='r4'></i>"
             + ''.join(f"<p><span><b>{a}</b>{b}</span><span>{c}</span></p>" for a, b, c in rows)
             + "<i class='r8'></i><p class='pr'><span>Price</span><span>₹2,399</span></p>"
             "<small>Not for eating. Fine with sweat, water and daily wear.</small></div>")
    return css, (p_photo() + p_tab()
                 + f"<div class='h ink fit' style='left:56px;top:58px;font-size:120px;width:970px'>ZERO SUGAR.</div>"
                 + f"<div class='t rani' style='left:60px;top:178px;font-size:94px'>all sparkle.</div>"
                 + label + p_foot('LEARN MORE', product=False, logo_right=True))


def p3():
    ell = rough_ellipse(530, 615, 420, 196, rot=-19.3, seed=7)
    marks = svg(1080, 1350, [
        (ell, RANI, 6, ''),
        (arrow(842, 362, 770, 420, bend=-.25), RANI, 4.5, ''),
        (arrow(640, 1064, 672, 988, bend=.2, head=18), P_INK, 3.5, ''),
        (arrow(888, 1060, 902, 984, bend=-.2, head=18), P_INK, 3.5, ''),
        (arrow(1000, 795, 985, 712, bend=.25, head=18), P_INK, 3.5, ''),
    ])
    lab = lambda x, y, r: f"<div class='k ink' style='left:{x}px;top:{y}px;font-size:36px;transform:rotate({r}deg)'>sweet</div>"
    return '', (p_photo() + p_tab()
                + f"<div class='h ink fit' style='left:56px;top:58px;font-size:104px;width:970px'>ONE OF THESE</div>"
                + f"<div class='t rani' style='left:60px;top:168px;font-size:90px'>isn't a sweet.</div>"
                + marks
                + f"<div class='k rani' style='left:640px;top:296px;font-size:44px;transform:rotate(-4deg)'>not a sweet. ₹2,399</div>"
                + lab(600, 1070, -5) + lab(838, 1064, 4) + lab(952, 800, -3)
                + p_foot('SHOP NOW'))


def p4():
    css = f"""
.panel{{position:absolute;left:0;top:790px;width:1080px;height:560px;background:{RANI};color:{P_CREAM}}}
.cmp{{position:absolute;left:56px;right:56px;top:220px;display:grid;grid-template-columns:1fr 1.18fr;column-gap:26px;font-family:'Rupee','JostF',sans-serif}}
.cmp div{{font-size:25px;line-height:1.2;padding:9px 0;border-top:1.5px solid rgba(251,245,234,.35)}}
.cmp .hd{{font-weight:500;font-size:17px;letter-spacing:.2em;border-top:none;padding-bottom:6px;opacity:.85}}
.cmp .no{{font-weight:300;opacity:.62}}
.cmp .yes{{font-weight:500}}
.cmp .yes::before{{content:'';display:inline-block;width:11px;height:11px;border-radius:50%;background:{P_CREAM};margin:0 12px 3px 0}}
.panel .pfl{{position:absolute;left:56px;bottom:48px;display:flex;align-items:center;gap:20px;font-family:'Rupee','JostF',sans-serif;font-size:25px;letter-spacing:.02em}}
.panel .cta{{color:{P_CREAM};bottom:46px}}
"""
    rows = [('a soft layer', 'bonded in a vacuum'), ('wears off over time', 'far harder'), ('—', 'stands up to sweat'), ('—', 'waterproof, tarnish-free')]
    table = ("<div class='cmp'><div class='hd'>REGULAR PLATING</div><div class='hd'>NAIRA PVD</div>"
             + ''.join(f"<div class='no'>{a}</div><div class='yes'>{b}</div>" for a, b in rows) + '</div>')
    marks = svg(1080, 790, [(arrow(196, 132, 402, 238, bend=.2), P_INK, 3.5, ''), (arrow(906, 210, 1000, 262, bend=-.25), P_INK, 3.5, '')])
    return css, (p_photo('p_win', 0, 790) + p_tab() + marks
                 + f"<div class='k ink' style='left:46px;top:84px;font-size:40px;transform:rotate(-4deg)'>PVD coating</div>"
                 + f"<div class='k ink' style='left:700px;top:160px;font-size:40px;transform:rotate(3deg)'>sugar coating</div>"
                 + "<div class='panel'>"
                 + f"<div class='h fit' style='left:56px;top:40px;font-size:94px;width:968px;color:{P_CREAM}'>SUGAR COATING</div>"
                 + f"<div class='t' style='left:60px;top:136px;font-size:70px;color:{BLUSH}'>wears off. PVD doesn't.</div>"
                 + table
                 + f"<div class='pfl'>{logo(104, P_CREAM, '#FFBDA8')}<span>Prism Rivière Bracelet · ₹2,399</span></div>"
                 + f"<div class='cta'>LEARN MORE{ARROW}</div></div>")


def p5():
    css = f"""
.tagw{{position:absolute;left:64px;top:968px;transform:rotate(-8deg);filter:drop-shadow(0 14px 18px rgba(80,20,40,.32))}}
.tag{{position:relative;width:380px;height:222px;background:{RANI};clip-path:polygon(0 50%,15% 0,100% 0,100% 100%,15% 100%)}}
.tag .hole{{position:absolute;left:28px;top:96px;width:30px;height:30px;border-radius:50%;background:#EFE2CF;box-shadow:inset 0 0 0 5px #E3B98C}}
.tag .tt{{position:absolute;left:84px;top:22px;right:18px;color:{P_CREAM}}}
.tag .k1{{font-family:'KalamR','Kalam',cursive;font-size:42px;line-height:1.16}}
.tag .k1 u{{text-decoration:none;border-bottom:2px solid rgba(251,245,234,.7);padding:0 10px}}
.tag .sm{{margin-top:12px;font-family:'Rupee','JostF',sans-serif;font-weight:400;font-size:19px;letter-spacing:.04em;line-height:1.35}}
"""
    string = svg(1080, 1350, [('M108 1099 C 64 1010, 150 868, 214 770', RANI, 4, ''), ('M206 764 l16 10 m-14 2 l12 -12', RANI, 4, '')])
    tag = ("<div class='tagw'><div class='tag'><i class='hole'></i><div class='tt'>"
           "<p class='k1'>To: <u>you</u></p><p class='k1'>From: <u>me</u></p>"
           "<p class='sm'>Prism Rivière · ₹2,399<br>in a Naira Petite box</p></div></div></div>")
    return css, (p_photo() + p_tab()
                 + f"<div class='h ink fit' style='left:56px;top:58px;font-size:112px;width:970px'>FOR THE ONE</div>"
                 + f"<div class='t rani' style='left:60px;top:176px;font-size:92px'>you're sweet on.</div>"
                 + string + tag + p_foot('ORDER NOW', product=False, logo_right=True))


def p6():
    css = f"""
.sug{{position:absolute;left:178px;top:150px;font-family:'Velista',serif;font-size:268px;line-height:1;letter-spacing:.005em;white-space:nowrap;
  background:url('{U['p_tex']}') center/cover;-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-stroke:2.5px {RANI_D};
  filter:drop-shadow(0 10px 16px rgba(120,30,60,.34))}}
.code{{position:absolute;left:56px;top:432px;transform:rotate(-3deg);background:{RANI};color:{P_CREAM};font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:26px;letter-spacing:.18em;padding:14px 22px;border-radius:12px;box-shadow:0 10px 22px rgba(90,10,40,.28)}}
"""
    return css, (p_photo() + p_tab()
                 + f"<div class='h ink' style='left:56px;top:40px;font-size:106px'>SWEETER</div>"
                 + f"<div class='t rani' style='left:64px;top:250px;font-size:92px'>by</div>"
                 + "<div class='sug'>10%</div>"
                 + "<div class='code'>CODE NAIRA10</div>"
                 + p_foot('GET OFFER'))


def p7():
    css = ".ig span{background:#141414;color:#fff;font-size:46px} .ig.small span{font-size:30px;font-weight:500}"
    return css, (p_photo() + p_tab()
                 + "<div class='ig' style='top:96px'><p><span>pov: you came for the sweets</span></p><p><span>and left with the bracelet</span></p></div>"
                 + "<div class='ig small' style='top:1120px'><p><span>₹2,399 · waterproof · tarnish-free</span></p></div>"
                 + p_foot('BUY NOW'))


# ================================================================== WOVEN · story 1080 x 1920
def w1():
    css = f".smear{{padding:0 .16em;margin:0 -.03em;color:{OX};background:url(\"{SMEAR_URI}\") center/100% 96% no-repeat}}"
    return css, (w_photo() + w_head()
                 + f"<div class='h cr fit safe' style='left:60px;top:384px;font-size:138px;width:960px'>WATERPROOF.</div>"
                 + f"<div class='t gold safe' style='left:64px;top:530px;font-size:78px'>only the <span class='smear'>haldi</span> washes off.</div>"
                 + w_foot('SHOP NOW'))


def w2():
    top = 560
    css = f".cut{{position:absolute;left:0;top:{top}px;width:1080px;height:1320px;background:url('{U['w_hoops']}') 0 0/100% 100% no-repeat}}"
    ell = rough_ellipse(492, 806, 470, 152, rot=-4, seed=11, turns=1.08)
    marks = svg(1080, 1920, [(ell, HALDI, 6, ''), (arrow(842, 582, 806, 666, bend=-.3), HALDI, 4.5, '')])
    return css, (w_photo('push', top) + w_head()
                 + f"<div class='t gold safe' style='left:64px;top:430px;font-size:96px'>not a typo.</div>"
                 + f"<div class='h cr' style='left:58px;top:664px;font-size:300px'>₹1,199</div>"
                 + "<div class='cut'></div>" + marks
                 + f"<div class='k safe' style='left:690px;top:512px;font-size:44px;color:{HALDI};transform:rotate(-6deg)'>checked twice.</div>"
                 + w_foot('BUY NOW', "Woven Gold Hoops · 25mm braided · 18k gold PVD"))


def w3():
    big, R = (868, 712), 172
    small, r = (790, 1130), 95
    css = (f".lens{{position:absolute;left:{big[0] - R}px;top:{big[1] - R}px;width:{2 * R}px;height:{2 * R}px;border-radius:50%;background:url('{U['w_lens']}') center/cover;"
           f"box-shadow:0 0 0 6px {GOLD},0 0 0 9px rgba(0,0,0,.35),0 26px 50px rgba(0,0,0,.55)}}"
           ".lens::after{content:'';position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 30% 24%,rgba(255,255,255,.26),rgba(255,255,255,0) 44%)}")
    (a1, b1), (a2, b2) = tangents(big, R + 6, small, r)
    lines = [(f'M{a1[0]:.1f} {a1[1]:.1f} L{b1[0]:.1f} {b1[1]:.1f}', GOLD, 2.5, "stroke-dasharray='2 9'"),
             (f'M{a2[0]:.1f} {a2[1]:.1f} L{b2[0]:.1f} {b2[1]:.1f}', GOLD, 2.5, "stroke-dasharray='2 9'")]
    ring = f"<circle cx='{small[0]}' cy='{small[1]}' r='{r}' fill='none' stroke='{GOLD}' stroke-width='3.5'/>"
    return css, (w_photo() + w_head()
                 + f"<div class='h cr fit safe' style='left:60px;top:384px;font-size:122px;width:960px'>LOOK CLOSER.</div>"
                 + f"<div class='t gold safe' style='left:64px;top:510px;font-size:72px'>every strand is there.</div>"
                 + svg(1080, 1920, lines, ring) + "<div class='lens safe'></div>"
                 + w_foot('LEARN MORE'))


def w4():
    css = f"""
.chips{{position:absolute;left:60px;top:646px;width:980px;display:flex;flex-wrap:wrap;gap:14px 12px}}
.chip{{display:flex;align-items:center;gap:13px;height:68px;padding:0 26px 0 14px;border-radius:34px;background:rgba(30,2,4,.58);border:2px solid rgba(247,235,221,.5);
  font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:25px;letter-spacing:.18em;color:{W_CR}}}
.chip i{{width:40px;height:40px;border-radius:50%;background:{HALDI};display:grid;place-items:center}}
"""
    chips = ''.join(f"<div class='chip'><i>{TICK}</i>{f}</div>" for f in ['ROKA', 'HALDI', 'MEHENDI', 'SANGEET', 'PHERAS', 'RECEPTION'])
    return css, (w_photo() + w_head()
                 + f"<div class='h cr fit safe' style='left:60px;top:384px;font-size:136px;width:960px'>ONE PAIR.</div>"
                 + f"<div class='t gold safe' style='left:64px;top:524px;font-size:86px'>every function.</div>"
                 + f"<div class='chips safe'>{chips}</div>"
                 + w_foot('ORDER NOW'))


def w5():
    d = 336; r = d / 2; rr = r - 30
    css = f"""
.coin{{position:absolute;left:{846 - r:.0f}px;top:{690 - r:.0f}px;width:{d}px;height:{d}px;border-radius:50%;transform:rotate(9deg);
  background:radial-gradient(circle at 34% 28%,#FFF6CF 0%,#F3D687 20%,#DDB258 44%,#BE8F38 70%,#8C6320 100%);
  box-shadow:0 20px 44px rgba(0,0,0,.55),inset 0 0 0 3px rgba(255,240,200,.45),inset 0 -12px 26px rgba(90,50,10,.4)}}
.coin svg{{position:absolute;left:0;top:0}}
.cin{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#3A1406}}
.cin b{{font-family:'Velista',serif;font-weight:400;font-size:104px;line-height:.9}}
.cin span{{font-family:'Rupee','JostF',sans-serif;font-weight:500;font-size:24px;letter-spacing:.34em;margin-top:6px;padding-left:.34em}}
"""
    ring_txt = 'CODE NAIRA10 · ANY ORDER · NO MINIMUM · CODE NAIRA10 · ANY ORDER · NO MINIMUM · '
    circ = 2 * math.pi * rr
    coin = (f"<div class='coin safe'><svg width='{d}' height='{d}' viewBox='0 0 {d} {d}'><defs><path id='cr' d='M {r},{r} m -{rr},0 a {rr},{rr} 0 1,1 {2 * rr},0 a {rr},{rr} 0 1,1 -{2 * rr},0'/></defs>"
            f"<circle cx='{r}' cy='{r}' r='{r - 8}' fill='none' stroke='#6E4712' stroke-width='1.6' opacity='.6'/>"
            f"<circle cx='{r}' cy='{r}' r='{r - 52}' fill='none' stroke='#6E4712' stroke-width='1.6' opacity='.6'/>"
            f"<text font-family='JostF' font-weight='500' font-size='15' fill='#3A1406' textLength='{circ - 6:.0f}' lengthAdjust='spacing'><textPath href='#cr'>{ring_txt}</textPath></text>"
            "</svg><div class='cin'><b>10%</b><span>OFF</span></div></div>")
    return css, (w_photo() + w_head()
                 + f"<div class='h cr fit safe' style='left:60px;top:384px;font-size:112px;width:960px'>TAKE 10% OFF.</div>"
                 + f"<div class='t gold safe' style='left:64px;top:500px;font-size:80px'>keep all the gold.</div>"
                 + coin + w_foot('GET OFFER', "Woven Gold Hoops · <b>₹1,199</b> · 10% off with NAIRA10"))


def w6():
    s, x0, y0 = 1080 / 1287, 313, 513                 # push placement maps source -> frame
    def P(fx, fy):                                     # from the full-bleed grid (scale 1080/1296, x0 308) to push coords
        sx, sy = fx / (1080 / 1296) + 308, fy / (1080 / 1296)
        return round((sx - x0) * s), round(600 + (sy - y0) * s)
    css = f"""
.fp{{position:absolute;font-family:'Plex',monospace;font-weight:500;font-size:23px;letter-spacing:.06em;color:{W_CR};white-space:nowrap}}
.fp em{{font-style:normal;color:{HALDI};margin-right:12px}}
"""
    A = {'tab': P(330, 830), 'top': P(590, 700), 'lb': P(330, 1135), 'rb': P(800, 1050)}
    L = [  # label (x, y, align), anchor, text
        ((64, 690, 'l'), A['tab'], '<em>01</em>BRAIDED ROPE OF GOLD-TONE STRANDS'),
        ((1016, 742, 'r'), A['top'], '<em>02</em>18K GOLD PVD COATING'),
        ((64, 1352, 'l'), A['lb'], '<em>03</em>SURGICAL STAINLESS STEEL'),
        ((1016, 1390, 'r'), A['rb'], '<em>04</em>WATERPROOF · TARNISH-FREE'),
    ]
    paths, labels, dots = [], '', ''
    for (x, y, al), (ax, ay), txt in L:
        ly = y + 13
        sx_ = x + (8 if al == 'l' else -8)
        paths.append((f'M{sx_} {ly + (18 if ly < ay else -18)} L{ax} {ay}', W_CR, 1.8, "opacity='.85'"))
        dots += f"<circle cx='{ax}' cy='{ay}' r='7' fill='{HALDI}' stroke='{OX}' stroke-width='2'/>"
        pos = f'left:{x}px' if al == 'l' else f'right:{1080 - x}px'
        labels += f"<div class='fp safe' style='{pos};top:{y}px'>{txt}</div>"
    dim = (f"<path d='M470 828 H962 M470 816 V840 M962 816 V840' stroke='{W_CR}' stroke-width='2' fill='none'/>"
           f"<text x='716' y='808' text-anchor='middle' font-family='Plex' font-size='21' font-weight='500' letter-spacing='1.5' fill='{W_CR}'>25 MM</text>")
    return css, (w_photo() + w_head()
                 + f"<div class='h cr fit safe' style='left:60px;top:384px;font-size:104px;width:960px'>THE FINE PRINT.</div>"
                 + f"<div class='t gold safe' style='left:64px;top:494px;font-size:80px'>all good news.</div>"
                 + svg(1080, 1920, paths, dim + dots) + labels
                 + "<div class='pl safe' style='top:1428px;font-family:Plex,monospace;font-weight:500;font-size:23px;letter-spacing:.06em'><span style='color:#F2B705'>05</span>&nbsp;&nbsp;HYPOALLERGENIC · ONE PAIR · ₹1,199</div>"
                 + f"<div class='cta safe' style='top:1466px'>SHOP NOW{CHEV}</div>")


def w7():
    css = ".ig span{background:#fff;color:#141414;font-size:48px} .ig.small span{font-size:38px;font-weight:600}"
    return css, (w_photo('full') + w_head()
                 + "<div class='ig safe' style='top:388px'><p><span>pov: someone asks if</span></p><p><span>your hoops are real gold</span></p></div>"
                 + "<div class='ig small safe' style='top:1262px'><p><span>18k gold PVD on surgical steel</span></p><p><span>₹1,199. you can tell them.</span></p></div>"
                 + w_foot('SHOP NOW', None))


P_ADS = [('P1', 'treat-yourself', p1), ('P2', 'zero-sugar-label', p2), ('P3', 'one-of-these', p3), ('P4', 'sugar-coating-vs-pvd', p4),
         ('P5', 'gift-tag', p5), ('P6', 'sweeter-by-10', p6), ('P7', 'pov-sweets', p7)]
W_ADS = [('W1', 'waterproof-haldi', w1), ('W2', 'price-not-a-typo', w2), ('W3', 'look-closer', w3), ('W4', 'every-function', w4),
         ('W5', 'take-10-off', w5), ('W6', 'fine-print', w6), ('W7', 'pov-real-gold', w7)]

if __name__ == '__main__':
    import sys
    only = set(sys.argv[1:])
    jobs = []
    for vid, slug, fn in P_ADS:
        if only and vid not in only: continue
        css, body = fn(); jobs.append((f'{vid}_prism-sugar_{slug}_feed', doc(*FEED, FEED_CSS + css, body), FEED))
    for vid, slug, fn in W_ADS:
        if only and vid not in only: continue
        css, body = fn(); jobs.append((f'{vid}_woven-red_{slug}_story', doc(*STORY, STORY_CSS + css, body), STORY))
    render(jobs)
