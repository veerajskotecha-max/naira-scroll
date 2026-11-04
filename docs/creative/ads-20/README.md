# Twenty Meta ads in four sets of five (4 Nov 2026)

The ask: study how GIVA and Palmonas make their ads, score their ads and ours on one scorecard, then make 20 ads for Naira in four sets of five with new Higgsfield photos, comparing and redoing each set before starting the next.

Nothing here has been uploaded to Meta or changed on Shopify. The ads are ready to upload; the owner decides what runs.

The review page, with every Feed card beside its Story, the score and the judge's note: https://claude.ai/artifact/PFfemVEbFQVCZfQbVmVAX5 (private until the owner shares it).

## Files

| Path | What it is |
|---|---|
| `ads/` | The 40 finished files: each ad as a Feed card (1080×1350) and a Story (1080×1920) |
| `captions.json` | A headline and primary text per ad, CTA Shop now |
| `review/set1_sheet.jpg` … `set4_sheet.jpg` | Each set on one sheet, Feed above Story |
| `build/scores.json` | The rubric, the first-pass benchmark scores, and both rounds of the independent judge |
| `build/setN.json` | The photo briefs per set (shot, fidelity lock, scale, skin, scene, light, negatives) and every redo or edit with its reason |
| `build/setN_layout.json` | The type layout per ad and format |
| `build/render.py`, `shot.cjs` | The type system: HTML set in Cormorant Garamond and Jost over the photo, rendered by Chromium |
| `build/prompts.py`, `sheet.py`, `board.py`, `merge_scores.py` | Prompt assembly, review sheets, the review page, the score merge |

The raw Higgsfield photos (1536×2752) stay in the session scratchpad and are not committed; every finished file is in `ads/`.

## The benchmark

Live ads in the Meta Ad Library, India, 2–4 Nov: GIVA (page 350941852220221, 430 active ads) and Palmonas (page 104818178629041, 2,122 active). The strongest was Palmonas's "9KT Pendant Free" carousel: an on-model beauty crop with the whole lockup at the bottom (wordmark, an upright serif offer, a qualifier, an outlined button). GIVA's best was "A hot cup of silver, anyone?": one idea, hands, a two-line serif with wit, no price.

What theirs had and our recent ads did not: the piece on skin at a readable size, type that is legible on a phone, the offer inside the image, and one strong ground instead of beige on beige.

The rubric has ten criteria, weighted: stop .15, truth (product and scale) .15, craft .15, desire .10, hierarchy .10, offer .10, brand .05, series .05, platform .05, compliance .10.

## The four sets

| Set | Grammar | Pieces |
|---|---|---|
| 1 · Studio product cards | Palmonas's carousel card on a rosewood studio, plus the price and the Buy 2 / Buy 3 chip | Baguette Tennis Necklace, Woven Gold Hoops, Prism Rivière Bracelet, Cushion Halo Ring, Toggle Link Chain |
| 2 · Wedding-season moments | GIVA's grammar: one Indian ritual and one witty serif line | Verdant Eternity Band (mehendi), Baguette Huggies (gajra), Kiss Knot Bangle (gift), Marquise Layering Set (sangeet), Verdant Circlet Studs (Banarasi) |
| 3 · Offer heroes | The Palmonas lockup on a black camisole and a blush set, one true reason to buy per card | Baguette Tennis Bracelet (any three, 20% off), Brushed Gold Huggies (₹799), Halo Curve Ring (free insured shipping), Pearl Nugget Hoops (gift box), Emerald Deco Hoops (cash on delivery) |
| 4 · Best of, after the judge | One occasion, one line, one saturated colour behind the piece, four type lines at most, the Story composed first | Prism Cluster Studs (teal), Marquise Drop Choker (haldi yellow), Silk Mesh Cuff (navy), Ribbon Bead Bracelet (rani pink), Aqua Heart Drops (wine) |

## How every frame was checked

