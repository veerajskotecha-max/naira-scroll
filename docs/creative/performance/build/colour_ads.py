# Colour-coded 50 (Oct 2026): the fruit-plate format with the least graphics, built from build/colour50.json.
#   Story 1080x1920: the photograph alone, as the 2.94x anaar Story ran; the words live in the primary text.
#   Feed  1080x1350: a 4:5 window of the plate (top edge `feed_top` px, centred when absent) with one small tone-on-tone block in the
#         calmest corner: the NAIRA wordmark, the line in Cormorant italic and NAME · PRICE in Jost, all in the shot's own `ink`.
# Placement is the house placer (perf_ads.PLACE_JS): in the page it tries every corner, width, offset and a slightly smaller size,
# measures the real text box on the busy-and-tone grid and keeps the cheapest; the type stays in the shot's ink whatever it picks.
# The grid reads smooth pale props (petha, petals) as calm, so an entry can fix the block with `pos` ({"left"|"right", "top"|"bottom"}
# in px) after a look at the Feed; `w` narrows the block so a line breaks in two.
# Usage: colour_ads.py [NN ...] -> ../ads/colour/<NN>-<handle>-feed.jpg and -story.jpg
import json, os, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.normpath(f"{PERF}/../finished-ads"))
import build_ads as B
from perf_ads import grid, PLACE_JS

WORK, OUT = f"{B.SPB}/perf/colour/ads", f"{PERF}/ads/colour"

CSS = """
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:1080px;height:1350px;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative}
.t{position:absolute;left:76px;top:84px;width:560px;color:%(ink)s;display:flex;flex-direction:column;align-items:flex-start}
.wm{height:30px;margin-bottom:30px}
.h{font-family:CGI;font-weight:500;font-size:64px;line-height:1.02;letter-spacing:-.004em;text-wrap:balance}
.c{font-family:Jost;font-weight:500;font-size:18px;letter-spacing:.2em;text-transform:uppercase;margin-top:24px;opacity:.86;white-space:nowrap}
"""

def logo(ink):
    """the ink wordmark recoloured to the shot's own ink"""
    path = f"{WORK}/logo_{ink.strip('#')}.png"
    if not os.path.exists(path):
        im = Image.open(f"{B.BRAND}/logo_ink.png").convert("RGBA"); a = im.getchannel("A")
        rgb = tuple(int(ink.strip("#")[i:i + 2], 16) for i in (0, 2, 4))
        out = Image.new("RGBA", im.size, rgb + (0,)); out.putalpha(a); out.save(path)
    return path

def feed(e):
    im = Image.open(f"{PERF}/{e['plate']}").convert("RGB")
    y0 = min(max(int(e.get("feed_top", 285)), 0), 570); im = im.crop((0, y0, 1080, y0 + 1350))
    bg = f"{WORK}/{e['n']}_bg.jpg"; im.save(bg, quality=95)
    P = dict(grid(bg), sel=".t", foot=False, quiet=False, W=1080, H=1350, top=64, bot=72, n=10, side=76, hs=e.get("hs", 64), cs=18,
             pref=e.get("at", "tl"), tone0="ink", ats=[e["at"]] if e.get("pin") else ["tl", "tr", "bl", "br"], ws=[e.get("w", 560), 470, 400],
             INK=e["ink"], PAPER=e["ink"], sy=None, lh=1.02, hl=1, fixed=bool(e.get("pos")), lock=True, noglow=True)
    css = CSS % dict(f=B.FONTS, bg="file://" + bg, ink=e["ink"])
    if e.get("pos"):
        right = "right" in e["pos"]
        css += ".t{left:auto;top:auto;width:%dpx;%s;%s}" % (e.get("w", 560), ";".join(f"{k}:{v}px" for k, v in e["pos"].items()),
                                                               "align-items:flex-end;text-align:right" if right else "")
    name = B.glue(e["title"] + (f" · {e['variant']}" if e.get("variant") else ""))
    html = (f'<meta charset="utf-8"><style>{css}</style><body><div class="t"><img class="wm" src="file://{logo(e["ink"])}">'
            f'<div class="h">{e["line"]}</div><div class="c">{name} &nbsp;·&nbsp; {e["price"]}</div></div>{PLACE_JS % json.dumps(P)}</body>')
    page = f"{WORK}/{e['n']}-feed.html"; open(page, "w").write(html); return f"{e['n']}-feed"

def main():
    want = set(sys.argv[1:]); L = json.load(open(f"{HERE}/colour50.json"))
    for d in (WORK, OUT): os.makedirs(d, exist_ok=True)
    jobs, done = [], []
    for e in L:
        if want and e["n"] not in want: continue
        base = os.path.basename(e["plate"])[:-4]
        Image.open(f"{PERF}/{e['plate']}").convert("RGB").save(f"{OUT}/{base}-story.jpg", quality=92, subsampling=0)
        page = feed(e); jobs.append(f"{page}:1080:1350"); done.append((page, base))
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    if jobs: subprocess.run(["node", f"{HERE}/render_perf.cjs", WORK, *jobs], check=True, env=env)
    for page, base in done:
        Image.open(f"{WORK}/{page}.png").convert("RGB").save(f"{OUT}/{base}-feed.jpg", quality=92, subsampling=0); print("ad", base)

if __name__ == "__main__":
    main()
