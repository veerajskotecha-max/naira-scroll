# b02 loop check (19 Nov 2026, about 18:40 UTC)

**What I looked at**
- At 200 px: `sheet.jpg` and `sheet_story.jpg` for b02, and `batches/b01/sheet.jpg`.
- At full size: all ten b02 pictures in `pics/` (both tries of every slot), with the Feed crop simulated at several offsets.
- Our five tested winners in `build/anchors/`, and board ranks 1, 3, 4, 26, 42, 55, 57, 66 and 96.

**What I read**
- b02: `review.md`, `verify.md`, `brief.md`, `jobs.json`, `b02-1.copy.json` and both b02-1 pages.
- b01: `review.md`, `loop.md` and the b01-1 and b01-4 Feed pages.
- `build/learnings.md`, `build/ledger.json`, `build/study/products.md`, `RULINGS.md`, and PLAYBOOK §4.0, A1–A5 and §5.2–5.3.
- On Higgsfield (read-only, nothing generated): the balance and the transaction log.

**Better than the previous batch:** not better.
- **Ads shipped:** 1 of 5, against b01's 2 of 5. With b01-4 now held, that is 1 against 1.
- **Shipped mean:** 7.35, against 7.26. That is no real lift on one ad.
- **The batch's own success test:** it fails 3 of its 4 counts.
- **Stop power:** it fell from 7.63 to 7.00, and that is the dimension where every winner anchor beats us.
- **No ad beat the winner anchor** with either critic.
- **One ad is better:** b02-1 is a better Woven ad than b01-4. Truth is 8 with both critics, desire is 7.0, and the product type now reads at 200 px.

## Layer by layer

| Layer | Verdict | Evidence |
|---|---|---|
| Picture: subject and scale | change (3, 4) | Worn pictures passed 1 of 10 over two batches. Product-only pictures shipped 2 of 10, and 2 more (b02-2 try 2, b02-5 try 1) passed truth but failed only on position. b02-1's hoops are each 13% of the width, at the frame edges. |
| Picture: colour ownership | holds as written | b02-1 puts gold on a same-hue apricot ground, so the hair lands first at 200 px. The learnings' b03 fix target already bans same-hue grounds. |
| Picture: surprise | change (4) | No honest surprise has shipped in two batches. b02-2 try 2 did render a clean float with detached shadows (a real A13). It was dropped only because of the crop. |
| Camera | holds | Camera-behind (C2) was the first worn geometry to hold no-face and true scale, but only for a piece that hangs below the lobe (change 3). |
| Light | change (4) | The L5 bloom, the L3 rim and b01's A6 cone did not render as asked. Shipped lights so far: L1, L1 and a soft key logged as L7. |
| Layout | change (1, 5) | In five of the seven dropped slots, at least one try had its subject or shadow under the fixed card (Feed 940) in the fixed central crop. b02-1's beat is 0.52 times the headline, under the §4.0 floor of 0.6. |
| Branding | holds | One card, the 56 px wordmark and one offer line. Ink on skin worked on the nape. |
| Copy and Meta text | holds, except the beat size (5) | The first beat is a listing truth and the claim is the second beat. The Meta headline is 37 characters and the description 30, with the value inside. The primary text is 157 characters, with the offer by character 119. |
| Offer | holds | BUY2 and BUY3 are verified and the box now says CODES. NAIRA10 stays queued. b01-1 still prints `CODE` (6). |
| Product mix and stock | change (4) | Over two batches only Cushion and Woven have shipped. Prism, Verdant Eternity and Brushed have each failed 4 pictures, and the Circlet 2. Five in-stock SKUs have never been briefed. |
| Prompting | change (1, 3) | Placement percentages never moved the subject, and subjects grew 1.3–1.75 times. The b03 new move, as the learnings write it, cannot meet its own size bar (3). |
| Process | change (2, 4, 6) | **Re-score:** the critics again scored the pre-fix renders (18:15:10), and nobody re-scored after the fixes. b01 loop change 8 is not met. **Ledger:** b01-4 is still marked "ship" there. **Lost credits:** b02-5's regeneration spent 2 credits on a pose change that the crop rule forced, and that change broke the S-wave. **Credits now:** 28.46 is enough for one batch (4). |

## Changes for b03

### 1. Slide the Feed crop to fit the picture, and stop asking the model for a position

**The finding**
- The model centres the subject whatever the prompt asks: 6 of 8 placement asks in b01, and every try in b02.
- The Feed is the fixed central 4:5 crop, and the card is fixed at Feed 940. Together they dropped these pictures, which were good on truth:
  - b02-2 try 2: shadows at 68.9–71.6%;
  - b02-5 try 1: the ring at 34.5–71.3%.
- They also pushed b02-5's regeneration into a new pose, which flattened the S-wave.
- The skeptic already found that b02-2 try 2 works with the crop moved down. The rescue was not taken, because RULINGS §4 says "the central crop".

