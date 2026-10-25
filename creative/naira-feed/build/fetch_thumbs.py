"""Download the small webp of every library image that is not already on disk (safe to re-run)."""
import json, sys, os, concurrent.futures as cf, urllib.request
from pathlib import Path
lib = json.load(open(sys.argv[1])); out = Path(sys.argv[2]); out.mkdir(exist_ok=True)
todo = [(x["id"], x["min"] or x["raw"]) for x in lib if x.get("min") or x.get("raw")]
todo = [(i, u) for i, u in todo if not (out / (i + ".webp")).exists()]
def get(iu):
    i, u = iu
    try:
        with urllib.request.urlopen(u, timeout=60) as r: (out / (i + ".webp")).write_bytes(r.read()); return 1
    except Exception as e: return 0
with cf.ThreadPoolExecutor(16) as ex: n = sum(ex.map(get, todo))
print("downloaded", n, "of", len(todo))
