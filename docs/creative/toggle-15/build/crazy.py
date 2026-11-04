# Toggle 10 crazy: ten hook tests for the Toggle Link Chain, built only on photos that passed the clasp audit (audit.json),
# because Higgsfield had 1.71 credits. The craziness is in the hook and the format, from the research (README): lo-fi
# (a sticky note, marker scribbles), platform-native (a plain post, a notes-style list, a hyperlink), the clever one (a
# Bollywood title), the candid price reveal, one core idea, and the four-panel checkerboard.
# Usage: crazy.py [key ...] -> <scratchpad>/toggle15/crazy/<key>_{feed,story}.jpg
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CR = os.path.normpath(os.path.join(HERE, "../.."))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
OUT = f"{SPB}/toggle15/crazy"
F1 = f"{SPB}/c4/fonts"; F2 = f"{SPB}/toggle15/fonts"
BRAND = os.path.join(CR, "finished-ads/brand")
SIZE = {"feed": (1080, 1350), "story": (1080, 1920)}
PRICE = "₹1,199"

# the four photos that passed, with the clasp's ring centre and the pave bar's two ends in plate pixels
PL = {
 "worn":  {"f": "performance/plates/toggle-link-chain-worn.jpg", "w": 1080, "h": 1920, "ring": (526, 1063), "r": 76, "bar": ((455, 976), (526, 1039))},
 "sage":  {"f": "colour-camps/plates/SAGE/sage_YF5143_S1_a5g.jpg", "w": 1080, "h": 1935, "ring": (365, 1260), "r": 108, "bar": ((291, 1127), (344, 1249))},
 "night": {"f": "performance/plates/crazy3/02-toggle-link-chain-night.jpg", "w": 1080, "h": 1920, "ring": (686, 1388), "r": 73, "bar": ((589, 1338), (679, 1375))},
 "clips": {"f": "performance/plates/colour/51-toggle-link-chain.jpg", "w": 1080, "h": 1920, "ring": (712, 1462), "r": 92, "bar": ((588, 1407), (699, 1439))},
}

CSS = """
@font-face{font-family:CG;src:url("file://%(f1)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f1)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f1)s/Jost[wght].ttf");font-weight:100 900}
@font-face{font-family:Kalam;src:url("file://%(f2)s/Kalam-Regular.ttf");font-weight:400}
@font-face{font-family:Kalam;src:url("file://%(f2)s/Kalam-Bold.ttf");font-weight:700}
@font-face{font-family:Inter;src:url("file://%(f2)s/Inter[opsz,wght].ttf");font-weight:100 900}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;background:#F3EDE4}
.ph{position:absolute;inset:0;background-repeat:no-repeat}
.abs{position:absolute}
.cgi{font-family:CGI;font-weight:500;letter-spacing:-.005em;line-height:1.0;text-wrap:balance}
.cg{font-family:CG;font-weight:500}
.jost{font-family:Jost;font-weight:500;letter-spacing:.2em;text-transform:uppercase}
.kalam{font-family:Kalam}
.inter{font-family:Inter}
svg{position:absolute;inset:0;overflow:visible}
"""

def place(pl, W, H, s=None, focus=None, at=None):
    """Cover-fit the plate at scale s (at least cover), putting plate point `focus` at canvas point `at` (clamped)."""
    p = PL[pl]; cover = max(W / p["w"], H / p["h"]); s = max(s or cover, cover)
    bw, bh = p["w"] * s, p["h"] * s
    fx, fy = focus or (p["w"] / 2, p["h"] / 2); ax, ay = at or (W / 2, H / 2)
    bx = min(0, max(W - bw, ax - fx * s)); by = min(0, max(H - bh, ay - fy * s))
    m = lambda x, y: (x * s + bx, y * s + by)
    html = ('<div class="ph" style="background-image:url(\'file://%s\');background-size:%.1fpx %.1fpx;background-position:%.1fpx %.1fpx"></div>'
            % (os.path.join(CR, p["f"]), bw, bh, bx, by))
    return html, m, s

