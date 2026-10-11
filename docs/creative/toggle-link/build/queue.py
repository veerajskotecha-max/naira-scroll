# Builds generate_image_batch requests from shots.json: reference 1 = listing photo (still or worn), reference 2 = clasp.
import json, sys
here = __file__.rsplit("/", 1)[0]
S = json.load(open(f"{here}/shots.json")); M = json.load(open(f"{here}/refs/media.json"))
want = sys.argv[1].split(",") if len(sys.argv) > 1 else [s["id"] for s in S]
reqs = []
for s in S:
    if s["id"] not in want: continue
    reqs.append({"index": int(s["id"][1:]), "params": {"model": "nano_banana_pro", "resolution": "2k",
        "aspect_ratio": s["aspect"], "prompt": s["prompt"],
        "medias": [{"value": M[s["ref"]], "role": "image_references"}, {"value": M["clasp"], "role": "image_references"}]}})
print(json.dumps(reqs, ensure_ascii=False))
