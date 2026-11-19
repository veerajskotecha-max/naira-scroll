

---

# critiques 1

Review of the draft playbook: visual, idea-strength, archetype and batch-1 defects

Before writing this I checked the plates and our ad results directly (read-only). Contact sheets are in /tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/review/ (s1.jpg = the batch-1 plates, s2.jpg = our winners and losers, s3.jpg = X10 and the colour plates, s4.jpg = the A1/A2/A5 source plates, s5.jpg = ads-20 Set 1, c53.jpg = droplets in colour/53). Spend figures are from scratchpad/meta/ads_30d.csv. Judge scores are from docs/creative/ads-20/build/scores.json.

Overall: the board study is thorough, but the system built on it misreads our own two winners. It re-imposes the lighting sameness it criticises. Its rubric would fail our best statics. Its picture inventory breaks its own size rule. Batch 1 has no "crazy" ad: it re-runs a Toggle ad that already lost and ignores finished, judged ads that never got spend.

1. The playbook misdescribes our two static winners.
   - What the draft says (§0 item 1, §2): both winners share "one saturated colour field that rhymes".
   - What the images show: ruby anaar sits on pale cream plaster and has no text, name, price or offer at all. F2 is ads-20 S1_01 on a cocoa ground, with no headline. What they actually share:
     - both are deep-red ruby baguette pieces, so the saturated colour is the piece itself;
     - the piece spans about 55–65% of the frame width;
     - neither has a headline.
   - The A1 rule "ground deepened, never pale" contradicts the anaar plate that A1 borrows from.
   - Fix:
     - Rewrite §0.1, §2 point 2 and the A1 palette line: "the most saturated colour in the frame belongs to the piece, or to its 1:1 rhyme, against a neutral or dark ground; neither winner had a headline."
     - Add to §8.13: Baguette Tennis Bracelet Ruby and Baguette Tennis Necklace Ruby are behind both static winners and are not in the 20+ set. Restocking them is an owner decision.
     - Give A1 and A2 slots first to the saturated-stone SKUs (Verdant ×2, Halo Curve tiger eye, Monochrome, the Baguette Huggies line-up). Put clear and silver pieces only on A5, dark grounds or flat saturated grounds.

2. The "headline everywhere" rule and the §7 rubric would fail both winners.
   - The ads-20 independent judge scored ruby anaar 6.15, the lowest group, and told it to "add a headline, price and wordmark". It did not pick S1_01 (F2) to launch and told it to "swap for an occasion headline".
   - The playbook repeats this: §3.5 calls the S1 no-headline cards a weakness, and A2 adds a two-beat headline to the F2 grammar.
   - The §7 cap "No wordmark: max 5" also contradicts A1's mandated no-logo Story twin.
   - Fix:
     - Add an "A0 Product card" archetype, the F2 card exactly: centred wordmark, name, ₹price, one variant or fit line and an offer box, over a dark gradient, with no headline.
     - Exempt no-text Stories from the wordmark cap.
     - Make every 4th A2 a no-headline card.
     - Run one same-frame pair (headline vs no headline) in batch 1.

3. The critic loop is uncalibrated and invites score inflation.
   - The same 10-criterion judge ranked anaar (24 sales, 2.29x) below DIW 08 pouches (0 sales, 7.23) and Apricot.
   - The gates "mean must rise every batch" and "≥8.8 by batch 20" are above the best competitor on that rubric (Palmonas hero, 8.57). Hitting them means inflating scores.
   - Fix:
     - Before batch 1, have both critics score 12 anchors blind: 6 winners (anaar, F2, W1 woven red, VK F18, Apricot quiet, a Halo video frame) and 6 losers (A07, P2, SA08, VK S5, kandil, W1 Waterproof).
     - If at least 5 winners do not score above the losers' median, re-weight the rubric (raise stop power at 200 px and piece colour; lower copy and brand).
     - Put 2 anchors, unlabelled, into every batch sheet.
     - Replace the absolute gates with "beats the anchor pair in a blind pairwise comparison at 200 px". Delete the 8.8 target.

4. The "hero ≥35% of canvas width" rule cannot be met for worn rings and earrings, and most listed plates break it.
   - Arithmetic: a jaw-to-chest crop (about 22 cm over 1350 px) puts a 12 mm halo at about 74 px, roughly 7% of the width.
   - Measured by eye on the listed sources:

| Plate | Piece share of width |
|---|---|
| cushion-halo-ring-worn | ~14% |
| woven-gold-hoops-worn, verdant-eternity-band-worn, halo-curve-ring-worn | ~10% |
| crazy3 06, 08, 16, 22 | 8–12% |
| colour/55 | ~20% |
| verdant-eternity-band-rhyme | ~25% |

   - Cropping a 1080-wide 9:16 plate to 4:5 cannot make the piece bigger.
   - Fix:
     - Replace the rule with a per-archetype metric:
       - product-only: ≥35% of width, or ≥25% of frame area for hanging or linear pieces;
       - worn: state the field of view in cm in the prompt so the key detail is ≥12% of width (ring: frame about 9–10 cm, hand only; earring: about 12 cm, ear and jaw; pendant: about 18 cm; collars and tennis necklaces fine at jaw to chest).
     - Re-audit the "existing plates" lists against this metric and strike every failure.
     - Recount the "290 ads without new frames". Expect fewer than half.

5. The A5 source list is wrong.
   - The crazy3 night plates are prop still lifes (fan, clutch, candle, rose) with the piece at 8–12% of width. They are not spotlight-on-riser frames.
   - Fix: delete them from A5. Only 02 (Toggle) and 04 (Prism) can serve, and as A3/A4 sources. A5 needs new frames, so add them to §5.4.

6. Several A1 and A2 sources break the playbook's own rules.
   - colour/53 (paper boats) has visible water droplets on the ground (c53.jpg), which breaks "no water, droplets".
   - colour/03 and colour/53 are pale grounds, yet A1 says "Prism (dark ground only)".
   - A2 lists woven-gold-hoops-worn (ivory shirt and low bun) and the cream-linen worn plates while saying "never the ivory-shirt-and-bun look again".
   - Fix: strike these plates. Add a pre-flight lint that checks every reused plate for water, pale piece on pale ground, styling repeats and the size metric in item 4.

