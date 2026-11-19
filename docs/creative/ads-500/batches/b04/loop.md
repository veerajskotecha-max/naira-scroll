# b04 loop check (19 Nov 2026, about 23:30 UTC)

**What I looked at**
- At 200 px: `b04/sheet.jpg` and `b04/sheet_story.jpg`, `b03/sheet.jpg`, a 200 px sheet of the 8 newest live Feeds beside every
  anchor in `build/anchors/` (4 winners, 6 losers), and board ranks 1, 3, 4, 26, 42, 55, 57, 66 and 96.
- At full size: the b04-1 Story (the chin band), the b04-3 and b04-4 Feeds, and the refs for Toggle (clasp), Verdant Circlet
  (pack), Serpentine Silver (plinth, detail) and Monochrome (pack). The dropped b02-4 Prism pictures (`b02/pics/b02-4*.png`).

**What I read**
- b04: `review.md` (all of it), `verify.md` (verdicts, skeptic notes and prompting learnings), `brief.md` §0, §1, §4 and the
  unshot slots b04-5 and b04-7, `jobs.json`, the four `copy.json`, the page sources.
- `build/learnings.md` (including the b04 notes and the rule 11 promotion), `build/ledger.json`, `build/meta_upload.csv`,
  `build/study/meta-results.md` (the live winners), `build/study/products.md`, `RULINGS.md`, PLAYBOOK §5.3, `b03/loop.md`.

**Checks run (read-only)**
- All five b03 loop changes were done and pass their own tests: no `>Code BUY2` left in any Feed; b02-1's beat is 56 px; the
  ledger verdicts read b01-4 "held", b02-2 "reject", b02-5 "ship"; every one of the 11 ship rows has a `scoredFile` and
  `scoredStory` equal to the JPGs' `stat -c %y`; `b04/review.md` has no "re-score still due"; each b04 job was submitted after
  the previous verdict; the b03-4 rescue (b04-0) has two critic scores.
- b04 copy and pages: no banned word, no compare-at price, no shipping line, no claim on Monochrome or Toggle, no water in any
  picture, no signed URL. Every live Story except the b01-1 control and b04-1 prints the offer.
- Balance 0.46 (review shooting log). Generation has stopped under RULINGS §1.3; every change below that needs a picture waits
  for the owner's credits.

## Better than the previous batch: yes, narrowly

It met its own fix target, shipped the run's first honest surprise and widened what is live. The ads are not better on average,
and the headline claim "three ads beat the winner" does not hold up (change 1).

**Better**
- **Desire, the fix target: 6.94 → 7.38**, the largest move of any dimension. Every shipped ad is 7 or more with both critics.
  Skin (b04-1, B desire 8) and an occasion beat (b04-3, B 8) did it.
- **Stop power: 7.69 → 7.88.** b04-3 has B's 9; b04-0 has 8.5 with both.
- **The first honest surprise shipped** after 0 for 15: the b04-0 float, at zero credits, from a b03 picture.
- **The first worn frame since b02** (b04-1), with scale locked at 1.07× by link counts and ring widths.
- **Range:** four SKUs that had no live ad now have one, including Toggle, the deepest stock (77) and never briefed before.
  Construction held on 7 of 7 pictures (14 of 14 over b03 and b04).
- **Process:** every score is on the shipping file, for the first time in four batches; both regenerations aimed at a single
  measured fault passed (b04-1 scale, b04-4 chain path).

**Level**
- **Mean of the shipped ads 7.747 against b03's final 7.754.** Four ads each.
- **Credits per live ad: 3.5 in both** (14 credits for 4 ads), but b04 needed the zero-credit b04-0 to get there.

**Worse**
- **Best ad:** b04-3 at 7.91, under b03-1 (7.99) and b03-2 (7.96).
- **Picture yield:** 3 ads from 7 new pictures (43%), against 4 from 7 (57%). b04-2 Prism spent 4 credits on two different
  scene faults.
- **Archetype fit 7.69 → 7.38** (B 6.5 on b04-4) and **purchase cues 8.25 → 7.88**: both devices the model was asked to draw
  (the drained world, the warm spot) did not read, and the b04-1 Story has no offer.
- **Copy 7.56 → 7.44, truth 8.31 → 8.19.** "One bold ear is enough" over a pair reads as "wear one"; b04-0's primary text is
  ungrammatical; truth sits at the 8 floor on b04-3 and b04-4.

**Not a real gain: "three ads beat the winner with both critics, the first time in four batches."**
- b04's blind Feed sheets carried two winners (apricot hoops and vkf18) and counted a win over either. PLAYBOOK §5.3.3 asks for
  one winner and one loser per sheet.
