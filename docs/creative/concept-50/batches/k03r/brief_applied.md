# k03r · brief applied (camp k03 BEST OF THREE., rescue of cards 1, 2, 3 and 5)

Take A for each card is the card's planned `prompt` in `crazy100.json`, with these edits written in:

- the four points of `batches/k03r/brief_diff.md`;
- every redo-fix clause in `batches/k03a/verify/k03-N.md`, together with the "what next" lessons from each log's redo section, because those say which fix clauses failed on take R;
- `build/learnings.md` (wave 1 lessons 1-7 and wave 2 lessons 8-15).

The camp idea and the copy stay as the bible has them: the milk paraat, the mehendi hands, the ring-finding game, every headline and every device. The prompts are in `prompts.json`. Lint is clean on all six (see the last section).

Sources read:

- `crazy100.json`: camp k03 (idea, textual graphic, brand features, palette, sell lever, changes) and ads 1, 2, 3 and 5;
- `CRAZY100.md`: §6 k03, §9 and the owner rulings;
- `build/learnings.md` and `batches/bakeoff/README.md`;
- the k03a logs `verify/k03-1.md`, `k03-2.md`, `k03-3.md` and `k03-5.md` (take and redo sections);
- the k03a `prompts.json`, `jobs_redo.json` and `brief_applied.md`;
- the four product cards;
- the wave-2 logs for the same pieces on the new models: `k04r/verify/k04-3.md`, `k08a/verify/k08-4.md` and `k09a/verify/k09-3.md` (Verdant), and `k01r/verify/k01-1.md`, `k04r/verify/k04-1.md` and `k07a/verify/k07-5.md` (Woven).

**`batches/k03a/loop.md` does not exist,** so there was nothing to apply from it.

## Models and references

- **Take A:** `gpt_image_2_6`, quality medium, 2k, 9:16, use_unlim false. None of the four product cards has a `shootModel` field.
- **Take B:** `seedream_v5_pro`, 2k, 9:16, use_unlim false.
- **References** come from the product card's `mediaIds`, with reference 1 first.
- **Reference 3** is the card's `scaleRef`, where one exists, and the prompt says what it is, in the words of `scaleRef.use`:
  - Verdant: `6286cc23…`, `refs/verdant-eternity-band/02_scale_crop.jpg`, the index-finger worn crop.
  - Woven: `ea0201cf…`, `refs/woven-gold-hoops/05_ear_crop.jpg`, the ear crop.
- Droplet and Mint Pear have no `scaleRef`.

## Take B: two cards, k03-3 and k03-5

**Why these two.** The cards' `risk` fields and the past verification lessons pick them as the hardest for the image model.

