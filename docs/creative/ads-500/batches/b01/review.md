# b01 review (19 Nov 2026)

This is the finisher's record for batch b01. It covers two critics (A, the creative director; B, product truth and compliance), the fixes applied after them, and the final renders. Both critics reviewed the laid-out ads blind, at full size and on a 200 px sheet with anchors. Their pre-fix scores are below; nobody re-scored after the fixes.

## Result

| Id | Product | Archetype · light · camera | Final verdict | A weighted | B weighted | Mean | Beats loser (A / B) | Beats winner (A / B) |
|---|---|---|---|---|---|---|---|---|
| b01-1 | Cushion Halo Ring | A6 Single Spotlight · L1 · C3 | **ship** | 7.40 | 7.50 (stated 7.70) | **7.45** | yes / yes | no / no |
| b01-4 | Woven Gold Hoops | A4 Monument Macro, claim as proof · L1 · C5 | **ship, with a truth caveat** | 6.60 | 7.53 | **7.06** | yes / yes | no / **yes** |
| b01-2 | Brushed Gold Huggies | A13 Suspended · L1 · C2 | dropped (picture) | – | – | – | – | – |
| b01-3 | Verdant Eternity Band | A1 Product Card, mehendi hand · L4 · C4 | dropped (picture) | – | – | – | – | – |
| b01-5 | Prism Rivière Bracelet | A2 Worn Editorial · L2 · C4 | dropped (picture) | – | – | – | – | – |

- **Shipped: 2 of 5.** The mean weighted score of the shipped ads is **7.26**. That is the mean of the two critics on both ads, using the §7 weights.
- **Critic B's b01-1 score.** B stated 7.70, but B's own dimension scores give 7.50 under the §7 weights. The table and the ledger use the recomputed 7.50. If B's stated figure is used instead, the batch mean is 7.31.
- **Anchors.** Both critics used `win_twenty_f2_tennis_ruby` as the winner and `lose_a07_toggle_story` as the loser on their blind sheets. The brief had named VK S5 as the loser because b01-5 answered it, but b01-5 was dropped.
- **Share beating each anchor:**
  - The loser: both shipped ads, by both critics.
  - The winner: none by A; b01-4 by B, on stop power.
- **Thumbnail test** (216 px, after the fixes):
  - The two ads are easy to tell apart.
  - Both headlines read.
  - Both products can be named. Before the fixes, b01-4 read as a bracelet.

### Mean per dimension (both critics, both shipped ads)

| Stop | Message | Truth | Layout | Brand | Copy | Fit | Desire | Cues |
|---|---|---|---|---|---|---|---|---|
| 7.63 | 7.25 | 7.50 | 7.00 | 7.75 | 7.50 | 7.25 | **6.75** | 7.00 |

**Ship-rule check (PLAYBOOK §7)**

Both ads:
- pass compliance with both critics;
- have no dimension under 6;
- were picked over the loser by both critics.

On product truth:
- **b01-1** scores 8 from both critics.
- **b01-4** scores 8 from B (the truth critic) and 6 from A. A expects about 7.5 once the type fixes are in.
- b01-4 ships on both critics' explicit "ship-after-fixes" verdicts. Every fix A made a condition of shipping has been applied.
- The caveat stays on record. The latch is drawn as a chunky hinge block with a hooked wire, where the real piece has a thin latch wire, and the wires are about 1.3× too thick. Only a new picture fixes these. **Lead: hold b01-4 if you read the 8+ truth floor as applying to each critic.**

---

## b01-1 · Cushion Halo Ring · A6 Single Spotlight · ship

Files:
- Feed: `b01-1_feed.jpg`
- Story: `b01-1_story.jpg`
- Copy: `b01-1.copy.json`
- Picture: job `810ed20b-9aff-483f-8f68-715342f70d73` (try 2)

| Dimension | A | B |
|---|---|---|
| Stop | 7 | 7 |
| Message | 8 | 8 |
| Truth | 8 | 8 |
| Layout | 7 | 7 |
| Brand | 8 | 8 |
| Copy | 8 | 7 |
| Fit | 7 | 8 |
| Desire | 7 | 7 |
| Cues | 7 | 8 |
| **Weighted** | **7.40** | **7.50** |

