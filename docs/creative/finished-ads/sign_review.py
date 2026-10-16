# Snapshots each ad's settings as the reviewer saw them, so the contact sheet shows a score only for the exact version reviewed.
# Run right after a review lands. Usage: sign_review.py review_rN.json
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
review = sys.argv[1] if os.path.isabs(sys.argv[1]) else os.path.join(HERE, sys.argv[1])
ads = json.load(open(f"{HERE}/ads.json"))["ads"]
sig = {a["id"]: json.dumps({k: v for k, v in a.items() if k not in ("id", "src")}, sort_keys=True, ensure_ascii=False) for a in ads}
json.dump(sig, open(review[:-5] + ".sig.json", "w"), indent=1, ensure_ascii=False); print("signed", len(sig), "ads for", os.path.basename(review))
