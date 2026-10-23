# Colour-coded 50: the Meta upload sheet, one row per ad (Feed and Story of each shot), in the columns of meta.csv.
# The Story carries no words, so the line, the product truth and the offer live in the primary text; the URL opens the shot's
# own variant. Handles, variant ids and stock were read from Shopify on 23 Oct 2026 (read-only).
# Usage: colour_meta.py -> colour_meta.csv
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from ad_copy import OFFER

# shot -> (Shopify handle, variant id or None, units in stock for that variant, ad set)
SHOP = {
    "01": ("toggle-link-chain", None, 79, "Necklaces & rings"), "02": ("baguette-tennis-necklace", 50651962441890, 30, "Necklaces & rings"),
    "03": ("prism-riviere-bracelet", None, 67, "Bracelets"), "04": ("woven-gold-hoops", None, 63, "Earrings"),
    "05": ("verdant-eternity-band", None, 60, "Necklaces & rings"), "06": ("cushion-halo-ring", None, 60, "Necklaces & rings"),
    "07": ("baguette-tennis-bracelet", 50651931738274, 29, "Bracelets"), "08": ("baguette-huggies", 50651968995490, 15, "Earrings"),
    "09": ("bold-nocturne-chain", None, 54, "Necklaces & rings"), "10": ("bold-nocturne-bracelet", None, 50, "Bracelets"),
    "11": ("halo-curve-ring", None, 45, "Necklaces & rings"), "12": ("kiss-knot-bangle", 50651938881698, 20, "Bracelets"),
    "13": ("silk-mesh-cuff", 50651894546594, 20, "Bracelets"), "14": ("marquise-layering-set", None, 40, "Necklaces & rings"),
    "15": ("ribbon-bead-bracelet", None, 35, "Bracelets"), "16": ("brushed-gold-huggies", None, 35, "Earrings"),
    "17": ("riviere-eternal-bracelet", None, 34, "Bracelets"), "18": ("lilac-papillon-ring", None, 30, "Necklaces & rings"),
    "19": ("aqua-heart-drops-silver", None, 30, "Earrings"), "20": ("prism-cluster-studs-silver", None, 30, "Earrings"),
    "21": ("molten-panel-bracelet", None, 30, "Bracelets"), "22": ("torsade-pearl-cuff", None, 30, "Bracelets"),
    "23": ("baguette-halo-drops", None, 30, "Earrings"), "24": ("verdant-cushion-studs", None, 30, "Earrings"),
    "25": ("quatrefoil-eclat-studs", None, 30, "Earrings"), "26": ("bold-dome-huggies", None, 30, "Earrings"),
    "27": ("torsade-huggies", None, 29, "Earrings"), "28": ("baguette-eternity-band", 50651962048674, 7, "Necklaces & rings"),
    "29": ("heartbead-bracelet", None, 25, "Bracelets"), "30": ("serpentine-whisper-chain-silver", None, 23, "Necklaces & rings"),
    "31": ("baroque-shell-bracelet", None, 23, "Bracelets"), "32": ("petite-square-huggies", None, 22, "Earrings"),
    "33": ("riviere-huggies-silver", None, 21, "Earrings"), "34": ("emerald-square-ear-cuff", None, 20, "Earrings"),
    "35": ("pear-point-open-cuff", None, 20, "Bracelets"), "36": ("bold-nocturne-drops", None, 20, "Earrings"),
    "37": ("marquise-drop-choker", None, 20, "Necklaces & rings"), "38": ("droplet-open-cuff", 50651971190946, 10, "Bracelets"),
    "39": ("petal-flower-studs", 50651971125410, 10, "Earrings"), "40": ("fine-tennis-bracelet", None, 20, "Bracelets"),
    "41": ("duo-link-bracelet", None, 20, "Bracelets"), "42": ("mint-pear-drop-earrings", None, 20, "Earrings"),
    "43": ("north-star-bangle", 50651938816162, 10, "Bracelets"), "44": ("droplet-open-ring", 50651931869346, 10, "Necklaces & rings"),
    "45": ("marquise-wheat-cuff", None, 20, "Bracelets"), "46": ("triple-coil-wrap-bangle", 50651931639970, 10, "Bracelets"),
    "47": ("garnet-cable-cuff", None, 20, "Bracelets"), "48": ("charm-box-chain", None, 20, "Necklaces & rings"),
    "49": ("serpentine-whisper-chain", None, 20, "Necklaces & rings"), "50": ("baguette-tennis-necklace", 50651962474658, 20, "Necklaces & rings"),
}

