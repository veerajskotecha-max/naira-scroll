# Naira Petite: static playbook for 500 Meta ads (final)

*This is a read-only study dated 19 Nov 2026. Nothing was generated in Higgsfield, written to Shopify or changed in Meta. Board ranks refer to the winners board (artifact 4QL6qL6EkKzrRwxiUsdb4f). Account numbers come from Meta account 903466039148509, pulled on 19 Nov 2026 for 20 Oct to 18 Nov, unless another date is given. Before finalising I re-checked a few things against the repo and the 30-day ad export:*
- *Ad-set spend shares and the Toggle totals.*
- *The `docs/creative/ads-20` judge file (`build/scores.json`) and the frame notes in `build/set1.json` to `set3.json`.*
- *The four ads-20 frames proposed for batch 1. A contact sheet is at `/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/final/b1cands.jpg`.*

*Appendix A lists the review points not applied, or applied only in part, with a one-line reason for each.*

---

## 0. The decision in one screen

1. **Statics underperform, and the two that worked sell products this plan cannot use.**
   - In the last 30 days statics returned 1.02x (₹96,261 spend, 65 purchases). Catalogue carousels returned 2.28x and brought 67% of purchases.
   - The two tested static winners both show ruby baguette tennis pieces:
     - Ruby anaar, a Story with no text: ₹14,248, 24 purchases, 2.29x.
     - Twenty F2, a worn feed card: ₹2,348, 6 purchases, 4.74x.
   - Neither piece is in the stock-20-plus set.
   - What the two share: the most saturated colour in the frame belongs to the piece. Anaar sits on pale cream plaster and F2 on a cocoa ground. In both the piece fills about 55–65% of the frame width, and neither has a headline.
   - Whether that grammar carries over to eligible pieces is the hypothesis that batches 1–10 have to test. It is not a proven control.
2. **Most of our "losers" were never tested.** Meta put most of each ad set's budget on one ad: F2 took 82% of an 8-ad set, and the other seven got ₹29–139 each. The median spend of the 163 ads with no purchase was ₹113. This playbook treats an ad as tested only after ₹1,500 of spend.
3. **The winners board adds moves we have never made:**
   - a graphic layer that makes the claim literal (ranks 1, 40, 55);
   - a monument-scale piece with an honest size tag (26, 42, 95, 190);
   - two-beat headlines (4, 26, 55, 57);
   - numbers taken from the listing (11, 22, 88);
   - honest "physics" and type tricks: levitation (96), frozen motion (66, 109), the product standing in for a letter (155), selective colour (85);
   - a set worn on one body (5, 25);
   - the same body shown twice with one change (20, 21, 92).