**k03-3 Droplet Open Ring** (the plan's own hedge card):
- Two hands must not touch, and the ring's teardrop invites symmetry.
- On k03a, take A held construction but was letterboxed and framed at 34 cm. Redo R then split the ring across two fingers and turned the teardrop into a free spike: one product read as two rings. R was also 1.5-1.6x.
- There is no new-model evidence for this piece.

**k03-5 Mint Pear Drop Earrings:**
- An 8-stone sweep with a named morph: take A came out as a straight column of 2 clear pears.
- Scale drifted 2.1-2.3x on take A and about 3x on take R.
- There is no new-model evidence for this piece.

**Not taken:**
- **k03-1 Verdant.** The same ring has now passed construction and scale on the new models three times: k04r k04-3 (1.1-1.25x in a hand), k08-4 and k09-3.
- **k03-2 Woven.** On gpt_image_2_6 the construction holds in every pose (k01-1, k04-1, k05-5, k07-5, k09-5). Its one live fault is a marginal 1.35x in hands, which seedream repeated in k04r R. A second model would not hedge it.

**Not taken: the bible's composite hedges.** The hard rules forbid compositing.

**k03-3B (same idea, the hedge is the ring and the hand):**
- Her hand copies reference 2's own worn pose: the back of the hand, fingers relaxed, the ring on the middle finger just below the knuckle, the ball on the index side and the teardrop on the ring-finger side.
- It droops like the resting hand of the ceiling fresco, its index finger reaching toward his. The two fingertips stop about 1 cm apart over the milk.
- Leaving the reference pose is what split the ring on R. This take borrows the only listing photo that shows the ring on a hand at true size (18 cm frame).

**k03-5B (same idea, the hedge is scale):**
- This is the tightest crop: only her index and middle fingertips (the last two segments, from the left edge) in a frame about 6 cm wide.
- The pair rests on the two pads exactly as on the block in reference 1, and each earring is one third of the frame width.
- The model's preferred legible size is then the true size. That is the scale tactic the k03-5 redo log asks for.
- Everything else is take A's: the sweep, the count, the petal shower, the milk threads and the oxblood.

## Edits applied to all four take A prompts

| # | Source | Edit |
|---|---|---|
| G1 | diff 4, learning 5, k03-3 fix 2 | Full bleed: "a full-bleed photograph edge to edge with no borders, bands or panels: one continuous photograph fills the whole tall frame from the top edge to the bottom edge, never a square picture padded with flat colour, no frame within the frame, no split or collage". |
| G2 | shooter spec | The reference sentence is now exact, with the card's own note on reference 2 after it. |
| G3 | diff 1-3, learnings 2 and 10 | **Scale:** two body referents touching the piece (finger width and fingernail, or finger width and the open centre of the hoop), the field of view in cm, and a sentence naming last time's mis-scale ("never again"). That sentence is the k04r k04-3 wording, which held on gpt_image_2_6. |
| G4 | learning 9, diff 3 | Counts are written in digits and words: 1 disc (never 2); 3 petals; 3 + 1 stones per earring, 8 in the pair. |
| G5 | learning 6 | Every part is named in one metal tone (band, claws and tips; wire, disc, hinge and latch; claws, posts and backs). |
| G6 | shooter spec | "two lights only": one soft key and one small hard specular kicker. |
| G7 | shooter spec | "no face, no eyes, no eyebrows, no head" and "No text, no letters, no numbers, no logos, no watermark anywhere", kept from k03a. |
| G8 | shooter spec | "One product only: this one ring / pair is the only jewellery in the frame". |
| G9 | product cards | Each lock is pasted verbatim from the product card, including its "Must stay … never …" clause. |
| G10 | Verdant morph note | The word "eternity" is kept out of the Verdant prompt. |

## k03-1A Verdant Eternity Band (gpt_image_2_6 medium, 3 refs)

The base is the planned prompt. The k03a redo fixes 1-8 are applied as k03-1R wrote them, then changed as below.

| # | Source | was (plan) → now |
|---|---|---|
| 1 | fix 1 (redo) | The hold "burst straight up … holds the ring upright between the tips of her thumb and index finger, front of the ring facing the camera" becomes the forearm rising straight up out of the milk, palm to camera, the ring pinched only at the lowest point of its band, standing in reference 1's three-quarter pose with both looped tips visible and the other fingers curled. It adds "the ring is held, never worn on a finger". The ring's centre is set at about 40% down (Story 700-880 in the plan). |
| 2 | fix 2 + diff 1 + R "what next" | The scale clause "a little wider than the fingertip pad that grips it; field of view about 12cm" becomes: "outside height only a little more than the width of her index finger (about 17mm) and about one and a half times the width of her index fingernail (about 12mm); its opening exactly as wide as her index finger and narrower than her thumb; each green oval about a third as wide as her fingernail". The frame is about 11 cm wide and 20 cm tall, the palm spans about three quarters of the frame width, the frame edges come close to the sides of her hand, and the ring is one sixth of the frame width. "Three times before … two to four and a half times too big … never again." The R log's "make the crop concrete" is written as the palm filling most of the width. |
| 3 | fix 3 | The milk sentence becomes a coronet of loose beads, sheets and arcs around the wrist in the lowest fifth: never a smooth collar or cuff, never above the knuckles, and no bead on the ring. |
| 4 | fix 4 + R "what next" + k09-3 wave wording | THE WAVE: "ONE slim line, two rows of distinct round clear stones like reference 1, that snakes from oval to oval: it cups one side of an oval, crosses … and cups that one on the opposite side … never a broad sugared or frosted band, never a frame, loop or halo round any oval". Added: "each green oval faceted and glassy like reference 1 … never a matte glittery grain"; "4 short claws, never a row of tall spikes". |
| 5 | fix 5 | "The rhodium stays a cool bright white silver tone; the warm key never tints the metal or the claws champagne or gold tone." |
| 6 | fix 6 | Calm areas: oxblood in the top 30% and above and left of the ring, for the call and the size-gun arc. Exactly three petals (3, never four; R had four) sit in the upper half right of centre, clear of the call. The 50-78% band holds only the palm, wrist and oxblood, for the card. No petals or fairy lights below the middle. |
| 7 | fix 7 | Dropped: "palm up and flat", "fingers together", "held up like a trophy", "spans a sixth of the frame width". |
| 8 | fix 8 | Kept: the full lock, the reference sentence, the shamiana and fairy lights, the two lights, the contact shadow and the no-face, no-text and one-piece clauses. |
| 9 | k03-1B lesson (POSE) | "POSE, the most important instruction": the ref-1 three-quarter pose, never a new angle. |
| 10 | scaleRef | Reference 3 is the worn crop, with the card's `scaleRef.use` sentence plus "never that hand's pose, nails or background". |

## k03-2A Woven Gold Hoops (gpt_image_2_6 medium, 3 refs)

The base is the planned prompt. The k03a redo fixes 1-6 are applied as k03-2R wrote them, then changed as below.

| # | Source | was (plan) → now |
|---|---|---|
| 1 | fix 1 + diff 2 + learning 1 | The DISC clause: exactly one flat round mirror disc per hoop (1, never 2), about a third of the hoop's width, face up on the front of the braid at the top on the latch side, exactly as in reference 2; the other end is a hinge knuckle with no disc. Added from the R log: "a round coin … never turned edge-on into a thin tab". |
| 2 | k07-5 lesson | "Nothing hangs from the hinge: no added loop, jump ring or hanger anywhere." |
| 3 | fix 2 + diff 2 | THE BRAID IS OPEN: fat polished round wires laid in pairs, in loose raised chevron loops, over a see-through core of finer wires with dark gaps; milk or skin shows through; no granular, frosted, glitter or mesh fill. Added from R: "never … a tight three-strand plait". |
| 4 | fix 3 + learning 6 | Colour: "warm pale yellow, never orange or brassy" becomes "a bright, pale, warm lemon-yellow 18k gold tone with near-white highlights on every wire, the disc, the hinge and the latch; never orange, copper, amber or brassy, and no warm cast from the skin". |
| 5 | fix 4 + diff 2 + k04r lesson | SCALE: "these are small everyday 25 mm hoops and they must look small on her hand"; 16 cm field; an adult hand 17 cm long and 8 cm across; two referents ("about one and a half of her fingers wide, never two; its braid about half as wide as one of her fingernails; the open centre a little narrower than one of her fingers"); the pair narrower than her palm, with skin on every side; "1.4 times too big on a small, child-sized hand … never again". The placement becomes: across the middle segments of her four fingers, each hoop about one and a half fingers, fingertips no higher than 30%, hoops at about 45%, hinge top left and disc top right. |
| 6 | fix 5 | The rim crosses only the top-right corner as a near-straight arc of a platter nearly three times the frame's width. The ripples are crisp, circular, centred on her palm and the hoops, and visible at thumbnail size (the RIPPLE TEXT device traces them). |
| 7 | fix 6 + R note | Exactly three petals (3; R had four), in the middle band. The top third holds no petal and no fingertip; the bottom quarter is calm milk. |
| 8 | scaleRef (learning 12) | Reference 3 is the ear crop, with the card's `scaleRef.use` sentence. |
| 9 | R log "what next" | **Not applied** in take A: "tilt the camera to the reference's angle". The camp idea is the wire cam straight down, and the diff keeps the idea. That advice was given for nano_banana_2. gpt_image_2_6 has since drawn this hoop's disc and open core right in five other poses. |

## k03-3A Droplet Open Ring (gpt_image_2_6 medium, 2 refs)

The base is the planned prompt. The k03a redo fixes are applied, with the R log's "what next" corrections.

| # | Source | was (plan) → now |
|---|---|---|
| 1 | fix 1 | "the subject centred inside the central 4:5 window" becomes "the two fingertips meeting at the horizontal centre of the frame at 45 percent of the frame height". |
| 2 | fix 2 | The quarter-calm sentence (it caused take A's letterbox) becomes FRAME AND CALM AREAS: one continuous photograph; velvet in soft folds with real texture to the top edge (headline); the milk surface and brass rim to the bottom edge, leaving at the lower corners (card). |
| 3 | fix 3, corrected by R "what next" 2 and 5 | "SCALE: field of view about 11cm" becomes "true size, the frame about 20 cm wide at the hands". The R log blamed "large and clearly legible" and "can never read as two matching balls" for the split and the spike, so both are **dropped**. The 17 cm frame is widened to 20 cm, inside the log's 20-24 cm. A's 34 cm made the ring a glint. |
| 4 | diff 1 | Two body referents on her index finger: both ends together (13.5 mm) a little narrower than that finger (16 mm); each end about half her fingernail's width, the size of a green pea. "Before … half again too big, with its two ends pulled apart onto two fingers: never again." |
| 5 | R "what next" 3 | ONE FINGER, ONE RING: "both ends sit on top of the same one index finger, side by side, under 1 mm apart; the wire swells into the teardrop's narrow tail, which flows down the side of that finger into the band … only the teardrop's fat rounded end is free … never one end per finger, never two rings, never a free pointed tail or spike". |
| 6 | R "what next" 4 | The index fingers point level toward each other across the frame, like the two hands of a Renaissance ceiling fresco, never down at the milk. The forearms enter from the left and right edges, just risen wet from the paraat. |
| 7 | fix 4 | "stop about 1cm apart, a gap nearly as wide as her fingertip, and never touch". |
| 8 | R "what next" 1 | A's ring wording is kept (the lock and "never 2 matching ends … never a hooked tip; no stone, pearl or bezel"). It held construction. |
| 9 | k03-3A colour note | "The ring stays a cool rhodium silver tone, never warmed by the skin or the lamp." |

## k03-5A Mint Pear Drop Earrings (gpt_image_2_6 medium, 2 refs)

The base is the k03-5R prompt, which is the planned prompt with fixes 1-6 applied. Construction passed on R, so its clauses are kept whole. Only the scale tactic changes, as the R log asks.

| # | Source | was (plan) → now |
|---|---|---|
| 1 | fix 1 | The pinch ("holds the pair up like a trophy, pinching both posts …") becomes a pose: the pair rests on her finger pads exactly as on the block in reference 1, posts pointing away with the butterfly backs visible, and her fingertips take the block's place ("like a trophy on a plate"). Nothing pinches and nothing hangs. |
| 2 | fix 2 + diff 3 + learning 9 | THE SWEEP is copied exactly from reference 1: pear 1 at the post, 2 down and out, 3 further and tucked under the mint, the mint BESIDE 2 and 3. COUNT: "three clear pears (3) and one mint pear (1) on each earring, four stones (4) per earring and eight stones (8) in the pair; never two clear pears, never a straight column, never the mint hanging centred below". Reference 2 carries the warning that it looks like a column. |
| 3 | fix 3, replaced by R "what next" | The 9 cm scale clause becomes "a close-up of her fingertips only … cut at the middle knuckles, so only the last two segments of her four fingers … cross the frame … the frame is about 8cm wide; her palm, wrist and forearm are out of frame". R's "her hand is large in the frame" sentence is **cut**: the model met it by growing the earrings to 3x. Two referents: each earring a little longer than her index fingernail and narrower than one fingertip; the mint about half her fingertip's width, a green pea. |
| 4 | fix 4 | "two small milk drops fall from the lowest claws" becomes milk streaming off the sides of her fingers in thin threads, with "no milk drop, drip or bead" on the earrings or any stone. |
| 5 | fix 5 | Placement: the earrings sit 35-47% down and centred; the top third is calm oxblood with at most two petals; 50-68% is the card zone; the lowest third is the soft paraat rim and the milk crown, with no petals. |
| 6 | R prompt | Kept: the "LAST TIME THIS WENT WRONG" sentence, now naming both failures (the column, 2 pears, the gold-tone block, the dangle and the drips at 2x; then the palm at 3x). |
| 7 | learning 6 | "Every claw, post and butterfly back is the same polished 18k gold tone." |

## Take B prompts

- **k03-3B** keeps take A's lock, ONE FINGER clause, frame, calm areas, lights and negatives. It replaces the pose and scale with reference 2's worn hand and ring place (middle finger, 18 cm frame, two referents on that finger).
- **k03-5B** keeps take A's references, sweep, count, last-time sentence, scene, placement, lights and negatives. It replaces the scale and pose with the two-fingertip macro (6 cm frame, each earring a third of the frame width, "never more").

## Flags for the finisher (not prompt edits)

- **Shipping line (owner ruling, 20 Nov 2026).** Every k03 ad carries "FREE INSURED SHIPPING · CASH ON DELIVERY".
  - OBJECTION card 1 and OFFER card 5 may use it in the hook and the primary text.
  - It overrides the camp's switched-off delivery slot.
  - No ad promises a delivery time or claims returns or exchanges.
- **Links and offers.** Every card links to its own product page; there is no BUY3 collection. BUY2 10%, BUY3 20% and BUY4 30% are live.
- **k03-2 size line.** Print "PARAAT ABOUT 45 CM" only if the plate's rim curvature supports it (the k03a log found 25-36 cm).
- **k03-3 gap label.** "THEIR GAP · ABOUT 1 CM" must be measured on the chosen plate.
  - If the chosen take is 3B, the ring is on the middle finger, as in the listing's worn photo.
  - The bracket device still reads "ITS ENDS · ALMOST TOUCHING".
- **Compositing.** The camp's motion lines ("cut-out tracked rigidly") are overridden by the hard rule: motion starts from the verified still and is never composited.

## Lint

The script is `scratchpad/k03r/build_prompts.py`.

- **Banned words:** every prompt was checked for diamond, real gold, solid gold, freshwater, emerald, ruby, huggie, eternity and sterling, and for "gold" or "silver" not followed by "tone". All six are clean.
  - "pearl" appears only in the Droplet negative "no stone, pearl or bezel".
  - "golden undertones" describes skin.
- **Required clauses:** each prompt was checked for 9:16, full-bleed, the exact reference sentence, the verbatim lock with its must-stay clause, mm scale, a contact shadow, "two lights only" with a soft key and a kicker, calm areas, the exact no-text and no-face phrases, and "One product only". All six pass.
- **Water imagery:** all four pieces are tagged waterproof on their product cards, so the milk is allowed.

## Generation record

- **Balance:** 113.71 before. At the end it read 95.21; other batches share the account.
- **This batch's spend:** 9.0 credits, per the transaction log:
  - 4 x GPT Image 2.6 at 1 credit;
  - 2 x Seedream 5.0 Pro at 2.5 credits;
  - spends at 20:09:04-05 UTC (first call) and 20:09:57-58 (the resubmit).
- **Rate limit:**
  - In the first `generate_image_batch` call, items 2 (k03-3A) and 3 (k03-3B) were refused with `submission_failed` (429 rate_limit_reached), so they were never submitted.
  - The four submitted jobs were polled with `jobs_wait` for about 30 s, then items 2 and 3 were resubmitted in round 1 and accepted.
  - No item had an unknown outcome, and no job failed or was flagged nsfw.
- **Served models:** every job was served by the requested model.
  - gpt_image_2_6 pictures are 1520 x 2688.
  - seedream_v5_pro pictures are 1536 x 2720.
- **Records:** `jobs.json` holds no URLs. The pictures were downloaded with curl straight to `pics/<slot>.png`.

## Shooter's first look (for the verifier; not a verdict)

- **k03-1A:** the S-wave of two-row pavé cups the ovals on alternating sides and both looped tips show. The ring is pinched at the band in the ref-1 pose. Check the scale against the thumb: the ring may still read about 1.3-1.5x, and the palm fills less than the asked three quarters.
- **k03-2A:** both hoops have one round disc face up at the latch side, an open plait and a hinge knuckle, with ripples centred on the hand.
  - Check the hoop-to-finger ratio.
  - The fingertip mehendi is four-dot crosses, with no letters.
  - The milk surface reads a little like white ceramic.
- **k03-3A:** **likely fail on construction.** At 1x the index-finger ring shows two stacked balls beside the teardrop (three ends). The level fresco reach and the gap work.
- **k03-3B:** the ring on the middle finger shows one ball beside one teardrop, the tail running down into the band, close to reference 2.
  - Her index fingertip and his are very close: measure the gap (it may be a few mm, not 1 cm).
  - Both hands angle down toward each other rather than reaching level.
- **k03-5A:** **likely fail on scale again.** The pair is drawn very large across the fingers (the mint is about a finger's width) and is cropped at the frame's edge.
- **k03-5B:** the scale reads close to true (the mint is about half a finger's width).
  - Each earring has 3 clear pears and 1 mint.
  - The sweep is steeper than reference 1: pears 1 and 2 are nearly vertical and pear 3 is tucked beside the mint. Check it against the column morph.
