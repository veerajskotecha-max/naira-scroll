# Wall posters for the Naira Petite stall (Fashion Mantra Exhibition, Emerald Park, Nashik), in the three colour
# themes of the exhibition standees. One per shell-scheme panel, each 24 × 36 in (2 × 3 ft) portrait:
#   back:            the three catalogue covers, from covers_print.py
#   spare (SAGE):    sage-edit (Heartbead hero, four more pieces)  ·  about (who Naira is, three on-model arches)
#   left  (APRICOT): apricot-edit (Woven Gold Hoops hero)          ·  gifting (the blush box, prices by category)
#   right (LILAC):   lilac-edit (Prism Rivière hero)               ·  catalogue (twelve on-model pieces, a large QR)
# Pages are laid out at 96 CSS px per inch, so the PDF is exactly 24 × 36 in with the photos embedded at their own
# resolution; a 150 ppi JPG and a small preview are written too.
# Usage: posters.py [name ...] -> <scratchpad>/stall/out/Naira-Stall-<wall>-<n>-<name>-24x36in.{pdf,jpg}, previews/
import html, json, os, subprocess, sys
from PIL import Image, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(f"{HERE}/../catalogue"))
import cards as C

SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
IMG, WORK, OUT = f"{SP}/stall/img", f"{SP}/stall/work", f"{SP}/stall/out"
PLATES = os.path.normpath(f"{HERE}/../colour-camps/plates")
FONTS, BRAND = f"{SP}/cat/fonts", C.BRAND
W, H = 2304, 3456                                   # 24 × 36 in at 96 px/in
URL = "https://www.nairaflore.com/?utm_source=stall&utm_medium=poster&utm_campaign=fashion-mantra-nashik"
ROWS = {r["handle"]: r for r in json.load(open(f"{SP}/cat/src/products_pick.json"))}
def price(h): return f"₹{ROWS[h]['price']:,}"

THEME = {
    "APRICOT": dict(g1="#F8E9DF", g2="#F2D8C8", deep="#2E4A41", acc="#B85A3A", soft="#EFD3C2", line="rgba(46,74,65,.32)"),
    "SAGE":    dict(g1="#EEF3EF", g2="#DCE7DF", deep="#24433A", acc="#557C6C", soft="#D3E0D7", line="rgba(36,67,58,.30)"),
    "LILAC":   dict(g1="#F2ECF5", g2="#E4D8EC", deep="#3A2D52", acc="#76599B", soft="#DDD0E7", line="rgba(58,45,82,.30)"),
}
EDITS = {
    "APRICOT": dict(word="APRICOT", line="the colour of a slow afternoon.", hero=("A-apricot/i-001.jpg", (.49, .565)), h="woven-gold-hoops",
                    spec="25 mm braided hoops · gold tone", more=[("brushed-gold-huggies", "A-apricot/i-005.jpg", (.5, .5)),
                    ("heartline-paperclip-necklace", "A-apricot/i-007.jpg", (.5, .52)), ("ribbon-bow-earrings", "A-apricot/i-009.jpg", (.48, .45)),
                    ("ribbon-bead-bracelet", "A-apricot/i-011.jpg", (.5, .55))]),
    "SAGE":    dict(word="SAGE", line="the colour of quiet.", hero=("B-sage/i-003.jpg", (.55, .49)), h="heartbead-bracelet",
                    spec="6 mm steel beads · gold-tone toggle and heart", more=[("toggle-link-chain", f"{PLATES}/SAGE/sage_YF5143_S1_a5g.jpg", (.45, .46)),
                    ("verdant-circlet-studs", f"{PLATES}/SAGE/sage_FE02847B_S1_a4g.jpg", (.55, .45)), ("granule-dome-ring", f"{PLATES}/SAGE/sage_JDR0104337_S3_a2g.jpg", (.62, .38)),
                    ("chevron-whisper-ring", f"{PLATES}/SAGE/sage_JDR0303312-7_S3_a2g.jpg", (.6, .38))]),
    "LILAC":   dict(word="LILAC", line="the colour of evening.", hero=("C-lilac/i-006.jpg", (.52, .485)), h="prism-riviere-bracelet",
                    spec="5 mm cushion-cut cubic zirconia · rhodium", more=[("pearl-blossom-earrings", "C-lilac/i-015.jpg", (.55, .52)),
                    ("silver-drop-earrings", "C-lilac/i-024.jpg", (.55, .55)), ("serpentine-whisper-chain-silver", "C-lilac/i-037.jpg", (.5, .6)),
                    ("vintage-halo-ring", "C-lilac/i-046.jpg", (.5, .62))]),
}

