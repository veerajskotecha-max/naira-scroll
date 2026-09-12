#!/usr/bin/env python3
"""
NAIRA  ·  paid-social studio

The previous build ran one layout across 38 creatives - image, eyebrow, display line top-left,
wordmark bottom-left - and no amount of re-ragging fixes a set that is one design repeated.
This one is a library of ARCHITECTURES. Every creative is a different construction: a specimen
sheet, a colour band, a margin column, a diptych, an arch, a ticker, a price card, a poster.

What stays constant is the brand, not the layout:
  · Velista 400 display, Jost 300 support, sentence case, tracking never positive
  · Cream #FFF8F5 / Ink #1A1614 / Marigold #E8973A / Sage #99B4AF / Coral #FFBDA8
  · 64px (6%) side-safe, wordmark once per creative, contrast >= 4.5:1 on real pixels
  · no glow, no stroke, no scrim boxes, no default drop shadows, no fabricated scarcity

Rupee: neither Velista nor Jost carries U+20B9, so prices name 'DejaVu Sans' as the fallback for
that one glyph and are set at support size where the weight difference is not readable. The giant
numeral sets the mark at 0.30em, which is how currency marks are set beside display figures anyway.
"""
import base64, json, pathlib, sys
import colorsys
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("/tmp/claude-0/-home-user-naira-scroll/3afe135e-ba9d-5fe5-a4de-8088e2e02a7f/scratchpad")
FONTS = ROOT / "fonts"
W, H = 1080, 1350
SCALE = 4 / 3
GUT = 6.0                      # % - Reels side-safe
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CREAM, INK = "#FFF8F5", "#1A1614"
MARIGOLD, MARIGOLD_DEEP = "#E8973A", "#8F4E0E"
SAGE, CORAL = "#99B4AF", "#FFBDA8"
PRICE_STACK = "'JostF','DejaVu Sans',sans-serif"

TMP = ROOT / "_crops"
TMP.mkdir(exist_ok=True)
_b64 = {}


def subcrop(src, rect, tag):
    """Cut a region out of a plate. object-position can only slide a cover crop; when a cell must
    isolate one detail the pixels have to be cut."""
    im = Image.open(src).convert("RGB")
    x0, y0, x1, y1 = rect
    c = im.crop((int(x0 * im.width), int(y0 * im.height), int(x1 * im.width), int(y1 * im.height)))
    p = TMP / f"{tag}.png"
    c.save(p)
    return p


def b64(p):
    p = str(p)
    if p not in _b64:
        _b64[p] = base64.b64encode(pathlib.Path(p).read_bytes()).decode()
    return _b64[p]


def fonts():
    return (f"@font-face{{font-family:'Velista';src:url(data:font/ttf;base64,{b64(FONTS/'Velista-400.ttf')})"
            " format('truetype');font-weight:400;font-display:block}"
            f"@font-face{{font-family:'JostF';src:url(data:font/ttf;base64,{b64(FONTS/'jost-full-1.ttf')})"
            " format('truetype');font-weight:300;font-display:block}")


BASE = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
/* grayscale AA. Chromium's default subpixel rendering fringes every glyph edge orange and blue;
   those fringes are chroma detail, and Meta's 4:2:0 encode halves the chroma resolution, so they
   come back as coloured mush on the thinnest strokes of a high-contrast serif. */
html{{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{CREAM}}}
.canvas{{position:relative;width:{W}px;height:{H}px;overflow:hidden}}
img.h{{position:absolute;width:100%;height:100%;object-fit:cover;display:block}}
.v{{font-family:'Velista',Georgia,serif;font-weight:400;letter-spacing:-.012em;line-height:1.04;
   white-space:nowrap}}
.j{{font-family:'JostF',sans-serif;font-weight:300;letter-spacing:.14em;text-transform:uppercase}}
.jb{{font-family:'JostF',sans-serif;font-weight:300;letter-spacing:.02em}}
.pr{{font-family:{PRICE_STACK};font-weight:300}}
.logo{{position:absolute;width:8%}}
.ink{{filter:brightness(0)}}
.crm{{filter:brightness(0) invert(1)}}
.rule{{background:currentColor;opacity:.8}}
"""


HIDE_TYPE = False


def shell(css, body):
    # QA renders the same page twice, once with every mark hidden, and diffs. That gives the exact
    # glyph pixels and the exact ground behind them, which is the only honest way to measure
    # contrast across twenty-one different constructions.
    # visibility:hidden would also remove a chip's own background or a ticker strip's ink, and the
    # diff would then read cream-on-cream where the live render has cream-on-ink. Only the glyphs
    # come out; every ground, rule and border stays put in both passes.
    hide = (".v,.j,.jb,.pr,.lb,.lv,.dc,.icap,.cap{color:transparent!important;"
            "-webkit-text-fill-color:transparent!important}"
            ".logo{opacity:0!important}.big{visibility:hidden!important}" if HIDE_TYPE else "")
    return (f"<!doctype html><html><head><meta charset=utf-8><style>{fonts()}{BASE}{css}{hide}</style>"
            f"</head><body><div class=canvas>{body}</div></body></html>")


def hero(src, pos="50% 50%", cls="", style=""):
    return f"<img class='h {cls}' style='object-position:{pos};{style}' src='data:image/png;base64,{b64(src)}'>"


def logo(mode="ink", left=GUT, bottom=5.0, w=8.0, extra=""):
    cls = "ink" if mode == "ink" else "crm"
    return (f"<img class='logo {cls}' style='left:{left}%;bottom:{bottom}%;width:{w}%;{extra}' "
            f"src='data:image/png;base64,{b64(ROOT/'logo.png')}'>")


# ---------------------------------------------------------------- colour from the photograph ---
def _cover(path):
    im = Image.open(path).convert("RGB")
    s = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2,
                    (im.width - W) // 2 + W, (im.height - H) // 2 + H))


def tone(im, box, v=0.30, smax=0.42, smin=0.16, mul=3.2):
    """Deepen the frame's own ground into a panel colour that still belongs to the photograph."""
    x, y, w, h = box
    c = im.crop((int(x * W), int(y * H), int((x + w) * W), int((y + h) * H)))
    r, g, b = np.asarray(c.resize((16, 16)), dtype=float).reshape(-1, 3).mean(0) / 255.0
    hh, s, _ = colorsys.rgb_to_hsv(r, g, b)
    r, g, b = colorsys.hsv_to_rgb(hh, min(smax, max(smin, s * mul)), v)
    return f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"