4. **The system** has 15 archetypes, one fixed card (F2's own lockup), a light menu and a camera menu, and a per-archetype size rule. Its other rules:
   - every new frame is generated at 9:16 with the subject inside the central 4:5 window;
   - type is limited to Velista, Cormorant and Jost (Anton is a labelled experiment inside one archetype);
   - each ad carries one verified offer, or none while the terms are unverified.
5. **Product scope.** Of the 18 live SKUs with 20+ units, **14 qualify by default.** At variant level, every variant shown must have 20 or more units. That excludes:
   - Baguette Huggies (10/6/12/0);
   - Droplet Open Ring (9/11);
   - Marquise Drop Choker (15/9);
   - Triple Coil Wrap Bangle (20/19; it is also on hold until its turns are counted).

   The owner can opt any of them back in (§8). Six of the 14 are within five units of the threshold.
6. **Volume and pace.**
   - 100 batches of 5. Allocation is gated by stage: about 355 slots are allocated up front and a 145-ad pool is released to whatever sells.
   - Assuming about 95 new Higgsfield images (190 credits), about 36 keeper frames plus about 75 existing verified pictures build the 500. Most pictures have to be used 4–5 times. With about 1,000 credits that drops to about 2 uses per picture (§5.4).
   - The Higgsfield balance read on 19 Nov was 144.46 credits, which buys about 72 images.
7. **Testing cannot happen at ₹3,000 per ad.** Five hundred ads at ₹3,000 would be ₹15 lakh, about 6.6 months of the whole account's spend.
   - The plan uses a fixed test budget of about ₹20,000 a week (today's static share, restructured). That screens about 14 ads a week, so 500 take about 8 months.
   - Production stays at most 10 batches ahead of live results (§5.6).
8. **Before batch 1:**
   - verify the offer terms (value, code or automatic, threshold, COD fee);
   - commit ₹-capable font subsets;
   - run the anchor calibration of the rubric (§7);
   - get owner rulings on face crops and on Higgsfield edit passes. Our best static (F2) and the Cushion frame chosen for B1-01 were both made with an edit pass that shrank the piece (`set1.json` `edit_c`).

---

## 1. What winners do

### 1.1 Visual
- **One claim made literal with one prop or setting:**
  - a sun arc for duration (1), a spotlight for evening (3), a light burst for boldness (4);
  - a ladder for steps (28), a pour for texture (52), a neon window (56);
  - a glass shield for protection (87), ice for cool (100);
  - a cocktail glass for a product named "cocktail" (19), a padlock-shaped pack for "locked in" (82).
- **The product shown with the mark it leaves:** a swatch (67), a lash stroke (77), a mist (66), a drip (108), stripes (120), a pencil drawing through the headline (55, 81).
- **One colour world per frame.** Either tone-on-tone from the pack (22, 28, 52, 53, 54, 9, 19, 35, 74, 100, 110, 127, 135, 153, 190, 195) or one saturated flat field (17, 26, 42, 34, 76, 118). The saturated element is the product or its literal echo.
- **The product as a monument,** tilted and cropped off one or two edges (26, 42, 57, 66, 95, 175, 187).
- **Physics and type tricks that read in under a second:**
  - levitation with a detached shadow (96);
  - frozen motion (66, 109, 117, 131);
  - selective colour (85);
  - an object standing in for a letter (155);
  - the product in costume as another object (47, 72);
  - a prism streak (90);
  - light-burst blades (4).
- **The result as the hero, with no product in frame:** 14, 45, 105, 32, 198, 40, 169, 194.
- **Face and product reading as one unit:** 70, 88, 89, 126, 143, 162, 177, 179.
- **The same subject twice with one change:** 20, 21, 39, 75, 92, 150, 178, 181.
- **What does not transfer to jewellery:** the bottle oversized on an arm (22) and the forced-perspective push toward the lens (24). For jewellery both would misstate scale.

### 1.2 Camera and light
- **Product-only CGI or packshots dominate:** 15 of 19 in the benefit 1/3 group. The product fills 45–90% of the frame height, is tilted 5–40 degrees and is cropped by the frame (1, 26, 42, 52, 95, 122).
- **Hard key, backlight and low hero angles** (1, 3, 15, 175, 187):
  - spotlight on black (3, 166);
  - hard window sun with patterned shadows (72, 83, 91, 123);
  - raking chiaroscuro (124, 106).
- **People** are shot at 70–100 mm, eye level, chest up, often with the face cropped. The product sits at the face plane at true scale in the hand (2, 18, 70, 89, 126, 162). Body fragments always serve a demonstration (11, 22, 40, 86).
- **Evidence frames are locked off**, with identical crop and exposure (20, 21, 39, 75, 178). Macro texture can fill the whole frame (106, 146, 190, 199).

### 1.3 Layout
- **A hard two-zone split** puts product on one side and type on the other: about 12 of 19 in benefit 3/3, plus 11, 22, 57, 66, 68, 77, 87, 107, 108.
- **The headline is the largest type** unless a number is (11, 22, 88, 169).
- **Text covers 10–40% of the frame.** The strongest frames sit at 8–30%: 6 at 8%, 53 at 12%, 67 at 14%, and 76 has tape only.
- **Supporting devices:**
  - hairline leader callouts on a large product (40, 55, 79, 29, 183, 186);
  - numbered or verb triads (22, 28, 52, 66);
  - a two-weight headline, light set-up then heavy payoff (68, 77, 96);
  - a stat system bottom-left: giant numeral, a 2–4 word label, a footnote (2, 7, 41, 113, 119, 21).
- **Almost none carry a CTA button or a price.** Exceptions: 24 (savings band), 5 (offer line), 176 (ribbon).

### 1.4 Branding
- **The pack carries the logo, and corner logos are rare.** One accent colour is lifted from the pack into a keyword or proof chip: Foxtale orange (22, 28, 52), Sugar pink (4, 40, 55), BSC blue (26, 42), mCaffeine blue (11).
- **Series systems:**
  - BSC 26/42 share a face and blue;
  - Foxtale 53/54 share a text slot;
  - Arata 2/7/41/113/119/124 share cream condensed numerals, a rotated "Up to" and tiled sets;
  - Dr. Sheth's 14/45/105 use a mirrored template;
  - Sugar 5/62/80 share glitter serif and sun stripes;
  - Pilgrim 157/180/187 share teal serif, a seal and a footnote.
- **Type:** one display face plus one sans, with the second beat set in italic or the accent colour (4, 40, 55). Rank 107 adds a constant sign-off band.
- **For Naira:** jewellery has no pack, so the canvas must carry a fixed, legible lockup in the same place every time (107).

### 1.5 Copy
- **Two-beat lines:** "Bold Lashes. Zero Smudge." (4), "Stays put. Steals attention." (55), "No drama. Just freshness." (26), "Looks like a pillow. Feels like a hug." (79), "Light on weight / big on journeys" (96).
- **Number first:** 72 Hrs (11), 32% (22), 90 Mins (31), 17% (88), 48 HOURS (162), 40% = … (169).
- **Other devices:**
  - verb triads (22, 28, 52, 66);
  - personification (42, 101), simile (27, 199), pun (47, 82, 142, 155);
  - question and answer (109, 195);
  - self-identification (111, 167);
  - occasion framing (39, 71, 159, 161);
  - Hinglish (152), an idiom made literal (127), familiarity plus news (186).
- **Length:** headlines run 2–11 words, most of them 3–7.

### 1.6 Offer and proof
- **Proof sits beside the claim** as a chip, disc, seal or footnote (1, 11, 57, 77, 99, 138, 157, 187).
- **Small samples are disclosed:** n=15 (14, 45), 30 (11), 35 (21, 61), 50 (46, 154).
- **Review cards carry a name and city** (13, 81, 140, 156).
- **Comparisons** put the brand in colour and the rival in grey (8, 30, 37, 73, 102, 158).
- **Offers** are rarely on the canvas; named packs carry them (5, 25, 58, 59, 139).
- **For Naira:** we have no verified review, rating or count. Listing figures and service facts have to do the proof work. Whether an on-image offer helps is untested (§2), so the plan tests it.

---

## 2. What our own Meta winners and losers say

All figures are for 20 Oct to 18 Nov 2026, pulled 19 Nov, unless dated otherwise. "Tested" means at least ₹1,500 spend. "Share" is the ad's share of its ad set's spend.

**Account**

| Measure | Value |
|---|---|
| Spend | ₹2,28,954 (about ₹53k a week) |
| Purchases | 317 |
| Purchase value | ₹3,65,577 |
| ROAS | 1.60x |
| Cost per purchase | ₹722 |
| Average order | ₹1,153 |
| CPM | ₹373 |
| Link CTR | 2.79% |

Attribution is almost all 7-day click (E2 80 of 83; anaar 21 of 24; every other top ad 100%).

**Weekly ROAS**

| Week | 1–7 Oct | 8–14 Oct | 15–21 Oct | 22–28 Oct | 29 Oct–4 Nov | 5–11 Nov | 12–18 Nov |
|---|---|---|---|---|---|---|---|
| ROAS | 1.67x | 0.75x | 1.19x | 1.66x | 1.74x | 1.31x | 1.71x |

**Format**

| Format | Ads | Spend | Purchases | ROAS | Cost per purchase |
|---|---|---|---|---|---|
| Advantage+ catalogue carousels | 8 | ₹1,03,476 | 213 | 2.28x | ₹486 |
| Video | 13 | ₹15,674 | 32 | 1.75x | ₹490 |
| Static single image | 169 | ₹96,261 (about ₹22.5k a week) | 65 | 1.02x | ₹1,481 |
| Hand-built cover and lookbook carousels | 10 | ₹13,235 | 7 | 0.35x | ₹1,891 |

- 163 ads with no purchase took ₹50,386. Their median spend was ₹113, so most were never tested.

**Placement**

| Placement | ROAS | Purchases | Cost per purchase | Note |
|---|---|---|---|---|
| IG Feed | 1.74x | 181 | ₹666 | |
| IG Reels | 1.82x | 55 | ₹518 | Cheapest per sale, almost only video |
| IG Stories | 1.35x | 75 | ₹945 | Highest link CTR, 3.63% |
| FB Feed | 0.82x | 4 | | |
| Explore | | 0 | | ₹838 spend |

**Tested static winners (at least ₹1,500)**

| Ad | Product | Spend | Purchases | ROAS | Share | What it shows |
|---|---|---|---|---|---|---|
| E2 fruit · ruby anaar · Story 9:16 | Baguette Tennis Bracelet, Ruby (not eligible) | ₹14,248 | 24 | 2.29x | 86% | No text. Ruby bracelet with half a pomegranate on pale cream plaster. |
| Twenty F2 · S1_01 · Feed 4:5 | Baguette Tennis Necklace, Ruby (not eligible) | ₹2,348 | 6 | 4.74x | 82% of an 8-ad set; the other seven got ₹29–139 | Lips-to-chest crop, cocoa ground. Centred card: wordmark, name, ₹2,099, "In red, clear or green", "BUY 2 · 10% OFF • BUY 3 · 20% OFF". No headline. The frame was edited once to make the baguettes about 30% finer. |
| W1 "Woven, not cast." (red) · Story | Woven Gold Hoops | ₹4,863 | 5 | 1.23x | 99% (created 3 Nov in "Winners · Stories") | Texture-led headline on an oxblood dome |
| Shop All C01 "Almost edible" · Story | Prism Rivière | ₹2,372 | 2 | 1.52x | 94% | |
| Static Hoops Apricot quiet · Feed | Woven Gold Hoops | ₹3,215 | 3 | 1.31x | 100% | Was 1.72x on 22 Oct; decaying |
| VK F18 · Feed | Prism Cluster Studs (not eligible) | ₹1,993 | 3 | 2.38x | 42% | |

**Dated reads of ruby anaar** (the older "15 sales at 3.63x lifetime" figure is dropped because it has no date):
- 22 Oct read: 2.94x on 4 sales.
- ads-20 judge note, 14-day window in early November: ₹12,578, 20 purchases, 1.89x.
- 19 Nov pull: as in the table above.

**The rhyme did not travel, even on the same image:**
- Anaar Feed 4:5, same image: ₹123, 0 sales.
- W3 revival: ₹64, 0 sales.

**Tested static losers (at least ₹1,500, 0 purchases)**

| Ad | Spend | Share | Pattern |
|---|---|---|---|
| AB · W1 "Waterproof, for the wedding" · Story (created 12 Nov in a separate ad set) | ₹3,236 | 79% | Claim-led headline, yellow highlighter, category pill |
| VK S5 Prism on powder stripes · Story | ₹2,441 | 52% | Pale pastel piece on a pale ground |
| SA08 2×2 grid · Feed | ₹1,968 | 38% | A catalogue page, not an ad |
| P13 kandil lanterns · Story | ₹1,848 | 11% | Props outweigh the piece |
| C01 "Almost edible" doodles · Feed | ₹1,789 | 34% | Piece small; the Story cut sold 2 |
| AB P2 nutrition-label parody · Feed | ₹1,721 | 23% | Claims panel; 1.01% CTR |
| Old "Almost edible" static | ₹1,547 | 32% | Fatigued: 8 sales since 1 Oct, 0 in these 30 days |
| VK S1 Heartbead on sage · Story | ₹1,540 | 32% | Pale on pale |
| A07 "This is 50 cm" Toggle ruler, Feed carousel + Story | ₹1,474 + ₹1,387 | | Infographic; the headline just read "Naira" |

**The W1 pair is not a clean A/B.** The two W1 ads ran in different ad sets, were created nine days apart, and had different neighbours. Treat it as a direction (texture beat claim on the same photo), not proof.

**Video and catalogue**
- **Halo 15s B (Cushion Halo Ring), created 5 Nov:** ₹5,135, 20 purchases, 2.21x, 98% share, 18 of the purchases on Reels. Its sibling Halo 15s A made 4 purchases at 0.85x. Both primary texts carried the banned "waterproof and tarnish free" line, so their result is confounded by the claim.
- **Prism 11s:** ₹3,008, 7 purchases, 3.46x.
- **Catalogue E2:** ₹36,343, 83 purchases, 2.75x.
- **Core v2** (NAIRA10 plus "every piece here is in stock", linking to the homepage): ₹13,973, 37 purchases, 3.00x.
- **Bestsellers set 2:** 49 purchases, 2.04x.

**By product (non-catalogue)**
- **Toggle Link Chain:** about ₹8.0k for 4 purchases, about 0.3x.
  - T1 "No more hook laga do": Feed ₹1,699, 2 purchases, 0.59x; Story ₹1,820, 2 purchases, 0.66x.
  - T2 and T5: ₹543, 0.
  - Nine other Toggle statics: ₹3.9k, 0 (including A07).
- **Prism Rivière statics and Stories:** 26 ads, ₹28.9k, 9 purchases, 0.55x.
- **Woven Gold Hoops:** 18 ads, ₹13.7k, 8 purchases, 0.75x.
- **Verdant family** (several SKUs): ₹2.5k, 1 purchase.
- **Fruit plates:** most Feed plates got ₹17–475 and were never tested. The only tested non-anaar plate, the kandil Story, made 0 sales.

**What I take from this for statics**
1. The tested winners show one piece, large, whose own colour is the loudest thing in a neutral or dark frame, with no headline.
2. On the same photo, a sensory or craft headline did better than a claim headline. This is directional evidence only.
3. Infographics, grids, doodles and parody panels earned clicks, not purchases.
4. "An offer on every image" is untested. Only F2 carried one on the image, and anaar carried no text at all. The plan tests it.
5. Most ads were never shown enough to judge, so the plan changes the test structure as well as the creative.

---

## 3. What is missing from our creatives, ranked by expected impact

| Rank | Dimension | Gap | Main fix |
|---|---|---|---|
| 1 | Visual | The piece is neither the largest thing in the frame nor the most colourful | Size rule per archetype; the piece owns the colour |
| 2 | Visual / camera | Few, repetitive worn pictures; occasion pictures never given spend | A1, A2, A15; true-size field-of-view rule |
| 3 | Visual idea | Nothing honestly surprising ("crazy" is under-supplied) | A6, A7, A13, A14, A15, A2 selective colour |
| 4 | Product truth | Fidelity breaks on the pieces we would scale | Locks, references and re-checks before generation |
| 5 | Offer | No verified value on the image; ₹699 pieces cannot pay back alone | Verified offer box; bundle-led copy for ₹699 SKUs |
| 6 | Copy | Concept nouns and generic occasions instead of a truth | Craft or mechanism first beat |
| 7 | Camera and light | One camera, one light | Light and camera menus; at least 3 of each per batch |
| 8 | Layout | Explainer archetypes missing, and the ones we tried were too small | A8, A9, A5 only on a large piece |
| 9 | Offer | Bundles priced as sums | A10 sets with the code as the headline |
| 10 | Branding | Eight visual systems, a tiny wordmark, the ₹ glyph falling back to another font | One card, one type set, 56 px wordmark |
| 11 | Platform | Stories mirror-stretched; text under the Reels and Story UI | Native 9:16 frames, text only between y 270 and 1250 |
| 12 | Proof | None verifiable | Listing numerals now; owner decision on proof |
| 13 | Process | Unspent finished ads, self-scored sets, starved delivery | Batch 0, anchor calibration, a test budget |
| 14 | Compliance | Files on record break the house rules | Never reuse finished ads; re-check plates |

**1. [Visual] The piece is neither the biggest thing nor the most colourful thing in the frame.**
- *Our files:*
  - Jewellery takes 2–5% of the frame in `performance/ads/crazy3/06-woven-gold-hoops-night-feed.jpg`, `crazy3/21-brushed-gold-huggies-day-story.jpg` and `colour/15`, `colour/14`, `colour/67`.
  - About 3% in `diwali-10/ads/09`, about 12% in `finished-ads/e2/out/E2_chai_a1.jpg`, and hidden under a stamp in `night-shift/02-the-test/feed/T5-perfume`.
  - Text panels take 40–50% of the night-shift and three-camps cards.
  - The tested losers were concept-led: lanterns, a gummy bowl, a ruler, a nutrition label.
  - Pale pieces on pale grounds lost: VK S5 Prism (₹2,441), VK S1 Heartbead (₹1,540).
- *Winners:* the product fills 45–90% of the frame height (26, 42, 57, 95, 175). In both of our tested static winners the saturated colour was the ruby piece itself, at about 55–65% of the width.
- *Fix (§4.0):*
  - A size metric per archetype.
  - The most saturated colour belongs to the piece or its literal one-to-one rhyme.
  - Clear, pastel and silver-tone pieces go only on dark or flat saturated grounds.
  - No text ever touches the piece.

**2. [Visual / camera] Worn pictures are rare and repetitive, and the occasion pictures we made never got spend.**
- *Our files:*
  - The 26 worn performance ads share one ivory shirt and low bun (audit sheet `s6_worn.jpg`).
  - Scale failures: `lilac-papillon-ring-worn-feed.jpg` reads at about 32 mm against a true 20 mm; the Soleil pendant came out at 32–34 mm against 18 mm.
  - The ads-20 occasion set got almost nothing. S2_06 Verdant mehendi was the judge's joint top pick (8.20) and spent ₹0. S3_12 Brushed (8.20) spent ₹0. S1_04 Cushion (8.05) spent ₹0. S2_10 Verdant Circlet Banarasi spent ₹69.
  - The account's top CTR is a creator reel ("Where is this from?", 11.47% CTR, 2.36% outbound).
- *Winners:* 24 of 200 are face, product and one line (70, 88, 89, 126, 148, 162). Body macros with callouts (40, 141).
- *Fix:*
  - A1 Product Card and A2 Worn Editorial, generated at true size with the field of view stated in centimetres.
  - A15 Phone POV / Mirror.
  - A Batch 0 pass over unspent finished ads (§5.0).
  - From batch 1, one occasion picture per batch while wedding season lasts.

**3. [Visual idea] Nothing honestly surprising.**
- *Our files:*
  - "Crazy" in the archive meant pun props: crazy13 butterfly, crazy04 bottle, crazy36 cuff. These were drawn 1.5–2.6× too large.
  - Or founder-rejected props: shoes, forceps, nimbu-mirchi, a toothbrush.
  - The one surprising honest image is `diwali-10/ads/10-bold-nocturne-bracelet-feed.jpg`, the bracelet as the only moon.
- *Winners:* levitation (96), frozen motion (66, 109, 117, 131), selective colour (85), an object as a letter (155), a spotlight (3), hazard tape (76), a product splitting the headline (55).
- *Fix:* the crazy set is A6, A7, A11-tape, A13, A14, A15 and A2 selective colour. Every one keeps the piece at true size and as the hero, with one impossible-but-honest idea.

**4. [Product truth] Fidelity breaks on the pieces we would scale.**
- *Our files:*
  - **Toggle:** the clasp is drawn as a plain ring with a long bar on about 20 cards: `night-shift/03-the-clasp/feed/K1-toggle` (its callout reads "BAR · ABOUT 15MM"), A3-gold, all of `06-on-every-skin`, G2-chain, M3-one-neck, red-room R4, `keep-it-on/07-sweat`. `worlds-and-hours/feed/C5-link` shows no bar at all. `concept-camps/build/sheet_lines.json` logs eight or more failed Toggle renders.
  - **Stale size locks:** Brushed is listed at about 14 × 9.8 mm, not 12 mm; Verdant Circlet at 16.8 mm, not 20 mm.
  - **Heartbead** reads as three different products across sets.
  - **Listing contradictions:** Triple Coil turn count; Cushion "adjustable" against its K8 SKU suffix; Marquise silver photos that are recolours of the gold.
- *Winners:* proof sits on the visible part (60's dashed rings, 145's dimension lines, 79's cutaway).
- *Fix:*
  - Lock every prompt to the 19 Nov truth sheet. Slot 1 holds the approved listing photo, slot 2 a detail of the same piece only.
  - Gate the Toggle on the clasp reference (`concept-camps/build/refs/toggle/ref-clasp.jpg`).
  - Re-measure every reused plate.
  - Keep the variant-level stock gate.

**5. [Offer] No verified value on the image, and the cheapest pieces cannot pay back alone.**
- *Our files:*
  - NAIRA10, BUY4, COD and free insured shipping appear on no image in about 400 files.
  - `night-shift/07-the-light` argues against offers.
  - The one on-image offer, F2's box, states the value ("BUY 2 · 10% OFF • BUY 3 · 20% OFF").
  - W1's creative 1514460987246299 says 20/30% where the other ads say 10/20%.
  - The two ₹699 pieces: ₹699 less 10% is ₹629, below the account's ₹722 cost per purchase.
- *Winners:* a live-terms band (24), a ₹0 antithesis (136), a disc on a panel edge (57), a named edit (5).
- *Fix:*
  - One offer box stating the verified value, resolved at pre-flight, or none while the terms are unverified.
  - Test cells: offer box on against off, and BUY2 against NAIRA10.
  - Brushed and Ribbon ads lead with bundle value and are judged on order value.

**6. [Copy] Headlines name concepts instead of giving a reason to buy.**
- *Our files:*
  - Concept nouns: "APRICOT.", "LILAC.", "SAGE.", "THE CALLIPER.", "#C48B5F.", "QUIET.".
  - Generic occasion lines ("Make an entrance.", "Black tie.", "RSVP: yes.") all stayed under 2.2% CTR.
  - S1_01 to S1_05 have no headline. That is not automatically a weakness: F2 sold without one, so the plan tests it.
  - "X, not Y" lines reached 5.81–7.25% CTR but were shrunk into lowercase corrections, and the correction formula is worn out (`finished-ads/review_r24.json`).
  - "Woven, not cast." asserts a manufacturing process the listing does not state.
- *Winners:* two-beat lines (4, 26, 55, 57, 79), number first (11, 22, 88), personification (42).
- *Fix:*
  - The first beat states a listing-verifiable craft fact, benefit or mechanism in 2–6 words.
  - An occasion appears only as a concrete second beat or in the picture.
  - Process claims wait for supplier confirmation.

**7. [Camera and light] One camera and one light.**
- *Our files:*
  - A 30–45 degree tabletop, soft window light from the upper left and cream plaster across about 280 concepts.
  - 16 of 21 E2 feed ads sit on a pale neutral ground.
  - The draft of this playbook itself mandated "one warm key plus one specular kick" everywhere.
- *Winners:* a spotlight on black (3), hard sun with gobo shadows (72, 91, 123), low hero angles (1, 15, 175), a saturated flat field (17, 26, 118), macro texture (106, 190).
- *Fix:* every ad declares one light from the L1–L7 menu and one camera from C1–C6. At least three different lights and three different cameras per batch.

**8. [Layout] Explainer archetypes are missing, and the ones we tried were too small.**
- *Our files:*
  - X07 callouts were cut because the marks landed on the metal.
  - A07's ruler, P2's label and SA08's grid all lost with a small product.
  - Never made: same-body evidence, a decoder, callouts on a frame-filling piece.
- *Winners:* callouts and equations are 38 of 200 (40, 79, 29, 48, 169). Before/after is 21 of 200 (20, 21, 92). Decoders: 50, 36, 51.
- *Fix:* A8, A9 and A5 are allowed only on a piece that fills the frame, at 12–25% text.

**9. [Offer] Bundles are priced as sums.**
- *Our files:* `night-shift/05-the-layer` "THE STACK ₹2,998" and `worlds-and-hours/story/D5` "₹7,794". BUY2 and BUY3 appear only in primary text; BUY4 never appears.
- *Winners:* an occasion map (25), an equation (58), a staircase (59), a named edit (5).
- *Fix:* A10 sets show the code as the headline, never a price sum. The set appears as one photographed group at true relative scale, or one body wearing the whole set. No tiles.

**10. [Branding] There is no single brand system.**
- *Our files:*
  - About eight visual systems are in use.
  - The wordmark is 105–170 px wide and wanders between corners. It is missing on `ads-20/ads/S2_08`'s Story and lost on a white shirt in `night-shift/04/M3`.
  - No kit font has the ₹ sign (it falls back to Inter). Velista has no middle dot, en dash, arrows, warning sign, sun or moon, and draws a "TS" swash at zero tracking.
- *Winners:* series templates (Arata, Dr. Sheth's, BSC) and a constant sign-off (107).
- *Fix (§4.0):* one card (F2's), a 56 px wordmark, Velista, Cormorant and Jost only, ₹ subset fonts, inline SVG icons.

**11. [Platform] Stories and Reels are built badly.**
- *Our files:*
  - E2 Stories are 4:5 plates mirror-extended to 9:16: `E2_duo_a1-story` has a mirrored floor and `E2_tubogas` a dead bottom third.
  - Name, price and CTA sit under the reply bar on `night-shift/10/story/A1` and `APRICOT-A1-story`.
  - Reels is our cheapest placement per purchase, yet nothing is composed for it.
- *Fix:*
  - Generate every new frame at 9:16 with the subject inside the central 4:5 window.
  - Story and Reels text only between y 270 and 1250.
  - Never stretch or mirror a frame.

**12. [Proof] We have no proof we can verify.**
- No reviews, ratings or counts exist, and no review app is installed.
- Listing figures (A5 numeral, A8 callouts) do the proof work now. The other proof options are owner decisions (§8).

**13. [Process] Our test structure cannot tell good ads from bad ones.**
- Finished, judged ads never got spend (S2_06, S3_12, S1_04).
- Every night-shift and three-camps set scored itself 9.0–9.5.
- The ads-20 judge put the anaar Story (6.15) below ads that sold nothing.
- Meta starved most ads in shared ad sets.
- *Fix:* Batch 0, anchor calibration of the rubric, one ad per ad set, a fixed test budget (§5).

**14. [Compliance] Files on record break the house rules.**
- Water and colour-hold words: `ten-creatives/feed/A1`, A3, A4, A5; `night-shift/02` (all five cards) and `10/A1`–`A3`; red-room R1, R2, R4; the whole keep-it-on premise; `finished-ads/ads.json` P09.
- A banned word in `lilac-papillon-ring-crazy13` (Feed and Story, `build/meta.csv` lines 806 and 809, `copy.json` line 2991).
- "RUBY" in the spec line of `diwali-10/01`.
- Water droplets in `colour/53`.
- *Fix:* never reuse a finished ad without re-checking it; re-check every plate with the reuse lint (§5.5).

---

## 4. The Naira static system

### 4.0 Rules for every archetype

**Canvas and safe areas**
- **Feed master:** 1080 × 1350. Text safe area x 72–1008, y 84–1266.
- **Story and Reels twin:** 1080 × 1920, from the native 9:16 frame. Text only between y 270 and 1250. Never stretched, mirrored or outpainted.
- **New frames:** generated at 9:16 with the subject inside the central 4:5 window (y 285–1635 of the 9:16 frame) so one generation serves both formats.

**Size metric** (it replaces the draft's single 35% rule)
- **Product-only frames:** the piece spans at least 35% of the canvas width. Hanging or linear pieces may instead cover at least 25% of the frame area.
- **Worn frames:** the prompt states the field of view in centimetres:
  - ring: about 9–10 cm, hand only;
  - earring: about 12 cm, ear and jaw;
  - pendant: about 18 cm;
  - collars: jaw to chest.
- **Worn key detail:** at least 12% of the canvas width, target 15%. From 8% to 12% it is allowed only with a hairline locator (2 px line ending in a 10 px open circle, after rank 148). Under 8% the frame fails.
- **Worn scale:** within 1.2× true size against the body by pixel ruler. Frames that fail are discarded, never edited (the edit-pass question is §8).

**Size honesty on product-only frames**
- Prefer a known-size object in frame: a jasmine bud (about 2 cm), a cowrie, a sugar crystal or a fingertip. Never coins.
- Size tag when the piece is shown larger than life. Trigger: more than about 19 px per listed mm. A 1080 px image is about 6.8 cm wide on a phone, so life size is about 16 px/mm.
- Tag style: two lines in a 2 px hairline box, Jost 500 caps, 30 px, tracked .12em: "SHOWN MAGNIFIED" / "ABOUT 25 MM ACROSS". Write "about" wherever the listing does.

**Picture rules**
- The most saturated colour belongs to the piece or its literal rhyme. Clear, pastel and silver-tone pieces go only on dark or flat saturated grounds.
- Universal rules: gold renders warm-neutral, never brassy or orange; a true contact shadow; no AI star glints, floating props, pasted shadows or drawn shadows.
- No water, droplets, splash, ice, shower, pool or wet skin anywhere (§8).
- Every prop passes the one-second test. It is either where the piece is worn or given, a true look-alike of its shape, name or material, or a whole flower or whole fruit in the stones' colour.
- Founder-reject list (props never used): pantry or kitchen food, shoes, medical tools, nimbu-mirchi, toys, bathroom objects, puja objects, anything that reads as a face or body, pun-only props, flowers that swamp the piece, silk knots that read as ties, real brands, coins.

**Light menu (each ad declares one)**

| Code | Light |
|---|---|
| L1 | Single hard spot or chiaroscuro |
| L2 | On-camera direct flash with a hard drop shadow |
| L3 | Two-colour gel rim on a dark ground |
| L4 | Hard sun through a jaali or cane gobo |
| L5 | Backlit rim with bloom |
| L6 | Soft top-down flat lay |
| L7 | Soft directional window or beauty key (the old house light; at most 2 per batch) |

**Camera menu (each ad declares one)**

| Code | Camera |
|---|---|
| C1 | 90° top-down |
| C2 | Low hero at 10–15° |
| C3 | Eye-level front-on |
| C4 | 85 mm worn |
| C5 | 100 mm macro |
| C6 | Phone POV or mirror |

**Type, locked to three families**
- Velista (display caps), Cormorant Garamond (italic second beat, card price) and Jost (everything else).
- Anton only in A11 as a labelled experiment, at most once per batch. Bricolage is retired.
- Velista lines never contain digits, ₹, middle dots or dashes. Set Velista with letter-spacing .02em or more and `font-variant-ligatures: none`.

| Role | Face | Size at 1080 wide |
|---|---|---|
| H1, worn and rhyme (A2, A3, A6) | Velista caps | 64–84 |
| H1, macro, split, personality (A4, A5, A12) | Velista caps | 96–120 |
| H1, in-word (A14) | Velista caps | cap height = piece height (about 240–320) |
| Second beat | Cormorant Garamond italic 500 | 0.6–1.0 × H1, minimum 44 |
| Listing numeral (A5) | Jost 300 | 240–300 |
| Card: name | Jost 500 caps, .2em | 26 |
| Card: price | Cormorant Garamond 500 (₹ from a Noto Serif subset) | 56 |
| Card: one line | Jost 400 | 26 |
| Offer box | Jost 500 caps, .14em, 2 px hairline, padding 14/24 | 26 |
| Callouts | Jost 500 caps, plus Jost 400 | 26 |
| Size tag | Jost 500 caps, .12em, 2 px hairline | 30 |
| Footnote | Jost 400 | 22 |
| Poster H1 (A11 only) | Anton | 140–200 |

- Floor: 26 px for everything except 22 px footnotes.
- At most four text elements: the headline with both beats counts as one, a callout set as one, the card as one, the size tag as one.

**The Naira card (fixed on every ad; it is F2's lockup, measured from `ads-20/ads/S1_01_ruby_necklace_feed.jpg`)**
- Centred on x 540. Feed block y 880–1200:
  - wordmark PNG 56 px tall (about 250 px wide);
  - name;
  - price;
  - one line (a listing fact or variant line);
  - offer box.
- When a headline sits in the top zone, the wordmark moves to top-centre at y 84 (the S2_06 pattern) and the card keeps name, price, line and offer box.
- Scrim: a gradient in the ground colour from 0% at y 760 to 60% at y 1350, only if the photo is busy under the card.
- Story block: y 1000–1250.
- Logo choice: `logo_white` on dark grounds, `logo_ink` on light ones.
- No CTA button in the image; Meta adds "Shop Now".
- Type on dark grounds: bone #F4F0E8, accent --gold-light #E4C889. On light grounds: ink #1A1614, accent --coral-deep #C8664A or the stone hue.

**Offer box**
- One variable, resolved at pre-flight (§5.5), always stating the verified value. Examples: "BUY 2 · 10% OFF • BUY 3 · 20% OFF" (F2's wording) or "CODE NAIRA10 · 10% OFF".
- Drop the word "CODE" if the discount applies automatically in the bag.
- Until the value is verified, print no offer box.
- The box is omitted in test cells and on Stories with no text.

**Colour tokens**
--oxblood #6E1F23, --plum #4A2540, --terracotta #B5502F, --saffron #E8A33A, --sage-deep #5E7A6C, --sky #9EC3D6, --pista #B9C98A, ink #1A1614, bone #F4F0E8, --gold #C9A55C, --gold-light #E4C889, and a new --cocoa #3B2620 (sample it from S1_04 before committing).

**Kit fixes before batch 1** (all in `docs/creative/ads-500/kit/`)
- Commit ₹ subsets: Noto Sans U+20B9 matched to Jost, and Noto Serif U+20B9 matched to Cormorant, each via `unicode-range`.
- Inline SVG for ⚠, →, the sun and the crescent. No emoji fallback.
- Make `render.cjs` fail any render whose output lists a font fallback.
- Measure SVG text with `getComputedTextLength`, because `data-fit` does not see SVG.
- Add a `.card` component at the measurements above.
- Turn ligatures off for Velista.

### A1 · Product Card (F2 grammar, no headline)
- **Borrows:** our F2 (4.74x, the only on-image offer that sold); board 11 (product plus proof chip), 107 (constant sign-off), 13 (product held like a trophy).
- **Layout:**
  - Full-bleed worn or product frame.
  - No headline.
  - The card only, centred at y 880–1200.
  - Text share 15% or less.
  - Story twin: the native 9:16 frame with the card at y 1000–1250, or with no text at all.
- **Camera and light:** C4 worn on dark grounds (cocoa, ink, oxblood, plum, sage-deep) under the worn size rule; or a C5 product macro. Light L7, L1 or L5.
- **Palette:** dark ground, bone type, the piece's colour as the only saturated element.
- **Copy (the card's one line):**
  - "8 mm cubic zirconia · silver tone" (Cushion Halo)
  - "about 14 mm · brushed satin, 18k gold tone" (Brushed)
  - "emerald-green cubic zirconia · adjustable US 5 to 9" (Verdant Eternity)
- **Suits:** all 14. Saturated-stone pieces first (Verdant Eternity, Verdant Circlet, Halo Curve, Monochrome); clear and silver-tone pieces only on dark grounds.
- **Picture source:** existing frames (ads-20 S1_04, S2_06, S2_10, S3_12; listing worn images for Verdant Circlet, Pearl Double Halo and Monochrome) plus new worn frames.
- **Failure checks:** the piece under the worn metric; the card over the piece; a pale piece on a pale ground; a stale price; an unverified offer box; lips or face beyond the §8 ruling.

### A2 · Worn Editorial (headline plus card; selective-colour variant)
- **Borrows:** F2 and the Halo video hook ("Looks like a proposal."); board 88 (giant lower-third type over a close-up), 148 (leader line to a tiny piece), 11, 40, 141, 70; 85 for the selective-colour variant.
- **Layout:**
  - Headline either just above the card (y 680–860, clearing the piece by at least 120 px) or top-centre with the wordmark at top (the S2_06 pattern).
  - Velista 64–80, two lines, with a Cormorant italic second beat at 48–56 in the accent colour.
  - An optional hairline locator when the key detail is 8–12% of the width.
  - Text share 22% or less.
- **Camera and light:**
  - C4, generated at true size with the field of view in centimetres and the skin tone named in the prompt.
  - Styling varies every time; never the ivory shirt and low bun again.
  - Light L1, L4, L5 or L7.
  - In season, an occasion setting: mehendi, haldi, sangeet, reception, gifting.
- **Selective-colour variant (15 ads or fewer):**
  - A colour grade on a generated worn frame: black and white except the stone or metal. Grading only, no geometry change.
  - Only for coloured pieces: Verdant Eternity, Verdant Circlet, Halo Curve, Monochrome gold tone, Brushed.
- **Copy formula:** a craft truth or benefit as the first beat; a concrete moment only as the second beat.
  - "LOOKS LIKE / A PROPOSAL." + "priced like a present." (Cushion Halo)
  - "GREENER THAN / THE MEHENDI." (Verdant Eternity: the colour truth leads, the moment follows)
  - "TWO STONES. / ONE CURVE." + "tiger eye and champagne crystal." (Halo Curve)
- **Suits:** all 14. Rings, studs and pendants first.
- **Picture source:**
  - Existing: ads-20 S1_04 and S2_06; S2_10; S3_12 (subject to the face ruling); listing worn images; `prism-riviere-bracelet-worn` (dark-ground crop only).
  - Not for A2: `cushion-halo-ring-worn` and `verdant-eternity-band-worn` (ivory linen) and `woven-gold-hoops-worn` (ivory shirt and bun). They may serve A5 photo zones only.
  - New: worn frames per §5.4.
- **Failure checks:** over 1.2× true size; face beyond the ruling; skin that looks generated (S4_17); type on the piece; repeated styling within 10 batches; a generic occasion line as the first beat.

### A3 · Literal Rhyme (with a no-text Story)
- **Borrows:** our anaar (24 purchases, 2.29x as a Story; its Feed version sold nothing); board 67 (stone-colour slab), 74 (monochrome ingredient world), 99, 87, 27, 53.
- **Rule:**
  - One-to-one rhyme: the prop's units match the stones in size, shape and colour, as the arils matched the baguettes.
  - The piece's colour is the saturated element. The prop never outweighs the piece.
  - Whole flowers or whole fruit only.
  - Conceptual rhymes (a dandelion, a thali) move to A4 or A6.
- **Layout:**
  - Full bleed, the piece in the lower-middle third.
  - Headline top-left (x 72–700, y 96–330): Velista 72–84, two lines, with an italic material truth under it.
  - Card.
  - Text share 14% or less.
  - The Story twin is the native 9:16 frame with zero text and no logo. A3 tests Stories first, because the rhyme did not carry to Feed.
- **Camera and light:** C5 at 45 degrees or C2 at 15 degrees. The piece at 35–55% of the width. Light L4, L1 or L7.
- **Palette:** the rhyme hue from the stones, on a neutral or dark ground.
- **Copy formula:** an object line with a twist, then the material truth.
  - "TWO HEARTS. / ONE BOW." + "heart-cut cubic zirconia, 18k gold tone." (Ribbon Bead, `colour/66`, navy satin bow)
  - "GREEN ON / GREEN GLASS." + "emerald-green cubic zirconia, silver tone." (Verdant Eternity on stacked green glass bangles)
  - "BLACK. WHITE. / GOLD TONE." (Monochrome Enamel Hoops, top-down on zebra-crossing paint)
- **Suits:** Verdant Eternity, Verdant Circlet, Monochrome, Ribbon, Halo Curve, Prism (dark grounds only).
- **Picture source:**
  - Existing, re-checked: `performance/plates/colour/66-ribbon-bead-bracelet.jpg` (founder keep; the bracelet spans about 70% of the width).
  - Struck, with reasons:
    - `colour/53`: water droplets.
    - `colour/03`: sugared almonds on cream. Food and a pale ground; a founder-keep exception is an owner question.
    - `colour/15`: the piece is 2–5% of the frame.
    - `colour/55`: silver on pale lilac.
    - `halo-curve-ring-rhyme`: jaggery.
    - `verdant-eternity-band-rhyme`: thali and paan, star glints, 26% of the width.
    - `brushed-gold-huggies-rhyme`: cashews.
    - `verdant-eternity-band-play`: okra.
    - `crazy3/08`: the piece is 8–12% of the width.
  - New: Verdant Eternity on green glass bangles; Monochrome on zebra paint.
- **Failure checks:** the prop outweighs the piece; food or puja reading; a pale piece on pale; the prop drawn at the wrong relative size.

### A4 · Monument Macro
- **Borrows:** board 26 and 42 (monument crop), 95 (abstract crop plus a two-word claim), 106 (texture wall plus numerals), 190 ("shown magnified · actual X mm"); our W1 texture-led direction.
- **Layout:**
  - The piece fills 60–90% of the frame, tilted 10–35 degrees and cropped by one or two edges.
  - H1 in the calm corner: Velista 96–120, two lines.
  - Second beat in Cormorant italic 48.
  - Size tag next to the piece, then the card.
  - Text share 18% or less.
  - Story twin: the native frame with the wordmark only.
- **Camera and light:** C5, product only. L1 hard raking light, L4 gobo (a cane-blind gobo throwing tiger stripes across the Halo Curve) or L3 gel rim.
- **Palette:** the piece's complement or deep shade. Gold tone on oxblood, terracotta or plum; silver tone on plum or ink.
- **Copy formula:** a craft truth in listing words.
  - "BRUSHED, / NOT POLISHED." (Brushed: the listing says "soft brushed satin, not mirror polished")
  - "BRAIDED, / NOT PLAIN." (Woven. "Woven, not cast." only after the supplier confirms the process.)
  - "PAVÉ ON THE / SHOULDERS TOO." (Cushion Halo)
- **Suits:** Brushed, Cushion Halo, Verdant Eternity, Verdant Circlet, Halo Curve, Bold Nocturne, Monochrome, Woven (texture only), the Toggle clasp (after its gate), Prism halos.
- **Picture source:**
  - Existing: `colour-camps/plates/APRICOT/peach_E20267O_S3_a2.jpg` (Woven; mid-tone peach); `colour-camps/plates/SAGE/sage_FE02847B_S3_a2g.jpg` (Verdant Circlet); `edition-two-listings/exports/bold-nocturne-drops-04.jpg`; listing detail images. Crop each from the original at native resolution only.
  - New: the Halo Curve cane gobo; Brushed and Cushion macros.
- **Failure checks:** a missing size tag (worlds C4 made 12 mm huggies read as cuffs); the object unreadable at 200 px; brushed metal rendering as mirror; an unverified process claim.

### A5 · Truth Split (two-beat or listing numeral)
- **Borrows:** two-beat lines 4, 26, 55, 57, 79, 17; numerals 11, 22, 88, 106 and Arata 2/7/41/119; two-zone layouts 22, 57, 66, 68, 77.
- **Layout:**
  - Photo zone 58% (x 0–626) and a flat colour type zone 42%. A top/bottom split is fine for vertical pieces.
  - Type zone, one of two options:
    - (a) H1 in Velista 96–110, two lines, with the second beat in Cormorant italic at the same size;
    - (b) a numeral in Jost 300 at 240–300, a 2–4 word Jost 30 label at cap height, and a Jost 22 footnote.
  - The card centres in the type zone.
  - Text share 25–35%.
  - Numeral ads are capped at 12 until one wins in a wave.
- **Picture:** any verified plate cropped so the piece fills at least 50% of the photo zone's width. This is the main home for the ivory-linen worn plates.
- **Palette:** the type zone is the deep shade of the photo's ground.
- **Copy formula:** a gain then the absence of a pain; or a listing numeral that swallows its unit.
  - "NO OCCASION. / JUST TUESDAY." (Brushed)
  - "LOUD TEXTURE. / ZERO STONES." (Woven: the listing says no stones)
  - "4" + "g on the finger, two stones." with the footnote "*As listed. 18k gold tone PVD on surgical stainless steel." (Halo Curve)
- **Valid numerals:**
  - about 25 mm (Woven); 50 cm (Toggle); about 14 mm (Brushed); about 23 mm (Bold Nocturne);
  - 16–19 cm (Ribbon); US 5–9 (Verdant Eternity, Halo Curve; Cushion after the K8 check);
  - 10 mm (the Serpentine stone); 16.8 mm (Verdant Circlet); 4 g (Halo Curve); ₹699 (Brushed, Ribbon).
- **Footnotes by plating field:**
  - "*As listed. PVD rhodium, silver tone."
  - "*As listed. 18k gold tone PVD on surgical stainless steel."
  - "*As listed. Bright silver tone."
  - "*As listed. Gold tone."
- "Steel inside. / Gold tone outside." is allowed only where the listing states surgical stainless steel and PVD gold tone.
- **Suits:** all 14; Woven only with texture lines.
- **Picture source:** existing plates only.
- **Failure checks:** more than four text elements; any beat implying water or colour hold; a stale figure; a footnote with the wrong plating; a figure that reads as a percentage claim.

### A6 · Single Spotlight
- **Borrows:** board 3 (one of the best three), 166, 116 (with chiffon in place of a splash), 100.
- **Layout:**
  - 70–90% dark. The piece on a round bone riser, low centre, at least 35% of the width.
  - Headline in the upper third, staggered: Velista regular 64–80 tracked .12em in gold-light, with a Cormorant italic subline in bone at 44.
  - Card.
  - Text share 14% or less.
  - Story twin with no text.
- **Camera and light:**
  - C3 slightly above eye level, normal lens.
  - L1: one hard spot from the top right with a visible bloom and a long shadow toward the camera.
  - Prism variant for Prism and Cushion: a glass prism throws one spectrum band across ink. The light is generated in the scene, never painted onto the stones.
- **Palette:** near-black, ink, plum or oxblood, with gold-light and bone type.
- **Copy formula:** the mechanism or craft first.
  - "ONE LIGHT. / EVERY FACET." (Cushion Halo)
  - "PLAIN LINK. / PAVÉ LINK." (Bold Nocturne: the listing describes a polished oval link over a pavé oval link)
  - "TWO BANDS. / ONE LIGHT." (Pearl Double Halo)
- **Suits:** Cushion, Serpentine (both metals), Bold Nocturne, Pearl Double Halo, Prism, Halo Curve, Brushed.
- **Picture source:** new frames only. The crazy3 night plates are prop still lifes with the piece at 8–12% of the width; only crazy3/02 (Toggle) and crazy3/04 (Prism) are large enough, and only as A4 sources.
- **Failure checks:** the piece too small in the void; the logo lost; crushed blacks swallowing the metal; brassy gold.

### A7 · Split Headline (the piece cuts the type)
- **Borrows:** board 55 (one of the best three), 81, 4.
- **Limits:** only Serpentine (both metals), Bold Nocturne and the Toggle (after its gate). Never bracelets or the Marquise collar.
- **Layout:**
  - The piece hangs from the top edge on the centre axis.
  - Word 1 sits top-left at y 120.
  - Words 2 and 3 sit left and right of the piece at about two-thirds height: Velista 110 and Cormorant italic 110.
  - The chain tail coils into an S below.
  - Size tag, then the card.
  - Text share 20–25%.
- **Camera and light:** C3 slightly high. Hard side light from the left (L1), long shadow to the right, on bone plaster or a saturated ground. Product only.
- **Copy formula:** three opposed or alliterative words.
  - "SMALL STONE. / SERIOUS | SPARKLE." (Serpentine)
  - "PLAIN LINK, / PAVÉ | LINK." (Bold Nocturne)
  - "BAR | THROUGH / RING." (Toggle)
- **Picture source:** new.
- **Failure checks:** the chain reads as a bracelet (crazy3/25 did); an oversized pendant without a tag; type colliding with the chain.

### A8 · Callout Anatomy
- **Borrows:** board 40, 79, 29, 60, 145, 183, 186. It corrects our A07 ruler (₹2,861, 0 purchases, small product, headline "Naira").
- **Layout:**
  - The piece covers at least 50% of the frame width.
  - At most three callouts: Jost 500 26 caps plus one Jost 400 26 line.
  - 2 px leaders end in 10 px open circles on metal edges, never on stones.
  - H1 in Velista 84–96, one or two lines, top or in a bottom band.
  - Card.
  - Text share 20% or less.
  - Sent to retargeting audiences (§5.6).
- **Camera and light:** C5 at a 3/4 high angle of about 30 degrees on bone or one field, or a true-size worn macro. L7 with one hard specular, or L1.
- **Copy formula:** the mechanism as the headline; every callout in listing words.
  - "ONE STUD, / THREE PARTS." with "10 MM EMERALD-GREEN CUBIC ZIRCONIA", "OPEN CIRCLET OF CLEAR CUBIC ZIRCONIA", "WHITE SHELL PEARL" (Verdant Circlet)
  - "TWO STONES. / ONE OPEN BAND." with "TIGER EYE, ABOUT 11.8 MM", "CHAMPAGNE CRYSTAL", "OPEN BAND · US 5 TO 9" (Halo Curve)
  - "FRONT / TOGGLE." with "TOGGLE CLASP · WORN AT THE FRONT", "4 MM PAPERCLIP LINKS", "50 CM · 18K GOLD TONE PVD" (Toggle, after its gate). The "hook laga do" line is retired: T1 made 0.59–0.66x on ₹3.5k.
- **Suits:** Verdant Circlet, Halo Curve, Pearl Double Halo (product name only, no pearl-source words), Verdant Eternity, Cushion (sizes only after the K8 check), Toggle.
- **Picture source:** existing large macros (listing details, SAGE S3); new frames where none is large enough.
- **Failure checks:**
  - marks on stones;
  - more than three callouts;
  - non-listing words ("spring-gate ring" and "cubic zirconia bar" stay out until the listing states them);
  - measured, unlisted numbers (no "22 mm ring").

### A9 · Same Body, One Change (including day/night)
- **Borrows:** board 20 (triptych with an odd process frame), 21 (evidence pair with a quantity tab), 92 (one face split by a hairline), 75, 39, 150, 181; board 1 for the worn-arc day/night variant.
- **Layout:**
  - One generated image holding both states, split into two or three panels by an 8 px bone gutter or a hairline.
  - White corner tabs in Jost 500 26 caps: "BARE" / "WITH ONE PAIR".
  - H1 top-centre in Velista 72–80.
  - Card.
  - Text share 20% or less.
- **Day/night variant (10 or fewer):**
  - An ear in profile at true size, with a morning-light side and a tungsten side.
  - An arc headline of at most 16 characters on the arc's middle 50% (startOffset 25%, textLength 650), digits in Jost, sun and moon as inline SVG, the arc never crossing the piece.
- **Camera and light:** C4, generated at true size, both states in identical light, never pasted halves.
- **Copy formula:** the same thing with one change. Never a change over time.
  - "SAME TEE. / NEW NECKLINE." (Serpentine)
  - "BARE. / DONE." (Pearl Double Halo)
  - "DESK LIGHT. / LAMP LIGHT." (Brushed day/night: hours of wear, not durability)
- **Suits:** Serpentine (both metals), Pearl Double Halo, Brushed, Verdant Circlet, Monochrome, Halo Curve, Cushion (on a hand).
- **Picture source:** always new.
- **Failure checks:** states that differ in light or scale; visible seams; any reading of "it lasts"; "Click on." for Brushed unless the listing confirms the hinge.

### A10 · Set or Pick-Your
- **Borrows:** board 25 (anaphora occasion map), 58 (equation), 59 (staircase), 5 (named edit), 16 and 103 (what's in the box), 172; decoders 50, 36, 51, 146.
- **Variants:**
  - (a) One body wearing the whole set at true size: an ear stack, a hand stack, ear plus wrist.
  - (b) A photographed group at true relative scale on stepped plinths.
  - (c) Pick-your: two eligible products as a choice, for example two greens, Verdant Eternity in silver tone against Verdant Circlet in gold tone.
  - No tiles, grids or price sums.
- **Layout:**
  - The code as the headline in Velista 84–96.
  - Each piece named once in the card line.
  - Text share 30% or less.
  - The landing page is a cart permalink with the discount pre-applied (§5.6).
- **Camera and light:** C4 for the worn variant, C2 or C3 for groups. Light L5 or L7.
- **Copy formula:** a named set plus the verified code. Examples below assume the 10% value is confirmed.
  - "EAR AND WRIST. / ANY 2, 10% OFF." (Brushed and Ribbon, both ₹699)
  - "TWO GREENS. / ANY 2, 10% OFF." (Verdant Eternity and Verdant Circlet; the mixed metals are stated in the line)
  - "ONE HAND, / TWO RINGS." (Cushion Halo and Verdant Eternity, both silver tone)
- **Approved sets** (every variant at 20+ units; re-check before each batch):
  - Brushed + Ribbon (BUY2)
  - Serpentine Silver + Pearl Double Halo (BUY2; the pairing is the listing's own styling tip)
  - Verdant Eternity + Verdant Circlet (BUY2)
  - Cushion Halo + Verdant Eternity (BUY2)
  - Bold Nocturne + Serpentine gold (BUY2)
  - Brushed + Toggle + Cushion Halo (BUY3, once the Toggle gate passes)
  - Brushed + Toggle + Cushion Halo + Woven (BUY4; Marquise is removed because its gold variant has 15 units)
  - Pick-your never sets Serpentine gold (₹1,299) and silver (₹899) side by side with prices.
- **Failure checks:** false relative scale; a price sum; a piece under 20 units; five or more pieces; a grid (SA08 sold nothing on ₹1,968).

### A11 · Offer Poster (including hazard tape)
- **Borrows:** board 136 (₹0 numeric antithesis), 24 (angled offer band with terms), 76 (crossed caution tapes), 57 (disc on a panel edge), 129 (candour card), 118.
- **Layout:**
  - A flat loud ground.
  - Anton H1 at 140–200 (a labelled experiment, at most one per batch), or Velista at 120.
  - A macro packshot at 45–60% of the width, or two tapes crossing behind the piece (SVG ⚠).
  - One disc or angled band with the verified offer and its terms in Jost 22 microtext.
  - Card.
  - Text share 30–40%.
  - Sent to retargeting audiences.
- **Camera and light:** C5 product only. L2 flash or L1.
- **Palette:** terracotta with pista tape; oxblood with saffron; sky with ink.
- **Copy formula:** a numeric antithesis on offers only, or a warning written as a compliment.
  - "₹0 SHIPPING." + insured (only after the free-shipping threshold check). "₹0 upfront" waits for COD and RTO rates (§8).
  - "⚠ CAUSES STARING ⚠" (tape around the Cushion Halo)
  - "ANY PIECE. / CODE NAIRA10." (only once the NAIRA10 terms are read; never "first piece")
- **Suits:** Cushion Halo, Brushed, Ribbon, Verdant Eternity, Woven, Halo Curve.
- **Picture source:** existing listing details and macros for the tape; new frames for any glossy-floor version.
- **Failure checks:** an unverified percentage; "across India"; urgency or scarcity; a catalogue-page layout; emoji fallback.

### A12 · Personality Series ("The ___ one.")
- **Borrows:** board 42 (a colour-coded variant personality), 68, 146, 115.
- **Layout:**
  - Generated directly on the flat token field, never masked onto it. The piece is oversized, tilted 15 degrees and cropped off the top-right, with a true contact shadow and a size tag.
  - Right-aligned stack at x 72–560: the name in Velista 56; "THE ___ ONE." in Velista 110; two mood lines in Cormorant italic 44; specs in Jost 26 separated by pipes.
  - Card.
  - Text share about 25%.
- **Palette:** one fixed token per piece across the series: Brushed on terracotta, Monochrome on bone, Verdant Circlet on sage-deep, Pearl Double Halo on ink, Halo Curve on oxblood.
- **Copy:**
  - "THE EVERYDAY ONE." (Brushed)
  - "THE SHARP ONE." (Monochrome)
  - "THE QUIET ONE." (Pearl Double Halo)
- **Picture source:** new, one frame per SKU.
- **Failure checks:** a pasted look; a personality that contradicts the piece; token drift across the series.

### A13 · Suspended (levitation or frozen fall)
- **Borrows:** board 96 (levitation with a detached shadow), 66, 109, 117, 131 (frozen motion), 4 (light blades).
- **Picture:**
  - *Levitation:* the piece hovers 2–4 cm above a flat field, with crisp detached shadows directly below and a known-size object (a jasmine bud) on the floor.
  - *Frozen fall:* a chain falls in an S from a hand above the frame into an open palm, links sharp, fingers in the chain's plane, at true size.
  - Light L1 hard top spot or L5. Camera C2.
- **Layout:**
  - H1 top-centre in Velista 84–96, or Cormorant italic 96 when the headline holds a price.
  - Card.
  - Text share 18% or less.
  - Story twin from the native frame.
- **Copy:**
  - "The ₹699 pair." + "brushed, not polished." (Brushed)
  - "BLACK. WHITE. / GOLD TONE." (Monochrome on saffron)
  - "FALLS LIKE / A SNAKE CHAIN." + "2 mm, 40 cm plus 5 cm." (Serpentine)
- **Suits:** Brushed, Cushion Halo, Monochrome, Halo Curve, Serpentine (fall), Toggle (fall, after its gate), Verdant Circlet.
- **Picture source:** new.
- **Failure checks:** visible wires or stands; attached or pasted shadows; the piece oversized against the referent; anything wet.

### A14 · In-Word Swap
- **Borrows:** board 155 (a switch as the O in UNLOCK), 82 (a pun on the pack's form), 69 and 115 (3D type).
- **Picture:** the piece is generated at letter cap height on a flat field, with a true contact shadow and light matched to the type. Light L2 flash or L7; camera C3.
- **Layout:**
  - Velista letters set around the piece, with the cap height equal to the piece height.
  - Second beat in Cormorant italic 52.
  - Size tag and card.
  - Text share about 25%.
- **Copy:**
  - "Z[OO]M / IN." with the Brushed pair as the OO
  - "PR[O]POSAL." with the Cushion Halo standing as the first O
  - "W[O]VEN." with one Woven hoop as the O (the product name only)
- **Picture source:** new.
- **Failure checks:** the piece does not read as a letter, or the letter does not read as the piece; a missing size tag; the Velista ligature.

### A15 · Phone POV / Mirror
- **Borrows:** our creator reel ("Where is this from?", 11.47% CTR), board 70 and 195 (occlusion, adapted so the phone hides the face), 72 (product in costume).
- **Picture:** generated at true size.
  - A mirror selfie where the phone covers the face and the piece is visible: the ring on the hand holding the phone; earrings on the ear opposite the phone.
  - Or a POV of a hand opening the Naira box toward the lens (only if that box is what ships).
  - Light L2 flash or L7; camera C6. No phone brand marks. Mirror text must not read reversed.
- **Layout:** the card only, or one Velista 64 line. Never fake platform UI, comments, ratings or creator names.
- **Copy:**
  - "RING HAND, / PHONE HAND." (Cushion Halo)
  - "HAIR TUCKED. / STUDS ON." (Verdant Circlet)
  - "OPEN IT / HERE." (box POV)
- **Picture source:** new.
- **Failure checks:** the face visible beyond the ruling; the ring enlarged by perspective (fingers must stay in the ring's plane); fake UI; brand logos.

### 4.16 Idea bank by SKU (screened against the founder-reject list and the one-second test)

| SKU (stock / headroom above 20) | Ideas (archetype · set · light) |
|---|---|
| Cushion Halo Ring (45 / 25) | (1) S1_04 card, A1 · cocoa · L7. (2) "PR[O]POSAL", A14 · plum · L7. (3) Levitation over a black mirror floor with a jasmine bud, A13 · L1. (4) Spotlight on a bone riser, prism band, A6 · L1. (5) Mirror selfie, ring on the phone hand, A15 · L2. (6) Hazard tape "CAUSES STARING", A11 · terracotta · L2. |
| Brushed Gold Huggies (58 / 38) | (1) Levitation on oxblood, A13 · L1. (2) "Z[OO]M IN.", A14 · sky · L2. (3) Brushed band monument, "BRUSHED, NOT POLISHED.", A4 · L1. (4) Ear day/night twin, A9 · L7 and tungsten. (5) Ear-and-wrist set with Ribbon, A10 · L5. (6) "THE EVERYDAY ONE.", A12 · terracotta. |
| Verdant Eternity Band (58 / 38) | (1) Mehendi hand on marigold silk (S2_06), A2. (2) Green glass bangles, A3 · L4. (3) Selective colour, only the green stones in colour, A2. (4) Callouts on oval stones and scalloped pavé, A8. (5) Ring stack with Cushion Halo, A10. (6) Two greens with Verdant Circlet, A10c. |
| Halo Curve Ring (29 / 9) | (1) Cane-blind gobo throwing tiger stripes, A4 · L4. (2) Callouts "TWO STONES. ONE OPEN BAND.", A8. (3) Hand at jaw on oxblood, A2 · L1. (4) Levitation on saffron, A13. (5) Selective colour with the tiger eye in colour, A2. |
| Verdant Circlet Studs (32 / 12) | (1) Banarasi ear (S2_10), A2. (2) "ONE STUD, THREE PARTS.", A8. (3) Mirror tuck, A15. (4) Macro with size tag, A4. (5) Two greens, A10c. |
| Monochrome Enamel Hoops (24 / 4) | (1) Levitation on saffron, A13 · L1. (2) Top-down on zebra-crossing paint, A3 · L6. (3) Flash portrait with a white collar, A2 · L2. (4) "THE SHARP ONE.", A12 · bone. |
| Pearl Double Halo Studs (25 / 5) | (1) Spotlight on ink, A6. (2) "BARE. / DONE.", A9. (3) Set with Serpentine Silver on one body, A10. (4) Callouts on the two bands, A8. (5) Mirror, A15. |
| Serpentine Whisper Chain, silver (23 / 3) and gold (20 / 0) | (1) One S, top-down on plum, A4 · L6. (2) Split headline, A7. (3) Frozen fall into a palm, A13. (4) Collarbone at 18 cm, A2. (5) "SAME TEE. NEW NECKLINE.", A9. Gold and silver are never priced side by side. |
| Ribbon Bead Bracelet (21 / 1) | (1) `colour/66` navy satin bow, A3. (2) "TWO HEARTS. ONE BOW.", A5. (3) Set with Brushed, A10. (4) Gifting wrist, December, A2. |
| Bold Nocturne Drops (20 / 0) | (1) The only lit object, cast as the moon, A6 (after the `diwali-10/10` mechanism). (2) Split headline "PLAIN LINK, PAVÉ LINK.", A7. (3) A new ear frame at about 23 mm, A2. |
| Toggle Link Chain (77 / 57; clasp gate) | (1) Frozen fall into a palm, A13. (2) Split headline, A7. (3) Callouts in listing words, A8. (4) `colour/51` paperclip card, A1. All after the clasp passes. |
| Woven Gold Hoops (89 / 69; cap 15) | (1) Braid monument on oxblood, A4. (2) "W[O]VEN.", A14. (3) Spotlight, A6. Texture lines only. |
| Prism Rivière Bracelet (42 / 22; cap 10) | (1) Glass-prism spectrum on ink, A6. (2) Worn wrist on a dark ground, A2. No pale grounds. |

---

## 5. Production plan: 500 ads in 100 batches of 5

### 5.0 Batch 0: unspent inventory (before any new generation; re-renders are not counted in the 500)
Take every finished ad or plate that got less than ₹500 of spend, on a SKU whose shown variants all have 20+ units. Re-check scale, fidelity against the 19 Nov truth sheet, compliance, the face ruling, the edit-pass ruling and the live price. Re-render the passes into wave 1.

| Candidate | Spend (20 Oct–18 Nov) | Status |
|---|---|---|
| ads-20 S3_13 Halo Curve "free insured shipping" (judge 7.92) | not run | Re-check; lead with a craft line instead of shipping |
| DIW 06 Cushion "All eyes on your hand." | ₹38 | Re-check price and copy |
| A01 Cushion "I do" | ₹33 | Generic occasion line: rewrite or drop |
| p3-08 Verdant Eternity "Dinner in green." | ₹36 | Generic occasion line: rewrite or drop |
| `colour/51` Toggle "Paperclip, promoted." | ₹52 | Only after the clasp gate |
| ads-20 S1_02 Woven Gold Hoops | ₹328 | Edit-passed frame: depends on the §8 ruling |

ads-20 S1_04, S2_06, S2_10 and S3_12 are used as new layouts in batches 1–4. S4_17 (Marquise gold, 15 units), S2_07 (Baguette Huggies) and S4_19 (the Ribbon bow reads about 1.3× too large) are out.

### 5.1 Allocation by product (stage-gated)

**Gating rules**
- Every variant shown must have 20+ units at the pre-batch read.
- Headroom is stock minus 20. Products with headroom under 10 get no more than 10 ads built ahead until there is a restock date.
- Queued ads per product are capped at what can run before stock is projected to fall under 20.
- Phase 1 runs through batches 1–10.
- A product unlocks 10 more slots, up to its ceiling, once its first 5 tested ads produce at least 2 purchases at 1.5x or better at stage 2 (§5.6).
- Brushed and Ribbon (₹699) are judged on order value, not purchase count.

| Product | Stock 19 Nov | Headroom | Live price | Evidence (20 Oct–18 Nov) | Phase 1 (b1–10) | Ceiling if unlocked |
|---|---|---|---|---|---|---|
| Cushion Halo Ring | 45 | 25 | ₹999 | Halo B video: 20 purchases, 2.21x; Halo A: 4, 0.85x. Both carried banned claim text. | 12 | 55 |
| Brushed Gold Huggies | 58 | 38 | ₹699 | No tested static; ₹699 is below cost per purchase | 10 | 20, rising to 35 if its ads' average order is at least ₹1,150 |
| Verdant Eternity Band | 58 | 38 | ₹1,049 | Untested statics; catalogue 0 on ₹691 | 5 | 45 |
| Halo Curve Ring | 29 | 9 | ₹899 | Untested | 3 | 30 |
| Verdant Circlet Studs | 32 | 12 | ₹899 | Untested (S2_10, ₹69) | 3 | 30 |
| Monochrome Enamel Hoops | 24 | 4 | ₹999 | Never advertised | 3 | 25 |
| Pearl Double Halo Studs | 25 | 5 | ₹1,199 | Untested | 2 | 20 |
| Serpentine Whisper Chain, silver | 23 | 3 | ₹899 | Untested | 2 | 20 |
| Toggle Link Chain | 77 | 57 | ₹999 | About ₹8.0k, 4 purchases, about 0.3x | 2 (0 if the clasp gate fails) | 20 |
| Woven Gold Hoops | 89 | 69 | ₹1,049 | 18 ads 0.75x; W1 texture line 1.23x | 2 | 15 |
| Ribbon Bead Bracelet | 21 | 1 | ₹699 | Untested | 1 | 15 |
| Prism Rivière Bracelet | 42 | 22 | ₹2,399 | Statics 0.55x on ₹28.9k; video 3.46x | 1 | 10 |
| Serpentine Whisper Chain, gold | 20 | 0 | ₹1,299 | n/a | 1 | 10 |
| Bold Nocturne Drops | 20 | 0 | ₹1,299 | n/a | 1 | 10 |
| A10 set ads | | | | | 2 | 30 |
| **Allocated** | | | | | **50** | **355** |
| Earned pool | | | | | | **145** |
| **Total** | | | | | | **500** |

- **Earned pool:** released in three tranches, at batches 20, 40 and 60. It goes to products by 7-day-click purchases per ₹1,000 in their tested ads, capped by headroom. Owner opt-ins (§8) draw from it too: Baguette Huggies, Droplet and Marquise line-ups; Triple Coil once its turns are counted; restocked ruby tennis pieces or catalogue best sellers.
- **The tension:** the pieces with the most stock (Woven, Toggle, Prism) have the weakest sales evidence. The best-evidence pieces (the two ruby tennis pieces) are not eligible at all. This plan does not resolve that tension by itself; it is listed as an owner decision.

### 5.2 Archetype mix and rotation

**Mix at about 95 new images, the plan of record**

| Archetype | Ads | Archetype | Ads |
|---|---|---|---|
| A1 Product Card | 65 | A9 Same Body | 15 |
| A2 Worn Editorial (15 selective colour) | 60 | A10 Set or Pick-Your | 35 |
| A3 Literal Rhyme | 30 | A11 Offer Poster (15 tape) | 40 |
| A4 Monument Macro | 50 | A12 Personality | 20 |
| A5 Truth Split (12 or fewer numerals) | 45 | A13 Suspended | 30 |
| A6 Spotlight | 20 | A14 In-Word | 20 |
| A7 Split Headline | 10 | A15 POV / Mirror | 20 |
| A8 Callout Anatomy | 40 | **Total** | **500** |

- The crazy set (A2 selective, A6, A7, A11 tape, A13, A14, A15) comes to 130 ads, about 1.3 per batch.
- The type-led family (A5, A11 non-tape, A12, A10 pick-your) comes to about 100 ads, which is its cap.
- The about-1,000-credit mix is in §5.4.
- Once live waves have run, purchase data re-weights this mix every 10 batches.

**Calibration grid, batches 1–4 (20 ads)**
- The two heroes, Cushion Halo and Brushed, each run through the same five archetypes: A1, A2, A13, A14, A6.
- Each batch adds one occasion picture and the controlled test cells.

| Batch | Slot 1 | Slot 2 | Slot 3 | Slot 4 | Slot 5 |
|---|---|---|---|---|---|
| 1 | Cushion · A1 (S1_04, no headline) | Cushion · A2 (same frame, with headline) | Brushed · A13 levitation (new) | Brushed · A14 "Z[OO]M IN." (new) | Verdant Eternity · A2 mehendi (S2_06) |
| 2 | Cushion · A13 levitation, BUY2 box (new) | Cushion · A14 "PR[O]POSAL." (new) | Brushed · A1 (S3_12 frame, or a new jaw-limit ear frame) | Brushed · A2 (same frame, with headline) | Verdant Circlet · A2 Banarasi (S2_10, cropped from the 2K original) |
| 3 | Cushion · A6 spotlight (new) | Brushed · A6 spotlight (new) | Verdant Eternity · S2_06 with the offer box off (test cell against B1-05) | Monochrome · A13 levitation on saffron (new) | Halo Curve · A4 cane gobo (new) |
| 4 | Cushion · A13 same frame as B2-1, NAIRA10 box (test cell) | Ribbon · A3 `colour/66` (gifting) | Pearl Double Halo · A9 "BARE. / DONE." (new) | Serpentine Silver · A7 (new) | Set · A10 Brushed + Ribbon on one body (new) |

- The B2-1 frame carries two live ads (BUY2 and NAIRA10), the per-plate maximum.
- Ribbon (1 unit of headroom) and Monochrome (4) are dropped from their slots if the pre-batch read shows under 20.

**From batch 5**

| Slot | Role | Archetypes |
|---|---|---|
| 1 | Control | A1, A2 or A4 |
| 2 | Crazy | A6, A7, A11 tape, A13, A14, A15 or A2 selective |
| 3 | Explainer | A5, A8 or A9 |
| 4 | Value | A10, A11 or A12 |
| 5 | Season or wildcard | An occasion picture while in season; otherwise a second crazy ad |

**Constraints for every batch from batch 5**
- At least 4 different archetypes and at least 3 products; no more than 2 ads per product.
- At least 3 lights and 3 cameras from the menus.
- At most one Anton ad and at most 2 type-led ads.
- No plate used twice in a batch.
- Each plate used no more than 5 times in the whole plan, in at least 2 archetypes, with no more than 2 ads per plate live at once.
- At least one crazy ad in every batch, and two in at least 30 of the 100 batches (in all of them at about 1,000 credits).

**Calendar (dates, not batch numbers)**

| Window | Work |
|---|---|
| Now to about 15 Dec | Wedding-guest occasion pictures (mehendi, haldi, sangeet, reception), one per batch |
| From about 5 Dec | December gifting (bow, box POV, sets), only after confirming the Naira gift box ships and reading the courier cut-off date |
| From about 25 Jan | Valentine's ring and stud ads |

**Phases**

| Phase | Batches | Work |
|---|---|---|
| Calibration | 1–4 | The grid above |
| Spread | 5–10 | Winning archetypes across the phase-1 caps |
| Scale | 11–40 | Earned pool tranche 1; first unlocks |
| Series and season | 41–80 | A12 series, sets, gifting, Valentine's |
| Refresh | 81–100 | New crops, grounds and copy on the top 20%; owner opt-ins |

### 5.3 How each batch must improve on the last

1. **Calibrate before batch 1.** Two critics score 13 tested anchors blind:
   - Critic A: creative director. Critic B: product truth and compliance.
   - Winners: anaar Story, F2, W1 "Woven, not cast", VK F18, Apricot quiet.
   - Losers: W1 Waterproof, VK S5, SA08 Feed, P13 kandil Story, C01 Feed, P2, old "Almost edible", VK S1.
   - Pass condition: the rubric (§7) must rank anaar, F2 and W1 "not cast" above all eight losers, and at least 4 of the 5 winners above the losers' median.
   - If it fails, re-weight (raise stop power at 200 px and piece colour; lower copy and brand) and repeat.
   - Why this matters: the ads-20 judge scored the anaar Story 6.15, below the DIW 08 pouches, which sold nothing.
2. **Score every ad blind** on the §7 rubric. A compliance failure from either critic means a rebuild. Tie each score to the exact file version that was reviewed (`finished-ads/sign_review.py` practice).
3. **Run a pairwise test at 200 px.** Each batch sheet carries two unlabelled anchors: one tested winner and one tested loser, rotated from the list above.
   - An ad ships only if both critics pick it over the loser anchor, no dimension scores under 6, and product truth scores 8 or more.
   - Beating the winner anchor is the "strong" tier.
   - The draft's absolute gates ("8.0 overall", "8.8 by batch 20") are dropped. Our best static was judged 7.92, and those gates invite score inflation.
4. **Batch report:**
   - share of ads beating each anchor;
   - mean for each dimension;
   - a 200 px contact sheet next to the previous batch and the board ranks each ad borrows;
   - the thumbnail test: can a reviewer tell all 5 apart, name each product and read each headline?
5. **Carry learnings forward.** A device becomes a written rule in `learnings.md` once it has beaten the winner anchor in two batches. Example: "price at Cormorant 56 with the offer box beats a price-free card".
6. **Fix target:** the lowest-scoring dimension becomes the named, concrete fix for the next batch.
7. **One new move per batch.** Exactly one variable changes (light, ground, copy device or archetype variant), in the build and in what goes live, so every change can be traced.
8. **Live data overrides critics.**
   - From batch 11, every four-batch cycle cites the previous wave's purchases, cost per add-to-cart and outbound CTR in its brief.
   - Archetype weights are re-set every 10 batches from purchase data.
   - Production never runs more than 10 batches ahead of live results.
9. **Re-read stock and prices before every batch**, not every 10.

### 5.4 Credit plan

**Assumption and cost**
- About 95 new images at 2 credits each, so 190 credits. A 4-image Nano Banana Pro 2K call was quoted at 8 credits.
- Count images, not shots. Each shot gets 2 variants.
- The balance read on 19 Nov was 144.46 credits, about 72 images. Reaching 95 needs about 46 more credits; otherwise drop the A12 and A3 shots (about 9 shots).

| Shot type | Shots | Images |
|---|---|---|
| Worn true size, A2 (Cushion hand-only fallback, Halo Curve, Verdant Eternity selective source, Serpentine Silver, Bold Nocturne at about 23 mm, Monochrome flash, Prism dark wrist, Woven on oxblood) | 8 | 16 |
| Same body, A9 (Pearl, Brushed day/night, Serpentine, Halo Curve) | 4 | 8 |
| Suspended, A13 (Brushed, Cushion, Monochrome, Halo Curve, Serpentine fall, Verdant Circlet, Toggle fall after its gate) | 7 | 14 |
| In-word, A14 (Brushed, Cushion, Woven) | 3 | 6 |
| Spotlight, A6 (Cushion, Brushed, Pearl, Bold Nocturne moon, Prism spectrum) | 5 | 10 |
| Split headline, A7 (Serpentine silver, Serpentine gold, Bold Nocturne) | 3 | 6 |
| POV / mirror, A15 (Cushion, Verdant Circlet, Pearl, box POV) | 4 | 8 |
| Personality, A12 (Brushed, Monochrome, Pearl, Halo Curve) | 4 | 8 |
| Sets, A10 (Brushed + Ribbon, Serpentine Silver + Pearl, Cushion + Verdant Eternity) | 3 | 6 |
| Literal rhyme, A3 (Verdant Eternity glass bangles, Monochrome zebra) and macro, A4 (Halo Curve gobo) | 3 | 6 |
| Reshoot reserve | | 7 |
| **Total** | **44** | **95** |

**Expected keepers**
- Per image, assume a 40% keep rate for worn true-size frames (Soleil kept 0 of 2; crazy3 drew pieces 1.5–2.6× too large) and 60% for product-only frames. The founder kept 23 of 70 colour shots.
- Per shot with 2 variants that gives about 64% for worn and 84% for product-only shots.
- Keepers:
  - about 8 of 12 worn shots;
  - about 16 of 19 product-only crazy shots;
  - about 3 of 5 POV and set-on-body shots;
  - about 6 of 8 personality, rhyme and macro shots;
  - plus about 3 from the reshoot reserve.
- **Total: about 36 keeper frames.**

**Pictures for the 500 at about 95 images**

| Source | Pictures | Uses each | Ads |
|---|---|---|---|
| New keepers | about 36 | about 4 | about 145 |
| Existing plates that pass the re-audit (§5.5 lint; struck plates listed under A3 and A6) | about 30 | about 4.5 | about 135 |
| ads-20 frames (S1_04, S2_06, S2_10, S3_12; S1_02 depends on the edit-pass ruling) | 5–6 | about 4 | about 22 |
| Listing photographs (cubes, details, worn images generated at true size, such as Verdant Circlet's "true 16.8 mm size" worn photo; `edition-two-listings` exports for Bold Nocturne), cropped at native resolution | about 45 | about 4.4 | about 198 |
| **Total** | **about 117** | **about 4.3** | **500** |

- This works only if most pictures appear in 4–5 different layouts. The rule of no more than 2 live ads per plate stops them competing in delivery, but creative fatigue will show.
- Copy-only variants never count as separate ads; they go into Meta's multiple text options inside one ad.

**At about 1,000 credits (about 500 images, about 250 shots, about 180 keepers)**
- Reuse falls to about 2 uses per picture.
- Every A1, A3, A4 and A6 frame is native 9:16.
- Worn true-size coverage for all 14 SKUs across 3 body zones and 3 named skin tones.
- Every legacy plate with a scale or glint flag is retired.
- Each batch adds a picture-against-layout test (same copy, two pictures).
- Two reshoots per hard piece (the Toggle clasp). Triple Coil frames as soon as its turns are confirmed.
- The archetype mix shifts toward the crazy set:

| Archetype | Ads | Archetype | Ads |
|---|---|---|---|
| A1 | 40 | A9 | 25 |
| A2 | 60 | A10 | 35 |
| A3 | 35 | A11 | 30 |
| A4 | 35 | A12 | 15 |
| A5 | 30 | A13 | 55 |
| A6 | 30 | A14 | 30 |
| A7 | 15 | A15 | 40 |
| A8 | 25 | **Total** | **500** |

The crazy set then reaches 200 ads, two in every batch.

**Higgsfield settings**
- `generate_image_batch` with `model: nano_banana_pro`, `resolution: 2k`, `aspect_ratio: 9:16`, 2 images per shot.
- Slot 1: the approved listing packshot ("the authority on this exact piece; ignore its background and light"). Slot 2: a detail of the same piece only, with its role stated.
- Quote with `estimate_image_cost` before each call.
- Poll `jobs_wait` at intervals of 15 seconds or less. Never resubmit a job whose outcome is unknown.
- The model served can differ from the one requested, so judge every output by eye.

**Catalogue exports**
- Every A2 and A4 keeper is also exported as a 1:1 catalogue image (about 40 images) for a lifestyle-first catalogue test.
- These are extra exports, not ad slots.
- Whether they go into the Meta catalogue's additional images is the owner's choice.

### 5.5 Pre-flight before every batch (read-only)

**Stock and price**
- Live stock of 20+ for every variant shown, including every piece in a set; headroom checked against the queued ads.
- Live price, filled into the price layer at export. No price is ever typed into a template.

**Offer terms**
- BUY2, BUY3 and BUY4: value, mechanism (code or automatic in the bag), minimum quantity, dates, and whether they combine with compare-at sale prices.
- NAIRA10: terms, including any order or first order only.
- Any minimum order for free insured shipping (a ₹699 piece may not qualify).
- Any COD fee.

**Listing confirmations**
- All 45 Cushion Halo units are the adjustable version, before "adjustable" or "US 5 to 9" is printed for it.
- The Brushed listing confirms the hinge, before any "click" copy.
- The Woven listing or supplier confirms the process, before "Woven, not cast."

**Compliance lint**
- Banned words checked in on-image copy, primary text, the Meta headline, file names and the Higgsfield prompts.
- Prompt colour words must match the Plating field. A colour word in a prompt flips the metal; "freshwater" sits in `tested-prompts.md`.
- "COD" is written "on serviceable pincodes", never "across India".

**Plate re-audit lint (every reused plate)**
- no water or droplets;
- no pale piece on a pale ground;
- no styling repeated within 10 batches;
- passes the size metric;
- no star glints or pasted shadows;
- fidelity matches the 19 Nov lock;
- not a plate whose ads lost after tested spend (check its past creative IDs).

**Meta setup**
- Advantage+ creative enhancements off on every ad (image expansion, touch-ups, generated text or overlays). "Add catalogue items" runs only as a deliberate test cell.

### 5.6 Deployment and measurement (owner choice; nothing was changed in this run)

**Budget and pace**
- About ₹20,000 a week, today's static share (about ₹22.5k a week) restructured.
- Screens about 14 ads a week, about 60 a month. 500 ads take about 8 months.
- Catalogue stays the base and is not reduced.

**Stages**

| Stage | Spend | Pass condition | Next step |
|---|---|---|---|
| Screen | ₹1,000 over 4 days, in its own ad set (or Meta Experiments for head-to-head cells) | At least 1 purchase, or cost per add-to-cart below the account median | Advance; otherwise off, recorded as "screened out" |
| Test | Up to ₹3,000 more | Off at ₹1,500 total with 0 purchases | Continue |
| Graduate | | At least 3 purchases at 1.8x or better after at least ₹3,000 | Evergreen "Winners" ad set |

- Pull add-to-cart and initiate-checkout counts. CTR has not predicted purchases here: the play ads had the top CTR and no sales.

**Structure and audience**
- One ad per ad set for screens; report each ad's spend share next to its ROAS.
- A fixed prospecting audience: Advantage+ audience with a women 18–54 suggestion, all India.
- A small separate retargeting budget (30-day engagers, and people who added to cart without buying) for A8, A11, the A5 numeral ads and A10 pick-your.
- Prospecting for A1, A2, A3, A4, A6, A7, A13, A14, A15.
- Exclude FB Feed (0.82x) and Explore (0 sales) from test ad sets.

**Placements**
- Every ad carries a 9:16 asset through placement customisation: text-free, or text only between y 270 and 1250.

**Landing pages** (no Shopify write needed)
- Single-product ads: `/products/{handle}`.
- Code ads: `/discount/{CODE}?redirect=/products/{handle}`.
- Set ads: `/cart/{variantA}:1,{variantB}:1?discount={CODE}`.
- Pick-your ads: `/products/{handle}?variant={id}`.
- Product page against collection page runs as its own test cell (Core v2 linked to the homepage and made 3.00x).

**Naming and UTMs**
- Ad name: `b{nnn}-{slot}_{archetype}_{product}_{plate-id}_{offer}_{hook-slug}`.
- URL parameters: `utm_source=meta&utm_medium=paid&utm_campaign=ads500_w{n}&utm_content={{ad.id}}&utm_term={ad-name-slug}`.

**Weekly roll-up and checks**
- Roll-up by archetype, product and plate: spend share, purchases, cost per add-to-cart, average order value, COD share.
- Read Shopify orders by `utm_content` (read-only) for COD share and cancellations or returns to origin. Judge waves on delivered revenue.
- Weekly price audit of live ads (image and headline) against the store.

---

## 6. Batch 1 brief

**What batch 1 tests**
- Does a headline help or hurt the F2 card on the same frame (B1-01 against B1-02)?
- Do two honest "crazy" devices (levitation, in-word) stop the thumb on the entry-price hero?
- Does a wedding-season occasion picture that was judged well but never run sell?

**Also in batch 1**
- One proven-grammar control (B1-01).
- Lights: L7, L1, L2. Cameras: C4, C2, C3.

**Credits**
- B1-03 and B1-04: 2 images each, so 8 credits.
- The B1-01/02 fallback, if needed: 2–4 images, so 4–8 credits.

**Before building:**
- the §5.5 pre-flight;
- the anchor calibration;
- the §8 rulings on lips and edit passes.

In the copy below, "Buy 2, get 10% off" and "BUY 2 · 10% OFF • BUY 3 · 20% OFF" stand in for the verified terms. If the terms differ, replace them; if they are unverified, drop the offer box and the offer clause.

### B1-01 · Cushion Halo Ring · A1 Product Card (no headline) · existing frame
- **Stock and price:** 45 units, ₹999. Re-read both first.
- **Picture:** the text-free frame of `docs/creative/ads-20/ads/S1_04_cushion_halo_ring_feed.jpg`.
  - Retrieve it from Higgsfield generation history (read only, no credits). The raw file was in a scratchpad that has since been cleared.
  - Per `ads-20/build/set1.json` it is edit pass "c" on frame b, with the head made about 20% smaller after the judge read it as about 16 mm. **It may be used only if the owner allows edit passes and lips in the crop (§8).**
  - At 100%, check: the halo is within 1.2× of 12 mm against the finger (it measures about 13% of the canvas width, which passes the worn metric); one cushion-shaped row; silver tone; no star glints (the first try had them).
  - Story: use a native 9:16 text-free frame if history holds one; otherwise no Story twin, and never mirror-extend.
- **Fallback, if either ruling is no** (one shot, 2 images; it serves B1-01 and B1-02). Refs: slot 1 `94e89aaa-1d35-47ca-853e-da323cc0ac01` (upright; "the authority on this exact piece; ignore its background and light"); slot 2 `6b507080-6cf9-4452-83c1-6e5cabddcfa0` ("take only the halo construction"). 9:16, 2K. Prompt:
  > Tight editorial hand portrait in a 9:16 frame, 85 mm feel, eye level: the back of an Indian woman's right hand, warm medium-brown skin, fingers together and relaxed, raised to chest height in front of a plain black knit top, against a deep cocoa-brown seamless; the frame shows only the hand, the wrist and a band of the black knit, about 10 cm across, no face, no neck. She wears one ring on the ring finger: one 8 mm round brilliant clear cubic zirconia in 4 claws inside a single-row cushion-shaped (rounded-square) pavé halo about 12 mm across, pavé down both shoulders, a plain band with a small opening at the back hidden by the finger, all in cool PVD rhodium silver tone. The halo must stay one single row and cushion-shaped, never round, never two rows, and the metal stays cool silver tone, never gold. The 12 mm halo spans about two thirds of the width of her ring finger at the knuckle; the ring keeps its true small size and dominates by light and isolation, never by being enlarged, with a faint contact shadow on the skin. The hand sits inside the central 4:5 window of the frame, the ring between 38% and 48% of the frame height; the lower 35% of that window is calm black knit and cocoa backdrop for type, and nothing important touches the frame edges. One soft warm directional key from the upper left across the back of the hand, plus one hard specular kicker from the right so the cubic zirconia throws small points of colour; natural skin texture with visible pores, honest macro optics, shallow depth of field. No face, no lips, no other jewellery, no nail art, no star-shaped glints, no starburst, no lens flare, no text, no water, no droplets.
  - Acceptance: halo within 1.2× of true size by pixel ruler; one row; cushion shape; silver tone; ring at least 12% of the canvas width; no glints.
- **Layout:** the F2 card only, centred, y 880–1200:
  - wordmark `logo_white`, 56 px;
  - "CUSHION HALO RING" (Jost 500, 26, .2em);
  - "₹999" (Cormorant 500, 56);
  - one line: "8 mm cubic zirconia · silver tone" (Jost 400, 26; no "adjustable" until the K8 check passes);
  - offer box: "BUY 2 · 10% OFF • BUY 3 · 20% OFF".
  - Bone type on a cocoa scrim from y 760.
- **Primary text (166 characters; the offer ends at character 123):** "Looks like a proposal, priced like a present. Cushion Halo Ring, ₹999: 8 mm cubic zirconia, silver tone. Buy 2, get 10% off; cash on delivery on serviceable pincodes."
- **Headline field:** "Cushion Halo Ring · ₹999 · Buy 2: 10% off"
- **CTA:** Shop Now → `/products/cushion-halo-ring?utm_source=meta&utm_medium=paid&utm_campaign=ads500_w1&utm_content={{ad.id}}&utm_term=b001-01_a1_cushion-halo_s104_buy2_nohead`

### B1-02 · Cushion Halo Ring · A2 Worn Editorial (headline) · same frame
- **Hypothesis:** the proven video hook, set on the image, beats the card alone. Primary text, headline field, offer and audience are identical to B1-01, so only the on-image headline differs.
- **Layout:**
  - B1-01's card, unchanged, at y 880–1200.
  - Above it, centred, a block at y 690–870 that clears the ring by at least 120 px:
    - "LOOKS LIKE" / "A PROPOSAL." in Velista 64, tracked .02em, ligatures off, bone, broken deliberately onto two lines (about 350 px and 390 px wide);
    - "priced like a present." in Cormorant Garamond italic 500, 48, --gold-light.
  - If the block lands on the fingers at render, drop to one line, "LOOKS LIKE A PROPOSAL." in Velista 52 (about 630 px), at y 790–850.
- **Primary text, headline field and CTA:** as B1-01, with `utm_term=b001-02_a2_cushion-halo_s104_buy2_head`.

### B1-03 · Brushed Gold Huggies · A13 Suspended (levitation) · NEW frame
- **Stock and price:** 58 units, ₹699.
- **Hypothesis:** an impossible-but-honest physics image stops the thumb on the entry-price hero, with the price as the message.
- **Higgsfield call:** refs slot 1 `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f` (pack; "the authority on this exact piece"); slot 2 `4c630657-80e8-47f5-ad65-1f0938c70900` ("take only the brushed finish"). 9:16, 2K, 2 images. Prompt:
  > Product still life in a 9:16 frame, camera low at about 12 degrees above the floor, 100 mm macro feel: a pair of Brushed Gold Huggies hovering side by side about 3 cm above a flat matte oxblood-red floor that curves up into an oxblood wall with no horizon line, their two crisp soft-edged shadows lying on the floor directly below them and clearly separated from the pieces, and one fresh white jasmine bud about 2 cm long lying on the floor beside the shadows. Each huggie: a chunky huggie about 14 mm tall by 9.8 mm, a wide flat band about 6 mm deep in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, hidden hinge, zero stones. The finish must stay matte and light-scattering, never mirror-polished, ridged, hammered or stone-set, and never a large hoop. Each huggie is about 14 mm tall, a little shorter than the 2 cm jasmine bud; they keep their true small size and dominate by light and isolation, never by being enlarged. The pair floats at the centre of the frame between 42% and 55% of the frame height, inside the central 4:5 window, and together spans about half the frame width; the top 25% of the frame is empty oxblood wall for type, and the bottom 30% is empty floor apart from the bud and the shadows. One hard warm spotlight from directly above and slightly in front gives each band one broad soft sheen and casts the shadows straight down, with faint warm bounce from the floor; the gold tone stays warm-neutral, never orange or brassy. No hands, no people, no strings, wires, stands or supports, no text, no other jewellery, no star-shaped glints, no starburst, no lens flare, no water, no droplets.
- **Acceptance:**
  - satin finish, not mirror;
  - each huggie 0.6–0.8× the length of the bud;
  - shadows detached and directly below;
  - warm-neutral gold;
  - pair spans 45–60% of the width;
  - no glints and nothing that reads as a support.
- **Layout (Feed, from the central 4:5 window):**
  - Headline top-centre at y 110–230: "The ₹699 pair." in Cormorant Garamond italic 500, 96, bone, with ₹ from the Noto Serif subset.
  - Under it at y 250: "brushed, not polished." in Cormorant italic 44, --gold-light.
  - Size tag: not needed while the pair displays at about life size (the bud does the scale work). Add "SHOWN MAGNIFIED / ABOUT 14 MM TALL" only if it renders above 19 px/mm.
  - Card: wordmark; "BRUSHED GOLD HUGGIES"; "₹699"; "18k gold tone PVD · about 14 mm"; offer box.
  - Story: the native 9:16 frame, headline at y 300–420, card at y 1000–1250.
- **Primary text (143 characters):** "The ₹699 pair: Brushed Gold Huggies, about 14 mm, in brushed-satin 18k gold tone. Buy 2, get 10% off; cash on delivery on serviceable pincodes."
- **Headline field:** "Brushed Gold Huggies · ₹699 · Buy 2: 10% off". Once a test checkout confirms it, the line may state the two-pair price the checkout shows. Never compute it by hand.
- **CTA:** Shop Now → `/products/brushed-gold-huggies?…&utm_term=b001-03_a13_brushed_new-lev_buy2_699pair`

### B1-04 · Brushed Gold Huggies · A14 In-Word Swap · NEW frame
- **Hypothesis:** a type trick that invites a closer look at the brushed texture stops the thumb and keeps the product truth (brushed, not mirror) as the message.
- **Higgsfield call:** the same refs as B1-03. 9:16, 2K, 2 images. Prompt:
  > Eye-level front-on product still life in a 9:16 frame, normal lens, on a flat seamless sky-blue background where floor and wall are the same colour with no horizon: a pair of Brushed Gold Huggies stand upright on their edges, side by side about 1 cm apart, their round openings facing the camera so each reads as a letter O, lit by a direct on-camera flash that throws a short hard drop shadow behind and slightly below each one. Each huggie: a chunky huggie about 14 mm tall by 9.8 mm, a wide flat band about 6 mm deep in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, hidden hinge, zero stones. The finish must stay matte brushed satin under the flash, one broad soft sheen, never mirror-polished or glinting, never ridged or stone-set, never a large hoop. They keep their true small size; their crisp contact shadows show they stand on the surface. The pair sits exactly at the horizontal centre of the frame at 42% of the frame height, inside the central 4:5 window, each huggie about 20% of the frame width, with wide empty sky-blue space to the left and right for letters and empty space below. The gold tone stays warm-neutral against the blue, never orange, never reading as silver. No hands, no people, no props, no text, no other jewellery, no star-shaped glints, no starburst, no lens flare, no water, no droplets.
- **Acceptance:** satin under the flash; both huggies identical; the pair centred with clear space either side; warm-neutral gold; no glints.
- **Layout:**
  - Line 1: "Z" and "M" in Velista, ink #1A1614, with cap height matched to the huggies' height (about 260–300 px), flanking the pair so it reads "ZOOM". Measure the widths at render; the line must fit inside x 72–1008.
  - Line 2: "IN." in Velista at the same cap height, centred under the pair.
  - Second beat at y 1000 is not needed; the card's line carries the truth.
  - Size tag on the right, "SHOWN MAGNIFIED / ABOUT 14 MM TALL" (about 21 px/mm).
  - Card in ink on sky: wordmark `logo_ink`; "BRUSHED GOLD HUGGIES"; "₹699"; "brushed satin, not mirror polish"; offer box.
- **Primary text (161 characters):** "Zoom in: the brush lines are the point. Brushed Gold Huggies, ₹699, in brushed-satin 18k gold tone. Buy 2, get 10% off; cash on delivery on serviceable pincodes."
- **Headline field and CTA:** as B1-03, with `utm_term=b001-04_a14_brushed_new-zoom_buy2_zoomin`.

### B1-05 · Verdant Eternity Band · A2 Worn Editorial (occasion) · existing ad, re-rendered
- **Stock and price:** 58 units, ₹1,049.
- **Hypothesis:** a concrete wedding-season moment, led by the stone's colour, sells a ring that has never had a tested static.
  - The ads-20 judge scored this frame 8.20 (one of its two top scores) and picked it for launch, but it never ran.
- **Picture:** the text-free frame of `docs/creative/ads-20/ads/S2_06_verdant_band_mehendi_feed.jpg`.
  - It was generated directly, with no edit pass in `set2.json`.
  - The ring covers about 18% of the width, which passes the worn metric. Hand only, no face.
  - Re-check at 100% against the 19 Nov lock. At thumbnail size the green ovals read as a straight row, each in its own pavé ring. The lock needs ovals set alternately either side of one scalloped S-wave of pavé.
  - If it fails, the frame is out (no edits). The slot then goes to `performance/plates/colour/66-ribbon-bead-bracelet.jpg` as A3 ("TWO HEARTS. / ONE BOW.", ₹699, after re-checking it for glints and stock).
- **Layout** (the S2_06 pattern, with the judge's fixes):
  - Wordmark top-centre at y 84.
  - "Greener than / the mehendi." in Cormorant Garamond italic 500, 76, ink, at y 170–330. This keeps the existing italic headline, since the frame's tested look depends on it.
  - Card at the bottom: "VERDANT ETERNITY BAND"; "₹1,049"; offer box. The variant line is dropped, as the judge asked, to give the ring and headline more air.
  - Story: lift the text block 40 px out of the Shop zone and restore the wordmark (the judge's fix); all text between y 270 and 1250.
- **Primary text (161 characters; the offer ends at character 119):** "Greener than the mehendi. Verdant Eternity Band, ₹1,049: emerald-green cubic zirconia, silver tone. Buy 2, get 10% off; cash on delivery on serviceable pincodes."
- **Headline field:** "Verdant Eternity Band · ₹1,049 · Buy 2: 10% off"
- **CTA:** Shop Now → `/products/verdant-eternity-band?…&utm_term=b001-05_a2_verdant-eternity_s206_buy2_mehendi`

**What the batch 2 critic must answer**
1. Which of the 5 reads first at 200 px, and did any beat the winner anchor?
2. Do the levitation and the in-word swap read as honest at true size?
3. Which dimension scored lowest? That becomes the batch 2 fix target.
4. Once live: did B1-02 beat B1-01 on cost per add-to-cart? That decides whether A1 or A2 carries more of the worn slots.

---

## 7. Per-batch scoring rubric

**Compliance gate** (pass/fail, before any scoring):
- no banned word anywhere, including prompts and file names;
- every variant shown has 20+ units;
- price and offer verified live;
- no water imagery;
- worn frames generated directly at true size (or under the owner's edit-pass ruling);
- no invented number;
- face within the ruling.

Any failure means a rebuild.

**Weights.** These are starting values; the anchor calibration (§5.3) may change them. The two added dimensions are marked.

| Dimension | Weight |
|---|---|
| Stop power | .15 |
| One message | .10 |
| Product truth and scale | .15 |
| Layout craft | .10 |
| Brand consistency | .05 |
| Copy | .10 |
| Archetype fit | .05 |
| Desire (added) | .15 |
| Purchase cues (added) | .15 |

**Ship rule:** compliance passes; no dimension below 6; product truth 8 or more; both critics prefer it over the loser anchor in the blind pairwise test at 200 px.

| Dimension | Scores 5 | Scores 9 | Automatic caps |
|---|---|---|---|
| **Stop power** | Pleasant but beige; reads as a catalogue | At 200 px one shape lands in half a second; the piece is the brightest and most saturated thing; one honest surprise (spotlight, levitation, split headline, monument crop). Benchmarks: anaar, F2, board 3, 26, 55, 96. | Product-only piece under 15% of the width: 5. Worn key detail under 8%: 0, rebuild. Pale piece on pale ground: 6. |
| **One message** | Two ideas compete, or prop and claim pull apart | A stranger can say what it claims in one sentence, and the picture proves the headline (1, 22, 57) | More than four text elements: 6. Grid or infographic panel: 5. |
| **Product truth and scale** | One countable detail off, or size unclear | Every countable feature matches the 19 Nov lock (clasp, stone count and colour, finish, halo rows); within 1.2× of true size; size tag or known-size object on magnified macros; no glints or floating props | Any fidelity error: 4. Worn piece over 1.2×: 0, rebuild. |
| **Layout craft** | Type touches the piece; muddled order; type under 26 px | Text only in calm areas inside the safe zone; headline, then product, then card read in order; card in its fixed place; no orphans or broken words; Story text between y 270 and 1250 | Text on the piece: 5. Any font fallback in the render log: 6. |
| **Brand consistency** | Off-system type; wordmark wandering or tiny | F2 card in place; wordmark 56 px; Velista, Cormorant and Jost used by role; one token ground; warm-neutral gold; reads as the same series as the previous batch | No wordmark (except no-text Stories): 5. |
| **Copy** | Generic occasion line, or meaning needs decoding | 2–6 words carrying a listing-verifiable truth, benefit or mechanism through one device; the occasion only as the second beat; primary text 120–180 characters with the offer ending by character 125 and COD qualified | Concept-noun headline: 5. Claim-led headline: 6. Unverified process claim: 4. |
| **Archetype fit** | Borrows the look, not the mechanism | Executes the borrowed mechanism (ranks cited) plus the Naira honesty layer; a reviewer can name the source rank unprompted | Mislabelled archetype: 6. |
| **Desire** | Clean but cold; nobody would want to wear it | Styling, skin, light and moment make the piece wanted: a named occasion picture in season, skin with texture, the piece flattering the body or the scene (ads-20's best sets won here) | Generated-looking skin: 6. |
| **Purchase cues** | Price hard to find; offer unclear; product hard to name | Price legible at 200 px; offer states its verified value; product identifiable at 200 px; landing page matches the ad (product, set cart or discount link) | Price smaller than the name: 6. Offer without a value: 6. Set ad landing on a single product page: 6. |

---

## 8. Owner decisions needed

1. **Water and colour-hold claims** ("waterproof", "tarnish-free", "anti-tarnish", "non tarnish").
   - The house rule bans them.
   - The live listings carry them: 16 of the 18 SKUs are tagged "Waterproof", "Tarnish Free" and "Hypoallergenic", and 15 carry "Waterproof and tarnish free" in their care text.
   - Two ACTIVE ads state them in primary text: Halo 15s B (120250695335670553) and Prism 11s (120250695639710553).
   - Several board patterns would be stronger with the claim: 7, 21, 75, 57, 66, 77, 86, 87, 95, 120, 160, 175. The keep-it-on plates depend on it.
   - Account evidence: the claim-led W1 made 0 sales on ₹3,236, against 5 for the texture-led W1. That comparison is not controlled (different ad sets, nine days apart). The claims panel P2 made 0. The Halo video sold while carrying the claim, which confounds its result.
   - Options:
     - (a) keep the ban and clean the listings and active ads to match;
     - (b) allow the claim on SKUs whose listing states it, with a documented wear and water test;
     - (c) allow water imagery but not the words.
   - This playbook currently treats water imagery as implying the claim, and uses none.
2. **"Hypoallergenic" and "nickel-free"** would need supplier documentation. They are not used.
3. **Faces.**
   - The house brief allows nothing above the jaw.
   - Our best static, F2, shows lips. So does the S1_04 frame planned for B1-01/02. The S3_12 frame planned for B2 shows a full profile including the eye.
   - Options: keep the jaw limit; allow lips; allow a profile with the eye; or allow full generated faces.
   - A15 mirror frames avoid the question only when the phone fully covers the face.
4. **Higgsfield edit passes on scale.**
   - F2 (S1_01, baguettes made about 30% finer) and S1_04 (head about 20% smaller) were both made by an edit pass that shrank the piece after a judge read it as oversized.
   - Does that count as "generated directly"? If not, F2's grammar has to be rebuilt with fresh generations and B1-01/02 use the fallback frame.
5. **Proof.** No verified review, rating or customer count exists, and no review app is installed. Options:
   - install a review app and collect verified reviews (this unlocks review cards and count seals);
   - print verified per-SKU order counts read from Shopify (allowed by the house rule; the caption rules currently ban counts);
   - use creator stills where usage rights exist (Riya, Ananaya). The creator reel had the top CTR, 11.47%.
   - Until one is chosen, proof is listing figures and service facts.
6. **Reference prices.**
   - Halo 15s B says "₹1,099 (was ₹2,200)"; the listing is ₹999 with a compare-at of ₹1,669.
   - Prism 11s says "was ₹4,200"; the listing compare-at is ₹3,999.
   - Prices have also moved within weeks: Woven ₹1,199 to ₹1,049; Brushed ₹799 to ₹699; Toggle ₹1,199 to ₹999.
   - Decide whether compare-at prices may appear at all. They may only if they were charged as selling prices. The current default leaves them out.
7. **Offer terms, to confirm before any on-image offer:**
   - the live values of BUY2, BUY3 and BUY4 (W1 creative 1514460987246299 says 20/30%; F2 and the checkout read in early November say 10/20%);
   - code or automatic;
   - minimum quantity and dates;
   - whether they combine with compare-at prices;
   - NAIRA10's terms (any order or first order);
   - any free-shipping minimum;
   - any COD fee.
8. **COD risk.** Meta counts a COD order as a purchase when it is placed. Decide whether to read COD share and returns to origin by `utm_content` before running "₹0 upfront" lines.
9. **Triple Coil turn count.** The title says triple and the gallery shows three turns; the description, size guide and supplier photo show two. The current references would generate three turns. It stays held until the turns are counted on a physical unit.
10. **Pearl wording on the Pearl Double Halo Studs.** The house wording is "shell pearl", but the listing says the pearl's source is not stated, and it gives no material or plating. This playbook uses the product name plus "bright silver tone · cubic zirconia" until the supplier confirms. Separately, "freshwater" in the skill's `tested-prompts.md` should be removed.
11. **Listing contradictions that affect ad copy:**
    - Cushion Halo: stray "Adjustable version is live!" text and a K8 SKU suffix. Are all 45 units adjustable?
    - Halo Curve: has no halo, and the listing says "Solid gold tone band".
    - Marquise: "Metal: Gold", and the silver photos are recolours of the gold ones.
    - Serpentine: gold ₹1,299 and silver ₹899 for the same design.
    - Toggle: the listing omits the cubic zirconia on the bar.
    - Verdant Circlet: the copy says 1 pearl where the photos show 2.
    - Verdant Eternity: "claw set all round" against an open back.
    - Brushed: is the hinge stated?
    - Woven: is "not cast" true?
    - Baguette Huggies: Ruby is sold out but is still the first listing image.
12. **Variant-level stock gate.** No single variant reaches 20 on Baguette Huggies (10/6/12/0), Droplet (9/11) or Marquise (15/9), and Triple Coil's silver has 19. This playbook excludes them by default to keep to "only stock 20 plus". The option is to opt them back in as line-ups only, with no single-variant ads and no silver Marquise imagery until a silver unit is photographed.
13. **Restocks.**
    - The two tested static winners are ruby Baguette Tennis Bracelet and Necklace, neither in the 20+ set. Restocking them would allow iteration on the account's two proven statics (new crops and hooks on the anaar and F2 images).
    - Catalogue best sellers below 20: Silk Mesh Cuff (about 24 sales), Roman Numeral Trio Ring (20), Cushion Solitaire Ring (17), Mesh Band Ring (about 14).
    - Six eligible SKUs have 0–5 units of headroom (Ribbon, both Serpentines, Bold Nocturne, Monochrome, Pearl Double Halo). One sale drops three of them out of the plan.
14. **Spend plan.** A test budget of about ₹20,000 a week paces the 500 over about 8 months. The alternative is to spend more on tests and less elsewhere (catalogue earns 67% of purchases).
15. **Files on record that break the rules:**
    - `lilac-papillon-ring-crazy13` (Feed, Story, `meta.csv` lines 806 and 809, `copy.json` line 2991);
    - `ten-creatives` A1, A3, A4, A5;
    - `night-shift/02` and `10`;
    - red-room R1, R2, R4;
    - keep-it-on;
    - `finished-ads` P09;
    - "RUBY" in the spec line of `diwali-10/01`;
    - the water droplets in `colour/53`.

    Retire them from reuse or correct them.
16. **Smaller calls:**
    - **Confectionery:** founder-kept `colour/03` (sugared almonds) conflicts with the food ban.
    - **Dhanteras coin motif:** crazy28 can read as a purchase of precious gold. Either keep "gold tone" explicit everywhere or retire the motif.
    - **Catalogue images:** whether A2 and A4 exports go into the Meta catalogue as additional images.
    - **Gift box:** whether the Naira gift box ships, before any box POV or gifting copy.

---

## Appendix A. Review points not applied, or applied in part

- **Critic 1 #8 (funding the crazy set by cutting A4, A8, A12, A9 and the A10 tiles to specific numbers):** applied in direction, with different totals. At the stated 95 images the crazy set is 130 ads (about 1.3 per batch); 200 needs the about-1,000-credit plan, because new pictures, not layouts, fund these archetypes.
- **Critic 1 #8 / A19 ("the native POV settles the face question"):** adopted as A15, but it settles the question only when the phone fully covers the face.
- **Critic 1 #11 (B1-01 = S1_04 re-rendered):** applied, but made conditional. `set1.json` shows S1_04 is an edit-pass frame and it shows lips, so it depends on two owner rulings; a fallback frame is specified.
- **Critic 1 #13, option (a) (S3_12 as the batch-1 Brushed ad):** moved to batch 2. The frame shows the eye in profile (face ruling), and the huggie is about 8% of the width, so it needs a locator.
- **Critic 1 #2 ("make every 4th A2 a no-headline card"):** replaced by a separate A1 Product Card archetype (65 ads), which tests the same idea more cleanly.
- **Critic 1 #3 (a Halo video frame as an anchor):** not used. The anchors are limited to tested statics so the comparison stays like for like.
- **Critic 1 #4 and Critic 3 #3 (two different worn-size thresholds):** merged: key detail at least 12% (target 15%), and 8–12% only with a hairline locator.
- **Critic 2 #14 (calibration grid on two heroes for batches 1–10):** applied to batches 1–4 only. Fifty ads on two SKUs would exceed Brushed's ₹699 cap and Cushion Halo's 25 units of headroom.
- **Critic 2 #19 (plan about 70 frames):** the task fixes the assumption at about 95 images, so the plan keeps 95. It states that the 19 Nov balance (144.46 credits) covers only about 72 images, and what to drop if there is no top-up.
- **Critic 2 #13 ("reserve about 10% of output for the catalogue"):** applied as extra 1:1 exports of A2 and A4 keepers, not ad slots, so the 500 remain statics for the feed.
- **Critic 2 #1 and #17 (₹1,000 screen against "tested only after ₹1,500"):** combined into one ladder: a ₹1,000 screen, then a test that stops at ₹1,500 with no purchase.
- **Critic 2 #29 against the caption rule "offer sentence last":** reconciled by putting the offer in the Meta headline field and keeping primary texts short enough that the final offer sentence ends by character 125.
- **Critic 3 #1 (keep `crazy3/08` as an A3 source):** rejected. Critic 1 measured its piece at 8–12% of the width, which fails the product-only size rule.
- **Critic 3 #2 (swap B1-05 to `colour/66`):** S2_06 was chosen instead, per Critic 1 #14: it is wedding season, the frame is a ring, and it was judged 8.20. `colour/66` is B1-05's fallback and runs in batch 4.
- **Critic 3 #19 (occasion only as the second beat) against Critic 1 #25 (an occasion picture every batch):** both applied. The occasion lives in the picture; the headline leads with a truth ("Greener than the mehendi." leads with the colour).
- **Critic 3 #22 (the B1-04 cube prompt fixes):** moot, because the arc-on-cube ad was removed from batch 1. Its points (no steel cube beside brushed gold; an empty bottom zone; acceptance criteria) are carried into the A9 day/night spec and the new prompts.
- **Critic 3 #6 (B1-03 upscaled a body photo):** moot for batch 1, since the Toggle is out. The rule is kept for every later ad: crop body photos from 2K originals at native resolution and never upscale them.
- **Critic 2 #22 (retargeting for draft archetypes A7, A11, A12 and A14):** applied to their new equivalents: A8 Callout, A11 Offer Poster, the A5 numerals and A10 pick-your.
- **Draft rule "at least one ring per batch" (draft §5.2):** dropped with the ring bonus (Critic 2 #6). It is replaced by "no more than 2 ads per product per batch".
