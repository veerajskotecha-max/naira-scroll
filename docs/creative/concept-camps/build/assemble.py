# One command from verdicts to deliverables: picks the verified frames of the four concept camps and Edition One, builds every
# PDF, writes 1200px web and full-size JPGs, and builds the board page. Output: <SITE> (index.html, web/, full/, pdfs/).
# Usage: assemble.py
import json, os, shutil, subprocess, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
E1 = os.path.normpath(os.path.join(HERE, "..", "..", "edition-one", "build"))
SPB = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad"
SITE = f"{SPB}/site"
def run(*a):
    r = subprocess.run([sys.executable, *a], capture_output=True, text=True)
    print(r.stdout.strip()[-1500:]); r.stderr.strip() and print(r.stderr.strip()[-800:])
    if r.returncode: sys.exit(r.returncode)

for d in ["web", "full", "pdfs"]: os.makedirs(f"{SITE}/{d}", exist_ok=True)
run(f"{HERE}/select.py", f"{SPB}/c4/final.json")
run(f"{E1}/select_e1.py", f"{SPB}/e1/final_e1.json")
shutil.rmtree(f"{SPB}/c4/pdf_out", ignore_errors=True); shutil.rmtree(f"{SPB}/e1/pdf_out", ignore_errors=True)
run(f"{HERE}/pdfs.py", f"{SPB}/c4/final.json", f"{SPB}/c4/pdf_out")
run(f"{E1}/pdfs_e1.py", f"{SPB}/e1/final_e1.json", f"{SPB}/e1/pdf_out")

sel = json.load(open(f"{SPB}/c4/final.json")); sel1 = json.load(open(f"{SPB}/e1/final_e1.json"))
pdfs = {}
for f in sorted(os.listdir(f"{SPB}/c4/pdf_out")):
    shutil.copy(f"{SPB}/c4/pdf_out/{f}", f"{SITE}/pdfs/{f}")
    for camp in ["toggle", "woven", "heart", "prism"]:
        key = {"toggle": "Toggle", "woven": "Woven", "heart": "Heartbead", "prism": "Prism"}[camp]
        if f.startswith("Naira-Camp-") and key in f: pdfs[camp] = f
    if "Board" in f: pdfs["board"] = f
for f in os.listdir(f"{SPB}/e1/pdf_out"):
    shutil.copy(f"{SPB}/e1/pdf_out/{f}", f"{SITE}/pdfs/{f}"); pdfs["e1"] = f
json.dump(pdfs, open(f"{SITE}/pdfs.json", "w"), indent=1)

def jpgs(items, plates):
    for it in items:
        im = Image.open(f"{plates}/{it['file']}").convert("RGB")
        im.save(f"{SITE}/full/{it['id']}.jpg", quality=90, subsampling=0)
        s = 1200 / im.width
        im.resize((1200, round(im.height * s)), Image.LANCZOS).save(f"{SITE}/web/{it['id']}.jpg", quality=82)
for items in sel.values(): jpgs(items, f"{SPB}/c4/plates")
for items in sel1.values(): jpgs(items, f"{SPB}/e1/plates")

n4 = sum(len(v) for v in sel.values()); n1 = sum(len(v) for v in sel1.values())
stats = dict(note=(f"{n4 + n1} photographs passed: {n4} across the four concept camps and {n1} for Edition One. Each was checked by an "
                   "independent reviewer against the listing photos for construction, stones, metal, scale against a real object, no face "
                   "and no text, then scored as an ad; only frames scoring 8.5 of 10 or more are shown."),
             dataLede=("Naira's Meta account, every jewellery ad to 12 Oct 2026 (108 ads, ₹1.59 lakh), spend-weighted and corrected for "
                       "nine friends-and-family orders. Concept-led ads beat plain ones, but one image carries much of the lead."),
             data=[["1.44×", "ROAS on concept statics, against 0.57× on plain statics"],
                   ["10 of 10", "side-by-side ad sets where concept won outbound click-through"],
                   ["1.63×", "Prism Rivière concept ads: 12 of the 16 concept sales"],
                   ["1.79×", "concept statics in the 4:5 Instagram Feed; Stories 1.36×"]])
json.dump(stats, open(f"{SITE}/stats.json", "w"), indent=1, ensure_ascii=False)
run(f"{HERE}/build_page.py", f"{SPB}/c4/final.json", SITE, f"{SPB}/e1/final_e1.json")
tot = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(SITE) for f in fs)
print("site", round(tot / 1e6, 1), "MB;", n4, "+", n1, "frames")
