# Learnings ledger (read before every batch; the learnings agent appends after every batch)

A device becomes a **rule** once it has beaten the winner anchor in two batches (PLAYBOOK §5.3.5). Until then it is a **note**.
Each batch names one **fix target** (its lowest-scoring dimension) and makes exactly one **new move** (PLAYBOOK §5.3.6–7).

## Starting rules (from the 19 Nov study, PLAYBOOK §3)

1. The piece is the largest and the most saturated thing in the frame. Product-only: at least 35% of the width. Worn: the key detail
   at least 12% of the width (target 15%), within 1.2× true size.
2. Clear, pastel and silver-tone pieces go only on dark or flat saturated grounds. Pale on pale lost twice (VK S5, VK S1).
3. Every "crazy" ad has one impossible-but-honest idea that reads in half a second at 200 px (levitation, spotlight, split
   headline, in-word swap, frozen fall, selective colour). The piece stays at true size and stays the hero.
4. No text touches the piece. Type sits only in calm areas.
5. The F2 card is fixed on every ad: 56 px wordmark, name, price, one line, offer box. No CTA button (Meta adds Shop Now).
6. The first beat of a headline is a listing truth, benefit or mechanism in 2–6 words; an occasion is only ever the second beat
   or the picture. No concept nouns ("APRICOT."), no generic occasion lines ("Make an entrance.").
7. Each batch uses at least 3 lights (L1–L7) and 3 cameras (C1–C6); L7 soft window at most twice.
8. Water, tarnish and skin claims are allowed (RULINGS §1.1) but work best as proof (second beat, chip, callout, or shown by the
   picture), not as the whole headline: the claim-led W1 lost where the texture-led W1 sold.
9. Fidelity: name the piece in a few countable words and add one "must stay X, never Y" clause for the part that morphs. Slot 1 is
   the listing packshot (the authority), slot 2 a detail of the same piece only. Never two products in a frame unless it is a set ad.
10. Scale is built: mm plus a referent (a jasmine bud about 2 cm, a fingertip), a true contact shadow, honest macro depth of field.

## Batch notes

### b01

Shipped 2 of 5: b01-1 Cushion A6 spotlight (mean 7.45) and b01-4 Woven A4 monument (mean 7.06, shipped with a truth caveat).
The batch mean is 7.26. Both ads beat the loser anchor with both critics. Neither beat the winner anchor with both critics:
b01-4 beat F2 on stop power with B only. No note qualifies for promotion to a rule yet, because none beat the winner anchor
in two batches. Full record: `batches/b01/review.md`.

**What worked (notes, not rules)**
- **Construction locks held on all five pictures.** The "must stay X, never Y" clause plus a few countable words kept
  claws, halo rows, brushed finish, braid and stone colours right every time.
- **A ratio inside the piece fixed scale on a rigid piece.** "Band outer 2.5× the stone, opening 2× the stone, never a big
  stone on a small band" corrected b01-1 completely.
- **Low camera works when the result is described.** "About 8°, a long low flat ellipse a third as tall as it is wide",
  with the disc placed where it adds no height, fixed b01-4's placement.
- **Gold mass on a saturated plum ground gave the strongest stop in the batch.** It was about equal to F2 for A and beat F2
  for B. It is a candidate for promotion if it beats the winner again with both critics.
- **The claim as proof read correctly.** The second beat sat at 48 px in gold-light, with droplets in the picture, under
  a texture headline (rule 8). The test is confounded, though, because the picture also changed against W1.
- **"LOOKS LIKE / A PROPOSAL." was the most legible headline on the 200 px sheet.** It was staggered Velista 76 px .12em
  in gold-light over a dark ground. The beat "priced like a present." carries the price surprise.
- **A scrim in the picture's own ground colour calms the card zone without washing the frame.** This was a radial
  rgba of the ground, not the token. The oxblood token flattened the spotlight.

**What failed, and why**
- **Yield 2 of 5: the model centres the subject whatever the percentages say.** Six of eight placement asks landed at
  about 37–62%. Separately, worn and prop-referenced pieces came out 1.27–1.6× true size (bud, finger, wrist), and
  "relaxed hand" came out as a fist. Those three slots (levitation, mehendi hand, worn Prism) were dropped after their
  one regeneration.
- **One earring lying flat at monument scale reads as a bangle or bracelet at 200 px.** The product type sat only in the
  26 px card. Fix: name the type in the headline ("BRAIDED HOOPS.") and the size tag, or brief earrings upright or worn.
