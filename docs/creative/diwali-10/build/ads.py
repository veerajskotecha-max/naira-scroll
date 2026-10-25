# Diwali 10 (25 Oct 2026): the finished ads from the verified plates, in the house overlay of the approved colour ads
# (docs/creative/performance/build/colour_ads.py): the NAIRA wordmark, the line in Cormorant italic and NAME · PRICE in tracked Jost,
# all in the shot's own ink, placed by the house placer (perf_ads.PLACE_JS) in the calmest corner.
#   Feed  1080x1350: a 4:5 window of the plate (top edge `feed_top` px, centred when absent) with the block.
#   Story 1080x1920: the whole plate with the same block kept clear of the Story interface (top 300 px, bottom 400 px).
#   Clean 1080x1920: the plate alone, as the account's best Story (ruby anaar, 5.5% CTR) ran; offered as the A/B against the overlay.
# An entry's `feed` / `story` dict overrides its fields per format (`at`, `pos`, `w`, `hs`, `cs`, `ink`).
# Usage: ads.py [--copy variants.json] [NN ...]   (variants.json: the regional wordings of an ad, same plate)
import json, os, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); CREATIVE = os.path.dirname(ROOT)
sys.path.insert(0, f"{CREATIVE}/performance/build"); sys.path.insert(0, f"{CREATIVE}/finished-ads")
import build_ads as B
from perf_ads import grid, PLACE_JS

WORK, OUT = f"{B.SPB}/diwali10/work", f"{ROOT}/ads"
CSS = """
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:1080px;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative}
.t{position:absolute;left:76px;width:560px;color:%(ink)s;display:flex;flex-direction:column;align-items:flex-start}
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

def page(e, fmt):
    e = dict(e, **e.get(fmt, {}))
    im = Image.open(f"{ROOT}/{e['plate']}").convert("RGB").resize((1080, 1920), Image.LANCZOS)
    if fmt == "feed":
        y0 = min(max(int(e.get("feed_top", 285)), 0), 570); im = im.crop((0, y0, 1080, y0 + 1350)); H, top, bot = 1350, 64, 72
    else:
        H, top, bot = 1920, 300, 400
    bg = f"{WORK}/{e['n']}_{fmt}_bg.jpg"; im.save(bg, quality=95)
    P = dict(grid(bg), sel=".t", foot=False, quiet=False, W=1080, H=H, top=top, bot=bot, n=14 if fmt == "story" else 10, side=76,
             hs=e.get("hs", 64), cs=18, pref=e.get("at", "tl"), tone0="ink", ats=[e["at"]] if e.get("pin") else ["tl", "tr", "bl", "br"],
             ws=[e.get("w", 560), 470, 400], INK=e["ink"], PAPER=e["ink"], sy=None, lh=1.02, hl=1, fixed=bool(e.get("pos")), lock=True, noglow=True)
    css = CSS % dict(f=B.FONTS, bg="file://" + bg, ink=e["ink"], h=H)
    if e.get("pos"):
        right = "right" in e["pos"]
        css += ".t{left:auto;top:auto;bottom:auto;width:%dpx;%s;%s}" % (e.get("w", 560), ";".join(f"{k}:{v}px" for k, v in e["pos"].items()),
                                                               "align-items:flex-end;text-align:right" if right else "")
        if e.get("hs"): css += ".h{font-size:%dpx}" % e["hs"]
    if e.get("cs"): css += ".c{font-size:%dpx}" % e["cs"]
    name = B.glue(e["title"] + (f" · {e['variant']}" if e.get("variant") and not e.get("stack") else ""))
    price = f"{e['variant']} &nbsp;·&nbsp; {e['price']}" if e.get("stack") and e.get("variant") else e["price"]
    html = (f'<meta charset="utf-8"><style>{css}</style><body><div class="t"><img class="wm" src="file://{logo(e["ink"])}">'
            f'<div class="h">{e["line"]}</div><div class="c">{name}{"<br>" if e.get("stack") else " &nbsp;·&nbsp; "}{price}</div></div>'
            f'{PLACE_JS % json.dumps(P)}</body>')
    name = f"{e['n']}-{fmt}"; open(f"{WORK}/{name}.html", "w").write(html); return f"{name}:1080:{H}"

def main():
    args = sys.argv[1:]; name = "copy.json"
    if "--copy" in args: i = args.index("--copy"); name = args[i + 1]; del args[i:i + 2]
    want = set(args); L = json.load(open(f"{HERE}/{name}"))
    for d in (WORK, OUT): os.makedirs(d, exist_ok=True)
    jobs, done = [], []
    for e in L:
        if want and e["n"] not in want: continue
        base = f"{e['n']}-{e['key']}"
        Image.open(f"{ROOT}/{e['plate']}").convert("RGB").resize((1080, 1920), Image.LANCZOS).save(f"{OUT}/{base}-story-clean.jpg", quality=92, subsampling=0)
        for fmt in ("feed", "story"): jobs.append(page(e, fmt)); done.append((f"{e['n']}-{fmt}", f"{base}-{fmt}"))
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    if jobs: subprocess.run(["node", f"{CREATIVE}/performance/build/render_perf.cjs", WORK, *jobs], check=True, env=env)
    for page_id, out in done:
        Image.open(f"{WORK}/{page_id}.png").convert("RGB").save(f"{OUT}/{out}.jpg", quality=92, subsampling=0); print("ad", out)

if __name__ == "__main__":
    main()
