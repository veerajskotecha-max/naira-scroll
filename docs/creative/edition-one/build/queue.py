# Builds generate_image_batch requests for Edition One frames: reference 1 = listing-1 (the pair), reference 2 = listing-5 (macro).
# Usage: queue.py ID1,ID2 [overrides.json]     (ids like aqua1, halo4)
import json, sys, os
here = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(f"{here}/frames.json")); M = json.load(open(f"{here}/media_ids.json"))
over = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
idx = {f["id"]: f for f in D["frames"]}
reqs = []
for i, fid in enumerate(sys.argv[1].split(",")):
    f = idx[fid]; k = f["camp"]
    ref1 = M[f"{k}_4"] if (k == "papillon" and f["ref"] == "worn") else M[f"{k}_1"]
    reqs.append({"index": i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": f["aspect"],
        "prompt": over.get(fid, f["prompt"]),
        "medias": [{"value": ref1, "role": "image_references"}, {"value": M[f"{k}_5"], "role": "image_references"}]}})
print(json.dumps(reqs, ensure_ascii=False))
