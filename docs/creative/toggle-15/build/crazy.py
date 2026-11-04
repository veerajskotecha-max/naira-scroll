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

def name_price(x, y, color, w=None, align="left", ns=32, ps=62, gap=6, row=False):
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
def x01(fmt, W, H, line=("Kabhi front.", "Kabhi side."), sub="The clasp sits front or side"):
    if fmt == "feed":
        # the tank's neckline dips lowest in the middle (canvas y ~1020), so the block sits on white cotton only
        ph, m, s = place("worn", W, H, focus=PL["worn"]["ring"], at=(540, 523))
        return (ph + fade("bottom", 380, "251,248,243", .6, 0, .32) +
                '<div class="abs cgi" style="left:0;right:0;top:1032px;text-align:center;color:%s;font-size:82px">%s<br>%s</div>' % (INK, line[0], line[1]) +
                '<div class="abs jost" style="left:0;right:0;top:1206px;text-align:center;color:%s;font-size:28px;letter-spacing:.14em">%s</div>' % (INK, sub) +
                name_price(0, 1252, INK, w=W, align="center", ns=32, ps=52, row=True))
    ph, m, s = place("worn", W, H)
    cloud = '<div class="abs" style="left:40px;top:250px;width:1000px;height:460px;background:radial-gradient(ellipse at 50%% 50%%,rgba(251,248,243,.94) 0%%,rgba(251,248,243,.82) 42%%,rgba(251,248,243,0) 72%%)"></div>'
    return (ph + cloud + logo("ink", 540, 304, 160, center=True) +
            '<div class="abs cgi" style="left:0;right:0;top:372px;text-align:center;color:%s;font-size:104px">%s<br>%s</div>' % (INK, line[0], line[1]) +
            '<div class="abs jost" style="left:0;right:0;top:594px;text-align:center;color:%s;font-size:30px;letter-spacing:.14em">%s</div>' % (INK, sub) +
            '<div class="abs" style="left:0;right:0;top:1372px;height:160px;background:linear-gradient(to bottom,rgba(20,11,9,0),rgba(20,11,9,.40) 50%%,rgba(20,11,9,0))"></div>' +
            name_price(0, 1412, IVORY, w=W, align="center", ns=32, ps=58, row=True))

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
                m_arrow(590, 492, 420, 560, rx - 8, ry - 114, INK, 9, 38) + logo("ink", 540, 1250, 150, center=True))
    else:
        ph, m, s = place("worn", W, H)
        rx, ry = m(*PL["worn"]["ring"])
        body = (ph + fade("top", 380, "251,248,243", .85, 0, .45) + logo("ink", 400, 304, 150, center=True) +
                sticky(540, 400, 460, 3.5, lines, fs=56) + m_arrow(580, 820, 400, 880, rx - 8, ry - 116, INK, 10, 40))
    return body

def post_card(x, y, w, text, fs=46, img=None):
    """A plain post from Naira: avatar, name, the line, optionally a photo inside the card, the product and price."""
    av = ('<div style="width:84px;height:84px;border-radius:50%%;background:#F1E4DC;display:flex;align-items:center;justify-content:center;flex:none">'
          '<img src="file://%s" style="width:62px"></div>' % os.path.join(BRAND, "logo_ink.png"))
    head = ('<div style="display:flex;gap:20px;align-items:center;margin-bottom:24px">%s<div><div style="font-weight:700;font-size:34px;color:#0f0f0f">Naira</div>'
            '<div style="font-size:28px;color:#6b6b6b;margin-top:2px">nairaflore.com</div></div></div>' % av)
    pic = ""
    if img:   # (plate, crop box in plate px, display height)
        pl, (x0, y0, x1, y1), dh = img; p = PL[pl]; iw = w - 84; s = iw / (x1 - x0)
        pic = ('<div style="margin-top:26px;width:%dpx;height:%dpx;border-radius:18px;background-image:url(\'file://%s\');background-repeat:no-repeat;'
               'background-size:%.1fpx %.1fpx;background-position:%.1fpx %.1fpx"></div>' % (iw, dh, os.path.join(CR, p["f"]), p["w"] * s, p["h"] * s, -x0 * s, -y0 * s))
    foot = '<div style="margin-top:24px;font-size:32px;color:#4a4a4a">Toggle Link Chain &middot; %s</div>' % PRICE
    return ('<div class="abs inter" style="left:%dpx;top:%dpx;width:%dpx;padding:38px 42px 34px;background:#fff;border-radius:30px;'
            'box-shadow:0 18px 40px rgba(0,0,0,.14)">%s<div style="font-weight:500;font-size:%dpx;line-height:1.22;color:#0f0f0f;letter-spacing:-.01em">%s</div>%s%s</div>'
            % (x, y, w, head, fs, text, pic, foot))

