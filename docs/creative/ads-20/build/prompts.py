# Assembles each ad's Higgsfield request from a set file (shot, lock, scale, skin + the set's common scene, light and negatives)
# and prints the generate_image_batch requests as JSON. Usage: prompts.py set1.json [key ...]
import json, os, sys

def requests(path, keys=None, start=0):
    s = json.load(open(path)); c = s["common"]; out = []
    for i, a in enumerate(x for x in s["ads"] if not keys or x["key"] in keys):
        p = " ".join([a["shot"], a["lock"], a["scale"], a["skin"], a.get("scene") or c.get("scene", ""), a.get("light") or c["light"], a.get("neg") or c["neg"]])
        out.append({"index": start + i, "key": a["key"], "params": {"model": c["model"], "resolution": c["resolution"],
                    "aspect_ratio": a.get("aspect_ratio", c["aspect_ratio"]), "prompt": p,
                    "medias": [{"value": a["ref"], "role": "image_references"}]}})
    return out

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    r = requests(os.path.join(here, sys.argv[1]), sys.argv[2:] or None)
    print(json.dumps([{"index": x["index"], "params": x["params"]} for x in r], ensure_ascii=False))
    for x in r: print(x["index"], x["key"], len(x["params"]["prompt"]), "chars", file=sys.stderr)