def lift(im, box, v=0.955, s=0.075):
    """The pale twin of tone(): the frame's hue held at near-paper value, for grounds and trays."""
    x, y, w, h = box
    c = im.crop((int(x * W), int(y * H), int((x + w) * W), int((y + h) * H)))
    r, g, b = np.asarray(c.resize((16, 16)), dtype=float).reshape(-1, 3).mean(0) / 255.0
    hh, s0, _ = colorsys.rgb_to_hsv(r, g, b)
    r, g, b = colorsys.hsv_to_rgb(hh, min(s, max(0.03, s0 * 0.55)), v)
    return f"rgb({int(r*255)},{int(g*255)},{int(b*255)})"


# ---------------------------------------------------------------------------- small components --
def vlines(lines, size, colour, lh=1.04, cls=""):
    return "".join(f"<div class='v {cls}' style='font-size:{size}px;line-height:{lh};color:{colour}'>{l}</div>"
                   for l in lines)


def eyebrow(text, colour, size=17, mb=0):
    return (f"<div class='j' style='font-size:{size}px;color:{colour};margin-bottom:{mb}px'>{text}</div>")


def ticks(items, colour, size=20, gap=26, dot=MARIGOLD_DEEP):
    cells = "".join(
        f"<span style='display:inline-flex;align-items:center;gap:9px'>"
        f"<i style='width:5px;height:5px;border-radius:50%;background:{dot};display:inline-block'></i>{t}</span>"
        for t in items)
    return (f"<div class='j' style='font-size:{size}px;color:{colour};display:flex;flex-wrap:wrap;"
            f"gap:{gap}px;letter-spacing:.10em'>{cells}</div>")


def price(txt, size, colour, weight=""):
    return f"<span class='pr' style='font-size:{size}px;color:{colour};letter-spacing:.01em;{weight}'>{txt}</span>"


def cta(text, fg=CREAM, bg=INK, size=20):
    return (f"<div class='j' style='display:inline-block;font-size:{size}px;color:{fg};background:{bg};"
            f"padding:15px 30px 13px;letter-spacing:.16em'>{text}</div>")


# ====================================================================== ARCHITECTURES ============
L = {}


def arch_(name):
    def d(f):
        L[name] = f
        return f
    return d


# 1 --------------------------------------------------------------------------------- SPECIMEN --
@arch_("specimen")
def _specimen(s, im, src):
    """An annotation sheet. Hairline leaders run from labels in the empty field to the piece."""
    rows = ""
    for lab, lx, ly, ln in s["labels"]:
        rows += (f"<div class='lab' style='left:{lx}%;top:{ly}%'><b></b>"
                 f"<i style='width:{ln}px'></i><span class='j'>{lab}</span></div>")
    css = f"""
    .lab{{position:absolute;display:flex;align-items:center;color:{INK}}}
    .lab .j{{font-size:{s.get('labSize',19)}px;letter-spacing:.16em;white-space:nowrap;padding-left:14px}}
    .lab i{{height:1px;background:{INK};opacity:.50;display:block}}
    .lab b{{flex:none}}
    .lab b{{width:5px;height:5px;border-radius:50%;background:{s.get('dot',INK)};display:block}}
    .foot{{position:absolute;left:{s['footx']}%;{s.get('footEdge','bottom')}:{s['footy']}%;width:{s.get('footw',60)}%}}
    .frm{{position:absolute;left:{GUT}%;right:{GUT}%;top:4.4%;bottom:4.4%;border:1px solid rgba(26,22,20,.34)}}
    .idx{{position:absolute;top:6.6%;left:{GUT+2.4}%;right:{GUT+2.4}%;font-size:19px;letter-spacing:.24em;
      color:{INK};display:flex;justify-content:space-between}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + "<div class=frm></div>"
            + f"<div class='j idx'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>" + rows
            + f"<div class=foot>{vlines(s['lines'], s['size'], INK)}</div>"
            + logo("ink", GUT + 2.4, 7.0, 7.0))
    return shell(css, body)


# 2 ------------------------------------------------------------------------------ ANGLED FIELD --
@arch_("angled")
def _angled(s, im, src):
    """A flat field cut on the photograph's own diagonal - the graphic continues the picture."""
    g = s.get("ground") or lift(im, (0.05, 0.75, 0.3, 0.2))
    css = f"""
    .wedge{{position:absolute;inset:0;background:{g};clip-path:polygon({s['poly']})}}
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;width:{s.get('tw',70)}%}}
    """
    body = (hero(src, s.get("pos", "50% 50%")) + "<div class=wedge></div>"
            + f"<div class=tx>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 22)}"
            f"{vlines(s['lines'], s['size'], INK)}"
            f"<div style='margin-top:26px'>{ticks(s['ticks'], 'rgba(26,22,20,.66)', 18, 24)}</div></div>"
            + logo("ink", GUT, 5.4, 7.6))
    return shell(css, body)


