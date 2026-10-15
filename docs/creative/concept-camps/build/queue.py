# Builds generate_image_batch requests from frames.json: reference 1 = whole piece (still or worn), reference 2 = detail crop.
import json, sys
here = __file__.rsplit("/", 1)[0] or "."
D = json.load(open(f"{here}/frames.json")); R = json.load(open(f"{here}/refs.json"))
want = sys.argv[1].split(",")
over = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}   # optional {id: prompt} overrides for reshoots
idx = {f["id"]: f for f in D["frames"]}
reqs = []
for i, fid in enumerate(want):
    f = idx[fid]; r = R[f["camp"]]
    reqs.append({"index": i, "params": {"model": "nano_banana_pro", "resolution": "2k", "aspect_ratio": f["aspect"],
        "prompt": over.get(fid, f["prompt"]),
        "medias": [{"value": r[f["ref"]], "role": "image_references"}, {"value": r["detail"], "role": "image_references"}]}})
print(json.dumps(reqs, ensure_ascii=False))
