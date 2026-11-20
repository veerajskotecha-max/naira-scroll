# k01b brief diff (camp k01 AUNTY NE CHASHMA LAGAYA., cards 6-10), from the k01a loop

Written 20 Nov 2026 by the k01a loop writer. The numbers behind every edit are in `batches/k01a/loop.md`.

**How to apply.** Every edit below is an exact string operation on `crazy100.json`. Apply each one once, in the order
given, and log it in `batches/k01b/brief_applied.md`:

- `replace`: the old string becomes the new string;
- `after`: the new string is inserted directly after the old string;
- `set`: the whole field becomes the new string.

The camp edits (C1-C13) touch `camps[k01]`. The card edits touch `camps[k01].ads[card]`. Each old string was checked to
occur exactly once in its field at the moment it is applied, and the whole diff (97 edits) was applied in order to
a copy of the plan with no miss (`/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/k01a_loop/spec.py` and `/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/k01a_loop/simulate.py`; the applied copy is
`/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/k01a_loop/crazy100_k01b_applied.json`). Every new string was linted for the banned words and bare metal words, and every
new primary text for BUY3 ending before character 125.

**What does not change.** Nothing here tames the camp. Every world, headline and device stays:

- the clock-order log, from the pheras at 2:10 a.m. to the kitty party on Sunday;
- GOLD TONE weds SILVER TONE, set like a shaadi card;
- the mala count of twenty, done twice;
- the tailor's matching card;
- the repeat register;
- the four aunties and the padosan's payoff.

Every picture gets one push:

| Card | Push |
|---|---|
| 6 | marigold petals thrown at the pheras, frozen in mid-air round the collar |
| 7 | a second ring of ticks for the second count |
| 8 | even the aunty in cocoa, so the stud is the only colour in the room |
| 9 | her fingertips yellow with the haldi she has just applied |
| 10 | card 5's order slip comes back with four lines, and the padosan is not struck out this time |

Every headline gets a comeback (the new move). The edits come from four sources:

- the hard-rule faults this loop found in the plan;
- the k01a verification and rating lessons;
- `build/learnings.md` (1-29);
- what the new models did with these five pieces in other batches.

## 0. Batch rules (before the card edits)

**Models and credits** (learnings 1, 15 and 16; `batches/bakeoff/README.md`):

- Take A for all five cards is `gpt_image_2_6`, quality medium, 2k, 9:16. No card has a `shootModel`.
- No take B. Learnings 16 drops the plan's hedge takes for k01-7 and k01-10.
- A failed card gets one redo on `gpt_image_2_6` medium, with the verifier's fix clauses written in. The exception is
  card 8: its redo goes to `seedream_v5_pro` 2k, which held the six-pearl map on k07-2 after gpt medium added a seventh.
- Never request `nano_banana_pro`. All 9 k01a jobs asked for it and were served `nano_banana_2`.
- Retry a 429 patiently (learnings 7). Two k01a redos were refused, and with the retry blocked they were never shot.
- The k01-7 Kling clip is made only from an approved still, and only with credits left after the b-batches and the
  rescues.

**References,** in this order. Three of the five cards change reference 2 to the face-free scale crop, because
k01-5R's chin and earring came in at the top edge of a neck crop.

| Card | Reference 1 | Reference 2 | Reference 3 |
|---|---|---|---|
| 6 Duo Link Necklace | `15c3d44e-a47a-4528-99b9-4d1fd03c5166` (01 packshot) | `161af9d8-61b1-494b-a42b-59e31434baec` (02_scale_crop, worn, no face), **not** 02.jpg `321f9752…` (lips and chin) | `refs/duo-link-necklace/03.jpg`, the knot-connector macro: upload it first (no media id yet; checked, no face) |
| 7 Baguette Halo Drops | `fe641c74-45f1-4dd3-ba9f-9e39bd1a6bcd` (01 pair packshot) | `ad662d34-c133-4319-84a0-b5aff74012a3` (03 disc macro) | `fddcdcb0-7bbd-4c1e-93c7-f42a8a772903` (scaleRef, worn ear crop) |
| 8 Prism Cluster Studs | `47443201-a8bb-41ed-92ce-5184a8dc6757` (03 pair packshot) | `30ff9523-0c67-4094-9086-53e22831e693` (04_scale_crop, ear only), **not** 04.jpg `60f7ac77…` (lips) | none |
| 9 Marquise Drop Choker | `4d76bbd0-a098-4bbe-93b0-5c13a4df23b5` (05 laid, gold) | `706193dc-688e-48ba-b0e1-679c00fd8b13` (02_scale_crop, no face), **not** 02.jpg `f2e3533e…` (chin) | `af160bac-86eb-4835-be60-5262fb0c6133` (03 marquise-in-claws macro) |
| 10 Verdant Eternity Band | `2c3d1209-2571-4e63-95af-807e4650a83a` (03 upright) | `702645c3-7920-48ac-afaa-5ce4d51e868a` (01 from above) | `6286cc23-cfde-49e6-b57a-b5c3745af05a` (scaleRef, worn finger crop) |

**Conformance** (k01r G1-G12). The card edits already write these in:

- the full-bleed sentence;
- the exact reference sentence;
- counts in digits and words;
- one metal tone named for every part;
- "two lights only";
- the exact no-face, no-text and one-product clauses;
- placement as landmarks plus percentages;
- named calm zones for the headline and the card;
- "at high resolution" in place of "at 4K".

**The lens moves into the HTML** (C1, C5). This is the main verification lesson of k01a: no plate landed a real lens on
a small piece, whether 18 mm or 550 Feed px off, over an eye, or with a phantom ring painted inside the glass. The plate
now shows the aunty's real folded half-moons beside the piece, plus a CLEAN SPACE clause. The designer draws the
half-moon rim in SVG over the piece and fills it with exactly 2.0x of the same plate about its centre, which is
k01r's method and passed verify on cards 1, 2 and 3. Two rules for the drawn lens:

- The inner glass is at least 2.3 times the magnified part's longest side.
- The piece never crosses the rim half in and half out. On k01-4, perf1 read the toggle as 2.5-3x where the drop crossed
  the rim at almost the same scale.

**Type budget** (learnings 20 and 21; C4). The Feed carries six text elements:

1. the log;
2. the eye chart, without acuity marks on the Feed;
3. the comeback row;
4. the lens with its scale tag, plus at most one card device with at most one label;
5. the F2 card, with the 6/6 line as its one line;
6. the trust line "FREE INSURED SHIPPING · CASH ON DELIVERY".

The FIG callouts, the seal and the acuity marks move to the Story. The Story is the full-bleed plate with no empty
colour block.

**The new move: THE COMEBACK ROW** (C4, 6.11, 7.12, 8.11, 9.11, 10.10). Directly under aunty's eye chart, the buyer answers
in one short Hinglish line in Cormorant italic gold-light. The row is set larger than the chart's last row, so the chart
breaks its own rule because she answers louder. It carries no claim.

| Card | Aunty | Comeback |
|---|---|---|
| 6 | GOLD TONE weds SILVER TONE. | Love cum arranged. |
| 7 | SHE COUNTED TWENTY. TWICE. | Phir poocha: kahan se? |
| 8 | ITNE RANG, EK KAAN PE? | Haan. Baaki sab cocoa. |
| 9 | PICHLI SHAADI MEIN BHI YAHI THA? | Nahi aunty. Pehli baar. |
| 10 | AUNTY KI KITTY BHI LEGI. | Is baar padosan bhi. |

**The basket ask** (C9; basket rate 0.0). Every offer box reads "THIS + ANY TWO · BUY3 · 20% OFF" after three
order-slip tick boxes, the first ticked. Two cards differ:

- **Card 9:** the repeat register is the meter (HALDI ticked, SANGEET and PHERE empty), so its box has no tick boxes.
- **Card 10:** four boxes, all ticked, before "ANY FOUR · BUY4 · 30% OFF". Its order slip lists four rings.

No price, total or saving is printed.

**Hard-rule faults this diff removes from the plan:**

- **A real lens in front of the piece.** It never landed in k01a. It painted a second ring inside the glass (two
  products), and it sat over an eye (face rule).
- **Voice and music on the Reels** (cards 7 and 10, and the camp idea). Owner ruling 5 says motion in this run is silent.
- **The trust line switched off.** The F2 footer read "CASH ON DELIVERY" only. The owner ruling of 20 Nov 2026 puts
  "FREE INSURED SHIPPING · CASH ON DELIVERY" on every card. The OBJECTION card (6) and the OFFER card (10) also carry it
  in the primary text.
- **BUY3 at character 173** in the carousel text (rule: before 125). The new text also leaves out the k01a carousel's
  "Every piece here is in stock", because cards 7 and 8 are pre-order.
- **Card 10's "open back" lens.** A palm-down hand hides the open back, so the lens would claim what the plate cannot
  show. Four honest 2x lenses also cannot sit on one 18 mm ring, so card 10 has one lens.
- **Card 9's water droplets "on the collarbone".** They sat beside two clear pear stones, where a droplet reads as a
  third stone (learnings 27). They move to the shoulders.
- **"never warmed to gold"** in card 6's prompt, a bare metal word. It now reads "gold tone".
- **References showing lips or a chin** as reference 2 on cards 6, 8 and 9. They are replaced by the scale crops.

Card 7's 6/6 line keeps "PVD 18K GOLD COATING". The product card allows it as a material fact, with no claims.


## 1. Camp-level edits

