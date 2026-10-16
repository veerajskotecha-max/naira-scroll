# Builds finished ads from the keepers: each keeper photograph cropped to its exact Meta size (Feed 4:5 at 1080×1350, Stories 9:16
# at 1080×1920) with the copy from ads.json set in the Naira typefaces, rendered by Chromium. Output: <scratchpad>/ads/out/<id>.jpg
# and a contact sheet. Usage: build_ads.py [--cfg controls.json] [id ...]   (no ids = all; ads.json by default)
# An entry with "path" uses that photo (relative to docs/creative) instead of a keeper plate, as the plain controls do.
import json, os, re, subprocess, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
OUT, WORK, FONTS = f"{SPB}/ads/out", f"{SPB}/ads/work", f"{SPB}/c4/fonts"
SIZE = {"4:5": (1080, 1350), "9:16": (1080, 1920)}
SAFE = {"4:5": (72, 72), "9:16": (290, 380)}            # clear space from the top and bottom edges (Stories keep clear of the UI)
INK, CREAM = "#1C1C1C", "#FBF8F3"

CSS = """
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative}
.t{position:absolute;display:flex;flex-direction:column;gap:%(gap)dpx;color:var(--tone);isolation:isolate}
.h{font-family:CGI;font-weight:500;font-size:%(hs)dpx;line-height:.98;letter-spacing:-.005em;text-wrap:balance}
.c{font-family:CG;font-weight:500;font-size:%(cs)dpx;line-height:1.2;text-wrap:balance}
.n{font-family:Jost;font-weight:500;font-size:%(ns)dpx;letter-spacing:.2em;text-transform:uppercase;margin-top:8px;line-height:1.5}
.scrim::before{content:"";position:absolute;inset:-70px -90px;z-index:-1;
  background:radial-gradient(closest-side,var(--glow) 0%%,var(--glow) 45%%,transparent 100%%)}
.card{background:rgba(251,248,243,.94);padding:30px 34px 26px}
"""

def prep(ad):
    src = os.path.join(HERE, "..", ad["path"]) if "path" in ad else f"{SPB}/{ad['src']}/plates/{ad['id']}.png"; W, H = SIZE[ad["fmt"]]
    im = Image.open(src).convert("RGB"); w, h = im.size
    if w / h > W / H: nw = round(h * W / H); box = (round((w - nw) * ad.get("cx", .5)), 0, round((w - nw) * ad.get("cx", .5)) + nw, h)
    else: nh = round(w * H / W); box = (0, round((h - nh) * ad.get("cy", .5)), w, round((h - nh) * ad.get("cy", .5)) + nh)
    path = f"{WORK}/{ad['id']}_bg.jpg"; im.crop(box).resize((W, H), Image.LANCZOS).save(path, quality=95); return path

def glue(t):
    return re.sub(r"(\d) (mm|cm)\b", "\\1\u00a0\\2", t)                  # never break a number from its unit

def html(ad, bg):
    W, H = SIZE[ad["fmt"]]; top, bottom = SAFE[ad["fmt"]]; side = ad.get("x", 72)
    pos = {"tl": f"left:{side}px;top:{ad.get('y', top)}px", "tr": f"right:{side}px;top:{ad.get('y', top)}px;text-align:right;align-items:flex-end",
           "bl": f"left:{side}px;bottom:{ad.get('y', bottom if ad['fmt'] == '9:16' else 72)}px",
           "br": f"right:{side}px;bottom:{ad.get('y', bottom if ad['fmt'] == '9:16' else 72)}px;text-align:right;align-items:flex-end"}[ad["at"]]
    tone = CREAM if ad.get("tone") == "cream" else INK
    glow = "rgba(28,22,18,.45)" if ad.get("tone") == "cream" else "rgba(250,243,236,.78)"
    cls = "t" + (" scrim" if ad.get("scrim") else "") + (" card" if ad.get("card") else "")
    css = CSS % dict(f=FONTS, w=W, h=H, bg="file://" + bg, hs=ad.get("hs", 92), cs=ad.get("cs", 42), ns=ad.get("ns", 23), gap=ad.get("gap", 18))
    return (f'<meta charset="utf-8"><style>{css}</style><div class="{cls}" style="{pos};width:{ad["w"]}px;--tone:{tone};--glow:{glow}">'
            f'<div class="h">{glue(ad["h"])}</div><div class="c">{glue(ad["c"])}</div><div class="n">{glue(ad["n"])}</div></div>')

def main():
    args = sys.argv[1:]; name = "ads.json"
    if "--cfg" in args: i = args.index("--cfg"); name = args[i + 1]; del args[i:i + 2]
    cfg = json.load(open(f"{HERE}/{name}"))["ads"]; want = args
    for d in [OUT, WORK]: os.makedirs(d, exist_ok=True)
    jobs = []
    for ad in cfg:
        if want and ad["id"] not in want: continue
        open(f"{WORK}/{ad['id']}.html", "w").write(html(ad, prep(ad)))
        W, H = SIZE[ad["fmt"]]; jobs.append(f"{ad['id']}:{W}:{H}")
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", f"{HERE}/render.cjs", WORK, *jobs], check=True, env=env)
    for j in jobs:
        i = j.split(":")[0]; Image.open(f"{WORK}/{i}.png").convert("RGB").save(f"{OUT}/{i}.jpg", quality=92, subsampling=0); print("ad", i)
    ids = [a["id"] for a in cfg if os.path.exists(f"{OUT}/{a['id']}.jpg")]
    tw = 360; ims = [Image.open(f"{OUT}/{i}.jpg") for i in ids]; ims = [im.resize((tw, round(im.height * tw / im.width))) for im in ims]
    cols = 5; rows = [ims[r:r + cols] for r in range(0, len(ims), cols)]
    sheet = Image.new("RGB", (cols * (tw + 12) + 12, sum(max(i.height for i in r) + 12 for r in rows) + 12), (236, 232, 226)); y = 12
    for r in rows:
        for k, im in enumerate(r): sheet.paste(im, (12 + k * (tw + 12), y))
        y += max(i.height for i in r) + 12
    sheet.save(f"{SPB}/ads/sheet_{name.split('.')[0]}.jpg", quality=86); print("sheet", sheet.size)

if __name__ == "__main__":
    main()
