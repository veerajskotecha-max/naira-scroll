# Renders finished ads from a layout file: each photo cropped to Feed 4:5 (1080x1350) and Story 9:16 (1080x1920), with the
# Naira type system set in HTML and rendered by Chromium. Usage: render.py layout.json [key ...] -> <scratchpad>/ads20/out/<key>_{feed,story}.jpg
#
# The system (set 1, from the GIVA/Palmonas benchmark, 4 Nov 2026):
#  - One block at the bottom on a soft fade: the NAIRA wordmark heading it (a jewellery-tag lockup), optional serif line, the
#    piece's name in tracked Jost caps, the price in the serif, large, and the buy-more offer as an outlined chip. Sizes are set
#    for a phone: nothing under 27px on a 1080 canvas (about 10pt on a 390pt-wide screen); Stories a size up.
#    The wordmark sat top-centre in the first renders, the competitors' place for it, but on lips-down beauty crops that is
#    where the mouth and chin are, so it moved into the block; 'logo_at': 'top' (with 'logo_pos') brings it back per ad.
#  - Stories: the block ends 380px above the bottom (clear of the Shop button), the house rule of the earlier ads
#    (finished-ads/build_ads.py SAFE); anything at the top starts at 300px or lower, clear of the profile bar.
#  - theme 'light' sets ink type on an ivory fade, for photos whose lower part is pale (a white shirt).
#  - set 2: 'line_at': 'top' sets the serif line large at the top on its own fade ('ttheme' picks that fade's ground);
#    'src' crops the photo to a window first; 'cx'/'cy' place the crop.
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
FONTS = f"{SPB}/c4/fonts"
BRAND = os.path.normpath(os.path.join(HERE, "../../finished-ads/brand"))
OUT = f"{SPB}/ads20/out"
SIZE = {"feed": (1080, 1350), "story": (1080, 1920)}

CSS = """
@font-face{font-family:CG;src:url("file://%(f)s/CormorantGaramond[wght].ttf");font-weight:300 700}
@font-face{font-family:CGI;src:url("file://%(f)s/CormorantGaramond-Italic[wght].ttf");font-weight:300 700}
@font-face{font-family:Jost;src:url("file://%(f)s/Jost[wght].ttf");font-weight:100 900}
@font-face{font-family:Velista;src:url("file://%(b)s/Velista.ttf");font-weight:400 600}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;background:#140c0a}
.bg{position:absolute;inset:0;background:url("file://%(bg)s") no-repeat;background-size:%(bw)dpx %(bh)dpx;background-position:%(bx)dpx %(by)dpx}
.fade{position:absolute;left:0;right:0;bottom:0;height:%(fade)dpx;background:linear-gradient(to top,rgba(%(rgb)s,%(fa).2f) 0%%,rgba(%(rgb)s,%(fb).2f) 45%%,rgba(%(rgb)s,0) 100%%)}
.topfade{position:absolute;left:0;right:0;top:0;height:%(tfade)dpx;background:linear-gradient(to bottom,rgba(%(trgb)s,%(ta).2f),rgba(%(trgb)s,0))}
.logo{position:absolute;top:%(ly)dpx;width:%(lw)dpx;%(lpos)s}
.blk{position:absolute;left:%(side)dpx;right:%(side)dpx;%(anchor)s;display:flex;flex-direction:column;align-items:%(ai)s;text-align:%(ta2)s;color:%(fg)s;gap:0}
.line{font-family:CGI;font-weight:500;font-size:%(hs)dpx;line-height:1.02;letter-spacing:-.005em;text-wrap:balance;margin-bottom:%(hgap)dpx}
.line em{font-style:normal;font-family:CG}
.name{font-family:Jost;font-weight:500;font-size:%(ns)dpx;letter-spacing:.2em;text-transform:uppercase;line-height:1.35;text-wrap:balance}
.price{font-family:CG;font-weight:500;font-size:%(ps)dpx;letter-spacing:.01em;margin-top:%(pgap)dpx;line-height:1}
.price s{opacity:.62;font-weight:400;font-size:.72em;margin-left:14px;letter-spacing:.04em}
.note{font-family:Jost;font-weight:400;font-size:%(nts)dpx;letter-spacing:.04em;margin-top:12px;opacity:.9;line-height:1.3}
.chip{margin-top:%(cgap)dpx;border:1.5px solid %(cb)s;padding:13px 24px 12px;font-family:Jost;font-weight:500;font-size:%(cs)dpx;letter-spacing:.16em;
 text-transform:uppercase;line-height:1;white-space:nowrap;display:flex;gap:18px;align-items:center}
.chip i{width:6px;height:6px;background:%(dot)s;transform:rotate(45deg);display:block}
.blogo{width:%(blw)dpx;margin-bottom:%(blgap)dpx;display:block}
.tline{position:absolute;left:%(side)dpx;right:%(side)dpx;top:%(tly)dpx;text-align:center;color:%(tfg)s;font-family:CGI;font-weight:500;
 font-size:%(ths)dpx;line-height:1.02;letter-spacing:-.005em;text-wrap:balance}
.tline em{font-style:normal;font-family:CG}
.up{font-family:CG!important;font-weight:500;letter-spacing:-.012em}
.tchip{position:absolute;left:50%%;transform:translateX(-50%%);top:%(tcy)dpx;border:1.5px solid %(tcb)s;padding:13px 24px 12px;font-family:Jost;font-weight:500;
 font-size:%(cs)dpx;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap;display:flex;gap:18px;align-items:center;color:%(tfg)s}
.tchip i{width:6px;height:6px;background:%(tdot)s;transform:rotate(45deg);display:block}
.line.withsub{margin-bottom:6px}
.sub{font-family:Jost;font-weight:400;font-size:%(sbs)dpx;letter-spacing:.03em;line-height:1.3;margin-bottom:%(hgap)dpx;opacity:.92;text-wrap:balance}
"""

