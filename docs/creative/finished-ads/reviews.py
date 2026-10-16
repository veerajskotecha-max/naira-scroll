# Merges every review round: for each ad, the newest review whose snapshot matches the ad's current settings.
# Usage: from reviews import current; current("review", ads) -> {id: review entry}
import glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
def adsig(a): return json.dumps({k: v for k, v in a.items() if k not in ("id", "src")}, sort_keys=True, ensure_ascii=False)
def current(prefix, ads):
    files = sorted((f for f in glob.glob(f"{HERE}/{prefix}_r*.json") if re.search(r"_r\d+\.json$", f)),
                   key=lambda f: int(re.search(r"_r(\d+)\.json$", f).group(1)))
    now = {a["id"]: adsig(a) for a in ads}; out = {}
    for f in files:
        sf = f[:-5] + ".sig.json"
        if not os.path.exists(sf): continue
        sig = json.load(open(sf))
        for r in json.load(open(f)):
            if sig.get(r["id"]) is not None and sig.get(r["id"]) == now.get(r["id"]): out[r["id"]] = r
    return out