7. §4.0 re-imposes the lighting sameness the playbook criticises.
   - It mandates "one warm directional key plus one specular kick" on every ad. That is the cream, soft-window sameness the audit flagged. Direct flash, gels, backlight, gobo shadows and top-down light are all absent.
   - Fix:
     - Keep only "gold warm-neutral" and "true contact shadow" as universal rules.
     - Add a light menu; every ad declares one:
       - L1 single hard spot or chiaroscuro;
       - L2 on-camera direct flash with a hard drop shadow (night/party);
       - L3 two-colour gel rim on dark;
       - L4 hard sun through a jaali or cane gobo;
       - L5 backlit rim with bloom;
       - L6 soft top-down flat lay.
     - Batch rule: at least 3 different lights and 3 camera angles per batch (90° top-down, low hero at 10–15°, 85 mm worn, 100 mm macro, POV in hand).

8. "Crazy" is under-supplied.
   - Only A5, A6, A11 tape and A13 qualify, the rotation allows one heavy experiment per batch, and batch 1 has none.
   - Board devices that transfer honestly are missing:
     - frozen motion (66, 109, 117, 131);
     - levitation with a detached shadow (96);
     - selective colour (85);
     - in-word object swap (155);
     - product as another object or costume (47, 72);
     - prism streak (90);
     - light-burst blades (4).
   - Fix: add five archetypes.
     - A15 Frozen Motion: e.g. Toggle Link Chain falling in an S from a hand above frame into an open palm, links sharp at 1/8000 s, fingers in the chain's plane, hard top spot, ink ground.
     - A16 Levitation: e.g. Monochrome Enamel Hoops hovering about 4 cm over a flat saffron floor, crisp detached shadow, hard top light.
     - A17 Selective Colour: a worn frame graded black and white except the green stone or the gold.
     - A18 In-word Swap: e.g. "PROP O SAL" with the Cushion Halo Ring standing as the O, plus a size tag; or a toggle ring as the O.
     - A19 Native POV / mirror selfie: the phone hides the face, which also settles §8.3.
   - Fund them by cutting A4 from 50 to 25, A8 from 25 to 10, A12 from 25 to 12, A9 from 25 to 15, and dropping the A10 tiles.
   - Batch rule: at least 2 ads per batch from the crazy set, one of them new to the account.

9. There is no visual idea bank, only copy examples.
   - 500 ads on 18 SKUs need picture ideas, not formulas.
   - Fix: add a table of SKU × 6 ideas × archetype × prop, each run through the founder-reject list and the one-second test before any generation. Seeds:
     - Halo Curve: a cane-blind gobo throwing tiger stripes across the ring.
     - Prism: a glass-prism spectrum band across an ink ground (this also fixes pastel on pale).
     - Monochrome: a lone black-and-white object on flat saffron (118), or top-down on zebra-crossing paint.
     - Serpentine: one S on a saturated field (64).
     - Bold Nocturne: the only lit object, cast as the moon (the diwali-10/10 mechanism).
     - Brushed: the pair as the "OO" of a word.
     - Cushion Halo: the ring box opened at the lens.
     - Toggle: frozen mid-fall.

10. B1-03 re-runs an ad that already lost, and §2 under-reports the Toggle.
   - T1 "No more hook laga do" (toggle-15 X10, the same listing worn photo as ref-clasp) spent ₹3,519 for 4 purchases: Feed 0.59x, Story 0.66x.
   - "Toggle: 9 ads, ₹3.9k, 0 sales" leaves out T1, T2 and T5 (₹4,060, 4 sales). The true figure is about ₹8k for 4 sales, around 0.3x.
   - B1-03's callouts "SPRING-GATE RING" and "CUBIC ZIRCONIA BAR" are not listing words (the listing omits the CZ). That breaks A7's own rule.
   - Fix:
     - Correct §2 and §5.1. Cut the Toggle from 40 ads to about 20, conditional on the clasp gate.
     - Remove B1-03 from batch 1.
     - Any later Toggle ad uses a new idea (A15) and listing-only callouts: "TOGGLE CLASP · WORN AT THE FRONT", "4 MM PAPERCLIP LINKS", "50 CM · 18K GOLD TONE PVD".

11. B1-01 rebuilds an F2 sibling that already exists, never got spend, and changes two variables at once.
   - ads-20/ads/S1_04_cushion_halo_ring_feed.jpg uses the same Set 1 system as F2 (cocoa ground, centred card, offer box). The judge called it "most convincing hand of the 20" (8.05). Spend: ₹0.
   - B1-01 instead pays for a new frame, bans lips (F2 shows lips) and adds a headline.
   - Its "proposal" line is not shown in the picture: a hand resting on a collarbone does not say proposal.
   - Fix:
     - B1-01 = S1_04 re-rendered at ₹999 with the F2 card and no headline. Its raw PNG was in the cleared scratchpad/ads20/raw, so retrieve the generation from Higgsfield history (no credits).
     - B1-01b = the same frame with "LOOKS LIKE A PROPOSAL. / priced like a present."
     - If a new frame is still wanted, use the show-the-ring gesture: back of the hand to camera, fingers together, at chest height, 85 mm, frame about 10 cm wide (halo about 13% of width). Lips follow the §8.3 decision.

12. B1-02 is not a new move.
   - It uses the same "Woven, not cast." line as W1 (1.23x on oxblood), on the Apricot peach palette that §2 calls decaying (1.72x falling to 1.31x) and that §3.6's pale-ground rule argues against.
   - Woven is also the most over-tested SKU (18 ads, 0.75x).
   - Layout collision: the Cormorant 46 italic line at y 1000 (about 40 characters, about 780 px from x 72) runs into the size tag at x 760–1008, y 1050.
   - Fix: give the slot to A16 Levitation on Monochrome Enamel Hoops (24 units, never advertised) on flat saffron.

13. B1-04's arc is decorative and technically broken.
   - Board rank 1 works because the sun's path measures the claim. A pair of huggies on a cube with no wearer cannot show "still on".
   - Brushed gold on brushed steel invites the known "reads silver" failure (QUIET failed on this twice).
   - The headline is 29 characters at Velista 50 with .06em tracking, about 1,100 px, on an arc about 1,465 px long. The text runs into the near-vertical flanks and the letters turn sideways.
   - Velista's digits are stylised (the brand rule is digits in Jost).
   - ☀/☾ (U+2600/263E) fall back to colour emoji in Chromium.
   - Fix, either:
     - (a) replace it with ads-20 S3_12 "The ₹799 pair." (judge 8.2, ₹0 spent), re-priced to "The ₹699 pair."; or
     - (b) rebuild A8 as worn: an ear in profile generated at true size, with an arc from a morning-light side to a tungsten side. Headline at most 16 characters on the arc's middle 50% (startOffset 25%, textLength 650). Digits in Jost. Sun and moon as inline SVG. Measure with getComputedTextLength, because render.cjs data-fit does not see SVG text.