def html(ad, fmt, bg, iw, ih):
    ad = {**ad, **ad.get(fmt, {})}        # per-format overrides: "feed": {...} / "story": {...}
    W, H = SIZE[fmt]
    # cover-fit the photo, then place it by the crop centre (fraction of the photo's height) for this format
    s = max(W / iw, H / ih); bw, bh = round(iw * s), round(ih * s)
    cy = ad.get("cy", {}).get(fmt, 0.5); cx = ad.get("cx", {}).get(fmt, 0.5)
    bx = round(min(0, max(W - bw, W / 2 - cx * bw))); by = round(min(0, max(H - bh, H / 2 - cy * bh)))
    story = fmt == "story"; light = ad.get("theme") == "light"
    tlight = ad.get("ttheme", ad.get("theme")) == "light"          # the top can sit on a different ground from the bottom block
    top_line = bool(ad.get("line")) and ad.get("line_at", "block") == "top"
    logo_top = ad.get("logo_at", "block") == "top"                   # default: the wordmark heads the bottom block, clear of faces
    tfade = ad.get("tfade", (760 if story else 470) if top_line else ((420 if story else 260) if logo_top else 0))
    d = dict(rgb="251,248,243" if light else "20,11,9", trgb="251,248,243" if tlight else "20,11,9", fg="#1A1614" if light else "#FBF8F3",
             tfg="#1A1614" if tlight else "#FBF8F3",
             tcb="rgba(26,22,20,.7)" if tlight else "rgba(251,248,243,.78)", tdot="#9A6B2F" if tlight else "#E8C98F",
             tcy=ad.get("tly", 330 if story else 80) + round((ad.get("line", "").count("<br>") + 1) * ad.get("ths", 96 if story else 84) * 1.02) + ad.get("tcgap", 26),
             ai={"center": "center", "right": "flex-end", "left": "flex-start"}[ad.get("align", "center")], ta2=ad.get("align", "center"),
             cb="rgba(26,22,20,.7)" if light else "rgba(251,248,243,.78)", dot="#9A6B2F" if light else "#E8C98F",f=FONTS, b=BRAND, w=W, h=H, bg=bg, bw=bw, bh=bh, bx=bx, by=by,
             fade=ad.get("sfade", 820) if story else ad.get("fade", 560), fa=ad.get("fa", .82), fb=ad.get("fb", .45),
             tfade=tfade, ta=ad.get("ta", (.62 if story else .58) if top_line else (.40 if story else .32)),
             ly=300 if story else 62, lw=ad.get("lw", 190 if story else 170), side=72,
             lpos={"center": "left:50%;transform:translateX(-50%)", "right": "right:72px", "left": "left:72px"}[ad.get("logo_pos", "center")],
             # Stories: the block ends 420px above the bottom (y=1500), a 40px margin over the Shop-button zone (judge, round 1)
             anchor=("bottom:%dpx" % ad.get("sbot", 420)) if story else ("bottom:%dpx" % ad.get("bot", 74)),
             hs=ad.get("hs", 84 if story else 74), hgap=ad.get("hgap", 22),
             tly=ad.get("tly", 330 if story else 80), ths=ad.get("ths", 96 if story else 84),
             blw=ad.get("blw", 170 if story else 150), blgap=ad.get("blgap", 26 if story else 22),
             sbs=ad.get("sbs", 32 if story else 29),
             ns=ad.get("ns", 34 if story else 30), ps=ad.get("ps", 70 if story else 62), pgap=ad.get("pgap", 8),
             cs=ad.get("cs", 30 if story else 27), cgap=ad.get("cgap", 24), nts=ad.get("nts", 30 if story else 27))
    blogo = os.path.join(BRAND, "logo_ink.png" if light else "logo_white.png")
    tlogo = os.path.join(BRAND, "logo_ink.png" if tlight else "logo_white.png")
    parts = []
    if ad.get("logo_at", "block") == "block": parts.append('<img class="blogo" src="file://%s">' % blogo)   # 'none': the page header carries the brand
    up = " up" if ad.get("line_style") == "upright" else ""          # set 3: the Palmonas-style upright serif offer
    if ad.get("line") and not top_line:
        parts.append('<div class="line%s%s">%s</div>' % (up, " withsub" if ad.get("sub") else "", ad["line"]))
    if ad.get("sub"): parts.append('<div class="sub">%s</div>' % ad["sub"])   # the qualifier under the offer
    parts.append('<div class="name">%s</div>' % ad["name"])
    if ad.get("price"): parts.append('<div class="price">%s</div>' % ad["price"])
    if ad.get("note"): parts.append('<div class="note">%s</div>' % ad["note"])
    # parts are substituted as %s values below, so a percent sign here is literal: one %, never %%
    chip_top = ad.get("chip_at") == "top"                            # the chip under the top line, when the bottom is crowded
    if ad.get("chip", True) and not chip_top: parts.append('<div class="chip">Buy 2 · 10% off<i></i>Buy 3 · 20% off</div>' if ad.get("chip", True) is True else '<div class="chip">%s</div>' % ad["chip"])
    top = ('<div class="topfade"></div>' if tfade else "") + ('<img class="logo" src="file://%s">' % tlogo if logo_top else "") + \
          ('<div class="tline%s">%s</div>' % (up, ad["line"]) if top_line else "") + \
          ('<div class="tchip">Buy 2 · 10% off<i></i>Buy 3 · 20% off</div>' if chip_top and top_line else "")
    return ("<!doctype html><html><head><meta charset=utf-8><style>%s</style></head><body><div class=bg></div>"
            '<div class="fade"></div>%s<div class="blk">%s</div></body></html>') % (CSS % d, top, "".join(parts))