- **The kit's `.offer small` (20 px) failed the 26 px floor in every ad.** Fix: one 26 px line, `CODE BUY2 · 10% OFF ◆
  BUY3 · 20% OFF`, with the 9 px gold-light lozenge. Make it the kit default.
- **Meta headlines of 42–43 characters were cut at 40.** The cut dropped the offer's two-piece condition. Fix: cap at 40
  with the value inside, for example `Woven Gold Hoops · ₹1,049 · 10% off 2`.
- **Story twins had no name or price, and b01-4's showed a bangle-like shape.** Fix: name and price in the Story's calm
  band. b01-1's no-text twin stays live as the control.
- **Both shipped ads use L1 on a dark jewel ground with no skin.** They read as one cold mood. Desire is 6.75, the lowest
  dimension, and study gaps 2 and 7 are unmet.
- **The spotlight beam came out as a faint smear, not a cone, so the honest surprise of board 3 is lost.** Separately,
  the Cushion pedestal was more saturated than the ring, and the ring was 31.8% of the width against the 35% rule.
- **The ₹699 SKUs and the bundle offer did not ship.**
- **Budget: 2 credits a picture** (corrected in b02: the b01 "4 credits" read included another session's jobs; the
  transaction log shows 2 per picture). Every job was served as `nano_banana_2`, though `nano_banana_pro` was requested.

**Production hygiene for every ad from b02** (finisher fixes in b01, not creative rules)
- The offer box is one 26 px line. No text is under 26 px in any render.
- The Meta headline is at most 40 characters with the offer value inside. The description is at most 30.
- Every Story carries the product name and price unless it is the named control arm.
- Earring macros name the product type in the headline or show the piece upright or worn.

**Fix target for b02: desire.** Ship at least 2 worn frames, so brief 3:
- **Placement.** The key detail at 36–60% of the frame height and at least 15% of the width. The headline at frame
  15–33% (Feed y 84–340), the card at Feed 900–1258, and Story text in 270–700.
- **Crops where a 20–30% overshoot stays honest.** Woven: an ear-and-jaw crop, no eyes. Serpentine: F2's lips-to-chest
  crop.
- **Skin and styling.** A named skin tone with texture, and one wedding-season detail in the picture: mehendi, a zari
  edge or jasmine.
- **Scale.** Lock it first by a ratio inside the piece, then by one body ratio. Measure with a pixel ruler, and drop
  anything over 1.2×.

**One new move for b02: the worn Woven ear crop with b01-4's copy unchanged.** Brief an ear-and-jaw crop of Woven Gold
Hoops: the pair visible, no eyes, the same on-image copy ("BRAIDED HOOPS. / ZERO STONES." + "and yes, waterproof."), and
the same card and offer. Only the picture changes, from monument to body, so live results against b01-4 isolate whether
the body beats the monument. Everything else in b02 follows the rules above with no other new variable.

### b02

Shipped 1 of 5: b02-1 Woven A2 worn nape (mean 7.35; A 7.15, B 7.55). Both critics picked it over the loser anchor
(`lose_c01_almost_edible_feed`); neither picked it over the winner (`win_e2_ruby_anaar`). The batch failed its own success
test on 3 of 4 counts (only desire, 7.0 against 6.75, passed). b01-4 is held under loop change 8 (A's re-score keeps its
truth at 6), so the body-against-monument test is gone and b02-1 is read against W1 "Woven, not cast". No ad has beaten the
winner anchor with both critics in either batch, so **no note is promoted to a rule**; b01's candidate (gold mass on a
saturated plum ground) got no second win. Full record: `batches/b02/review.md`.

**What worked (notes, not rules)**
- **The camera directly behind the head is the first worn geometry that held no-face and true scale.** The face is
  physically hidden, and anatomy anchors the placement: the hair cut by the top edge, the ears at fixed body positions.
- **A "SCALE, the most important instruction" clause with a visible body referent fixed worn scale on simple pieces.**
  Woven went from 1.7× to 1.1–1.2× with three ratios (hoop about 40% of the ear's height, four hoops across the neck, one
  eighth of the frame width) plus never-limits. On Prism, "one eighth of the wrist's width, never one sixth or one fifth"
  with "twelve stones edge to edge" moved pitch ÷ wrist from 0.178 to 0.150.
- **Skin raised desire.** Real pores, wet sleek hair and a warm world moved desire from 6.75 to 7.0, and truth reached 8
  with both critics.
- **A worn pair names the earring type at 200 px**, in Feed and Story, with no size tag.
- **The Story with headline, name, price and offer** in the hair band lifted purchase cues to 7.5.
- **Construction locks held again:** direct black-and-white selective colour (zero coloured pixels outside the stud,
  twice), the brushed finish, braid, latch and disc, Prism colours and halos.

**What failed, and why**
- **Yield 1 of 5 (3 of 10 over two batches).** The model still centres subjects and grows them 1.3–1.75× past the size
  asked. The fixed F2 card at Feed 940–1258 kills any picture whose subject or shadow reaches past about 62%: Brushed's
  float shadows landed at 62–72% twice, the Verdant Eternity ring reached 66–71%, and Prism's second arm ran diagonally to
  74%.
- **Stop power fell (7.63 → 7.00) because the piece was not the hero.** Each hoop is 13% of the width at the far frame
  edges, warm gold on a same-hue apricot ground, so the hair silhouette lands first at 200 px. The pair-at-the-nape framing
  caps out at 13%.
- **Tight-crop clauses do not keep eyes out.** "The hair covers the top of the ear" was ignored twice and "11 cm across"
  came out about 15 cm, so the Circlet ear profile showed the eye corner both times.
- **A scale clause on the whole outline of a composite piece inflates its parts.** The Circlet's circlet swelled, the round
  pearl became a teardrop and a sixth stone appeared. Lock the internal ratio first, then size the outline.
- **Leaving the reference pose breaks complex settings.** Verdant Eternity's new 35° pose flattened the S-wave into a row.
- **Described light did not render.** L5 backlight came out soft frontal; the L3 gel rim came out a flat stroke.
- **A bead on the piece reads as hardware** (a gold eyelet) at phone size, and a blue floor tints brushed gold grey-green.
- **The brief's "true" ratios were wrong where taken from nominal mm** (Woven diameter ÷ braid about 4.1, Prism pitch about
  8.1 mm, Verdant Eternity oval ÷ opening 0.19). Measure acceptance ratios from the reference photos.
- **The new move was confounded:** the headline alignment, card colour, letter-spacing and offer label changed with the
  picture.

**Production hygiene from b03** (finisher fixes, not creative rules)
- Two-code offer boxes say `CODES BUY2 · 10% OFF ◆ BUY3 · 20% OFF` (RULINGS §2). b01-1 and b01-4 still say `CODE`.
- Velista headlines at .02em or more, never .01em.
- Log the light that rendered, not the one asked (b02-1: "L5 asked, rendered L7-like soft key").
- Verifiers use the brief's referent ranges (wrist 5.5–6.5 cm, ear about 6 cm) and report the central estimate.
- Every prompt that puts water near a piece adds "no water bead or droplet on the jewellery itself".
- Credits are 2 a picture; the balance read 28.46 after b02 (about 18:07), which keeps 4 slots under the brief's rule.

**Fix target for b03: stop power, through the piece.** At 200 px the piece, not the hair, body, ground or headline, is the
first shape to land.
- The worn key detail is at least **18% of the Feed width**: a single-ear crop about 12 cm across for earrings, a 9–10 cm
  hand crop for rings.
- The piece sits in the central column (target x 300–780, never outside x 216–864), with the headline above and the card
  below, built around the model's centring.
- Gold goes on a ground darker or cooler than gold (oxblood, cocoa, ink, deep teal, sage-deep); clear, silver and green stones
  on dark or flat saturated grounds. Never a same-hue ground.
- Gate before layout on the 200 px sheet: measure the piece's width share and its colour difference from the ground behind
  it; drop anything where the hair, head or headline lands first.
- One honest surprise ships. Acceptance: both critics name the product in half a second on the blind sheet, and at least
  one ad beats the winner anchor with at least one critic.

**One new move for b03: b02-1's camera-behind geometry at a single-ear crop.** A back three-quarter view of ONE ear, about
12 cm across, so the piece lands at about 18–21% of the width near the centre and the face is physically hidden. Brief it
first on Verdant Circlet in black-and-white selective colour (board 85), the green stud the only colour, with the circlet's
internal ratio locked first ("about 1.3× the green stone's width, never twice; the big pearl is a round bead"). The one new
variable is the single-ear framing from behind; everything else in b03 follows the rules and the fix target above.

### b03

Shipped 4 of 5, the best yield so far (b01 2, b02 2 of 5: b02-1 and b02-5 from the rescue): b03-2 Cushion A1 NAIRA10 macro
(mean 7.91), b03-1 Brushed A4 plum monument (7.82), b03-5 Pearl Double Halo A6 pool (7.73) and b03-3 Halo Curve A8 callouts
(7.34). The batch mean is **7.70** (A 7.73, B 7.67), against 7.44 for b02's two (b02-1 7.35, b02-5 7.53). Every ad beat the loser anchor with both critics, and truth is 8 or more on all four with both.
b03-1 beat the winner with A only and b03-2 with B only, so **no ad has beaten a winner anchor with both critics in three
batches, and no note is promoted to a rule.** The b03-4 Monochrome float was dropped on extent after its regeneration. The
finisher's fixes came after scoring, so both critics still owe one re-score of b03-1, the b03-2 Story and the b03-3 Feed
(brief loop change 6). Full record: `batches/b03/review.md`.

**The new move's outcome: the note "gold-tone mass on a saturated dark ground" is retired** (loop change 3). It needed a win
over the winner anchor with both critics.
- A voted to promote it: the plum monument was the first shape on the sheet.
- B voted no: the Feed beats `win_static_hoops_apricot` only narrowly, and the Story loses to W1's braid and droplets.
- Over b01 and b03 it won with one critic each time, never with both.

**What worked (notes, not rules)**
- **The product-only monument fixed stop power** (7.00 → 7.69, the b03 fix target). The method:
  - the piece is the largest and brightest shape, centred, at 47–76% of the width;
  - the sliding Feed crop (RULINGS §4) places it;
  - the extent gate is measured first, before any layout.

  b02's "hair lands first" failure did not recur.
- **"Exactly as in the macro/pack reference" plus the reference's own pose held construction on all 7 pictures,** with no morph.
  It is the best fidelity run so far:
  - Cushion: 4 claws and a single-row halo;
  - Brushed: satin finish;
  - Monochrome: 1 + 1 stripes, 3 rails, open C;
  - Pearl: two bands with a bridged gap;
  - Halo Curve: two unmatched stones.
- **Pose and aspect, not size words, control the vertical extent.** b03-3 went from 26% to 21% of the height when the prompt
  copied the ref's own pose ("about 1.3 times as wide as tall; never stood up tall") and raised the camera to 35°.
- **Shadow geometry described by its result renders.** "Short, tucked directly behind and under, no further than a quarter of
  the ring's height; never a long shadow sideways" removed a frame-wide shadow.
- **Dark saturated grounds (plum, ink) gave the loudest frames.** The mid-tone cocoa and sage read drab. This is a production
  fact, not a candidate rule.
- **The price in the beat ("the ₹699 …") was the most legible purchase cue at 200 px.** Purchase cues rose to 8.06.
- **An evening moment in the beat lifts desire even with no skin.** b03-5's "for the sangeet, after dark." under an L1 pool had
  the batch's best desire, 7.5 with both critics.
- **Both critics read the b03-2 macro as a halo ring in half a second.** B rated it the strongest thumbnail, and the NAIRA10
  single-product offer is live-ready as a clean card-variable test.

**What failed, and why**
- **Desire fell to 6.94 (A 7.13, B 6.75), the lowest dimension and the only one that fell.**
  - All four are bare product-on-seamless still lifes, with no skin, prop, rhyme or world.
  - There has been no worn frame for two batches.
  - b03-3's flat mid-sage under a soft key scored desire 6 with B ("a catalogue page").
- **The honest surprise is 0 for 5 over three batches.**
  - The float died on extent again. A floating pair (hoop, gap and shadow) needs about 700 Feed px at the model's hero size,
    against 550 for a headline plus a card.
  - The L1 pool renders as a soft vignette, never a crisp pool.
- **Size words are ignored below the model's preferred hero size** (about 47–76% of the width, 21–26% of the height for a lone
  product).
  - With the 0.7× rule, renders still came out at 1.3–1.85× the share asked.
  - Asking for a third of the share gave a larger picture (2.5–2.65× the ask).
- **An upright earring macro does not name its type at 200 px.**
  - The face-on Brushed huggie read as a cuff or napkin ring to both critics; the finisher had to put "earrings" in the beat.
  - "Huggie" alone does not help: in India, Huggies is a nappy brand.
- **Light words that did not render:**
  - L2 "direct on-camera flash" came out as a soft key twice.
  - "No horizon line" at a 35° camera gave a seam.
  - "A satin-sheen glaze floor" gave a reflection glow under the card.
- **Colour words leak.** "A soft pink-white lustre" gave a blush pearl (a* about 7 against the ref's 2–4). The pearl also showed
  8 regular bridges (the ref has about 5 irregular ones) and micro-glitter pavé. Truth held at 8 only because the count of
  bands and gaps was exact.
- **The brief's reference numbers were wrong twice:**
  - Monochrome H ÷ W is 1.37 on the pack ref, not 1.65.
  - Halo Curve's 11.8 mm is probably the stone's length, not its face (8.6–10.2 mm on the worn close ref).
- **Copy lists parts instead of selling** ("TWO STONES. ONE OPEN BAND.", "TWO BANDS. ONE LIGHT."). The best hooks ("proposal-style",
  "toi-et-moi") stayed in the primary text.
- **Three Stories leave the bottom 35–40% as dead floor.** The model centres the piece, and Story text must end by 1250.

**Production hygiene from b04** (finisher fixes, not creative rules)
- One boxed element per Story: the offer. Size tags in a Story are one plain centred line with no box, because two stacked boxes
  read as two buttons at 216 px.
- On mid-tone grounds, 26 px bone needs 4.5:1. Get there with:
  - Jost 500 on callout lines;
  - wall-sampled scrims at about .5 with a 40 px feather inside the box (24 px reads as tiles);
  - the card scrim at .75.
- Every card line states the metal tone in the listing's own words, for example "surgical stainless steel · 18k gold tone PVD".
- Meta headlines name the product type. Pearl Double Halo uses "Double Halo Studs · …"; "pearl" appears only inside the full
  name.
- Feed text share is a hard gate: A4 stays at .18 or less. A longer beat that crosses it gets shorter words, not a smaller size.
- Log the rendered light ("L2 asked, rendered L7-like soft key") and any card-only variable (NAIRA10) in the ledger.
- Credits: 2 per picture, every job served as `nano_banana_2`. The balance read **14.46** after b03, which leaves **2 pictures**
  for b04 under the 10-credit floor unless the owner adds credits.

**Fix target for b04: desire.** Every frame carries one second element that makes the piece wanted, while the piece still lands
first at 200 px.
- At least one worn frame with real skin, using one of the two proven no-face geometries: b02-1's camera behind the head, or
  F2's lips-to-chest crop.
  - Deep warm skin with pores, a zari or silk neckline cue, and a dark saturated ground.
  - The key detail at 15% or more of the Feed width.
  - Scale locked by a body ratio first; drop anything over 1.2×.
- Every product-only frame becomes either:
  - an **A3 Literal Rhyme**: an in-season prop that rhymes and doubles as the true-scale referent, such as a mogra bud by the
    Pearl studs, a marigold by the Brushed huggies, or chai and mishri by Halo Curve; or
  - a frame with a **time of day in its light** (an evening pool or a warm window rake) on a material surface.
- Grounds are dark and saturated only: plum, ink, oxblood, deep teal, or sage "as dark as forest moss". The floor is matte where
  the card sits.
- Stories put the piece on a riser whose front face fills the lower third.
- The first beat is a reason to want the piece; the occasion goes in the second beat.
- **Acceptance:**
  - the piece lands first and the rhyme or skin second on the blind 200 px sheet;
  - desire is 7 or more on every shipped ad with both critics, and the batch desire mean is 7.25 or more;
  - truth stays at 8 or more, and no dimension falls below 7.

**One new move for b04: the F2 lips-to-chest worn crop on Serpentine Whisper Chain Silver** (23 in stock, claims allowed). It is
the desire fix both critics name, and it has never been generated in ads-500.
- No eyes.
- Deep warm skin with texture.
- A zari or silk neckline edge.
- A dark plum or ink ground.
- The chain's key detail at 15% or more of the Feed width.
- Scale locked by the collarbone ratio first ("the chain runs along the collarbone, about one third of the shoulder width"),
  measured, and dropped above 1.2×.

Everything else in b04 follows the rules and the fix target, with no other new variable. With 2 pictures in the budget, this
slot goes first.

At zero credits before b04, the lead may also lay out the b03-4 float as a card-only A1 at Feed P 100, as both critics
recommend (see the review). That is a rescue of an existing picture, not a new move.