14. B1-05 fails three of the playbook's own rules.
   - The ring is about 25% of the width, under the 35% rule.
   - A silver ring on a brass thali with a paan leaf reads as puja or food, both founder rejects.
   - The chip "ADJUSTABLE US 5–9 · COD" carries no offer, against "every ad carries one verified offer".
   - Fix: swap in ads-20 S2_06, the Verdant Eternity Band on a mehendi hand on haldi-yellow silk (judge 8.2, ₹0 spent). Re-price it to ₹1,049, add a BUY2 chip, and re-copy "emerald" as "emerald-green cubic zirconia". It is wedding season now.

15. The credit arithmetic contradicts itself.
   - Batch 1 says "2 new frames = 4 credits", but B1-01 and B1-04 each request 4 frames: 8 generations, 16 credits.
   - §5.4's "95 frames = 190 credits" becomes 760 credits at 4 variants per shot, against the 200-credit budget.
   - Fix:
     - Count generations, not frames. Default to 2 variants per shot.
     - At 200 credits that is 100 generations, or 50 shots. Expected keepers are about 25–30: assume a 40% keep rate for worn true-size frames (Soleil 0 of 2; CRAZY3 drew pieces 1.5–2.6× too large) and 60% for product-only.
     - Recompute the "about 210 ads from new frames".

16. Finished ads that never got spend are ignored.
   - ads-20 S1_04, S3_12, S2_06 and S1_05 got ₹0. 51 Paperclip (₹52), p3-08 (₹36), DIW 06 (₹38) and A01 (₹33) are unjudged, not losers.
   - Fix: add a §5.0 "unspent inventory" pass. Take every finished ad or plate with under ₹500 spend on a SKU with 20+ units, re-check scale, compliance and live price, and put the passes into wave 1 before generating anything.
   - Note: S4_17 haldi is on the Marquise gold variant, which has 15 units.

17. A1 is over-allocated on one data point.
   - 62 ads, yet the other 20 rhyme plates made 0 sales on ₹4.6k.
   - Fix: cut A1 to about 35 and require a literal 1:1 rhyme: the prop's units match the stones in size, shape and colour, as arils match baguettes. The piece's colour must be the saturated element. Conceptual rhymes (dandelion, thali) move to A3 or A5.

18. A10a tiles are the 2×2 grid that lost.
   - A 3–4-tile occasion map is the SA08 grid (₹1,968, 0 sales), which the failure check itself bans.
   - Fix: drop A10a. Show sets only as one photographed group at true relative scale (A10c) or one generated body wearing the whole set (ear stack, hand stack) at true size, with the BUY code as the headline.

19. A9's masked cut-outs with "drawn contact shadows" are the pasted-shadow AI tell the audit flagged (crazy3/21).
   - Fix: generate A9 product-only frames directly on the flat token field in Higgsfield, with a real contact shadow. Two frames per SKU covers the series.

20. Too many archetypes look the same at thumbnail size.
   - A3, A4, A9, A12 and the non-tape A11 are all "packshot plus big type on a flat field": about 183 ads, 37% of the plan, read as one family at 200 px.
   - A12 has only about 10 valid listing figures for 25 ads. A8 has one claim for 25 ads.
   - Fix:
     - Cap this type-led family at about 100 ads.
     - Cap A8 at 10 and A12 at 12 until one of each wins in a wave.
     - Move the roughly 70 freed slots to A15–A19.

21. The size tag is illegible.
   - 22–24 px in a hairline box is about 8 pt on a phone, so it fails as honesty and adds legal clutter to about 250 ads.
   - Fix: make it a brand device in a fixed foot position: a 1:1 "actual size" silhouette, or a known-size object in frame (jasmine bud, cowrie, sugar crystal), plus "ACTUAL 25 MM" in Jost 500 at 30 px.

22. The wordmark keeps the size the audit called illegible.
   - At 40 px tall it is about 179 px wide; the audit flagged 105–170 px as too small to read the flower in the I.
   - Fix: 56 px tall (about 250 px wide) on Feed, or add a fixed colour tab as the series signature.

23. Some symbols will render as emoji or a fallback font.
   - ⚠ (A11 tape) and ☀/☾ (A8) render as system emoji in Chromium. Check → (A14) in Jost.
   - Fix: inline SVG icons. Add this to the kit fixes alongside ₹.

24. The rubric has no "desire" dimension.
   - The ads-20 rubric had one, and its best sets won on it. As written, a clean catalogue card scores high.
   - Fix: add Desire at .15 (styling, skin, occasion, aspiration). Take .05 each from Layout, Brand and Archetype fit.

25. Wedding season is deferred to batches 41–80.
   - It is 19 Nov, peak shaadi season. Generic occasion lines lost (<2.2% CTR), but the occasion pictures (ads-20 Sets 2 and 4: mehendi, haldi, sangeet, the best-judged sets) were never properly spent.
   - Fix: from batch 1, at least one ad per batch pairs an occasion picture with a concrete line naming the moment.
   - Minor: A13 lists a single Baguette Huggies colour while A14 bans single variants. Make it a three-colour ear stack.

Suggested batch 1 after these fixes (6 credits for 3 new shots at 2 variants each, plus the anchor calibration first):
- S1_04, no headline, ₹999 (0 credits);
- S1_04 with the "Looks like a proposal" headline (0 credits);
- S2_06 Verdant mehendi, re-priced (0 credits);
- A16 Monochrome levitation on saffron (new);
- A15 Toggle frozen fall, or the A8 worn ear arc on Brushed (new).
That gives one headline A/B, one occasion picture, two crazy ads, and a proven-grammar control.

---

# critiques 2

Review of the 500-ad static playbook. Lens: grounding in our Meta results, whether the plan can be tested at our spend, and what is missing for conversion.

How I checked: I re-read the 30-day ad CSV (/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/meta/ads_30d.csv), with ad-set names and per-ad spend. I opened the plates named in batch 1. I made two read-only Higgsfield calls, a balance check and a cost estimate for one 4-image generation. Nothing was generated, written or changed.

Defects, most important first:

