# Naira Flore: Meta ads performance + current Instagram feed (pulled 25 Oct 2026, read-only)

Scope: Meta Ads accounts 903466039148509 ("naira flore meta ads", main), 1088886349394166, 1498422677060515; Instagram @naira.flore (IG account 17841475924464756) via `ads_get_ig_media`; Motion Creative Analytics (blocked, see section 9).
Nothing was created, edited, boosted or paused. All money in INR (Rs). "Last 90 days" = Meta `last_90d` preset = 27 Jul to 24 Oct 2026 (today excluded). Purchases/ATC are Meta-attributed (`omni_purchase`, `omni_add_to_cart`, account default attribution window), not Shopify orders.

Files written alongside this note:
- `research/ig-current-grid.jpg` (+ `-part1`, `-part2`): latest 30 posts as a 3-column profile grid, newest top-left.
- `research/meta-top-sheet.jpg`: contact sheet of the top ad creatives. Images in `assets/meta-top/` (README.txt inside maps each file to its creative ID and numbers).
- `assets/ig-current/NN_date_type_shortcode.jpg`: 30 newest IG posts, numbered newest-first.
- `data/ig-media.tsv`: all 140 IG media (type, timestamp, likes, comments, shortcode, caption start). Permalink = https://www.instagram.com/p/<shortcode>/
- `data/meta-ads-90d.json` / `-rows.json`: all 169 ads with spend in the last 90 days. `data/meta-creatives-90d-grouped.json`: same, grouped by creative (156 creatives). `data/meta-creatives-text.json`: copy of the 26 ranked creatives. `data/meta-dpa-product-breakdown.json`: catalogue ads split by product. `data/meta-tables.md`: the four ranking tables below.

---

## 1. Account overview

| Account | Window | Spend | Impr. | CTR (all) | Link clicks | LPV | ATC | Checkouts | Purchases | Cost / purchase | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 903466039148509 main | last 90d | Rs 2,07,419 | 1,830,919 | 1.98% | 30,269 | 23,553 | 1,105 | 412 | **100** | Rs 2,074 | **1.03** |
| 903466039148509 main | lifetime | Rs 2,68,956 | 3,907,427 | 5.52% | 133,760 | 57,509 | 1,199 | 444 | 104 | Rs 2,586 | 0.81 |
| 1088886349394166 | lifetime | Rs 26,516 | 209,926 | 2.36% | n/a | n/a | 57 | n/a | 2 | Rs 13,258 | 0.15 |
| 1498422677060515 | lifetime | Rs 43,196 | 1,812,643 | 0.93% | n/a | n/a | 0 | n/a | 0 | n/a | n/a |

Notes
- 90-day funnel (main): LPV to ATC 4.7%, ATC to checkout 37%, checkout to purchase 24%, LPV to purchase 0.42%. Implied AOV of attributed purchases = ROAS x spend / purchases = **~Rs 2,126**, which matches Shopify's jewellery AOV (mean Rs 2,304, median Rs 1,926, per `data-shopify.md`). The CLAUDE.md line "pieces at Rs 24,000 to 44,000" is wrong for this catalogue: live prices are Rs 699 to Rs 2,399.
- Lifetime minus 90d = ~Rs 61.5k spent before late July. Of that, the March to May 2026 couture-era campaigns ("New Sales campaign" Rs 32,739, CTR 9.95%, 77,737 link clicks; "Cbo / 24 Mar" Rs 20,686; "Cb / 20 May" Rs 2,114) = **Rs 55,540 with 0 purchases** (31 ATC). Very high CTR + zero purchases = traffic that never bought.
- 1088886349394166: Dec 2025 couture lead-gen (Rs 14,111, leads objective) and Sep 2026 **boosted organic jewellery posts**: "The one you reach for when..." Rs 6,998, 26 ATC, 1 purchase, ROAS 0.36; "Lac bone asks you to slow down..." Rs 3,638, 17 ATC, 1 purchase, ROAS 0.41; "Gold, caught mid-thought..." Rs 1,734, 14 ATC, 0 purchases. Boosting the existing launch posts did not sell.
- 1498422677060515: campaigns are "Adenoids WhatsApp Campaign 21st Nov 25" and "Adenoids, 5rd March 2026" (lead objective). **Not Naira**: appears to be an unrelated (medical) advertiser on the same login. Excluded from everything below.
- Shopify cross-check (from `data-shopify.md`): 141 orders in 120 days. Meta claims 104 purchases lifetime, i.e. ~74% of all orders. Plausible given ads drive most traffic, but Meta's view-through attribution over-claims and Nashik buyers (29 orders, the studio's own city) are likely partly word of mouth. Treat Meta purchase counts as directional. Unverified.

### Weekly trend, main account (last 90d, Meta weeks)
| Week | Spend | Impr. | CTR | ATC | Purch. | Cost/purch | ROAS |
|---|---|---|---|---|---|---|---|
| 27 Jul to 16 Aug | 0 | 0 | | | | | |
| 17 to 23 Aug | 6,585 | 364,511 | 1.45% | 20 | 0 | | |
| 24 to 30 Aug | 13,823 | 501,334 | 1.77% | 32 | 8 | 1,728 | 2.38 |
| 31 Aug to 6 Sep | 40,197 | 210,167 | 2.17% | 101 | 12 | 3,350 | 0.64 |
| 7 to 13 Sep | 35,465 | 254,453 | 2.09% | 110 | 12 | 2,955 | 0.82 |
| 14 to 20 Sep | 30,687 | 251,722 | 1.89% | 107 | 10 | 3,069 | 0.60 |
| 21 to 27 Sep | 8,450 | 54,860 | 1.55% | 54 | 3 | 2,817 | 1.05 |
| 28 Sep to 4 Oct | 14,068 | 52,861 | 1.78% | 110 | 8 | 1,759 | 1.41 |
| 5 to 11 Oct | 15,291 | 26,852 | 2.57% | 101 | 9 | 1,699 | 1.06 |
| 12 to 18 Oct | 13,831 | 56,386 | 4.62% | 80 | 4 | 3,458 | 0.51 |
| **19 to 24 Oct** | **29,023** | 57,773 | 4.08% | **390** | **34** | **854** | **1.87** |