def logo(kind, x, y, w, center=False):
    st = "left:%dpx;top:%dpx;width:%dpx" % (x - (w // 2 if center else 0), y, w)
    return '<img class="abs" src="file://%s" style="%s">' % (os.path.join(BRAND, "logo_%s.png" % kind), st)

def name_price(x, y, color, w=None, align="left", ns=30, ps=62, gap=6, row=False):
    st = "left:%dpx;top:%dpx;color:%s;text-align:%s;%s" % (x, y, color, align, ("width:%dpx;" % w) if w else "")
    if row:
        return ('<div class="abs" style="%s;display:flex;gap:22px;align-items:baseline;justify-content:%s"><span class="jost" style="font-size:%dpx">Toggle Link Chain</span>'
                '<span class="cg" style="font-size:%dpx;line-height:1">%s</span></div>') % (st, {"left": "flex-start", "center": "center", "right": "flex-end"}[align], ns, ps, PRICE)
    return ('<div class="abs" style="%s"><div class="jost" style="font-size:%dpx;line-height:1.3">Toggle Link Chain</div>'
            '<div class="cg" style="font-size:%dpx;line-height:1;margin-top:%dpx">%s</div></div>') % (st, ns, ps, gap, PRICE)

def fade(side, h, rgb, a0, a1=0.0, mid=None):
    mid = mid if mid is not None else (a0 + a1) / 2
    d = "to bottom" if side == "top" else "to top"
    return ('<div class="abs" style="left:0;right:0;%s:0;height:%dpx;background:linear-gradient(%s,rgba(%s,%.2f) 0%%,rgba(%s,%.2f) 55%%,rgba(%s,%.2f) 100%%)"></div>'
            % (side, h, d, rgb, a0, rgb, mid, rgb, a1))

# hand-drawn marker shapes: two slightly different passes read as a felt-tip, not a vector
def m_ellipse(cx, cy, rx, ry, col, wdt=7, rot=-6):
    def one(dx, dy, k, start):
        import math
        pts = []
        for i in range(0, 39):
            t = start + i / 36 * 2 * math.pi * 1.08
            pts.append((cx + dx + rx * k * math.cos(t), cy + dy + ry * k * math.sin(t)))
        return "M" + " L".join("%.1f %.1f" % p for p in pts)
    return ('<svg><g transform="rotate(%d %d %d)" fill="none" stroke="%s" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="%s" stroke-width="%d" opacity=".92"/><path d="%s" stroke-width="%d" opacity=".55"/></g></svg>'
            % (rot, cx, cy, col, one(0, 0, 1.0, -0.4), wdt, one(4, -3, 1.04, -0.25), max(2, wdt - 3)))

def m_arrow(x0, y0, cx, cy, x1, y1, col, wdt=7, head=30):
    import math
    ang = math.atan2(y1 - cy, x1 - cx)
    a1 = (x1 - head * math.cos(ang - 0.45), y1 - head * math.sin(ang - 0.45))
    a2 = (x1 - head * math.cos(ang + 0.45), y1 - head * math.sin(ang + 0.45))
    return ('<svg><g fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f"/><path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f"/></g></svg>'
            % (col, wdt, x0, y0, cx, cy, x1, y1, a1[0], a1[1], x1, y1, a2[0], a2[1]))

def m_check(x, y, col, sz=40, wdt=7):
    return ('<svg><path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            % (x, y + sz * .55, x + sz * .38, y + sz * .92, x + sz * 1.05, y, col, wdt))

INK, IVORY, GOLD, RED = "#1A1614", "#FBF8F3", "#E8C98F", "#D23B2A"

# ---------- the ten ads ----------
def x01(fmt, W, H, line=("Kabhi front.", "Kabhi side."), sub=None):
    if fmt == "feed":
        ph, m, s = place("worn", W, H, focus=PL["worn"]["ring"], at=(540, 600))
        body = (ph + fade("bottom", 420, "251,248,243", .55, 0, .30) +
                '<div class="abs cgi" style="left:0;right:0;top:%dpx;text-align:center;color:%s;font-size:96px">%s<br>%s</div>' % (1010, INK, line[0], line[1]) +
                (('<div class="abs jost" style="left:0;right:0;top:1218px;text-align:center;color:%s;font-size:27px;letter-spacing:.12em">%s</div>' % (INK, sub)) if sub else "") +
                name_price(0, 1268 if sub else 1236, INK, w=W, align="center", ns=27, ps=46, row=True) + logo("white", 72, 66, 150))
    else:
        ph, m, s = place("worn", W, H)
        body = (ph + fade("top", 760, "251,248,243", .97, 0, .78) + logo("ink", 540, 300, 170, center=True) +
                '<div class="abs cgi" style="left:0;right:0;top:372px;text-align:center;color:%s;font-size:112px">%s<br>%s</div>' % (INK, line[0], line[1]) +
                (('<div class="abs jost" style="left:0;right:0;top:612px;text-align:center;color:%s;font-size:30px;letter-spacing:.12em">%s</div>' % (INK, sub)) if sub else "") +
                # name and price on a soft dark band over the lower chest, ending above y=1500 (clear of the Story's Shop button)
                '<div class="abs" style="left:0;right:0;top:1380px;height:150px;background:linear-gradient(to bottom,rgba(20,11,9,0),rgba(20,11,9,.38) 50%,rgba(20,11,9,0))"></div>' +
                name_price(0, 1418, IVORY, w=W, align="center", ns=30, ps=56, row=True))
    return body

def x10(fmt, W, H):
    return x01(fmt, W, H, line=("No more", "&lsquo;hook laga do&rsquo;."), sub="The clasp sits at the front")

def sticky(x, y, w, rot, lines, fs=54, price=True):
    tape = '<div class="abs" style="left:%dpx;top:-26px;width:170px;height:52px;background:rgba(255,255,255,.55);transform:rotate(-4deg);box-shadow:0 1px 3px rgba(0,0,0,.08)"></div>' % (w // 2 - 85)
    txt = "".join('<div>%s</div>' % l for l in lines)
    pr = ('<div style="margin-top:22px;font-size:%dpx;opacity:.85">Toggle Link Chain, %s</div>' % (int(fs * .62), PRICE)) if price else ""
    return ('<div class="abs kalam" style="left:%dpx;top:%dpx;width:%dpx;padding:52px 46px 40px;background:linear-gradient(170deg,#FFF3A6,#FFE16B);'
            'color:#211c12;font-size:%dpx;line-height:1.12;transform:rotate(%.1fdeg);box-shadow:0 22px 34px rgba(0,0,0,.28),0 2px 4px rgba(0,0,0,.12)">%s%s%s</div>'
            % (x, y, w, fs, rot, tape, txt, pr))

def x02(fmt, W, H):
    lines = ["Note to self:", "the clasp goes", 'in <span style="font-weight:700;text-decoration:underline;text-decoration-thickness:5px;text-underline-offset:8px">FRONT</span>.']
    if fmt == "feed":
        ph, m, s = place("worn", W, H, focus=PL["worn"]["ring"], at=(470, 760))
        rx, ry = m(*PL["worn"]["ring"])
        body = (ph + sticky(560, 70, 440, 3.5, lines, fs=52) +
                m_arrow(590, 492, 420, 560, rx - 8, ry - 96, INK, 9, 38) + logo("ink", 540, 1250, 150, center=True))
    else:
        ph, m, s = place("worn", W, H)
        rx, ry = m(*PL["worn"]["ring"])
        body = (ph + fade("top", 420, "251,248,243", .9, 0, .5) + logo("ink", 72, 300, 150) +
                sticky(540, 400, 460, 3.5, lines, fs=56) + m_arrow(580, 820, 400, 880, rx - 8, ry - 98, INK, 10, 40))
    return body

def post_card(x, y, w, text, fs=46):
    av = ('<div style="width:84px;height:84px;border-radius:50%%;background:#F1E4DC;display:flex;align-items:center;justify-content:center;flex:none">'
          '<img src="file://%s" style="width:62px"></div>' % os.path.join(BRAND, "logo_ink.png"))
    head = ('<div style="display:flex;gap:20px;align-items:center;margin-bottom:24px">%s<div><div style="font-weight:700;font-size:34px;color:#0f0f0f">Naira</div>'
            '<div style="font-size:27px;color:#6b6b6b;margin-top:2px">nairaflore.com</div></div></div>' % av)
    foot = '<div style="margin-top:26px;font-size:28px;color:#6b6b6b">Toggle Link Chain &middot; %s</div>' % PRICE
    return ('<div class="abs inter" style="left:%dpx;top:%dpx;width:%dpx;padding:38px 42px 34px;background:#fff;border-radius:30px;'
            'box-shadow:0 18px 40px rgba(0,0,0,.18)">%s<div style="font-weight:500;font-size:%dpx;line-height:1.24;color:#0f0f0f;letter-spacing:-.01em">%s</div>%s</div>'
            % (x, y, w, head, fs, text, foot))

def x03(fmt, W, H):
    t = "Unpopular opinion: the clasp is the best part of a necklace."
    if fmt == "feed":
        ph, m, s = place("sage", W, H, focus=PL["sage"]["ring"], at=(400, 1000))
        return ph + post_card(64, 52, 952, t, fs=44)
    ph, m, s = place("sage", W, H, s=1.02, focus=PL["sage"]["ring"], at=(380, 1220))
    return ph + post_card(64, 300, 952, t, fs=50)

def x04(fmt, W, H):
    if fmt == "feed":
        ph, m, s = place("night", W, H, focus=PL["night"]["ring"], at=(686, 930))
        return (ph + fade("bottom", 380, "12,10,10", .55, 0, .3) + logo("white", 72, 64, 150) +
                '<div class="abs cgi" style="left:72px;top:1046px;color:%s;font-size:104px">Looks expensive.</div>' % IVORY +
                '<div class="abs cg" style="left:72px;top:1158px;color:%s;font-size:104px;line-height:1">Isn&rsquo;t.</div>' % GOLD +
                name_price(560, 1178, IVORY, w=448, align="right", ns=27, ps=72))
    ph, m, s = place("night", W, H)
    return (ph + fade("top", 620, "12,10,10", .75, 0, .45) + logo("white", 72, 300, 160) +
            '<div class="abs cgi" style="left:72px;top:386px;color:%s;font-size:118px">Looks expensive.</div>' % IVORY +
            '<div class="abs cg" style="left:72px;top:510px;color:%s;font-size:118px;line-height:1">Isn&rsquo;t. <span style="font-size:.62em;color:%s;margin-left:10px">%s</span></div>' % (GOLD, IVORY, PRICE) +
            '<div class="abs jost" style="left:72px;top:1462px;color:%s;font-size:28px">Toggle Link Chain</div>' % IVORY)

def x05(fmt, W, H):
    if fmt == "feed":
        ph, m, s = place("clips", W, H, focus=PL["clips"]["ring"], at=(712, 880))
        return (ph + logo("ink", 72, 1052, 150) +
                '<div class="abs cgi" style="left:72px;top:1110px;color:%s;font-size:100px">Gem clip, promoted.</div>' % INK +
                name_price(72, 1230, INK, ns=27, ps=46, row=True))
    ph, m, s = place("clips", W, H)
    return (ph + logo("ink", 72, 300, 160) +
            '<div class="abs cgi" style="left:72px;top:376px;color:%s;font-size:118px">Gem clip,<br>promoted.</div>' % INK +
            name_price(72, 640, INK, ns=30, ps=56, row=True))

def x06(fmt, W, H):
    link = ('<span class="inter" style="font-style:normal;font-weight:600;color:#6FA8FF;text-decoration:underline;text-decoration-thickness:6px;'
            'text-underline-offset:10px;letter-spacing:-.02em;font-size:.86em">link</span>')
    if fmt == "feed":
        ph, m, s = place("night", W, H, s=1.18, focus=PL["night"]["ring"], at=(600, 900))
        return (ph + fade("top", 420, "12,10,10", .7, 0, .4) + logo("white", 72, 64, 150) +
                '<div class="abs cgi" style="left:72px;top:150px;color:%s;font-size:124px">Tap the %s.</div>' % (IVORY, link) +
                name_price(72, 1210, IVORY, ns=27, ps=46, row=True))
    ph, m, s = place("night", W, H, s=1.2, focus=PL["night"]["ring"], at=(600, 1280))
    return (ph + fade("top", 760, "12,10,10", .8, 0, .5) + logo("white", 72, 300, 160) +
            '<div class="abs cgi" style="left:72px;top:390px;color:%s;font-size:140px">Tap the %s.</div>' % (IVORY, link) +
            '<div class="abs jost" style="left:72px;top:1462px;color:%s;font-size:28px">Toggle Link Chain &middot; <span class="cg" style="letter-spacing:0;font-size:40px;text-transform:none">%s</span></div>' % (IVORY, PRICE))

def x07(fmt, W, H):
    if fmt == "feed":
        ph, m, s = place("sage", W, H, s=1.18, focus=PL["sage"]["ring"], at=(430, 830))
    else:
        ph, m, s = place("sage", W, H, s=1.3, focus=PL["sage"]["ring"], at=(420, 1060))
    (rx, ry), R = m(*PL["sage"]["ring"]), PL["sage"]["r"] * s
    (b0x, b0y), (b1x, b1y) = m(*PL["sage"]["bar"][0]), m(*PL["sage"]["bar"][1])
    lx, ly = m(520, 1110)                       # a link on the right-hand strand
    def lab(x, y, t, fs=42, w=None):
        return ('<div class="abs kalam" style="left:%dpx;top:%dpx;%scolor:%s;font-size:%dpx;line-height:1.08;font-weight:700;background:rgba(251,248,243,.86);'
                'padding:8px 16px 6px;border-radius:10px;transform:rotate(-1.5deg)">%s</div>' % (x, y, ("width:%dpx;" % w) if w else "", RED, fs, t))
    st = fmt == "story"
    title = ('<div class="abs kalam" style="left:64px;top:%dpx;color:%s;font-size:%dpx;font-weight:700;line-height:1.02">Anatomy of a<br>show-off clasp</div>'
             % (300 if st else 60, INK, 80 if st else 70))
    body = ph + fade("top", 700 if st else 380, "236,244,239", .88, 0, .55) + title + logo("ink", 846 if st else 860, 312 if st else 70, 170 if st else 150)
    body += m_ellipse(rx, ry, R * 1.24, R * 1.18, RED, 8, -8)                       # the ring
    if st:
        body += lab(40, 650, "toggle bar,<br>one line of tiny<br>clear stones", 44) + m_arrow(300, 800, 330, 850, b0x + 4, b0y + 18, RED, 7, 28)
        body += lab(610, 1235, "the ring,<br>about 15&nbsp;mm", 46) + m_arrow(640, 1240, 560, 1215, rx + R * .78, ry + R * .9, RED, 7, 28)
        body += lab(640, 600, "4&nbsp;mm paperclip<br>links, 50&nbsp;cm", 44) + m_arrow(720, 735, 700, 790, lx + 8, ly - 14, RED, 7, 28)
        body += name_price(64, 1430, INK, ns=28, ps=48, row=True)
    else:
        body += lab(40, 455, "toggle bar,<br>one line of tiny<br>clear stones", 40) + m_arrow(260, 600, 300, 640, b0x + 4, b0y + 16, RED, 7, 26)
        body += lab(600, 985, "the ring, about 15&nbsp;mm", 42) + m_arrow(620, 990, 560, 975, rx + R * .8, ry + R * .78, RED, 7, 26)
        body += lab(660, 452, "4&nbsp;mm paperclip<br>links, 50&nbsp;cm", 40) + m_arrow(730, 575, 690, 615, lx + 8, ly - 12, RED, 7, 26)
        body += name_price(64, 1196, INK, ns=27, ps=44, row=True)
    return body

def checklist(x, y, w, items, fs=46, head=56):
    rows = "".join('<div style="display:flex;align-items:center;gap:22px;margin-top:16px"><div style="position:relative;width:46px;height:46px;flex:none;border:3px solid #2b2b2b;border-radius:9px">'
                   '%s</div><div class="kalam" style="font-size:%dpx;line-height:1.1">%s</div></div>' % (m_check(4, 2, RED, 40, 7), fs, it) for it in items)
    return ('<div class="abs inter" style="left:%dpx;top:%dpx;width:%dpx;padding:40px 44px 40px;background:#FFFDF6;border-radius:30px;color:#151515;'
            'box-shadow:0 18px 40px rgba(0,0,0,.2)"><div style="font-weight:700;font-size:%dpx;letter-spacing:-.02em">Goes with:</div>%s'
            '<div style="margin-top:26px;font-size:27px;color:#6b6b6b">Toggle Link Chain &middot; %s</div></div>' % (x, y, w, head, rows, PRICE))

def x08(fmt, W, H):
    items = ["white tee", "office shirt", "kurta", "saree blouse", "turtleneck", "the Monday after the wedding"]
    if fmt == "feed":
        ph, m, s = place("worn", W, H, s=1.0, focus=PL["worn"]["ring"], at=(540, 820))
        return ph + checklist(520, 46, 500, items[:5] + [items[5]], fs=38, head=48) + logo("ink", 72, 1250, 150)
    ph, m, s = place("worn", W, H)
    return ph + checklist(72, 300, 640, items, fs=46, head=56)

def x09(fmt, W, H):
    # checkerboard: text / photo on the first row, photo / text on the second
    if fmt == "feed":
        gx, gy, tw, th = 0, 0, 540, 675
    else:
        gx, gy, tw, th = 0, 300, 540, 600
    def photo_tile(pl, x, y, s, at):
        p = PL[pl]; ph, m, _ = place(pl, tw, th, s=s, focus=p["ring"], at=at)
        return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;overflow:hidden">%s</div>' % (x, y, tw, th, ph)
    t1 = ('<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:#F1E4DC;display:flex;flex-direction:column;justify-content:center;padding:0 52px">'
          '<div class="cgi" style="font-size:%dpx;color:%s">The clasp<br>is the<br>point.</div></div>') % (gx, gy, tw, th, 92 if fmt == "feed" else 86, INK)
    t2 = ('<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:#1A1614;color:%s;display:flex;flex-direction:column;justify-content:center;padding:0 52px">'
          '<div class="jost" style="font-size:24px;letter-spacing:.16em;margin-bottom:14px">Toggle Link Chain</div><div class="cg" style="font-size:84px;line-height:1">%s</div><div class="jost" style="font-size:24px;letter-spacing:.14em;line-height:1.6;margin-top:22px">Gift-boxed<br>Free insured shipping<br>Front or side</div>'
          '<img src="file://%s" style="width:130px;margin-top:30px"></div>') % (gx + tw, gy + th, tw, th, IVORY, PRICE, os.path.join(BRAND, "logo_white.png"))
    body = t1 + photo_tile("worn", gx + tw, gy, 1.35, (270, 360 if fmt == "feed" else 320)) + photo_tile("sage", gx, gy + th, 1.25, (300, 330 if fmt == "feed" else 300)) + t2
    if fmt == "story":
        body = '<div class="abs" style="inset:0;background:#F3EDE4"></div>' + body
    return body

ADS = {"X01_kabhi_front": x01, "X02_sticky_note": x02, "X03_unpopular_opinion": x03, "X04_looks_expensive": x04, "X05_gem_clip": x05,
       "X06_tap_the_link": x06, "X07_anatomy": x07, "X08_goes_with": x08, "X09_checkerboard": x09, "X10_hook_laga_do": x10}

def main():
    keys = sys.argv[1:] or list(ADS)
    os.makedirs(OUT, exist_ok=True); tmp = tempfile.mkdtemp(dir=f"{SPB}/toggle15"); jobs = []
    for k in keys:
        for fmt in ("feed", "story"):
            W, H = SIZE[fmt]
            page = "<!doctype html><html><head><meta charset=utf-8><style>%s</style></head><body>%s</body></html>" % (CSS % dict(f1=F1, f2=F2, w=W, h=H), ADS[k](fmt, W, H))
            p = os.path.join(tmp, f"{k}_{fmt}.html"); open(p, "w").write(page)
            jobs.append({"html": p, "out": os.path.join(OUT, f"{k}_{fmt}.jpg"), "w": W, "h": H})
    jp = os.path.join(tmp, "jobs.json"); json.dump(jobs, open(jp, "w"))
    r = subprocess.run(["node", os.path.join(HERE, "shot.cjs"), jp], capture_output=True, text=True)
    print(r.stdout.strip()[-800:], r.stderr.strip()[-800:])

if __name__ == "__main__":
    main()