**Fixes applied**
1. **Offer box (both critics: the render gate failed at minFont 20).** The offer is now one 26 px line: `CODE BUY2 · 10% OFF ◆ BUY3 · 20% OFF`.
   - The kit's 20 px `<small>` codes line is gone.
   - The line uses B's one-line markup and the 9 px gold-light lozenge separator, which A asked to keep as the batch's single offer device.
2. **Card top moved from 910 to 920 (B).**
   - B tested this together with the one-line offer, which makes the card 29 px shorter.
   - The wordmark gains clearance from the ring's contact shadow, and the card ends at 1232, inside 1266.
3. **Meta headline: `Cushion Halo Ring · ₹999 · 10% off 2` (36 characters; B).**
   - At 42 characters, the old headline was cut at 40 to "…10% off". That dropped the two-piece condition and misstated the verified offer.
4. **Meta description: `Silver tone · cubic zirconia` (28 characters; B).** "Adjustable" already appears on the card and in the primary text.

**Not applied**
- **A's headline at 80 px / .10em with a 52 px beat.** Only A proposed it. B rated this headline the most legible on the sheet.
- **A's Story text** ("LOOKS LIKE / A PROPOSAL." plus "priced like a present: ₹999.").
  - B and the A6 spec both keep the no-text twin.
  - It ships as the control arm, so the next batch can test whether a Story with name and price beats it (see "Fix target").
- **Copy.** Both critics left the primary text unchanged: 159 characters, with the offer ending at character 115.

**Final render**
- Feed: `failed [] · overflow [] · fallback [] · outside [] · textShare 0.126 · minFont 26`.
- Story: `textShare 0 · minFont null` (no text, by spec).

**Truth notes (no change needed)**
- One small 4-point glint on the back-right claw.
- The shoulder pavé covers about 2/3 of the band; the real piece covers about 1/2.
- The ring is 31.8% of the frame width; rule 1 asks for 35%.
- Scale is 16.3 px/mm, so no size tag is needed.
- These features match `cushion-halo-ring__upright.jpg`: 1 round stone, 4 claws, a single-row cushion halo, an open back with overlapping ends, and a cool silver tone.

---

## b01-4 · Woven Gold Hoops · A4 Monument Macro, claim as proof · ship (truth caveat)

Files:
- Feed: `b01-4_feed.jpg`
- Story: `b01-4_story.jpg`
- Copy: `b01-4.copy.json`
- Picture: job `85ffa05a-dbd5-45e2-ad6d-bdacb83e9d5d` (try 2)

| Dimension | A | B |
|---|---|---|
| Stop | 8 | 8.5 |
| Message | 6 | 7 |
| Truth | 6 | 8 |
| Layout | 7 | 7 |
| Brand | 7 | 8 |
| Copy | 7 | 8 |
| Fit | 7 | 7 |
| Desire | 6 | 7 |
| Cues | 6 | 7 |
| **Weighted** | **6.60** | **7.53** |

**The shared finding.** Both critics say that one hoop lying flat at 85% of the width reads as a bangle or bracelet at 200 px, and that the product type has to be named. A made the headline and the size tag conditions of shipping. Without them, A rejects the ad.

