# b02 rescue: b02-2 and b02-5 laid out at zero credits (19 Nov 2026, about 18:52 UTC)

This is b02 loop change 2. The pictures already existed. Nothing was generated, edited, scaled or composited, and no Higgsfield
tool was called. The two Feed crops use the RULINGS §4 rule as amended at 18:45 ("Feed = any 4:5 window,
`.pic { object-position: 50% P% }`, T = 5.85 × P, Feed y = src y × 0.703125 − T"). Each Story is the native frame
(Story y = src y × 0.703125 − 7.5).

Both ads still go to both critics, scored on the final JPGs listed at the end. Nothing here is a ship verdict. Ledger and
learnings untouched.

## Crops and subject extents

Extents were measured on the source: sky-difference mask for b02-2, a green-or-unsaturated mask for b02-5. The verifier's
numbers agree to within about 5 px.

| Ad | Picture | P | T | Subject extent on the Feed | Gate |
|---|---|---|---|---|---|
| b02-2 | `pics/b02-2.png` (try 2) | **85** | 497 | huggies y 333–603, x 283–821 (49.8% wide); shadows y 831–886; full extent **333–886 (553 px)** | headline + card band 380–930 holds 550 px. The extent is **3 px too tall** for any T, so it can never sit strictly inside. The 47 px above 380 is plain sky under the beat (beat glyphs end at about 278). |
| b02-5 | `pics/b02-5_try1.png` (try 1) | **100** | 585 | ring y 79–792 (lowest prong 797), x 317–802 (45% wide); contact shadow to the right, y 690–840; full extent **79–840** | card-only band 84–930. The ring's top arc reaches 79, **5 px above 84**. T is already at its maximum (585). That 5 px is picture, not text. |

**Why b02-2 uses P 85, not loop.md's P 80**
- At P 80 (T 468) the extent is 362–915, and the shadows end only 25 px above the wordmark at 940. The card crowded the float,
  and the float is the proof.
- At P 85 the gaps are even: about 55 px from the beat to the huggies, and 54 px from the shadows to the card.
- The headline moved from top 104 to 96, and the beat from 226 to 214, to keep the top gap.

**Scale**
- **b02-2:** about 17 px/mm (338 px for 14 mm on the source × 0.703). That is under the 19 px/mm trigger, so there is no size tag.
- **b02-5:** the front ovals measure 110–120 × 85–96 px for 5 × 4 mm, which is about 23–24 px/mm. The ring's height alone would
  give about 35 px/mm, because the model drew the stones small for the band (oval ÷ inner opening 0.19, the same as the upright
  reference). Either way it is over 19, so the size tag is on both formats.

## Copy chosen, and why

### b02-2 · Brushed Gold Huggies · A13 Suspended

**On image: the brief's copy, with two fixes**
- **Headline:** "The ₹699 pair."
  - Cormorant Garamond italic 500, 96 px, ink. A13 allows Cormorant 96 when the headline holds a price.
  - The rupee and the digits cannot go in Velista, so no Velista is used on this ad.
- **Beat:** "any three pieces, 20% off."
  - **60 px.** The brief's 52 px is 0.54 × the headline, under the §4.0 floor of 0.6. At 60 px it is 0.625.
  - Set in **--oxblood**, not coral-deep: coral-deep reads 1.8:1 on this sky, oxblood 5.4:1.
  - The bundle line is allowed because BUY3 is verified, and the offer box on the same frame names the code.
- **Card line:** the brief's "soft brushed satin, not mirror polished" became **"about 14 mm · brushed satin, 18k gold tone"**
  (PLAYBOOK A1's Brushed line). `products.md` lists "mirror" as forbidden for this SKU.
- **Offer:** `Codes BUY2 · 10% off ◆ BUY3 · 20% off`, with an oxblood lozenge.
- **Story:** the brief's stack (headline Cormorant 80, beat 52 at 0.65, name and price on one baseline, offer), spaced
  270–714 so that about 108 px of plain wall stays above the pair.

**Meta**
- **Primary text:** the brief's last sentence "Never mirror polished, and waterproof." became "And yes, waterproof and tarnish-free."
  (the same "mirror" reason; the claims sit last, as proof).
  - "The ₹699 pair: Brushed Gold Huggies, about 14 mm, in soft brushed satin 18k gold tone. Any 3 pieces with BUY3: 20% off. And yes, waterproof and tarnish-free."
  - 157 characters; the offer ends at character 119.
- **Headline:** "Brushed Gold Huggies · ₹699 · 20% off 3" (39 characters).
- **Description:** "Brushed satin · 18k gold tone" (29 characters).
- **URL:** `utm_campaign=ads500_b02`, `utm_term=b02-2_a13_brushed-699-levitation`.

### b02-5 · Verdant Eternity Band · A1 Product Card (was A5)

**On image**
- No headline.
- **Size tag:** "SHOWN MAGNIFIED / ABOUT 16.5 MM INSIDE", from the listing's inner diameter of about 16.5 mm.
- **Card line:** "emerald-green cubic zirconia · adjustable US 5 to 9". `products.md` gives oval green CZ 5 × 4 mm, an open back
  adjustable US 5–9, and the allowed words "emerald-green cubic zirconia" and "adjustable". The wording matches the listing,
  so it was kept as given.

**Feed layout**
- **Tag:** kit 30 px, padding 8/16, centred at 820–912.
  - It sits 23 px under the lowest prong and 28 px over the wordmark.
  - It is set in ink-soft so that it reads as the ring's caption, below the brand in the hierarchy.
  - Beside the ring there is at most about 340 px of width, too narrow for the 438 px tag.
- **Card:** top 940 to 1252, on plain saffron.
- **Lozenge:** the stones' own green (#196B3E, sampled). Coral-deep disappears on saffron.

**Story layout**
- The whole card moves above the ring and ends at 626, before the 630 limit; the ring starts at 656.
- **Stack:** wordmark 270–326, name and price on one baseline, line, offer 458–520, then the tag at 540–626.
- **The tag** keeps the Feed's two-line form, at the brief's Story size of 26 px. A one-line tag ran 720–820 px wide and read
  as a second offer bar stacked under the first.

**Meta (the brief's, unchanged)**
- **Primary text:** "US 5 to 9, one ring: Verdant Eternity Band, ₹1,049, emerald-green cubic zirconia, open back adjusts. BUY2: 10% off 2 pieces. Silver tone, and waterproof."
  - 153 characters; the offer ends at character 124.
- **Headline:** "Verdant Eternity · ₹1,049 · 10% off 2" (37 characters).
- **Description:** "Adjustable US 5 to 9" (20 characters).
- **utm_term:** changed to `b02-5_a1_verdant-us5-9` to match the new archetype.

### Banned-word scan

Over all four pages and both copy files there are no hits for diamond, real gold, solid gold, freshwater, emerald or ruby as a
noun, free shipping, compare-at or "was" prices, or "mirror". Gold and silver appear only as "18k gold tone", "silver tone"
and inside product names.

## Contrast

Each text box was measured against the picture behind it. Figures are the median, with the 2nd percentile in brackets. No
scrim was needed anywhere.

| Page | Readings |
|---|---|
| b02-2 Feed | headline ink 8.6 (8.2) · beat oxblood 5.4 (5.2) · wordmark 12.7 · name 12.2 · price 11.5 · line 10.9 · offer 10.3 |
| b02-2 Story | wordmark 8.0 · headline 8.2 · beat oxblood 5.1 · name and price 8.5 · offer 8.6 |
| b02-5 Feed | tag ink-soft 7.3 (4.7 where the box edge meets the shadow) · wordmark 11.0 · name 11.0 · price 10.9 · line 10.8 · offer 10.7 |
| b02-5 Story (darker saffron at the top) | wordmark 5.8 · name and price 5.9 · line 6.0 · offer 6.1 · tag ink-soft 4.2 (3.9). The tag is 26 px Jost 500, which counts as large text. |

## Renders (final, from `batches/b02`, `node ../../kit/render.cjs`)

```
{"out":"b02-2_feed.jpg","size":"1080x1350","failed":[],"overflow":[],"fallback":[],"textShare":0.12,"outside":[],"minFont":26}
{"out":"b02-2_story.jpg","size":"1080x1920","failed":[],"overflow":[],"fallback":[],"textShare":0.064,"outside":[],"minFont":26}
{"out":"b02-5_feed.jpg","size":"1080x1350","failed":[],"overflow":[],"fallback":[],"textShare":0.078,"outside":[],"minFont":26}
{"out":"b02-5_story.jpg","size":"1080x1920","failed":[],"overflow":[],"fallback":[],"textShare":0.057,"outside":[],"minFont":26}
```

Final JPG times (`stat -c %y`), for the critics' `scoredFile`:

| File | Modified (UTC) |
|---|---|
| b02-2_feed.jpg | 2026-11-19 18:51:53 |
| b02-2_story.jpg | 2026-11-19 18:51:54 |
| b02-5_feed.jpg | 2026-11-19 18:51:54 |
| b02-5_story.jpg | 2026-11-19 18:51:54 |

## What I could not satisfy

1. **b02-2: the placement gate, by 3 px.** The extent is 553 px against a 550 px band, so no T fits it strictly inside
   380–930. Nothing touches type: the gaps are about 55 px above and 54 px below.
2. **b02-2: the picture's colour.** The grey-green lower halves (saturation 0.07–0.12) stay, because they are in the picture.
   The pair also spans about 49–50% of the width, against the brief's 35–45%.
3. **b02-5: the ring's top arc** sits at Feed 79, 5 px above the card-only band, with T already at its maximum. Its headroom
   (79 px) is tighter than its room below (23 px to the tag, then the card).
4. **b02-5: the space around the tag.** The tag has only 148 px between the ring and the card. It is centred with
   gaps of 23 and 28 px. That is legible, but a tag-then-card column is tighter than an art director would choose.
5. **b02-5: the Story size tag** is 26 px, the brief's Story size, not the PLAYBOOK's 30 px. At 30 px the two-line tag does not
   fit above the ring by 630 together with the card line.
6. **The kit's coral-deep accent** fails on both grounds. Oxblood is used on sky and the stone green on saffron. I did not
   change the kit.
7. **No ledger rows were written** (out of scope). Loop change 2's ledger test still needs the lead to add the new verdicts and
   the `scoredFile` values once the critics have scored.

## Fixes after the first critique

Finisher pass on **b02-5 only** (19 Nov 2026, about 19:12 UTC). First-round results on the 18:51:54 renders: A ship-after-fixes
(weighted 6.95, layout 6), B ship-after-fixes (7.65, layout 7), skeptic not refuted. Nothing was generated, edited, scaled or
composited; the crop (P 100, T 585) and the picture are unchanged. b02-2 is untouched. Ledger and learnings untouched.
Files changed: `b02-5_feed.html`, `b02-5_story.html`, `b02-5.copy.json`, and the two JPGs below.

The critics agree on the fault (the size tag jammed 23 px under the prongs and 28 px over the wordmark, a dense 820–1252 column
on the Feed, and a Story tag 30 px over the ring). They disagree on the cure: A moves the card, B says the card needs no change.
Neither critic raised a compliance fail, so no fix came from compliance.

### Applied

1. **Feed card: name and price on one baseline (A).** Jost 500 26 px .2em caps name and Cormorant Garamond 500 56 px price, gap
   24 px, centred, the same arrangement as this ad's Story twin. The card moves down: wordmark 940 → **992** (A asked "about 990";
   992 keeps the offer box exactly where it was, 1190–1252). Measured boxes: wordmark 992–1048, name and price row 1068–1124,
   line 1138–1176, offer 1190–1252.
   - *Disagreement, decided for A.* B's "no change to the card" is about its content, which stays the same: the same five elements
     at the same sizes. Only the arrangement changes, and it is the arrangement already used on the Story twins of b02-2 and b02-5.
     B's own write-up names the dense tag-plus-card column as the layout fault, and layout is the lowest dimension for both
     critics. Freeing one card row is the only way to add air without touching the picture or shrinking type. The offer box
     cannot go lower (the safe area ends at 1266), and the ring cannot go higher (T is already at its maximum, 585).
2. **Feed size tag 820–912 → 854–946 (A asked about 852–944).** Now 57 px under the lowest prong (797; was 23) and 46 px over the
   wordmark (was 28).
   - *Why 2 px lower than A's figure.* The ring's contact shadow trails right and fades out by about y 866 at x 660–880. Its
     luminance is 185–193 against a 199 ground at y 848–860. The tag's glyphs now start at about y 870, on clean saffron.
   - The tag's worst-case contrast rose from **4.7 to 7.1** (median 7.3 → 7.5), which confirms it has left the shadow.
   - No type is on the ring or its shadow.
3. **Card line, Feed and Story: "adjustable US 5 to 9 · emerald-green cubic zirconia" (A).** B did not object; it raised nothing
   about the order.
   - *Decided to apply.* The words are the same, so compliance is unchanged, and "emerald-green cubic zirconia" stays one phrase.
   - Fit is the main objection to buying a ring online. The card now leads with it, as the primary text already does ("US 5 to 9,
     one ring").
4. **Story stack closed up by 12 px (A).** The tag moves from 540–626 to **532–614**. It now clears the ring's top arc (656) by
   **42 px** instead of 30. All text stays in 270–614.
   - **Changes:**
     - line-to-offer glyph gap 14 → 12 (offer box 458–520 → 456–518);
     - offer-to-tag gap 20 → 14;
     - tag padding 10/18 → 8/16, the same as the Feed tag, which saves 4 px.
   - *Not A's example of an 8 px line-to-offer gap.* That would be the tightest gap in the stack and would jam the 26 px line onto
     the box. Taking 4 px from the tag padding gives the same 12 px, with gaps of 12 and 14, which matches the card's 14 px rhythm.
5. **Meta headline: "Verdant Eternity · ₹1,049 · 10% off 2" (37) → "Verdant Eternity Band ₹1,049 · 10% off 2" (40, at the cap) (B).**
   A made no comment on the Meta copy.
   - *Decided to apply.* It names the product in full, as on the landing page.
   - "Band" answers A's note that at 200 px the upright open band could read as a cuff or bangle. This follows the b01 learning:
     name the type in words where the picture cannot.
   - The value and the two-piece condition stay inside 40 characters, so nothing is cut (b01 hygiene).

### Declined

6. **B (optional): tag line "ABOUT 16.5 MM ACROSS INSIDE".**
   - "Inside" already names the inner diameter, the figure ring buyers compare.
   - The longer line would widen the Feed tag from 438 to about 580 px (Story 385 to about 510), close to the 726 px offer box.
     That strengthens the "twin of the offer box" fault A scored, and on the Story the tag sits only 14 px under the offer box.
   - The skeptic found the tag true as written on both formats.
7. **B: "no change to the picture, card or offer".** The picture and the offer are unchanged. The card's content is unchanged; its
   arrangement changed under fix 1, for the reason given there.

### Skeptic's copy fix

None needed. "Keep stone millimetres out of all copy" is already true. The scan finds no "5 x 4" and no 4 mm or 5 mm figure in the
on-image text, the Story text or the Meta fields. The only millimetre figure is the listing's 16.5 mm inner diameter, in the tag.

### Left as they are (noted by the critics, no fix asked)

- **The ring's top arc at Feed y 79**, 5 px above the 84 gate. It is picture, not text, and T is at its maximum.
- **The Story tag at 26 px, not the 30 px role** (B). At 30 px it would be about 10 px taller and end near 624, 32 px over the ring.
  The 42 px clearance wins.
- **A light, saturated saffron ground with ink type, where A1 specifies dark with bone** (fit 7 from both critics). This is the
  picture. Learnings rule 2 allows a flat saturated ground.
- **The skeptic's lead note:** the picture closely follows the listing photo's pose (generated, job a51af63b, so it passes
  RULINGS §1.2). That call is the lead's.

### Checks

- **Banned words:** none in either page or `b02-5.copy.json`. No diamond, real gold, solid gold, freshwater, emerald or ruby as a
  noun, free shipping, compare-at or "was", mirror, or gold or silver alone as the metal.
- **Meta lengths:** primary text 153, headline 40, description 20.
- **Looked at** both final JPGs at full size and at 216 px wide.
  - **Feed, full size:** clear air above and below the tag, and the shadow's tail ends before the tag's glyphs.
  - **Story, full size:** one block above the ring with a clean 42 px gap.
  - **At 216 px:** the green-on-saffron ring lands first on both formats, and the price shape and the offer box read. The tag and
    the name do not read at that size, as before.

| Page | Contrast, median (2nd percentile), against the picture under each box |
|---|---|
| b02-5 Feed | tag ink-soft 7.5 (7.1) · wordmark 11.0 · name and price 10.9 · line 10.8 · offer 10.7 |
| b02-5 Story | line 6.0 · offer 6.1 · tag ink-soft 4.2 (3.9), 26 px Jost 500 (large text) · wordmark and name unchanged (5.8, 5.9) |

### Final renders (from `batches/b02`, `node ../../kit/render.cjs b02-5_feed.html b02-5_feed.jpg b02-5_story.html b02-5_story.jpg`)

```
{"out":"b02-5_feed.jpg","size":"1080x1350","failed":[],"overflow":[],"fallback":[],"textShare":0.079,"outside":[],"minFont":26}
{"out":"b02-5_story.jpg","size":"1080x1920","failed":[],"overflow":[],"fallback":[],"textShare":0.056,"outside":[],"minFont":26}
```

| File | Modified (UTC, `stat -c %y`) |
|---|---|
| b02-5_feed.jpg | 2026-11-19 19:12:07 |
| b02-5_story.jpg | 2026-11-19 19:12:07 |

These replace the 18:51:54 renders that the first critique scored. `b02-5.copy.json` → `review.scoredFiles` now points to them.

## Critique and verdict

Recorded on 19 Nov 2026 at about 19:20 UTC from the lead's computed results. The weights are PLAYBOOK §7: stop .15, message .10,
truth .15, layout .10, brand .05, copy .10, fit .05, desire .15, cues .15. The ship rule has five conditions:
- compliance passes with both critics;
- truth is 8 or more with both;
- no dimension is under 6;
- the ad beats the loser anchor with both;
- no skeptic refutation is left unanswered.

Nothing was generated, edited or re-rendered for this record. The ledger and learnings were not touched. The two rows are in
`rescue-ledger.json` for the lead to merge.

| Ad | Verdict | Weighted A / B (mean) | Lowest scores | Beats loser (A / B) | Beats winner (A / B) | Skeptic |
|---|---|---|---|---|---|---|
| b02-2 Brushed Gold Huggies, A13 | **reject** (round 1) | 6.55 / 7.10 (6.83) | desire 5 (A); truth 7 with both | yes / yes | no / no | **refuted** (metal tone; scale mis-logged) |
| b02-5 Verdant Eternity Band, A1 + size tag | **ship** (round 2, after fixes) | 7.30 / 7.75 (7.53) | 6 (A's desire) | yes / yes | no / no (round 1: yes / yes) | not refuted |

b02 now ships **2 of 5** (b02-1 and b02-5). Loop change 2 hoped for 3 of 5 if both rescues shipped, so that target is not met.

### b02-2 · Brushed Gold Huggies · A13 Suspended · reject

This ad was scored once, on the 18:51:53 Feed and 18:51:54 Story renders, at P 85 / T 497. It was rejected in the first round,
so there was no finisher pass and no second round. The final scores are the round-1 scores.

| Dimension (weight) | A, round 1 = final | B, round 1 = final |
|---|---|---|
| Stop power (.15) | 6 | 6 |
| One message (.10) | 6 | 7 |
| Truth and scale (.15) | **7** | **7** |
| Layout (.10) | 7 | 8 |
| Brand (.05) | 6 | 8 |
| Copy (.10) | 7 | 8 |
| Archetype fit (.05) | 7 | 7 |
| Desire (.15) | **5** | 6 |
| Purchase cues (.15) | 8 | 8 |
| **Weighted** | **6.55** | **7.10** |
| Compliance | pass | pass |
| Anchors (winner / loser) | `win_static_hoops_apricot` / `lose_sa08_walls` | `win_vkf18_prism_cluster` / `lose_sa08_walls` |
| Beats loser anchor | yes | yes |
| Beats winner anchor | no | no |
| Critic's verdict | reject | reject |

**Why it fails the ship rule.** Three things fail:
- truth is 7 with both critics (8 is needed);
- A scores desire 5 (6 is needed);
- the skeptic's refutation cannot be answered with copy.

All three come from the picture, so no layout or copy pass can lift them.
- **Metal (both critics).** The lower half of each huggie reads grey-green or khaki: saturation about 0.08–0.13 at hue 73–142
  (B and the skeptic). The pack shows an even, warm yellow brushed gold: hue 35–36, saturation 0.43–0.45. At phone size the pair reads as pale champagne
  over sage, right under a card line that says "18k gold tone". `products.md` already records this failure for the SKU
  ("reads silver").
- **Stop.** The pale pair sits on a pale ground, with a luminance contrast of only 1.06–1.21:1 (B). The sky is more
  saturated than the gold (A).
  - At 200 px it clearly beats the four-panel sa08 loser, and "₹699" is the most legible price on both sheets.
  - It loses to the apricot hoops (A) and to the prism cluster (B).
- **Idea.** The float is a faithful copy of board 96's levitation, but it proves nothing the headline says (A). A13's
  jasmine-bud referent is missing (B).
- **Desire.** The studio is cool, with no skin and no moment. "The ₹699 pair." over a pale piece makes it look cheap (A).
- **Brand (A 6).** No Velista, the gold is not warm-neutral, and the cool pastel ground breaks with the b01/b02 series.
- **Copy.** The beat "any three pieces, 20% off." repeats the offer box (both critics).

**Critics' fixes, kept for any re-brief.** None were applied, because the ad is rejected.
- A: change the beat to "brushed, not polished." (the PLAYBOOK A13 line). Cormorant italic 500, 60 px on the Feed and
  52 px on the Story, in oxblood, at the same tops (214 and 470). No "mirror".
- B: correct the logged scale (see below). Change the beat to "huggie earrings, about 14 mm.", and the Meta description to
  "Huggie earrings · about 14 mm" (29 characters).
- Both critics ask for a new picture:
  - a ground darker or warmer than gold (cocoa or oxblood);
  - a gold bounce named as the only light from below;
  - a bud on the floor as a size referent.

**Skeptic: refuted.** Measured on `pics/b02-2.png` (1536 × 2752) with PIL and cv2, using a sky mask of R − B > −25.

1. **Metal tone: fail.**
   - **The refs are one even yellow gold.**
     - Pack face: rgb(214,177,122), hue 36, saturation 0.43.
     - Macro: hue 33, saturation 0.47.
     - 0–1% of the refs' metal pixels have a hue over 55. On the macro, 79% of metal pixels are gold-like.
   - **The picture splits in two.**
     - Left top half: rgb(225,194,153), hue 34, saturation 0.32. Paler than the ref, but gold.
     - Left bottom half: rgb(169,174,151), hue 73, saturation 0.13.
     - Right lower band: rgb(159,168,150), hue 90, saturation 0.11.
   - **Share of metal pixels per huggie (left / right):**
     - hue over 55: 42% / 30%;
     - saturation under 0.20: 54% / 44%;
     - gold-like: 31% / 37%.
   - In the lower halves green is at least as strong as red (G ≥ R). No gold tone looks like that.
   - The Feed JPG gives the same figures, so the colour comes from the picture, not the render.
2. **Scale: the decision not to use a size tag rests on a wrong number.**
   - The huggie is 377–383 px tall on the source, not 338 px.
   - That is 265–269 px on the Feed and Story, so **18.9–19.3 px/mm** for the listed 14 mm. Using the size check's measured
     13.1–14.5 mm gives 18.3–20.6 px/mm.
   - That is about 1.2× life size and right at the 19 px/mm trigger, with no referent in the frame.
   - The same error produced the logged face aspect of 0.79. The true aspect is 273/378 = **0.72**, against 0.70 listed, so
     the shape passes.
   - The "Scale" bullet in the layout record above and the scale note in `b02-2.copy.json` still give 338 px and 17 px/mm.
     This section replaces them.
3. **Passes:**
   - zero stones;
   - the two huggies are identical;
   - soft brushed satin with fine vertical lines and one broad sheen, not mirror;
   - the inside of the band is hue 36, saturation 0.37.
4. **Unverified:** the right huggie shows a clicker post and a seam at the bottom. Neither ref shows the opening side, and the
   listing does not confirm a hinge. Not decisive.

- **Copy fix: not possible.**
  - The colour needs a new picture.
  - The scale flaw alone could be answered with copy: put the tag "SHOWN MAGNIFIED / ABOUT 14 MM TALL" on both formats and
    correct the notes.

### b02-5 · Verdant Eternity Band · A1 Product Card with size tag · ship

Round 1 scored the 18:51:54 renders. The finisher pass ("Fixes after the first critique", above) made four changes:
- moved the Feed card and size tag;
- reordered the card line;
- closed up the Story stack;
- lengthened the Meta headline.

The final scores are on the 19:12:07 renders, at P 100 / T 585.

| Dimension (weight) | A, round 1 | B, round 1 | A, final | B, final |
|---|---|---|---|---|
| Stop power (.15) | 8 | 8 | 8 | 8 |
| One message (.10) | 7 | 7 | 7 | 7 |
| Truth and scale (.15) | 8 | 9 | 9 | 9 |
| Layout (.10) | **6** | 7 | 7 | 8 |
| Brand (.05) | 7 | 8 | 7 | 8 |
| Copy (.10) | 6 | 7 | 7 | 7 |
| Archetype fit (.05) | 7 | 7 | 7 | 7 |
| Desire (.15) | 6 | 7 | 6 | 7 |
| Purchase cues (.15) | 7 | 8 | 7 | 8 |
| **Weighted** | **6.95** | **7.65** | **7.30** | **7.75** |
| Compliance | pass | pass | pass | pass |
| Anchors (winner / loser) | `win_static_hoops_apricot` / `lose_sa08_walls` | `win_vkf18_prism_cluster` / `lose_sa08_walls` | `win_e2_ruby_anaar` / `lose_w1_waterproof_wedding` | `win_w1_woven_red_story` / `lose_w1_waterproof_wedding` |
| Beats loser anchor | yes | yes | yes | yes |
| Beats winner anchor | yes | yes | no | no |
| Critic's verdict | ship-after-fixes | ship-after-fixes | ship | ship |

The mean was 7.30 in round 1 and is **7.53 final**. That is the highest mean of any ads-500 ad shipped so far: b01-1 7.45,
b02-1 7.35, b01-4 7.07. The lowest score is 6 (A's desire). Truth is 9 with both critics.

**What lifted it.**
- **Layout** rose from 6 to 7 (A) and from 7 to 8 (B):
  - the Feed tag now has 57 px of air under the prongs and 46 px over the wordmark;
  - the name and price share one row;
  - the Story tag clears the ring by 42 px.
- **Copy** rose from 6 to 7 (A): the card line now leads with fit.
- **Cues** held at 8 (B). "Band" in the Meta headline answers the risk that the open band reads as a cuff.
- **Truth** rose from 8 to 9 (A).

**What keeps it under the winner anchors in the final round.**
- **No honest surprise.** The pose is nearly the listing photo on a coloured sweep, so stop is 8, not 9.
- **Desire 6–7.** It is a studio packshot with no skin, no occasion and no styling. The saffron-and-green palette is its only
  warmth.
- **Ground too saturated.** The saffron (CIELAB chroma about 61) is more saturated than the stones (median 33). That goes
  against the rule that the piece is the most saturated thing in the frame (B).
- **Off-spec ground.** A1 asks for a dark ground with bone type; this is light saffron with ink type. Fit is 7 with both
  critics. Learnings rule 2 allows a saturated ground for green stones.
- **The anchor changed between rounds.** The better final layout lost to the anaar and to the W1 woven red Story, while
  the weaker round-1 layout had beaten the apricot hoops and the prism cluster.

**Remaining notes.** These are optional and were not applied. The ad ships as scored, on the 19:12:07 renders.
- **A, Story:** the offer box (456–518) and the tag (532–614) are two hairline boxes 14 px apart, and they read as one double
  box. Setting the Story tag frame to ink-soft at 2 px, as on the Feed, would separate them.
- **A, Meta primary text:** it ends flat on "Silver tone, and waterproof." An ending such as "Silver tone. Waterproof."
  keeps the text within 153 characters, with the offer still ending by character 124.
- **Both critics, picture placement:** the ring's top arc sits at Feed y 79, 5 px above the 84 gate, with T already at its
  maximum. The Story tag is 26 px, not the 30 px role. Neither can be fixed in layout.
- **Small size:** at 200 px the price is about 10 px tall, and without its name the open band could read as a cuff. "Band" in
  the Meta headline covers this.

**Skeptic: not refuted.** Measured on `pics/b02-5_try1.png` (1536 × 2752), with cv2 green-stone components compared against
`__upright.jpg` and `__cube.jpg`.

1. **Construction: nearly one-to-one with `__upright.jpg`.**
   - Seven front-arc ovals map in order onto the ref's.
   - They alternate either side of one scalloped clear-pavé S-wave about two stones wide. The wave has not flattened into a
     row.
   - Three to four back-arc ovals show through the opening.
   - Each front oval has 4 claws.
   - The open back ends in two looped tips with figure-8 holes and a gap.
2. **Stones.**
   - Oval, not round.
   - Emerald green, not teal: hue median 142, saturation 0.68. The refs give 150 / 0.64 and 146 / 0.58.
   - Proportion: the oval's long axis divided by the height of the green stones is 0.171, against the ref's 0.165 (+4%).
   - The green stones' width-to-height ratio is 0.69, against the ref's 0.75. The ring is turned about 8% further: a pose
     difference, not a construction change.
3. **Metal: silver tone holds.**
   - Interior metal has a median saturation of 0.17. The refs give 0.16 and 0.09.
   - 12% of the metal pixels are warm. They sit on edges and on surfaces facing the saffron floor, which is honest reflection.
     Nothing reads as gold.
4. **Scale and tag: the tag is true.**
   - Measured by the stones the ring is 21–24.5 px/mm, by the ring's outer size 26–28 px/mm, and by its height up to 35 px/mm.
   - That is 1.3–2.2× life size and over 19 px/mm on both formats, so "SHOWN MAGNIFIED" is true.
   - "ABOUT 16.5 MM INSIDE" is the listing's inner diameter word for word. It agrees with "adjustable US 5 to 9", which
     covers about 15.7–18.9 mm.

- **Caveat, kept.** The listing's 5 × 4 mm ovals do not fit the real photo's stone-to-ring ratio of 0.165.
  - No stone size in millimetres is printed anywhere in the ad or the copy (the finisher's scan above confirms it), so
    nothing conflicts.
  - Keep stone sizes in millimetres out of all copy.
- **For the lead.** The picture copies the listing photo's pose almost exactly.
  - That is good for truth.
  - It was generated (job a51af63b), so it passes RULINGS §1.2 as written.
  - Whether it reads as a re-shoot of the listing photo is the lead's call.

### Open items for the lead

- **Ledger:** merge `rescue-ledger.json` into `build/ledger.json`. It has one row per ad, each with `rescue: true`.
- **Stale notes in the copy files:**
  - `b02-2.copy.json` → `review.status` still says "not scored", and its scale note still says 17 px/mm.
  - `b02-5.copy.json` → `review.status` still describes the first critique.
  - This record did not edit either file.
- **Contact sheets:** `sheet.jpg` and `sheet_story.jpg` were rebuilt from the shipped b02 ads, b02-1 and b02-5.
- **`tmp/`:** deleted (the critics' blind sheets, keys and zooms). The `tmp/` paths cited in `verify.md` no longer
  resolve.

### What these two ads prove for later batches

The slid Feed crop (RULINGS §4, amended at 18:45) works: two pictures dropped for position alone were laid out at zero credits
with clean render logs and no type on either piece, and one shipped at 7.53, the best ads-500 mean so far, so position alone
should never again cost a regeneration; but the crop only picks the window, and it cannot fix colour, scale or headroom that
are in the picture (b02-5's top arc still sits 5 px over the gate at the maximum T, and b02-2's colour went into the reject
with it). The A13 float renders and reads at 200 px, and both critics put it clearly over the loser, but brushed gold over a
blue floor turned grey-green in both tries despite a "never" clause, so a later A13 needs a ground darker or warmer than gold
(cocoa or oxblood), a gold bounce as the only light from below, a referent on the floor, a headline the float proves, and scale
measured on the piece's full height (the 338 px misreading hid a size-tag trigger). A1 with a size tag is now a proven form for
a magnified product-only macro: a pose that follows the reference photo scores truth 9 with both critics, and an honest
"SHOWN MAGNIFIED / ABOUT X MM" tag carrying the listing's figure word for word (never a stone size in millimetres), with about
50 px of air on each side so it does not read as a twin of the offer box, makes 1.3–2.2× magnification cost no truth points;
its ceiling is surprise and desire (stop 8, desire 6–7), and because the same ad beat two winner anchors in round 1 but lost to
two others in the final round, later batches should fix each ad's winner anchor before scoring.