1. The deployment plan costs far more than we spend.
- At ₹3,000 per ad, 500 ads cost ₹15,00,000. That is 6.6 months of the whole account's spend (₹2,28,954 in 30 days, about ₹53k a week) and about 16 months of the current static spend (about ₹22.5k a week).
- Waves of 15 ads at ₹3,000 come to ₹45k a week, 84% of weekly account spend. That would starve catalogue, which returns 2.28x and brings 67% of purchases.
- ₹3,000 buys about 2 purchases at the static cost per purchase (₹1,481), or about 4 at the account's (₹722). That is too few to tell one ad from another.
- FIX: rewrite §5.6 as a fixed testing budget, about ₹20k a week (today's static share, restructured).
  - Stage 1: each new ad gets ₹1,000 over 4 days, about 14 ads a week.
  - Stage 2: the top 2–3 get another ₹3,000 each.
- That screens about 60 ads a month, so 500 take about 8 months. Say this plainly and pace production to it (see 15).

2. Meta never spent on most of the ads the draft calls losers or controls.
- The CSV shows Meta putting most of an ad set's budget on one ad:
  - Twenty F2 took 82% of its 8-ad ad set. The other seven got ₹29–139 each.
  - In AB·Woven red, the 'Waterproof' ad took 79%.
- The median spend of the 163 ads with no purchase is ₹113. Most were never shown enough to be judged.
- Waves of 15 ads in shared ad sets will repeat this, so the '₹3,000 each' will not happen.
- FIX:
  - For head-to-head tests, put one ad per ad set (ad-set budgets) or use Meta's A/B test feature (Experiments).
  - Count an ad as 'tested' only after ₹1,500 of spend.
  - Report each ad's share of its ad set's spend next to its ROAS.

3. §2 overstates the winners and the losers.
- **W1 is not a like-for-like A/B.** 'Woven, not cast' was created on 3 Nov in the 'Winners · Stories' ad set, next to ruby anaar. 'Waterproof, for the wedding' was created on 12 Nov in a different ad set ('AB · Woven red').
- **The colour rhyme does not travel even within the same image.** The 'ruby anaar' Feed 4:5 version of the same image (E2_ruby_anaar2) got ₹123 and 0 sales. A revival as W3 got ₹64 and 0 sales.
- **Most fruit plates were never tested.** They got ₹17–475 each in Feed. Only the kandil Story reached ₹1,848. So 'the other 20 plates made 0 sales' is not evidence that colour rhyme fails, and the one Stories win is not evidence that A1 is a proven control.
- **F2 is thin evidence.** It is 6 purchases, on an ad Meta picked from 8.
- FIX: rebuild the §2 tables with a 'tested (≥₹1,500)' column.
  - Tested winners: anaar Story, F2, W1 'not cast', VK F18, Apricot.
  - Tested losers (all ₹1,540–3,236, 0 sales): W1 Waterproof, VK S5, SA08, P13 kandil Story, C01, P2, VK S1, old 'Almost edible'.
  - Drop the word 'clean' from the W1 claim, in §2 and in owner decision §8.1.
  - Relabel A1 and A2 as 'promising, n=1', not 'proven control'.

4. Both static winners sell products this plan cannot use.
- Ruby anaar is the ruby Baguette Tennis Bracelet. F2 is the ruby Baguette Tennis Necklace. Neither is among the 18 SKUs with 20+ units.
- So the draft cannot separate the layout's effect from product and colour (red baguette cubic zirconia).
- FIX:
  - Say this in §0 and §2.
  - Add an owner decision: restock the ruby baguette tennis pieces and iterate on the two proven winners (new crops and hooks on the anaar and F2 images). For the next 30 days that is likely the highest-return static work available.
  - Until then, treat 'grammar transfers to eligible SKUs' as the hypothesis batches 1–10 must test.

5. The product allocation ignores our own sales data, and the weighting formula is not shown.
- Prism gets 28 ads. It is our most-tested static failure (0.55x on ₹28.9k).
- Woven gets 38. It has 0.75x on ₹13.7k over 18 ads.
- Toggle gets 40 with 0 sales on ₹3.9k. That is really untested (A07 alone took ₹2.9k).
- 'Stock tier × sales evidence + ring bonus' does not produce these numbers.
- FIX: replace the fixed 466-ad table with a stage-gated allocation.
  - Phase 1 cap per product: 10 ads (15 for Cushion Halo).
  - A product unlocks 10 more only after its first 5 ads produce at least 2 purchases at 1.5x or better at stage 2.
  - Prism: at most 10 statics, worn on dark grounds only. Put Prism's effort into video, where it made 3.46x.
  - Woven: at most 15, texture-led only.
  - Print the formula and the inputs used.

6. The 'ring bonus' rests on rings this plan does not include.
- Catalogue ring sales come from Roman Numeral Trio, Cushion Solitaire, Mesh Band and Baguette Eternity, none of them eligible.
- In the pulled catalogue rows, the eligible rings show little: Cushion Halo 1 purchase, Verdant Eternity 0 on ₹691, Halo Curve 0, Droplet 1.
- FIX: drop the bonus. Justify Cushion Halo by its video results (24 purchases). Give Verdant Eternity, Halo Curve and Droplet only phase-1 caps.

7. The two ₹699 pieces cannot pay back alone.
- Average order is ₹1,153 and the account pays ₹722 per purchase. One ₹699 order less 10% is ₹629, which is a loss on ads at that cost.
- Yet Brushed gets 40 ads and Ribbon gets 20.
- FIX:
  - Every Brushed and Ribbon ad leads with bundle value: 'any 2 / any 3' with the verified saving and the resulting price.
  - Judge them on order value, not purchase count.
  - Cut Brushed to 20 until order-value data exists.

8. The offer chip names the code but not the saving.
- 'CODE BUY2 · COD' does not tell anyone what BUY2 gives. Our best static (F2) printed 'BUY 2 · 10% OFF • BUY 3 · 20% OFF'.
- FIX:
  - The chip must state the verified value, for example 'ANY 2 · 10% OFF'. If checkout applies the discount automatically, drop the word 'CODE'.
  - Until the terms are confirmed (§8.7), print no code on images at all.
  - Add three read-only checks to §5.5:
    - the code's value, minimum quantity and dates, and whether it combines with compare-at sale prices;
    - any minimum order for free shipping (a ₹699 piece may not qualify);
    - any COD fee.

9. 'An offer on every image' has never been tested.
- 'Every winner carried an offer' refers to the ad text below the image, and losers carried it too.
- On the image itself, only F2 had an offer. The anaar winner had no text at all. 'W5 Offer' got ₹35 and was never really shown.
- FIX: put two controlled tests in wave 1, same image in each.
  - Chip versus no chip.
  - BUY2 versus NAIRA10. Core v2 with NAIRA10 is our best catalogue ad, at 3.00x.

10. Ads land on pages that don't match the offer.
- A10 set ads and code ads land on single product pages, so the shopper has to rebuild the set and remember the code.
- FIX (no Shopify write needed):
  - Set ads: a cart permalink with the discount pre-applied, /cart/{variantA}:1,{variantB}:1?discount=BUY2.
  - Code ads: /discount/NAIRA10?redirect=/products/{handle}.
  - Decoder ads (A14): /products/{handle}?variant={id}.
  - Core v2, which linked to the homepage, made 3.00x. Test product page against collection page as its own cell.

11. Placement assets are missing, so Meta will crop or stretch our images.
- B1-01 and B1-04 are generated at 4:5. Story twins exist for only three archetypes.
- Under Advantage+ placements Meta will crop or AI-expand the 4:5 images into Stories and Reels. That repeats the mirror-extension fault and can break honest scale.
- Reels is our cheapest placement per purchase (₹518, 1.82x). The draft's Story safe zone (text down to y 1500) sits under the Reels caption and CTA.
- FIX:
  - Generate every new frame at 9:16 with the subject inside the central 4:5 window, as the brand-system practice already says.
  - Give every ad a 9:16 asset through placement customisation: text-free, or with text only between y 270 and 1250.
  - Exclude FB Feed (0.82x) and Explore (0 sales) from test ad sets.

12. Advantage+ creative enhancements are not mentioned.
- Brand-system §8.12 says to turn them off. Image expansion, visual touch-ups and generated text or overlays would alter scale and copy.
- FIX:
  - Add to §5.5: turn off standard enhancements on every ad.
  - Test 'add catalogue items' as a deliberate cell, given catalogue's 2.28x.

13. None of the output strengthens the catalogue, which earns most of our money.
- FIX: reserve about 10% of output for the catalogue:
  - A2 worn frames and A3 macros uploaded as extra catalogue images, testing a lifestyle first image against the packshot;
  - a catalogue overlay test with price plus the verified offer.

14. The batch rules make results impossible to attribute.
- Each batch must have 5 archetypes and at least 4 products. Batch 1 tests 5 different hypotheses with one ad each on 5 different products.
- FIX: make calibration (batches 1–10) a grid.
  - The same two hero products (Cushion Halo and Brushed), each run across the same 5 archetypes, with fixed copy device and offer.
  - Product spread comes only after an archetype wins.
  - 'One new move per batch' must also apply to what goes live, not only to the critic loop.

15. The improvement loop runs on critic scores alone.
- 100 batches will be finished long before the first 7-day readout. The note that 'purchase data replaces critic scores' never takes effect.
- FIX:
  - Build at most 10 batches ahead of the live waves.
  - From batch 11, each 4-batch cycle must cite the previous wave's purchase, cost-per-add-to-cart and outbound CTR results in its brief.

16. The rubric has no conversion dimension and has never been validated.
- 20% of the weight goes to 'brand' and 'archetype fit'.
- Our earlier sets all scored themselves 9.0–9.5 and none was tested.
- FIX:
  - Add 'Purchase cues' at .15: price legible, offer value stated, product identifiable at 200 px, landing page matches. Cut archetype fit to .05 and brand to .05.
  - Before batch 1, have both critics score the tested set from item 3. If the rubric does not rank the anaar Story, F2 and W1 'not cast' above the eight losers, recalibrate it.

17. There are no rules for killing or scaling an ad.
- FIX: add to §5.6.
  - Kill: no purchase after ₹1,500 (about 2× the account cost per purchase).
  - Advance to stage 2: at least 1 purchase, or cost per add-to-cart below the account median. Pull add_to_cart and initiate_checkout; CTR has not predicted purchases, since the play ads had the top CTR and no sales.
  - Graduate to the evergreen 'Winners' ad set: at least 3 purchases at 1.8x or better after ₹3,000 or more.

18. Reused plates will compete with each other.
- Ads that share a plate will be grouped by Meta's creative similarity and will split delivery. Some plates already ran: the Prism and Woven families sit inside 0.55–0.75x histories.
- FIX:
  - Check each reused plate against past ad creative IDs. Drop plates whose ads lost after real spend.
  - No more than 2 live ads per plate at once.
  - Run copy-only variants as Meta's multiple text options inside one ad, not as separate ads.
  - Count '500' as distinct images times layouts, not copy swaps.

19. The credit plan does not fit our balance or our generation habits.
- The balance read on 19 Nov is 144.46 credits; the plan needs 190.
- A 4-image Nano Banana Pro 2K call is quoted at 8 credits. B1-01 and B1-04 each ask for 4 frames, so batch 1 costs 16 credits, not 4. Run as 4-image calls, 95 frames would cost 760.
- The 65% keep rate is unsupported. The founder kept 23 of 70 colour shots (33%), and the Toggle failed 8 or more times.
- A6 (25 ads) is funded with 4 frames, which would need more than 5 uses each and breaks the 5-use cap. A8's arc has no frames beyond B1-04.
- FIX:
  - Plan about 70 frames at 1–2 images per call (about 140 credits) with a 40% keep rate, so about 28 keepers.
  - Shrink A6, A8 and A13 to what their frames can fund.
  - Move the freed slots to A2, A3 and A4 on existing verified plates.

20. Purchase counts ignore cash-on-delivery losses.
- Meta records a COD order as a purchase when it is placed. A11's '₹0 upfront' line invites COD.
- FIX:
  - Read Shopify orders by utm_content (read-only) for COD share and cancellations or returns to origin. Judge waves on delivered revenue.
  - Hold '₹0 upfront' until those rates are known.

21. Two active ads show reference prices that do not match the store.
- Halo 15s B says '₹1,099 (was ₹2,200)'. The listing says ₹999, compare-at ₹1,669.
- Prism 11s says 'was ₹4,200'. The listing's compare-at is ₹3,999.
- Prices have also moved within weeks: Woven ₹1,199 to ₹1,049, Brushed ₹799 to ₹699, Toggle ₹1,199 to ₹999.
- FIX:
  - Add both active ads to the §8 flags.
  - Keep the price as a template layer filled from a live read at export.
  - Add a weekly price audit of live ads, covering the image and the headline.

22. The plan does not say who sees which ads.
- Our statics ran on mixed audiences (men and women 18–65 all India versus women 18–65 in 7 metros), which confounds the comparisons.
- FIX:
  - Use one fixed test audience: Advantage+ audience with a women 18–54 suggestion, all India.
  - Send A7, A11, A12 and A14 to retargeting (30-day engagers, and people who added to cart without buying) on a small separate budget. Use A1, A2, A3, A5 and A6 for prospecting.

23. Proof options are missing from §8.5.
- Verified per-SKU order counts can be read from Shopify today. The house rule allows verified numbers; the caption rules ban counts, so the owner must choose.
- Creator photos with usage rights (Riya, Ananaya) are absent, though the 'Where is this from?' creator reel had our top CTR (11.47%).
- FIX: add both to §8.5. Add creator stills as an A2 picture source if rights are confirmed.

24. Two anaar figures contradict each other.
- §2 quotes '15 sales at 3.63x lifetime' next to '24 sales' in the last 30 days. A lifetime count cannot be lower than a 30-day count.
- FIX: put a read date on each figure, or drop the older one.

25. The seasonal work is scheduled by batch number, not by date.
- Wedding-season and gifting work sits in batches 41–80, which at a real testing pace falls in 2027.
- FIX:
  - Give occasion slots calendar dates: wedding-guest now, December gifting launched by about 5 Dec.
  - Confirm that the gift box ships, and the courier cut-off, before any gifting copy.

26. Stock is not linked to how many ads are built.
- Cushion Halo has 45 units and sold about 20 through video alone in 30 days. One winning static could take it below 20 within weeks, and 50 queued ads would then be waste.
- Marquise has only 15 gold units.
- FIX: cap queued ads per product at what can run before stock is projected to fall under 20, and tie extra ads to a restock date.

27. Batch 1 does not test what it claims.
- B1-01 claims to test the F2 grammar but bans the lips, which were F2's distinctive feature.
- B1-02 compares a Feed ad with a Story result (W1).
- Two of the five slots go to the weakest-evidence products (Toggle, Woven).
- B1-05 drops the offer, against the draft's own rule.
- FIX:
  - Get the face decision (§8.3) before B1-01, or run lips against jaw-only as a split.
  - Rebuild batch 1 as the item-14 grid.
  - Give B1-05 the verified offer chip.

28. There is no measurement setup.
- FIX:
  - Name every ad: b{nnn}-{slot}_{archetype}_{product}_{plate-id}_{offer}_{hook-slug}.
  - Use utm_content={{ad.id}}.
  - Pull a weekly roll-up by archetype, product and plate, with spend share, purchases, cost per add-to-cart, average order value and COD share.

29. The offer falls below the fold in the ad text.
- B1 primary texts run to about 185 characters, so the offer lands after the roughly 125-character cut-off on mobile.
- FIX: put the verified offer within the first 125 characters, or in the link description, for example 'Cushion Halo Ring · ₹999 · Any 2: 10% off', once the value is verified.

---

# critiques 3

Product-truth and brand review of the draft playbook: 30 defects, each with its fix. Nothing was written to Shopify, Meta or Higgsfield.

**What I checked:**
- Every plate the batch-1 brief and A1/A5 rely on, opened as images.
- Planned text boxes drawn over the B1-02 and B1-05 crops.
- The glyph coverage of all seven kit fonts (with fontTools).
- Velista headline widths against the planned text boxes.
- The primary-text character counts.

Evidence files are in /tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/critic/: sheet1.jpg, sheet2.jpg, b1_02.jpg, b1_05.jpg and c53.jpg.

**A. Breaches of the house rules or the draft's own gates**

1. **A1's existing-plate list breaks the no-water rule and A1's own rules.**
   - performance/plates/colour/53-prism-riviere-bracelet.jpg has clear water droplets beside the paper boats (c53.jpg). It is also a pastel piece on pale blue.
   - colour/03 is food (sugared almonds) on cream. That breaks both "Prism: dark ground only" and the A1 food ban.
   - halo-curve-ring-rhyme.jpg has a brass bowl of jaggery, which is also food.
   - colour/55 is a silver-tone ring on pale lilac-grey: a pale piece on a pale ground, which the rubric caps at 6.
   - colour/15 is a tiny gold bracelet on cream (audit 1 measured it at 2–5% of the frame).
   - colour/51 is gold on cream.
   - **Fix:**
     - Retire colour/53 for good.
     - Remove colour/03, colour/15, halo-curve-ring-rhyme and colour/55 from A1.
     - Keep colour/66 (navy ground, satin bow) and crazy3/08 (deep green clutch) as A1 sources.
     - Reword the food rule as "no pantry or kitchen food; whole flowers or fruit only". The owner should say whether confectionery the founder kept (colour/03) is an exception.

2. **The B1-05 plate (verdant-eternity-band-rhyme.jpg) fails the draft's own gates** (b1_05.jpg):
   - Four-point AI star glints on the ring; §4.0 bans them.
   - The ring is about 26% of the canvas width, under the 35% rule.
   - The brass thali and paan leaf read as food or a puja offering, and the headline names the thali.
   - The ring is magnified but carries no size tag.
   - "THE GREENEST THING" in Velista 72 is about 733 px wide against a 568 px box.
   - The chip carries no BUY2/BUY3 or NAIRA10 offer.
   - The fallback "green glass bangle" plate is not among §5.4's 12 new rhyme plates.
   - **Fix:** swap B1-05 to colour/66 (Ribbon Bead Bracelet, navy, a founder keep; the bracelet spans about 70% of the width).
     - Headline: 'TWO HEARTS. / ONE BOW.' with the Cormorant line 'heart-cut cubic zirconia, 18k gold tone.'
     - Price ₹699.
     - Tag: 'SHOWN MAGNIFIED · BOW 10 × 5.5 MM'.
     - Check it for glints at 100% and re-read stock first (21 units).
   - To keep the ring test instead: budget one new Verdant Eternity rhyme concept on deep green glass bangles, generated at 9:16 with the ring at 35% of the width or more, and retire the thali plate.

3. **The 35%-of-width rule cannot be met by worn rings or earrings.**
   - In the existing cushion-halo-ring-worn.jpg the ring is about 12% of the width. A 12 mm halo in B1-01's jaw-to-chest crop would be about 5%.
   - The rubric cap ("piece under 15% of the frame: max 5") therefore fails B1-01 against its own ship rule (no dimension below 7) before it is generated.
   - cushion-halo-ring-worn and verdant-eternity-band-worn are also on ivory linen, which breaks A2's deep-ground and "no ivory styling" rules.
   - **Fix:**
     - Write a worn-frame rule: the piece is at least 15% of the frame width, or at least 8% with a hairline locator.
     - Exempt worn frames from the 35% rule and from the under-15% cap, in those words.
     - Recrop B1-01 to the hand at the collarbone, about 90 mm wide, so the halo is at least 15% of the width.
     - Move the ivory worn plates out of A2 and into A12 or A13 only.

4. **Cushion Halo "adjustable US 5–9" is printed while the draft itself doubts it.** It appears in B1-01's spec line and primary text, in A7's "One ring. / US 5 to 9." and in A12. But §8.10 flags the K8 SKU suffix and the stray "Adjustable version is live!" copy, and the truth sheet says to confirm all the stock is the adjustable version.
   - **Fix:**
     - Add "all 45 units are the adjustable version" to the §5.5 pre-flight.
     - Until that is confirmed, the B1-01 spec reads '8 mm cubic zirconia · cushion pavé halo · silver tone', and the A7 and A12 Cushion examples drop the sizes.

5. **B1-03's callouts are not listing words.** "CUBIC ZIRCONIA BAR" and "SPRING-GATE RING" break A7's rule that every callout uses listing words; the draft's own flag says the listing omits the stones on the bar.
   - **Fix:** use 'TOGGLE CLASP', 'WEAR IT AT THE FRONT' and '4 MM LINKS · 50 CM'. Add the cubic zirconia bar only after the listing states it.

6. **B1-03 resizes a body photo by hand.**
   - ref-clasp.jpg is a 900 × 780 crop of the clasp on skin. Upscaling it ×1.2 is literally resizing an on-body photo by hand, and it softens the image.
   - The claim that it was cut from listing image hf_20261021… is unverified. listing-0-onbody.jpg is a different, wider neck shot.
   - **Fix:** pull the original from the Shopify CDN. If it is under 1080 px wide, place it at native size inside the 1080 frame with an ink margin.

7. **The offer mechanism is hard-coded and inconsistent.**
   - Every B1 chip prints 'CODE BUY2', but docs/creative/shop-all/research/caption_rules.md rule 5 says "No codes (drop BUY2/BUY3)… applied in your bag", and toggle-15 agrees.
   - B1-03's primary text omits the BUY2 that its chip shows.
   - B1-05 carries no code offer at all.
   - **Fix:** make the chip a variable that the pre-flight resolves, and keep chip and primary text identical. Until it is verified, use the caption-rule wording 'Buy 2, get 10% off', and only once that percentage is confirmed live.

8. **COD wording and length.**
   - All five B1 primary texts end with a bare "COD". Caption rule 6, and the draft's own §5.5, require 'Cash on delivery on serviceable pincodes.'
   - B1-01's primary text is 181 characters, over the 180 limit.
   - **Fix:** use the qualified line, and trim B1-01 (for example, drop "an").

9. **Variant stock is gated at product level, against the user's "only in stock 20 plus" instruction.**
   - No single variant reaches 20 units for Baguette Huggies (10/6/12/0), Droplet (9/11) or Marquise (15/9). The plan still gives them 65 ads and puts Marquise in the calibration batches.
   - The draft contradicts itself:
     - §8.11 says "line-ups only";
     - §5.1 says Marquise "Gold leads";
     - the A10 BUY4 set uses "Marquise gold" (15 units);
     - A13 lists Baguette, but one pair on a body is a single colour.
   - **Fix:**
     - Default all three products to zero ads and move their 65 slots to Cushion Halo, Toggle, Brushed, Verdant Eternity and Woven, unless the owner opts in.
     - If the owner opts in, ban single-variant ads, swap Marquise out of the BUY4 set for Woven, and drop Baguette from A13.
     - Change the compliance gate to "every variant shown has 20 or more units".

10. **The Marquise silver images are AI recolours of the gold** (truth sheet). A14's "Warm or cool? / Wear both." and the "silver beside gold" rule would sell a recolour as a silver product.
    - **Fix:** no silver Marquise imagery until a silver unit has been photographed. Remove Marquise from A14.

11. **Pearl Double Halo copy says "white pearl".** That breaks the binding "shell pearl" wording and can read as a natural pearl.
    - **Fix:** use the product name only, plus 'bright silver tone · cubic zirconia', on the image and in primary text, until the supplier confirms the pearl.

12. **A12's footnote template is wrong for most SKUs.** "*As listed. 18k gold tone plating." is false for the rhodium silver-tone pieces (Cushion Halo, Verdant Eternity, Prism, Serpentine silver). It is unsupported for Pearl Double Halo and Monochrome, whose listings state no plating.
    - **Fix:** write each footnote from that listing's Plating field:
      - '*As listed. PVD rhodium, silver tone.'
      - '*As listed. Bright silver tone.'
      - '*As listed. Gold tone.'

13. **Approximate listing sizes are printed as exact.**
    - Woven: B1-02's tag 'ACTUAL 25 MM', its primary text '25 mm braid', and A12's '25 mm'.
    - Brushed: '14 mm' in B1-04 and A12.
    - The listings say "about 25mm" and "about 14 x 9.8mm".
    - **Fix:** 'SHOWN MAGNIFIED · ABOUT 25 MM ACROSS', 'about 14 mm', and the same for any other "about" figure.

14. **"Woven, not cast." asserts a manufacturing process the listing does not state.** The listing only says braided rope on surgical stainless steel with PVD. It is used in B1-02 and A3, and caption_rules.md uses it as a model line, but nobody has verified it.
    - **Fix:** get supplier confirmation, or use 'Braided, not plain.'

15. **A13's "Click on." for Brushed rests on a hidden hinge that only the fidelity lock mentions.** An earlier brief said to confirm the listing says hinged.
    - **Fix:** use it for Brushed only if the listing confirms the hinge.

16. **A11 offer lines imply terms nobody has verified.**
    - "Your first piece. / Code NAIRA10." implies a first-order-only code. The only live NAIRA10 copy (Core v2) says "10% off any order".
    - "₹0 upfront" and "₹0 shipping" need a COD-fee check and a free-shipping-threshold check, and §5.5 has neither.
    - **Fix:** 'Any piece. / Code NAIRA10.' once the terms are read, and add both checks to the pre-flight.

17. **A9 asks for "a drawn contact shadow", but §4.0 bans pasted shadows** (and the audits flag them as an AI tell).
    - **Fix:** mask the packshot so its photographed shadow comes with it, or generate the piece directly on the flat field.

18. **A5 and the A8 twin depend on crazy3 plates where the piece is tiny.**
    - crazy3/10 (the ring) and crazy3/22 (the huggies) show the piece at about 5% of the frame (sheet1.jpg). crazy3/06 and crazy3/21 were 2–5% in audit 1.
    - Some of these plates were shrunk or re-plated in post (shrink.py and fakeplate.py; crazy3/21 has a pasted shadow).
    - A 1.3× whole-frame zoom cannot lift 5% to 35%, and it drops the effective resolution to about 830 px.
    - **Fix:**
      - Drop crazy3/06, 10, 21 and 22 from A5 and A8.
      - Use a crazy3 plate only when its piece measures at least 20% of the width (crazy3/02, the Toggle with a rose, qualifies).
      - Budget new spotlight frames for the rest.

19. **The occasion copy contradicts the draft's own evidence.**
    - §2 shows generic occasion lines all stayed under 2.2% CTR, and caption rule 2 bans opening with an occasion.
    - Yet the draft uses:
      - A5: "Wear it to dinner…" and "Lights low. / Studs on."
      - A8: "Desk at 9. / Dinner at 9."
      - A10: "One for the desk. / One for the date."
      - Batches 41–80: wedding-season occasion lines.
    - **Fix:** lead with a craft truth or mechanism (for example A5 Cushion: 'One light. / Every facet.'), and let an occasion appear only as the second beat.

**B. Fonts and type**

20. **The kit fonts are missing glyphs the draft uses** (fontTools check on ads-500/kit/fonts):
    - None of the seven files has ₹, ⚠, →, ☀ or ☾. Velista also lacks · and –.
    - So A11's '⚠ CAUSES STARING ⚠' would fall back to a colour emoji, A14's 'Warm → gold tone' falls back to another font, and A8's sun and moon glyphs exist in no kit font.
    - The ₹ fix in §4.0 names no font file.
    - **Fix:**
      - Draw ⚠, the arrows, the sun and the crescent as inline SVG.
      - Commit a ₹-capable font subset (U+20B9, matched to Jost 500) with a unicode-range rule.
      - Never put · or – in a Velista line.
      - Fail any render whose render.cjs output lists a fallback.

21. **B1-04 sets its times in Velista.** The arc headline "ON AT 9 AM. STILL ON AT 2 AM." is in Velista, whose digits are stylised; the brand-system study keeps all numbers in Jost.
    - **Fix:** set the arc in Jost 500 caps tracked .12em, or wrap the digits in Jost spans.

22. **B1-04 prompt risks:**
    - A brushed stainless-steel cube beside brushed-satin gold invites the model to give both the same finish; the truth sheet already notes the satin reading as silver.
    - "Camera at table height looking up" contradicts "contact shadows on the cube top".
    - The cube's front face fills the bottom 15%, exactly where the foot sits.
    - Unlike B1-01, it has no acceptance criteria.
    - **Fix:**
      - Use a 3 cm oxblood lacquer or bone-plaster cube.
      - Set the camera about 10° above the cube's top face.
      - Keep the bottom 22% as empty gradient.
      - Acceptance: satin finish, not mirror; warm-neutral, not orange; each huggie 0.42–0.52× the cube's height; the two match; no glints.

23. **The type ladder breaks inside the draft.**
    - The offer chip is Jost 24, under the 26 px floor, and it is not legal microtext or a size tag. The same goes for A7's second line and A12's micro-qualifier (24).
    - H1 runs at 60–72 (A2), 64 (B1-01), 72 (B1-05) and 50 (B1-04), against a ladder of 84–120.
    - A5 asks for "thin" Velista, but Velista.ttf has one weight.
    - **Fix:** chip at Jost 600 26, an explicit H1 range per archetype, and A5 in regular Velista tracked .12em.

24. **B1-01's headline overflows.** "LOOKS LIKE A PROPOSAL." in Velista 64 is about 773 px wide against a 688 px box. It will wrap and, with the 56 px second beat, spill out of y 900–1070.
    - **Fix:** break it deliberately as 'LOOKS LIKE / A PROPOSAL.' and move the box to y 840–1070.

**C. Brand consistency**

25. **Five typefaces and two colour-token sets work against "one brand system".**
    - Bricolage 800 (A4, A9, A13, A14) and Anton (A10, A11) have never run in a Naira ad, and the brand bible says Naira is "not loud".
    - A8's "Warm Gold to Near-Black" uses the Lac & Bone values (#C2A05A, #3A0F13), which are not kit tokens. A2's cocoa is not a token either.
    - **Fix:**
      - Lock the type to Velista, Cormorant and Jost.
      - Allow Anton only in A11, as a labelled experiment, at most once per batch.
      - Run A8 from --gold #C9A55C to --ink #1A1614.
      - Add a --cocoa token if cocoa grounds are going to recur.

26. **The wordmark stays too small to fix the branding gap.** At 40 px tall the logo is about 179 px wide (4.48:1), which is the 105–170 px range the audits called illegible (the tulip in the I is lost at feed size).
    - **Fix:** 56 px tall on Feed (about 250 px wide), and add a check at 200 px thumbnail size to the batch report.

**D. Plan arithmetic and pre-flight**

27. **The credit maths is wrong.**
    - B1-01 and B1-04 each request 4 frames, so batch 1 costs 8 generations = 16 credits, not 4.
    - At that rate the "95 frames, about 60 keepers" plan yields roughly 24 concepts.
    - Several archetypes have no budget to match:
      - B1-04's arc and every A8 arc plate are missing from §5.4;
      - A6 has 4 hanging frames for 25 ads;
      - A13 says "always new" but has 10 frames for 25 ads, so each image would repeat inside A13, breaking the "at least 2 archetypes per plate" rule.
    - **Fix:**
      - Fix the frames per concept (2 for product-only, 4 for worn) and recompute against the roughly 200 credits available.
      - Add a line for arc plates.
      - Cut A6 and A13 to about 10 ads each, or budget them as concepts.

28. **Story twins contradict the generation settings.** A1, A3 and A5 promise native 9:16 Story twins, while §5.4 generates 4:5 by default.
    - **Fix:** generate every new A1, A3 and A5 frame at 9:16, with the subject inside the central 4:5 window.

29. **The pre-flight and compliance gate have holes.**
    - The banned-word lint skips the Higgsfield prompts, where a colour word can flip the metal and where 'freshwater' sits in tested-prompts.md.
    - The stock gate is product-level only (see item 9).
    - Nothing checks the free-shipping threshold, a COD fee, the NAIRA10 terms or the Cushion Halo adjustable version.
    - **Fix:** add all of these to §5.5 and to the §7 gate.

30. **Factual slips in the plan:**
    - §5.1 calls the Toggle "highest stock"; Woven is higher (89 against 77).
    - Cushion Halo's "24 purchases (2.21x)" merges Halo B (20 sales, 2.21x) with Halo A (4 sales, 0.85x). Both carried the banned "waterproof and tarnish free" text, so the top allocation rests on evidence confounded by the claim.
    - "Verdant: 13 ads, 1 sale" is a family-wide figure, not Verdant Eternity's.
    - The ruby anaar figures mix three dates, and the "lifetime 15 sales" figure is older than the 30-day count of 24.
    - Woven is ruled "texture and monument archetypes only", yet A4, A9 and A12 use Woven examples.
    - A6 hangs Prism, Ribbon and Marquise vertically: bracelets then read as pendants (the identity confusion already flagged on crazy3/25 and X04), and Marquise is really a 41 cm collar with a sideways marquise.
    - **Fix:** correct the figures, date each stat, and limit A6 to Serpentine (both metals), Toggle and Bold Nocturne.

**Checked and found correct:** all 18 prices and stock counts; the archetype totals (500) and product totals (466 + 34); the ring count (125); the kit token hex values; the B1-02 crop and text boxes (they clear the hoops); and B1-01's prompt (metal lock, no face, no glints).