# the product truth, one sentence each: gold tone or silver tone, cubic zirconia, white shell pearl, as the listings say
TRUTH = {
    "01": "A 50 cm paperclip chain in 18k gold tone that closes with a pavé bar through a ring.",
    "02": "One line of clear baguette cubic zirconia that sits right at the base of the neck.",
    "03": "Aqua, pink and yellow cubic zirconia, each in its own pavé halo, in rhodium silver tone.",
    "04": "25 mm hoops of braided rope in 18k gold tone. No stones, all texture.",
    "05": "Emerald-green oval cubic zirconia along a wave of pavé, in rhodium silver tone.",
    "06": "An 8 mm round cubic zirconia in a cushion halo, pavé down the shoulders, in rhodium silver tone.",
    "07": "Clear baguette cubic zirconia, lined up edge to edge in 18k gold-tone claws.",
    "08": "Emerald-green baguette cubic zirconia across the front of a 15 mm hinged huggie, in 18k gold tone.",
    "09": "Chunky 18k gold-tone links and one link set all over in pavé.",
    "10": "Chunky 18k gold-tone links and one link set in pavé.",
    "11": "A tiger's eye and a champagne crystal, side by side on an open 18k gold-tone band.",
    "12": "A flexible ribbed bangle whose ends cross in one polished X, in 18k gold tone.",
    "13": "A 19 mm tube of fine woven mesh with mirror-polished end caps, in 18k gold tone.",
    "14": "A 40 cm marquise solitaire and a 45 cm Y-lariat, made to be worn together.",
    "15": "A small crystal bow on a fine 18k gold-tone chain.",
    "16": "Small huggie hoops with a satin-brushed finish in 18k gold tone.",
    "17": "One fine line of clear cubic zirconia with a polished buckle clasp.",
    "18": "A gold-tone butterfly whose wings are set edge to edge in lilac pavé.",
    "19": "A curve of clear brilliants with an icy aqua heart below, rhodium silver tone.",
    "20": "Purple, pink and yellow cubic zirconia in one small arc, with tiny pearls.",
    "21": "Small oval plates laid in rows like kernels, in satin-polished 18k gold tone.",
    "22": "Two white shell pearls at the ends of a twisted 18k gold-tone cuff, with pavé collars.",
    "23": "A 14 mm sunburst of clear baguettes around a small pearl, with a white pearl drop below.",
    "24": "An emerald-green cushion cubic zirconia in a sunburst halo of clear stones, rhodium silver tone.",
    "25": "A 15 mm four-point star in clear cubic zirconia: a pavé outline, four pear stones and a round centre.",
    "26": "16 mm dome huggies in mirror-polished 18k gold tone, with a hinged snap.",
    "27": "20 mm huggies with a fine twisted rope texture all the way round, in 18k gold tone.",
    "28": "Ruby-red baguette cubic zirconia set crosswise all the way round, each held by small 18k gold-tone claws.",
    "29": "6 mm mirror-polished steel beads, a gold-tone toggle and one puffed gold-tone heart.",
    "30": "A 2 mm snake chain with one 10 mm cushion-cut clear cubic zirconia in a four-prong basket, in rhodium silver tone.",
    "31": "Flat baroque white shell pearls, each a different shape, with small gold-tone beads between and one pearl drop on the toggle.",
    "32": "Squared huggies in polished 18k gold tone, with four tiny white pearls on each, two on each side.",
    "33": "Open hoops made of one row of slightly oval clear cubic zirconia, each in a beaded cup, in rhodium silver tone.",
    "34": "No piercing needed: a polished 18k gold-tone cuff with one square emerald-green cubic zirconia in four claws.",
    "35": "A slim open cuff in 18k gold tone with one pear-cut clear cubic zirconia at each end.",
    "36": "A polished oval link on a post with a larger pavé oval link below, in 18k gold tone.",
    "37": "A ribbed snake collar with a sideways marquise cubic zirconia and a fine 6 cm drop of two pear stones, in 18k gold tone.",
    "38": "An open cuff of polished 18k gold-tone wire, a ball at one end and a teardrop at the other. No stones.",
    "39": "Three round clear cubic zirconia and one pear below, around a polished 18k gold-tone centre.",
    "40": "One continuous row of small round clear cubic zirconia, each in its own gold-tone claw cup, with a box clasp.",
    "41": "Long oval links in gold tone and silver tone, joined by small stacked gold-tone rings.",
    "42": "Three small clear pear-cut cubic zirconia leading down to one pale mint-green pear, in fine 18k gold-tone claws.",
    "43": "A slim mirror-polished bangle in 18k gold tone: engraved north stars alternating with round clear cubic zirconia.",
    "44": "An adjustable open ring in polished silver tone, a round ball at one end and a teardrop at the other.",
    "45": "Clear marquise cubic zirconia set in two slanting rows on an 18k gold-tone coil cuff, with a polished ball at each end.",
    "46": "One ribbed snake-coil wire that wraps the wrist twice, each end capped in clear pavé, in 18k gold tone.",
    "47": "A twisted silver-tone cable cuff with gold-tone pavé ends and one round garnet-red stone at each tip.",
    "48": "A 50 cm fine box chain in 18k gold tone with one barrel charm set all round in clear cubic zirconia.",
    "49": "A 2 mm snake chain with one 10 mm cushion-cut clear cubic zirconia in a four-prong basket, in 18k gold tone.",
    "50": "Emerald-green baguette cubic zirconia, edge to edge on a 36 cm choker line in 18k gold-tone claws.",
}

def main():
    L = json.load(open(f"{HERE}/colour50.json"))
    cols = ["ad", "product", "format", "placement", "variant", "reserve", "primary_text", "headline", "cta", "url", "campaign", "adset", "wave"]
    with open(f"{HERE}/colour_meta.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for e in L:
            handle, vid, stock, adset = SHOP[e["n"]]; base = os.path.basename(e["plate"])[:-4]
            url = f"https://www.nairaflore.com/products/{handle}?" + (f"variant={vid}&" if vid else "") + \
                  f"utm_source=meta&utm_medium=paid&utm_campaign=perf_oct26_colour&utm_content={base}"
            head = " · ".join(x for x in (e["title"], e.get("variant"), e["price"]) if x)
            pt = f"{e['line']} {TRUTH[e['n']]} The {e['title']}, {e['price']}.\n\n{OFFER}"
            for t in ("feed", "story"):
                w.writerow(dict(ad=f"{base}-{t}", product=e["title"], format="colour", placement=t, variant=e.get("variant") or "",
                                reserve="", primary_text=pt, headline=head, cta="SHOP_NOW", url=url,
                                campaign="PERF · Colour 50 (least graphics) · Oct 2026", adset=adset, wave=1))
    print(2 * len(L), "rows")

if __name__ == "__main__":
    main()
