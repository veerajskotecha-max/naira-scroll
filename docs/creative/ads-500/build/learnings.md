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
- **Budget: 4 credits a picture, not 2.** Every job was served as `nano_banana_2`, though `nano_banana_pro` was requested.

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