**C1** · `idea` · replace
- old: `every frame shows the real piece worn at true size (an ear from behind, a hand, a collarbone, a wrist) and, between the camera and the piece, an aunty's reading glasses: tortoiseshell half-moons held by an older hand whose wrist disappears into a rani-pink pallu. Inside the lens the finished ad shows an honest 2x crop of the same photograph, built in HTML from a 4K plate and clipped to the real rim;`
- new: `every frame shows the real piece worn at true size (an ear from behind, a hand, a collarbone, a wrist) and, beside the piece, an aunty's folded reading glasses: tortoiseshell half-moons held by an older hand whose wrist disappears into a rani-pink pallu. Her lens is drawn in HTML over the piece (a tortoiseshell half-moon rim), and inside it the finished ad shows an honest 2x crop of the same photograph about the piece's centre, clipped to the drawn rim; the photograph never puts a real lens in front of the piece (k01a: it landed 18 mm to 550 Feed px off, and once painted a second ring inside the glass);`
- why: k01a verify: no plate landed a real lens on the piece (k01-2A phantom ring, k01-4A 18 mm off, k01-3A over an eye); k01r's drawn lens passed verify on cards 1, 2 and 3 (learnings 4).

**C2** · `idea` · replace
- old: `On Reels the device becomes physical: her voice opens the ad ('Beta, zara idhar aana'), the headline stays out of focus until her glasses lock on (THE SQUINT), and the lens is live.`
- new: `On Reels the device becomes physical: the headline stays out of focus until her lens locks on (THE SQUINT), and the lens is live. Motion in this run is silent (owner ruling 5: no voice or music), so 'Beta, zara idhar aana' opens each Reel as a 0.8 s Cormorant title, never a voice.`
- why: Owner ruling 5 (CRAZY100.md §9): motion in this run is silent.

**C3** · `textualGraphic` · replace
- old: `In the x 72 gutter each row carries its acuity mark in Jost 300 16 px gold-light at 70%: 6/60, 6/36, 6/24.`
- new: `On the Story only, in the x 72 gutter, each row carries its acuity mark in Jost 300 16 px gold-light at 70%: 6/60, 6/36, 6/24; the Feed drops them (k01a: three critics asked to cut 'the eye-chart numbers').`
- why: k01-4 worst issues (craft1, perf2 on V3, truth1 on V1): the acuity numbers were clutter at Feed size.