def src(p): return p if p.startswith("/") else f"{IMG}/{p}"

def crop_to(path, aspect, centre, out, width=None, frac=1.0):
    """Crops a photo to aspect (w/h) round centre (fractions), as large as `frac` of the photo allows; saves JPEG."""
    im = Image.open(src(path)).convert("RGB"); w, h = im.size
    cw = min(w * frac, h * aspect * frac); ch = cw / aspect
    x0 = min(max(centre[0] * w - cw / 2, 0), w - cw); y0 = min(max(centre[1] * h - ch / 2, 0), h - ch)
    c = im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch)))
    if width and c.width > width: c = c.resize((width, round(width / aspect)), Image.LANCZOS)
    p = f"{WORK}/{out}.jpg"; c.save(p, quality=93, subsampling=0); return p

def qr_svg(colour, size):
    py = f"{SP}/venv/bin/python"
    code = ("import segno,sys,io;q=segno.make(sys.argv[1],error='m');b=io.BytesIO();"
            "q.save(b,kind='svg',dark=sys.argv[2],light=None,border=0,xmldecl=False,omitsize=True);print(b.getvalue().decode())")
    svg = subprocess.run([py, "-c", code, URL, colour], capture_output=True, text=True, check=True).stdout.strip()
    return svg.replace("<svg ", f'<svg width="{size}" height="{size}" shape-rendering="crispEdges" style="display:block" ', 1)

def fit_size(text, width, font=f"{FONTS}/Velista.ttf", track=.02):
    f = ImageFont.truetype(font, 400); w = f.getlength(text) + track * 400 * (len(text) - 1)
    return int(width * 400 / w)

HEAD = """<!doctype html><html><head><meta charset="utf-8"><style>
@page{size:24in 36in;margin:0}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Velista;src:url("file://%(f)s/Velista.ttf")}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:%(W)spx;height:%(H)spx;overflow:hidden}
.pg{position:relative;width:%(W)spx;height:%(H)spx;overflow:hidden;color:%(deep)s;background:linear-gradient(180deg,%(g1)s 0%%,%(g1)s 35%%,%(g2)s 100%%)}
.a{position:absolute}.c{left:0;right:0;text-align:center}
.logo{position:absolute;left:50%%;transform:translateX(-50%%)}
.eyebrow{font:600 30px/1 Jost;letter-spacing:.52em;text-transform:uppercase;color:%(acc)s;padding-left:.52em}
.word{font-family:Velista;line-height:.86;letter-spacing:.02em;font-variant-ligatures:none;color:%(deep)s}
.ital{font:400 italic 66px/1.1 CGI;color:%(deep)s}
.arch{position:absolute;overflow:hidden;border-radius:9999px 9999px 0 0}
.arch img{display:block;width:100%%;height:100%%;object-fit:cover}
.archline{position:absolute;border:2.5px solid %(line)s;border-bottom:0;border-radius:9999px 9999px 0 0}
.label{font:600 25px/1 Jost;letter-spacing:.4em;text-transform:uppercase;padding-left:.4em}
.nm{font-family:Velista;font-variant-ligatures:none;text-transform:uppercase}
.spec{font:500 28px/1 Jost;letter-spacing:.22em;text-transform:uppercase;opacity:.78;padding-left:.22em}
.price{font:500 74px/1 CG;color:%(acc)s;letter-spacing:.02em}
.rule{position:absolute;left:150px;right:150px;height:0;border-top:2px solid %(line)s}
.body{font:400 56px/1.36 CG}
</style></head><body><div class="pg">
"""

def head(t): return HEAD % dict(t, f=FONTS, b=BRAND, W=W, H=H)