**How**
- **The ruling.** The lead amends RULINGS §4. The Feed may be any 4:5 window of the 9:16 picture, at the same scale, set by `.pic { object-position: 50% P% }` with P from 0 to 100 and chosen for each picture.
  - Nothing in the picture is scaled, moved or edited.
  - The Story stays the native frame.
- **Coordinates.** The source is 1536 × 2752, shown at 1080 × 1935. The window top is T = 5.85 × P px (0 to 585), and Feed y = src_y × 0.703125 − T.
- **The verifier's placement gate.** This replaces "drop anything outside 35–62%".
  - Measure the subject's full extent: the piece, its shadow and any referent.
  - **Headline plus card:** the picture passes if some T puts that extent inside Feed y 380–930. That is a span of at most 550 Feed px, about 28% of the frame height.
  - **Card only (A1):** the extent must fit inside Feed y 84–930. That is 846 px, about 44% of the frame height.
  - Log the extent, T and P in `verify.md`.
- **Prompts.** Prompts stop giving positions as percentages.
  - Ask for "centred in the frame".
  - Give the size as a share of the frame **height**, at about 0.7 times the share wanted. Subjects grew 1.3–1.75 times in both batches.

**Test**
- Every b03 Feed HTML sets its P.
- `verify.md` logs each picture's extent, T and P.
- Every render reports `outside []`.
- No b03 slot is dropped, and none is regenerated, for position alone.

### 2. Before b03, lay out the two b02 pictures that pass truth and failed only the crop (zero credits)

**b02-2 try 2** (`pics/b02-2.png`, job `6e938236`)
- **Crop:** P 80 (T 468). The skeptic's fit:
  - huggies at Feed 365–624 and shadows at 866–919;
  - headline 104–215 and beat 226–290;
  - the card at 940, on plain floor.
- **Copy and Story:** use the brief's b02-2 copy and Story unchanged. The Story already fits: the huggies sit at Story y 824–1083.
- **Notes for critic B:**
  - the lower halves of both huggies go grey-green (saturation 0.07–0.12);
  - the pair spans 49% of the width (the rule asks at least 35%);
  - the scale is 17 px/mm, so no size tag.
- **If it ships, these go live for the first time:** a ₹699 ad, a bundle line ("any three pieces, 20% off.") and an honest surprise.