**C4** · `textualGraphic` · replace
- old: `(2) BEAT: Cormorant Garamond italic 500, 34-44 px, gold-light, at most two lines, set under the lens in the calm dark band (Feed y 806-930), so the eye reads headline, lens, beat, card; on card 4 the Feed carries only the punch, under the headline.`
- new: `(2) THE COMEBACK ROW (k01a loop, the new move): directly under the eye chart the buyer answers aunty in one short Hinglish line, Cormorant Garamond italic 500, gold-light, set LARGER than the chart's last row (about 0.8-0.9 of row 1), so the chart breaks its own rule because she answers louder ('EK BHI MATCH NAHI KARTA.' / 'Isiliye toh liya.'). It is read second, never last, and it carries no claim: facts live in the lens's scale tag, the device's one label or the F2 card's 6/6 line. TYPE BUDGET, Feed: six text elements only: (a) the log, (b) the eye chart, (c) the comeback row, (d) the lens with its scale tag plus at most ONE card device with at most one label, (e) the F2 card with the 6/6 line folded in, (f) the trust line. No FIG callout and no seal on the Feed.`
- why: Fix target (message 5.56 across k01-4's three variations, under 6 on all three; fit 5.33 on the chosen): about 14 text elements and a payoff set last (learnings 20, 21).

**C5** · `textualGraphic` · replace
- old: `(3) THE LENS: the tortoiseshell rim is in the photograph. The glass is filled in HTML with the same photograph at exactly 2.0x about the lens centre (background-size twice the canvas, background-position at minus the lens centre), with a clip-path traced to the rim's inner edge,`
- new: `(3) THE LENS: the tortoiseshell half-moon rim is DRAWN in HTML (SVG: flat top, curved base, dark tortoiseshell) and placed with its centre on the part the headline names; the photograph shows her real folded glasses beside the piece. The glass is filled with the same photograph at exactly 2.0x about the drawn lens's centre (background-size twice the canvas, background-position at minus the lens centre), with a clip-path on the drawn rim's inner edge; size the glass so the magnified part fits inside it whole with a margin (inner glass at least 2.3x the part's longest side), and never let the piece cross the rim half in and half out (k01-4: perf1 read the T-bar as 2.5-3x where the drop crossed the rim; k01-3R: a 2x stud could not fit its lens),`
- why: Learnings 4 and k01r; k01-3R lens geometry; k01-4 truth 7.17 from the scale jump at the rim.

**C6** · `textualGraphic` · replace
- old: `Plates are generated at 4K (2160 x 3840) so the 2x crop uses native pixels, and the earrings and the ring are shot in an 11 cm field, so the lens shows them at about 19.6 Feed px per mm, over the ads-500 line of 19 px per mm for 'magnified'.`
- new: `Plates are generated at 2k (about 1520 x 2688; read W and H), so the 2x crop upsamples about 1.4x: before printing it, set the crop beside the same crop of reference 1 and check the construction still reads true (learnings 18). The scale tag always prints the listed size; the photograph outside the lens stays under 19 Feed px per mm.`
- why: Every k01a and k01r plate rendered at 2k; nano_banana_pro 4k was refused (bake-off).

**C7** · `textualGraphic` · replace
- old: `(4) THE REPORT: up to three gold-light 1.5 px hairline leaders, each starting`
- new: `(4) THE REPORT, Story only and at most one callout (the Feed's six-element budget has no room for it): one gold-light 1.5 px hairline leader,`
- why: k01-4 V1: the FIG callouts and their quotes were the first thing every critic asked to cut.

**C8** · `textualGraphic` · replace
- old: `(6) THE SEAL: a 150 px roundel top right (Feed x 858, y 84),`
- new: `(6) THE SEAL, Story only: a 150 px roundel top right (Story x 858, y 276),`
- why: Type budget: the Feed keeps six text elements.

**C9** · `textualGraphic` · replace
- old: `and the footer CASH ON DELIVERY in Jost 20 px.`
- new: `and the footer 'FREE INSURED SHIPPING · CASH ON DELIVERY' in Jost 20 px (owner ruling, 20 Nov 2026; never a delivery time). The offer box asks for the basket: three 14 px order-slip tick boxes in gold-light, the first ticked, before 'THIS + ANY TWO · BUY3 · 20% OFF' (card 9: the repeat register is the meter, so no boxes; card 10: four boxes, all ticked, before 'ANY FOUR · BUY4 · 30% OFF').`
- why: Owner ruling on the trust line; basket rate 0.0 (threshold: strengthen the BUY3 line).

**C10** · `textualGraphic` · replace
- old: `Story uses the full plate (text only between y 270 and 1250):`
- new: `Story uses the full plate, full bleed behind every element, never an empty colour block (k01-4 V1 and V3 lost the bottom 35% of the Story to flat plum, and every customer named it) (text only between y 270 and 1250):`
- why: k01-4 V3 customer lines (6 of 6) and critics: 'the Story is half empty purple'.

**C11** · `brandFeatures` · replace
- old: `The F2 card is unchanged: name, price, one line, offer box, footer CASH ON DELIVERY,`
- new: `The F2 card is unchanged: name, price, one line (the 6/6 line), offer box, footer FREE INSURED SHIPPING · CASH ON DELIVERY,`
- why: Owner ruling, 20 Nov 2026.

**C12** · `brandFeatures` · replace
- old: `plus, on Reels, the same aunty voice and THE SQUINT.`
- new: `plus, on Reels, THE SQUINT (silent: owner ruling 5).`
- why: Owner ruling 5.

**C13** · `carouselText` · set
- set to: `Every wedding has an aunty who leans in. We handed her the glasses. Aunty remembers repeats: any three, 20% off with BUY3; any four, 30% off with BUY4. Free insured shipping, cash on delivery.`
- why: The plan's text (262 characters) put BUY3 at character 173 (rule: before 125). Now 192 characters, BUY3 ends at 121, with the owner's trust line. It does not repeat the k01a carousel's 'Every piece here is in stock', because cards 7 and 8 are pre-order. Every carousel card links to its own product page.

## 2. Card 6 · Duo Link Necklace · ₹1,099 · OBJECTION / EDUCATION · "GOLD TONE WEDS SILVER TONE."

**The push:** the petal shower of the pheras, frozen in mid-air at both sides of the collar and kept off the chain.
Both lenses are drawn across the chain, one over a gold tone link and one over a silver tone link, so for once both
lenses work.

**Expected scale:** about 6 Feed px per mm at an 18 cm field, so a link is about 120 Feed px long, and about 12 px per mm
inside the 2x lenses. That is under 19, so the scale tag owns the 2x. Each lens is about 300 px wide, which is 2.3 times
a link at true size, so the whole link fits with a margin.

**6.1** · `picture` · replace
- old: `The aunty holds her glasses level across it, and for once both lenses work: the left over an 18k gold tone link, the right over a rhodium silver tone link three links along.`
- new: `Marigold petals thrown at the pheras hang frozen in the air at both sides of her neck. The aunty holds her folded glasses low at the edge; in the finished ad her two lenses are drawn across the chain, and for once both lenses work: the left over an 18k gold tone link, the right over a rhodium silver tone link three links along.`
- why: Drawn lenses (C1, C5); the petal shower is this card's picture push (crazy 6.83 < 7.5).

**6.2** · `prompt` · replace
- old: `Vertical 9:16 editorial wedding-night portrait crop at 4K (2160 x 3840), 85 mm lens, front-on: a young Indian woman's neck and collarbones at the pheras, cropped from just below the chin to mid-chest, so no chin, lips or face appear; an ivory satin camisole with thin straps.`
- new: `Vertical 9:16 editorial wedding-night photograph at high resolution, 85 mm lens, front-on, a full-bleed photograph edge to edge with no borders, bands or panels: a young Indian woman's neck and collarbones at the pheras. The top edge of the picture cuts straight across the middle of her neck, well below the jaw, and her ears are outside the frame: no chin, jaw, lips, nose, eye, eyebrow or earring anywhere in frame. An ivory satin camisole with thin straps and a plain neckline with no trim.`
- why: k01-5A/5R (neck crops): the chin came back at the top edge and 5R added an earring there (hard rule); learnings 5 (letterbox); plates render at 2k.

**6.3** · `prompt` · replace
- old: `Reference 1 is the authority on this exact piece: copy the necklace's construction exactly and ignore its plaster, background and light; reference 2 shows it worn at true scale.`
- new: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece, worn at the base of the neck, resting on the collarbones like a collar, at true size (41 cm chain plus a 5 cm extender; each oval link about 20 x 7 mm, about as long as a Rs 1 coin is wide and about as wide as a pencil; about 8 or 9 links across the front of the neck): match that scale and the way it sits exactly; copy only the scale, never a face, a camisole or a wall.`
- why: Exact reference sentence. MEDIA: reference 2 becomes the face-free scale crop 161af9d8-61b1-494b-a42b-59e31434baec (refs/duo-link-necklace/02_scale_crop.jpg) in place of 02.jpg (321f9752…), which shows lips and chin.

**6.3b** · `prompt` · after
- after: `copy only the scale, never a face, a camisole or a wall.`
- insert: ` Reference 3 is a close-up of the same piece: one 18k gold tone link, one knot connector (a thick loop, two grooved stacked rings, a thick loop) and one rhodium silver tone link; copy the connector's construction from it, never its framing, focus or size.`
- why: The card's first morph is the knot connector. MEDIA: upload refs/duo-link-necklace/03.jpg (the listing macro, no face; checked) and add it as reference 3; it has no media id yet.

**6.4** · `prompt` · replace
- old: `FIDELITY: the necklace, a 41 cm collar chain of elongated oval links about 20 x 7 mm in round wire, alternating strictly: 18k gold tone, rhodium silver tone, 18k gold tone, and so on; between every two links one 18k gold tone knot connector: a loop on each side and two stacked rings in the middle. One or two gold tone links are rope-twisted.`
- new: `FIDELITY: the necklace, a 41 cm collar chain of 17 (seventeen) elongated oval links about 20 x 7 mm in round wire, 9 (nine) in 18k gold tone and 8 (eight) in rhodium silver tone, alternating strictly: 18k gold tone, rhodium silver tone, 18k gold tone, and so on; between every two links exactly one 18k gold tone knot connector, 16 (sixteen) in all: a thick loop on each side and two stacked grooved rings in the middle, about half a link long. One or two gold tone links carry a fine rope twist. Every knot connector is 18k gold tone, never silver tone; only the eight oval links in between are rhodium silver tone.`
- why: Learnings 6 and 9: counts in digits and words, the tone of every part named (k01-5B rendered a jump ring silver tone).

**6.4b** · `prompt` · replace
- old: `the silver tone links stay cool bright white, never warmed to gold;`
- new: `the silver tone links stay cool bright white, never warmed to gold tone;`
- why: Prompt lint: no bare 'gold' as a metal word.

**6.5** · `prompt` · replace
- old: `SCALE: the chain sits at the base of the neck on the collarbones like a collar, about eight or nine links across the front, each link about as long as a 20 mm coin; field of view about 20 cm wide; soft contact shadows on the skin.`
- new: `SCALE, set by her body exactly as in reference 2: the chain sits at the base of the neck and rests on the collarbones like a collar; 8 or 9 links (eight or nine) span the front from one side of her neck to the other, never five or six bigger ones; each link about as long as a Rs 1 coin is wide and about as wide as a pencil; her neck at its narrowest fills about 60% of the frame's width and the chain's front arc about three quarters of it; field of view about 18 cm wide; soft true contact shadows where every link and knot touches the skin. Necklaces in this camp came out 1.3 to 1.8 times too big when sized by fractions of the frame (k01-5A, k01r k01-5A): size it by counts against her body.`
- why: Learnings 2, 10 and 24; k01-5A drew the neck at 57% of the width and the clasp 1.45-1.8x.

**6.6** · `prompt` · replace
- old: `THE AUNTY: from the lower right, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu, holds half-moon reading glasses with thin dark tortoiseshell frames level across the front of the chain about 8 cm in front of it: the left lens centred over one 18k gold tone link and the right lens centred over the rhodium silver tone link three links along; each lens about 26% of the frame's width; the glass is perfectly clear, showing what is behind it at the same size, undistorted and untinted, reflecting nothing, never a face or eyes.`
- new: `THE AUNTY: from the lower right edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu, holds her folded half-moon reading glasses by one folded temple arm (two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin bridge), low at the right edge below the chain, beside it and never in front of it: no part of the glasses or her fingers crosses the chain, and the glass shows only soft background, never the chain. CLEAN SPACE: the whole front of the chain across the collarbones is evenly lit, with nothing in front of it, so two lenses can be drawn over it later; no magnifier and no magnified view anywhere in the picture.`
- why: C1/C5: the lenses are drawn in HTML; k01r G1-G3 wording, which passed on cards 1-3.

**6.7** · `prompt` · replace
- old: `WORLD: the mandap far behind in soft blur: strings of marigold and mango leaves, a faint warm haze, and the glow of the sacred fire only as soft orange bokeh in the lower left corner, never on the skin or the chain.`
- new: `WORLD: the mandap far behind in soft blur: strings of marigold and mango leaves, a faint warm haze, and the glow of the sacred fire only as soft orange bokeh in the lower left corner, never on the skin or the chain. THE BLESSING, frozen: at the instant of the pheras a handful of loose marigold petals, thrown by the family, hangs frozen in mid-air at both sides of her neck, between the tops of her shoulders and the height of the chain, two or three crisp and the rest soft and out of focus; no petal touches the skin or the chain, none comes nearer the chain than the length of one link, and none sits in front of it.`
- why: PUSH (crazy 6.83 < 7.5): the pheras' petal shower frozen in the air around the collar; kept off the piece (learnings 27).

**6.8** · `prompt` · replace
- old: `COMPOSITION: chain and glasses between 33% and 53% of the frame height; from 14% to 32% calm blurred marigold and plum; below 55% soft ivory satin.`
- new: `COMPOSITION: the chain's front arc sits just above the middle of the frame, its lowest link at about 50% of the height and its sides rising toward the tops of the shoulders at about 36%; the aunty's hand and the folded glasses only in the lower right corner, below 58%; from the top edge to about 32% the upper neck falls into soft warm shadow, clearly darker than the lit chain, with blurred marigold and plum at both sides, calm for the headline; below 58% soft ivory satin, calm for the price card.`
- why: Learnings 26 and k01r G12: placement as landmarks plus percentages (percentages alone were ignored on k01-1R and k01-3R); k01r k01-5 top-band clause for bone type over skin.

**6.9** · `prompt` · replace
- old: `LIGHT: soft neutral fill from above left with a neutral white balance, so both tones stay true;`
- new: `LIGHT, two lights only: soft neutral fill from above left with a neutral white balance, so both tones stay true and the petals and fire never warm the rhodium links;`
- why: Two-light rule; the card's logged morph (warm light turns rhodium gold).

**6.10** · `prompt` · replace
- old: `NEGATIVES: no text, letters, numbers or logos anywhere; no face; one product only: no earrings, rings, bangles or second necklace; no fabric, thread or knot touching the chain.`
- new: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark anywhere; no face, no eyes, no eyebrows, no chin; one product only: no earrings, rings, bangles or second necklace; no fabric, thread, petal or knot touching the chain; never links hooked straight into one another like a plain paperclip chain; no silver tone knot connector.`
- why: Exact no-text and no-face clauses; the lock's must-stay clause as a negative.

**6.11** · `beat` · set
- set to: `Love cum arranged.`
- why: THE COMEBACK ROW (C4). The bible's facts (sixteen gold-tone knots) move to the Story FIG and the primary text; 'love cum arranged' was the line the plan itself expected people to repeat.

**6.12** · `layout` · set
- set to: `LOG: 'PHERAS · 2:10 AM · INSPECTION 6 OF 10'. WEDDING-CARD HEADLINE in the eye-chart grid, no acuity marks on the Feed: GOLD TONE (Velista 112 px) / weds (Cormorant italic 64 px gold-light, lowercase, centred on the rows like a shaadi card) / SILVER TONE. (Velista 84 px), bone, x 128 from y 112. COMEBACK ROW directly under it, about y 384-470: 'Love cum arranged.' in Cormorant italic 500, 92 px, gold-light (larger than SILVER TONE.). TWO DRAWN LENSES (SVG half-moons, flat top, dark tortoiseshell rims, joined by a drawn bridge), each filled with exactly 2.0x of the same plate about its own centre and clipped to its rim: the left centred on one 18k gold tone link, the right on the rhodium silver tone link three links along, each about 300 px wide, in y 500-800 (choose the crop P that puts the chain there); the rest of the chain stays visible at true size outside them. The lenses' one label is the scale tag under the right lens: 'IN HER LENSES ABOUT 2× · LINKS ACTUAL 20 × 7 MM'. No FIG callout, no name key and no seal on the Feed. F2 card on plum from y 990: DUO LINK NECKLACE; the 6/6 line '41 CM + 5 CM · 21.4 G · WATERPROOF · TARNISH FREE'; ₹1,099 in Cormorant; the offer box with three order-slip tick boxes, the first ticked, then 'THIS + ANY TWO · BUY3 · 20% OFF'; the wordmark; the footer 'FREE INSURED SHIPPING · CASH ON DELIVERY'. STORY: the plate full bleed, no empty block; log y 276, headline y 304 with the acuity marks, comeback under it, lenses y 690-900, seal top right, compact card y 1030-1250 over the satin; one FIG on the Story only: FIG. 1 · SIXTEEN KNOTS, 18K GOLD TONE 'dono ko baandh diya', its leader from a knot between the lenses.`
- why: Type budget (C4): log, chart, comeback, lenses with one tag, card, trust line.

**6.13** · `offer` · set
- set to: `THIS + ANY TWO · BUY3 · 20% OFF`
- why: Basket rate 0.0: the offer box asks for three (C9).

**6.14** · `primaryText` · set
- set to: `Gold tone or silver tone? Both: sixteen gold-tone knots tie them into one line. ₹1,099. Any three, 20% off with BUY3. Free insured shipping, cash on delivery.`
- why: 158 characters, BUY3 ends at 116. OBJECTION card, so the owner's trust line goes in the primary text.

**6.15** · `risk` · set
- set to: `The knot connectors collapsing into a plain paperclip chain, and the fire glow, petals or warm haze turning the rhodium links gold tone (both logged morphs); a silver-tone knot or jump ring (k01-5B's two-tone fault); the chin or an earring creeping in at the top edge (k01-5R); a petal touching the chain and reading as a part. No take B (learnings 16); one redo on gpt_image_2_6 medium with the verifier's clauses written in; never a composite.`
- why: Learnings 16 drops b-batch hedge takes; the k01a and k01r faults on neck crops.

## 3. Card 7 · Baguette Halo Drops · ₹1,199, pre-order · OUTCOME / TRUST · "SHE COUNTED TWENTY. TWICE."

**The push:** the count is drawn twice, as twenty numerals and then a tighter ring of twenty ticks, with the 20 ringed
both times. It is printed only if verify counts exactly 20 baguettes at 2x. Otherwise the plan's hedge headline "SHE
COUNTED THEM. TWICE." runs, with the numerals dropped.

**Expected scale:** about 9 Feed px per mm at a 12 cm field. The 14 mm disc is about 126 Feed px across outside the lens
and about 252 inside it. The 2.3x rule therefore asks for an inner glass about 300 px tall, so the drawn half-moon is
about 540 px wide. Plan the lens zone for it.

**7.1** · `picture` · replace
- old: `The aunty's lens hovers over the disc.`
- new: `The aunty's folded glasses wait in her hand below the ear; in the finished ad her lens is drawn over the disc.`
- why: Drawn lens (C1, C5).

**7.2** · `prompt` · replace
- old: `Vertical 9:16 editorial wedding-night photograph at 4K (2160 x 3840), 100 mm macro-portrait lens at ear height, seen from behind and slightly to the left of a young Indian woman at a reception at midnight.`
- new: `Vertical 9:16 editorial wedding-night photograph at high resolution, a full-bleed photograph edge to edge with no borders, bands or panels, 100 mm macro-portrait lens at ear height, the camera behind her and slightly to the left of a young Indian woman at a reception at midnight.`
- why: 2k render; learnings 5.

**7.3** · `prompt` · replace
- old: `Reference 1 is the authority on this exact piece: copy the earring's construction exactly and ignore its plaster, background and light; reference 2 shows the disc in detail.`
- new: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece: the clearest view of the disc's twenty tapered baguettes, the bead dividers and the open centre window; count the baguettes from it. Reference 3 shows this exact piece worn on the earlobe at true size (a 27 mm drop, just over an inch, about the top joint of a thumb: the 14 mm sunburst disc covers most of the lobe and is about a thumbnail wide, and the 9.5 mm pearl hangs just below the lobe): match that scale exactly; copy only the scale, never a face.`
- why: Exact reference sentence; MEDIA: add the scaleRef fddcdcb0-7bbd-4c1e-93c7-f42a8a772903 as reference 3 (learnings 11-14).

**7.4** · `prompt` · replace
- old: `inside it exactly twenty tapered clear baguette cubic zirconia set radially like a sunburst,`
- new: `inside it exactly 20 (twenty) tapered clear baguette cubic zirconia set radially like a sunburst, never 16, 18, 22 or 24,`
- why: Learnings 9: counts in digits and words; the numeral ring is count-gated.

**7.5** · `prompt` · after
- after: `the drop pearl stays round and smaller than the disc; do not redesign or add anything.`
- insert: ` The rim, the beads, the spokes, the loop, the bell cap and the post are all the same 18k gold tone; exactly 2 (two) pearls: the small one at the heart and the round one below.`
- why: Learnings 6 and 9.

**7.6** · `prompt` · replace
- old: `SCALE: the disc sits on the lobe and covers most of it, the pearl hangs just below the lobe; field of view about 11 cm wide, so the disc is about 13% of the frame's width; a soft contact shadow under the disc.`
- new: `SCALE, set by her ear exactly as in reference 3: the disc sits on the lobe and covers most of the lobe, about a thumbnail wide; the round pearl hangs just below the lobe; the whole earring, from the top of the disc to the bottom of the pearl, is a little less than half the ear's height from the top of the helix to the bottom of the lobe; the ear fills a little under a third of the frame's height; field of view about 12 cm wide; a soft contact shadow under the disc. Earrings in this camp came out 1.35 to 1.6 times too big when sized by fractions of the frame (k01-1A, k01-1R, k01-3A): never larger than the lobe.`
- why: Learnings 2 and 24; k01a scale drift on worn ears.

**7.7** · `prompt` · replace
- old: `BODY: her head is turned well away; the right frame edge falls just behind the jaw hinge, so no cheek, eyebrow, eye, nose or lips appear;`
- new: `BODY: the camera is behind her; her head is turned fully away, so the jaw and cheek are hidden behind the ear and hair; no eyelash, eyelid, brow, cheek, nose or lip breaks the outline of her head anywhere in the frame;`
- why: k01-1A and k01-3A/3R showed lashes, brow and an eye corner with 'turned well away'; k01-1R's wording held (learnings 3).

**7.8** · `prompt` · replace
- old: `THE AUNTY: from the left edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu, holds half-moon reading glasses with thin dark tortoiseshell frames so one lens hovers about 8 cm in front of the disc, centred on it, about 38% of the frame's width; the glass is perfectly clear, showing what is behind it at the same size, undistorted and untinted, reflecting nothing, never a face or eyes.`
- new: `THE AUNTY: from the lower left edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu, holds her folded half-moon reading glasses by one folded temple arm (two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin bridge), below and to the left of the earring, about 4 cm from it, never in front of it: no part of the glasses or her fingers crosses the ear or the earring, and the glass shows only soft background. CLEAN SPACE: an evenly lit area about 5 cm across centred on the disc, with only the ear, the lobe and the earring in it and nothing in front of them, so a lens can be drawn over it later; no magnifier and no magnified view anywhere in the picture.`
- why: C1/C5; k01r G1-G3.

**7.9** · `prompt` · replace
- old: `COMPOSITION: earring and lens between 33% and 53% of the frame height; from 14% to 32% calm plum bokeh with soft marigold points; below 55% soft champagne silk and shadow.`
- new: `COMPOSITION: the disc sits just above the middle of the frame, at about 45% of the height and a little right of centre, the pearl just below it, so the whole earring lies between about 42% and 54%; above the ear, from the top edge to about 30%, only the dark hair of the bun and calm plum night with soft marigold points, calm for the headline; the aunty's hand and glasses only in the lower left, between 56% and 75%; below 56% her neck and the champagne silk collar fall into soft shadow, calm for the price card.`
- why: Landmarks plus percentages (learnings 26, k01r G12).

**7.10** · `prompt` · replace
- old: `LIGHT: soft warm fill from above left;`
- new: `LIGHT, two lights only: soft warm fill from above left;`
- why: Two-light rule.

**7.11** · `prompt` · replace
- old: `NEGATIVES: no text, letters, numbers or logos anywhere; no face or eyes; one product only, no other jewellery on anyone; no flower covering the earring; no star-shaped glints.`
- new: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark anywhere; no face, no eyes, no eyebrows; one product only: one earring, no second earring and no other jewellery on anyone; no flower or hair covering the earring; no star-shaped glints; no round centre stone and no ring of small round stones on the disc.`
- why: Exact clauses; the card's named morph (round pave halo) as a negative.

**7.12** · `beat` · set
- set to: `Phir poocha: kahan se?`
- why: THE COMEBACK ROW (C4): the outcome, 'then she asked where you got them', in the buyer's own Hinglish.

**7.13** · `layout` · set
- set to: `LOG: 'RECEPTION · 12:20 AM · INSPECTION 7 OF 10'. EYE-CHART HEADLINE, no acuity marks on the Feed: SHE COUNTED (Feed 116 px) / TWENTY. TWICE. (84), bone, x 128 from y 112. COMEBACK ROW directly under it, about y 330-420: 'Phir poocha: kahan se?' in Cormorant italic 500, 92 px, gold-light. THE LENS: an SVG half-moon (flat top, dark tortoiseshell rim) drawn over the disc, about 540 px wide with an inner glass about 300 px tall (the 2x disc is about 252 px), filled with exactly 2.0x of the same plate about the disc's centre and clipped to the rim, in y 450-800; the whole disc inside the glass with a margin, and the pearl below it at true size outside the rim, never cut by it. THE COUNT, the lens's one label, printed only if verify counts exactly 20 baguettes at 2x: twenty Jost 300 13 px gold-light numerals, 1 to 20, on a circle just outside the magnified disc, inside or across the rim, each aligned to its own baguette like beads on a mala, and a second, tighter ring of twenty 4 px ticks for the second count; the 20 ringed by a 1 px gold-light circle with '×2' beside it. Scale tag at 7 o'clock on the rim: 'IN HER LENS ABOUT 2× · ACTUAL 27 MM DROP'. No FIG callout and no seal on the Feed. F2 card on plum from y 990: BAGUETTE HALO DROPS; the 6/6 line '18K GOLD TONE · PVD 18K GOLD COATING · PRE-ORDER'; ₹1,199; the offer box with three order-slip tick boxes, the first ticked, then 'THIS + ANY TWO · BUY3 · 20% OFF'; the wordmark; 'FREE INSURED SHIPPING · CASH ON DELIVERY'. STORY: the plate full bleed, no empty block; log y 276, headline y 304 with the acuity marks, comeback under it, lens y 660-1000, seal top right, compact card y 1030-1250; one FIG on the Story only: FIG. 1 · A PEARL BELOW, IT SWINGS 'chalte hue hilta hai', its leader from the bell cap, never the pearl.`
- why: Type budget (C4); count-gated device (PLAN §9 step 4).

**7.14** · `offer` · set
- set to: `THIS + ANY TWO · BUY3 · 20% OFF`
- why: Basket rate 0.0 (C9).

**7.15** · `primaryText` · set
- set to: `She counted twenty baguettes round a pearl. Twice. Then asked: kahan se? ₹1,199, pre-order. Any three, 20% off with BUY3. A pearl swings below, 27 mm.`
- why: 150 characters, BUY3 ends at 120. Pre-order and no claims (product card).

**7.16** · `motion` · replace
- old: `Sound: bead clicks over a soft shehnai, and the aunty's voice under the second pass: '...bees. Haan, bees.'`
- new: `Silent (owner ruling 5: no voice or music in this run): under the second pass, 'bees. haan, bees.' appears for 0.6 s in Cormorant italic gold-light instead of a voice. The live lens uses the drawn rim, which never moves. Kling only from the approved still and only with credits left after the b-batches and the rescues (learnings 16).`
- why: Owner ruling 5; learnings 16.

**7.17** · `risk` · after
- after: `Hedge headline if the count cannot be verified at 2x: 'SHE COUNTED THEM. TWICE.' with the numerals dropped.`
- insert: ` No take B (learnings 16); one redo on gpt_image_2_6 medium with the verifier's clauses written in, and the count re-checked at 2x.`
- why: Learnings 16.

## 4. Card 8 · Prism Cluster Studs · ₹1,299, pre-order · OUTCOME / EDUCATION · "ITNE RANG, EK KAAN PE?"

**The push:** the whole room is cocoa, and so is the aunty's pallu this once. The stud is the only colour in the frame,
which is the card's outcome made literal. It also removes the card's own named risk: rani pink competing with the pink
baguettes.

**8.1** · `picture` · replace
- old: `The aunty's lens (a sliver of rani-pink pallu at the edge) hovers over it; inside, at 2x, five clean cuts in order with six pinhead pearls.`
- new: `Even the aunty is in cocoa this once: her pallu is cocoa-and-wine silk, so nothing in the room competes. Her folded glasses wait in her hand; in the finished ad her lens is drawn over the stud, and inside, at 2x, five clean cuts in order with six pinhead pearls.`
- why: PUSH: the outcome made literal (the stud is the only colour in the frame); the card's own risk (rani pink competing with the pink baguettes) and its hedge (a wine pallu) become take A.

**8.2** · `prompt` · replace
- old: `Vertical 9:16 editorial cocktail-night photograph at 4K (2160 x 3840), 100 mm macro-portrait lens at ear height, seen from behind and slightly to the right of a young Indian woman.`
- new: `Vertical 9:16 editorial cocktail-night photograph at high resolution, a full-bleed photograph edge to edge with no borders, bands or panels, 100 mm macro-portrait lens at ear height, the camera behind her and slightly to the right of a young Indian woman.`
- why: 2k render; learnings 5.

**8.3** · `prompt` · replace
- old: `Reference 1 is the authority on this exact piece: copy the earring's construction exactly and ignore its cube, background and light; reference 2 shows it worn at true scale.`
- new: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light; it shows the pair, and this picture shows only the left stud. Reference 2 is a detail of the same piece worn at true size (the arc about 20 mm long, the centre stone about 6 mm; the stud spans about the width of the lobe, far smaller than the ear, about the diameter of a Rs 1 coin): match that scale exactly; copy only the scale, never a face.`
- why: Exact reference sentence. MEDIA: reference 2 becomes the scale crop 30ff9523-0c67-4094-9086-53e22831e693 (refs/prism-cluster-studs-silver/04_scale_crop.jpg) in place of 04.jpg (60f7ac77…), which runs from the lips down.

**8.4** · `prompt` · replace
- old: `six tiny white pearls tucked in the gaps; one post.`
- new: `exactly 6 (six) tiny white pearls tucked in the gaps, never seven or eight, placed exactly: one pearl above and one below the join of the first purple princess and the first pink baguette; one pearl above the yellow; one small pearl below the join of that pink and the yellow; one slightly larger pearl below the join of the yellow and the second purple; one pearl below the join of the second purple and the last pink, and nothing above that join but claws; one post. Behind and between the claws only thin bright rhodium silver tone setting bars, the same polished metal as the claws: no cream, ivory or matte beads and no half-hidden pearls behind the claws.`
- why: k07-2A (gpt_image_2_6 medium) drew a seventh pearl and cream 'gallery beads'; its pearl-map clause held on k07-2R and k08-3A.

**8.5** · `prompt` · replace
- old: `SCALE: the arc lies along the earlobe and spans about the lobe's width, about the size of a 20 mm coin; field of view about 11 cm wide, so the arc is about 18% of the frame's width; a soft contact shadow under the arc.`
- new: `SCALE, set by her ear exactly as in reference 2: the arc lies along the earlobe and spans about the lobe's width, about the diameter of a Rs 1 coin; the ear, from the top of the helix to the bottom of the lobe, is about three arcs tall, so the stud is about a third of the ear's height, never half; the ear fills a little under a third of the frame's height; field of view about 12 cm wide; a soft contact shadow under the arc. The listing's own worn photo drew this stud 1.5 times too big: never wider than the lobe.`
- why: Product card morph (1.5x on the ear); learnings 2 and 24.

**8.6** · `prompt` · replace
- old: `BODY: her head is turned well away; the left frame edge falls just behind the jaw hinge, so no cheek, eyebrow, eye, nose or lips appear;`
- new: `BODY: the camera is behind her; her head is turned fully away, so the jaw and cheek are hidden behind the ear and hair; no eyelash, eyelid, brow, cheek, nose or lip breaks the outline of her head anywhere in the frame;`
- why: Same face fix as 7.7 (k01-1R wording).

**8.7** · `prompt` · replace
- old: `THE AUNTY: from the right edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu (only a sliver of the pink shows at the frame edge), holds half-moon reading glasses with thin dark tortoiseshell frames so one lens hovers about 8 cm in front of the stud, centred on the yellow stone, about 38% of the frame's width; the glass is perfectly clear, showing what is behind it at the same size, undistorted and untinted, reflecting nothing, never a face or eyes.`
- new: `THE AUNTY: from the lower right edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a deep cocoa-and-wine silk pallu in the same family as the blouse, so the stud stays the only colour in the frame; she holds her folded half-moon reading glasses by one folded temple arm (two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin bridge), below and to the right of the stud, about 4 cm from it, never in front of it: no part of the glasses or her fingers crosses the ear or the stud, and the glass shows only soft dark background. CLEAN SPACE: an evenly lit area about 5 cm across centred on the yellow stone, with only the ear, the lobe and the stud in it and nothing in front of them, so a lens can be drawn over it later; no magnifier and no magnified view anywhere in the picture.`
- why: C1/C5 and the picture push in 8.1.

**8.8** · `prompt` · replace
- old: `COMPOSITION: stud and lens between 33% and 53% of the frame height; from 14% to 32% calm dark cocoa bokeh; below 55% soft cocoa velvet.`
- new: `COMPOSITION: the stud sits just above the middle of the frame, at about 46% of the height and a little left of centre, the ear rising above it; from the top edge to about 30% only dark hair and calm dark cocoa bokeh, calm for the headline; the aunty's hand and glasses only in the lower right, between 56% and 75%; below 56% the cocoa velvet blouse in soft shadow, calm for the price card.`
- why: Landmarks plus percentages.

**8.9** · `prompt` · replace
- old: `LIGHT: soft warm fill from above right;`
- new: `LIGHT, two lights only: soft warm fill from above right;`
- why: Two-light rule.

**8.10** · `prompt` · replace
- old: `NEGATIVES: no text, letters, numbers or logos anywhere; no face or eyes; one product only, no other jewellery on anyone; no pastel or pale background; no bottles or glasses in sharp focus.`
- new: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark anywhere; no face, no eyes, no eyebrows; one product only: one stud, no second earring and no other jewellery on anyone; no rani pink and no other bright colour anywhere but the stones; no pastel or pale background; no bottles or drinking glasses in sharp focus; no blue or green stone; never seven or eight pearls.`
- why: Exact clauses; the lock's morphs as negatives.

**8.11** · `beat` · set
- set to: `Haan. Baaki sab cocoa.`
- why: THE COMEBACK ROW (C4): answers 'so many colours on one ear?' and teaches the styling tip (wear it with a neutral) in four words.

**8.12** · `layout` · set
- set to: `LOG: 'COCKTAIL · 10:05 PM · INSPECTION 8 OF 10'. EYE-CHART HEADLINE, no acuity marks on the Feed: ITNE RANG, (Feed 120 px) / EK KAAN PE? (90), bone, x 128 from y 112. COMEBACK ROW directly under it, about y 340-430: 'Haan. Baaki sab cocoa.' in Cormorant italic 500, 96 px, gold-light. THE LENS: an SVG half-moon (flat top, dark tortoiseshell rim) drawn over the stud, about 440 px wide, filled with exactly 2.0x of the same plate about the yellow stone and clipped to the rim, in y 460-800, the whole arc inside the glass with a margin; scale tag at 5 o'clock: 'IN HER LENS ABOUT 2× · ACTUAL 20 MM ARC'. THE MATCHING CARD, the one device (left column x 72-300, y 470-790): a bone 1.5 px hairline card with a 26 px SVG staple at its top; three 120 x 56 px pinked swatches filled with the lilac, pink and lemon colour-picked from the stones in this photograph, each tied by a 1 px gold-light leader to its stone's claw in the lens, with no words; a fourth swatch in the cocoa colour-picked from her blouse, with a bone chalk tick and the card's one label 'YOUR BLOUSE · ANY NEUTRAL'. No 'MATCHING CENTRE' header, no FIG callout and no seal on the Feed. F2 card on plum from y 990: PRISM CLUSTER STUDS; the 6/6 line 'RHODIUM SILVER TONE · CUBIC ZIRCONIA · PRE-ORDER'; ₹1,299; the offer box with three order-slip tick boxes, the first ticked, then 'THIS + ANY TWO · BUY3 · 20% OFF'; the wordmark; 'FREE INSURED SHIPPING · CASH ON DELIVERY'. STORY: the plate full bleed, no empty block; log y 276, headline y 304 with the acuity marks, comeback under it, lens y 660-990 with the matching card beside it and its swatch labels (PURPLE PRINCESS CUT · PINK BAGUETTE · YELLOW EMERALD CUT, 6 MM), seal top right, compact card y 1030-1250; one FIG on the Story only: FIG. 4 · SIX TINY WHITE PEARLS 'aur yeh chhote safed?'.`
- why: Type budget (C4): the matching card keeps one label on the Feed; the cut names move to the Story.

**8.13** · `offer` · set
- set to: `THIS + ANY TWO · BUY3 · 20% OFF`
- why: Basket rate 0.0 (C9).

**8.14** · `primaryText` · set
- set to: `Itne rang, ek kaan pe? Haan. Lilac, pink and lemon in one 20 mm arc. ₹1,299, pre-order. Any three, 20% off with BUY3. Wear it with cocoa or black.`
- why: 146 characters, BUY3 ends at 116. Pre-order and no claims.

**8.15** · `risk` · replace
- old: `Hedge take: the aunty's hand from the left with a wine-coloured pallu and no bar cart.`
- new: `The wine pallu is now take A (8.1, 8.7). No take B (learnings 16). A failed take gets one redo on seedream_v5_pro, 2k (2.5 credits): on k07-2 it held the six-pearl map that gpt_image_2_6 medium broke with a seventh pearl.`
- why: k07a verify k07-2 (take A gpt medium fail on a seventh pearl; R seedream pass).

## 5. Card 9 · Marquise Drop Choker · ₹999 · PAIN / TRUST · "PICHLI SHAADI MEIN BHI YAHI THA?"

**The push:** the aunty's fingertips are bright yellow with the haldi she has just put on the bride, which makes this
unmistakably the haldi and keeps the paste away from the choker. The repeat register becomes the basket meter: three
functions, one ticked.

**9.1** · `picture` · replace
- old: `The aunty's lens hovers over the marquise and its claws.`
- new: `The aunty, her fingertips bright yellow with the haldi she has just put on the bride, holds her folded glasses low at the edge; in the finished ad her lens is drawn over the marquise and its claws.`
- why: PUSH: the haldi on the aunty's own fingers makes the frame unmistakably the haldi; drawn lens (C1).

**9.2** · `prompt` · replace
- old: `Vertical 9:16 editorial wedding-morning photograph at 4K (2160 x 3840), 85 mm lens, front-on: a young Indian woman's neck and collarbones at her haldi, cropped from just below the chin to the top of the chest, so no chin, lips or face appear; a marigold-yellow cotton kurta with a deep V neck.`
- new: `Vertical 9:16 editorial wedding-morning photograph at high resolution, a full-bleed photograph edge to edge with no borders, bands or panels, 85 mm lens, front-on: a young Indian woman's neck and collarbones at her haldi. The top edge of the picture cuts straight across the middle of her neck, well below the jaw, and her ears are outside the frame: no chin, jaw, lips, nose, eye, eyebrow or earring anywhere in frame. A marigold-yellow cotton kurta with a deep V neck.`
- why: Same neck-crop fix as 6.2 (k01-5A/5R).

**9.3** · `prompt` · replace
- old: `Reference 1 is the authority on this exact piece: copy the necklace's construction exactly and ignore its background and light; reference 2 shows it worn at true scale.`
- new: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece worn on a woman at true size (a 41 cm ribbed collar about 2 mm thick, snug at the base of the neck; the 12.3 mm marquise lies sideways, about as wide as the hollow at the base of the throat; the 2 pear drops fall about 4 marquise lengths, the end pear landing on the top of the breastbone, well above the neckline): match that scale and the way it sits exactly; copy only the scale, never a face or a camisole.`
- why: Exact reference sentence. MEDIA: reference 2 becomes the scale crop 706193dc-688e-48ba-b0e1-679c00fd8b13 (refs/marquise-drop-choker/02_scale_crop.jpg) in place of 02.jpg (f2e3533e…), which shows her chin.

**9.3b** · `prompt` · after
- after: `copy only the scale, never a face or a camisole.`
- insert: ` Reference 3 is a close-up of the marquise in its four claws, lying sideways along the ribbed collar with the fine chain leaving from below it: copy the marquise's orientation, its claws and the collar's ribs from it, never its framing or its size.`
- why: The card's known morph (marquise upright or hanging). MEDIA: add the listing macro 03 af160bac-86eb-4835-be60-5262fb0c6133 (pixel-matched, product card) as reference 3.

**9.4** · `prompt` · replace
- old: `holding exactly two clear pear stones, points up: one small halfway down, one larger at the end.`
- new: `holding exactly 2 (two) clear pear stones, points up, never three: one small halfway down, one larger at the end, about 1.3 times the first. The collar, the four claws, the fine chain and both settings are the same 18k gold tone.`
- why: Learnings 6 and 9.

**9.5** · `prompt` · replace
- old: `SCALE: the collar sits snug at the base of the neck, the marquise in the hollow at the base of the throat, about its width; the end pear lands two to three finger widths lower on the breastbone; field of view about 15 cm wide, so the marquise is about 8% of the frame's width; soft contact shadows.`
- new: `SCALE, set by her body exactly as in reference 2: the collar sits snug at the base of the neck, about as thick as a strand of spaghetti; the marquise lies in the hollow at the base of the throat and is about as wide as that hollow, never wider; the end pear lands two to three finger widths lower, on the top of the breastbone; her neck at its narrowest fills about two thirds of the frame's width; field of view about 15 cm wide; soft true contact shadows under the collar, the marquise and both pears. An earlier ad drew this marquise too large: never wider than the hollow of the throat.`
- why: Learnings 2, 10, 24; product card scale note.

**9.6** · `prompt` · replace
- old: `a few loose marigold petals on the kurta and three or four small clear water droplets on the collarbone.`
- new: `a few loose marigold petals on the kurta, and three or four small clear water droplets only at the outer ends of the collarbones near the shoulders, each at least three finger widths from the drop and never on the collar, the chain or a stone, so no droplet can be read as a third stone.`
- why: Learnings 27: liquid never sits on the piece (a drop beside two clear pears reads as a third).

**9.7** · `prompt` · replace
- old: `THE AUNTY: from the left edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, the wrist under a rani-pink silk pallu, holds half-moon reading glasses with thin dark tortoiseshell frames so one lens hovers about 8 cm in front of the marquise, centred on it, about 34% of the frame's width; the glass is perfectly clear, showing what is behind it at the same size, undistorted and untinted, reflecting nothing, never a face or eyes.`
- new: `THE AUNTY: from the lower left edge, an older Indian woman's hand, about sixty, warm brown skin with soft creases, short bare nails, no rings, bangles, watch or mehendi, her fingertips stained bright yellow with fresh haldi paste because she has just put haldi on the bride, the wrist under a rani-pink silk pallu; she holds her folded half-moon reading glasses by one folded temple arm (two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin bridge), low at the left edge below the collarbone, beside the drop and never in front of it: no part of the glasses, her fingers or the haldi touches or crosses the choker, and the glass shows only soft background. CLEAN SPACE: the front of the collar, the marquise and the whole drop are evenly lit, with nothing in front of them, so a lens can be drawn over the marquise later; no magnifier and no magnified view anywhere in the picture.`
- why: C1/C5 and the picture push in 9.1.

**9.8** · `prompt` · replace
- old: `COMPOSITION: marquise, drop and lens between 33% and 55% of the frame height; from 14% to 32% calm marigold-and-saffron bokeh; below 57% soft yellow cotton.`
- new: `COMPOSITION: the marquise sits just above the middle of the frame, at about 40% of the height and at the centre of the width, the drop falling to about 52%; from the top edge to about 32% the upper neck falls into soft warm shadow, clearly darker than the lit choker, with marigold-and-saffron bokeh at both sides of the neck, calm for the headline; the aunty's hand only in the lower left, between 56% and 75%; below 57% soft yellow cotton, calm for the price card.`
- why: Landmarks plus percentages; the top band darker for the ink headline.

**9.9** · `prompt` · replace
- old: `LIGHT: soft warm daylight from above left;`
- new: `LIGHT, two lights only: soft warm daylight from above left;`
- why: Two-light rule.

**9.10** · `prompt` · replace
- old: `NEGATIVES: no text, letters, numbers or logos anywhere; no turmeric paste on the necklace; no face; one product only: no earrings, rings, bangles or second necklace.`
- new: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark anywhere; no turmeric paste or water on the choker; no face, no eyes, no eyebrows, no chin; one product only: no earrings, rings, bangles or second necklace; the marquise never upright and never hanging below the collar; never a third stone.`
- why: Exact clauses; the lock's morphs as negatives.

**9.11** · `beat` · set
- set to: `Nahi aunty. Pehli baar.`
- why: THE COMEBACK ROW (C4): answers the repeat-pain question with a first sighting.

**9.12** · `layout` · set
- set to: `LOG in ink: 'HALDI · 10:30 AM · INSPECTION 9 OF 10'. EYE-CHART HEADLINE, no acuity marks on the Feed: PICHLI SHAADI (Feed 100 px) / MEIN BHI (80) / YAHI THA? (62), ink #1A1614, x 128 from y 112, on a soft saffron scrim if the bokeh is bright. COMEBACK ROW directly under it, about y 384-460: 'Nahi aunty. Pehli baar.' in Cormorant italic 500, 76 px, oxblood. THE LENS: an SVG half-moon (flat top, dark tortoiseshell rim) drawn over the marquise and its claws, about 380 px wide, filled with exactly 2.0x of the same plate about the marquise's centre and clipped to the rim, in y 480-760; the two pears hang below it at true size, never cut by the rim; scale tag at 5 o'clock: 'IN HER LENS ABOUT 2× · MARQUISE ACTUAL 12.3 MM'. AUNTY'S REPEAT REGISTER, the one device and the basket meter (left column x 72-330, y 480-790): headed 'AUNTY'S REPEAT REGISTER' in Jost caps 14 px .2em ink; three rows HALDI / SANGEET / PHERE in Jost caps 15 px with hairline rules; HALDI's box ticked in oxblood and stamped 'first sighting' in Cormorant italic 32 px oxblood inside a hand-drawn oval at -6 degrees; SANGEET and PHERE empty, waiting for two more pieces. No FIG callout and no seal on the Feed. F2 card on a solid plum panel with a 1.5 px gold-light hairline, y 990-1266: MARQUISE DROP CHOKER; the 6/6 line '41 CM + 5 CM · 18K GOLD TONE PVD · WATERPROOF · TARNISH FREE'; ₹999; the offer box 'THIS + ANY TWO · BUY3 · 20% OFF' (no tick boxes: the register is the meter); the wordmark; 'FREE INSURED SHIPPING · CASH ON DELIVERY'. STORY: the plate full bleed, no empty block; log y 276, headline y 304 (100/80/62) with the acuity marks, comeback under it, lens y 690-980 with the register beside it, the seal in oxblood top right, compact card y 1030-1250; one FIG on the Story only: FIG. 1 · MARQUISE, SET SIDEWAYS 'naya hai', its leader from a claw.`
- why: Type budget (C4); the register becomes the basket meter (three functions, three pieces).

**9.13** · `offer` · set
- set to: `THIS + ANY TWO · BUY3 · 20% OFF`
- why: Basket rate 0.0 (C9).

**9.14** · `primaryText` · set
- set to: `Pichli shaadi mein bhi yahi tha? Nahi aunty, pehli baar. Marquise Drop Choker, ₹999. Any three, 20% off with BUY3: a new piece for every function. Waterproof.`
- why: 158 characters, BUY3 ends at 113. Waterproof is on the product card.

**9.15** · `risk` · replace
- old: `Hedge take: the same crop at a night sangeet in a plum silk blouse, keeping the register.`
- new: `No take B (learnings 16). One redo on gpt_image_2_6 medium; if the daylight warms the clear stones or the marquise stands up again, the redo moves to a night sangeet in a plum silk blouse, keeping the register and the haldi-stained fingertips out.`
- why: Learnings 16.

## 6. Card 10 · Verdant Eternity Band · ₹1,049 · OFFER / SELL · "AUNTY KI KITTY BHI LEGI."

**The push:** card 5's order slip comes back with four lines: MAUSI US 5, BUAJI US 7, CHACHI US 9 and PADOSAN US 6.
This time the padosan is not struck out. The comeback "Is baar padosan bhi." pays off the series, and the slip shows a
basket of four for BUY4. The ring is worn and seated, as on k04r, the only take of this ring that came out true size.

**10.1** · `picture` · replace
- old: `Four lenses, four 2x views: the S-wave, the open back, the green ovals, the bright rhodium. Their tags carry their ring sizes (US 5, 7, 9 and 6), all inside the band's US 5 to 9, and the padosan who was struck off on card 5 is back: 'is baar main bhi'.`
- new: `One honest 2x lens is drawn over the ring: the S-wave, the green ovals, the bright rhodium (the open back stays hidden on the palm side, so no lens claims it). Their ring sizes (US 5, 7, 9 and 6, all inside the band's US 5 to 9) fill the four lines of her order slip from card 5, back again, and this time the padosan's line is not struck out: 'is baar padosan bhi'.`
- why: TRUTH: a palm-down hand hides the open back, so a lens labelled OPEN BACK would show what the plate does not; four lenses cannot all sit honestly on one 18 mm ring. BASKET: the order slip shows a basket of four.

**10.1b** · `picture` · replace
- old: `From the four frame edges, only the fingertips and thumbs of four aunties grip four pairs of half-moon reading glasses, each with a sliver of a different pallu at the very edge (rani pink, mustard, parrot green, peacock blue).`
- new: `From the two side edges, only the thumbs and fingertips of four aunties pinch four pairs of folded half-moon reading glasses, each hand with a sliver of a different pallu (rani pink, mustard, parrot green, peacock blue).`
- why: Exactly four hands, side edges only (10.6).

**10.2** · `prompt` · replace
- old: `Vertical 9:16 editorial overhead photograph at 4K (2160 x 3840), 50 mm lens looking straight down at a kitty-party table the Sunday after a wedding, covered in deep plum velvet with a scalloped cream lace runner along one edge.`
- new: `Vertical 9:16 editorial overhead photograph at high resolution, a full-bleed photograph edge to edge with no borders, bands or panels, 50 mm lens looking straight down at a kitty-party table the Sunday after a wedding, covered in deep plum velvet with a scalloped cream lace runner along the bottom edge.`
- why: 2k render; learnings 5; the lace moves out of the headline band.

**10.3** · `prompt` · replace
- old: `Reference 1 is the authority on this exact piece: copy the ring's construction exactly and ignore its cube, background and light; reference 2 shows the ovals and the wave from above.`
- new: `Reference 1 is the authority on this exact piece: copy its construction exactly and ignore its background and light. Reference 2 is a detail of the same piece from above: it shows how the ovals alternate either side of the wave. Reference 3 shows this exact ring worn on a finger at true size (about 16.5 mm inside, US 6; oval stones about 5 x 4 mm; about 5 green ovals span the top of the finger; the band no wider than the finger): copy its scale and the way the band sits on the finger exactly; never copy a face, neck, hair, strap or background from it.`
- why: Exact reference sentence; MEDIA: add the scaleRef 6286cc23-cfde-49e6-b57a-b5c3745af05a as reference 3 (k03r k03-1 wording).

**10.4** · `prompt` · after
- after: `never a straight row of ovals and never a full ring of pave around each oval; do not redesign or add anything.`
- insert: ` THE WAVE, exactly as reference 2: one single slim line of tiny clear stones snakes across the front in an S, curving under one oval and over the next; each green oval is cupped by the wave on one side only, and its other side is bare claws and metal; never a second line of clear stones. Never a closed ring. The band, the claws and the looped tips are all the same cool rhodium silver tone.`
- why: k04r k04-3 and k09a k09-3 held the S-wave with this paragraph on gpt_image_2_6.

**10.5** · `prompt` · replace
- old: `SCALE: about five ovals span the top of the finger; field of view about 20 cm wide, so the ring is about 10% of the frame's width; a crisp contact shadow on the velvet beside the finger. HAND: the young woman's left hand lies flat and relaxed in the centre of the frame; warm wheatish skin, five fingers, correct anatomy, short bare nails, no other ring, bangle or watch.`
- new: `HAND: the young woman's left hand enters from the bottom edge and lies flat and relaxed, palm down, fingers pointing up toward the top edge; warm wheatish skin, five fingers, correct anatomy, short bare nails, no other ring, bangle or watch. The ring is WORN on her ring finger: slid all the way down and seated snugly at the base of that finger just beyond the knuckle, the front wave of clear pave and the green ovals facing up toward the camera, its open back hidden on the palm side; never loose, never held, never on any other finger. SCALE, the most important instruction: her fingers are big in the frame and the ring is small and fine on them. Field of view about 20 cm wide: each of her fingers is about one twelfth of the frame's width and her hand from wrist to fingertips is about half the frame's height; the band is exactly as wide as the finger it sits on, never wider and never hanging loose; it is about 6 mm deep along the finger, much shorter than the finger's lowest segment; about 5 green ovals span the top of the finger, each about a third as wide as her fingernail. Held or pinched, this ring came out two to four times too big (k03-1, k04a); worn and seated it came out true (k04r): never a chunky, bangle-sized or giant ring. A true contact shadow where the band meets her skin and where her hand rests on the velvet.`
- why: k04r k04-3 passed at 1.1-1.25x with the ring worn and seated; k03r k03-1A failed at 2.3x pinched (learnings 24, 25).

**10.6** · `prompt` · replace
- old: `THE KITTY: at the four frame edges, only the fingertips and thumbs of four older Indian women (about sixty, warm brown skin with soft creases, short bare nails, no rings, no bangles, no watches) enter the frame, each pair gripping the temple arm of half-moon reading glasses with thin dark tortoiseshell frames; a sliver of a different silk saree pallu shows at each edge: rani pink upper left, mustard upper right, parrot green lower left, peacock blue lower right; the four pairs of glasses point their lenses toward the ring hand at different angles, one lens of each hovering about 6 cm above the hand, two of them over the ring itself, each lens about 22% of the frame's width; the glass is perfectly clear, showing what is behind it at the same size, undistorted and untinted, reflecting nothing, never a face or eyes.`
- new: `THE KITTY: exactly four older Indian women's hands (about sixty, warm brown skin with soft creases, short bare nails, no rings, no bangles, no watches) enter from the two side edges, two from the left and two from the right, between about 33% and 62% of the frame's height; each shows only a thumb and two fingertips pinching one pair of folded half-moon reading glasses (two flat-topped D-shaped lenses with the straight edge on top, thin dark tortoiseshell rims, a thin bridge) by a folded temple arm, the glasses lying on the velvet and pointing toward the ring hand; no glasses, fingers or pallus come nearer the ring hand than the width of two fingers, and no glass lies over the hand; the glass shows only plum velvet. A sliver of a different silk saree pallu at each of the four hands, dull and in soft shadow: rani pink upper left, mustard upper right, parrot green lower left, peacock blue lower right; the green ovals stay the most saturated green in the frame. CLEAN SPACE: an evenly lit area about 5 cm across centred on the ring, with only her finger and the ring in it, so a lens can be drawn over it later; no magnifier and no magnified view anywhere in the picture.`
- why: C1/C5; the card's own risk (up to twenty fingertips): exactly four hands, side edges only, out of the headline and card bands.

**10.7** · `prompt` · replace
- old: `COMPOSITION: ring hand and lenses between 32% and 58% of the frame height; from 12% to 30% calm plum velvet; below 60% calm plum velvet and the lace edge.`
- new: `COMPOSITION: her fingertips reach up to about 30% of the frame's height; the ring sits at about 46% of the height, just right of centre; from the top edge to 30% only calm plum velvet, calm for the headline; the aunty hands only at the side edges between 33% and 62%; below 62% the back of her hand and her wrist fall into soft shadow on dark velvet, and the lace runner lies along the bottom edge, calm for the price card.`
- why: Landmarks plus percentages.

**10.8** · `prompt` · replace
- old: `LIGHT: soft warm overhead fill;`
- new: `LIGHT, two lights only: soft warm overhead fill;`
- why: Two-light rule.

**10.9** · `prompt` · replace
- old: `NEGATIVES: no text, letters, numbers or logos anywhere; no playing cards, tickets, papers or cups; no faces; no jewellery on any aunty; no extra fingers; one product only.`
- new: `NEGATIVES: no text, no letters, no numbers, no logos, no watermark anywhere; no playing cards, tickets, papers or cups; no faces, no eyes, no eyebrows; no jewellery on any aunty; exactly four aunty hands and one young hand, no extra fingers; one product only: this one ring, no second ring on any finger; never a closed full-eternity ring.`
- why: Exact clauses; the card's morphs as negatives.

**10.10** · `beat` · set
- set to: `Is baar padosan bhi.`
- why: THE COMEBACK ROW (C4): pays off card 5's struck-out 'padosan ke liye · agli baar'.

**10.11** · `layout` · set
- set to: `LOG: 'KITTY PARTY · SUNDAY 4 PM · INSPECTION 10 OF 10'. EYE-CHART HEADLINE, no acuity marks on the Feed: AUNTY KI KITTY (Feed 108 px) / BHI LEGI. (82), bone, x 128 from y 112. COMEBACK ROW directly under it, about y 316-400: 'Is baar padosan bhi.' in Cormorant italic 500, 92 px, gold-light. THE LENS: one SVG half-moon (flat top, dark tortoiseshell rim) drawn over the ring, about 400 px wide, filled with exactly 2.0x of the same plate about the ring's centre and clipped to the rim, in y 440-780: the S-wave, the green ovals and the bright rhodium, the whole front of the band inside the glass with a margin; scale tag under it: 'IN HER LENS ABOUT 2× · OVALS ACTUAL 5 × 4 MM · ADJUSTS US 5 TO 9'. THE ORDER SLIP, the one device (card 5's slip back again; right gutter x 740-1008, y 470-790): a bone hairline slip, four lines in Jost 500 caps 15 px, '1 · MAUSI · US 5', '2 · BUAJI · US 7', '3 · CHACHI · US 9', '4 · PADOSAN · US 6', each with a gold-light tick, the fourth unstruck this time. No FIG callout, no kitty ruler and no seal on the Feed. F2 card on plum from y 990: VERDANT ETERNITY BAND; the 6/6 line 'ADJUSTABLE US 5 TO 9 · WATERPROOF · TARNISH FREE · HYPOALLERGENIC'; ₹1,049; the offer box enlarged to two lines: four order-slip tick boxes, all ticked, before 'ANY FOUR · BUY4 · 30% OFF' in gold-light, then 'ANY THREE · BUY3 · 20% OFF'; the wordmark; 'FREE INSURED SHIPPING · CASH ON DELIVERY'. STORY: the plate full bleed, no empty block; log y 276, headline y 304 with the acuity marks, comeback under it, lens y 640-1000 with the slip beside it, the seal top right reading KITTY APPROVED, compact card y 1040-1250.`
- why: Type budget (C4); basket made visible: a slip of four rings for BUY4.

**10.12** · `sizeLine` · set
- set to: `IN HER LENS ABOUT 2× · OVALS ACTUAL 5 × 4 MM`
- why: One honest lens, not four (10.1).

**10.13** · `offer` · set
- set to: `ANY FOUR · BUY4 · 30% OFF ◆ ANY THREE · BUY3 · 20% OFF`
- why: The batch's close leads with the bigger basket (threshold: strengthen card 5, the batch's fifth card).