def footer(t, qr=True, y=3236):
    x = f'<div class="rule" style="top:{y}px"></div>'
    x += f'<div class="a" style="left:150px;top:{y + 52}px;font:400 italic 54px/1 CGI">nairaflore.com</div>'
    x += f'<div class="a c" style="top:{y + 64}px;font:600 22px/1 Jost;letter-spacing:.42em;padding-left:.42em;opacity:.8">SOFTLY, SLOWLY, WORN.</div>'
    if qr:
        x += f'<div class="a" style="right:150px;top:{y + 36}px;display:flex;align-items:center;gap:22px"><span class="label" style="font-size:20px;color:{t["acc"]}">Scan to shop</span>{qr_svg(t["deep"], 150)}</div>'
    else:
        x += f'<div class="a" style="right:150px;top:{y + 64}px;font:600 22px/1 Jost;letter-spacing:.42em;opacity:.8">NAIRA PETITE</div>'
    return x

def tinted_logo(colour):
    p = f"{WORK}/logo-{colour.strip('#')}.png"
    if not os.path.exists(p):
        a = Image.open(f"{BRAND}/logo_ink.png").convert("RGBA").split()[3]
        im = Image.new("RGBA", a.size, colour); im.putalpha(a); im.save(p)
    return p

def top(t, eyebrow, logo_w=520, y=150):
    lh = round(logo_w * 268 / 1200)
    return (f'<img class="logo" src="file://{tinted_logo(t["deep"])}" style="top:{y}px;width:{logo_w}px;height:{lh}px">'
            f'<div class="a c eyebrow" style="top:{y + lh + 56}px">{html.escape(eyebrow)}</div>')

def edit(camp):
    t, e = THEME[camp], EDITS[camp]
    x = head(t) + top(t, f"Naira Petite · the {camp.lower()} edit")
    fs = min(fit_size(e["word"], 1880), 430); wt = 420 + (430 - fs) // 3
    x += f'<div class="a c word" style="top:{wt}px;font-size:{fs}px">{e["word"]}</div>'
    wy = wt + round(fs * .86) + 30
    x += f'<div class="a c ital" style="top:{wy}px">{html.escape(e["line"])}</div>'
    ay, aw = wy + 128, 1360; ah = 2380 - ay
    ax = (W - aw) // 2
    hp = crop_to(e["hero"][0], aw / ah, e["hero"][1], f"hero-{camp}", width=2294)
    x += f'<div class="archline" style="left:{ax - 34}px;top:{ay - 34}px;width:{aw + 68}px;height:{ah + 34}px"></div>'
    x += f'<div class="arch" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px"><img src="file://{hp}"></div>'
    cy = ay + ah + 60
    x += f'<div class="a c nm" style="top:{cy}px;font-size:84px">{html.escape(ROWS[e["h"]]["title"])}</div>'
    x += f'<div class="a c spec" style="top:{cy + 112}px">{html.escape(e["spec"])}</div>'
    x += f'<div class="a c price" style="top:{cy + 170}px">{price(e["h"])}</div>'
    ry = cy + 296
    x += f'<div class="a c label" style="top:{ry}px;color:{t["acc"]}">Also in the {camp.lower()} edit</div>'
    d, gap = 250, 140; x0 = (W - (4 * d + 3 * gap)) / 2
    for i, (h, p, cen) in enumerate(e["more"]):
        cp = crop_to(p, 1, cen, f"more-{h}", width=900, frac=.72)
        cx = x0 + i * (d + gap)
        nm = ROWS[h]["title"].replace(" — Silver", "")
        x += (f'<div class="a" style="left:{cx - 60:.0f}px;top:{ry + 60}px;width:{d + 120}px;text-align:center">'
              f'<img src="file://{cp}" style="width:{d}px;height:{d}px;border-radius:50%;display:block;margin:0 auto;box-shadow:0 0 0 2.5px {t["line"]}">'
              f'<div style="font:500 23px/1.25 Jost;letter-spacing:.14em;text-transform:uppercase;margin-top:22px">{html.escape(nm)}</div>'
              f'<div style="font:500 36px/1 CG;color:{t["acc"]};margin-top:10px">{price(h)}</div></div>')
    return x + footer(t) + "</div></body></html>"

