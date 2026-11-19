# b03 brief (19 Nov 2026, written about 18:55 UTC)

Creative director's brief for batch b03: 5 static ads, `b03-1` to `b03-5`. Sources, in order of precedence: `RULINGS.md`,
`PLAYBOOK.md`, `build/study/products.md`, `build/learnings.md`, `build/ledger.json`, then `batches/b02/review.md`,
`batches/b02/loop.md` (its six changes are applied below, one by one) and `batches/b02/verify.md`. Nothing has been
generated for b03 yet.

## 0. Pre-flight

| Check | Result |
|---|---|
| Higgsfield balance | **28.46 credits at about 18:50 UTC.** Unchanged since b02's last job (18:03) and the loop check (18:36). |
| Picture budget (loop change 4) | Keeping the 10-credit floor: (28.46 − 10) ÷ 2 = **9 pictures**. The 5 first tries go in **one** `generate_image_batch` call. Then at most 4 regenerations, only for a slot whose first try failed on size, extent, float, light or calm zones. **Never regenerate a slot whose piece morphed.** The generator re-reads the balance right before the call. If it is under 28, it makes (balance − 10) ÷ 2 pictures, cutting regenerations first, then slots in this order: b03-3, b03-5, b03-2, b03-4. b03-1 (the new move) is cut last. If more than 4 slots fail, regenerations go in this order: b03-1, b03-2, b03-4, b03-5, b03-3. |
| Stock and price (Shopify `graphql_query`, read-only, about 18:52 UTC) | All match RULINGS §2. This batch uses: Brushed Gold Huggies 58 · ₹699; Cushion Halo Ring 45 · ₹999; Halo Curve Ring 29 · ₹899; Monochrome Enamel Hoops 24 · ₹999; Pearl Double Halo Studs 25 · ₹1,199. All are single-variant SKUs. |
| Offers (same read) | All ACTIVE codes: NAIRA10 (10%, any order, no minimum), BUY2 (10%, 2+ items), BUY3 (20%, 3+), BUY4 (30%, 4+). FRIENDSANDFAMILY is internal, not for ads. No free-shipping discount exists. |
| Claims | Brushed, Cushion and Halo Curve carry the Waterproof, Tarnish Free and Hypoallergenic tags, so the claim may appear, and only as proof in the primary text (learnings rule 8). **Monochrome and Pearl Double Halo carry no claim tags: no claim and no water anywhere.** No picture in b03 shows water. |
| Excluded this batch | Toggle (no clasp-locked slot), Prism and Verdant Circlet (loop change 4: no worn retries), Woven (at its phase-1 cap), Serpentine gold and Bold Nocturne (exactly 20 units, no headroom). Serpentine Silver and Ribbon are queued for b04 (§6). |
| Zero-credit items owned by the lead and finisher, to finish **before** b03 renders (loop changes 2 and 6) | (a) Lay out **b02-2 try 2** (Brushed float, Feed P 80, b02-2's copy unchanged) and **b02-5 try 1** (Verdant Eternity standing ring, Feed P 100, re-labelled A1 with the size tag), with the loop's exact numbers. Both go to both critics under the normal ship rule. (b) Set b01-4's ledger verdict to "held (critic A truth 6 on re-score, under the 8 floor)". (c) Re-render `b01-1_feed.jpg` with `Codes BUY2 · 10% off ◆ BUY3 · 20% off`. (d) Re-render b02-1 with the 56 px beat (loop change 5), then have both critics re-score it. None of these spends a credit, and none is a b03 slot. |

## 1. Batch idea

**The piece is the monument.** All five frames are product-only, and each is built around the model's habit of centring the
subject. The sliding Feed window (loop change 1) does the placing, so the prompt only has to get the **size** right. In
every frame the piece is the largest, brightest and most saturated shape, at 45–66% of the Feed width. Each ground is darker
or cooler than gold for the gold pieces, and dark or flat-saturated for the silver and clear pieces. The batch's honest
surprise is one the model has already rendered twice: the float with detached shadows.

**What b03 tests**
1. **The one new move (loop change 3).** It replicates the only candidate note, "gold-tone mass on a saturated dark ground"
   (b01-4 on plum), on **Brushed Gold Huggies as an A4 monument on a plum glaze**. A win over the winner anchor with both
   critics makes it the first ads-500 rule. A loss retires the note.
2. **Does the F2 and anaar grammar (one huge piece, card only, no headline) carry onto an eligible hero?** b03-2 puts the
   Cushion Halo at about 60% of the width, the anaar bracelet's share. It also carries the **NAIRA10 single-product offer
   cell**, queued since b01 (b02 brief "Queued for b03"). The offer is a card variable, not the creative move. Log it so live
   reads can separate it.
3. **Does an honest surprise finally ship?** b03-4 is the Monochrome float (A13). The crazy slots are 0 for 4 over two batches.
4. **Three never-briefed SKUs enter:** Halo Curve, Monochrome and Pearl Double Halo.

## 2. What b02 lacked, and how b03 answers it

What I looked at: b02 `sheet.jpg` and `sheet_story.jpg` (only b02-1 shipped); all ten b02 pictures in `pics/`, on one contact
sheet with the 4:5 window marked; b01's `sheet.jpg`; the five winner anchors; and board ranks 1, 3, 4, 22, 26, 40, 42, 55, 57,
66, 79, 81, 85, 95, 96, 109, 155 and 190.

| Layer | Missing or weak in b02 (1 of 5 shipped, mean 7.35, stop power 7.63 → 7.00) | b03 answer |
|---|---|---|
| Visual: hero | b02-1's hoops are 13% of the width each, at the far frame edges, gold on a same-hue apricot ground. The black hair is the shape that lands at 200 px. The reading column (headline, then card) ran down the centre and skipped the product. | Five product-only frames. Each piece is centred, at 45–66% of the Feed width (anaar and F2 sit at 55–65%), with its key details inside x 216–864. Grounds: plum, cocoa, deep sage, terracotta, ink. Each is darker or cooler than gold for the gold pieces, and dark for silver and clear. None is the same hue as the piece. |
| Visual: surprise | Crazy slots went 0 for 4: the levitation was dropped twice, the selective colour once, and b01's cone came out a smear. The b02-2 float did render (twice); it died only on the fixed crop. | b03-4 is a float the model has already drawn, now with the sliding crop and a size it can fit. b03-5's spotlight is described only by its result (a crisp pool of light on the riser, near-black around it), never as a beam or haze. It is not the batch's crazy slot. |
| Camera | Worn frames passed 1 of 10 over two batches. Subjects grew 1.3–1.75× past the size asked. Moving Verdant Eternity out of its reference pose collapsed the S-wave. | No worn frame (loop change 4 allows at most one, and no worn geometry with a proven pass fits an eligible piece; §6). Every piece keeps its **reference pose**: Brushed upright as b02-2 rendered it, Cushion in its macro pose, Halo Curve in its cube pose, Monochrome and Pearl in their pack poses. Sizes are asked at about 0.7× the share wanted, as a share of the frame **height**. Cameras: C2, C5 and C3. |
| Light | L5 bloom and the L3 gel rim did not render. b02 effectively shipped one soft frontal light. | Only lights that have rendered, each described by what it does to the piece: L1 raking (b01-4), L7 soft window (b02-5), L2 flash (b02-3), L6 soft overhead (the shadow geometry of b02-2's float) and L1 pool. Four codes, with L7 used once. |
| Layout | The fixed central crop and the card at Feed 940 killed 5 of the 7 dropped slots. b02-1's beat was 0.52× the headline, so it was invisible at 200 px. | Sliding Feed window (loop change 1). Each spec states its extent budget and a starting P. Every beat is at least 0.6× the headline, logged. Every Story stack has a measured order and a rule for what to drop if the piece sits higher than expected. All widths below come from the kit fonts, measured with the kit CSS in Chromium. |
| Branding | The card and the 56 px wordmark held. b01-1 still prints `CODE` before two codes. | The same F2 card on all five, in the same place. Every two-code box says `CODES`, and the NAIRA10 box says `CODE` (one code). Bone on dark everywhere, so this batch shows one consistent series. |
| Copy | The first beats were truth-led and held. Still never live: a ₹699 ad, a bundle line, a single-product offer, any of five SKUs. | Five truth-led first beats: "BRUSHED, / NOT POLISHED." (listing finish line); "TWO STONES. / ONE OPEN BAND."; "BLACK. WHITE. / GOLD TONE."; "TWO BANDS. / ONE LIGHT."; and A1 with no headline. The occasion appears only as a second beat ("for the sangeet, after dark."). ₹699 sits in the beat with BUY3 in the primary text. NAIRA10 is on one card. Meta headlines are 34–39 characters with the value inside. Each offer ends at character 123–125. |
| Products | Only Cushion and Woven have shipped. Five in-stock SKUs had never been briefed. | Heroes Brushed (the new move) and Cushion (resting since b01) lead. Halo Curve, Monochrome and Pearl Double Halo appear for the first time. Verdant Eternity's turn rides on the b02-5 layout (§0). |
| Process | The critics scored pre-fix renders. | Scoring order and `scoredFile` with modification time (loop change 6, §5). |

### Loop changes, one by one

1. **Slide the Feed crop; stop asking for positions.**
   - Every Feed page sets `.pic { object-position: 50% P% }`. The window top is T = 5.85 × P, and Feed y = src_y × 0.703125 − T.
   - Each spec gives its subject-extent band and a starting P computed from a centred subject. The verifier sets the final
     P from the measured extent (piece, its shadow and any referent) and logs extent, T and P in `verify.md`.
   - Prompts say "centred in the frame" and give sizes as a share of the frame **height** (and width) at about 0.7× the share
     wanted. They never give a placement percentage, apart from naming the central 4:5 window.
   - No slot is dropped or regenerated for position alone.
2. **The two b02 pictures that pass truth.** b02-2 try 2 and b02-5 try 1 are laid out at zero credits before b03, per the
   loop's numbers (§0). b03 does not duplicate them: no Brushed float and no Verdant Eternity standing ring in b03.
3. **New move.** Brushed A4 monument: the pair upright on a deep plum glaze, the only gold in the frame, low camera at about 8°,
   each huggie about 26–30% of the Feed width (the pair 58–70%), no blue or yellow near the satin. Copy "BRUSHED, / NOT
   POLISHED." with the size tag. `verify.md` logs each huggie's width share. The review states the note's outcome: promoted
   or retired.
4. **Credits and slot mix.**
   - 5 slots and 9 pictures (§0).
   - **5 of 5 product-only** (at least 4 required), 0 worn.
   - **3 never-briefed SKUs** (Halo Curve, Monochrome, Pearl Double Halo; at least 2 required).
   - No Prism, no Circlet, no Toggle.
   - The crazy slot is b03-4, a float the model has already drawn twice. No crazy slot depends on a described light effect.
5. **Beat at least 0.6× the headline.**

   | Ad | Feed H1 | Feed beat | Ratio | Story H1 | Story beat | Ratio |
   |---|---|---|---|---|---|---|
   | b03-1 | 100 | 64 | .64 | 80 | none | – |
   | b03-4 | 92 | 56 | .61 | 80 | none | – |
   | b03-5 | 76 | 48 | .63 | 72 | 44 | .61 |

   - b03-2 (A1) has no headline. b03-3 (A8) has callouts, not a beat.
   - The finisher logs H1 px, beat px and the ratio in each `copy.json` `layout`. Under 0.6 is a fail.
6. **Score the shipped file.** The finisher applies the fixes, then both critics score the final Feed and Story JPGs. If a
   critic's change is applied, both critics re-score that ad once. The ledger's `scoredFile` names the final JPG and its
   `stat -c %y`. The b01-4 and b01-1 record fixes are pre-b03 items (§0).

## 3. Shared layout system for b03

- **Picture.** 9:16, 2K (1536 × 2752). `.pic` is object-fit cover, so it displays at 1080 × 1935.
  - Feed: `object-position: 50% P%`, T = 5.85 × P (0–585), Feed y = src_y × 0.703125 − T.
  - Story: native frame, Story y = src_y × 0.703125 − 7.5, x = src_x × 0.703125.
- **Feed card (fixed).** Top 940, centred on x 540. Measured stack: `logo_white` 56 (plus 6) · name Jost 500 26 .2em (line
  38) · price Cormorant 500 56 · line Jost 400 26 · offer one 26 px line (box 62 tall). Gaps 14. It ends at about 1252, or
  about 1200 with no line.
- **Offer text.** `Codes BUY2 · 10% off <span class="sep"></span> BUY3 · 20% off` (726 px), except b03-2:
  `Code NAIRA10 · 10% off` (449 px).
- **Type.** Bone on every ground, since all five are dark or mid-dark. Accent gold-light. Velista lines carry no digits, ₹,
  middle dots or dashes. Floor 26 px. At most four text elements per ad.
- **Story.** All text inside y 270–1250, ending at least 24 px above the subject's measured top. Every Story carries name and
  price on one baseline (24 px gap) and the offer. Where an ad has a Feed beat, the Story drops it first if space runs short.
- **Render gates.** `failed [] · overflow [] · fallback [] · outside []`, `minFont ≥ 26`, text share within each
  archetype's target, and the beat ratio of at least 0.6 logged.
- **Anchors for the blind 200 px sheets** (rotated; b01 used F2 and the Toggle Story, b02 the anaar and C01 Feed):
  - Feed sheet: winner `win_static_hoops_apricot` (a product-only gold pair, the like-for-like comparator) and loser
    `lose_p2_proof_parody`.
  - Story sheet: winner `win_w1_woven_red_story` (gold on an oxblood glaze, the exact note b03-1 replicates) and loser
    `lose_vks5_prism_close` (pale on pale, which tests rule 2).

## 4. The five ads

| Id | Product (stock · price) | Archetype | Light | Camera | Ground | Crazy | Feed extent band | Start P |
|---|---|---|---|---|---|---|---|---|
| b03-1 | Brushed Gold Huggies (58 · ₹699) | A4 Monument Macro (new move) | L1 | C2 | plum glaze | no | 424–930 (≤ 506) | 50 |
| b03-2 | Cushion Halo Ring (45 · ₹999) | A1 Product Card (macro, NAIRA10) | L7 | C5 | cocoa, tone on tone | no | 330–930 (≤ 600) | 62 |
| b03-3 | Halo Curve Ring (29 · ₹899) | A8 Callout Anatomy | L2 | C5 | deep sage | no | 384–804 (≤ 420) | 64 |
| b03-4 | Monochrome Enamel Hoops (24 · ₹999) | A13 Suspended (float) | L6 | C2 | terracotta | **yes** | 380–930 (≤ 550) | 53 |
| b03-5 | Pearl Double Halo Studs (25 · ₹1,199) | A6 Single Spotlight | L1 | C3 | ink | yes (A6) | 350–930 (≤ 580) | 56 |

- Archetypes: 5 different (A1, A4, A6, A8, A13).
- Lights: 4 (L1, L2, L6, L7), with L7 used once.
- Cameras: 3 (C2, C3, C5).
- Products: 5, one ad each.
- Type-led ads: 0. Anton: none.
- PLAYBOOK §5.2 roles: control (A4, A1), crazy (A13, plus A6), explainer (A8). The value role sits in the offer box and the ₹699
  beat this batch.

---

### b03-1 · Brushed Gold Huggies · A4 Monument Macro · L1 · C2 · the one new move

- **Concept.**
  - The ₹699 pair as a gold monument: two short brushed-satin barrels standing on a deep plum glaze, seen from almost floor
    level, the only gold in the frame.
  - The satin-sheen floor is the "polished" foil to the matte brushed metal.
  - The headline is the listing's own finish line, and the beat is the price.
  - This replicates b01-4's note (gold mass on a saturated plum ground) on a second product.
- **Borrows.**
  - Board 26 and 42: the piece as a monument on one saturated field, with two-line type.
  - Board 95: abstract crop plus a two-word claim.
  - Board 190: "shown magnified".
  - Our W1 "Woven, not cast" (gold on an oxblood glaze, texture-led, sold 5) and b01-4 (gold on plum, the candidate note).
  - The mechanism is the piece as the single loudest shape on one dark saturated field, with a craft truth in two beats.
- **Refs.**
  - Slot 1: `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f`, `build/refs/brushed-gold-huggies__pack.jpg`. "The authority on this exact
    piece; ignore its background and light."
  - Slot 2: `4c630657-80e8-47f5-ad65-1f0938c70900`, `build/refs/brushed-gold-huggies__macro.jpg`. "Take only the brushed-satin
    finish with its fine parallel brush lines."
- **Prompt.**
  > Vertical 9:16 product photograph, 100 mm macro lens, low hero camera about 8 degrees above the floor, front-on, so the floor reads as a narrow band and the two pieces rise from it like short gold-tone monuments: the pair of Brushed Gold Huggies from the reference stand upright on their edges side by side, about 2 mm apart, centred in the frame, the only gold-tone object in the picture; the left huggie shows its broad brushed front face to the camera, the right huggie is turned three-quarters so its round opening and the inside of its band show, as the pair is posed in the reference. FIDELITY: each is a chunky huggie about 14 mm tall by 9.8 mm, a wide flat band in soft brushed-satin 18k PVD gold tone covered in very fine parallel brush lines, a hidden hinge, zero stones; the two are identical. The finish must stay matte and light-scattering with one broad soft sheen, never mirror-polished, never ridged, hammered or stone-set, and each must stay a short chunky barrel, never a thin large hoop. SCALE: each huggie is about 1.4 times as tall as it is wide; each huggie's height is about one sixth of the frame's height and the pair together spans a little under half the frame's width; each stands on the glaze with a crisp, short, true contact shadow; honest macro depth of field with both pieces sharp. SCENE: a deep saturated plum (aubergine) ceramic glaze floor with a soft satin sheen sweeps up into a matching plum wall with no horizon line; there is no mirror reflection of the huggies in the floor and nothing else in the frame; everything above the pair is calm, evenly lit plum wall and everything below it is calm plain plum floor, and the pair stays well inside the central 4:5 window of the 9:16 frame. LIGHT, L1: one hard warm spotlight from the left at about the pieces' height rakes across both bands so the fine brush lines show as a satin grain, throwing crisp short shadows to the right on the glaze; plus one large soft fill from the front right that keeps the shaded sides readable. The gold tone stays warm-neutral, never orange or brassy, never grey or greenish. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no other jewellery, no props, no hands, no water or droplets, no reflections of the pieces.
- **Acceptance.**
  - **Extent (first).** The pair plus contact shadows is at most 506 Feed px tall, so some P puts it inside Feed y 424–930.
    Log extent, T and P.
  - **Pose.** Both upright and whole, the left face-on and the right three-quarters with its opening showing. Both sharp.
  - **Finish.** Brushed satin with fine parallel lines and one broad sheen, never mirror, ridged, hammered or stone-set. Zero
    stones, hidden hinge, an identical pair.
  - **Ratio inside the piece (log it).** Huggie height ÷ face width = 1.25–1.5 (the pack ref measures 1.37).
  - **Width share (log it: the new-move metric).** Each huggie 25–30% of the Feed width; the pair 58–70%. The pair is centred
    on x 540, the brush-line faces and the opening are inside x 216–864, and the outer edges are inside x 170–910.
  - **Scale.** Log px/mm on the 1080 Feed. Expect about 29–32 (about 2×), so the size tag is required.
  - **Colour.** Warm-neutral gold, never orange, grey or greenish. The plum behind the pair is darker and cooler than the
    gold (log the ΔE). The pair is the only gold.
  - **Floor.** No mirror reflection extending the extent, no water, no props.
  - **Calm zones.** Plain wall behind Feed y 84–400 (headline, beat and tag), and plain floor under the card.
  - **200 px gate.** On the blind sheet the pair is the first shape and reads as a pair of earrings (the opening helps).
  - **Negatives.** No star glints, no flare, no text.
- **Layout.**
  - **Feed** (`body.dark`). Text share ≤ .18 (A4).
    - `.pic` `object-position: 50% P%` (start P 50).
    - `.h1` "Brushed,<br>not polished." Velista 100, .02em, bone, left 72, top 96. Lines at 96–194 and 194–292, measured
      widths 460 and 709.
    - `.beat` "the ₹699 pair." Cormorant Garamond italic 500, 64 px (0.64× the headline), gold-light, left 72, top 304. Width
      319, ends about 369.
    - `.sizetag` "Shown magnified<br>about 14 mm tall" 30 px, bone, right 72, top 304. Box 379 × 96: x 629–1008, y 304–400.
      It must clear the pair by 24 px; if not, move it to top 84, right 72.
    - `.card` top 940: `logo_white`; "Brushed Gold Huggies"; "₹699"; line "soft brushed satin · 18k gold tone PVD" (435 px);
      the two-code offer. It ends at about 1252.
    - A linear scrim in the picture's own plum (0 at y 860 to .55 at 1350) only if the floor under the card is not calm.
    - Nothing over the pair. Log H1 100, beat 64, ratio .64.
  - **Story** (`body.dark story`).
    - `logo_white` 270–326.
    - `.h1` Velista 80, centred, 346–502 (368 / 567).
    - Name and price on one baseline, 522–578.
    - Offer 596–658.
    - Size tag on one line, "Shown magnified · about 14 mm tall", Jost 500 26 .12em hairline (650 × 62), 676–738.
    - All text ends at least 24 px above the pair's measured top. If it does not fit, move the size tag to 24 px below the
      pair (when that ends by 1250), then set the headline at 72.
    - The beat is Feed-only.
- **Copy.**
  - **Primary text** (157 characters; offer ends at 123): "Brushed, not polished: Brushed Gold Huggies, ₹699, about 14 mm,
    in brushed-satin 18k gold tone. BUY3: 20% off any 3 pieces. Waterproof and tarnish-free, too."
  - **Headline** (39): "Brushed Gold Huggies · ₹699 · 20% off 3"
  - **Description** (29): "Brushed satin · 18k gold tone"
  - **URL:** `https://www.nairaflore.com/products/brushed-gold-huggies?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b03&utm_content={{ad.id}}&utm_term=b03-1_a4_brushed-not-polished`

---

### b03-2 · Cushion Halo Ring · A1 Product Card (macro, no headline) · L7 · C5 · NAIRA10 offer cell

- **Concept.**
  - F2's grammar with anaar's scale, on the best-evidence hero (the Halo video sold 20).
  - The ring in its listing macro pose, the halo face-on and the pavé shoulders running out sideways, about 60% of the width,
    standing on a cocoa plaster block in a cocoa room, tone on tone.
  - No headline: the piece, the size tag and the card do the work.
  - The first on-image NAIRA10 offer, the one code that does not ask for a second piece.
- **Borrows.**
  - Our F2 (card only, no headline, cocoa ground, 4.74x) and anaar (one piece at about 60% of the width, the loudest thing in
    a quiet frame, no text).
  - Board 107 (a constant sign-off) and board 190 ("shown magnified").
  - The mechanism: one hero shape, the card as the only voice.
- **Refs.**
  - Slot 1: `94e89aaa-1d35-47ca-853e-da323cc0ac01`, `build/refs/cushion-halo-ring__upright.jpg`. "The authority on this exact
    piece; ignore its background and light."
  - Slot 2: `6b507080-6cf9-4452-83c1-6e5cabddcfa0`, `build/refs/cushion-halo-ring__macro.jpg`. "Take the face-on pose, the
    single-row cushion halo and the shoulder pavé from this one."
- **Prompt.**
  > Vertical 9:16 jewellery macro photograph, 100 mm macro lens at the height of the ring's head, tilted down about 10 degrees, front-on: the Cushion Halo Ring from the reference stands upright on the flat top of a matte cocoa-brown plaster block, its head facing the camera exactly as in the macro reference, the cushion halo seen face-on, the pavé shoulders running out to the left and right and the band curving away behind, centred in the frame. FIDELITY: one 8 mm round brilliant clear cubic zirconia held by exactly 4 claws, inside a single-row cushion-shaped (rounded-square) halo of tiny clear pavé about 12 mm across, one row of small pavé stones down each shoulder, a plain band with a small opening at the back hidden behind the head, all in cool PVD rhodium silver tone. The halo must stay one single row and cushion-shaped, never round and never two rows; the metal stays cool bright silver tone, never gold tone. SCALE: the centre stone is about three quarters of the halo's width, and the ring from shoulder tip to shoulder tip is about 1.7 times the halo's width; the halo's height is about one seventh of the frame's height and the ring spans a little under half the frame's width; the band rests on the plaster with a soft, true contact shadow; honest macro depth of field, the halo and claws tack sharp, the far shoulder tips softening slightly. SCENE: the block and the seamless backdrop behind it are the same deep cocoa brown, matte, tone on tone; the block's top edge runs straight across the frame just below the ring and its front face below is plain cocoa plaster; nothing else. Everything above the ring is calm, softly graded cocoa backdrop, everything below it is the plain front face of the block, and the ring stays well inside the central 4:5 window of the 9:16 frame. LIGHT, L7: one large soft warm window light from the upper left wraps the band and the halo and gives the cocoa a gentle falloff; plus one small hard specular kicker from the right so the cubic zirconia throws small crisp round points of white and faint rainbow colour, never rays. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no other jewellery, no ring box, no flowers or props, no hands, no water.
- **Acceptance.**
  - **Extent (first).** Ring plus contact shadow at most 600 Feed px, so some P puts it inside Feed y 330–930. Log extent, T
    and P.
  - **Construction.**
    - one round brilliant centre stone in exactly 4 claws;
    - one single-row cushion-shaped (rounded-square) halo, never round and never two rows;
    - one row of pavé down each shoulder;
    - cool bright silver tone, never gold.
  - **Pose.** The head face-on as in the macro ref, the shoulders running left and right.
  - **Ratios inside the piece (log them).** Centre stone ÷ halo width = 0.66–0.80 (macro ref 0.76). Shoulder span ÷ halo width
    = 1.5–1.9 (ref 1.69).
  - **Width share.** Shoulder span 52–66% of the Feed width (target 60%, the anaar share); the halo at least 30%. Halo and
    claws inside x 216–864.
  - **Scale.** Log px/mm. Expect about 28–34 (about 2×), so the size tag is required.
  - **Light.** A soft wrap and small round speculars with faint fire. No rays, no star glints.
  - **Ground.** Backdrop and block tone on tone in cocoa. Nothing more saturated than the ring's sparkle: no coloured
    pedestal, which was b01-1's fault. The block face under the card is plain.
  - **200 px gate.** The ring is the first and brightest shape and reads as a halo ring.
- **Layout.**
  - **Feed** (`body.dark`). A1, no headline. Text share ≤ .15 (A1).
    - `.pic` start P 62.
    - `.sizetag` "Shown magnified<br>halo about 12 mm" 30 px bone (382 × 96), right 72, its bottom edge 24 px above the
      ring's measured top. It must not overlap the ring.
    - `.card` top 940 on the plain block face: `logo_white`; "Cushion Halo Ring"; "₹999"; line "8 mm cubic zirconia · silver
      tone · adjustable" (519 px; "adjustable" is cleared by the Adjustable tag, RULINGS §2); `.offer` "Code NAIRA10 · 10% off"
      (449 px).
    - A scrim in the picture's own cocoa only if the block face is not calm.
  - **Story** (`body.dark story`).
    - `logo_white` 270–326.
    - Name 350–388.
    - Price 404–460.
    - Line 476–514.
    - Offer 532–594.
    - Size tag, two lines, 614–710.
    - The ring's top must be at or below 734. If it is higher, drop the line first, then set the tag on one 26 px line.
- **Copy.**
  - **Primary text** (158; offer ends at 124): "Proposal-style halo, ₹999: Cushion Halo Ring, 8 mm cubic zirconia,
    silver tone, adjustable. Code NAIRA10: 10% off any order. Waterproof and tarnish-free, too."
  - **Headline** (34): "Cushion Halo Ring · ₹999 · 10% off"
  - **Description** (24): "Code NAIRA10 · any order"
  - **URL:** `https://www.nairaflore.com/products/cushion-halo-ring?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b03&utm_content={{ad.id}}&utm_term=b03-2_a1_cushion-macro-naira10`

---

### b03-3 · Halo Curve Ring · A8 Callout Anatomy · L2 · C5

- **Concept.**
  - The toi-et-moi explains itself: a frame-filling ring on a deep sage field under a direct flash.
  - Three hairline callouts in listing words name the tiger eye, the champagne crystal and the open band (US 5 to 9, 4 g).
  - Halo Curve's first ad.
- **Borrows.**
  - Board 40 and 79: hairline leader callouts on a large product, with a two-line headline above.
  - Board 29, 183 and 186.
  - Board 57: proof beside the claim.
  - PLAYBOOK A8 copy.
  - The mechanism: the picture proves the headline part by part, every leader ending on the part it names. It corrects our
    A07 ruler, which lost on a small product.
- **Refs.**
  - Slot 1: `ac8bad23-c21e-447f-801c-3ec328d118f6`, `build/refs/halo-curve-ring__cube.jpg`. "The authority on this exact piece;
    ignore its background and light."
  - No slot 2. The only detail ref, `halo-curve-ring__close.jpg`, is a worn hand, and it would invite a hand into a
    product-only frame.
- **Prompt.**
  > Vertical 9:16 jewellery macro photograph, 100 mm macro lens, camera about 30 degrees above the surface in a three-quarter high view, as in the reference: the Halo Curve Ring from the reference stands upright on its open band on a flat matte deep sage-green surface that sweeps up into a matching sage wall with no horizon line, its two stones on top facing the camera at a slight angle, the tiger eye on the left and a little higher, the champagne crystal on the right and a little lower, the open loop of the band visible at the lower left, centred in the frame. FIDELITY: an open bypass ring of one smooth round 1.5 mm polished 18k PVD gold-tone wire, about 17 mm across inside, whose two ends pass each other and sit side by side, each holding one stone in a slim irregular gold-tone bezel: an opaque banded golden-brown tiger eye about 11.8 mm, a softly faceted cushion with a silky moving band of sheen, and a faceted transparent pale champagne crystal cushion a little smaller. Exactly two stones and they must stay unmatched, one opaque banded brown and one clear pale champagne, never two matching cushions, never a transparent or glassy tiger eye, never a halo of small stones, never a thick or flat band; the band stays open between the two ends. SCALE: the tiger eye is about eight times as wide as the wire is thick and about a third of the ring's full width; the ring is about 1.3 times as wide as it is tall; the ring's height is about one seventh of the frame's height and it spans a little over a third of the frame's width; it stands on the surface with a crisp, true contact shadow under the band; honest macro depth of field, both stones sharp. SCENE: a plain matte deep sage-green (grey-green) seamless and nothing else; everything above the ring is calm empty wall and everything below it is calm empty floor, and the ring stays well inside the central 4:5 window of the 9:16 frame. LIGHT, L2: one direct on-camera flash, hard and frontal, gives the gold-tone wire a crisp bright edge, wakes the tiger eye's silky band and throws a short hard drop shadow of the ring onto the sage surface just behind it; plus one large soft overhead fill so the shaded part of the band and the crystal's facets keep their detail. The gold tone stays warm-neutral, never orange or brassy. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no other jewellery, no props, no hands, no water.
- **Acceptance.**
  - **Extent (first).** Ring plus its shadow at most 420 Feed px, so some P puts it inside Feed y 384–804. Log extent, T and P.
  - **Construction.**
    - one smooth round gold-tone wire, an open bypass with the band open between the ends;
    - exactly two unmatched stones in slim irregular bezels: an opaque banded golden-brown tiger eye with a silky band of
      sheen, and a faceted transparent pale champagne crystal;
    - no halo, no extra stones, never matching cushions, never a transparent tiger eye, never a thick band.
  - **Ratios inside the piece (log them).** Tiger eye width ÷ wire thickness = 7–10 (cube ref about 9). Tiger eye ÷ ring width
    = 0.30–0.42 (ref 0.36). Ring width ÷ height = 1.15–1.45 (ref 1.29).
  - **Width share.** The ring is 46–56% of the Feed width, centred, both stones inside x 216–864.
  - **Scale.** Log px/mm. Expect about 24–26 (about 1.5×), so the "Shown magnified" tag is required.
  - **Colour.** Warm-neutral gold. The deep sage is cooler than the gold. The tiger eye stays golden-brown, not black.
  - **Callout points.** Three leader ends can sit on metal (the tiger eye's bezel rim, the crystal's bezel rim, the band wire
    at the open loop) without any leader crossing a stone. If the stones land mirrored, the finisher swaps C1 and C2 sides.
  - **Light.** A short hard drop shadow, no rays, no star glints.
  - **Calm zones.** Plain sage above (Feed 84–372) and below (Feed 820–1260).
  - **200 px gate.** It reads as a two-stone ring.
- **Layout.**
  - **Feed** (`body.dark`, bone on deep sage). Text share ≤ .20 (A8).
    - `.pic` start P 64.
    - `.h1` "Two stones.<br>One open band." Velista 84 .02em, bone, centred, top 96. Lines 96–178 and 178–260, widths 541 / 658.
    - **Callouts** (`.callout`: `b` Jost 500 26 caps .1em over `span` Jost 400 26, two lines, 76 px):
      - C1 "Tiger eye" / "about 11.8 mm" at left 72, top 284.
      - C2 "Champagne crystal" / "faceted, pale champagne", right-aligned to 1008, top 284 (320 px wide).
      - C3 "Open band" / "adjusts US 5 to 9 · about 4 g" at left 72, top 828 (317 px wide).
    - **Leaders.** Inline `svg.overlay`: 2 px bone lines ending in 10 px open circles on metal only. C1 ends on the tiger eye's
      bezel rim, C2 on the crystal's bezel rim, C3 on the band wire at the open loop. Never on or across a stone.
    - `.sizetag` on one line, "Shown magnified", 30 px (379 × 62), right 72, top 828.
    - `.card` top 940 with **no line** (the callouts carry the truths): `logo_white`; "Halo Curve Ring"; "₹899"; the two-code
      offer. It ends at about 1200.
    - Four text elements: the headline, the callout set, the size tag and the card.
  - **Story** (`body.dark story`).
    - `logo_white` 270–326.
    - `.h1` Velista 76, centred, 346–494 (490 / 595).
    - Name and price on one line, 514–570.
    - Offer 588–650.
    - Size tag on one line, "Shown magnified", 26 px (333 × 62), 668–730.
    - The callouts are Feed-only. The ring's top must be at or below 754; if not, drop the tag to 24 px below the ring.
- **Copy.**
  - **Primary text** (158; offer ends at 123): "Two stones, one open band: Halo Curve Ring, ₹899, tiger eye and champagne
    crystal in 18k gold tone. BUY2: 10% off 2 pieces. Adjusts US 5 to 9, and waterproof."
  - **Headline** (34): "Halo Curve Ring · ₹899 · 10% off 2"
  - **Description** (29): "Tiger eye · champagne crystal"
  - **URL:** `https://www.nairaflore.com/products/halo-curve-ring?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b03&utm_content={{ad.id}}&utm_term=b03-3_a8_halocurve-two-stones`
  - Banned for this SKU: "halo" as a description (the piece has none; only the product name), "solid gold", and calling
    the crystal cubic zirconia.

---

### b03-4 · Monochrome Enamel Hoops · A13 Suspended (float) · L6 · C2 · the crazy slot

- **Concept.**
  - The graphic pair floats over a terracotta field, each hoop with its own detached C-shaped shadow on the floor: the honest
    surprise.
  - The headline names exactly what the eye sees (black, white, gold tone), and the beat gives the listing's own styling
    line.
  - Monochrome's first ad, with no claim and no water.
- **Borrows.**
  - Board 96: levitation with a detached soft shadow, two-weight type.
  - Board 26 and 42: one flat saturated field.
  - Board 1: the piece lifted above its ground.
  - b02-2's float, which the model rendered twice.
  - PLAYBOOK A13 copy for Monochrome. The mechanism: impossible-but-honest physics at true size, read in half a second.
- **Refs.**
  - Slot 1: `970635a3-fe88-4ac1-bdf9-a62c7554a87e`, `build/refs/monochrome-enamel-hoops__pack.jpg`. "The authority on this
    exact piece; ignore its background and light."
  - Slot 2: `2ee2cf91-322a-4c28-819c-94b7b7c9989d`, `build/refs/monochrome-enamel-hoops__detail.jpg`. "Take only the stripe
    order and widths, the three fine gold rails and the open C."
- **Prompt.**
  > Vertical 9:16 product photograph, 100 mm lens, low hero camera about 12 degrees above the floor: the pair of Monochrome Enamel Hoops from the reference hover side by side in mid-air above a flat matte terracotta floor that sweeps up into a terracotta wall with no horizon line, both upright and turned three-quarters to the camera exactly as in the reference, the black-and-white striped front face toward the camera, the open side of the C toward the right and the short post at the top, about one hoop-width apart, centred in the frame. FIDELITY: each is a chunky C-shaped post hoop about 20 mm tall and 7 mm wide in polished gold tone; its curved front face carries exactly one black enamel stripe and one white enamel stripe side by side, separated and edged by three fine polished gold-tone rails; the inside of the C is plain polished gold tone; zero stones; the two are identical. They must stay exactly one black and one white stripe per hoop, never more stripes, never alternating bands or stones, and each must stay an open C, never a closed circle. SCALE: each hoop is about 1.65 times as tall as it is wide and the pair together is about 1.5 times as wide as it is tall; each hoop's height is about one ninth of the frame's height and the pair spans about a third of the frame's width; directly below each hoop on the floor lies its own soft-edged shadow of the same C shape, separated from the hoop by a clear gap of empty floor about half a hoop tall, so the pair visibly floats; honest depth of field, both hoops sharp. SCENE: a saturated matte terracotta (burnt orange-red) seamless and nothing else; everything above the hoops is calm empty wall and everything below their shadows is calm empty floor, and the hoops and their shadows stay well inside the central 4:5 window of the 9:16 frame. LIGHT, L6: one large soft light directly overhead casts each hoop's shadow straight down onto the floor and lays a smooth glossy highlight along the enamel's curve; plus one small hard kicker from the front left that draws a crisp bright line on each gold-tone rail. The gold tone stays warm-neutral, never orange or brassy; the white enamel stays clean white and the black stays deep black. NEGATIVES: no text, no logos, no strings, wires, stands, pins or supports of any kind, no hands, no star-shaped glints, no starburst, no lens flare, no other jewellery, no props, no water.
- **Acceptance.**
  - **Extent (first).** Hoops plus shadows at most 550 Feed px, so some P puts them inside Feed y 380–930. Log extent, T and P.
  - **Float.** A clear gap of floor between each hoop and its own shadow, at least 0.4× the hoop height. The shadows sit
    directly below and match the C shape. No wire, stand or support of any kind.
  - **Construction.** Per hoop:
    - exactly one black and one white enamel stripe between three fine gold rails;
    - an open C, never a closed circle;
    - plain polished gold inside, a post at the top, zero stones.

    The pair is identical, in the three-quarter pose with the stripes to the camera.
  - **Ratios inside the piece (log them).** Hoop height ÷ width = 1.45–1.85 (pack ref 1.65). Black ÷ white stripe width =
    0.8–1.25.
  - **Width share.** The pair is 40–52% of the Feed width, each hoop at least 18%, centred on x 540.
  - **Scale.** Log px/mm. Expect about 14–17 (life size); add a size tag only above 19.
  - **Colour.**
    - The gold stays warm-neutral, not orange on the terracotta.
    - The white is clean and the black deep.
    - The terracotta is darker than the gold (log the ΔE). It is not a same-hue ground: the field is red-orange and darker,
      the gold yellow and lighter.
  - **Calm zones.** Plain wall above (Feed 84–360), plain floor under the card.
  - **200 px gate.** Two floating earrings land first, and the float reads in half a second.
- **Layout.**
  - **Feed** (`body.dark`, bone on terracotta, about 5:1). Text share ≤ .18 (A13).
    - `.pic` start P 53.
    - `.h1` "Black. White.<br>Gold tone." Velista 92 .02em, bone, centred, top 96. Lines 96–186 and 186–276, widths 616 / 513.
    - `.beat` "for the white shirt, or all in black." Cormorant italic 500, 56 px (0.61×), gold-light, centred, top 290.
      Width 673, ends about 347.
    - No size tag unless measured above 19 px/mm.
    - `.card` top 940: `logo_white`; "Monochrome Enamel Hoops" (523 px); "₹999"; line "black and white enamel · gold tone" (405
      px); the two-code offer.
    - No scrim on the flat field unless needed.
  - **Story** (`body.dark story`).
    - `logo_white` 270–326.
    - `.h1` Velista 80, centred, 346–502 (536 / 446).
    - Name and price on one line, 522–578 (657 px wide).
    - Offer 596–658.
    - The top of the hoops-plus-shadows extent must be at or below 682. The beat is Feed-only.
- **Copy** (no claim, no water).
  - **Primary text** (160; offer ends at 125): "Black, white, gold tone: Monochrome Enamel Hoops, ₹999, one black and one
    white enamel stripe a hoop. BUY2: 10% off 2 pieces. For the white shirt, or all black."
  - **Headline** (35): "Monochrome Hoops · ₹999 · 10% off 2"
  - **Description** (22): "Black and white enamel"
  - **URL:** `https://www.nairaflore.com/products/monochrome-enamel-hoops?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b03&utm_content={{ad.id}}&utm_term=b03-4_a13_monochrome-float`
  - Banned for this SKU: PVD, steel, 18k, waterproof, tarnish-free, hypoallergenic.

---

### b03-5 · Pearl Double Halo Studs · A6 Single Spotlight · L1 · C3

- **Concept.**
  - Two studs on a dark riser in an almost black room, lit by one hard spot. The pool of light is the only lit thing; the
    two white pearls and their double pavé bands glow.
  - The headline names the construction (two bands) and the scene (one light). The beat sets the moment: the sangeet, after
    dark.
  - Pearl Double Halo's first ad, with no claim and no water.
- **Borrows.**
  - Board 3: one spotlight, the product the only lit object, a staggered two-line headline, "Spray it in the evening".
  - Board 166, 116 and 100.
  - Our b01-1 (A6 shipped at 7.45). Its smeared beam is fixed by describing only the pool of light.
  - The mechanism: one light, one hero, the occasion as the second beat.
- **Refs.**
  - Slot 1: `82a6fb43-78f4-40b7-a2f0-ae30d4da0fd2`, `build/refs/pearl-double-halo-studs__pack.jpg`. "The authority on this
    exact piece; ignore its background and light."
  - Slot 2: `08ee5809-9c82-443b-be16-6bedda5e5482`, `build/refs/pearl-double-halo-studs__detail.jpg`. "Take only the two
    separate pavé bands, the open gap with its tiny bridges, and the pearl's lustre."
- **Prompt.**
  > Vertical 9:16 product photograph, normal-perspective close-up lens at eye level, a little above the pieces, front-on: the pair of Pearl Double Halo Studs from the reference stand upright side by side on the top of a low round matte charcoal riser, faces toward the camera exactly as in the reference, about a quarter of a stud apart, centred in the frame, in an almost black room. FIDELITY: each stud is about 17.5 mm across in bright silver tone: one round white pearl about 10 mm at the centre, ringed by an inner round band of fine clear pavé, then a narrow open gap crossed by a few tiny metal bridges, then an outer softened-square band of fine clear pavé; the two are identical. Each must keep two separate pavé bands with the open gap between them, never one single halo and never a closed or filled gap; the outer band stays a softened square, never a circle; the metal stays bright silver tone, never gold tone or grey; the pearl stays a smooth round white sphere with a soft pink-white lustre. SCALE: the pearl is about half the width of the outer band; each stud's height is about one eighth of the frame's height and the pair spans a little under half the frame's width; each stud stands on the riser with a crisp, true contact shadow. SCENE: the riser and the room are the same near-black ink tone; only the riser's top and the studs are lit; nothing else. Everything above the studs is calm near-black, the riser's dark front face below them is calm, and the studs stay well inside the central 4:5 window of the 9:16 frame. LIGHT, L1: one hard spotlight from high behind and to the right lands as a crisp-edged circular pool of light on the riser's top around the studs, rims both pavé bands and throws two soft-edged shadows of the studs forward toward the camera across the riser; the rest of the frame falls away to near black; plus one soft low fill from the front so the pearls keep their full round lustre and the pavé its detail. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no visible light beam, no haze or smoke, no other jewellery, no props, no hands, no water.
- **Acceptance.**
  - **Extent (first).** The studs plus their shadows on the riser top (not the riser itself) are at most 580 Feed px, so some
    P puts them inside Feed y 350–930. Log extent, T and P.
  - **Construction, per stud.**
    - one round white pearl at the centre;
    - an inner round band of clear pavé;
    - a narrow open gap with a few small bridges;
    - an outer softened-square band of clear pavé;
    - bright silver tone, never gold.

    The pair is identical, faces to the camera.
  - **Ratios inside the piece (log them).** Pearl ÷ outer band width = 0.45–0.60 (pack ref 0.48, detail ref 0.57). Inner
    band's outer edge ÷ outer band = 0.70–0.82.
  - **Width share.** The pair is 52–66% of the Feed width, centred, both pearls inside x 216–864.
  - **Scale.** Log px/mm. Expect about 15–18 (about life size); add a size tag only above 19.
  - **Light.**
    - A crisp pool of light on the riser around the studs, the frame 70–90% near-black.
    - No beam, haze, rays or star glints.
    - The pearls keep a round lustre, the silver stays bright and not grey, and the blacks do not swallow the metal.
  - **Riser.** No lighter or more saturated than the studs.
  - **Calm zones.** Near-black above (Feed 84–330, the headline stagger), the dark riser face or floor under the card.
  - **200 px gate.** Two white pearls in silver bands are the first shape and read as stud earrings.
- **Layout.**
  - **Feed** (`body.dark`). Text share ≤ .14 (A6).
    - `.pic` start P 56.
    - `.h1` staggered, Velista 76, letter-spacing .12em, gold-light: "Two bands." at left 72, top 110 (525 px), and "One
      light." at left 236, top 188 (464 px, x 236–700).
    - `.beat` "for the sangeet, after dark." Cormorant italic 500, 48 px (0.63×), bone, left 236, top 276. Width 448, ends
      about 325.
    - `.card` top 940: `logo_white`; "Pearl Double Halo Studs" (466 px); "₹1,199"; line "silver tone · cubic zirconia" (305
      px; RULINGS §3: "pearl" only inside the product name); the two-code offer.
    - A size tag only if measured above 19 px/mm: "Shown magnified / about 17.5 mm across", right 72, top 110.
  - **Story** (`body.dark story`). The A6 no-text twin is not used: b01-1 already holds that control.
    - `logo_white` 270–326.
    - Staggered `.h1` Velista 72 .12em gold-light: line 1 at left 150, top 346 (497 px); line 2 at left 300, top 419 (440 px).
    - Beat 44 (0.61×) bone, left 300, top 506 (411 px).
    - Name and price on one line, 571–627 (about 640 px).
    - Offer 645–707.
    - The studs' top must be at or below 731. If it is higher, drop the beat first.
- **Copy** (no claim, no water; "pearl" only inside the product name).
  - **Primary text** (157; offer ends at 123): "Two pavé bands, one light: Pearl Double Halo Studs, ₹1,199, bright silver
    tone with cubic zirconia. BUY2: 10% off 2 pieces. Made for the sangeet, after dark."
  - **Headline** (38): "Pearl Double Halo · ₹1,199 · 10% off 2"
  - **Description** (28): "Silver tone · cubic zirconia"
  - **URL:** `https://www.nairaflore.com/products/pearl-double-halo-studs?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b03&utm_content={{ad.id}}&utm_term=b03-5_a6_pearl-two-bands`
  - Banned for this SKU: PVD, rhodium, steel, 18k, shell, freshwater, any claim.

---

## 5. Notes for the next steps

- **Generator.**
  - Re-read the balance first, then make one `generate_image_batch` call with the five first tries: `nano_banana_pro`, 2K, 9:16,
    one image per slot, refs in slot order (b03-3 has slot 1 only).
  - Log `submitted_at`, `credits` and `served_model` from `transactions` in `jobs.json`. The model served has been
    `nano_banana_2` every time, so judge every output by eye.
  - On a 429, resubmit only the failed item, after the first job completes.
  - At most 4 regenerations (§0). Each carries its fix in the prompt; for size, ask about 0.7× of the last try's measured share.
- **Verifier.** In this order:
  1. Measure each subject's full extent and the P that fits its band. A position miss alone is never a drop.
  2. The construction checks and the logged ratios in each acceptance list.
  3. The width share, px/mm, and the ΔE of the piece against the ground behind it.
  4. The 200 px gate: build a sheet of the five raw pictures at 200 px and drop any frame where something other than the
     piece lands first.

  Also log the light that rendered, not the one asked. For b03-1, log each huggie's width share.
- **Finisher.**
  - Kit classes only.
  - Sample scrims from each picture's own ground, never a token.
  - Each `copy.json` `layout` logs H1 px, beat px and the ratio.
  - `CODES` on two-code boxes, `CODE` on NAIRA10.
  - Every render passes the §3 gates.
- **Critics.**
  - Score the final JPGs, at full size and at 200 px, with the anchors in §3.
  - For b03-1, state whether it beats `win_static_hoops_apricot` (Feed) and `win_w1_woven_red_story` (Story) with each
    critic. The note "gold-tone mass on a saturated dark ground" is **promoted** only on a win over the winner anchor with
    both critics; otherwise **retired** (loop change 3).
- **b03 is better than b02 only if:**
  - it ships at least 3 of 5;
  - stop power (mean over shipped ads) is above 7.00;
  - one honest surprise ships (b03-4 or b03-5);
  - both critics name each shipped product in half a second on the blind sheet;
  - at least one ad beats the winner anchor with at least one critic.

## 6. Rotation and what is queued for b04

| Product | Briefed so far (ledger + b03) | Shipped | Next |
|---|---|---|---|
| Cushion Halo | b01-1, b03-2 | b01-1 | b04: a second archetype if b03-2 ships |
| Brushed | b01-2, b02-2, b03-1 (+ b02-2 try 2 layout) | – | Depends on the new-move read and the b02-2 rescue |
| Verdant Eternity | b01-3, b02-5 (+ b02-5 try 1 layout) | – | b04 hero slot in its upright reference pose (A3 or A10 with Cushion) |
| Woven | b01-4 (held), b02-1 | b02-1 | Capped |
| Prism, Verdant Circlet | 2 and 1 | – | Product-only only when they return |
| Halo Curve, Monochrome, Pearl Double Halo | b03 (first time) | – | – |
| **Serpentine Silver** | never | – | **b04.** A7 needs its own Story solution: the chain on the centre axis blocks a centred Story card, and the flanking words cap the pendant near 33% of the width. Alternatives: an A4 S-curve top-down, or A6. |
| **Ribbon Bead** | never | – | **b04:** an A10 set with Brushed (both ₹699, BUY2), or A3 |
| Toggle | never | – | Only with the clasp lock from RULINGS §3 in the prompt |
| Serpentine gold, Bold Nocturne | never | – | Held at exactly 20 units |

**Why no worn frame this batch.** The one worn geometry that has passed (camera behind the head) works only for a piece
hanging at least 22 mm below the lobe. Of those, Woven is capped and Bold Nocturne has no headroom. Hand crops for rings
failed scale in b01 and b02. Desire is the dimension most at risk in an all-product batch. Each frame earns it through light
and material instead: L7 warm window on cocoa, an evening spotlight with a sangeet beat, a styling beat for Monochrome, glaze
and plaster surfaces. If desire falls below 6.75, b04's fix target is a worn hanging piece.