The last week (Edition Two launched 16 Oct; fruit-plate statics + Edition Two catalogue) is the best week the account has had: 34% of all 90-day purchases in 6 days. The Sep weeks (collab reels + generic catalogue at Rs 30 to 40k/week) were the most expensive per purchase.

### Campaigns, last 90 days (main account, spend > 0)
| Campaign | Status | Spend | CTR | ATC | Purch. | Cost/purch | ROAS |
|---|---|---|---|---|---|---|---|
| Clean Metro Prospecting (28 Aug), catalogue sets A "Finish / close-up" + B "Daily wear" | paused | 46,398 | 1.63% | 153 | 15 | 3,093 | 0.62 |
| Pankti Collab Reel, Rs 400/day (cut 15 Sep) | paused | 28,182 | 3.83% | 70 | 8 | 3,523 | 0.79 |
| Statics + Riya Collab Reel, Rs 1,000/day | paused | 27,244 | 5.37% | 59 | 8 | 3,405 | 0.63 |
| one winner - Copy (Prism "Almost edible" + Garba hoops + reels) | paused | 25,496 | 3.15% | 159 | 13 | 1,961 | 1.24 |
| Jewllery launch sales camp 1 (catalogue) | paused | 17,554 | 1.63% | 51 | 8 | 2,194 | 1.88 |
| IG Top 20, Stories + Feed (designed statics) | paused | 14,240 | 2.87% | 107 | 8 | 1,780 | 1.05 |
| Statics, Rs 1,000/day, Oct 2026 (Apricot hoops, Almost edible) | **active** | 7,560 | 1.57% | 46 | 5 | 1,512 | 1.11 |
| **Catalogue, Edition Two (31 pieces), broad, Rs 1,000/day** | **active** | 6,225 | 5.07% | 162 | 12 | **519** | **3.07** |
| Crazy concepts, 16 statics | paused | 6,171 | 2.95% | 53 | 3 | 2,057 | 0.97 |
| Reels, 3 x Rs 500 (Sonal, Pankti v11, Ananaya) | paused | 6,102 | 6.50% | 41 | 2 | 3,051 | 0.49 |
| **Edition Two, fruit plates, no text, 26 ads, women 18+, 7 metros** | **active** | 5,977 | 5.33% | 113 | 14 | **427** | **3.55** |
| catalogue testing (CT1 earrings / CT3 necklaces+bracelets) | paused | 5,184 | 1.12% | 25 | 1 | 5,184 | 0.42 |
| Static Winners Rs 800/day (15 Sep) | paused | 4,015 | 4.90% | 16 | 1 | 4,015 | 0.44 |
| Sept Test COLD / WARM / HOT | paused | 3,838 | 5.34% | 21 | 2 | 1,919 | 0.80 |
| Retarget, 5 bestsellers (covers) | paused | 989 | 2.03% | 9 | 0 | | |
| sonal reel (nsk and mumbai) | paused | 977 | 2.39% | 3 | 0 | | |
| Catalogue, Pending 59 pieces, 5 sets x Rs 200 (24 Oct) | active | 868 | 2.77% | 7 | 0 | | |
| Approved ads test, 33 ads, Rs 2,000/day (25 Oct) and Catalogue 12 new pieces (25 Oct) | active, new | 0 in window | | | | | |

### Where it delivered (placement, last 90d)
| Placement | Spend | Impr. | CTR | ATC | Purch. | ROAS |
|---|---|---|---|---|---|---|
| Instagram feed | 94,678 | 139,569 | 2.91% | 465 | **52** | 1.15 |
| Instagram stories | 49,456 | 145,970 | **4.70%** | 362 | **32** | **1.32** |
| Instagram reels | 34,242 | 1,310,721 | 1.68% | 185 | 10 | **0.49** |
| Facebook feed | 21,030 | 33,554 | 3.74% | 63 | 6 | 1.02 |
| Facebook reels / stories / other | ~5,650 | ~46,000 | | 19 | 0 | |
| WhatsApp status | 1,311 | 147,551 | 0.64% | 9 | 0 | |
| Audience network | 621 | 538 | | 1 | 0 | |

84% of purchases came from the Instagram feed and stories, i.e. a 4:5 or 9:16 still (or catalogue card) seen in the IG feed. Reels bought 72% of impressions and returned 10% of purchases.

### Who bought (age x gender, last 90d)
| Segment | Spend | CTR | ATC | Purch. | ROAS |
|---|---|---|---|---|---|
| Women 35 to 44 | 61,553 | 3.40% | 358 | **37** | 1.19 |
| Women 45 to 54 | 33,266 | 4.45% | 202 | **17** | 1.19 |
| Women 25 to 34 | 42,336 | 2.48% | 225 | 16 | 0.71 |
| Women 55 to 64 | 15,491 | 4.58% | 92 | 9 | 1.12 |
| Men 18 to 24 | 13,851 | 1.62% | 42 | 9 | 2.21 |
| Women 18 to 24 | 9,436 | 1.66% | 56 | 4 | 0.75 |
| Men 25 to 34 | 12,398 | 2.30% | 59 | 3 | 0.51 |
| Other (men 35+, women 65+, unknown) | ~19,100 | | ~71 | 5 | |

Women 35+ = 64 of 100 purchases. The buyer is not Gen Z: she is a 35 to 54 woman in a metro (Shopify: Mumbai, Nashik, Delhi NCR, Bengaluru). Men 18 to 24 converting at ROAS 2.2 suggests gifting (small sample, 9 purchases; unverified).

---

## 2. Creatives ranked (main account, last 90 days, grouped by creative ID)

156 creatives had spend; Meta concentrated spend hard, so only 26 creatives crossed Rs 1,000. Rankings B and C use that Rs 1,000 floor; anything below it is noise. "Link CTR" here = link clicks / impressions. Headline = Meta `title`, primary text = Meta `body`, verbatim (trimmed). Catalogue (DPA) creatives show `{{product.name}}` because the card is filled from the Shopify catalogue. Images: `assets/meta-top/` and `research/meta-top-sheet.jpg`.