**10.14** · `primaryText` · set
- set to: `Four aunties, four sizes, one ring that adjusts from US 5 to 9. ₹1,049. Any three, 20% off with BUY3; any four, 30% off with BUY4. Free insured shipping, cash on delivery.`
- why: 171 characters, BUY3 ends at 100. OFFER card, so the owner's trust line goes in.

**10.15** · `motion` · replace
- old: `from 0.6 to 2.0 s the four 2x lens composites open one after another (an iris wipe from each lens centre, 0.35 s each), each with an aunty's 'tch', and each tag types on with its US size; from 2.2 to 3.0 s the four sizes drop as dots onto the US 5 to 9 kitty ruler under the ring;`
- new: `from 0.6 to 1.0 s the one 2x lens opens over the ring (an iris wipe from its centre); from 1.2 to 2.8 s the four slip lines write on one after another, each tick landing 0.4 s apart, the padosan's line last and unstruck; from 2.8 to 3.2 s the comeback row 'Is baar padosan bhi.' sets in;`
- why: One honest lens (10.1); the slip device (10.11).

**10.16** · `motion` · replace
- old: `Sound: four voice actors overlapping ('lehar jaisi', 'mujhe bhi aayegi?', 'mehendi jaisa hara', 'is baar main bhi'), then laughter and a teacup clink.`
- new: `Silent (owner ruling 5: no voice or music in this run).`
- why: Owner ruling 5.