def tile(h, name, size=900):
    r = ROWS[h]; path = f"{SP}/cat/src/full/{h}-worn.jpg"; Wp, Hp = Image.open(path).size
    b = C.load_boxes().get(f'{r["n"]}w')
    rect = C.crop(Wp, Hp, b["focus"] if r["type"] in ("Earrings", "Ring") else b["box"], 1, C.FILL.get(r["type"], .6), .48, .56)
    C.WORK = WORK; return C.cut(path, rect, (size, size), name)[0]

def about():
    t = THEME["SAGE"]
    x = head(t) + top(t, "About us", logo_w=820, y=170)
    x += f'<div class="a c word" style="top:520px;font-size:230px">SOFTLY, SLOWLY,</div>'
    x += f'<div class="a c" style="top:700px;font:400 italic 250px/1 CGI">worn.</div>'
    aw, ah, gap = 580, 860, 70; x0 = (W - (3 * aw + 2 * gap)) // 2; ay = 1040
    for i, h in enumerate(["marquise-drop-choker", "kiss-knot-bangle", "pearl-circlet-studs"]):
        p = tile(h, f"about-{h}", 1100)
        ap = crop_to(p, aw / ah, (.5, .5), f"about-arch-{h}", frac=1)
        ax = x0 + i * (aw + gap)
        x += f'<div class="archline" style="left:{ax - 20}px;top:{ay - 20}px;width:{aw + 40}px;height:{ah + 20}px"></div>'
        x += f'<div class="arch" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px"><img src="file://{ap}"></div>'
    by = ay + ah + 110
    copy = ("Naira is an Indian couture label: slow-made, hand-finished, and quiet by design. Naira Petite is its demi-fine "
            "jewellery line, the same soul in a smaller object. Gold-tone and silver-tone pieces, set with cubic zirconia, "
            "made to be worn every day rather than saved for one.")
    x += f'<div class="a c body" style="top:{by}px;left:260px;right:260px">{html.escape(copy)}</div>'
    py = by + 560
    cols = [("Nº 01", "Everyday demi-fine", "Made to be worn, not kept in a drawer."),
            ("Nº 02", "Gold tone & silver tone", "Finished pieces set with cubic zirconia."),
            ("Nº 03", "Gift-ready", "Every piece comes in our blush Naira box.")]
    cw = 620; x0 = (W - 3 * cw) // 2
    for i, (n, a, b) in enumerate(cols):
        x += (f'<div class="a" style="left:{x0 + i * cw}px;top:{py}px;width:{cw}px;text-align:center;padding:0 40px">'
              f'<div class="label" style="color:{t["acc"]}">{n}</div>'
              f'<div class="nm" style="font-size:64px;margin-top:28px;line-height:1.05">{html.escape(a)}</div>'
              f'<div style="font:400 italic 48px/1.3 CGI;margin-top:22px">{html.escape(b)}</div></div>')
        if i: x += f'<div class="a" style="left:{x0 + i * cw}px;top:{py + 10}px;height:330px;border-left:2px solid {t["line"]}"></div>'
    return x + footer(t) + "</div></body></html>"

def gifting():
    t = THEME["APRICOT"]
    x = head(t) + top(t, "For gifting")
    x += f'<div class="a c word" style="top:450px;font-size:330px">GIFT IT</div>'
    x += f'<div class="a c" style="top:740px;font:400 italic 190px/1 CGI">beautifully.</div>'
    aw, ah = 1440, 1360; ax = (W - aw) // 2; ay = 1020
    bp = crop_to(f"{SP}/stall/box/b3.jpg", aw / ah, (.5, .55), "gift-box", frac=1)
    x += f'<div class="archline" style="left:{ax - 34}px;top:{ay - 34}px;width:{aw + 68}px;height:{ah + 34}px"></div>'
    x += f'<div class="arch" style="left:{ax}px;top:{ay}px;width:{aw}px;height:{ah}px"><img src="file://{bp}"></div>'
    y = ay + ah + 80
    x += f'<div class="a c" style="top:{y}px;font:400 italic 64px/1.2 CGI">Every piece arrives in our blush Naira box, ready to give.</div>'
    lo = {}
    for r in ROWS.values(): lo[r["type"]] = min(lo.get(r["type"], 10**9), r["price"])
    rows = [("Earrings", lo["Earrings"]), ("Rings", lo["Ring"]), ("Bracelets", lo["Bracelet"]), ("Necklaces", lo["Necklace"])]
    y += 160; x0, x1 = 520, W - 520
    x += f'<div class="a c label" style="top:{y}px;color:{t["acc"]}">Gifts from ₹{min(v for _, v in rows):,}</div>'
    for i, (k, v) in enumerate(rows):
        yy = y + 90 + i * 110
        x += (f'<div class="a" style="left:{x0}px;width:{x1 - x0}px;top:{yy}px;display:flex;align-items:baseline;gap:24px">'
              f'<span class="nm" style="font-size:58px">{k}</span><span style="flex:1;border-bottom:3px dotted {t["line"]};transform:translateY(-12px)"></span>'
              f'<span style="font:400 italic 44px/1 CGI">from</span><span class="price" style="font-size:66px">₹{v:,}</span></div>')
    return x + footer(t) + "</div></body></html>"