### A. Top 10 creatives by purchases (last 90 days)
| # | Ad name (first ad using it) | Creative ID | Spend Rs | Impr. | Link CTR | ATC | ATC per Rs1k | Purch. | Cost/purch Rs | ROAS | Headline (title) | Primary text (body) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | E2 fruit · E2_ruby_anaar2_916 · Stories 9:16 | 2916197152089370 | 4,691 | 5,424 | 5.13% | 106 | 22.6 | 14 | 335 | 4.52 | Baguette Tennis Bracelet · ₹1,699 | Anaar, pre-peeled. ✨ Ruby-red baguette cubic zirconia, lined up in 18k gold-tone claws. The Baguette Tennis Bracelet, ₹1,699.  Pick Ruby on the pro... |
| 2 | A · Finish / close-up (set 1) | 3018503908494517 | 27,538 | 442,926 | 1.47% | 113 | 4.1 | 13 | 2,118 | 0.95 | {{product.name}} | Demi-fine jewellery, finished to be seen up close. |
| 3 | Catalogue E2 · carousel · 31 new pieces | 1138710695402004 | 6,225 | 15,629 | 4.37% | 162 | 26.0 | 12 | 519 | 3.07 | {{product.name}} | Edition Two is here: 31 new pieces, just landed. Take 2 pieces for 10% off, or 3 for 20% off, applied in your bag. Free insured shipping and cash o... |
| 4 | 104 bracelet ad – Copy | 2063058210986252 | 20,013 | 35,667 | 2.73% | 116 | 5.8 | 11 | 1,819 | 1.44 | Loading piece / Naira Flore | A prism takes one beam of light and lets it come apart. This bracelet does the same. A single line of multicolour stones, each holding a different ... |
| 5 | Static · Hoops · Apricot quiet · original post · Feed only | 2555829581555220 | 9,841 | 17,886 | 1.52% | 70 | 7.1 | 9 | 1,093 | 1.46 | Woven Gold Hoops · ₹1,499 | Texture does the talking here.  Woven Gold Hoops: 25mm of braided gold rope. No stones. |
| 6 | jewellery catalogue ad 2 | 1744930063475131 | 8,948 | 337,486 | 1.67% | 27 | 3.0 | 8 | 1,118 | 3.68 | {{product.name}} | Jewellery you don't save for occasions. Gold-coated, tarnish-resistant, and made for daily wear. Shop the new Naira Petite drop. |
| 7 | pankti collab reel | 3310237479186316 | 28,182 | 29,855 | 2.90% | 70 | 2.5 | 8 | 3,523 | 0.79 |  | Two pieces from Naira, opened today.   Brushed Gold Huggies, satin rather than mirror.   Toggle Link Chain,closes with a turn.  Tarnish free. Water... |
| 8 | riya reel | 1034012832789720 | 17,382 | 49,013 | 1.99% | 42 | 2.4 | 6 | 2,897 | 0.71 |  | You’re welcome, but keep it between us 💌 ... @naira.flore 🤍 ... #antitarnish #jewellery #viral #haul #reels |
| 9 | Crazy · H08_a1 · The gold note. | 1076618338337075 | 3,259 | 4,761 | 2.39% | 29 | 8.9 | 3 | 1,086 | 1.83 | Heartbead Bracelet · ₹1,299 | 6 mm mirror-polished steel beads, one puffed gold-tone heart and a toggle clasp at the front. The Heartbead Bracelet.  Take 2 pieces for 10% off, o... |
| 10 | W2 · STORY · S2 Woven Gold Hoops v2 | 1949749419053322 | 2,271 | 1,440 | 5.00% | 6 | 2.6 | 2 | 1,136 | 1.56 | Woven Gold Hoops · ₹1,799 | Braided from separate strands of gold-tone metal. No stones at all. |

### B. Top 10 creatives by add-to-carts per Rs1,000 (creatives with Rs1,000+ spend, n=26)
| # | Ad name (first ad using it) | Creative ID | Spend Rs | Impr. | Link CTR | ATC | ATC per Rs1k | Purch. | Cost/purch Rs | ROAS | Headline (title) | Primary text (body) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Catalogue E2 · carousel · 31 new pieces | 1138710695402004 | 6,225 | 15,629 | 4.37% | 162 | 26.0 | 12 | 519 | 3.07 | {{product.name}} | Edition Two is here: 31 new pieces, just landed. Take 2 pieces for 10% off, or 3 for 20% off, applied in your bag. Free insured shipping and cash o... |
| 2 | E2 fruit · E2_ruby_anaar2_916 · Stories 9:16 | 2916197152089370 | 4,691 | 5,424 | 5.13% | 106 | 22.6 | 14 | 335 | 4.52 | Baguette Tennis Bracelet · ₹1,699 | Anaar, pre-peeled. ✨ Ruby-red baguette cubic zirconia, lined up in 18k gold-tone claws. The Baguette Tennis Bracelet, ₹1,699.  Pick Ruby on the pro... |
| 3 | Crazy · P02_a2c · Rangoli, in a line. | 1152223680815293 | 1,087 | 2,622 | 2.48% | 13 | 12.0 | 0 | - | 0.00 | Prism Rivière Bracelet · ₹2,399 | Aqua, pink and yellow stones in one straight line, each framed by a fine pavé halo. The Prism Rivière Bracelet, adjustable from 15 to 19 cm.  Take ... |
| 4 | Reel · Pankti v11 · not all gold | 1102312058949030 | 1,424 | 2,855 | 1.26% | 16 | 11.2 | 0 | - | 0.00 | Satin, not mirror. | Not all gold has to shine. Brushed Gold Huggies ₹1,099 + Toggle Link Chain ₹1,499, worn together every day. Any 2 pieces get 10% off in the bag: bo... |
| 5 | ad 102 reel riya – Copy | 1745765676644657 | 1,259 | 4,349 | 2.12% | 14 | 11.1 | 0 | - | 0.00 |  | You’re welcome, but keep it between us 💌 ... #antitarnish #jewellery #viral #haul #reels |
| 6 | Story · ccquiet-A1 · Apricot quiet · Woven Gold Hoops | 1415908293225487 | 4,533 | 4,982 | 3.09% | 47 | 10.4 | 1 | 4,533 | 0.24 | Woven Gold Hoops · ₹1,499 | Texture does the talking here.  Woven Gold Hoops: 25mm of braided gold rope. No stones. |
| 7 | Feed · 08-M2 · THE WIDTH. | 29597528473169130 | 1,359 | 1,296 | 2.85% | 13 | 9.6 | 1 | 1,359 | 1.10 | Woven Gold Hoops · ₹1,499 | 25 millimetres across. One pair. No stones, all braid.  The Woven Gold Hoops: a thick rope of gold strands, 18k gold tone on surgical steel. Tarnis... |
| 8 | Crazy · H08_a1 · The gold note. | 1076618338337075 | 3,259 | 4,761 | 2.39% | 29 | 8.9 | 3 | 1,086 | 1.83 | Heartbead Bracelet · ₹1,299 | 6 mm mirror-polished steel beads, one puffed gold-tone heart and a toggle clasp at the front. The Heartbead Bracelet.  Take 2 pieces for 10% off, o... |
| 9 | Static · Hoops · Apricot quiet · original post · Feed only | 2555829581555220 | 9,841 | 17,886 | 1.52% | 70 | 7.1 | 9 | 1,093 | 1.46 | Woven Gold Hoops · ₹1,499 | Texture does the talking here.  Woven Gold Hoops: 25mm of braided gold rope. No stones. |
| 10 | 105 golden woops – Copy | 1816121026501980 | 3,191 | 3,375 | 3.14% | 22 | 6.9 | 1 | 3,191 | 0.47 | Woven Gold Hoops · Demi-Gold Jewellery / Naira Flore | Garba moves in circles. So do these. Golden woven hoops for nine nights of turning, and every ordinary morning after. |

