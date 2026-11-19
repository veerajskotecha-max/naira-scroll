# b01 loop check (19 Nov 2026, about 16:55 UTC)

**What I looked at**
- At 200 px: `sheet.jpg` and `sheet_story.jpg`.
- At full size: both Feeds, the three dropped pictures (both tries) and the Woven references.
- The 14 anchors in `build/anchors/`.
- PLAYBOOK §3, §5.1–5.3 and §7.
- Board ranks 1, 3, 4, 26, 42, 55, 57, 66 and 96.

**What I read**
- `review.md`, `verify.md`, `learnings.md`, `ledger.json` and `jobs.json`.
- Both `copy.json` files, the page HTML and `kit/kit.css`.
- On Higgsfield (read-only, nothing generated): the balance, the transaction log, and a cost quote for `nano_banana_pro` and `nano_banana_2` at 9:16 2K.

**Better than the previous batch:** not applicable. b01 is the first ads-500 batch, so it sets the baseline:
- 2 of 5 shipped.
- The shipped mean is 7.26 (critic A 7.00, critic B 7.52).
- Against the tested anchors: both shipped ads beat the loser with both critics. Neither beat the winner with both critics; b01-4 beat F2 on stop power, with B only.

## Layer by layer

| Layer | Verdict | Evidence |
|---|---|---|
| Picture: identity | holds | The construction locks held on all 5 pictures. |
| Picture: placement and scale | change (3) | 3 of 5 were dropped. The model centred subjects at 37–62% whatever the prompt asked, and drew worn or referenced pieces at 1.27–1.6× true size. |
| Picture: colour ownership | holds, one note | b01-4's gold-tone mass owns its plum frame. b01-1's velvet riser is more saturated than the ring; that is allowed for a clear piece on a dark ground, but the ring is 31.8% of the width against the 35% rule. |
| Picture: surprise | change (3) | Nothing honestly surprising shipped. b01-1's beam is a faint smear, not the cone of board 3, and the A13 levitation was dropped. |
| Camera and light | change (5) | Both shipped ads use L1, a low tabletop camera (C3, C5), a dark jewel ground and no skin: one cold mood. The 3-light, 3-camera rule was met only through the dropped slots. |
| Layout | Feed holds; Story changes (4) | The Feed render gates are clean: minFont 26, `outside []`, textShare 0.126 and 0.173. b01-4's Story drops "BRAIDED HOOPS.", the headline that fixed the Feed's bangle misread, and has no offer, so on `sheet_story.jpg` the hoop reads as a braided bangle again. |
| Branding | holds; kit not updated (8) | One F2 card, a 56 px wordmark and one offer box on both ads. `kit/kit.css` still carries the 20 px `.offer small`. |
| Copy and Meta text | holds | First beats are truth-led and the claim is the second beat. The primary texts are 157–159 characters, with the offer ending by character 119. Meta headlines are ≤40 and descriptions ≤30 characters, with the value inside. |
| Offer | holds for b02 | The verified BUY2 / BUY3 value is on both ads. A NAIRA10 test is queued at the end of this file. |
| Product mix and stock | change (7) | Only Cushion (45 units) and Woven (89) shipped: no ₹699 piece and no bundle line. Woven reaches its phase-1 cap of 2 (PLAYBOOK §5.1) with b02's new move. |
| Prompting | change (3) | Placement asked as frame percentages fails. Physical geometry and a described result work (b01-4 try 2). |
| Process | change (1, 9) | The credit cost was mis-measured. The critics scored pre-fix renders, one weighted score was mis-added, and the truth floor was left to the lead. |

## Changes for b02

### 1. Count credits from the transaction log, at 2 credits a picture, and plan against an account someone else is draining

**The finding: b01 cost 2 credits a picture, not 4.** These three records are wrong:
- `learnings.md` ("Budget: 4 credits a picture, not 2");
- `review.md` (prompting learning 7);
- `verify.md` ("about 3.6").

The Higgsfield transaction log shows b01's ten jobs at 2 credits each, 20 in all:
- the five first tries at 15:55:40–42 UTC;
- the five second tries at 16:18:34–16:20:19.

Both sets match the jobs' file timestamps. The "182.46 after" read also included five jobs that another session submitted at 16:26:02–04. A quote today for `nano_banana_pro` and for `nano_banana_2` at 9:16 2K is 2 credits each.

**Someone else is spending on the account.** Since 16:26, another session has spent about 98 credits in about 27 minutes. The balance at this check was **94.46**. That same outside spending explains the verifier's "2.46, production has to stop" read.