# 3 -------------------------------------------------------------------------------- DEEP BAND ---
@arch_("band")
def _band(s, im, src):
    """A deep band anchored to a dark the photograph already contains; the type reverses out."""
    t = s.get("tone") or tone(im, tuple(s["toneBox"]), v=s.get("v", 0.26))
    top = s["top"]
    css = f"""
    .bd{{position:absolute;left:0;right:0;top:{top}%;bottom:0;background:{t};
      display:flex;flex-direction:column;justify-content:center;padding:0 {GUT}%}}
    .bd .edge{{position:absolute;left:0;right:0;top:0;height:1px;background:rgba(255,248,245,.34)}}
    .meta{{position:absolute;left:{GUT}%;right:{GUT}%;top:{top-6.2}%;display:flex;
      justify-content:space-between;align-items:flex-end;color:{INK};font-size:18px;letter-spacing:.2em}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class='j meta'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + f"<div class=bd><div class=edge></div>{vlines(s['lines'], s['size'], CREAM)}"
            + f"<div style='margin-top:26px'>{ticks(s['ticks'], 'rgba(255,248,245,.80)', 19, 30, CORAL)}</div></div>"
            + logo("crm", 100 - GUT - 7.6, 5.2, 7.6))
    return shell(css, body)


# 4 ------------------------------------------------------------------------------ COMMERCE TRAY --
@arch_("tray")
def _tray(s, im, src):
    """The direct-response build: picture on top, a paper tray under it doing the selling."""
    g = s.get("ground") or lift(im, (0.05, 0.03, 0.3, 0.12))
    cut = s["cut"]
    css = f"""
    .pic{{position:absolute;left:0;right:0;top:0;height:{cut}%;overflow:hidden}}
    .tray{{position:absolute;left:0;right:0;top:{cut}%;bottom:0;background:{g};padding:{s['pad']}% {GUT}% 0}}
    .row{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:30px}}
    .hr{{height:1px;background:rgba(26,22,20,.20);margin:28px 0 22px}}
    """
    body = (f"<div class=pic>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=tray>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 18)}"
            + vlines(s["lines"], s["size"], INK)
            + "<div class=hr></div>"
            + ticks(s["ticks"], "rgba(26,22,20,.72)", 19, 28)
            + f"<div class=row><div>{price(s['price'], 46, INK)}"
            f"<span class='jb' style='font-size:20px;color:rgba(26,22,20,.55);margin-left:14px'>{s['sub']}</span></div>"
            f"{cta(s['cta'])}</div></div>"
            + logo("ink", GUT, 4.2, 6.6))
    return shell(css, body)


# 5 ----------------------------------------------------------------------------- CIRCLE WINDOW ---
@arch_("circle")
def _circle(s, im, src):
    g = s.get("ground") or lift(im, (0.05, 0.05, 0.25, 0.12), v=0.945, s=0.10)
    d = s.get("d", 80)
    css = f"""
    .ring{{position:absolute;left:50%;top:{s['cy']}%;width:{d}%;aspect-ratio:1;transform:translate(-50%,-50%);
      border-radius:50%;overflow:hidden}}
    .halo{{position:absolute;left:50%;top:{s['cy']}%;width:{d+5.2}%;aspect-ratio:1;
      transform:translate(-50%,-50%);border-radius:50%;border:1px solid rgba(26,22,20,.28)}}
    .top{{position:absolute;left:{GUT}%;top:7.0%;right:{GUT}%;display:flex;justify-content:space-between;
      color:{INK};font-size:18px;letter-spacing:.22em}}
    .tx{{position:absolute;left:{GUT}%;bottom:14%;right:{GUT}%}}
    """
    body = (f"<div style='position:absolute;inset:0;background:{g}'></div>"
            + f"<div class='j top'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + "<div class=halo></div>"
            + f"<div class=ring>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=tx>{vlines(s['lines'], s['size'], INK)}</div>"
            + logo("ink", GUT, 5.6, 7.4))
    return shell(css, body)


# 6 ---------------------------------------------------------------------------- VERTICAL CLIMB ---
@arch_("vertical")
def _vertical(s, im, src):
    """The line is set climbing, because the frame's shadows climb. Device = the frame's own law."""
    css = f"""
    .cl{{position:absolute;left:{s['x']}%;bottom:{s['y']}%;transform-origin:left bottom;
      transform:rotate(-90deg);display:flex;align-items:baseline;gap:34px}}
    .eb{{position:absolute;left:{GUT}%;top:7%;color:{INK};font-size:18px;letter-spacing:.22em}}
    .tick{{position:absolute;right:{GUT}%;top:7%;color:{INK};font-size:18px;letter-spacing:.22em}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class='j eb'>{s['eyebrow']}</div><div class='j tick'>{s['index']}</div>"
            + f"<div class=cl>{vlines(s['lines'], s['size'], INK)}</div>"
            + logo("ink", GUT, 5.4, 7.4))
    return shell(css, body)