def x03(fmt, W, H):
    t = "Unpopular opinion: the clasp should be at the front."
    bg = '<div class="abs" style="inset:0;background:linear-gradient(180deg,#F1E4DC,#F6EFE8)"></div>'
    # the photo inside the post: the chain and clasp from the gem-clip plate, cropped below the clips (they end at y ~1110)
    if fmt == "feed":
        return bg + post_card(64, 52, 952, t, fs=48, img=("clips", (300, 1120, 1080, 1900), 868))
    return bg + post_card(64, 300, 952, t, fs=56, img=("clips", (300, 1120, 1080, 1860), 740))   # the card ends above y=1500

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
    ph, m, s = place("clips", W, H, s=1.15, focus=PL["clips"]["ring"], at=(720, 1385))
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
    st = fmt == "story"
    if st:
        ph, m, s = place("clips", W, H, s=1.2, focus=PL["clips"]["ring"], at=(600, 1150))
    else:
        ph, m, s = place("clips", W, H, s=1.12, focus=PL["clips"]["ring"], at=(610, 820))
    (rx, ry), R = m(*PL["clips"]["ring"]), PL["clips"]["r"] * s
    (b0x, b0y), (b1x, b1y) = m(*PL["clips"]["bar"][0]), m(*PL["clips"]["bar"][1])
    cx_, cy_ = m(880, 1075)                      # the lowest gem clip's bottom end
    def lab(x, y, t, fs=44):
        return ('<div class="abs kalam" style="left:%dpx;top:%dpx;color:%s;font-size:%dpx;line-height:1.08;font-weight:700;background:rgba(251,248,243,.9);'
                'padding:8px 16px 6px;border-radius:10px;transform:rotate(-1.5deg)">%s</div>' % (x, y, RED, fs, t))
    title = ('<div class="abs kalam" style="left:64px;top:%dpx;color:%s;font-size:%dpx;font-weight:700;line-height:1.02">Anatomy of a<br>show-off clasp</div>'
             % (300 if st else 56, INK, 82 if st else 70))
    body = ph + fade("top", 640 if st else 330, "251,248,243", .9, 0, .55) + title
    if st:
        body += m_ellipse(rx, ry, R * 1.45, R * 1.18, RED, 8, -6)                    # squashed so it ends above the Shop zone
        body += name_price(64, 492, INK, ns=32, ps=50, row=True)
        body += lab(560, 690, "a gem clip,<br>for scale", 46) + m_arrow(760, 815, 800, 850, cx_ - 6, cy_ - 30, RED, 7, 28)
        body += lab(64, 990, "toggle bar,<br>one line of tiny<br>clear stones", 46) + m_arrow(300, 1178, 380, 1240, b0x - 12, b0y - 22, RED, 7, 28)
        body += lab(730, 1080, "the ring,<br>about 15&nbsp;mm", 48) + m_arrow(800, 1192, 790, 1225, rx + R * 1.0, ry - R * 0.98, RED, 7, 28)
    else:
        body += m_ellipse(rx, ry, R * 1.5, R * 1.42, RED, 8, -8)                     # clear of the ring, gate and nub
        body += lab(48, 470, "toggle bar,<br>one line of tiny<br>clear stones", 40) + m_arrow(250, 620, 300, 700, b0x - 10, b0y - 20, RED, 7, 26)
        body += lab(640, 1010, "the ring, about 15&nbsp;mm", 42) + m_arrow(660, 1012, 650, 960, rx + R * 1.0, ry + R * 1.06, RED, 7, 26)
        body += lab(600, 330, "a gem clip, for scale", 40) + m_arrow(800, 395, 850, 430, cx_ - 4, cy_ - 26, RED, 7, 26)
        body += name_price(64, 1236, INK, ns=32, ps=50, row=True) + logo("ink", 870, 64, 150)
    return body

def checklist(x, y, w, items, fs=46, head=56):
    rows = "".join('<div style="display:flex;align-items:center;gap:18px;margin-top:14px"><div style="position:relative;width:48px;height:46px;flex:none">%s</div>'
                   '<div class="kalam" style="font-size:%dpx;line-height:1.1">%s</div></div>' % (m_check(2, 4, RED, 42, 8), fs, it) for it in items)
    return ('<div class="abs inter" style="left:%dpx;top:%dpx;width:%dpx;padding:38px 44px 36px;background:#FFFDF6;border-radius:30px;color:#151515;'
            'box-shadow:0 18px 40px rgba(0,0,0,.2)"><div style="font-weight:700;font-size:%dpx;letter-spacing:-.02em">Goes with:</div>%s'
            '<div style="margin-top:24px;font-size:32px;color:#4a4a4a">Toggle Link Chain &middot; %s</div></div>' % (x, y, w, head, rows, PRICE))

