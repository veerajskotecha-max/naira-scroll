# Downloads every listing image and size guide from the Shopify CDN and compares each with the local file it was made from.
# Usage: cdn_compare.py ADITYA_FOLDER EMPTY_DOWNLOAD_DIR  (prints one OK/BAD line per image, then the failure count)
import json, sys, subprocess, os
from PIL import Image, ImageChops, ImageStat
root, dl = sys.argv[1], sys.argv[2]
pushed = json.load(open(f"{root}/shopify/pushed.json")); sg = json.load(open(f"{root}/shopify/sizeguide_urls.json"))
def get(url, dst):
    r = subprocess.run(["curl", "-sS", "-o", dst, "-w", "%{http_code}", url], capture_output=True, text=True)
    return r.stdout.strip()
def diff(a, b):
    A = Image.open(a).convert("RGB").resize((322, 400)); B = Image.open(b).convert("RGB").resize((322, 400))
    return sum(ImageStat.Stat(ImageChops.difference(A, B)).mean) / 3
def best_other(img, h, pos, cands):
    # nearest local export other than the expected one, to prove the match is unique
    return min((diff(img, c), os.path.basename(c)) for c in cands if c != f"{root}/exports/{h}-{pos:02d}.jpg")
allx = sorted(f"{root}/exports/{f}" for f in os.listdir(f"{root}/exports"))
bad = 0; rows = []
for p in pushed:
    for m in p["media"]:
        dst = f"{dl}/{p['handle']}-{m['position']:02d}.jpg"; code = get(m["url"], dst)
        d = diff(dst, f"{root}/{m['export']}") if code == "200" else None
        o = best_other(dst, p["handle"], m["position"], allx) if code == "200" else None
        ok = code == "200" and d < 3 and o[0] > 3 * max(d, 1)
        bad += not ok; rows.append((p["handle"], m["position"], m["key"], code, d, o, ok))
        print(f"{'OK ' if ok else 'BAD'} {p['handle']:28s} #{m['position']} {m['key']:7s} http {code}  diff {d:.2f}  next-nearest {o[1]} {o[0]:.1f}" if d is not None else f"BAD {p['handle']} #{m['position']} http {code}")
for h, url in sg.items():
    dst = f"{dl}/{h}-size-guide.jpg"; code = get(url, dst)
    d = diff(dst, f"{root}/shopify/sizeguides/{h}-size-guide.jpg") if code == "200" else None
    ok = code == "200" and d < 3; bad += not ok
    print(f"{'OK ' if ok else 'BAD'} size guide {h:28s} http {code}  diff {d:.2f}" if d is not None else f"BAD size guide {h} http {code}")
print("FAILURES:", bad)