# 7 --------------------------------------------------------------------------------- SWAP GRID ---
@arch_("swap")
def _swap(s, im, src):
    g = s.get("ground") or lift(im, (0.05, 0.05, 0.25, 0.1))
    css = f"""
    .pair{{position:absolute;left:{GUT}%;right:{GUT}%;top:{s['top']}%;display:flex;gap:14px}}
    .cell{{flex:1;aspect-ratio:1;overflow:hidden;position:relative}}
    .cap{{position:absolute;left:{GUT}%;right:{GUT}%;top:{s['top']+s['capdy']}%;display:flex;gap:14px;
      color:rgba(26,22,20,.70);font-size:18px;letter-spacing:.15em}}
    .cap span{{flex:1}}
    .tx{{position:absolute;left:{GUT}%;top:{s['tyy']}%;right:{GUT}%}}
    .sw{{position:absolute;left:50%;top:{s['top']+s['capdy']-3.6}%;transform:translateX(-50%);
      width:32px;height:32px;border:1px solid rgba(26,22,20,.60);border-radius:50%;
      display:flex;align-items:center;justify-content:center;background:{g}}}
    .sw i,.sw u{{position:absolute;width:15px;height:1.4px;background:{INK};text-decoration:none}}
    .sw i{{top:13px}} .sw u{{top:18px}}
    """
    cid = s["id"]
    cells = "".join(f"<div class=cell>{hero(subcrop(src, r, cid + '_' + str(i)))}</div>"
                    for i, r in enumerate(s["crops"]))
    caps = "".join(f"<span>{c}</span>" for c in s["caps"])
    body = (f"<div style='position:absolute;inset:0;background:{g}'></div>"
            + f"<div class=tx>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 20)}"
            f"{vlines(s['lines'], s['size'], INK)}</div>"
            + f"<div class=pair>{cells}</div>"
            + f"<div class='j cap'>{caps}</div><div class=sw><i></i><u></u></div>"
            + logo("ink", GUT, 5.4, 7.4))
    return shell(css, body)


# 8 ----------------------------------------------------------------------------------- WHISPER ---
@arch_("whisper")
def _whisper(s, im, src):
    """Maximum restraint - one small line at the foot. The set needs a quiet beat."""
    css = f"""
    .tx{{position:absolute;left:{GUT}%;bottom:{s['y']}%}}
    .hr{{width:46px;height:1px;background:{INK};opacity:.55;margin:0 0 20px}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class=tx><div class=hr></div>{vlines(s['lines'], s['size'], INK)}"
            + f"<div class='j' style='font-size:18px;letter-spacing:.2em;color:rgba(26,22,20,.62);margin-top:22px'>{s['eyebrow']}</div></div>"
            + logo("ink", 100 - GUT - 7.2, 5.4, 7.2))
    return shell(css, body)


# 9 --------------------------------------------------------------------------------- OVERPRINT ---
@arch_("overprint")
def _overprint(s, im, src):
    """Display type at poster scale, bleeding off the edge. Confidence, not decoration."""
    css = f"""
    .tx{{position:absolute;left:{s['x']}%;top:{s['y']}%}}
    .eb{{position:absolute;left:{GUT}%;bottom:5.8%;color:{INK};font-size:18px;letter-spacing:.22em}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class=tx>{vlines(s['lines'], s['size'], s.get('colour', INK), 0.93)}</div>"
            + f"<div class='j eb'>{s['eyebrow']}</div>"
            + logo("ink", 100 - GUT - 7.2, 5.2, 7.2))
    return shell(css, body)


