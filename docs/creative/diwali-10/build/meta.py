# Diwali 10 (25 Oct 2026): the Meta upload sheet and the page manifest, from copy.json.
# One row per ad file: Feed 4:5 (with the overlay), Story 9:16 (with the overlay) and the text-free Story (the A/B the account's best
# Story suggests: the ruby anaar plate ran text-free at 5.5% CTR). The primary text carries the product truth from the live listing and
# the live BUY2 / BUY3 offer; every link opens the shot's own variant. Stock and variant ids were read from Shopify on 25 Oct 2026.
# variants.json holds the regional wordings of ad 07 (Amma's for the South, Ma's for Kolkata): same plate, Feed and Story only.
# Nothing here touches Meta; the sheet is for the founder to upload when the campaign is approved.
# Usage: meta.py -> meta.csv, manifest.json
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(f"{HERE}/../../performance/build"))
from ad_copy import OFFER

CAMPAIGN = "Naira · Diwali, as it happens · 10 ads · Nov 2026"
# n -> (handle, variant id or None, units for that variant (or the product), ad set, flight)
SHOP = {
 "01": ("baguette-tennis-necklace", 50651962409122, 20, "Diwali night", "29 Oct – 8 Nov"),
 "02": ("prism-riviere-bracelet", None, 67, "Diwali night", "29 Oct – 8 Nov"),
 "03": ("baguette-tennis-bracelet", 50651931738274, 29, "Diwali night", "29 Oct – 10 Nov"),
 "04": ("toggle-link-chain", None, 79, "Gifting", "29 Oct – 5 Nov"),
 "05": ("woven-gold-hoops", None, 63, "Gifting", "29 Oct – 6 Nov (so he can still order in time for Bhai Dooj)"),
 "06": ("cushion-halo-ring", None, 60, "Diwali night", "1 Nov – 8 Nov"),
 "07": ("bold-nocturne-chain", None, 53, "Gifting", "29 Oct – 8 Nov"),
 "08": ("baguette-huggies", None, 57, "Gifting", "29 Oct – 5 Nov"),
 "09": ("verdant-eternity-band", None, 60, "Diwali night", "29 Oct – 6 Nov"),
 "10": ("bold-nocturne-bracelet", None, 49, "Diwali night", "3 Nov – 8 Nov"),
}
# the product truth, from the live listing descriptions (25 Oct 2026): gold tone or silver tone, cubic zirconia, never real or diamond
TRUTH = {
 "01": "Deep ruby-red baguette cubic zirconia set crosswise, edge to edge, each held at its four corners by 18k gold-tone claws: a 36 cm "
       "choker line that sits at the base of the neck. The Baguette Tennis Necklace in Ruby, ₹2,300. Also in Crystal and Emerald.",
 "02": "Aqua, pink and pale-yellow cubic zirconia, about 5 mm each, every stone framed in its own halo of tiny pavé, in one 18 cm line of "
       "rhodium silver tone. The Prism Rivière Bracelet, ₹2,399.",
 "03": "Let them. Every clear baguette sits in its own gold-tone box setting, held by four claws, edge to edge for 17 cm, with a box clasp "
       "and a fold-over safety. The Baguette Tennis Bracelet in Crystal, ₹1,699. Also in Ruby and Emerald.",
 "04": "A 50 cm chain of open paperclip links in 18k gold tone that fastens at the front with a round ring and a short pavé bar, so the "
       "clasp is part of the look. The Toggle Link Chain, ₹1,299. Gifting more than one?",
 "05": "Hoops 25 mm across, each a thick braid of gold-tone strands with raised ridges, and no stones at all. The Woven Gold Hoops, "
       "₹1,299 a pair. Forward this to your brother. Consider it the hint.",
 "06": "One 8 mm round clear cubic zirconia in four claws, inside a cushion-shaped halo of tiny pavé, with pavé down both shoulders. "
       "Rhodium silver tone; the open back adjusts to fit US 5 to 7. The Cushion Halo Ring, ₹1,199.",
 "07": "Bold oval links in polished 18k gold tone, about 11.7 mm wide, with one link set all over in clear cubic zirconia; 46 cm with a "
       "5 cm extender. The Bold Nocturne Chain, ₹1,799.",
 "08": "The same 15 mm gold-tone huggies for everyone, one row of baguette cubic zirconia along the front, in ruby red, crystal, emerald "
       "green or amethyst. The Baguette Huggies, ₹1,199 a pair.",
 "09": "Oval green cubic zirconia, about 5 by 4 mm, claw-set all the way round, each cradled in a scalloped line of tiny clear pavé. "
       "Rhodium silver tone; the open back adjusts to fit US 5 to 8. The Verdant Eternity Band, ₹1,099.",
 "10": "Diwali falls on amavasya, the night with no moon. Chunky oval links in polished 18k gold tone, one of them set all over in clear "
       "cubic zirconia; 20 cm with a 3 cm extender. The Bold Nocturne Bracelet, ₹1,599.",
}
# where each wording runs; ads without an entry run in every city of their ad set
GEO = {"07": "every city; if the regional versions run, every city except Bengaluru, Chennai, Hyderabad and Kolkata",
       "07b": "Bengaluru, Chennai and Hyderabad", "07c": "Kolkata"}
COLS = ["ad", "file", "product", "line", "placement", "variant", "primary_text", "headline", "cta", "url", "campaign", "adset", "flight",
        "geo", "stock"]

def entry(e):
    handle, vid, stock, adset, flight = SHOP[e["n"][:2]]; base = f"{e['n']}-{e['key']}"
    url = (f"https://www.nairaflore.com/products/{handle}?" + (f"variant={vid}&" if vid else "") +
           f"utm_source=meta&utm_medium=paid&utm_campaign=diwali10_nov26&utm_content={base}")
    head = " · ".join(x for x in (e["title"], e.get("variant") if e["n"] != "08" else "4 colours", e["price"].replace(" a pair", "")) if x)
    return dict(n=e["n"], base=base, handle=handle, variant_id=vid, stock=stock, adset=adset, flight=flight, url=url, line=e["line"],
                headline=head, primary_text=f"{e['line']} {TRUTH[e['n'][:2]]}\n\n{OFFER}", geo=GEO.get(e["n"], ""))

def main():
    L = json.load(open(f"{HERE}/copy.json")); V = json.load(open(f"{HERE}/variants.json")); rows, man = [], []
    for e in L + V:
        a = entry(e); man.append(dict(e, **a, variant_of=e["n"][:2] if e in V else None))
        places = (("feed", "feed"), ("story", "story")) + ((("story (text-free A/B)", "story-clean"),) if e not in V else ())
        for place, suffix in places:
            rows.append(dict(ad=f"{a['base']}-{suffix}", file=f"ads/{a['base']}-{suffix}.jpg", product=e["title"], line=e["line"],
                             placement=place, variant=e.get("variant") or "", primary_text=a["primary_text"], headline=a["headline"],
                             cta="SHOP_NOW", url=a["url"], campaign=CAMPAIGN, adset=a["adset"], flight=a["flight"], geo=a["geo"],
                             stock=a["stock"]))
    with open(f"{HERE}/meta.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); [w.writerow(r) for r in rows]
    json.dump(man, open(f"{HERE}/manifest.json", "w"), indent=1, ensure_ascii=False)
    print(len(rows), "rows,", len(L), "ads,", len(V), "regional wordings")

if __name__ == "__main__":
    main()
