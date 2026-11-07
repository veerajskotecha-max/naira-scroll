# Writes ../plan.json for the aesthetic Shop All ten: the idea, the link, how to run them beside the first ten, the rules
# for the first two weeks, where the photos came from and the things to know. Usage: python3 build/make_plan.py
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

plan = {
    "_about": "Shop All, the aesthetic ten: campaign plan (7 Nov 2026), built by make_plan.py",
    "title": "Shop All, the aesthetic ten",
    "idea": "The same job as the first ten (send people to every piece Naira sells), told quietly. One photo the account "
            "already knows sells, given room to breathe, and one calm line that opens the door to the rest: a magazine "
            "cover whose issue is the whole shop, a gallery wall where the best seller has a red Sold dot and the rest "
            "are on view, a book plate whose index is everything else, a three-line poem with more verses inside. "
            "Editorial type, palettes taken from the photos, no stickers, no shouting, and the offer left for the caption.",
    "n_concepts": 18,
    "link_base": "https://nairaflore.com/jewellery?utm_source=meta&utm_medium=paid&utm_campaign=shopall_aesthetic_nov26",
    "slugs": {"A01": "one_link", "A09": "slip_models_own", "A03": "everything_issue", "A02": "sold_rest_on_view",
              "A07": "verse", "A05": "come_in", "A08": "fig_1", "A12": "set_in_gold_tone", "A10": "gold_tone_edit",
              "A04": "subtitles"},
    "first_board": "https://claude.ai/artifact/EennScYjuLekNowJ6nqvv3",
    "setup": [
        ["Where", "As a second ad set, 'Aesthetic', inside the Shop All campaign from the first board, beside the first ten's "
                  "'Never just one' ad set. Same objective, audience, placements and link, so the only difference is the style."],
        ["Budget (suggested)", "If you approve the ₹1,000 a day from the first board: split it ₹500 a day to the first ten "
                               "(loud) and ₹500 a day to these ten (quiet) for 7 days, with ad-set budgets so each style "
                               "gets a fair read. Then move the money to whichever sells more. Total spend stays ₹1,000 a day."],
        ["On their own", "Or run these ten alone at ₹1,000 a day in place of the first ten. Same rules below."],
        ["Objective", "Sales: website purchases on the Naira pixel, 7-day click and 1-day view attribution (the account's default)."],
        ["Audience", "All India, Advantage+ audience, women 20-45 as the suggestion; exclude people who bought in the last 30 days if that audience exists."],
        ["Placements", "Advantage+ placements. Each ad carries both images: the 4:5 Feed image for Feed and Explore, the 9:16 Story image for Stories and Reels."],
        ["Link", "https://nairaflore.com/jewellery with utm_source=meta, utm_medium=paid, utm_campaign=shopall_aesthetic_nov26 and utm_content set per ad."],
        ["Start", "When you approve it. Nothing has been created on Meta."],
    ],
    "rules": [
        "A05 ('Come in.', the rangoli) is a Diwali-week ad: start it with the ad set and end it on 15 Nov.",
        "A04 (the subtitles) uses the same hoops photo as Diwali 10 ad 05: start it after Diwali week, or exclude people who engaged with that ad.",
        "Leave everything alone for the first 48 hours, while Meta learns.",
        "Day 3: pause any ad below 1.5% CTR after 2,000 impressions. Quiet ads click a little less than loud ones; judge them on purchases.",
        "Day 7: compare the two ad sets on purchases and ROAS, not CTR. Move the budget to the better one; keep the best two or three of the other.",
        "Pause any ad that has spent ₹1,500 at under 1.0x ROAS. Keep ads at 1.5x or better; raise the budget 20% every three days if the ad set holds 2.0x.",
        "Check stock weekly. Pause an ad whose named piece drops below 10 units (A01's Bold Nocturne Chain has 17; A02 names the emerald green and crystal bracelets, 17 and 38).",
    ],
    "sources": [
        {"ad": "Woven Gold Hoops ('Woven, not cast.' / 'It has been rolling for miles.')", "result": "5.81% and 6.08% CTR; 'most loved' on the site", "used": "A03 (persimmon), A04 (in his hand)"},
        {"ad": "E2 fruit plate: Ruby Baguette Tennis Bracelet with anaar, no text", "result": "4.32% CTR lifetime on 20,253 impressions, 24 purchases at 2.27x: the best-converting single photo in the account. The bracelet is sold out.", "used": "A02, only with the red Sold dot, no price, pointing to the rest"},
        {"ad": "Diwali 10 ad 01, the ruby necklace with anaar (successor to 'Anaar, pre-peeled.')", "result": "'Anaar, pre-peeled.' ran 5.49% CTR, 15 sales at 3.63x", "used": "A07"},
        {"ad": "Prism Rivière Bracelet on rangoli ('Rangoli, in a line.' / 'Almost edible.')", "result": "6.10% and 6.21% CTR Stories", "used": "A05"},
        {"ad": "'Rangoli you can wear.' Prism Cluster Studs", "result": "5.21% CTR Feed", "used": "A08 (the same headline, now as the plate caption)"},
        {"ad": "'Sealed with a kiss.' Kiss Knot Bangle", "result": "3.90% CTR", "used": "A12"},
        {"ad": "Bestsellers catalogue carousel of the on-model listing photos", "result": "5.73% CTR, 43 purchases at 2.67x in the last 14 days: the account's best purchase driver", "used": "A01 (chain close-up), A09 (choker and cuff), A10 (huggies and bangle close-ups)"},
    ],
    "flags": [
        "Nothing has been created on Meta and nothing has changed on Shopify.",
        "The first board's three questions still stand: approval to create the campaign, what '10:10' meant, and whether to pause Winners revived (0.76x) to fund it.",
        "Range wording: 133 pieces were in stock on 7 Nov, so '130+' has 3 to spare. These ten never print a count; they say 'rings, earrings, necklaces, bracelets' and '₹599 to ₹2,399' or 'from ₹599'. The captions follow the same rule.",
        "A02 shows the sold-out Ruby Baguette Tennis Bracelet, on purpose: a red dot and the word Sold, no price, and the label points to the emerald green and crystal versions that are in stock. If you would rather not show a sold piece at all, A11 (the same hoops in a frame on a brown wall) is built and can replace it, but not in the same ad set as A03, which uses the same photo.",
        "A10 names a rakhi and a temple bell as comparisons ('Knotted, like a rakhi'). Nothing religious is shown; if you would rather avoid the words, the line can go back to 'Twisted. Knotted. Polished.' alone.",
        "A12's plaster background was cleaned of two light flares and a few specks. The bangle, seal and envelope were not touched. A04's and A05's photos are unretouched.",
        "A09's headline 'Slip, model's own.' is a stylist's credit: the slip is not for sale. The caption says so plainly.",
        "Quiet ads usually click less than loud ones. That is why the suggestion is a split test against the first ten on purchases, not a straight swap.",
        "The two ads not picked (A06 'Left ear, right ear.' and A11 'Hang at ear height.') are saved in ads/other/ as replacements when an ad tires.",
    ],
}
json.dump(plan, open(os.path.join(ROOT, "plan.json"), "w"), ensure_ascii=False, indent=1)
print("wrote", os.path.join(ROOT, "plan.json"))