def main():
    from PIL import Image
    lay = json.load(open(os.path.join(HERE, sys.argv[1]))); keys = sys.argv[2:]
    os.makedirs(OUT, exist_ok=True); jobs = []
    tmp = tempfile.mkdtemp(dir=f"{SPB}/ads20")
    for ad in lay["ads"]:
        if keys and ad["key"] not in keys: continue
        bg = ad["photo"] if ad["photo"].startswith("/") else os.path.join(SPB, "ads20", ad["photo"])
        im = Image.open(bg); iw, ih = im.size
        for fmt in ad.get("formats", ["feed", "story"]):
            # optional source window [x0, y0, x1, y1] as fractions (one for both formats, or per format), e.g. to drop a letterbox band
            box = ad.get("src"); box = box.get(fmt) if isinstance(box, dict) else box
            if box:
                c = im.crop((round(box[0] * iw), round(box[1] * ih), round(box[2] * iw), round(box[3] * ih)))
                src = os.path.join(tmp, f"{ad['key']}_{fmt}_src.png"); c.save(src); fbg, fw, fh = src, c.width, c.height
            else:
                fbg, fw, fh = bg, iw, ih
            p = os.path.join(tmp, f"{ad['key']}_{fmt}.html"); open(p, "w").write(html(ad, fmt, fbg, fw, fh))
            jobs.append({"html": p, "out": os.path.join(OUT, f"{ad['key']}_{fmt}.jpg"), "w": SIZE[fmt][0], "h": SIZE[fmt][1]})
    jp = os.path.join(tmp, "jobs.json"); json.dump(jobs, open(jp, "w"))
    r = subprocess.run(["node", os.path.join(HERE, "shot.cjs"), jp], capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip()[-600:])

if __name__ == "__main__":
    main()
