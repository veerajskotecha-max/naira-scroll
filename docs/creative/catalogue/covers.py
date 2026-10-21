# Three cover options for the Naira catalogue carousel, each at 1:1 (1080×1080), 4:5 (1080×1350) and 9:16 (1080×1920).
# All photos are the store's own listing photos (no new shoots); every piece shown is in stock.
#   1 "The Wall"         every in-stock piece, on her, in one dense wall; a coral badge; marker circles on favourites
#   2 "Now Showing"      a Bollywood film poster: CHAMAK in gold-tone 3D type, the cast of pieces, a billing block
#   3 "The Naira Times"  a tabloid front page: SHE WORE IT ALL., a lead photo, side stories with prices, an EXTRA! stamp
# Usage: covers.py [wall|poster|times ...]  -> <scratchpad>/cat/out/covers/naira-cover-<name>-<1x1|4x5|9x16>.jpg
# A fourth layout, "2x3" (1080×1620), is the 24 × 36 in stall poster; ../stall/covers_print.py renders it for print and sets
# the print hooks below (RES, UP, SR, QR).
import html, json, math, os, random, subprocess, sys
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cards as C

WORK, OUT = f"{C.SP}/work/covers", f"{C.SP}/out/covers"
FORMATS = {"1x1": (1080, 1080), "4x5": (1080, 1350), "9x16": (1080, 1920), "2x3": (1080, 1620)}
SCREEN = ("1x1", "4x5", "9x16")
MARKER = "#E2412B"
RES = 1.0      # print: crops are cut at RES × their layout size
UP = {}        # print: source photo -> an upscaled copy of it
SR = None      # print: SR(path, rect, size, name) -> path, for crops enlarged more than 1.6×
QR = None      # print: QR(colour, size) -> svg markup of the shop QR code
rows = {r["handle"]: r for r in json.load(open(f"{C.SRC}/products_pick.json"))}
boxes = C.load_boxes()
COUNT = len(rows); LO = min(r["price"] for r in rows.values()); HI = max(r["price"] for r in rows.values())