# 10 ------------------------------------------------------------------------------ MARGIN COLUMN -
@arch_("margin")
def _margin(s, im, src):
    g = s.get("ground") or lift(im, (0.05, 0.03, 0.25, 0.12))
    c = s["col"]
    css = f"""
    .col{{position:absolute;left:0;top:0;bottom:0;width:{c}%;background:{g};padding:{GUT*1.5}% 5% 0 {GUT}%;
      display:flex;flex-direction:column}}
    .pic{{position:absolute;left:{c}%;right:0;top:0;bottom:0;overflow:hidden}}
    .spec{{margin-top:auto;margin-bottom:{s['sb']}%}}
    .spec div{{font-size:19px;letter-spacing:.02em;color:rgba(26,22,20,.66);line-height:1.85}}
    .hr{{width:38px;height:1px;background:{INK};opacity:.5;margin:22px 0 26px}}
    """
    spec = "".join(f"<div class=jb>{x}</div>" for x in s["spec"])
    body = (f"<div class=pic>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=col>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 17)}"
            f"<div class=hr></div>{vlines(s['lines'], s['size'], INK, 1.08)}"
            f"<div class=spec>{spec}</div></div>"
            + logo("ink", GUT, 5.4, 8.6))
    return shell(css, body)


# 11 --------------------------------------------------------------------------------- TOP BAND ---
@arch_("bandtop")
def _bandtop(s, im, src):
    g = s.get("ground", CORAL)
    css = f"""
    .bd{{position:absolute;left:0;right:0;top:0;height:{s['h']}%;background:{g};
      padding:{GUT*0.9}% {GUT}% 0;display:flex;flex-direction:column;justify-content:center}}
    .pic{{position:absolute;left:0;right:0;top:{s['h']}%;bottom:0;overflow:hidden}}
    .row{{position:absolute;left:{GUT}%;right:{GUT}%;top:{GUT*0.9}%;display:flex;
      justify-content:space-between;color:rgba(26,22,20,.85);font-size:18px;letter-spacing:.2em}}
    .ft{{position:absolute;left:{GUT}%;bottom:6.4%;color:{s.get("footColour", CREAM)};font-size:22px;letter-spacing:.03em}}
    """
    body = (f"<div class=pic>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=bd>{vlines(s['lines'], s['size'], INK)}</div>"
            + f"<div class='j row'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + f"<div class='jb ft'>{s['foot']}</div>"
            + logo(s.get("logoMode","crm"), 100 - GUT - 7.2, 5.6, 7.2))
    return shell(css, body)