### C. Bottom 10 creatives by add-to-carts per Rs1,000 (Rs1,000+ spend)
| # | Ad name (first ad using it) | Creative ID | Spend Rs | Impr. | Link CTR | ATC | ATC per Rs1k | Purch. | Cost/purch Rs | ROAS | Headline (title) | Primary text (body) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A7 · The Demi-Fine Edit — bracelets | 27876452092024747 | 1,740 | 1,907 | 4.67% | 2 | 1.1 | 0 | - | 0.00 | The demi-fine edit | Cubic zirconia, not candy. Demi-fine pieces on surgical steel, waterproof and tarnish free, from ₹899. |
| 2 | A6 · Sweet On You · bracelets | 4458058627842140 | 4,917 | 4,525 | 2.59% | 8 | 1.6 | 1 | 4,917 | 0.58 | Bracelets from ₹899 | The charm bracelet edit. Toggles, hearts and beads built to take daily wear and water. 10% off your first order with NAIRA10. |
| 3 | B · Daily wear — cleaned copy (set 2) | 1014996834886168 | 18,860 | 223,085 | 1.68% | 40 | 2.1 | 2 | 9,430 | 0.15 | {{product.name}} | Jewellery you don't save for occasions. Tarnish-resistant, made for daily wear. |
| 4 | catalalogue 1 | 2169210780300461 | 1,341 | 60,539 | 2.05% | 3 | 2.2 | 0 | - | 0.00 | {{product.name}} |  |
| 5 | riya reel | 1034012832789720 | 17,382 | 49,013 | 1.99% | 42 | 2.4 | 6 | 2,897 | 0.71 |  | You’re welcome, but keep it between us 💌 ... @naira.flore 🤍 ... #antitarnish #jewellery #viral #haul #reels |
| 6 | pankti collab reel | 3310237479186316 | 28,182 | 29,855 | 2.90% | 70 | 2.5 | 8 | 3,523 | 0.79 |  | Two pieces from Naira, opened today.   Brushed Gold Huggies, satin rather than mirror.   Toggle Link Chain,closes with a turn.  Tarnish free. Water... |
| 7 | W2 · STORY · S2 Woven Gold Hoops v2 | 1949749419053322 | 2,271 | 1,440 | 5.00% | 6 | 2.6 | 2 | 1,136 | 1.56 | Woven Gold Hoops · ₹1,799 | Braided from separate strands of gold-tone metal. No stones at all. |
| 8 | jewellery catalogue ad 2 | 1744930063475131 | 8,948 | 337,486 | 1.67% | 27 | 3.0 | 8 | 1,118 | 3.68 | {{product.name}} | Jewellery you don't save for occasions. Gold-coated, tarnish-resistant, and made for daily wear. Shop the new Naira Petite drop. |
| 9 | ad 101 – Copy | 1941406646534654 | 2,379 | 8,547 | 1.38% | 9 | 3.8 | 1 | 2,379 | 0.55 | {{product.name}} |  |
| 10 | A · Finish / close-up (set 1) | 3018503908494517 | 27,538 | 442,926 | 1.47% | 113 | 4.1 | 13 | 2,118 | 0.95 | {{product.name}} | Demi-fine jewellery, finished to be seen up close. |

