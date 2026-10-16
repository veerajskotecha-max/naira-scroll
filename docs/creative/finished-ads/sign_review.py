# Snapshots each ad's settings as the reviewer saw them, so the contact sheet and PDF show a score only for the exact version
# reviewed. Run right after a review lands. Usage: sign_review.py review_rN.json [--cfg controls.json] [--only id,id,...]
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]; cfg = "ads.json"; only = None
if "--cfg" in args: i = args.index("--cfg"); cfg = args[i + 1]; del args[i:i + 2]
if "--only" in args: i = args.index("--only"); only = set(args[i + 1].split(",")); del args[i:i + 2]
review = args[0] if os.path.isabs(args[0]) else os.path.join(HERE, args[0])
ads = json.load(open(f"{HERE}/{cfg}"))["ads"]
sig = {a["id"]: json.dumps({k: v for k, v in a.items() if k not in ("id", "src")}, sort_keys=True, ensure_ascii=False)
       for a in ads if only is None or a["id"] in only}
json.dump(sig, open(review[:-5] + ".sig.json", "w"), indent=1, ensure_ascii=False); print("signed", len(sig), "for", os.path.basename(review))