**How**
- The generator writes `submitted_at` and `credits` for every job into `jobs.json`, taken from the `transactions` rows at those timestamps.
- The learnings agent corrects the three budget lines.
- The balance is read once, immediately before the single `generate_image_batch` call.
- Reserve 2 credits per slot for its one regeneration, plus the 10-credit floor.
- If (balance − 10) is less than 4 × the number of slots, cut slots. Keep the worn Woven new move first, then the other worn slots.
- The lead tells the owner about the outside spending. If it continues at that rate, it reaches the floor within about 25 minutes, with or without b02.

**Test:** the credits in b02's `jobs.json` add up to its own transaction rows. The b02 brief's pre-flight shows the time of the balance read, the reserve and any slot cut.

### 2. Fix target is desire: ship at least 2 worn frames (brief 3), with the worn Woven ear crop as the one new move

Adopt the learnings' "Fix target for b02" and "One new move for b02" exactly as written:
- an ear-and-jaw crop with no eyes and the pair visible;
- b01-4's on-image copy, card and offer unchanged, so only the picture changes;
- a named skin tone with texture;
- one wedding-season detail in the picture.

Add one constraint: this ad is Woven's second phase-1 ad, so b03–b10 brief no more Woven unless its first ads unlock more slots (§5.1).

**Test:**
- At least 2 worn ads ship.
- Each key detail is at least 15% of the frame width and at most 1.2× true size by a pixel ruler, logged in `verify.md`.

### 3. One composition template for every slot, built around the model's centring; light described by its visible result

The learnings give the bands for worn frames only. The product-only slots failed the same way:
- b01-2's shadows and bud landed at 57.5–69%;
- b01-4's first try ran from 29% to 69%.

**How**
- **Subject band.** Every prompt places the subject's whole extent (the piece, its shadow and any referent) at **36–61% of the 9:16 frame height**. That is Feed y 404–888 and Story y 689–1173.
- **Placement in the prompt.** State placement as physical geometry: camera height, which edge crops what, and which way the fingers point. Never rely on "nothing below X%" alone.
- **Fixed text bands for every ad:**
  - Feed headline, beat and size tag: y 84–370.
  - Feed card: top at 930–950, ending by 1258.
  - Story: all text inside y 270–650.
- **Scale.** Keep the learnings' order: a ratio inside the piece first, then one body ratio for worn pieces.
- **Light.** Describe light by its visible result, as the camera already is. For any A6, ask for "a thin haze in the air so the beam shows as a sharp-edged cone from the top right, ending in a hard-edged pool of light on the riser". b01-1's beam came out as a smear, with a mean luminance of 29, and board 3's surprise was lost.
- **Verifier.** The verifier measures the subject's extent first and drops any picture whose subject runs outside 35–62%, before any other check.

**Test:** `verify.md` lists each picture's measured extent, and every render reports `outside []`.

### 4. The product type and the purchase cues read at 200 px in both placements; fix b01-4's Story now

**Earrings.** Earrings are shown as a **pair, upright or worn**, never as one flat hoop. Every Woven ad that sold on our account (W1 texture, Apricot) shows the upright pair. b01-4's headline patch fixed the Feed but not the Story. Every earring prompt says "the pair, both standing upright (or worn), the opening visible", and the acceptance list rejects a single or flat earring.

**Story twins.** From b02, every Story carries:
- the Feed's headline, when the Feed has one;
- the product name;
- the price;
- the 26 px offer line, all inside y 270–650.

A no-text Story (the A6 spec, and our anaar Story winner) is used only where the picture alone names the product at 200 px, as b01-1's ring on its riser does. That Story stays as it is.

**Before b02 (zero credits): re-render `b01-4_story.jpg`.** Add:
- "BRAIDED HOOPS. / ZERO STONES." in Velista 76–92 px;
- the name and ₹1,049;
- the one-line offer.

All of it goes above the hoop, which starts at y 709, inside 270–650.

**Test:**
- On the 200 px Story sheet, a reviewer names every product without reading small type.
- Every Story with text reports `outside []` and minFont 26.

### 5. Variety is counted on what ships, not on what is briefed

