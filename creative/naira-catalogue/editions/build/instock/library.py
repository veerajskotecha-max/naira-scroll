"""products.json (live Shopify feed) -> library.json: every Naira Petite piece that is in stock today.
Pre-order pieces are left out (they are available to order but not in stock)."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
P = json.load(open(D / "products.json"))["products"]
TYPES = {"Earrings": "Earrings", "Ring": "Ring", "Necklace": "Necklace", "Bracelet": "Bracelet"}
GRID_OVERRIDE = {"riviere-eternal-bracelet": D / "raw" / "b0ddc22f.png"}   # the only shop photos are worn and a size card
# rings made in one size: no Size option and not adjustable; the size is in the listing's Details
FIXED_SIZE = {"vintage-halo-ring": "US 6, fixed", "pearl-ribbon-ring": "US 7, fixed",
              "chevron-whisper-ring": "US 7, fixed", "whisper-pave-band": "US 6½, fixed"}


def text(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h or "")).strip()


def metal(p, body):
    tags = p["tags"]
    opt = {o["name"]: o["values"] for o in p["options"]}
    if len(opt.get("Metal", [])) > 1:
        return "18k gold or rhodium"
    if "Rose Gold Tone" in tags:
        return "Rose gold coated"
    if "Tri Tone" in tags:
        return "Three-tone coated"
    if "Two Tone" in tags:
        return "Gold and rhodium coated"
    if any(t.startswith("Rhodium") for t in tags) or re.search(r"Plating: PVD rhodium", body):
        return "Rhodium coated"
    return "18k gold coated"


def extras(p):
    """Short words for the price line: sizes, stones, colours, months."""
    av = [v for v in p["variants"] if v["available"]]
    out = []
    for i, o in enumerate(p["options"]):
        vals = []
        for v in av:
            x = v[f"option{i + 1}"]
            if x not in vals:
                vals.append(x)
        if o["name"] == "Size":
            nums = sorted(int(x) for x in vals if str(x).isdigit())
            if nums:
                out.append(f"US {nums[0]} to {nums[-1]}" if len(nums) > 1 else f"US {nums[0]}")
        elif o["name"] == "Stone" and len(vals) > 1:
            out.append(f"{len(vals)} stones")
        elif o["name"] == "Colour" and len(vals) > 1:
            out.append(" or ".join(v.lower() for v in vals))
        elif o["name"] == "Month" and len(vals) > 1:
            out.append(f"{len(vals)} birthstones")
    return " · ".join(out)


lib = {}
for p in P:
    if p["vendor"] != "Naira Petite" or p["product_type"] not in TYPES or "pre-order" in p["tags"]:
        continue
    av = [v for v in p["variants"] if v["available"]]
    if not av:
        continue
    body = text(p["body_html"])
    prices = sorted(set(float(v["price"]) for v in av))
    stones = []
    if "Pearl" in p["tags"]:
        stones.append("shell pearl" if re.search(r"shell pearl", body, re.I) else "pearl")
    if "Cubic Zirconia" in p["tags"]:
        stones.append("cubic zirconia")
    waterproof = "Waterproof" in p["tags"]
    grid = GRID_OVERRIDE.get(p["handle"], D / "shop" / p["handle"] / "0.jpg")
    fit, ext = None, extras(p)
    # which option moves the price above the lowest one (the "from" in the price list)
    from_by = [o["name"].lower() for i, o in enumerate(p["options"])
               if {v[f"option{i + 1}"] for v in av if float(v["price"]) == prices[0]} != {v[f"option{i + 1}"] for v in av}]
    if p["product_type"] == "Ring":
        sized = any(o["name"] == "Size" for o in p["options"])
        fit = "sized" if sized else "adjustable" if "Adjustable" in p["tags"] else "fixed"
        if fit == "fixed":
            assert p["handle"] in FIXED_SIZE, f"{p['handle']}: one-size ring, add its size to FIXED_SIZE"
            ext = " · ".join(x for x in (ext, FIXED_SIZE[p["handle"]]) if x)
    lib[p["handle"]] = {
        "handle": p["handle"], "title": p["title"], "type": TYPES[p["product_type"]], "price": prices[0], "from": len(prices) > 1, "from_by": from_by if len(prices) > 1 else [],
        "metal": metal(p, body), "stones": stones, "waterproof": waterproof,
        "hypoallergenic": "Hypoallergenic" in p["tags"] or bool(re.search(r"hypoallergenic", body, re.I)),
        "extras": ext, "fit": fit, "url": f"https://nairaflore.com/products/{p['handle']}", "grid": str(grid), "tags": p["tags"],
        "published": p["published_at"][:10],
    }
json.dump(lib, open(D / "library.json", "w"), indent=1, ensure_ascii=False)
if __name__ == "__main__":
    from collections import Counter
    print(len(lib), "pieces in stock:", dict(Counter(v["type"] for v in lib.values())),
          "| keep dry:", sum(not v["waterproof"] for v in lib.values()), "| hypoallergenic:", sum(v["hypoallergenic"] for v in lib.values()))
