# Builds the Edition Two ads board (artifact page): every ad with its newest signed-or-latest review score, verdict, copy and
# timing. Usage: board.py OUTDIR
import json, os, sys, glob, re, html
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); FA = os.path.dirname(os.path.dirname(H)); OUT = sys.argv[1]
SP = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
ads = json.load(open(f"{FA}/e2_ads.json"))["ads"]; e = html.escape
rev = {}
for f in sorted(glob.glob(f"{FA}/review_r*.json"), key=lambda f: int(re.search(r"_r(\d+)\.json$", f).group(1))):
    n = int(re.search(r"_r(\d+)\.json$", f).group(1))
    if n < 19: continue
    for r in json.load(open(f)): rev.setdefault(r["id"], []).append((n, r))
TIMING = {"P11": "Diwali window (to 8 Nov)", "P13": "Diwali window (to 8 Nov)", "P12": "Diwali + wedding season", "E2_choker": "Hold to June (monsoon)",
          "E2_droplet": "Hold to June (rain)", "E2_mint": "Hold: re-shoot at true scale", "E2_tennis": "Now, through Diwali", "E2_knot": "Now, wedding season"}
os.makedirs(f"{OUT}/img", exist_ok=True); cards = []
order = sorted(ads, key=lambda a: -(rev.get(a["id"], [(0, {"score": 0})])[-1][1]["score"]))
for a in order:
    i = a["id"]; im = Image.open(f"{SP}/ads/out/{i}.jpg"); w = 480 if a["fmt"] == "4:5" else 400
    im.resize((w, round(im.height * w / im.width))).save(f"{OUT}/img/{i}.jpg", quality=84, optimize=True)
    hist = rev.get(i, []); last = hist[-1][1] if hist else None
    trail = " → ".join(f"{r['score']:g}" for _, r in hist)
    tm = next((v for k, v in TIMING.items() if i.startswith(k)), "Now")
    sc = f'<span class="sc {last["verdict"]}">{last["score"]:g}</span>' if last else '<span class="sc">—</span>'
    issues = "".join(f"<li>{e(x)}</li>" for x in (last["issues"] if last else [])[:3])
    clean = lambda s: e(re.sub("<br>", " ", s))
    cards.append(f'''<article class="ad {a["fmt"].replace(":", "x")}" data-v="{last["verdict"] if last else "none"}"><img src="img/{e(i)}.jpg" alt="{clean(a["h"])} — {clean(a.get("spec", ""))}" loading="lazy">
<div class="meta"><div class="row">{sc}<code>{e(i)}</code><span class="fmt">{"Feed 4:5" if a["fmt"] == "4:5" else "Story 9:16"}</span></div>
<p class="h">{clean(a["h"])}</p><p class="c">{clean(a.get("c", ""))}</p><p class="s">{clean(a.get("spec", ""))} · {e(a.get("price", ""))}</p>
<p class="t">Rounds: {trail or "not reviewed"} · {e(tm)}</p>{f'<details><summary>Open notes</summary><ul>{issues}</ul></details>' if issues else ""}</div></article>''')
tpl = open(f"{H}/board_template.html").read()
n = len(ads); run = sum(1 for a in ads if rev.get(a["id"]) and rev[a["id"]][-1][1]["verdict"] == "run")
page = tpl.replace("%%CARDS%%", "\n".join(cards)).replace("%%N%%", str(n)).replace("%%RUN%%", str(run))
open(f"{OUT}/index.html", "w").write(page); print(n, "ads,", run, "run")