HEAD = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Velista;src:url("file://%(f)s/Velista.ttf")}
@font-face{font-family:Anton;src:url("file://%(f)s/Anton.ttf")}
@font-face{font-family:Marker;src:url("file://%(f)s/PermanentMarker.ttf")}
@font-face{font-family:OldStd;src:url("file://%(f)s/OldStandardTTwght700.ttf");font-weight:700}
@font-face{font-family:OldStdI;src:url("file://%(f)s/OldStandardTTital1.ttf")}
*{box-sizing:border-box}html,body{margin:0;width:%(w)spx;height:%(h)spx;overflow:hidden}
.a{position:absolute}img{display:block}
.grain{position:absolute;inset:0;pointer-events:none;opacity:%(grain)s;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .5 0 0 0 0 .5 0 0 0 1 0'/></filter><rect width='300' height='300' filter='url(%%23n)'/></svg>")}
</style></head><body>
"""

def head(w, h, grain=.22): return HEAD % dict(f=C.FONTS, w=w, h=h, grain=grain)

def photo(handle, kind, aspect, size, fill=None, ycen=.5, smin=.5, name=None, focus=True, sr=True):
    """A crop of a product's worn/alt/close photo round the piece, cut to `size` and saved for a cover."""
    r = rows[handle]; path = f"{C.SRC}/full/{handle}-{kind}.jpg"; path = UP.get(path, path); W, H = Image.open(path).size
    key = f'{r["n"]}{"a" if kind == "alt" else "w"}'
    b = boxes.get(key) if kind in ("worn", "alt") and r["worn"] else None
    fo = (b["focus"] if focus else b["box"]) if b else [.3, .3, .7, .7]
    rect = C.crop(W, H, fo, aspect, fill or C.FILL.get(r["type"], .6), ycen, smin)
    px = (round(size[0] * RES), round(size[1] * RES)); name = name or f"cov-{handle}-{kind}-{size[0]}x{size[1]}"
    if SR and sr and rect[2] * 1.6 < px[0]: return SR(path, rect, px, name)
    return C.cut(path, rect, px, name)[0]

def scribble(cx, cy, rx, ry, seed, turns=1.16):
    """A hand-drawn marker loop: a little more than one turn, wobbling and spiralling out."""
    rnd = random.Random(seed); n = 64; a0 = rnd.uniform(0, 2 * math.pi); pts = []
    for i in range(int(n * turns) + 1):
        t = a0 + 2 * math.pi * i / n
        k = 1 + .05 * math.sin(3 * t + seed) + rnd.uniform(-.012, .012) + .07 * i / (n * turns)
        pts.append((cx + rx * k * math.cos(t), cy + ry * k * math.sin(t - .08)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)

def arrow(x1, y1, x2, y2, bend=.25):
    """A curved marker arrow from (x1,y1) to (x2,y2) with an open head."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2; dx, dy = x2 - x1, y2 - y1
    cx, cy = mx - dy * bend, my + dx * bend
    ang = math.atan2(y2 - cy, x2 - cx); L = 26
    h1 = (x2 - L * math.cos(ang - .5), y2 - L * math.sin(ang - .5)); h2 = (x2 - L * math.cos(ang + .5), y2 - L * math.sin(ang + .5))
    return f"M{x1:.0f},{y1:.0f} Q{cx:.0f},{cy:.0f} {x2:.0f},{y2:.0f} M{h1[0]:.0f},{h1[1]:.0f} L{x2:.0f},{y2:.0f} L{h2[0]:.0f},{h2[1]:.0f}"

def scallop(cx, cy, r, n=26, depth=.055):
    pts = []
    for i in range(n * 10):
        t = 2 * math.pi * i / (n * 10); rr = r * (1 - depth * (.5 - .5 * math.cos(n * t)))
        pts.append(f"{cx + rr * math.cos(t):.1f},{cy + rr * math.sin(t):.1f}")
    return " ".join(pts)

def tape(x, y, w, h, rot, seed):
    rnd = random.Random(seed); j = lambda: rnd.uniform(-5, 5)
    pts = f"0,{4 + j()} {w},{j()} {w + j()},{h} {w * .5},{h + j()} 0,{h - 3 + j()}"
    return (f'<svg class="a" style="left:{x}px;top:{y}px;overflow:visible;transform:rotate({rot}deg)" width="{w}" height="{h}">'
            f'<polygon points="{pts}" fill="rgba(255,248,236,.86)" style="filter:drop-shadow(0 3px 6px rgba(0,0,0,.18))"/></svg>')

def qr_card(x, y, size, bg="#FFF8F5", fg="#1A1614", pad=12, ring=None):
    """The shop QR on a small card (print layouts only)."""
    b = f"box-shadow:0 0 0 2px {ring};" if ring else "box-shadow:0 10px 26px rgba(0,0,0,.28);"
    return f'<div class="a" style="left:{x}px;top:{y}px;padding:{pad}px;background:{bg};{b}">{QR(fg, size)}</div>'

# ---------------------------------------------------------------- 1 The Wall
WALL_NOTES = [("mine.", -8), ("obsessed", 6), ("her gift", -5), ("shaadi ✓", 7), ("need", -6), ("both colours", 5)]

def wall(fmt):
    w, h = FORMATS[fmt]
    cols, rws = {"1x1": (9, 9), "4x5": (8, 10), "9x16": (6, 11), "2x3": (7, 11)}[fmt]
    gap = 4; tw = (w - gap * (cols + 1)) / cols; th = tw
    order = sorted((r for r in rows.values() if r["worn"]), key=lambda r: r["n"])
    cats = {}
    for r in order: cats.setdefault(r["type"], []).append(r)
    mix = []                                    # deal the categories round-robin so no two neighbours match
    while any(cats.values()):
        for t in ("Earrings", "Bracelet", "Ring", "Necklace"):
            if cats.get(t): mix.append(cats[t].pop(0))
    rnd = random.Random(7); body = mix[:cols * rws]
    rnd.shuffle(body)
    x = head(w, h, .16) + f'<div class="a" style="inset:0;background:#FFF8F5"></div>'
    for i, r in enumerate(body):
        c, rr = i % cols, i // cols
        p = photo(r["handle"], "worn", 1, (300, 300) if fmt != "2x3" else (150, 150), ycen=.5, name=f"tile-{r['handle']}", sr=False)
        x += f'<img class="a" src="file://{p}" style="left:{gap + c * (tw + gap):.1f}px;top:{gap + rr * (th + gap):.1f}px;width:{tw:.1f}px;height:{th:.1f}px">'
    x += f'<div class="a" style="inset:0;background:radial-gradient(ellipse at 50% 52%,rgba(26,22,20,.42),rgba(26,22,20,.12) 46%,rgba(26,22,20,0) 70%)"></div>'
    # badge
    cx, cy, R = w / 2, {"1x1": 560, "4x5": 690, "9x16": 960, "2x3": 790}[fmt], {"1x1": 300, "4x5": 318, "9x16": 350, "2x3": 330}[fmt]
    top = {"1x1": 34, "4x5": 44, "9x16": 250, "2x3": 48}[fmt]
    x += (f'<svg class="a" style="left:0;top:0;overflow:visible" width="{w}" height="{h}"><g transform="rotate(-7 {cx} {cy})" '
          f'style="filter:drop-shadow(0 26px 40px rgba(20,10,5,.45))"><polygon points="{scallop(cx, cy, R)}" fill="#F0A08F"/>'
          f'<circle cx="{cx}" cy="{cy}" r="{R - 30}" fill="none" stroke="#1A1614" stroke-width="2" stroke-dasharray="2 9" stroke-linecap="round"/></g></svg>')
    s = R / 300
    x += (f'<div class="a" style="left:{cx - R}px;top:{cy - R}px;width:{2 * R}px;height:{2 * R}px;transform:rotate(-7deg);display:flex;'
          f'flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#1A1614">'
          f'<div style="font:700 {25 * s:.0f}px/1 Jost;letter-spacing:.42em;margin-left:.42em">THE WHOLE</div>'
          f'<div style="font:{90 * s:.0f}px/1 Velista;letter-spacing:-.01em;margin:{14 * s:.0f}px 0 {8 * s:.0f}px">CATALOGUE</div>'
          f'<div style="font:500 italic {44 * s:.0f}px/1.05 CGI">worn by her, ready for you.</div>'
          f'<div style="font:600 {26 * s:.0f}px/1 Jost;letter-spacing:.2em;margin-top:{22 * s:.0f}px">{COUNT} PIECES · ₹{LO:,}–₹{HI:,}</div>'
          f'<div style="font:700 {21 * s:.0f}px/1 Jost;letter-spacing:.3em;margin-top:{20 * s:.0f}px;padding:{13 * s:.0f}px {24 * s:.0f}px;'
          f'background:#1A1614;color:#FFF8F5;border-radius:999px">{"SCAN TO SHOP" if fmt == "2x3" else "SHOP NOW →"}</div></div>')
    # masthead on tape
    x += tape(w / 2 - 300, top - 16, 600, 128, -2.5, 3)
    x += f'<img class="a" src="file://{C.BRAND}/logo_ink.png" style="left:{w / 2 - 230}px;top:{top + 8}px;width:460px;transform:rotate(-2.5deg)">'
    # marker loops on a few tiles, away from the badge and the masthead
    picks = {"1x1": [(1, 7), (6, 0), (7, 7), (2, 1)], "4x5": [(2, 6), (7, 0), (8, 7), (2, 1), (5, 7)],
             "9x16": [(2, 5), (7, 0), (7, 5), (3, 0), (5, 5)], "2x3": [(2, 6), (7, 0), (7, 6), (2, 0), (5, 6)]}[fmt]
    svg = f'<svg class="a" style="left:0;top:0;overflow:visible" width="{w}" height="{h}"><g fill="none" stroke="{MARKER}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" style="filter:drop-shadow(0 2px 2px rgba(0,0,0,.25))">'
    notes = ""
    for k, (rr, c) in enumerate(picks):
        tx, ty = gap + c * (tw + gap) + tw / 2, gap + rr * (th + gap) + th / 2
        svg += f'<path d="{scribble(tx, ty, tw * .62, th * .6, k + 2)}"/>'
        word, rot = WALL_NOTES[k % len(WALL_NOTES)]
        def spot(sign):
            ny = ty + sign * th * 1.08; nx = min(max(tx, 130), w - 130)
            return nx, ny, math.hypot(nx - cx, ny - cy) > R + 70 and not (top - 20 < ny < top + 150) and 30 < ny < h - 40
        nx, ny, ok = spot(1 if ty > cy else -1)
        if not ok: nx, ny, ok = spot(-1 if ty > cy else 1)
        sgn = 1 if ny > ty else -1
        svg += f'<path d="{arrow(nx + (40 if nx < tx else -40 if nx > tx else 30), ny - sgn * 26, tx + (tw * .3 if nx >= tx else -tw * .3), ty + sgn * th * .5)}" stroke-width="6"/>'
        notes += (f'<div class="a" style="left:{nx - 130:.0f}px;top:{ny - 20:.0f}px;width:260px;text-align:center;'
                  f'font:38px/1 Marker;color:{MARKER};transform:rotate({rot}deg);text-shadow:0 2px 0 #FFF8F5,0 0 10px rgba(255,248,245,.9)">{html.escape(word)}</div>')
    x += svg + "</g></svg>" + notes
    if fmt == "2x3":
        x += (f'<div class="a" style="left:0;right:0;top:1500px;height:120px;background:#1A1614;color:#FFF8F5;display:flex;align-items:center;'
              f'padding-left:70px;font:600 28px/1 Jost;letter-spacing:.3em">SCAN TO SHOP ALL {COUNT} &nbsp;→</div>')
        x += qr_card(856, 1392, 160)
    elif fmt != "1x1":
        by = {"4x5": 1262, "9x16": 1590}[fmt]
        x += (f'<div class="a" style="left:0;right:0;top:{by}px;height:72px;background:#1A1614;color:#FFF8F5;display:flex;align-items:center;'
              f'justify-content:center;font:600 24px/1 Jost;letter-spacing:.32em">ALL {COUNT} IN STOCK · TAP TO SHOP</div>')
    if fmt != "2x3": x += '<div class="grain"></div>'
    return x

# ---------------------------------------------------------------- 2 Now Showing
CAST = ["kiss-knot-bangle", "woven-gold-hoops", "lilac-papillon-ring", "prism-riviere-bracelet"]
CAST_NAMES = {"kiss-knot-bangle": "Kiss Knot", "woven-gold-hoops": "Woven Hoops", "lilac-papillon-ring": "Lilac Papillon",
              "prism-riviere-bracelet": "Prism Rivière"}

def gold_title(text, size, x, y, w):
    layers = "".join(f"{i}px {i}px 0 #4A2A0C" for i in range(1, 11)) + ",14px 16px 22px rgba(0,0,0,.6)"
    base = f"position:absolute;left:{x}px;top:{y}px;width:{w}px;text-align:center;font:{size}px/1 Velista;letter-spacing:.02em;white-space:nowrap"
    return (f'<div style="{base};color:#5C3511;text-shadow:{layers}">{text}</div>'
            f'<div style="{base};background:linear-gradient(176deg,#FFF6D6 8%,#F6CF7A 30%,#C98A32 52%,#FFE7A1 64%,#A8691F 86%);'
            f'-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 18px rgba(255,196,110,.35))">{text}</div>')

def sparkle(x, y, s, o=1):
    return (f'<svg class="a" style="left:{x - s}px;top:{y - s}px;opacity:{o}" width="{2 * s}" height="{2 * s}" viewBox="-50 -50 100 100">'
            f'<path d="M0,-50 C6,-8 8,-6 50,0 C8,6 6,8 0,50 C-6,8 -8,6 -50,0 C-8,-6 -6,-8 0,-50Z" fill="#FFF4D2" '
            f'style="filter:drop-shadow(0 0 8px rgba(255,214,140,.95))"/></svg>')

def poster(fmt):
    w, h = FORMATS[fmt]
    ph_h = {"1x1": 1080, "4x5": 1350, "9x16": 1500, "2x3": 1340}[fmt]
    p = photo("verdant-drop-earrings", "worn", w / ph_h, (w, ph_h), fill=.18, ycen=.32, smin=.9, name=f"poster-{fmt}")
    x = head(w, h, .3) + f'<div class="a" style="inset:0;background:#120C08"></div>'
    x += f'<img class="a" src="file://{p}" style="left:0;top:0;width:{w}px;height:{ph_h}px;filter:saturate(1.08) contrast(1.06)">'
    x += (f'<div class="a" style="left:0;top:0;width:{w}px;height:{ph_h}px;background:radial-gradient(ellipse 80% 70% at 60% 30%,rgba(0,0,0,0) 40%,rgba(12,7,4,.55) 100%),'
          f'linear-gradient(rgba(12,7,4,.55),rgba(12,7,4,0) 22%,rgba(12,7,4,0) 40%,rgba(12,7,4,.82) 68%,#120C08 100%)"></div>')
    x += f'<div class="a" style="left:0;top:0;width:{w}px;height:{ph_h}px;background:linear-gradient(115deg,rgba(255,150,60,.28),rgba(255,150,60,0) 35%);mix-blend-mode:screen"></div>'
    T = {"1x1": 40, "4x5": 52, "9x16": 250, "2x3": 60}[fmt]
    x += f'<img class="a" src="file://{C.BRAND}/logo_white.png" style="left:{w / 2 - 120}px;top:{T}px;width:240px;opacity:.95">'
    x += (f'<div class="a" style="left:0;right:0;top:{T + 66}px;text-align:center;font:600 19px/1 Jost;letter-spacing:.62em;color:#F4E3C8;'
          f'margin-left:.31em">P R E S E N T S</div>')
    # certificate
    x += (f'<div class="a" style="left:{w - 168}px;top:{T - 6}px;width:118px;height:118px;border:3px solid #F4E3C8;border-radius:50%;color:#F4E3C8;'
          f'display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(8deg)">'
          f'<div style="font:52px/1 Anton">U</div><div style="font:600 10px/1.25 Jost;letter-spacing:.16em;text-align:center">UNIVERSALLY<br>ADORED</div></div>')
    ty = {"1x1": 560, "4x5": 612, "9x16": 1000, "2x3": 690}[fmt]; ts = {"1x1": 232, "4x5": 246, "9x16": 262, "2x3": 252}[fmt]
    x += gold_title("CHAMAK", ts, 0, ty, w)
    for (sx, sy, ss) in [(.2, .1, 42), (.79, .02, 34), (.62, .74, 26)]:
        x += sparkle(w * sx, ty + ts * sy, ss)
    tg = ty + ts + {"1x1": 6, "4x5": 14, "9x16": 18, "2x3": 16}[fmt]
    x += (f'<div class="a" style="left:0;right:0;top:{tg}px;text-align:center;font:500 italic {46 if fmt == "1x1" else 52}px/1 CGI;color:#FFF1DD">'
          f'Ek catalogue. {COUNT} kahaaniyan.</div>')
    y = tg + (70 if fmt == "1x1" else 92)
    if fmt != "1x1":
        cs = {"4x5": 118, "2x3": 128}.get(fmt, 150); gapc = 70 if fmt in ("4x5", "2x3") else 60; total = len(CAST) * cs + (len(CAST) - 1) * gapc; x0 = (w - total) / 2
        for i, hnd in enumerate(CAST):
            cp = photo(hnd, "close", 1, (2 * cs, 2 * cs), fill=.62, name=f"cast-{hnd}")
            cx = x0 + i * (cs + gapc)
            x += (f'<div class="a" style="left:{cx - 40}px;top:{y}px;width:{cs + 80}px;text-align:center;display:flex;flex-direction:column;align-items:center">'
                  f'<img src="file://{cp}" style="width:{cs}px;height:{cs}px;border-radius:50%;border:4px solid #E7C27A;box-shadow:0 10px 26px rgba(0,0,0,.5)">'
                  f'<div style="font:600 15px/1.2 Jost;letter-spacing:.16em;color:#F4E3C8;margin-top:12px;text-transform:uppercase">{CAST_NAMES[hnd]}</div>'
                  f'<div style="font:500 14px/1 Jost;letter-spacing:.14em;color:#E7C27A;margin-top:6px">₹{rows[hnd]["price"]:,}</div></div>')
        y += cs + 66
    bill = ("NAIRA PETITE <i>presents</i> A SHAADI SEASON PRODUCTION &nbsp; STARRING KISS KNOT BANGLE · WOVEN GOLD HOOPS · BOLD NOCTURNE CHAIN · "
            f"LILAC PAPILLON RING · PRISM RIVIÈRE BRACELET · VERDANT DROP EARRINGS &nbsp; AND {COUNT - 6} MORE &nbsp; "
            "MUSIC BY THE JHUMKAS &nbsp; COSTUMES BY YOUR MOOD &nbsp; DIRECTED BY YOU")
    x += (f'<div class="a" style="left:70px;right:70px;top:{y}px;text-align:center;font:{19 if fmt == "1x1" else 21}px/1.25 Anton;letter-spacing:.06em;'
          f'color:#CDB79A;transform:scaleY(1.18);transform-origin:top">{bill}</div>')
    by = y + {"1x1": 92, "4x5": 104, "9x16": 110, "2x3": 104}[fmt]
    x += (f'<div class="a" style="left:0;right:0;top:{by}px;text-align:center"><span style="display:inline-block;padding:14px 30px 13px;'
          f'background:linear-gradient(90deg,#B57A2A,#F2C36B,#B57A2A);color:#1A0F07;font:700 22px/1 Jost;letter-spacing:.3em">'
          f'NOW SHOWING · ₹{LO:,} ONWARDS · NAIRAFLORE.COM</span></div>')
    if fmt == "2x3":
        qy = by + 82
        x += qr_card(w / 2 - 190, qy, 128, bg="#F7EBD3", fg="#1A0F07", pad=10, ring="#E7C27A")
        x += (f'<div class="a" style="left:{w / 2 - 20}px;top:{qy + 30}px;color:#F4E3C8"><div style="font:600 18px/1 Jost;letter-spacing:.36em;color:#E7C27A">SCAN TO SHOP</div>'
              f'<div style="font:500 italic 40px/1 CGI;margin-top:14px">every piece, from ₹{LO:,}</div></div>')
    else: x += '<div class="grain"></div>'
    return x

# ---------------------------------------------------------------- 3 The Naira Times
SIDE = [("woven-gold-hoops", "HOOPS SIGHTED AT CHAI STALL", "Witnesses report a braid of gold tone and zero regrets."),
        ("lilac-papillon-ring", "BUTTERFLY LANDS ON RING FINGER", "Refuses to leave. Lilac cubic zirconia, gold tone."),
        ("pearl-legacy-necklace", "PEARLS REFUSE TO RETIRE", "Baroque, unbothered, back for another season.")]

def times(fmt):
    w, h = FORMATS[fmt]; ink = "#16110E"; red = "#C8321F"
    T = {"1x1": 28, "4x5": 40, "9x16": 240, "2x3": 44}[fmt]
    x = head(w, h, .35) + f'<div class="a" style="inset:0;background:#F2EADF"></div>'
    x += f'<div class="a" style="inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(255,252,244,.6),rgba(201,186,160,.35))"></div>'
    # masthead: THE [NAIRA] TIMES
    x += (f'<div class="a" style="left:0;right:0;top:{T}px;display:flex;align-items:center;justify-content:center;gap:22px;color:{ink}">'
          f'<span style="font:700 76px/1 OldStd">THE</span><img src="file://{C.BRAND}/logo_ink.png" style="width:400px">'
          f'<span style="font:700 76px/1 OldStd">TIMES</span></div>')
    y = T + 104
    x += (f'<div class="a" style="left:40px;right:40px;top:{y}px;border-top:3px solid {ink};border-bottom:1px solid {ink};padding:9px 0 8px;'
          f'display:flex;justify-content:space-between;font:600 15px/1 Jost;letter-spacing:.14em;color:{ink}">'
          f'<span>{"NASHIK EDITION · FASHION MANTRA" if fmt == "2x3" else "TUESDAY, 20 OCTOBER 2026"}</span><span style="font:italic 19px/1 OldStdI;letter-spacing:.02em">“All the jewellery that’s fit to wear”</span>'
          f'<span>₹{LO:,} ONWARDS</span></div>')
    y += 48
    hs = {"1x1": 150, "4x5": 152, "9x16": 214, "2x3": 152}[fmt]
    x += (f'<div class="a" style="left:30px;right:30px;top:{y}px;text-align:center;font:{hs}px/.92 Anton;color:{ink};letter-spacing:.005em;'
          f'transform:scaleY(1.04)">{"SHE WORE<br>IT ALL." if fmt == "9x16" else "SHE WORE IT ALL."}</div>')
    y += round(hs * .98) * (2 if fmt == "9x16" else 1) + 10
    x += (f'<div class="a" style="left:60px;right:60px;top:{y}px;text-align:center;font:500 italic 33px/1.15 CGI;color:{ink}">'
          f'{COUNT} pieces. One saffron camisole. Zero repeats. The whole catalogue, inside.</div>')
    y += 100 if fmt == "9x16" else 62
    x += f'<div class="a" style="left:40px;right:40px;top:{y}px;border-top:1px solid {ink}"></div>'
    y += 18
    bottom = {"1x1": 1010, "4x5": 1266, "9x16": 1632, "2x3": 1552}[fmt]
    if fmt == "9x16":
        lead_w, lead_h = 1000, 400
    else:
        lead_w, lead_h = 600, bottom - y - 70
    lp = photo("marquise-drop-choker", "worn", lead_w / lead_h, (lead_w, lead_h), fill=.6, ycen=.5, smin=.7, name=f"times-lead-{fmt}", focus=False)
    x += f'<img class="a" src="file://{lp}" style="left:40px;top:{y}px;width:{lead_w}px;height:{lead_h}px;filter:contrast(1.04) saturate(.96)">'
    cap_y = y + lead_h + 8
    x += (f'<div class="a" style="left:40px;width:{lead_w}px;top:{cap_y}px;font:600 15px/1.3 Jost;color:{ink}"><b style="letter-spacing:.12em">SPOTTED:</b> '
          f'<span style="font:italic 19px/1.2 OldStdI">the Marquise Drop Choker, ₹{rows["marquise-drop-choker"]["price"]:,}, refusing to be subtle.</span></div>')
    # stamp
    sx, sy = 40 + lead_w - 96, y + 26
    x += (f'<svg class="a" style="left:{sx - 120}px;top:{sy - 30}px;overflow:visible" width="240" height="240"><g transform="rotate(14 120 120)">'
          f'<polygon points="{scallop(120, 120, 118, 18, .16)}" fill="{red}" style="filter:drop-shadow(0 8px 14px rgba(0,0,0,.3))"/></g></svg>'
          f'<div class="a" style="left:{sx - 120}px;top:{sy - 30}px;width:240px;height:240px;display:flex;flex-direction:column;align-items:center;'
          f'justify-content:center;color:#FFF4E6;transform:rotate(14deg);text-align:center"><div style="font:58px/1 Anton">EXTRA!</div>'
          f'<div style="font:700 16px/1.2 Jost;letter-spacing:.2em;margin-top:6px">SHOP THE<br>ISSUE</div></div>')
    # side stories
    if fmt == "9x16":
        sw = 310; sy0 = cap_y + 44
        for i, (hnd, hl, dek) in enumerate(SIDE):
            sxp = 40 + i * (sw + 35)
            sp = photo(hnd, "worn", 1, (sw, sw), ycen=.5, name=f"times-side-{hnd}")
            x += (f'<div class="a" style="left:{sxp}px;top:{sy0}px;width:{sw}px;height:{sw}px"><img src="file://{sp}" style="width:{sw}px;height:{sw}px">'
                  f'<div class="a" style="left:0;right:0;bottom:0;height:150px;background:linear-gradient(rgba(10,6,4,0),rgba(10,6,4,.8))"></div>'
                  f'<div class="a" style="left:14px;right:14px;bottom:14px;font:27px/1.02 Anton;color:#FFF4E6">{hl}</div>'
                  f'<div class="a" style="left:12px;top:12px;font:700 17px/1 Jost;letter-spacing:.12em;padding:9px 12px 8px;background:{red};color:#FFF4E6">₹{rows[hnd]["price"]:,}</div></div>')
    else:
        cx0 = 40 + lead_w + 34; cw = w - 40 - cx0; ph = {"1x1": 150, "4x5": 196, "2x3": 196}[fmt]; step = (bottom - y - 20) / (4 if fmt == "2x3" else 3)
        x += f'<div class="a" style="left:{cx0 - 18}px;top:{y}px;height:{bottom - y - 30}px;border-left:1px solid {ink}"></div>'
        for i, (hnd, hl, dek) in enumerate(SIDE):
            yy = y + i * step
            sp = photo(hnd, "worn", 1, (ph, ph), ycen=.5, name=f"times-side-{hnd}-{ph}")
            x += (f'<div class="a" style="left:{cx0}px;top:{yy:.0f}px;width:{cw}px;color:{ink};display:flex;gap:14px">'
                  f'<img src="file://{sp}" style="width:{ph}px;height:{ph}px;flex:none">'
                  f'<div><div style="font:{25 if fmt == "1x1" else 28}px/1.02 Anton">{hl}</div>'
                  f'<div style="font:italic 16px/1.22 OldStdI;margin-top:6px">{dek}</div>'
                  f'<div style="font:700 15px/1 Jost;letter-spacing:.14em;margin-top:8px;color:{red}">₹{rows[hnd]["price"]:,}</div></div></div>')
    if fmt == "2x3":
        qy = y + 3 * step
        x += qr_card(cx0, qy, 170, bg="#FFFDF7", fg=ink, pad=10, ring=ink)
        x += (f'<div class="a" style="left:{cx0}px;top:{qy + 206}px;width:{cw}px;font:22px/1.05 Anton;color:{ink}">SCAN TO SHOP THE ISSUE</div>')
    # ticker
    x += (f'<div class="a" style="left:0;right:0;top:{bottom}px;height:{68 if fmt == "2x3" else 58}px;background:{red};color:#FFF4E6;display:flex;align-items:center;'
          f'white-space:nowrap;overflow:hidden;font:27px/1 Anton;letter-spacing:.05em">'
          f'<span style="background:{ink};padding:16px 20px 15px;margin-right:18px">BREAKING</span>'
          f'{"NAIRA IS AT FASHION MANTRA, EMERALD PARK · FROM ₹" + format(LO, ",") if fmt == "2x3" else "ALL " + str(COUNT) + " PIECES IN STOCK · CUBIC ZIRCONIA · FROM ₹" + format(LO, ",")}</div>')
    if fmt != "2x3": x += '<div class="grain"></div>'
    return x

BUILDERS = {"wall": wall, "poster": poster, "times": times}

def main(names):
    os.makedirs(WORK, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    C.WORK = WORK; jobs = []
    for n in names:
        for fmt in SCREEN:
            w, h = FORMATS[fmt]; k = f"naira-cover-{n}-{fmt}"
            open(f"{WORK}/{k}.html", "w").write(BUILDERS[n](fmt) + "</body></html>"); jobs.append(f"{k}:{w}:{h}")
    env = dict(os.environ, NODE_PATH="/opt/node-tools/node_modules")
    subprocess.run(["node", f"{C.HERE}/render.cjs", WORK, *jobs], check=True, env=env)
    for j in jobs:
        k = j.split(":")[0]; os.replace(f"{WORK}/{k}.jpg", f"{OUT}/{k}.jpg")
    print(len(jobs), "covers ->", OUT)

if __name__ == "__main__":
    main(sys.argv[1:] or list(BUILDERS))