- Detail against the product photo: stone count, cut, colour order, metal tone, clasp.
- Size against the body, with a pixel ruler on the ear, finger, hand or neck, against the size on the product page; anything reading more than about 1.2× its listed size was fixed. The fix was an edit pass with the frame as the reference: the piece made smaller, everything else kept.
- Anatomy: hands counted, every arm traced to a shoulder.
- Type: nothing under 27px on a 1080 canvas (about 10pt on a phone); Story type kept between y=270 and y=1500, clear of the profile bar and the Shop button.
- Claims: only what the storefront states today. Metals as gold tone or silver tone, colours as colours (never gem names), no durability words.

Redone or edited along the way, with the reason recorded in `setN.json`: the ruby necklace (twice: chunky collar, then 30% finer after the judge), the woven hoop (34mm against 25mm), the prism bracelet (a second hand with no arm), the halo ring (twice: oversize head and star glints, then 20% smaller after the judge), the baguette huggie (22mm against 15mm), the kiss knot bangle (a letterboxed frame), the marquise set (pink on pink, reshot in magenta), the verdant stud (23mm against 16.8mm), the tennis bracelet hero (the bracelet sat in the type zone), the pearl and emerald hoops (about 1.9× and 1.8×), the ribbon bracelet's bow and the aqua heart drop.

## Scores

An independent judge (a separate agent that saw only the images and the rubric, never these scores) scored every ad by eye, twice. Weighted mean out of 10:

| Group | Round 1 (Sets 1-2 as first built) | Round 2 (all 20 after the fixes) |
|---|---|---|
| GIVA and Palmonas live ads | 7.09 | 7.05 |
| Naira's recent ads | 6.83 | 6.60 |
| Set 1 · studio product cards | 7.62 | 7.71 |
| Set 2 · wedding-season moments | 8.03 | 7.98 |
| Set 3 · offer heroes | | 7.90 |
| Set 4 · best of | | 7.90 |

The best competitor ad, Palmonas's 9KT hero, scored 8.75 and 8.57. The 20 new ads average 7.87, about 1.3 above our recent ads. Most of the gain is in truth (every piece on a body at a believable size) and offer (the price and the bundle chip in the image). They sit 0.4 to 0.6 below the Palmonas hero on photo craft (skin that can read as generated) and desire. Most also stack five or six lines of type, where the Palmonas hero uses three or four; that is the next thing to cut.

Top of round 2: Verdant Eternity Band, mehendi (8.20); Brushed Gold Huggies, ₹799 (8.20); Marquise Layering Set, sangeet (8.18); Marquise Drop Choker, haldi (8.07); Cushion Halo Ring and Ribbon Bead Bracelet, bridesmaids (8.05). Lowest: Prism Rivière (7.33, no occasion), Emerald Deco Hoops (7.45, the cheek reads plastic), Toggle Link Chain (7.55, cream on cream).

The judge's launch picks: S2_06 mehendi band, S2_09 sangeet layers, S4_17 haldi choker, S3_12 ₹799 huggies, S4_19 bridesmaid bracelet and S3_11 three-for-20%, with S1_04 as first reserve. They cover a ring, two necklaces, earrings and bracelets from ₹799 to ₹1,599 and test a named wedding moment against a hard reason to buy now.

After round 2, the five Story fixes it asked for were made (the choker headline off the skin, ink type on the bangle's pink box, a short Buy 3 chip clear of the fingers on the cuff and bridesmaid Stories, the prism wordmark off the bracelet); the scores above are from before those fixes.

## Flags for the owner

- Two frames still read slightly large against the body: the Emerald Deco Hoop (about 1.3× by the ear, the same as the live listing's own "worn, shown at true size" photo; three edit passes) and the Ribbon Bead Bracelet's bow (about 1.3×). Both are noted in `setN.json`.
- Several live product descriptions say "Waterproof and tarnish free" and "anti-tarnish", and some product tags read Hypoallergenic, Tarnish Free and Waterproof. The ads avoid these words; the listings were not changed.
- The live W2 "Almost edible" ad's caption still says 20% / 30% off while checkout gives 10% / 20%. Not changed; any Meta change waits for the owner.

Higgsfield: about 78 credits across the four sets, redos and edits included (one edit was sent with the wrong reference and its result was not used); 3.71 credits left.