### D. Bottom 10 by purchases: highest-spend creatives with zero purchases
| # | Ad name (first ad using it) | Creative ID | Spend Rs | Impr. | Link CTR | ATC | ATC per Rs1k | Purch. | Cost/purch Rs | ROAS | Headline (title) | Primary text (body) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | A7 · The Demi-Fine Edit — bracelets | 27876452092024747 | 1,740 | 1,907 | 4.67% | 2 | 1.1 | 0 | - | 0.00 | The demi-fine edit | Cubic zirconia, not candy. Demi-fine pieces on surgical steel, waterproof and tarnish free, from ₹899. |
| 2 | Reel · Pankti v11 · not all gold | 1102312058949030 | 1,424 | 2,855 | 1.26% | 16 | 11.2 | 0 | - | 0.00 | Satin, not mirror. | Not all gold has to shine. Brushed Gold Huggies ₹1,099 + Toggle Link Chain ₹1,499, worn together every day. Any 2 pieces get 10% off in the bag: bo... |
| 3 | catalalogue 1 | 2169210780300461 | 1,341 | 60,539 | 2.05% | 3 | 2.2 | 0 | - | 0.00 | {{product.name}} |  |
| 4 | ad 102 reel riya – Copy | 1745765676644657 | 1,259 | 4,349 | 2.12% | 14 | 11.1 | 0 | - | 0.00 |  | You’re welcome, but keep it between us 💌 ... #antitarnish #jewellery #viral #haul #reels |
| 5 | Crazy · P02_a2c · Rangoli, in a line. | 1152223680815293 | 1,087 | 2,622 | 2.48% | 13 | 12.0 | 0 | - | 0.00 | Prism Rivière Bracelet · ₹2,399 | Aqua, pink and yellow stones in one straight line, each framed by a fine pavé halo. The Prism Rivière Bracelet, adjustable from 15 to 19 cm.  Take ... |
| 6 | Retarget · Carousel v2 · 5 bestsellers (offer first, jewelle | 1634835608148544 | 989 | 1,377 | 1.74% | 9 | 9.1 | 0 | - | 0.00 | Naira | 2 pieces 10% off, 3 pieces 20% off, applied in your bag. Five of our most-ordered pieces, from ₹1,099: Woven Gold Hoops, Prism Rivière Bracelet, Br... |
| 7 | CT1 · Earrings (14 in stock) | 1549907823817922 | 978 | 24,552 | 0.83% | 3 | 3.1 | 0 | - | 0.00 | {{product.name}} | Jewellery you don't save for occasions. Gold-coated, tarnish-resistant, and made for daily wear. |
| 8 | New Sales ad | 1128637019659430 | 977 | 11,626 | 1.24% | 3 | 3.1 | 0 | - | 0.00 |  | Not me developing a personality around jewellery!!! ... wanna be influenza / for my page / jewellery #fyp... #jewellery #naira |
| 9 | FEED · S2 Woven Gold Hoops v2 | 1391993805705770 | 891 | 842 | 4.51% | 3 | 3.4 | 0 | - | 0.00 | Woven Gold Hoops · ₹1,799 | Braided from separate strands of gold-tone metal. No stones at all. |
| 10 | A1 · Woven Gold Hoops | 2589324418173188 | 882 | 456 | 1.97% | 2 | 2.3 | 0 | - | 0.00 | Woven Gold Hoops · ₹1,799 | A thick braided rope of gold-tone strands, 25mm across, no stones at all. Waterproof and tarnish free, so it stays on through the day. |

Reading the tables
- **The two best creatives are 7 days old and both are Edition Two**: the Ruby "Anaar, pre-peeled" fruit plate (Rs 335 per purchase, ROAS 4.52, 22.6 ATC per Rs 1k) and the Edition Two catalogue carousel (Rs 519, ROAS 3.07, 26 ATC per Rs 1k). Small spend (Rs 4.7k and Rs 6.2k), so expect regression, but they beat every September creative by 4 to 8x on cost per purchase.
- **Same image, different words**: the Prism "ALMOST EDIBLE. cubic zirconia, not candy." image (gummies bowl) ran with poetic copy ("A prism takes one beam of light and lets it come apart...") for 11 purchases on Rs 20k, and with "The demi-fine edit... from Rs 899" copy for 2 ATC and 0 purchases on Rs 1.7k (different campaign and week, so not a clean test). Price-led "from Rs 899" edit copy is the worst ATC rate in the account (1.1 and 1.6 per Rs 1k).
- **Collab/UGC reels bought reach, not baskets**: Pankti (Rs 28.2k) and Riya (Rs 17.4k) are #7 and #8 by purchases only because they had the most money; at 2.4 to 2.5 ATC per Rs 1k they are bottom-5 on efficiency, Rs 2,900 to 3,500 per purchase.
- **Generic catalogue with "daily wear / tarnish-resistant" copy was the single biggest waste**: "B Daily wear" Rs 18,860 for 2 purchases (ROAS 0.15). The same catalogue format with a reason to look ("Edition Two is here: 31 new pieces") was the best.
- Headline bug: creative 2063058210986252 shows the headline **"Loading piece | Naira Flore"**: the link preview scraped the PDP's loading-skeleton page title. It still sold, but any organic link card or ad built from a PDP URL can inherit it.

### Concept families (what the naming tells you about the creative system)
| Family | Ads | Spend | ATC | Purch. | Note |
|---|---|---|---|---|---|
| **E2 fruit plates, "no text"** (Edition Two, 7 metros, women 18+) | 25 | 5,977 | 113 | 14 | Every ad pairs a piece with an Indian food/object and a Hindi/Marathi word: `ruby_anaar` (pomegranate), `emerald_elaichi` (cardamom), `crystal_mishri` (rock sugar), `coil_jalebi`, `huggie_jamun`, `mint_nimbu` (lime), `meshring_chai`, `studs_mogra` (jasmine), `tennis_phuljhadi` (sparkler), `star_dhruv` (pole star), `knot_gath` (knot), `watch_haath` (hand), `tubogas_churi` (bangle), `roman_ghadi` (clock), `droplet_rain`, `choker_monsoon`, `duo_gangajamuni` (two-tone), `P11_diya`, `P12_saree`, `P13_kandil` (Diwali lantern). Meta put 78% of the budget on Ruby anaar; the other 24 got under Rs 250 each, so they are **untested, not losers**. |
| "Crazy concepts", 16 statics | 14 | 6,171 | 53 | 3 | Headlines: "The gold note." (Heartbead, 3 purchases), "Rangoli, in a line." (Prism on pastel powder, 12 ATC per Rs 1k, 0 purchases), "Hoop in a hoop.", "Braided, like the thread.", "Hanging by a thread.", "Woven, twice.", "Every beat, a little gold.", "Sweeter than mithai.", "One gift, two hoops. Diwali (ends 30 Oct)". Indian-pop wordplay already exists in the ad system. |
| IG Top 20 designed statics (Feed + Story) | 40 | 14,240 | 107 | 8 | Colour-camp still lifes ("Apricot quiet", "Lilac quiet", "framed"), type-led tiles ("THE WIDTH.", "PASTEL.", "PICK 'N' MIX.", "PAVÉ"), FAQ tiles ("will it tarnish? NO.", "will it fit my wrist? 15 TO 19."), gift tiles ("Gift: sister who borrows", "friend who wears colour"), "What I wear to the airport / brunch", "07:15 / 23:30". Only the apricot hoops still life got real spend (4 purchases feed, 1 story). |
| Static Winners / Sept Test S1 to S7 | 20+ | ~8,000 | ~40 | 4 | Woven hoops S1/S2, Cushion Halo, Baroque Pearl Lariat, Pearl Point Studs, Heartline Paperclip, Verdant Drop, Pearl Blossom: plain product + one physical fact. Mostly under Rs 300 each. |
| Reels Oct (Sonal, Pankti v11, Ananaya) | 6 | 6,102 | 41 | 2 | "Where is this from?" (Ananaya) CTR 11.5% but 7 ATC; Sonal "Doing all the work" 18 ATC, 1 purchase. |

## 3. Which products sold through ads

Catalogue (DPA) ads split by product (`product_id` breakdown on the 7 catalogue ads that spent: Rs 64.2k, 36 purchases, 360 ATC; all 36 purchases accounted for):

| Product | Purch. | ATC | Spend shown on | Live price* | Stock* |
|---|---|---|---|---|---|
| **Roman Numeral Trio Ring** | **10** | **70** | 2,596 | 1,899 | **3 left** (one each 6/7/8) |
| Baguette Éclat Bracelet | 4 | 4 | 626 | | |
| Heartbead Bracelet | 3 | 28 | 8,213 | 1,299 | 25 |
| Star Point Band | 3 | 15 | 5,393 | | |
| Cushion Halo Ring | 2 | 12 | 1,737 | 1,199 | 60 |
| Pearl Ribbon Ring | 2 | 1 | 772 | | |
| Pearl Point Studs | 1 | 20 | 6,005 | | |
| Mesh Band Ring | 1 | 17 | 848 | | |
| Charm Box Chain | 1 | 14 | 3,105 | | |
| Verdant Eternity Band | 1 | 10 | 4,212 | | 60 |
| Brushed Gold Huggies | 1 | 9 | 2,728 | 999 | 35 |
| First Light Set, Filigree Bloom Studs, Rose Verdant Band, Petite Pavé Band, Blush Cluster Ring, Trio Oval Drop Earrings, North Star Bangle | 1 each | | | | |
| Baguette Tennis Bracelet (catalogue card) | 0 | 21 | 274 | 1,699 | 57 |
*Price and stock from `data-shopify.md` (Shopify, 25 Oct); blank = not checked here.

Named-product statics and reels (90d): **Woven Gold Hoops** ~Rs 28.8k, ~205 ATC, 16 purchases, ROAS ~0.88 · **Baguette Tennis Bracelet, Ruby** Rs 4.7k, 106 ATC, 14 purchases, ROAS 4.52 · **Prism Rivière Bracelet** Rs 23.3k, 141 ATC, 12 purchases, ROAS 1.41 · Brushed Gold Huggies + Toggle Link Chain (Pankti reels) Rs 29.8k, 86 ATC, 8 purchases · Heartbead Bracelet Rs 3.4k, 29 ATC, 3 purchases.

Cross-check with Shopify bestsellers (120d units, `data-shopify.md`): Woven Gold Hoops 20, Prism Rivière 14, Baguette Tennis Bracelet 13 (all since 16 Oct, Ruby 8 of 13), Heartbead 11, Molten Bloom Hoops 9 (sold out), Roman Numeral Trio Ring 8, Brushed Gold Huggies 8. The ad winners and the shop's bestsellers are the same five pieces. Rings sell through the catalogue (Roman Numeral, Star Point, Cushion Halo) even though no static ad ever led with a ring.

## 4. What won: message, product, visual

**Visual**
1. **Still life with an edible or everyday Indian prop, warm palette, product as the hero**: pomegranate for Ruby baguettes (#1), a bowl of sugared gummies for the pastel Prism (#4), a halved apricot for the woven hoops (#5, and the top ATC story). The three best static creatives in the account share this idea. The fruit-plate system extends it into an Indian object vocabulary (anaar, mishri, jalebi, chai, mogra, diya, kandil) that has not been tested yet.
2. **Physical-proof framing**: "THE WIDTH." (hoops in brass calipers, a 25 mm ruler) and "WOVEN, NOT CAST." both pulled above-average ATC. Showing the measurement or the making beats saying "premium".
3. **Colour-blocked, one-piece-per-frame layouts with a small serif caption** (Rangoli pastel powder stripes; apricot on blush; oxblood with droplets). No busy collage in any ad that performed; the maximalism lives in the colour and prop, not the layout.
4. Feed and stories stills sold (84% of purchases); reels mostly sold reach.

**Message**
1. A **specific, sensory fact** in plain words: "25mm of braided gold rope. No stones.", "6 mm mirror-polished steel beads, one puffed gold-tone heart", "Ruby-red baguette cubic zirconia, lined up in 18k gold-tone claws", "adjustable from 15 to 19 cm".
2. **A wink of wordplay** in the headline, Indian-rooted: "Anaar, pre-peeled.", "cubic zirconia, not candy", "Rangoli, in a line.", "The gold note.", "Garba moves in circles. So do these."
3. **The offer as mechanics, not shouting**: "Take 2 pieces for 10% off, or 3 for 20% off, applied in your bag. Free insured shipping and cash on delivery across India." It is on all three best October creatives.
4. **A reason to look now**: "Edition Two is here: 31 new pieces, just landed."

**What lost**
- "From Rs 899" / "The demi-fine edit" / "Bracelets from Rs 899" price-led edit copy (lowest ATC rates).
- Generic benefit copy with no object: "Jewellery you don't save for occasions. Tarnish-resistant, made for daily wear." (Rs 18.9k, ROAS 0.15).
- Couture-voice abstraction ("Lac bone asks you to slow down. To notice the grain... It's not loud. It's presence.") when boosted: ROAS 0.4.
- Creator haul/unboxing reels with hashtag-stuffed captions ("fyp, explore page, trending...", "wanna be influenza"): cheap views, Rs 2,900 to 3,500 per purchase.
- Pre-jewellery traffic campaigns (Mar to May 2026): Rs 55.5k, 0 purchases.

---

## 5. Instagram @naira.flore: the feed as it stands (all 140 media, paged to the end)

Source: `ads_get_ig_media` (advertisable feed media for IG 17841475924464756, via ad account 903466039148509). Caveat: this endpoint lists advertisable media; a post with licensed audio or a collab owned by another account could be missing, and follower counts, reach and saves are not available through it. A date-filtered query for 10 Aug to 25 Oct 2026 returned **zero** media. Timestamps are reported in US Pacific; IST = +12.5 h.

### Cadence
| Period | Posts | What |
|---|---|---|
| 23 Jul to 31 Aug 2025 | 60 | Couture launch. Dumped in batches: 12 posts on 19 Aug, 12 on 22 Aug, 6 on 14 Aug, 6 on 5 Aug. |
| Sep to Dec 2025 | 30 | Couture reels/carousels, Diwali 20%-off reels, wedding season. |
| Jan to Apr 2026 | 37 | Couture: influencer (@prackritipavani) carousels, meme/POV reels, Women's Day, Valentine's. |
| May 2026 | 0 | |
| 24 Jun 2026 | 3 | Couture editorial series: "The Haldi capsule, N° 01", "The Garden Series, N° 02", "Craft Files, N° 05". |
| 10 Aug 2026, 00:13 to 00:29 IST | 10 | **The only jewellery posts ever**: "Lac Bone" launch grid, all 10 posted inside 16 minutes. |
| 10 Aug to 25 Oct 2026 | **0** | **76 days silent**, through the Edition Two launch (16 Oct), Navratri and Diwali, while Meta spent ~Rs 2.07 lakh sending people to the brand. |

Mix: 71 images, 44 reels, 25 carousels. Line: 130 couture/Indo-western, **10 jewellery**. Jewellery carousels: 0. Jewellery reels: 2 (both title cards).

### Engagement
- All 140: median 9.5 likes, mean 84.6 (skewed by a few outliers). Comments are near zero on almost everything (max 20).
- Jewellery (10 posts): median 11 likes, mean 13.7. Best: "Introducing our premier campaign: Lac bone at Naira. Made in small numbers, as always." reel, 35 likes, 8 comments. Captionless tiles: 8 to 13 likes.
- Outliers are 2025 couture reels: "The Naira Experience" unboxing 3,410 likes, "masterji sketching dreams" 3,149, "Unboxing couture, the Naira way" 1,467, "October 3rd. Love story. Couture moment. #SwiftWeddingTrend" 661, Diwali reel 353, "You send the inspo / We create the sketch..." 332. These numbers are 100 to 300x the account median; they are probably boosted (unverified: no boost data for those dates on the accounts checked). The two topics that hit are **unboxing/packaging** and **process (sketch, karigar, hand embroidery)**.

### What the grid looks like (viewed: `research/ig-current-grid-part1.jpg`, `-part2.jpg`)
Newest first, 3 columns:
- **Row 1 (posts 1 to 3)**: a triptych banner: oxblood tile "LAC" in cream high-contrast serif | cream tile with the black flower mark | oxblood tile "BONE". Reads as one wide "LAC [flower] BONE" across the top of the profile. Strong, but it is a launch title from August.
- **Rows 2 to 4 (posts 4 to 10)**: quiet-luxury product editorial. Serpentine Whisper Chain with a baroque pearl on a white plaster block; Prism Rivière on a model's wrist (red satin shirt, oxblood ground, vertical small-caps label with price); Pearl Reverie Bracelet on linen; Molten Bloom Hoops on glossy oxblood with water drops (**now sold out**); a cream text tile "Softly, slowly, worn."; Cushion Halo Ring on a hand against oxblood (struck MRP + price); a cream spec tile "18K GOLD-PLATED / 316L STAINLESS STEEL / WATERPROOF · NON-TARNISH". Small type is unreadable at grid size; the palette is coherent (oxblood, cream, gold).
- **Rows 4 to 5 (posts 11 to 15)**: June couture editorial, a different art direction: bold mustard block "SPIN IT IN gold." (Haldi capsule), "INTO THE garden." over a lavender drape, "THE DRAPE, up close" split layout, then two influencer frames at a white-flower mandap.
- **Rows 6 to 10 (posts 16 to 30)**: spring 2026 couture/Indo-western content in a third style: influencer shots, a reel with a comment sticker ("Customized traditionals >>>>"), "POV: You order a customized outfit from your couch" with WhatsApp screenshots, a torn-paper collage "Why is old, time consuming, कारीगरी still relevant in 2026?" with a black-and-white karigar photo on red, "Where do you find gorgeous outfits like Nita Ambani (on a budget)", "Types of Design Work at NAIRA", a doodle-outlined cutout "Last weekend, I randomly ran into...", an illustrated "Spring-Inspired Indo-Western Outfits: A floral archive" collage, "The world will try to fit you into tight boxes" photo-grid box, chat-bubble testimonials.

Honest read: **the profile is three brands stacked on top of each other**, and the jewellery brand, which is the one the ads sell, is a ten-tile August launch frozen in place. Someone who taps through from an ad sees "LAC [flower] BONE" (a campaign name the website source never uses and the current ads do not carry; it appeared only in two September boosts of these same posts), six pieces of which one is sold out and none is the piece they clicked (no Woven Gold Hoops, no Heartbead, no Ruby baguettes, no Edition Two), then scrolls into lehengas and bridal couture. There are no prices readable at thumbnail size, no proof (reviews, wrists, unboxing), no offer, no Diwali, no reason to follow.

The couture era already proves the team can make the reference's kind of content: the कारीगरी torn-paper collage, the illustrated "floral archive", the doodle cutout and the numbered editorial series ("N° 01 / 02 / 05") are the closest things on the grid to @projecttteteatete. They were one-offs, not a system.

### What is missing compared with a curated feed
1. **A recurring visual system**: no motif, border, mascot, illustration style or type treatment that repeats across posts; each era restarts.
2. **Named, numbered series for the jewellery**: the couture "N°" series show the habit exists; jewellery has none.
3. **The current product**: Edition Two (31 pieces, live since 16 Oct and the ads' best performer), Ruby baguettes, Woven Gold Hoops (#1 bestseller), Heartbead, Prism on a fresh frame.
4. **Season**: Diwali (now), wedding season (next), gifting. The ads ran Garba and Diwali lines; the grid ran nothing.
5. **Proof and texture**: buyer wrists, unboxing (the 2025 unboxing reels are the account's biggest posts; the site has a 3D Naira box), the Nashik studio and its karigars, COD and insured shipping, the bag offer.
6. **Cadence**: batches of 10 to 12 posts in minutes, then months of silence. A curated feed needs a rhythm (the Shopify data says Sunday noon and Fri/Sun 18:00 to 21:00 IST are when buyers buy).
7. **Bridge from the ad world**: the fruit plates, apricot, gummies, calipers and Indian-word headlines that sell in ads never appear organically, so ad and profile feel like different companies.

---

## 6. Motion Creative Analytics: blocked

`get_auth_context` returned **FORBIDDEN, `mcp_billing_required`, reason `trial_expired`** ("Your trial or subscription has ended. Choose a plan in Motion to keep using MCP", org 6a7aeed822108baacbed94ac). Every other Motion tool needs the workspace ID from that call, so SPEND / HOOK / SCALING insights, workspace brand, competitors and inspo creatives were **not retrieved**. Fix: the owner renews the Motion plan, then re-run.

Partial fallback, Meta Ad Library (`ads_library_search`, "demi-fine jewellery anti tarnish", India, active, 25 Oct): ~114 active ads. Advertisers in the first page: Palmonas (8 ads launched 22 to 24 Oct), Anusi (6 ads 24 Oct, "All Products"), Neelorajewels ("Festive Sale Is Live!"), House of Theia ("Shop the Diwali Collection"), Elra ("Buy 1 Get 1 | 18K Gold, Waterproof"), Svora, Mauve Accessories, rubans.in, nyra jewels. The tool returns metadata only for commercial ads (no images or body text), so no creative or hook analysis was possible. What is visible says the category is shouting sales and BOGO this Diwali; Naira's best ads did the opposite (one object, one Indian wink, the offer stated calmly).

---

## 7. Implications for the organic feed

**Feature these products (they sell in ads and in Shopify, and are in stock)**
- **Baguette Tennis Bracelet in Ruby** (+ Baguette Huggies / Eternity Band / Tennis Necklace as the set). Best creative in the account (Rs 335 per purchase), 13 sold since 16 Oct, Ruby 8 of 13; 57 in stock, necklace 70 in stock and 0 sold.
- **Woven Gold Hoops**: #1 by units; ads proved "25 mm, braided, no stones" and the apricot still life. 63 in stock. Live price is **Rs 1,299** (ads said Rs 1,499 and Rs 1,799; use the live price).
- **Prism Rivière Bracelet**: #1 by revenue, the most colourful piece (aqua, pink, yellow), 67 in stock; "Almost edible" and "Rangoli, in a line" are its two working frames.
- **Heartbead Bracelet**: "The gold note." converted; gifting story; 25 in stock.
- **Edition Two as a world**: 31 pieces, best catalogue result ever. The grid has never shown it.
- Rings convert quietly through the catalogue (Roman Numeral Trio Ring 10 purchases, Star Point Band 3, Cushion Halo 2). **Do not hero the Roman Numeral Trio Ring**: 3 units left. **Do not show Molten Bloom Hoops or First Light Set**: sold out.

**Truths to carry (verified wording)**
- Exact physical facts: 25 mm braided rope, no stones; 6 mm mirror-polished beads; baguette CZ in 18k gold-tone claws; Prism adjustable 15 to 19 cm. Material line as on site/ads: "18K gold tone & rhodium plated" (do not say "18K gold"; some pieces are copper alloy per CLAUDE.md), surgical/316L steel where true, waterproof, tarnish free.
- The offer, stated calmly: 2 pieces 10% off, 3 pieces 20% off, applied in the bag; free insured shipping; cash on delivery across India (CLAUDE.md: COD carries a 5% fee shown in the bag, so on the feed say "COD available", not "free COD"). NAIRA10 is typed, open to everyone (not first-order only, despite older ad copy).
- Made in Nashik, by a studio that began in couture and made-to-measure. The couture era's best-liked posts were process (sketch, karigar, hand embroidery) and unboxing. That heritage is the jewellery brand's unfair advantage over Palmonas/GIVA-style steel brands; use it as provenance, not as a second product line.

**Voice that performed**
- Short, witty, Indian-rooted headline + one concrete fact + calm offer. Templates from winners: "Anaar, pre-peeled." / "cubic zirconia, not candy." / "Rangoli, in a line." / "The gold note." / "Garba moves in circles. So do these." / "THE WIDTH." / "WOVEN, NOT CAST."
- The untested fruit-plate vocabulary is a ready motif bank for a maximalist Indian-pop feed: anaar, elaichi, mishri, jalebi, jamun, nimbu, chai, mogra, phuljhadi, diya, kandil, dhruv, gath, haath, churi, ghadi, monsoon, gangajamuni, saree.
- Write for a 35 to 54 metro woman (64% of attributed purchases) who buys for herself and for gifting; not Gen Z slang.

**Format**
- Stills and carousels in the IG feed and stories earned 84% of purchases; reels earned 10% on 72% of impressions. The organic feed should lead with designed stills and carousels, with reels for process and unboxing (the two topics that ever broke out).
- One hero piece per frame, warm colour field, product large and legible at grid size; let the collage/illustration energy live around the product, not over it.
- Post on a rhythm (e.g. Sun noon, Fri/Sun evening IST), never 10 at once.

**Avoid**
- "From Rs 899" / price-led "edit" posts and generic "jewellery you don't save for occasions / tarnish-resistant" copy (lowest ATC rates; ROAS 0.15 at scale).
- Abstract couture-voice poetry with no object ("It's not loud. It's presence."): boosted, it returned ROAS 0.4.
- Hashtag-stuffed captions ("fyp, explore page, trending, viral", "wanna be influenza").
- Discount shouting, BOGO, "Festive Sale Is Live!": that is what every competitor is running this week.
- Showing sold-out or near-sold-out pieces as heroes; stale prices; any "Last 24 hours: N sold" style claim (CLAUDE.md: that number is a hash, not sales).
- A grid that mixes lehengas into the jewellery story without a frame; and dumping a whole grid in minutes.
- Link previews built from a PDP URL can show "Loading piece | Naira Flore" as the title.

**Open data gaps**: Motion insights (expired trial); IG follower count, reach, saves, profile visits (not exposed by this endpoint); creator reel thumbnails (partnership media, only 64 px thumbnails returned); fruit-plate images other than Ruby anaar were not downloaded (fetch by creative ID from account 903466039148509 if wanted).