**Fixes applied**
1. **Headline (A's gate fix 1; it answers B's finding).** `BRAIDED HOOPS. / ZERO STONES.`, Velista 92 px (down from 96), .01em, nowrap, at left 72, top 88. The headline is still texture-led, as in the W1 winner. At 216 px it now names the product.
2. **Size tag (A's gate fix 2, merged with B).** The tag reads `SHOWN MAGNIFIED / HOOP ABOUT 25 MM` on both the Feed and the Story.
   - It names the hoop as A asked.
   - It keeps the truth sheet's "about 25 mm", which B kept and which A's "actual hoop 25 mm" dropped.
3. **Card line (both critics, same wording):** `hoop earrings · 18k gold tone PVD`.
4. **Offer box (both critics; minFont 20 failed the gate).** One 26 px line with the same lozenge as b01-1, so the batch uses a single offer box.
5. **Card top moved from 945 to 962, gap 14 (B).** Tested with the one-line offer. The wordmark now clears the droplet at x 365–445, y 905–945 by 17 px, and the card ends at about 1258.
6. **Story: name and price added (A).** `WOVEN GOLD HOOPS` in Jost 26 px at top 520, and `₹1,049` in Cormorant 56 px at top 562. Both sit above the hoop, which starts at y 709.
   - Both critics had listed the missing name and price.
   - B's "Hoop earring" naming is carried by the tag's "HOOP" and by the product name.
7. **Primary text (A's first beat with B's truth fix).** 157 characters, with the offer ending at character 119. "about 25 mm across" replaces "about 25 mm of braided", which read as 25 mm of braid length:
   > Braided hoops, zero stones: Woven Gold Hoops, ₹1,049, about 25 mm across, in 18k gold tone PVD. BUY2: 10% off 2 pieces. And yes, waterproof and tarnish-free.
8. **Meta fields (B).** The headline is now `Woven Gold Hoops · ₹1,049 · 10% off 2` (37 characters). The old one was cut at 40 to "…10% of". The description is now `18k gold tone PVD · waterproof` (30 characters).

**Not applied**
- **Raising the claim beat to 56 px.** A said explicitly not to enlarge it; for B it was an optional nit. It stays at 48 px gold-light as proof (learnings rule 8).

**Final render**
- Feed: `failed [] · overflow [] · fallback [] · outside [] · textShare 0.173` (the A4 cap is 0.18) `· minFont 26`.
- Story: `textShare 0.026 · minFont 26 · outside []`.

**Residuals (they need a new picture)**
- The latch is drawn as a chunky box hinge with a hooked wire, not the thin latch wire.
- The wires are about 1.3× thicker, and fewer, than in the detail reference.
- Magnification is about 2.1× life, which the size tag declares.
- It is still one flat hoop, not the upright pair both W1 ads had.
- The construction is right: the braid, a mirror-polished disc at about 0.22 of the hoop width, zero stones, and a warm 18k gold tone.
- The droplets are 2–4 mm, and water is allowed for Woven (RULINGS §1.1).

---

## Dropped pictures (each regenerated once; RULINGS §1.2, so not edited)

| Id | Job (try 2) | Why |
|---|---|---|
| b01-2 Brushed huggies, levitation | `a6b9fc88-6a91-497e-9ac5-24c8a1e783dc` | The model centred the subject again. The shadows sit at 57.5–62% and the bud at 63.5–69%, under both cards. Try 1's huggies were 1.15× the bud, about 1.6× true size. |
| b01-3 Verdant, mehendi hand | `eca4d860-86f3-4290-8219-75e4a3c537dc` | The hand sits at 28–62% and the ring at 45.7–54.5%, where the card goes. The ovals read 1.4–1.6× true size against the finger and the nail. Try 1's pavé had closed into a full halo around each oval. |
| b01-5 Prism, worn flash | `85160c01-62a8-4e2d-ba9d-a2f37789c0ac` | The bracelet is centred at 47.9–51.6%, where 28–32% was asked. The link pitch is 0.198 of the wrist width against a true 0.13–0.16, so it reads 1.27–1.38×. Try 1 was a clenched fist. |

---

## Better than the previous batch because

b01 is the first ads-500 batch, so there is no previous batch. Against the anchors and the study:
- **Against the loser.** Both shipped ads clearly beat it (`lose_a07_toggle_story`, a pale chain under a dense text panel) at 200 px, by both critics.
- **Against the winner.**
  - b01-4 matches or beats F2 on raw stop power, by A and B respectively. Its gold mass is the largest, brightest and most saturated shape on the sheet.
  - b01-1's headline is the most legible on the sheet.
  - On understanding and desire, F2 still comes first.
- **Against our W1 pair.** b01-4 rebuilds the texture-led W1 winner correctly: a texture headline, the claim as the second beat, droplets as proof, a size tag and a plum ground. It clearly beats the claim-led W1 loser.
- **Fidelity locks.** They held on both shipped pictures. Every failure in b01 was placement or scale, never product identity.
- **Study gaps closed:**
  - gap 5: the verified offer is on the image, with values;
  - gap 6: truth-led first beats;
  - gap 10: one F2 card with a 56 px wordmark;
  - gap 11: native 9:16, with Story text inside 270–1250.
- **Gap 1 is half closed.** b01-4's piece dominates its frame. b01-1's ring is 31.8% of the width, and its pedestal is more saturated than the ring.
- **Fixes the finisher made that carry forward:**
  - every offer box now passes the 26 px floor;
  - every Meta headline keeps its offer value inside 40 characters;
  - b01-4 now names its product type at 200 px.

## Still missing

1. **Desire: no body, no skin, no moment.** Both shipped ads are cold product still lifes. Gap 2 is open, the one-occasion-per-batch rule is unmet, and one of our two tested statics that sold (F2) is worn.
2. **Variety of light and ground (gap 7).** Both shipped ads use L1, a hard spot on a dark jewel-tone ground (oxblood, plum), so they read as one mood. The rule of at least 3 lights and 3 cameras was met only by the dropped slots.
3. **An honest surprise (gap 3).** b01-1's spotlight beam is a faint smear rather than a visible cone, so it reads as a polished catalogue ring (nearer board 166 than board 3). The levitation (A13) was dropped. b01-4's monument sits whole, level and centred; boards 26 and 42 are tilted and cropped by two edges.
4. **₹699 and the bundle offer (the second half of gap 5).** Brushed was dropped, so no ₹699 SKU and no bundle-led ad shipped.
5. **The new move is confounded.** b01-4's claim-as-proof changed the picture too: one flat hoop at about 2× on plum, against an upright pair on oxblood in W1. Live results cannot isolate where the claim sits.
6. **Story purchase cues.** b01-1's Story has no name or price. It is kept as a control on purpose.
7. **Yield.** 2 of 5. The model centres subjects and oversizes worn pieces, so the batch matrix lost 3 of its 5 archetypes.

## Fix target for the next batch

**Desire.** It has the lowest dimension mean (6.75), and both critics name it. b02 must **ship at least 2 worn frames, so it should brief 3**. Each worn frame:
- **Composition.** Build around the model's centring habit, not against it:
  - the key detail at 36–60% of the frame height and at least 15% of the width;
  - the headline band at 15–33% (Feed y 84–340);
  - the card at Feed 900–1258;
  - Story text in 270–700.
- **Crops where a 20–30% overshoot is still honest:**
  - Woven: an ear-and-jaw crop at about 12 cm, the pair visible, no eyes.
  - Serpentine (or Toggle, but only after the clasp gate): F2's lips-to-chest crop at about 85 mm.
- **Skin and styling.** A named skin tone with visible texture, plus one concrete wedding-season detail in the picture, not the headline: mehendi, a zari blouse edge, or jasmine in the hair.
- **Scale.**
  - Lock it first by a ratio inside the piece: hoop diameter 5× the braid thickness; ring band 2.5× the stone; Serpentine's 10 mm stone against its 2 mm chain.
  - Then add one body ratio: about ten stones across the front of the wrist, the band one eighth of the wrist width.
  - Measure with a pixel ruler before layout, and drop anything over 1.2×.
- **Standing purchase cue (both critics).** Every Story carries the product name and price in its calm band. b01-1's no-text twin is the control already made.

## Ideas for the next batch

1. **Worn Woven, same copy (both critics).** An ear-and-jaw crop with no eyes:
   - wet hair after a swim, or wet oxblood behind;
   - the pair visible;
   - b01-4's exact on-image copy ("BRAIDED HOOPS. / ZERO STONES." + "and yes, waterproof.");
   - this tests body against monument with the copy held fixed, and the ear answers the bangle misread.
2. **Serpentine Whisper Chain (silver tone, 23 units) in F2 grammar.**
   - A lips-to-chest crop on deep-brown skin against cocoa or ink, with L2 flash and C4.
   - The 10 mm cushion cubic zirconia is the internal ruler.
   - Use either the A1 card with no headline or the queued A7 split headline.
3. **Make the light the idea, honestly.**
   - Rerun the Cushion A6 with atmospheric haze, so a visible cone falls from the top right (board 3).
   - Or try A7: the ring standing between "LOOKS LIKE" and "A PROPOSAL.", splitting the headline (board 55).
4. **Brushed ₹699 levitation, built for a centred subject.**
   - The card and headline go at the top (Feed 84–420), and the huggies at 36–50%.
   - The shadows and the bud stay visible at 57–72% as the proof.
   - Headline: "The ₹699 pair."
5. **A11 offer poster or bundle.** Pick one:
   - "BUY 3 · 20% OFF" as one photographed group at true relative scale (Brushed, Ribbon, Verdant Circlet);
   - or Brushed plus Ribbon (both ₹699) worn on one body, with "BUY 2. / 10% OFF.".
   - Either way it lands on a set or discount link, not a single product page.
6. **Saturated flat fields, not dark jewel tones.**
   - Gold tone on cobalt, deep teal, saffron or sky, in L6 or L4 sun.
   - The piece tilted 10–35° and cropped by two edges (boards 26, 42).
   - At most one dark spotlight per batch.
7. **Bold Nocturne Drops (20 units, at the stock edge; re-read stock first).**
   - An A6 spotlight on ink, both drops hanging so the two-link structure reads ("PLAIN LINK. / PAVÉ LINK.").
   - Lock: "exactly two links, top one plain".
8. **Prism on black, accepting the centred bracelet.**
   - The headline above, the card below, and the Story's name and price above the hand.
   - Lock about ten stones across the wrist.
9. **Picture lock for earring macros.** Show the earring upright or worn, never lying flat, so its type reads at 200 px without a tag.
10. **Kit.** Make the one-line 26 px offer box the kit default, remove `.offer small`, and cap Meta headlines at 40 characters with the value inside. These were finisher fixes in b01; the kit itself was not changed.

## Prompting learnings

1. **Construction locks hold; placement does not.**
   - All five pictures kept their countable construction:
     - 4 claws and a single halo;
     - brushed, not mirror;
     - a many-strand braid;
     - haloed pastels with no repeated neighbours;
     - green ovals.
   - The "must stay X, never Y" clause works.
   - The one drift was Verdant's pavé closing into a full halo around each oval. The lock now says "pavé on one side only, never a full halo around each oval".
2. **The model centres the subject, whatever the percentages say.**
   - Six of eight placement asks landed the subject at about 37–62%, including the second tries with "nothing below 50%" and the empty zone named as the largest area.
   - Design layouts around a centred subject. Describe placement as physical geometry ("lens almost at table level", "the sleeve cuff at 38%"), and state each calm band as a hard negative.
3. **Ratios inside the piece fix scale; scene referents do not.**
   - Fixed: "band outer = 2.5 × stone; opening = 2 × stone; never a big stone on a small band" corrected b01-1 completely.
   - Not fixed: against body or prop referents (finger, nail, wrist, bud), three of three came out 1.27–1.6×.
   - When a referent is used, state the relation as a comparison ("each huggie clearly SHORTER than the bud"), put it at the same depth ("never nearer the camera"), and give both sizes as shares of the frame width.
4. **Worn pieces get chunkier, and widening the frame does not shrink the jewellery.**
   - Lock the count across the body ("about ten stones across the front of the wrist"), the band against the body ("one eighth of the wrist width, never a quarter"), and the words "slim, delicate".
   - "Relaxed hand" needs "NOT a clenched fist".
5. **Low camera works when the result is described.**
   - "About 15°" came out at 35–40°.
   - "About 8°, a long low flat ellipse a third as tall as it is wide", with the disc placed where it adds no height, fixed b01-4.
6. **Glints.** "No star-shaped glints" does not stop them on a brilliant-cut stone under a hard spot. Ask for "soft round specular highlights only, no rays", or soften the key light for clear stones.
7. **Budget and the served model.**
   - Each picture cost 4 credits (202.46 → 182.46 for five).
   - Every job was served as `nano_banana_2`, although `nano_banana_pro` was requested. b01-1 still had the best fidelity, so the served model does not explain the misses.
   - Read the balance right before each generate call, and plan regenerations at 4 credits each.
   - A five-item batch hit one 429; resubmit only the failed item, after the first job completes.
8. **Earring macros lying flat read as bracelets.** Brief earrings upright or worn. If a macro of one flat hoop is unavoidable, the headline must name the type.