def catalogue():
    t = THEME["LILAC"]
    x = head(t) + top(t, "The full catalogue")
    x += f'<div class="a c word" style="top:450px;font-size:300px">SEE IT ALL</div>'
    x += f'<div class="a c ital" style="top:730px;font-size:96px">every piece, online and on her.</div>'
    picks = ["kiss-knot-bangle", "woven-gold-hoops", "marquise-drop-choker", "lilac-papillon-ring", "prism-riviere-bracelet", "pearl-legacy-necklace",
             "aqua-heart-drops-silver", "silk-mesh-cuff", "bold-nocturne-chain", "verdant-cushion-studs", "roman-numeral-trio-ring", "torsade-pearl-cuff"]
    ts, g = 440, 26; x0 = (W - (4 * ts + 3 * g)) // 2; y0 = 920
    for i, h in enumerate(picks):
        p = tile(h, f"cat-{h}")
        c, r = i % 4, i // 4
        x += f'<img class="a" src="file://{p}" style="left:{x0 + c * (ts + g)}px;top:{y0 + r * (ts + g)}px;width:{ts}px;height:{ts}px">'
    y = y0 + 3 * ts + 2 * g + 110
    x += (f'<div class="a" style="left:0;right:0;top:{y}px;display:flex;justify-content:center;align-items:center;gap:90px">'
          f'<div style="padding:34px;background:{t["g1"]};box-shadow:0 0 0 2.5px {t["line"]}">{qr_svg(t["deep"], 520)}</div>'
          f'<div style="width:760px"><div class="label" style="color:{t["acc"]}">Scan to shop</div>'
          f'<div class="nm" style="font-size:96px;margin-top:30px;line-height:1">Every piece</div>'
          f'<div style="font:400 italic 64px/1.2 CGI;margin-top:22px">Earrings, rings, bracelets and necklaces, from ₹799.</div>'
          f'<div style="font:400 italic 58px/1 CGI;margin-top:40px;color:{t["acc"]}">nairaflore.com</div></div></div>')
    return x + footer(t, qr=False) + "</div></body></html>"

POSTERS = [("spare", 1, "sage-edit", lambda: edit("SAGE"), "SAGE"), ("spare", 2, "about", about, "SAGE"),
           ("left", 1, "apricot-edit", lambda: edit("APRICOT"), "APRICOT"), ("left", 2, "gifting", gifting, "APRICOT"),
           ("right", 1, "lilac-edit", lambda: edit("LILAC"), "LILAC"), ("right", 2, "catalogue", catalogue, "LILAC")]

def main(names):
    for d in (WORK, OUT, f"{OUT}/previews"): os.makedirs(d, exist_ok=True)
    jobs = []
    for wall, n, name, fn, camp in POSTERS:
        if names and name not in names: continue
        k = f"Naira-Stall-{wall}-{n}-{name}-24x36in"; open(f"{WORK}/{k}.html", "w").write(fn()); jobs.append(k)
    env = dict(os.environ, NODE_PATH="/opt/node-tools/node_modules")
    subprocess.run(["node", f"{HERE}/render_print.cjs", WORK, OUT, *jobs], check=True, env=env)
    print(len(jobs), "posters ->", OUT)

if __name__ == "__main__":
    main(sys.argv[1:])