- Every win a critic named was over vkf18 (review lines 24–25). No ad beat F2 or the apricot hoops with both critics. A says
  b04-0 "matches the apricot hoops on stop but loses to them on desire" and b04-1 "does not beat F2 or the apricot hoops".
- b03-1 and b03-2 flipped from one critic to both on re-scores that moved only +0.17 and +0.05, once vkf18 was on the sheet.
  The ads did not change much. The anchor did.
- Against the anchor b03 used (apricot alone), b03 and b04 both have **0** ads that beat the winner with both critics.

## Changes for the next run (when credits are added)

Changes 1–4 cost no credits and can run before the top-up. Changes 5–7 are the first pictures, in rank order, one at a time
as in b04. Change 8 governs the brief that orders them.

### 1. Make "beats the winner" one test again, and re-test rule 11 on it (zero credits; before any picture)

**The finding**
- The anchor change above made b04's "3 of 4 beat the winner" a different measure from b03's "0 of 4".
- Rule 11 (the magnified product-only hero) was promoted on "two batches" that are one scoring session against one anchor:
  b03-1 and b03-2 on their b04 re-scores, plus b04-0 and b04-3, all beating vkf18.
- As written, rule 11 also contradicts our live evidence. It asks a product-only frame for "the piece the largest and
  brightest shape … on a ground darker than the piece". Three of the five live winners (apricot hoops, anaar bracelet, vkf18)
  are product-only rhymes on light warm grounds, where the prop is larger or more colourful than the piece. b03 loop change 5
  allowed exactly that for A3.

**How**
- **Ledger.** `beatsWinnerBy` becomes a map keyed by anchor file, for example
  `{"win_static_hoops_apricot": ["A"], "win_vkf18_prism_cluster": ["A", "B"]}`. The review reports the share of ads beating each
  anchor (PLAYBOOK §5.3.4).
- **Re-score now, at zero credits.** Both critics read the 11 live Feeds blind at 200 px on two sheets:
  - sheet 1: `win_static_hoops_apricot` with `lose_p2_proof_parody`;
  - sheet 2: `win_twenty_f2_tennis_ruby` with `lose_sa08_walls` (named in the b04 brief, never used).
- **Rule 11.** Back to "note (provisional)" unless ads from two different batches beat apricot or F2 with both critics on those
  sheets. In either case, add its scope: "lone-product frames (A1, A4, A6) only; an A3 rhyme follows b03 loop change 5: a light
  warm ground when the prop owns the colour, and the prop may be larger than the piece".
- **From the next batch on:** each blind sheet carries exactly one winner and one loser, rotated.

**Test**
- Every live ledger row has `beatsWinnerBy` keyed by anchor file names, with entries for apricot and F2.
- `learnings.md` rule 11 carries a status that matches the re-score, and its text contains "A3".
- Every next-batch sheet's file list contains exactly one `win_` file.

### 2. Bring the launch hand-off in line with the files that ship (zero credits)

**The finding**
- `build/meta_upload.csv` (20:35) has 7 rows: **none of the four b04 ads**.
- Its b03-1 row still carries the pre-fix Meta text. The CSV primary text names "Brushed Gold Huggies … brushed-satin 18k
  gold tone" and the description "Brushed satin · 18k gold tone". The final `copy.json` says "₹699 huggie earrings … soft satin
  18k gold tone PVD" and "Huggie earrings · gold tone". Both critics asked for the type to be named because "Huggies" alone reads
  as the nappy brand.
- Its `score_mean` column holds pre-re-score values: b01-1 7.45, b02-1 7.35, b03-1 7.82 and b03-2 7.92, against the ledger's
  7.53, 7.49, 7.99 and 7.96.
- Three `copy.json` review blocks are stale:
  - `b04-1.copy.json` line 129 still calls the 22:58 Feed "not yet scored", with mean 7.675 (final 7.725);
  - `b03-1.copy.json` lines 180–181 say the same, with mean 7.82 (final 7.99);
  - `b03-2.copy.json` keeps 7.91 and "beats winner: B only" (final 7.96, both).

**How**
- Rebuild the CSV from the ship rows of `ledger.json` and each row's `copy.json` `meta`: 11 rows.
- In those three `copy.json`, add a `final` review block (round 2 or re-score values, scored files, `beatsWinnerBy` after change
  1). Mark the old blocks superseded and do not delete them.

**Test**
- The CSV has exactly the 11 ship ids.
- Each row's primary text, headline and description equal its `copy.json` `meta`.
- `score_mean` equals the ledger's (A + B) ÷ 2 to 2 decimals.
- Each ship row's `copy.json` `final.mean` equals the ledger's mean.