**10.17** · `risk` · set
- set to: `Fingertips multiplying at the edges (now exactly four aunty hands, side edges only), jewellery creeping onto the aunties, glasses drifting over the ring hand, the ring drawn two to four times too big when it is not seated (k03-1, k04a), and the wave straightening into a row or closing into halos (the card's known morph). No take B (learnings 16). One redo on gpt_image_2_6 medium; if the hands multiply, the redo keeps two aunties (rani pink left, mustard right) and the slip keeps all four lines.`
- why: Learnings 16; the evidence from k03r, k04r and k09a on this ring.

**10.18** · `why10` · replace
- old: `four aunties with four ring sizes on one US 5 to 9 ruler make the adjustable fit the proof and BUY4 the joke, not a discount banner.`
- new: `four aunties with four ring sizes on one order slip make the adjustable fit the proof and BUY4 a basket of four, not a discount banner.`
- why: Order slip replaces the ruler (10.11).

## 7. Variation plan (three per ad, on the approved plate; PLAN §6 step 6)

**Rules from the k01a rating.**

- B (V2, a pushed headline on a clean two-row layout) won k01-4 by 0.04. It led on 200 px (5.92), stop (6.5) and copy
  (7.17).
- A (V1, the bible as written, about 14 text elements) had the higher would-buy (5.67 against 5.33), 4 of 6 buy-yes and
  half the customer favourites. It lost on layout (5.33).
