"""Merge every saved show_generations page into one library.json (dedup by id, newest first)."""
import json, glob, sys
from pathlib import Path
out = Path(sys.argv[1]); files = sorted(glob.glob(sys.argv[2]))
seen, items = {}, []
for f in files:
    try: d = json.load(open(f))
    except Exception as e: print("skip", f, e); continue
    for it in d.get("items", []):
        if it["id"] in seen or it.get("status") != "completed": continue
        p = it.get("params", {}) or {}
        r = it.get("results", {}) or {}
        med = p.get("medias") or []
        seen[it["id"]] = 1
        items.append({"id": it["id"], "t": it["createdAt"], "model": it.get("model"), "ar": p.get("aspect_ratio"),
                      "w": p.get("width"), "h": p.get("height"), "prompt": p.get("prompt", ""),
                      "refs": [m.get("value") or m.get("id") for m in med if isinstance(m, dict)],
                      "raw": r.get("rawUrl"), "min": r.get("minUrl"), "liked": it.get("liked", False)})
items.sort(key=lambda x: -x["t"])
json.dump(items, open(out, "w"))
print(len(files), "pages", len(items), "images", "oldest", items[-1]["t"] if items else None)