### 3. An offer in every Story: b04-1 first (zero credits)

**The finding**
- The b04-1 Story is the only live Story with a name and price but no offer. That is B's cues 7, the lowest cue in the batch,
  and the main reason purchase cues fell (8.25 → 7.88).
- B tested a line that fits: x 268–811, y 640–701, at least 60 px clear of both strands, on the plum fill. The kit's two-code
  box (726 px) does not fit between the strands.

**How**
- Add B's tested line "Code BUY2 · 10% off 2 pieces" to `b04-1_story.html` at top 640. It matches the Meta headline ("10% off
  2") and the primary text.
- Re-render with `node ../../kit/render.cjs`. Both critics re-score the Story only, then update `scoredStory`.
- Next brief: every Story prints an offer, except a control that is named as one (b01-1).

**Test**
- The render reports `failed`, `overflow`, `fallback` and `outside` empty, with minFont 26 or more.
- B's cues on b04-1 are 7.5 or more, and A's do not fall.
- Every live `*_story.html` except b01-1's contains `class="offer"`.

### 4. Headline arms built from the listings' own lines (zero credits; live A/B with the current ads as controls)

**The finding**
- Copy fell to 7.44. The b04 first beats are:
  - a mechanism ("Turn the clasp to the front");
  - a claim that misreads over a pair ("One bold ear is enough", flagged by both critics);
  - an abstraction ("One clear point of focus");
  - a parts list ("Black. White. Gold tone.").
- The device with the best record is the **two-beat contrast**:
  - W1 "Woven, not cast" sold 5, while its claim-led twin ("Waterproof") spent ₹3,236 and sold none;
  - "BRUSHED, NOT POLISHED." is our best ad (b03-1, 7.99, A copy 8.5);
  - five of the nine board ranks checked use it: 4 "Bold Lashes. Zero Smudge.", 26 "No drama. Just freshness.", 55 "Stays
    put. Steals attention.", 57 "Soothe your skin. Not burn it.", 96 "Light on weight / Big on journeys".
- The b04 listings already hold such lines (brief §0).