**b02-5 try 1** (`pics/b02-5_try1.png`, job `a51af63b`)
- **Crop:** the ring needs T of at least 450 to clear the card. At P 100 (T 585) it sits at Feed 83–795.
- **Size tag:** the ring is about 24 px/mm, over the 19 px/mm trigger, so it needs the tag. The tag goes at about 805–925, and the card at 940.
- **Archetype:** no headline fits, so it ships as **A1 Product Card**, not the A5 numeral. The card line is "emerald-green cubic zirconia · adjustable US 5 to 9". Log the archetype change in the ledger.
- **Story:** the ring sits at Story y 660–1373, so the Story text ends by y 630.
- **Why it is worth it:** the construction matched the upright reference (the verifier's own words). Green on saffron also gives the piece the frame's strongest colour contrast.

**Both ads:** each goes to both critics under the normal ship rule, which means truth 8 or more with each critic and a win over the loser anchor, at full size and at 200 px.

**Test**
- The b02-2 and b02-5 ledger rows carry a new verdict and a `scoredFile`.
- If both ship, b02 becomes 3 of 5.

### 3. Replace the b03 new move: a single-ear Circlet frame cannot meet its own bar

**The arithmetic**
- `learnings.md` asks for a back three-quarter view of one ear about 12 cm across, putting "the piece at about 18–21% of the width", first on the Verdant Circlet.
- The Circlet is 16.8 mm tall (`products.md`). At 12 cm that is 14% by height, and less by width. The 21% figure holds only for the 25 mm Woven hoop.

**The geometry**
- A stud faces out from the outer side of the lobe. From about 45° behind the side view, its face turns about 60° away from the camera and shows at roughly half its width.
- A hoop hangs below the lobe and stays visible from behind. That is why b02-1 worked.
- The record backs this up: worn studs went 0 of 2 in b02, with the eye showing both times, and worn frames overall went 1 of 10.

**The new move instead: replicate the one candidate note (gold-tone mass on a saturated dark ground, A4 Monument) on Brushed Gold Huggies** (58 units, ₹699)
- **Why this:** b01-4 gave the best stop power of the two batches. It beat F2 on stop power with critic B, and it is the only note waiting for a second win.
- **Picture:**
  - the pair stands upright on a deep oxblood or plum glaze, and it is the only gold in the frame;
  - use b01-4's low camera, described by its result ("about 8°, a long low flat ellipse a third as tall as it is wide");
  - each huggie is about 30% of the Feed width, so the upright pair stays under the 550 px band from change 1;
  - no blue or yellow anywhere near the satin, because both turned it grey-green or silver in b02 and in QUIET.
- **Copy:** "BRUSHED, / NOT POLISHED." (listing words, PLAYBOOK A4), with the size tag.
- **What decides it:** a win over the winner anchor with both critics makes it the first ads-500 rule. A loss retires the note.

**What happens to the camera-behind single-ear idea:** it waits for a hanging piece of 22 mm or more. That means Woven once it unlocks, or Bold Nocturne once its stock is above 20.

**Test**
- The b03 brief names this move.
- `verify.md` logs each huggie's share of the Feed width.
- The review states the candidate note's outcome as promoted or retired.

### 4. Spend the last 9 pictures on the slots most likely to pass

**Credits**
- The balance read **28.46 at 18:36 UTC**. It has not moved since b02's last job at 18:03, so there was no outside spending in that half hour.
- Staying at or above the 10-credit floor allows **9 pictures**.
- b01's reserve rule (2 credits per slot for its regeneration) would give 4 slots, 8 pictures, and leave 1 picture that no later batch could use.
- No b04 can run unless the owner adds credits.

**How**
- **Pictures.** b03 is **5 slots and 9 pictures**:
  - the five first tries go in one `generate_image_batch` call;
  - then at most 4 regenerations, given only to slots whose first try failed on size or position;
  - never regenerate a slot whose piece morphed: in b02-3 and b02-5 the morph came back on the second try.
- **Balance check.** Re-read the balance right before the call. If it is under 28, make (balance − 10) ÷ 2 pictures, cutting regenerations first.
- **Product-only slots.** At least 4 of the 5 slots are product-only, with the piece at 35% or more of the Feed width. At most 1 slot is worn.
- **Never-briefed SKUs.** At least 2 slots go to in-stock SKUs that ads-500 has never briefed, chosen for simple rigid shapes:
  - Halo Curve (29);
  - Pearl Double Halo (25; no claims, no water);
  - Monochrome (24; no claims, no water);
  - Serpentine Silver (23).
- **Left out:** no worn Prism and no worn Circlet in b03 (both failed both tries in b02). Toggle stays out until a slot carries its clasp lock.
- **The crazy slot.** Its surprise must be one the model has already rendered (the float with detached shadows, or selective colour), or it must live in the type (A7 split headline around a centred piece, board 55). Never a described light effect.

**Test**
- `jobs.json` lists 9 jobs or fewer, adding up to 18 credits or fewer in the transaction rows.
- The ledger shows at least 4 product-only slots and at least 2 new handles.

### 5. The second beat is at least 0.6 times the headline (PLAYBOOK §4.0); fix b02-1 now

**The finding**
- b02-1's Feed sets a Velista 92 headline over a 48 px beat. That is 0.52 times the headline; §4.0 asks for 0.6 to 1.0.
- At 200 px, "and yes, waterproof." is about 9 px tall. The proof beat that rule 8 relies on is invisible in the Feed (critic A).
- b01-4 had the same 92 and 48. A's 56 px fix was left out as "one critic only", although the playbook already requires it.

**How**
- **Now:** in `b02-1_feed.html`, set `.beat` to 56 px (0.61 times the headline) and keep it centred at top 290–296, on the hair (x 112–980). Re-render and confirm `outside []` and minFont 26.
- **From b03:** the finisher logs H1 px, beat px and their ratio in each `copy.json` `layout`. A ratio under 0.6 is a fail, like a font fallback.

**Test:** the `.beat` and `.h1` font sizes in every b03 Feed HTML give a ratio of 0.6 or more.

### 6. Score the file that ships, and correct the records before b03

**The finding**
- b01's loop change 8 is still not met. The b02 critics scored the 18:15:10 renders. The finisher then changed the letter-spacing, the offer label and the Story stack, and nobody re-scored.
- The ledger still says b01-4 "ship", although `review.md` holds it.
- b01-1 still prints `CODE` before two codes.

**How**
- **Order for b03:**
  1. The finisher applies the fixes.
  2. Both critics score the final Feed and Story JPGs.
  3. If a critic's change is applied, both critics re-score that ad once.
- **The ledger:** `scoredFile` names the final JPG and its modification time.
- **Now, at zero credits:**
  - both critics re-score b02-1 after change 5, and the two layouts from change 2, on the final JPGs;
  - the lead sets b01-4's ledger verdict to "held (critic A truth 6 on re-score, under the 8 floor)";
  - the lead re-renders `b01-1_feed.jpg` with `Codes BUY2 · 10% off ◆ BUY3 · 20% off`.

**Test**
- For every ledger row marked ship, the `scoredFile` time equals the Feed JPG's `stat -c %y`.
- `grep -l '>Code BUY2' batches/*/b0*_feed.html` returns nothing.
- b01-4's verdict begins with "held".

## Trend

From the scores in `ledger.json`:

| Batch | Shipped | Ad scores (mean of both critics) | Batch mean |
|---|---|---|---|
| b01 | 2 of 5 | b01-1 7.45 · b01-4 7.07 | 7.26 |
| b02 | 1 of 5 | b02-1 7.35 | 7.35 |

- With b01-4 held, b01's live mean is 7.45, so the shipped mean is flat at about 7.3–7.45.
- Yield is flat or falling.
- No ad has beaten the winner anchor with both critics in either batch.
- Truth and desire per ad are rising; stop power is falling.

Changes 1 and 2 are where the next gain comes from. They add yield without spending a credit.