- C (V3, a cream eye-chart poster over a half-circle crop) lost on everything: the piece was a sliver, and the Story was
  half empty.

Every k01b variation therefore carries:

- the six-element Feed and the comeback row directly under the headline;
- the photograph on at least 55% of the Feed, never a poster ground;
- a full-bleed Story with no empty block;
- the drawn lens at least 30% of the Feed width (learnings 17);
- the whole piece visible at true size outside the lens.

| Ad | V1 (A: the bible after this diff) | V2 (B: push the device) | V3 (C: lead with the basket) |
|---|---|---|---|
| k01-6 | the shaadi-card headline, 'Love cum arranged.', two lenses | the two lenses grow to about 340 px each and the drawn bridge sits over the knot between them; headline two rows: GOLD TONE / weds SILVER TONE. | comeback becomes 'Teen function, teen naye.'; the offer box doubles in size; the lenses stay |
| k01-7 | the mala count, 'Phir poocha: kahan se?' | the lens grows to about 640 px and the two count rings fill the lens zone; headline one row: TWENTY. TWICE. | comeback 'Teen function, teen naye.'; offer box doubled |
| k01-8 | the matching card, 'Haan. Baaki sab cocoa.' | the matching card leads: four swatches across the full width under the lens, the cocoa one ticked; lens 480 px | comeback 'Teen function, teen naye.'; offer box doubled |
| k01-9 | the register as the basket meter, 'Nahi aunty. Pehli baar.' | the register grows to the full left half beside the lens, and the 'first sighting' stamp crosses its rule | the register's three rows ARE the offer: HALDI ticked, SANGEET and PHERE as empty boxes beside 'THIS + ANY TWO · BUY3 · 20% OFF' |
| k01-10 | the order slip of four, 'Is baar padosan bhi.' | the slip becomes the hero: a torn paper slip about 40% of the Feed, the lens over the ring beside it | comeback 'Chaar aunty. Chaar ring.'; the BUY4 line takes the comeback's size |

The V3 lines carry no claim and no number beyond the codes. "Teen function, teen naye." means a new piece for each of
three functions, which is the camp's BUY3 reason.

## 8. Checks after applying (for the applier and the verifier)

- No card 6-10 prompt still contains "4K", "hovers", "centred on it" (for a real lens), "voice actor", "Sound:", "Hedge
  take" or "between 33% and 53%". The simulation found none left.
- Count-gated printing:
  - card 7's numerals only at exactly 20 baguettes;
  - card 8's swatches only from the stones actually in the plate;
  - card 10's slip sizes are all inside US 5 to 9;
  - no line-up or trace of parts the plate does not show (learnings, k01a section).
- The drawn lens's inner glass is at least 2.3 times the magnified part, and the piece never crosses the rim.
- Primary texts: BUY3 ends at 116, 120, 116, 113 and 100 (cards 6-10), and the carousel text at 121.
- Every card links to its own product page. There is no BUY3 collection.