# 12 ----------------------------------------------------------------------------------- TICKER ---
@arch_("ticker")
def _ticker(s, im, src):
    """The ring prints a track of thousands of dots, so the ad is set as printed matter."""
    strip = (s["strip"] + " &nbsp;&middot;&nbsp; ") * 9
    css = f"""
    .st{{position:absolute;left:0;right:0;height:{s['sh']}%;background:{INK};color:{CREAM};
      display:flex;align-items:center;overflow:hidden;font-size:23px;letter-spacing:.34em;white-space:nowrap}}
    .st.a{{top:{s['t1']}%}} .st.b{{bottom:{s['t2']}%}}
    .tx{{position:absolute;left:{GUT}%;bottom:{s['ty']}%;right:{GUT}%}}
    .pz{{position:absolute;right:{GUT}%;bottom:{s['ty']}%;text-align:right}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class='j st a'>{strip}</div><div class='j st b'>{strip}</div>"
            + f"<div class=tx>{vlines(s['lines'], s['size'], INK)}</div>"
            + logo(s.get("logoMode","ink"), s.get("lx", GUT), s["ly"], 7.2))
    return shell(css, body)


# 13 --------------------------------------------------------------------------------- ZOOM PAIR --
@arch_("zoom")
def _zoom(s, im, src):
    """Full frame plus a magnified inset - the 'how big is it really' answer, made graphic."""
    ix, iy, iw = s["ins"]
    css = f"""
    .ins{{position:absolute;left:{ix}%;top:{iy}%;width:{iw}%;aspect-ratio:1;overflow:hidden;
      border:1px solid rgba(255,248,245,.85);outline:1px solid rgba(26,22,20,.14)}}
    .icap{{position:absolute;left:{ix}%;top:{iy + iw*(W/H) + 1.8}%;color:{INK};font-size:18px;letter-spacing:.16em;white-space:nowrap}}
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;width:{s.get('tw',56)}%}}
    .ldr{{position:absolute;background:{INK};opacity:.40}}
    """
    ldr = "".join(f"<div class=ldr style='left:{a}%;top:{b}%;width:{c}%;height:1px'></div>"
                  for a, b, c in s.get("leaders", []))
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class=tx>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 20)}"
            f"{vlines(s['lines'], s['size'], INK)}</div>" + ldr
            + f"<div class=ins>{hero(subcrop(src, s['insCrop'], s['id'] + '_ins'))}</div>"
            + f"<div class='j icap'>{s['icap']}</div>"
            + logo("ink", GUT, 5.0, 7.2))
    return shell(css, body)


# 14 ----------------------------------------------------------------------------------- DIPTYCH --
@arch_("diptych")
def _diptych(s, im, src):
    g = s.get("ground") or CREAM
    css = f"""
    .hf{{position:absolute;top:0;height:{s['h']}%;width:calc(50% - 3px);overflow:hidden}}
    .hf.l{{left:0}} .hf.r{{right:0}}
    .ft{{position:absolute;left:0;right:0;top:{s['h']}%;bottom:0;background:{g};padding:0 {GUT}%;
      display:flex;flex-direction:column;justify-content:center}}
    .cap{{position:absolute;top:{s['h']-5.4}%;color:{s.get('capColour', CREAM)};font-size:18px;letter-spacing:.18em}}
    """
    body = (f"<div class='hf l'>{hero(s['srcL'], s['posL'])}</div>"
            + f"<div class='hf r'>{hero(s['srcR'], s['posR'])}</div>"
            + f"<div class='j cap' style='left:{GUT}%'>{s['capL']}</div>"
            + f"<div class='j cap' style='left:{50+GUT*0.5}%'>{s['capR']}</div>"
            + f"<div class=ft>{vlines(s['lines'], s['size'], INK)}"
            f"<div style='margin-top:20px'>{ticks(s['ticks'], 'rgba(26,22,20,.68)', 19, 26)}</div></div>"
            + logo("ink", 100 - GUT - 7.2, 4.4, 7.2))
    return shell(css, body)


# 15 --------------------------------------------------------------------------------- SIDE PANEL -
@arch_("side")
def _side(s, im, src):
    t = s.get("tone") or tone(im, tuple(s["toneBox"]), v=s.get("v", 0.28))
    c = s["col"]
    css = f"""
    .pn{{position:absolute;left:0;top:0;bottom:0;width:{c}%;background:{t};padding:{GUT*1.4}% 6% {GUT*1.4}% {GUT}%;
      display:flex;flex-direction:column}}
    .pic{{position:absolute;left:{c}%;right:0;top:0;bottom:0;overflow:hidden}}
    .bot{{margin-top:auto}}
    .hr{{width:36px;height:1px;background:{CREAM};opacity:.55;margin:20px 0 24px}}
    """
    body = (f"<div class=pic>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=pn>{eyebrow(s['eyebrow'], 'rgba(255,248,245,.72)', 17)}"
            + f"<div class=bot>{vlines(s['lines'], s['size'], CREAM, 1.06)}<div class=hr></div>"
            + f"<div class='jb' style='font-size:19px;color:rgba(255,248,245,.72);line-height:1.7'>{s['sub']}</div>"
            + f"<div style='margin-top:26px'>{price(s['price'], 38, CREAM)}</div></div></div>"
            + logo("crm", GUT, 5.0, 8.0))
    return shell(css, body)


# 16 ------------------------------------------------------------------------------------- ARCH ---
@arch_("archw")
def _archw(s, im, src):
    g = s.get("ground") or lift(im, (0.05, 0.03, 0.3, 0.14), v=0.94, s=0.12)
    css = f"""
    .ar{{position:absolute;left:{s['x']}%;right:{s['x']}%;top:{s['t']}%;bottom:{s['b']}%;overflow:hidden;
      border-radius:{s['r']}px {s['r']}px 6px 6px}}
    .top{{position:absolute;left:{GUT}%;right:{GUT}%;top:6.4%;display:flex;justify-content:space-between;
      color:{INK};font-size:18px;letter-spacing:.22em}}
    .tx{{position:absolute;left:{GUT}%;bottom:{s['ty']}%;width:64%}}
    .pz{{position:absolute;right:{GUT}%;bottom:{s['ty']}%;text-align:right}}
    """
    body = (f"<div style='position:absolute;inset:0;background:{g}'></div>"
            + f"<div class='j top'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + f"<div class=ar>{hero(src, s.get('pos','50% 50%'))}</div>"
            + f"<div class=tx>{vlines(s['lines'], s['size'], INK)}</div>"
            + f"<div class=pz>{price(s['price'], 34, 'rgba(26,22,20,.72)')}</div>"
            + logo("ink", GUT, 4.8, 7.2))
    return shell(css, body)


# 17 ------------------------------------------------------------------------------ FLOATING CARD -
@arch_("card")
def _card(s, im, src):
    g = s.get("ground") or lift(im, (0.05, 0.03, 0.25, 0.1), v=0.975, s=0.05)
    x, y, w, h = s["card"]
    rows = "".join(f"<div class='jb rw'>{r}</div>" for r in s["spec"])
    css = f"""
    .cd{{position:absolute;left:{x}%;top:{y}%;width:{w}%;height:{h}%;background:{g};
      padding:5.4% 6% 5%;display:flex;flex-direction:column;border:1px solid rgba(26,22,20,.10)}}
    .rw{{font-size:19px;color:rgba(26,22,20,.68);line-height:1.9;letter-spacing:.02em}}
    .pp{{margin-top:auto;display:flex;align-items:baseline;justify-content:space-between}}
    .hr{{height:1px;background:rgba(26,22,20,.18);margin:16px 0 14px}}
    .go{{border-bottom:1px solid {INK};padding-bottom:4px;font-size:19px;letter-spacing:.16em;color:{INK}}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<div class=cd>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 17, 14)}"
            + vlines(s["lines"], s["size"], INK, 1.06)
            + "<div class=hr></div>" + rows
            + f"<div class=pp>{price(s['price'], 42, INK)}<span class='j go'>{s['cta']}</span></div></div>"
            + logo("ink", GUT, 5.0, 7.6))
    return shell(css, body)