def x08(fmt, W, H):
    items = ["kurta", "office shirt", "saree blouse", "the Monday after the wedding"]
    if fmt == "feed":
        ph, m, s = place("worn", W, H, focus=PL["worn"]["ring"], at=(540, 900))
        return ph + checklist(560, 40, 470, items, fs=40, head=50)
    ph, m, s = place("worn", W, H)
    return ph + checklist(72, 300, 600, items, fs=48, head=58)

def x09(fmt, W, H):
    # checkerboard: text / photo on the first row, photo / text on the second; the Story's rows run edge to edge
    if fmt == "feed":
        rows = [(0, 675), (675, 675)]
    else:
        rows = [(0, 900), (900, 1020)]
    (y1, h1), (y2, h2) = rows; tw = 540
    def photo_tile(pl, x, y, th, s, at):
        ph, m, _ = place(pl, tw, th, s=s, focus=PL[pl]["ring"], at=at)
        return '<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;overflow:hidden">%s</div>' % (x, y, tw, th, ph)
    st = fmt == "story"
    t1 = ('<div class="abs" style="left:0;top:%dpx;width:%dpx;height:%dpx;background:#F1E4DC;display:flex;flex-direction:column;justify-content:%s;padding:%s 52px 0">'
          '<div class="cgi" style="font-size:%dpx;color:%s">The clasp<br>is the<br>point.</div></div>') % (y1, tw, h1, "flex-start" if st else "center", "420px" if st else "0", 96 if st else 92, INK)
    t2 = ('<div class="abs" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:#1A1614;color:%s;display:flex;flex-direction:column;justify-content:flex-start;padding:%s 52px 0">'
          '<div class="jost" style="font-size:28px;letter-spacing:.14em;margin-bottom:14px">Toggle Link Chain</div><div class="cg" style="font-size:84px;line-height:1">%s</div>'
          '<div class="jost" style="font-size:30px;letter-spacing:.12em;line-height:1.5;margin-top:22px">Gift-boxed<br>Free insured<br>shipping<br>Front or side</div>'
          '<img src="file://%s" style="width:130px;margin-top:30px"></div>') % (tw, y2, tw, h2, IVORY, "110px" if st else "150px", PRICE, os.path.join(BRAND, "logo_white.png"))
    body = (t1 + photo_tile("worn", tw, y1, h1, 1.35, (270, 520 if st else 360)) +
            photo_tile("sage", 0, y2, h2, 1.25, (300, 320 if st else 330)) + t2)
    return body

# X04 (Looks expensive. Isn't.) and X06 (Tap the link.) were cut by the judge: the rose takes over the picture and the
# chain reads as a bracelet; the blue hyperlink imitates a link that does not exist. Their code stays for the record.
ADS = {"X01_kabhi_front": x01, "X02_sticky_note": x02, "X03_unpopular_opinion": x03, "X05_gem_clip": x05,
       "X07_anatomy": x07, "X08_goes_with": x08, "X09_checkerboard": x09, "X10_hook_laga_do": x10}
CUT = {"X04_looks_expensive": x04, "X06_tap_the_link": x06}

def main():
    keys = sys.argv[1:] or list(ADS)
    allads = {**ADS, **CUT}
    os.makedirs(OUT, exist_ok=True); tmp = tempfile.mkdtemp(dir=f"{SPB}/toggle15"); jobs = []
    for k in keys:
        for fmt in ("feed", "story"):
            W, H = SIZE[fmt]
            page = "<!doctype html><html><head><meta charset=utf-8><style>%s</style></head><body>%s</body></html>" % (CSS % dict(f1=F1, f2=F2, w=W, h=H), allads[k](fmt, W, H))
            p = os.path.join(tmp, f"{k}_{fmt}.html"); open(p, "w").write(page)
            jobs.append({"html": p, "out": os.path.join(OUT, f"{k}_{fmt}.jpg"), "w": W, "h": H})
    jp = os.path.join(tmp, "jobs.json"); json.dump(jobs, open(jp, "w"))
    r = subprocess.run(["node", os.path.join(HERE, "shot.cjs"), jp], capture_output=True, text=True)
    print(r.stdout.strip()[-800:], r.stderr.strip()[-800:])

if __name__ == "__main__":
    main()