**How (one new H1 per ad; picture, card and offer unchanged, so live results isolate the headline)**
- **b04-1:** "CLOSES WITH A TURN, / NOT A CATCH." (the listing's "closes with a turn rather than a catch"). The beat stays.
- **b04-3:** "THE ONLY <span>COLOUR</span> / IN THE ROOM." with COLOUR in the stones' #08C694, and the beat in bone. This merges
  B's line and A's keyword-in-colour fix, the two remedies the critics gave for the device that did not read. It also drops the
  "one ear" misread.
- **b04-4:** "ONE STONE. / ONE SMOOTH LINE." (the listing's own line, cut before its bare metal word). The beat stays.
- **b04-0:** adopt A's grammatical primary text from the review ("… a black and a white enamel stripe on each …").

**Test**
- Each arm renders clean, within its text-share limit: A2 .22 (b04-1), A4 .18 (b04-3), A6 .14 (b04-4).
- Both critics score each arm beside its control on a single-winner sheet (change 1).
- An arm ships as a second ad only if copy is 8 or more with both critics and its mean is at least the control's. The b04-3 arm
  also needs fit 7.5 or more with both, which shows the device now reads.

### 5. Rank 1 when credits arrive: the gold-tone A3 rhyme on a light warm ground (the run's one new move)

**The finding**
- What sells in our account is a rhyme on a light warm ground. Three of the five live winners are exactly that (apricot hoops,
  anaar bracelet, vkf18), and products.md G7 rates RHYME the best Story archetype (2.75x).
- After four batches, ads-500 has:
  - shipped **0** A3s (b01-2 bud dropped, b04-2 powder dropped);
  - never generated an A3 on a light ground;
  - put 7 of its 11 live ads on dark grounds; the only light warm one is the b02-1 nape.
- b04 ranked both light-ground A3s 5th and 7th, behind slots with untried scene geometry, so the credits ran out first.

**How**
- Shoot **b04-5 (Toggle paperclips)** exactly as the b04 brief §5 wrote it:
  - cream laid paper, three coral-red clips, C1 overhead;
  - clasp ref in slot 1 and cube in slot 2;
  - the paperclip ÷ ring lock, and the same acceptance and layout.
- Add one b04 learning: ask margins at about 1.5× the one wanted (learning 7).
- It is the batch's only new variable. Its must-beat is the apricot hoops, alone on the sheet.

**Test**
- `verify.md` logs paperclip ÷ ring between 1.25 and 1.75 (true 1.5) and the ring at 14–22% of the Feed width.
- The clasp passes the b04-1 construction checks (sailor ring with gate and nub, bar 0.6–0.7× with one row of stones).
- It ships under §7 with desire 7.5 or more with both critics. The result against the apricot hoops is logged per critic.

### 6. Rank 2: the float again, briefed card-only from the start, on a second SKU (the candidate rule's second test)

**The finding**
- b04-0 is the only honest surprise to ship (stop 8.5 with both). The learnings call it a candidate that needs a second batch.
- Its picture died twice in b03 only because a floating pair plus its shadows needs about 700 Feed px, and a headline layout
  leaves 550. As a card-only A1 at P 100 it fits the 84–930 gate.
- The two earlier gold-tone floats failed for reasons we now know how to avoid:
  - b01-2: the bud referent came out 1.6×. A lone piece with no referent holds scale (b03).
  - b02-2: a sky-blue floor turned the lower halves grey-green.

**How**
- **Brushed Gold Huggies** (58 units, ₹699; one live ad, b03-1; check the PLAYBOOK §5.1 cap as the b04 brief did for Woven).
- The pair floats over one saturated warm field (saffron or terracotta, never blue), each earring over its own detached shadow.
  No prop and no referent. The pack ref's pose. C2 at about 12°, as in b03-4.
- Reuse b03-4's float and shadow wording, with the shadow described by its result.
- Lay it out card-only A1 from the start. The Feed has no headline; "Shown magnified · about 14 mm tall" is the float's caption.
  The Story names the type in the beat ("the ₹699 earrings.").

**Test**
- The extent of the pair plus shadows sits inside Feed 84–930 at some T.
- The gap between each earring and its shadow is at least 0.3× the earring's height.
- The lit gold-tone hue is within 6° of the pack ref, with no grey-green.
- Both critics name the float in the review. If it beats apricot or F2 with both critics on a single-winner sheet, the float
  becomes a rule.

### 7. Rank 3: Prism, cheapest route first, then one paid try with fixes already proven, then park it

**The finding**
- Prism is the account's best live seller (the 11 s Prism video: 7 sales, 3.46x) and the dearest SKU (₹2,399, 39 units). Yet
  it is 0 for 3 slots, and no bracelet is live.
- Every Prism failure was placement or scene geometry, never a morph:
  - b01-5: scale and a fist;
  - b02-4: scale, then a diagonal arm under the card;
  - b04-2: powder rising to the back edge, then a plinth seen corner-on.
- Both b04-2 faults now have fixes proven in b04:
  - the slab sentence fixed plinth geometry on the first try, twice (b04-3, b04-4);
  - "level, within the loop's height, margins counted in stones" fixed the powder's extent on b04-2 try 2.

**How**
- **(a) Zero credits first.** The verifier re-checks `b02/pics/b02-4.png` (b02-4 try 2, a forearm on ink velvet, scale 0.15,
  about 1.0–1.2×). It was dropped before the RULINGS §4 sliding crop existed. Check it as a card-only A1, with the card over the
  hand the way b04-1's card sits over skin.
- **(b) If (a) fails:** one paid b04-2 try. The slab sentence replaces the plinth wording, try 2's powder clauses stay, and
  margins are asked at 1.5×.
- **(c) If (b) fails** on anything, Prism leaves the static list for this run.

**Test**
- (a) logs the bracelet's extent, T, P and width share. It ships only if the bracelet, not the arm, lands first on the 200 px
  gate. Expect the arm may win; that is the b02 "hair lands first" failure.
- (b) shows the loop plus powder at 550 Feed px or less, no corner or side face of the slab in view, and construction as in
  b04-2.

### 8. Brief no surprise that depends on a light shape; name each slot's device from what renders

**The finding**
- A light shape on the ground has failed every time it was the device:
  - b01-1's beam came out as a smear;
  - b03-5's pool came out as a soft vignette;
  - b04-4's spot came out as a flat top light, twice.

  L2 flash came out soft twice, and b02's L3 and L5 did not render either.
- Fit is the next fix target (7.38; B 6.5 on b04-4).
- What does render on `nano_banana_2`:
  - highlights on the piece (b04-1's crisp kicker lines);
  - cast shadows described by their result (b03-3, b04-0);
  - the float;
  - a rhyme prop;
  - type the layout controls.

**How**
- The next brief's slot table gets a "device" column. Its value is one of: object (float, rhyme prop), body (worn), shadow (by
  result), or type (the keyword in the piece's colour, the A7 split headline, the A14 in-word swap).
- Light stays a rendering note only.
- Rewrite the unshot b04-6 Ribbon slot before it is shot. Its device is a "warm low rake" on navy satin. Carry the bow in the
  type, or drop the slot (Ribbon has 21 units).

**Test**
- Every slot in the next brief has a device value from that list, and none is a spot, pool, beam, rake or flash.
- `verify.md` logs "device rendered: yes/no" for each picture.
- The batch's fit mean is 7.5 or more, with no fit under 7.

## Layer by layer

| Layer | Verdict | Evidence |
|---|---|---|
| Picture: subject | holds | The piece lands first on all four for both critics. Four SKUs gained their first live ad. |
| Picture: scale | holds | 7 of 7 constructions held. Toggle ring ÷ neck is 0.215 (1.07×). b04-4's pendant is 18% wide because "a fifth" was taken literally (learning 8). The worn ring is 13% of the width, at the floor of the 12–15% band. |
| Picture: colour | change 5 | b04-3's green on charcoal is the batch's best stop (B 9). On b04-1, the plum silk is more saturated than the gold-tone chain (A), which breaks starting rule 1. 7 of 11 live ads sit on dark grounds; the winners mostly do not. |
| Picture: surprise | changes 4, 6, 8 | The one that read is the float the model had already drawn. The drained world reads as a naturally black-and-white set, and the spot never rendered. |
| Camera | holds; one gap logged | C2, C4, C5, C5. Every live piece is upright, centred and frontal. Boards 1, 4, 26, 42 and 55 tilt the product or crop it off the edge. Untested, and not ordered: the run's one new move goes to the A3. |
| Light | change 8 | Light on the piece renders (kicker lines); a light shape on the ground does not, 0 for 4. |
| Layout | holds | Every render is clean at minFont 26. Extent comes first, and the sliding crop placed all three new pictures. The b04-0 card-only layout at P 100, with its caption between the float and the card, is the batch's best layout idea. |
| Branding | holds | 7.88. The ink card with `logo_ink` held brand where bone read only 2.6–2.9:1 on the terracotta. |
| Copy | change 4 | 7.44. A misread over a pair, an ungrammatical primary text, an abstraction. The two-beat contrast is our best-evidenced device and is unused in b04. |
| Meta text | holds; change 2 | Headlines are 35–40 characters with the value inside. The upload CSV is stale and missing b04. |
| Offer | change 3 | Codes and values match the live read. No compare-at price, no shipping line. The b04-1 Story has no offer. |
| Product mix and stock | changes 5, 7 | Live: 5 earrings, 4 rings, 2 necklaces, 0 bracelets. Prism, the account's best seller, is 0 for 3. Re-read Monochrome (24) and Serpentine Silver (23) before launch. The owner flag on Toggle's "Keep it dry" care text stays open; no copy claims waterproof for it. |
| Prompting | holds | 13 learnings logged: counts and widths for worn scale, the slab sentence, piece-unit paths, 1.5× margin asks, clothing words for the safety filter. Every job was served as `nano_banana_2`. |
| Process | changes 1, 2 | Scored file equals shipped file on all 11 rows, and one picture at a time paid off (keep it). But the anchor changed in mid-run, a rule was promoted on one session's reads, and the hand-off CSV and three `copy.json` blocks are stale. |

## Across the run

Final ledger scores (mean of both critics) for the ads live now.

| Batch | Pictures (credits) | Ads shipped (live) | Mean score | Best ad |
|---|---|---|---|---|
| b01 | 10 (20) | 2 (1: b01-4 held) | 7.53 | b01-1 Cushion Halo Ring, A6 spotlight, 7.53 |
| b02 | 10 (20) | 2 (2: b02-1, and b02-5 by rescue) | 7.51 | b02-5 Verdant Eternity Band, A1, 7.53 |
| b03 | 7 (14) | 4 (4) | 7.75 | b03-1 Brushed Gold Huggies, A4 plum monument, 7.99 |
| b04 | 7 (14), plus 1 refused and uncharged | 4 (4; b04-0 from a b03 picture, at zero credits) | 7.75 | b04-3 Verdant Circlet Studs, A4 selective colour, 7.91 |
| **All** | **34 (68)** | **12 (11 live)** | **7.69** | **b03-1, 7.99** |

- **Credits per live ad:** 20, 10, 3.5 and 3.5.
- **Yield and mean:** yield rose and then held. The mean rose about 0.2 a batch to b03, then held.
- **Desire** stayed near 6.9–7.0 until b04 raised it to 7.38.
- **Beating a strong winner:** no ad has beaten F2 or the apricot hoops with both critics in four batches (change 1).