# 18 ------------------------------------------------------------------------------------ RADIAL --
@arch_("radial")
def _radial(s, im, src):
    """Hairlines continue the folds the charm is already making. The graphic obeys the frame."""
    cx, cy = s["c"]
    import math
    lines = ""
    for a in s["angles"]:
        x2 = cx + math.cos(math.radians(a)) * 160
        y2 = cy + math.sin(math.radians(a)) * 160 * (W / H)
        lines += (f"<line x1='{cx}' y1='{cy}' x2='{x2:.2f}' y2='{y2:.2f}' "
                  f"stroke='{s.get('stroke','rgba(26,22,20,.30)')}' stroke-width='{s.get('sw',.14)}'/>")
    css = f"""
    svg.ry{{position:absolute;inset:0;width:100%;height:100%}}
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;right:{GUT}%}}
    .rn{{position:absolute;left:{cx}%;top:{cy}%;transform:translate(-50%,-50%);
      width:{s['rd']}%;aspect-ratio:1;border-radius:50%;border:1px solid rgba(26,22,20,.34)}}
    """
    body = (hero(src, s.get("pos", "50% 50%"))
            + f"<svg class=ry viewBox='0 0 100 100' preserveAspectRatio=none>{lines}</svg>"
            + "<div class=rn></div>"
            + f"<div class=tx>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 20)}"
            f"{vlines(s['lines'], s['size'], INK)}</div>"
            + logo("ink", GUT, 5.4, 7.4))
    return shell(css, body)


# 19 ------------------------------------------------------------------------------------ POSTER --
@arch_("poster")
def _poster(s, im, src):
    """No product at full size: pure typography plus three portholes. The feed needs a flat beat."""
    dots = "".join(f"<div class=dt><div class=dw>{hero(d[0], d[1])}</div>"
                   f"<div class='j dc'>{d[2]}</div></div>" for d in s["dots"])
    css = f"""
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;right:{GUT}%}}
    .strip{{position:absolute;left:{GUT}%;right:{GUT}%;bottom:{s['sy']}%;display:flex;gap:4.2%}}
    .dt{{flex:1}} .dw{{width:100%;aspect-ratio:1;border-radius:50%;overflow:hidden;position:relative}}
    .dc{{font-size:17px;letter-spacing:.14em;color:rgba(26,22,20,.82);margin-top:14px}}
    .top{{position:absolute;left:{GUT}%;right:{GUT}%;top:6.4%;display:flex;justify-content:space-between;
      color:{INK};font-size:18px;letter-spacing:.24em}}
    .hr{{position:absolute;left:{GUT}%;right:{GUT}%;top:{s['hy']}%;height:1px;background:rgba(26,22,20,.22)}}
    """
    body = (f"<div style='position:absolute;inset:0;background:{s['ground']}'></div>"
            + f"<div class='j top'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + f"<div class=tx>{vlines(s['lines'], s['size'], INK, 0.96)}</div>"
            + "<div class=hr></div>"
            + f"<div class=strip>{dots}</div>"
            + logo("ink", GUT, 5.0, 7.6))
    return shell(css, body)


# 20 ------------------------------------------------------------------------------------ LADDER --
@arch_("ladder")
def _ladder(s, im, src):
    """The whole price ladder as a typographic table. Honest, useful, and nothing like an image ad."""
    rows = ""
    for lab, val, fr, pos in s["rows"]:
        rows += (f"<div class=lr><div class=thumb>{hero(s['rowSrc'][fr], pos)}</div>"
                 f"<div class='jb lb'>{lab}</div><div class=lv>{price(val, 30, INK)}</div></div>")
    css = f"""
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;right:{GUT}%}}
    .tbl{{position:absolute;left:{GUT}%;right:{GUT}%;top:{s['by']}%}}
    .lr{{display:flex;align-items:center;gap:22px;padding:20px 0;border-top:1px solid rgba(26,22,20,.18)}}
    .lr:last-child{{border-bottom:1px solid rgba(26,22,20,.18)}}
    .thumb{{width:62px;height:62px;overflow:hidden;position:relative;flex:none;border-radius:50%}}
    .lb{{flex:1;font-size:22px;color:rgba(26,22,20,.80);letter-spacing:.02em}}
    .foot{{position:absolute;left:{GUT}%;right:{GUT}%;bottom:{s['fy']}%}}
    """
    body = (f"<div style='position:absolute;inset:0;background:{s['ground']}'></div>"
            + f"<div class=tx>{eyebrow(s['eyebrow'], MARIGOLD_DEEP, 18, 22)}"
            f"{vlines(s['lines'], s['size'], INK, 0.98)}</div>"
            + f"<div class=tbl>{rows}</div>"
            + f"<div class=foot>{ticks(s['ticks'], 'rgba(26,22,20,.70)', 19, 26)}"
            f"<div style='margin-top:26px'>{cta(s['cta'])}</div></div>"
            + logo("ink", 100 - GUT - 7.2, 5.0, 7.2))
    return shell(css, body)


