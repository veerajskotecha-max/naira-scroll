# Builds the "Naira Stories" artifact: all 21 Edition Two Stories (1080×1920) with a download button each, a download-all ZIP
# (packed in the browser), and the caption and link-sticker URL to post with each one. Stories come from e2/out (built by
# build_ads.py from e2_ads.json); captions and links from e2/meta_copy.json.
# Usage: e2_stories.py     writes <scratchpad>/e2stories/site/ (index.html, s/<id>.jpg full size, st/<id>.jpg thumbnails)
import ast, base64, json, os, re, shutil
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/e2stories"; SITE = f"{OUT}/site"
TITLE = {"Prism Rivière": "Prism Rivière Bracelet"}

def main():
    for d in ("s", "st"): os.makedirs(f"{SITE}/{d}", exist_ok=True)
    ads = json.load(open(f"{HERE}/e2_ads.json", encoding="utf-8"))["ads"]; meta = json.load(open(f"{HERE}/e2/meta_copy.json", encoding="utf-8"))
    flat = lambda t: re.sub(r"<[^>]+>", "", re.sub(r"\s*<br>\s*", " ", t))
    timing = ast.literal_eval(re.search(r"TIMING = (\{.*?\})\n", open(f"{HERE}/e2/tools/board.py").read(), re.S).group(1))
    ids = {a["id"] for a in ads}; stories = []
    for a in ads:                                        # Feed order, so each Story sits where its Feed ad does
        if a["fmt"] != "4:5" or a["id"] + "-story" not in ids: continue
        sid = a["id"] + "-story"; src = f"{HERE}/e2/out/{sid}.jpg"; m = meta[a["id"]]
        shutil.copyfile(src, f"{SITE}/s/{sid}.jpg")
        im = Image.open(src).convert("RGB"); im.resize((360, 640), Image.LANCZOS).save(f"{SITE}/st/{sid}.jpg", quality=82, optimize=True, progressive=True)
        prod = a["spec"].split(" · ")[0]
        stories.append(dict(id=sid, title=TITLE.get(prod, prod), price=a["price"], tag=a.get("tag", ""), hook=flat(a["h"]),
                            caption=m["primary"], url=m["url"], when=next((v for k, v in timing.items() if a["id"].startswith(k)), "Now"), t=f"st/{sid}.jpg", f=f"s/{sid}.jpg", file=f"Naira-Story-{sid.replace('-story', '')}.jpg"))
    b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
    page = (open(f"{HERE}/e2_stories_template.html", encoding="utf-8").read().replace("__VELISTA__", b64(f"{HERE}/brand/Velista.ttf"))
            .replace("__DATA__", json.dumps(dict(stories=stories), ensure_ascii=False).replace("</", "<\\/")))
    open(f"{SITE}/index.html", "w", encoding="utf-8").write(page)
    files = [x["t"] for x in stories] + [x["f"] for x in stories]
    json.dump([{"path": p} for p in files], open(f"{OUT}/files.json", "w"))
    print(len(stories), "stories,", round(sum(os.path.getsize(f"{SITE}/{p}") for p in files) / 1e6, 1), "MB")

if __name__ == "__main__":
    main()
