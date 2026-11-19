# b03 loop check (19 Nov 2026, about 20:25 UTC)

**What I looked at**
- At 200 px: `b03/sheet.jpg` and `b03/sheet_story.jpg`, `b02/sheet.jpg`, the anchors in `build/anchors/` (all five winners and five
  losers on one sheet), and board ranks 1, 3, 4, 26, 42, 55, 57, 66 and 96.
- The refs for Serpentine Silver (plinth, detail, the verified worn plate `lilac_YF8439-SLV_S2_a2c.jpg`) and Toggle (cube, clasp).

**What I read**
- b03: `review.md`, `verify.md` (with the skeptic), `brief.md` §0, §2, §5 and §6, the four `copy.json` and the page sources.
- b02: `review.md`, `loop.md`, `rescue.md` and `rescue-ledger.json`.
- `build/learnings.md`, `build/ledger.json`, `build/study/products.md` (Brushed, Cushion, Halo Curve, Serpentine Silver, Toggle,
  Ribbon), `RULINGS.md`.
- Live, read-only:
  - Higgsfield balance **14.46** at about 20:25 UTC. The transaction log shows b03's 7 pictures at 2 credits each (5 at 19:10, 2 at
    19:24) and no other spending since.
  - The Shopify listing of Brushed Gold Huggies: one variant at ₹699, 58 units. The text is plural ("These huggie hoops measure
    … keeps them quiet on the ear"). So the b03-1 beat "the ₹699 earrings." matches the listing, and review.md's open pre-launch
    check is closed. The listing never says "pair", so no copy should say "pair" until the owner confirms it.

**Better than the previous batch:** yes, on every measured count except desire and the honest surprise.
- **Ads shipped:** 4 of 5, against b02's 2 of 5 (b02-1, plus b02-5 from the rescue).
- **Shipped mean:** 7.70, against 7.44 for b02 (b02-1 7.35, b02-5 7.53).
- **Stop power:** 7.69, against 7.00. This was the b03 fix target, and it was met.
- **Truth:** 8 or more with both critics on all four ads (mean 8.19). Fidelity held on all 7 pictures, with no morph.
- **Credits:** 7 of the 9 allowed pictures, with no waste. The one failed regeneration (b03-4) tested an untried fix, and the
  lesson is now in the learnings (size words do not shrink a lone product).
- **Not better:**
  - Desire is 6.94, the lowest dimension and the only one that fell.
  - The honest surprise is still 0 for 5 after three batches.
  - No ad beats a winner anchor with both critics.
  - The critics scored three of the four ads before the finisher's fixes, for the third batch in a row (change 2).

## Changes for b04

### 1. Finish the record fixes that b02's loop ordered before b03 (zero credits; two batches overdue)

**The finding.** b03 `brief.md` §0 made (b), (c) and (d) pre-b03 items. None of them was done.
- `ledger.json` still says b01-4 "ship (truth caveat …)".
- `b01-1_feed.html`, a live ship row, still prints "Code BUY2 · 10% off" before two codes. So does b01-4.
- `b02-1_feed.html` still sets `.beat` at 48 px, which is 0.52× the 92 px headline (PLAYBOOK §4.0 floor 0.6).
- New: `ledger.json` still marks b02-5 "dropped" and b02-2 "dropped". Their real verdicts (b02-5 ship, means 7.3 / 7.75; b02-2
  reject) sit only in `batches/b02/rescue-ledger.json`. That is why the b03 review and learnings count b02 as "1 of 5". It was 2
  of 5, and the three-batch count is 7 live ads of 15.

**How**
- Set the b01-4 verdict to "held (critic A truth 6 on re-score, under the 8 floor)".
- Copy the b02-2 and b02-5 rows from `rescue-ledger.json` into `ledger.json`, replacing the "dropped" rows, including verdict,
  weightedA/B, feed, story, copy, scoredFile and `"rescue": true`.
- Change "Code BUY2" to "Codes BUY2" in `b01-1_feed.html` and `b01-4_feed.html`, and re-render.
- Set b02-1 `.beat` to 56 px (0.61×), keeping it centred at top 296, and re-render. The render must report `outside []` and
  minFont 26.
- Correct the b02 count in the b03 notes of `learnings.md` to 2 of 5.

**Test**
- `grep -l '>Code BUY2' batches/*/b0*_feed.html` returns nothing.
- b02-1 `.beat` is `font-size: 56px`.
- In `ledger.json`, b01-4's verdict starts with "held", b02-5's with "ship", and b02-2's with "reject".

### 2. Score the file that ships: the re-scores b03 still owes, and the order for b04

**The finding.** The b03 critics scored the 19:46–19:57 renders. Then the finisher changed:
- b03-1's beat, card line and Story tag (final 20:09:21);
- b03-2's Story tag (20:09:36);
- b03-3's callouts, metal line and scrims (20:12:01).

The review says the re-score "is still due". This is the third batch in a row that does not meet the scoredFile test (b02 loop
change 6). In the ledger, the b03-1 and b03-3 `scoredFile` times do not match the Feed JPGs' `stat -c %y`.

**How**
- **Before any b04 picture:** both critics re-score these final JPGs once, at full size and on the 200 px sheet with the same
  anchors:
  - the b03-1 Feed and Story;
  - the b03-2 Story;
  - the b03-3 Feed;
  - b02-1, after change 1.
- Replace weightedA/B and `scoredFile` (file plus `stat -c %y`) with the re-scores. An ad that breaks the PLAYBOOK §7 ship rule on
  re-score is held.
- **In b04:** `review.md` is written only after both critics have scored the final files. Any fix a critic asks for goes back to
  both critics in the same step, before the review, never after it.

**Test**
- For every ledger row whose verdict starts with "ship", the `scoredFile` time equals the Feed JPG's `stat -c %y`.
- `b04/review.md` contains no "re-score still due".

### 3. b04 has 2 pictures and is the last batch that can generate: make them one at a time

**The finding**
- At 14.46 credits with a 10-credit floor, b04 can make (14.46 − 10) ÷ 2 = **2 pictures**.
- After b04 the balance is 10.46, which allows 0 pictures. So under RULINGS §1.3 the loop stops after b04 unless the owner adds
  credits.
- One batch call would spend both pictures blind. A second picture chosen after the first has been verified can be its
  regeneration or a new slot, whichever helps more.
- PLAYBOOK rule 7 (at least 3 lights and 3 cameras) cannot hold with 2 pictures.

**How**
- **The owner.** The lead tells the owner before b04 that 2 pictures remain and the loop then stops. The owner decides whether to
  add credits. With more credits, b04 runs as a normal 5-slot batch under changes 4 and 5.
- **Picture 1.** One `generate_image` call for the new move (change 4). Then the verifier and the skeptic judge it.
- **Picture 2.** Re-read the balance, then choose:
  - picture 1 failed on scale, eyes or extent → its one regeneration, with the fix written as a pose, crop or ratio clause, never
    as size words alone (b03 prompting learnings 1–2);
  - picture 1 passed, or its clasp morphed (never regenerate a morph) → one A3 product-only slot under change 5.
- **Zero-credit ad.** Lay out the b03-4 Monochrome float try 1 (`pics/b03-4_try1.png`) as a card-only A1 at Feed P 100, with
  the verifier's numbers:
  - hoops and shadows at Feed 134–827;
  - "Shown magnified · about 20 mm tall" on one 26 px line at Feed 851–913;
  - the card at 940;
  - "BLACK. WHITE. / GOLD TONE." on the Story only;
  - no claim and no water.

  It goes to both critics as a new layout. It is the only honest surprise b04 can afford.
- **Rule 7.** The b04 brief states that rule 7 is suspended for a 2-picture batch.

**Test**
- `b04/jobs.json` has at most 2 jobs, and the second job's `submitted_at` is after picture 1's verdict time in `b04/verify.md`.
- The balance is 10 or more after b04.
- The b03-4 card-only rescue has two critic scores in `b04/review.md`.

### 4. Replace the new move: worn Serpentine Silver at the F2 lips-to-chest crop cannot meet its own size bar

**The arithmetic.** This is the same kind of failure b02 loop change 3 caught for the single-ear Circlet.
- **The bar.** The learnings ask for "the chain's key detail at 15% or more of the Feed width", at a lips-to-chest crop, within
  1.2× true size.
- **Read as the pendant**, the bar fails on scale:
  - the pendant is a 10 mm cushion stone in a basket (`products.md`), about 11 mm wide;
  - a lips-to-chest frame is about 25–30 cm wide (the F2 anchor spans the shoulders), so the pendant is about **3.5–4.5%** of the
    width at true size;
  - 15% needs a frame about 7 cm wide, which is a pendant macro, not a lips-to-chest crop;
  - even the verified worn plate (a neck crop about 14 cm wide) shows the pendant at about 7–8%;
  - the model will grow it toward the ask, and "the pendant grows" is this SKU's listed morph.
- **Read as the whole chain**, the bar fails at 200 px:
  - the 2 mm snake chain draws about 1.3 px wide on the thumbnail;
  - so the lips and skin land first, which is b02's "the hair lands first" failure and breaks starting rule 1.

**How: brief the worn slot on Toggle Link Chain, worn with the toggle at the front, in a neck-and-collarbone crop**
- **Why Toggle**
  - It has 77 units, the deepest stock of any SKU never briefed (0 of 15 slots), and claims are allowed.
  - Its 22 mm sailor ring and 4 mm paperclip links are a bold gold shape.
  - In a 14–15 cm-wide frame, the ring is **about 15%** of the width at true size.
  - `build/refs/toggle-link-chain__clasp.jpg` already shows the clasp worn at the front on skin. "Exactly as in the reference" plus
    the reference's own pose held construction on all 7 b03 pictures.
- **Prompt**
  - Ref slot 1 is the clasp (`59d6c393-…`), the authority for the clasp and the pose. Slot 2 is the cube (`d3c384eb-…`), for the
    links only.
  - Use the products.md lock word for word, plus RULINGS §3: a spring-gate sailor ring about 22 mm, a bar about 0.6–0.7× the ring
    with one row of tiny cubic zirconia; never a donut, never a lobster clasp.
  - "SCALE, the most important instruction": the ring is about one fifth as wide as the neck, never a third; the paperclip links
    are 4 mm wide.
  - The frame is the neck and collarbones only. The picture's top edge is at the chin or below, so there are no lips and no eyes,
    and the native 9:16 Story is safe.
  - Deep warm skin with visible pores, a zari or silk neckline edge at the bottom of the frame, and a dark plum or ink ground at the
    neck sides.
  - No water on the jewellery.
- **Acceptance (verifier)**
  - The clasp matches the clasp ref, and bar ÷ ring is 0.6–0.7.
  - The links are paperclip, never cable or curb.
  - Ring ÷ neck width is 0.17–0.22. Drop the picture above 0.24 (1.2×).
  - The ring is 13–18% of the Feed width.
  - ΔE76 between the ring and the skin behind it is 25 or more.
  - No eye, nose or lips anywhere in the native 9:16 frame, not only in the Feed window.
  - The ring lands first on the 200 px gate.
- **Copy.** The first beat is the listing's own mechanism ("turn the clasp to the front", the products.md MACRO archetype). The
  occasion goes in the second beat.
- **Serpentine Silver waits** for a product-only A4 or A6 frame. Its true-scale pendant can only be the hero there.
- **Learnings.** Update the "One new move for b04" text to this slot. If the lead keeps Serpentine instead, rewrite its bar to
  what a 10 mm pendant can honestly reach (about 7% of the width in a neck crop, no lips) and expect the 200 px gate to fail.

**Test, and the process fix behind it.** Every b04 slot spec states one line: the key detail's mm ÷ the frame width in mm implied
by the crop = the width share at 1.0×. A slot whose bar needs more than 1.2× is rewritten before any credit is spent.

### 5. If picture 2 is an A3 Literal Rhyme: lock the prop's scale, and follow the two sold A3 anchors on the ground

**The finding: the prop becomes a referent**
- The learnings' examples are a marigold head of about 4–5 cm by a 14 mm huggie, and a mogra bud of about 2 cm by 17.5 mm studs.
- Each puts a referent in the frame, and the skeptic measures the piece against it.
- The model grows pieces 1.27–1.6× against referents: b01-2's bud came out 1.6× and was dropped. A lone product takes 47–76% of
  the width.
- The b03 product-only frames passed scale only because they had **no** referent.

**The finding: the ground rule contradicts our A3 winners**
- The b04 fix target says "dark saturated grounds only". Both A3 winners that sold sit on light warm grounds: the apricot hoops on
  peach silk, and the anaar bracelet on cream.
- In both, the prop is larger than the piece and carries the saturated colour.
- Our light-ground losers failed for other reasons: pastel or clear pieces on pale grounds (kandil, vks5, p2), or heavy text
  (sa08). Starting rule 2 already covers the first.

**How**
- **Prompt.** Lock the piece ÷ prop ratio from real mm first, as "SCALE, the most important instruction", with a never-limit. For
  example: "each huggie is about one third as tall as the marigold head, never half".
- **Measure.** The verifier logs piece ÷ prop against the true ratio and drops anything above 1.25×. Or choose a prop with no
  fixed size: silk, loose petals, powder, a syrup or glaze pool.
- **Size.** The prop may be larger than the piece, as in both winners. "Lands first" then means the piece is the brightest metal
  shape.
- **Ground.** "Dark grounds only" applies to silver, clear and pastel pieces and to lone product frames. A gold-tone A3 may use a
  light warm ground when the prop owns the colour.

**Test**
- `b04/verify.md` logs piece ÷ prop against the true ratio for the A3 slot.
- The b04 brief names each slot's ground with the rule or anchor it follows.

## Layer by layer

| Layer | Verdict | Evidence |
|---|---|---|
| Picture: subject and scale | holds for product-only; change 4 (worn), 5 (A3) | 7 of 7 pictures held construction. The sliding window placed every kept picture. The two b04 ideas that bring a body or prop into the frame break true scale as written. |
| Picture: colour ownership | holds, scoped by change 5 | Plum and ink gave the loudest frames, and cocoa and sage read drab (already in the learnings). Our own sold anchors show that light warm grounds win when a rhyme prop owns the colour. |
| Picture: surprise | change 3 | 0 for 5 over three batches. The b03-4 card-only rescue is a float the model has already drawn, at zero credits. Board 96 is the same idea. |
| Camera | holds | Reference poses worked (C2, C5, C3). Every b03 piece is upright, centred and frontal. Boards 4, 26 and 42 tilt the product, but with 2 pictures there is no room to test a new pose. |
| Light | holds as logged | Do not brief L2 flash (soft twice). The pool edge stays soft. Both are in the learnings. |
| Layout | holds | Extent first, scrims sampled from the picture, one boxed element per Story, beat ratios logged (.64, .63). The dead Story floor is already in the b04 fix target (riser). |
| Branding | holds | 8.00. One card system, wordmark at 56 px. |
| Copy | holds as targeted | First beats list parts ("TWO STONES. ONE OPEN BAND."). The b04 fix target already asks for a reason to want first. b03-1's "earrings" matches the live listing (checked). |
| Meta text | holds | Headlines 34–39 characters, value inside. The Pearl headline is fixed. Descriptions are 24–29 characters. |
| Offer | change 1 | NAIRA10 is a clean card-only cell. b01-1 still prints "Code" before two codes. |
| Product mix and stock | change 4 | Toggle (77 units) has had 0 of 15 slots. Serpentine Silver has 23 units, 3 over the floor. |
| Prompting | holds, plus change 4's clasp-ref pose | The b03 learnings (11 items) cover size words, pose, shadows, pearl colour, matte floors and "dark sage". |
| Process | change 1, 2, 3 | Three pre-b03 record fixes were not done. The scored files are not the shipped files for the third batch. b02-5's ship is missing from the ledger. No credits were wasted. |

## Trend (ledger scores, mean of both critics, shipped ads)

| Batch | Shipped | Ads | Batch mean |
|---|---|---|---|
| b01 | 2 of 5 (1 live: b01-4 held) | b01-1 7.45 · b01-4 7.07 | 7.26 (7.45 live) |
| b02 | 2 of 5 (1 + the b02-5 rescue) | b02-1 7.35 · b02-5 7.53 | 7.44 |
| b03 | 4 of 5 | b03-2 7.91 · b03-1 7.82 · b03-5 7.73 · b03-3 7.34 | 7.70 |

- The scores rise about 0.2 per batch, and the yield doubled in b03.
- Truth climbs: every b03 ad is at 8 or more with both critics.
- Desire is flat at about 6.9–7.0.
- No ad has beaten a winner anchor with both critics in three batches, so no note has become a rule.
