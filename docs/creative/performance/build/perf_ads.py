# Performance ads (Oct 2026): every passed frame from the performance shoot, set in one of the four overlays that have sold:
#   deck   "Almost edible." / "Sweet On You.": Velista capitals, italic correction, rule + spec, ink CTA, price (build_ads.html_deck)
#   note   "The gold note.": italic headline, two roman lines, tracked name · price (build_ads.html, layout v1)
#   quiet  the Apricot camp (1.72×): NAIRA wordmark at the top, name and price centred at the foot
#   plain  the fruit-plate Story (2.94×): the photograph alone; the words live in the primary text
# Frames are 1080×1920 (9:16). Each copy entry makes a Story (the frame as shot) and a Feed post (a 1080×1350 window centred on
# the jewellery, `cy` = its centre as a fraction of the frame height). A rhyme frame's Story is plain unless "story": "deck".
# Usage: perf_ads.py [--copy copy.json] [id-prefix ...] -> <scratchpad>/perf/ads/out/<id>.jpg, copied to ../ads/<id>.jpg
import json, os, re, shutil, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); PERF = os.path.dirname(HERE)
sys.path.insert(0, os.path.normpath(f"{PERF}/../finished-ads"))
import build_ads as B

SPB = B.SPB; OUT, WORK = f"{SPB}/perf/ads/out", f"{SPB}/perf/ads/work"

QUIET_CSS = """
@font-face{font-family:Velista;src:url("file://%(b)s/Velista.ttf")}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
html,body{margin:0;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{background:url("%(bg)s") center/cover no-repeat;position:relative;color:%(ink)s}
.wm{position:absolute;left:50%%;transform:translateX(-50%%);top:%(top)dpx;height:%(wh)dpx}
.ft{position:absolute;left:0;right:0;bottom:%(bot)dpx;text-align:center}
.nm{font-family:Velista;font-size:%(ns)dpx;letter-spacing:.14em;line-height:1;margin-left:.14em}
.pr{font-family:Jost;font-weight:500;font-size:%(ps)dpx;letter-spacing:.22em;margin-top:18px;margin-left:.22em}
"""

def html_quiet(ad, bg):
    W, H = B.SIZE[ad["fmt"]]; story = ad["fmt"] == "9:16"
    top, bot = (300, 400) if story else (70, 76)
    ink = B.DECK_PAPER if ad.get("tone") == "cream" else "#2B2622"
    logo = "logo_white.png" if ad.get("tone") == "cream" else "logo_ink.png"
    css = QUIET_CSS % dict(b=B.BRAND, f=B.FONTS, w=W, h=H, bg="file://" + bg, ink=ink, top=ad.get("wy", top), wh=ad.get("wh", 44),
                           bot=ad.get("fy", bot), ns=ad.get("ns", 40), ps=ad.get("ps", 22))
    return (f'<meta charset="utf-8"><style>{css}</style><body><img class="wm" src="file://{B.BRAND}/{logo}">'
            f'<div class="ft"><div class="nm">{B.glue(ad["name"].upper())}</div><div class="pr">{ad["price"]}</div></div></body>')

def prep(ad):
    im = Image.open(f"{PERF}/{ad['plate']}").convert("RGB").resize((1080, 1920), Image.LANCZOS)
    if ad["fmt"] == "4:5":
        cy = ad.get("cy", .5); y0 = min(max(round(cy * 1920 - 675), 0), 1920 - 1350); im = im.crop((0, y0, 1080, y0 + 1350))
    path = f"{WORK}/{ad['id']}_bg.jpg"; im.save(path, quality=95); return path

def expand(entries):
    """one copy entry per frame -> a Feed ad and a Story ad"""
    ads = []
    for e in entries:
        base = e.get("id") or re.sub(r"\.jpg$", "", os.path.basename(e["plate"]))
        for fmt, tag in (("4:5", "feed"), ("9:16", "story")):
            ad = dict(e, fmt=fmt, id=f"{base}-{tag}")
            ad.update(e.get(tag, {}) if isinstance(e.get(tag), dict) else {})
            if fmt == "9:16" and e["plate"].endswith("-rhyme.jpg") and e.get("story") != "deck": ad["layout"] = "plain"
            ads.append(ad)
    return ads

def main():
    args = sys.argv[1:]; name = f"{HERE}/copy.json"
    if "--copy" in args: i = args.index("--copy"); name = args[i + 1]; del args[i:i + 2]
    ads = expand(json.load(open(name))["frames"])
    for d in (OUT, WORK, f"{PERF}/ads"): os.makedirs(d, exist_ok=True)
    jobs = []
    for ad in ads:
        if args and not any(ad["id"].startswith(a) for a in args): continue
        bg = prep(ad); lay = ad.get("layout", "deck")
        if lay == "plain": Image.open(bg).save(f"{WORK}/{ad['id']}.png"); jobs.append((ad["id"], None)); continue
        page = {"deck": B.html_deck, "note": B.html, "quiet": html_quiet}[lay](dict(ad, layout="v1") if lay == "note" else ad, bg)
        open(f"{WORK}/{ad['id']}.html", "w").write(page); W, H = B.SIZE[ad["fmt"]]; jobs.append((ad["id"], f"{ad['id']}:{W}:{H}"))
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    todo = [j for _, j in jobs if j]
    for k in range(0, len(todo), 40): subprocess.run(["node", f"{B.HERE}/render.cjs", WORK, *todo[k:k + 40]], check=True, env=env)
    for i, _ in jobs:
        Image.open(f"{WORK}/{i}.png").convert("RGB").save(f"{OUT}/{i}.jpg", quality=92, subsampling=0)
        shutil.copy(f"{OUT}/{i}.jpg", f"{PERF}/ads/{i}.jpg"); print("ad", i)

if __name__ == "__main__":
    main()
