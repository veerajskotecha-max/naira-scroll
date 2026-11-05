# Writes ../plan.json: the campaign setup, rules, flags, the high-CTR sources and the live account snapshot the board shows.
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
concepts = json.load(open(os.path.join(ROOT, "research/concepts.json")))
final = concepts["final"]
def slug(s, n=26):
    words, out = [w for w in re.sub(r"[^a-z0-9]+", " ", s.lower().replace("'", "")).split()], []
    for w in words:
        if len("_".join(out + [w])) > n: break
        out.append(w)
    return "_".join(out)
slugs = {c["no"]: slug(c["name"]) for c in final}
JP = os.path.join(ROOT, "research/judging.json")
picked = {p["no"]: p.get("photos", []) for p in json.load(open(JP))["pick"]["picks"]} if os.path.exists(JP) else None
def used(keys):
    pool = picked.items() if picked else ((c["no"], c["photos"]) for c in final)
    return ", ".join(sorted(no for no, ph in pool if any(any(k in p for k in keys) for p in ph))) or "not in the ten"
sources = [
 ("'Almost edible.' Prism Rivière Bracelet in a bowl of sugared sweets", "6.21% CTR Story, 5.61% Feed; 10 sales, the account's best-selling concept ad", used(["H01"])),
 ("'Rangoli, in a line.' Prism Rivière Bracelet on rangoli stripes", "6.10% CTR Story", used(["H02", "H03"])),
 ("'It has been rolling for miles.' / 'Woven, not cast.' Woven Gold Hoops", "6.08% and 5.81% CTR", used(["H07", "H08", "woven-gold-hoops"])),
 ("'Anaar, pre-peeled.' Ruby tennis bracelet (sold out); its successor, the ruby necklace with anaar", "5.49% CTR, 15 sales at 3.63x; 24 purchases lifetime", used(["H06"])),
 ("'Rangoli you can wear.' Prism Cluster Studs", "5.21% CTR Feed", used(["H04", "prism-cluster-studs"])),
 ("'Finer than pheni.' Silk Mesh Cuff", "4.32% CTR", used(["H05", "silk-mesh-cuff"])),
 ("'Nobody got the better pair.' Baguette Huggies", "4.01% CTR", used(["H09", "baguette-huggies"])),
 ("'Sealed with a kiss.' Kiss Knot Bangle", "3.90% CTR", used(["H16", "kiss-knot-bangle"])),
 ("'Paperclip, promoted.' Toggle Link Chain", "7.3% CTR on a small sample (41 impressions)", used(["H10", "toggle-link-chain"])),
 ("Catalogue carousels of the on-model listing photos (Bestsellers, Edition Two)", "6.28% CTR, 23 purchases, 2.93x in the last 7 days (Bestsellers); 4.37% and 41 purchases lifetime (Edition Two)", used(["worn/", "-worn.jpg"])),
]
live = [
 ("Catalogue · Bestsellers batch 1 (₹1,500/day)", "₹10,182", "6.28%", "23", "2.93x"),
 ("Catalogue · Edition Two, 31 pieces (₹1,300/day)", "₹8,674", "3.72%", "17", "2.05x"),
 ("Catalogue · 12 new pieces (₹500/day)", "₹5,040", "4.03%", "15", "2.19x"),
 ("VK statics, 27 ads (₹1,000/day)", "₹6,784", "3.26%", "4", "1.19x"),
 ("Edition Two fruit plates, no text (₹600/day)", "₹5,607", "3.35%", "2", "1.00x"),
 ("Winners revived, 5 ads (₹1,000/day)", "₹2,202", "2.75%", "1", "0.76x"),
 ("New collection cover carousels", "₹613", "2.24%", "0", "–"),
 ("Naira Twenty, 8 ads (₹800/day, new)", "₹0", "–", "–", "–"),
]
setup = [
 ("Campaign", "Naira · Shop All · Never just one · 10 ads · ₹1,000/day · all India · Nov 2026"),
 ("Objective", "Sales: website purchases on the Naira pixel, 7-day click and 1-day view attribution (the account's default)"),
 ("Budget", "₹1,000 a day as an Advantage campaign budget over one ad set. Ten ads on ₹1,000 is about ₹100 each if spread evenly; Meta will put most of it behind the two or three it likes, which is the point of the test."),
 ("Start", "When you approve it. If '10:10' meant a start time, it is scheduled for 10:10 AM IST; if it meant ten ads at ₹100 each, see Budget."),
 ("Audience", "All India, Advantage+ audience, with women 20-45 as the suggestion (as in the account's other static campaigns); exclude people who bought in the last 30 days if that custom audience exists."),
 ("Placements", "Advantage+ placements. Each ad carries both images: the 4:5 Feed image for Feed, Explore and the right column, and the 9:16 Story image for Stories and Reels (placement asset customisation)."),
 ("Ads", "The ten below, each with its own primary text, headline, description and the Shop now button."),
 ("Link", "https://nairaflore.com/jewellery (the live 'All pieces' page; /shop and /collections/all redirect there) with utm_source=meta, utm_medium=paid, utm_campaign=shopall_nov26 and utm_content set per ad, so each ad can be read in Shopify."),
]
rules = [
 "Leave it alone for the first 48 hours, while Meta learns.",
 "Day 3 (about ₹3,000 spent): pause any ad below 2% CTR after 2,000 impressions. The account's statics run at 2.2-3.3%.",
 "Day 7 (about ₹7,000 spent): pause any ad that has spent ₹1,500 at under 1.0x ROAS. Keep ads at 1.5x or better.",
 "If the campaign holds 2.0x or better over 7 days (the catalogue campaigns run 2.05-2.93x), raise the budget 20% every three days.",
 "When an ad's frequency passes 2.5 or its CTR falls a third below its first week, swap in the next-best of the other ten.",
 "Check stock weekly and pause any ad whose named piece drops below 10 units.",
]
flags = [
 "Three past winners cannot lead: the Ruby Baguette Tennis Bracelet ('Anaar, pre-peeled.') and the Molten Bloom Hoops ('Poured, not made.', 7.25%) are sold out, and the Ruby eternity band ('kesar') has 3 left. The ruby necklace stands in for the anaar ad.",
 "Ruby Baguette Huggies have 4 units. They appear in ads that show the huggies, alongside Crystal, Emerald and Amethyst (13-15 each).",
 "Statics click, catalogues sell: in the last 7 days the catalogue campaigns returned 2.05-2.93x, the static campaigns 0.76-1.19x. This campaign is the static test for the whole shop; judge it on purchases, not clicks.",
 "Overlap: three static campaigns already run to similar audiences (VK statics, Winners revived, Naira Twenty). Pausing Winners revived (0.76x) would fund this one without raising total spend. That is your call.",
 "Older captions in the account still say 'with codes BUY2 and BUY3 at checkout'. The codes still work, but the bag applies the offer by itself, so these ten never mention codes.",
 "The store shows percent-off badges against compare-at prices ('43% OFF'). These ads never use them.",
 "C19 ('Teen patti') shows playing cards at a Diwali card night. It sells jewellery, not betting, but Meta's automated review can be strict about card games. A fallback with the headline 'Card night.' is built and saved; if C19 is rejected, swap that in.",
 "C01 is the proven 'Almost edible.' photo. With one campaign budget, Meta may pour most of the ₹1,000 into it because it already has clicks; if it takes more than about a third of spend by day 3 while the others starve, pause it for a week so the new ads get a read.",
 "Nothing has been created on Meta and nothing has changed on Shopify.",
]
plan = {"_about": "Shop All campaign plan (5 Nov 2026), built by make_plan.py", "idea": "NEVER JUST ONE. " + concepts["campaign_idea"].split("NEVER JUST ONE.", 1)[-1].strip(),
        "link_base": "https://nairaflore.com/jewellery?utm_source=meta&utm_medium=paid&utm_campaign=shopall_nov26",
        "slugs": slugs, "sources": [dict(ad=a, result=r, used=u) for a, r, u in sources], "live": live, "setup": setup, "rules": rules, "flags": flags}
json.dump(plan, open(os.path.join(ROOT, "plan.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(slugs, ensure_ascii=False)); print([s["used"] for s in plan["sources"]]); print(plan["idea"][:300])