# 21 ----------------------------------------------------------------------------- GIANT NUMERAL --
@arch_("numeral")
def _numeral(s, im, src):
    """The floor price at poster scale with the photograph inside the figures."""
    css = f"""
    .big{{position:absolute;left:{s['x']}%;top:{s['y']}%;font-size:{s['size']}px;line-height:.86;
      background-image:url(data:image/png;base64,{b64(src)});background-size:{s['bs']};
      background-position:{s['bp']};-webkit-background-clip:text;background-clip:text;
      color:transparent;letter-spacing:-.03em}}
    .cur{{font-size:.30em;vertical-align:.92em;letter-spacing:0;margin-right:.05em;
      font-family:{PRICE_STACK};color:{INK};-webkit-text-fill-color:{INK}}}
    .tx{{position:absolute;left:{GUT}%;top:{s['ty']}%;right:{GUT}%}}
    .top{{position:absolute;left:{GUT}%;right:{GUT}%;top:6.4%;display:flex;justify-content:space-between;
      color:{INK};font-size:18px;letter-spacing:.24em}}
    .foot{{position:absolute;left:{GUT}%;right:{GUT}%;bottom:{s['fy']}%}}
    .hr{{height:1px;background:rgba(26,22,20,.20);margin-bottom:26px}}
    .strip{{position:absolute;left:{GUT}%;right:{GUT}%;bottom:{s.get('sy',22)}%;display:flex;gap:4.2%}}
    .dt{{flex:1}} .dw{{width:100%;aspect-ratio:1;border-radius:50%;overflow:hidden;position:relative}}
    .dc{{font-size:17px;letter-spacing:.13em;color:rgba(26,22,20,.82);margin-top:13px}}
    .dp{{font-size:19px;letter-spacing:.01em;color:{INK};margin-top:6px}}
    """
    strip = ""
    if s.get("dots"):
        strip = ("<div class=strip>" + "".join(
            f"<div class=dt><div class=dw>{hero(d[0], d[1])}</div>"
            f"<div class='j dc'>{d[2]}</div><div class='pr dp'>{d[3]}</div></div>"
            for d in s["dots"]) + "</div>")
    body = (f"<div style='position:absolute;inset:0;background:{s['ground']}'></div>"
            + f"<div class='j top'><span>{s['eyebrow']}</span><span>{s['index']}</span></div>"
            + f"<div class='v big'><span class=cur>&#8377;</span>{s['fig']}</div>" + strip
            + f"<div class=tx>{vlines(s['lines'], s['sub'], INK)}"
            + (f"<div class='jb' style='font-size:23px;color:rgba(26,22,20,.62);margin-top:22px'>"
               f"{s['subline']}</div>" if s.get("subline") else "") + "</div>"
            + f"<div class=foot><div class=hr></div>{ticks(s['ticks'], 'rgba(26,22,20,.72)', 19, 26)}</div>"
            + logo("ink", 100 - GUT - 7.2, 5.0, 7.2))
    return shell(css, body)


# ================================================================================== RENDER =======
def render(specs, outdir, bare=None):
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    frames = {}
    for jf in ("frames_lilac.json", "frames_soft.json"):
        ix = json.loads((ROOT / jf).read_text())
        for f in ix["frames"]:
            frames[f["id"]] = pathlib.Path(ix["root"]) / f["file"]
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=CHROME)
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=SCALE)
        for s in specs:
            src = frames[s["frame"]] if s.get("frame") else None
            if s.get("frameL"):
                s["srcL"], s["srcR"] = frames[s["frameL"]], frames[s["frameR"]]
            if s.get("dotFrames"):
                s["dots"] = [[frames[d[0]], *d[1:]] for d in s["dotFrames"]]
            if s.get("rows"):
                s["rowSrc"] = {r[2]: frames[r[2]] for r in s["rows"]}
            im = _cover(src) if src else Image.new("RGB", (W, H), CREAM)
            html = L[s["layout"]](s, im, src)
            if bare is not None:
                globals()["HIDE_TYPE"] = True
                pg.set_content(L[s["layout"]](s, im, src), wait_until="load")
                pg.wait_for_timeout(220)
                pg.screenshot(path=str(pathlib.Path(bare) / f"{s['id']}.png"))
                globals()["HIDE_TYPE"] = False
            pg.set_content(html, wait_until="load")
            pg.wait_for_timeout(300)
            out = outdir / f"{s['id']}.png"
            pg.screenshot(path=str(out))
            Image.open(out).resize((216, 270), Image.LANCZOS).save(outdir / f"{s['id']}_thumb.png")
            print(f"  {s['id']:<5}{s['layout']:<11}{s.get('frame') or s.get('frameL','-'):<5}"
                  f"{' '.join(s.get('lines', []))[:52]}")
        br.close()


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    bare = str(ROOT / "ads_bare") if "--bare" in sys.argv else None
    if bare:
        pathlib.Path(bare).mkdir(exist_ok=True)
    specs = json.loads(pathlib.Path(args[0]).read_text())
    only = args[2:] or None
    if only:
        specs = [s for s in specs if s["id"] in only]
    render(specs, args[1], bare)
    print(f"\n{len(specs)} creatives")