**How**
- **Lights.** The five b02 slots use **five different lights** from L1–L7, with L7 at most once, so whatever ships keeps at least 3.
- **Cameras.** At least 3 different cameras across the batch. The worn slots are not all C4: one can be C6 (phone POV or mirror) or C2 (low hero) for the ear.
- **Grounds.** At most one hard spot on a dark ground. At least two slots go on a light or flat saturated ground (sky, cobalt, saffron, apricot silk). These are the grounds of three of our five tested winners (Apricot, anaar, VK F18) and of boards 26 and 42.
- **Pose.** A gold-tone piece on such a ground is tilted 10–35° and cropped by one edge, as in A4.

**Test:** the ledger's light, camera and ground fields for b02's shipped ads.

### 6. One ₹699 slot, a fresh stock read, and no zero-headroom SKUs

**₹699 slot.** b01 shipped no ₹699 piece and no bundle line, which is the second half of gap 5. Brushed (58 units) was dropped on scale and centring, not on its idea.

**How**
- **Brushed slot.** b02 carries one Brushed slot, product-only, built on the template in change 3:
  - the upright pair at about 40% of the width;
  - a size tag if it renders over 19 px/mm;
  - the bundle value in the second beat or the headline, for example "BUY3 · 20% OFF" against ₹699.
  - It is a natural home for one of change 5's light grounds.
- **Stock read.** Re-read stock and price from Shopify for the b02 brief. b01's brief reused the 15:25 RULINGS read.
- **Zero-headroom SKUs.** Leave out Serpentine (gold) and Bold Nocturne. Both sit at exactly 20 with zero headroom, and one sale drops them out mid-flight.
- **New SKUs.** Include at least 3 SKUs that b01 did not ship.

**Test:** the b02 brief's pre-flight carries a timestamped Shopify read, and one Brushed ad ships.

### 7. Make the one-line offer the kit default

`kit/kit.css` line 46 still defines `.offer small` at 20 px, below the 26 px floor. The kit has no separator, so b01's pages each re-declared it inline.

**How**
- Delete line 46.
- Add the separator rule from `b01-4_feed.html` to the kit:
  `.offer .sep { display: inline-block; width: 9px; height: 9px; background: var(--gold-light); transform: rotate(45deg); vertical-align: middle; margin: -4px 20px 0 14px; }`
- b02 pages use the class, with no inline offer CSS.

**Test:**
- `grep -c 'offer small' kit/kit.css` returns 0.
- Every b02 render reports minFont 26 or more.

### 8. Score the file that ships, compute the weights by script, and apply the truth floor to each critic

**What went wrong in b01**
- The critics scored the pre-fix renders, and nobody re-scored. The ledger's b01-4 critic-A score (6.60, truth 6) belongs to a version A said it would reject.
- B's stated 7.70 for b01-1 is 7.50 under the §7 weights.
- The verifier's first pass passed b01-1 without testing band ÷ stone. Only the skeptic caught the 1.28–1.40× head, so that check depended on one pass.
- The truth floor was handed to the lead as "hold b01-4 if…".

**How**
- After the finisher's fixes, each critic scores the final Feed and Story JPGs at full size and at 200 px.
- A script computes the weighted means from the dimension scores and the §7 weights.
- The 8+ truth floor applies to each critic's score.
- `review.md` and `ledger.json` name the scored file and its modification time.
- The verifier's first pass logs one ratio inside each piece (for a ring, band ÷ stone), as the skeptic did.

**Now, for b01-4:** critic A re-scores the final render once (zero credits). If A's truth stays under 8, b01-4 is held, and the b02 worn Woven ad is read against W1 "Woven, not cast" instead.

**Test:**
- Every b02 ledger entry carries `scoredFile`.
- Its weighted values reproduce from the script.

## Queued for b03, not b02

The one-new-move rule keeps this out of b02, so that the worn Woven picture stays the only variable.

- **The finding.** NAIRA10 gives 10% off any order with no minimum (RULINGS §2). So "BUY2 · 10% OFF" asks the viewer to buy a second piece for a discount one piece already gets.
- **The test.** `CODE NAIRA10 · 10% OFF ◆ BUY3 · 20% OFF` on single-product ads, as b03's new move.
- **Meta fields.** The Meta headline becomes `<Name> · ₹<price> · 10% off` (no condition to cut at 40 characters), and the primary text names NAIRA10 by character 125.

## Trend

`ledger.json` holds one batch, so there is no trend yet:
- b01 shipped 2 of 5;
- b01-1 scored 7.45 and b01-4 7.06, a mean of 7.26.

b02 is better only if:
- it ships at least 3 of 5;
- its desire mean rises above 6.75;
- at least one ad beats the winner anchor with both critics.
