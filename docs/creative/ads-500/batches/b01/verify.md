# b01 picture verification (19 Nov 2026)

Verifier pass on the five b01 pictures in `pics/`, checked against `brief.md` (acceptance lists), `build/study/products.md`
(the truth sheet) and the reference photos `build/refs/<handle>__*.jpg`. Zoomed crops are in `tmp/`.

## Result

| Id | Product | Verdict | Deciding reason |
|---|---|---|---|
| b01-1 | Cushion Halo Ring | **pass-with-notes** | The product and its proportions match the packshot. Three small star glints are left in. The ring spans 32% of the width (the rule is 35%). Move the card down to 930. |
| b01-2 | Brushed Gold Huggies | **dropped** | Scale: each huggie renders 1.15× the jasmine bud (the brief requires 0.6–0.8×), which reads about 1.6× true size. The shadows and the bud sit under both cards. |
| b01-3 | Verdant Eternity Band | **dropped** | The fingers point down into the card zone (fingertips to 71.5%), and the ring sits at 46–52%, where the Story card goes. No calm zone exists for either card. The pavé also drifted into a full halo around each oval. |
| b01-4 | Woven Gold Hoops | **dropped** | The camera is at about 35–40°, not the 15° asked for, so the hoop fills 29–69% of the height. It runs through the headline band and the card band, and no Feed layout fits. |
| b01-5 | Prism Rivière Bracelet | **dropped** | Scale: the stone pitch is 24% of the wrist width (true is about 15%), so the bracelet reads 1.35–1.55× too big. It also sits at 49–53% height instead of 28–32%, and the hand is a clenched fist. |

**No regeneration was possible.** The Higgsfield balance read at verification was **2.46 credits**. The generator reported
26.46 right after the batch, so another session on the account has since spent 24. One picture costs about 3.6 credits, so
even one regeneration would take the balance below the 10-credit floor. RULINGS §1.3 says to stop production under 10, so
**production has to stop until the owner tops up**. The four dropped slots have corrected prompts below, ready to run as
one `generate_image_batch` call once there is enough credit (4 × 3.6 ≈ 14.4 credits, plus the 10 floor, so about 25 credits
needed). `jobs.json` is unchanged because nothing was regenerated.

Coordinates: the source is 1536 × 2752. `.pic` uses `object-fit: cover`, so the picture scales to 1080 × 1935. Story y = src_y × 0.703 − 7.5 and Feed y = src_y × 0.703 − 292.5.

---

## b01-1 · Cushion Halo Ring · A6 spotlight · pass-with-notes

Job `1f468bb4-0eff-42d6-a6c8-d4446c35d607`. The job reported the `nano_banana_2` model, although `nano_banana_pro` was requested.

**Fidelity (against `cushion-halo-ring__upright.jpg` and `__macro.jpg`)**
- One round brilliant clear centre stone held by **4 claws** (back, left, right and front all visible). Pass.
- The halo is a single sparkling rim with rounded-square corners. The camera sits about 10° above the pedestal and the ring stands upright, so the halo face is seen nearly edge-on. That makes "cushion, not round" only partly readable, though nothing reads round or as two rows. The halo's side wall has a scalloped, bead-like gallery the real piece lacks; at Feed size it reads as texture. Minor note.
- One row of pavé runs down the right shoulder and a row of small stones runs down the left. Pass.
- Cool silver tone everywhere, with no gold cast. Pass.
- **Open back:** the bottom of the band, at the velvet, looks continuous and the overlapping ends do not show. That is plausible, because the overlap sits at the contact point, in the nap and the shadow. Minor. The card line carries "adjustable".
- Proportions match the packshot: stone width ÷ total ring height is 0.38 here and 0.38 in `__upright.jpg`. One product, no extra jewellery, no ring box, no hands, no text.

**Scale and width share**
- The ring spans x 536–1031 of 1536, which is **32.2% of the width**. The brief asks 35–40% and learnings rule 1 sets 35%. That is short by about 3 points. It cannot be fixed by resizing, so it is accepted as a note.
- On the 1080 canvas the ring is 348 px wide, about 17 px/mm for a ring roughly 20 mm across. That is under 19 px/mm, so **no size tag**.
- The pedestal is about 2.6× the ring's width, roughly 5 cm. That is a believable ring-box cushion and does not mislead.
- The ring spans 34.0–59.4% of the frame height. The brief wanted the base at 57% or higher in the frame, and it sits at 59.4%. Inside the central 4:5. Pass.

**Negatives**
- **Three small star-shaped glints**: on the stone's top facet, on the right claw, and on the inner band near the base, at about Feed (540,355), (640,385) and (500,790). They are small, with rays of about 25–35 px at 1080. The brief bans them. They cannot be edited out, so they stay as a note. This is the weakest point of the frame.
- The glow is a soft diagonal beam from the top-right corner down toward the ring, not only the corner (x over 75%, y under 25%) asked for. It is faint (mean luminance 29), and the headline band stays dark.
- No flare, text, logos, people or water.

**Calm zones (measured luminance, 0–255)**
- **Feed (1080 × 1350):**
  - Ring box: x 377–725, y 365–858.
  - **Headline band y 84–300: dark and empty** (mean luminance 15–22). "LOOKS LIKE / A PROPOSAL." and the beat at the brief's positions (72/96, 232/166, beat 232/244, ending about 290) clear the ring top at 365 by 75 px. Pass.
  - **Card: do not use the brief's top of 880.** The ring base and its contact shadow reach y 858, which would leave a 22 px gap under the wordmark. **Set `.card` top to 930**; it ends about 1258, inside the safe area that ends at 1266.
  - Under the card: from 930 to about 1040 is the lit top of the oxblood velvet pedestal (mean luminance 33–48, 95th percentile 76–88, visible nap). From 1050 to 1258 is the near-black pedestal front (luminance 11 or less).
  - Bone and gold-light type both pass contrast there. **Use the brief's scrim** (`.scrim` top 760, `rgba(110,31,35,0)` → `rgba(110,31,35,.6)`) to calm the velvet nap behind the wordmark and the name.
- **Story (1080 × 1920):**
  - Ring box: x 377–725, y 650–1143.
  - Dark, empty band at y 270–630.
  - Lit velvet from about 1010 to 1330, then black below 1340.
  - The brief's Story has no text (the A6 twin), so nothing needs to move. If text is ever added, put it in 270–600.
- **Where type must NOT go:**
  - x 360–745, y 345–880 (Feed), which is the ring plus a 20 px margin;
  - the glint above the stone at Feed y 340–365.
  - Nothing may cross the ring's shadow ellipse on the velvet (Feed y 830–960, x 180–650) except the card itself, which starts at 930 and is fine there.

**If it is ever rerun** (not needed now):
- Replace the glint negative with "soft round specular highlights only; no rays, no cross- or star-shaped sparkle".
- Ask for the ring "about 37% of the frame width, its base resting at 55% of the frame height".

---

## b01-2 · Brushed Gold Huggies · A13 levitation · dropped

Job `65ea7f6a-eedd-46a7-bce6-a1b5be21d04d`.

**Fidelity: good**
- Exactly 2 huggies, a wide barrel band, zero stones.
- Brushed-satin finish with fine parallel lines and no mirror polish.
- The front one shows its broad face and the right one shows its C profile with the hinge opening. Width to height is 0.72, against 9.8/14 = 0.70.
- The gold tone is a warm-neutral pale yellow, never orange and never silver.
- The left huggie's lower third has a soft, slightly smeared edge and a pale reflection band (minor).

**Scale: FAIL**
- Each huggie is about 480 px tall in the source and 346 px wide. The jasmine bud, stem included, is about 416 px long, and only about 245 px for the white bud body.
- **Huggie ÷ bud = 1.15** (2.0 against the white bud alone). The brief's acceptance is **0.6–0.8**.
- The bud lies nearer the camera than the shadows, so its true size is even smaller relative to the huggies.
- A viewer reads each huggie as about 2.2–2.4 cm tall against a real 14 mm, about **1.6× true size**. A "Shown magnified" tag cannot rescue this, because the referent in the same frame contradicts it.
- The pair spans 22–80% of the width (58%) against 40–48%.

**Composition: FAIL**
- The pieces sit at 36–54% height.
- The shadows sit at 59–66% and the bud at 66–72%. In the Feed that is y 849–1119, x 91–893, right under the card (880–1208). In the Story it is y 1134–1404, under the card (995–1250).
- The card would cover the levitation proof and the scale referent, and no other card position meets the fixed F2 card.

**Corrected prompt** (refs unchanged: slot 1 `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f` pack, the authority; slot 2 `4c630657-80e8-47f5-ad65-1f0938c70900` macro, finish and barrel shape only):

> Product still life in a 9:16 vertical frame, everything at true life size, camera low at about 12 degrees above the floor, 100 mm macro lens: a pair of Brushed Gold Huggies hover side by side about 1 cm apart, about 1 cm above a flat matte sky-blue floor that curves up into a sky-blue wall with no horizon line. Directly below each huggie lies its own crisp, soft-edged darker-blue shadow, separated from the piece by a gap of clean floor about half a huggie tall. One fresh white jasmine bud, 2 cm long including its short green stem, lies on the floor right between the two shadows, at the same distance from the camera as the shadows, never nearer the camera, so the bud and the huggies can be compared directly: each huggie is clearly SHORTER than the bud, only about two thirds of the bud's length; the bud must always read longer than either huggie, never shorter. Each huggie, exactly as in reference 1: a chunky huggie 14 mm tall and 9.8 mm wide, a wide softly domed barrel-shaped band about 6 mm deep, in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, hidden hinge, zero stones; one shown in three-quarter front view with its broad brushed face to the camera, the other turned a little to show its curved C profile. The finish must stay matte and light-scattering, never mirror-polished, ridged, hammered or stone-set, and never a thin or large hoop. Size in the frame: each huggie is about 20% of the frame width tall and 14% of the frame width wide; the bud is about 30% of the frame width long; the pair together spans about 44% of the frame width, centred. Placement: the huggies sit between 30% and 41% of the frame height, their shadows and the bud between 43% and 50%; nothing at all is below 51% of the frame height: everything from 51% to the bottom is empty, evenly lit sky-blue floor for the price card, and the band from 15% to 28% is empty sky-blue wall for a headline; nothing touches the frame edges. Light code L1: one hard spotlight from directly above and slightly in front throws the two shadows straight down; one large soft fill from the front at low power shows the fine brush lines as one broad soft sheen on each band; the gold tone stays warm-neutral against the blue, never orange, brassy or reading as silver tone. No hands, no people, no strings, wires, stands, pins or supports of any kind, no text, no logos, no other jewellery, no extra buds or petals, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets.

---

## b01-3 · Verdant Eternity Band · A1 mehendi card · dropped

Job `148681d1-1f35-4c98-a03f-1f90090fd773`.

**Fidelity: partly right**
- About 5 green ovals show (3 full, 2 partial), in 4 claws.
- Emerald green, not teal; cool silver tone; no gold.
- **The pavé has drifted:** each oval is ringed almost completely by pavé, so it reads as a chain of haloed ovals with the pavé lines crossing between them. The real piece has one S-wave cupping the ovals on alternating sides. At Feed size it still reads "green ovals in a pavé wave", but this is the documented morph direction. It goes into the corrected lock.

**Scale: pass**
- The ring sits on the **ring finger**: from the left, the thumb at top left, then index, middle, ring and little. Traced through the knuckle creases.
- Each oval is about 4.8 × 3.9 mm by the finger-width ruler (true 5 × 4), and about 0.39× the nail width.
- The ring spans x 340–447 of 720, which is **14.9% of the width** (the rule asks at least 12%; the target is 14–18%).
- The field of view is about 12 cm.

**Styling: pass**
- Henna-dipped fingertips and a henna vine; the skin around the ring is clear.
- No other jewellery, natural skin texture, no face.
- The lattice falls only on the silk at the top left, and the ring is in clean sun.
- The thumb is visible, though the prompt asked for it tucked under the palm (minor).

**Composition: FAIL**
- The brief wanted the fingers pointing left, with the little-finger tip near 52%. The model turned the hand so the **fingers point down**.
- The fingertips reach **71.5% height** across x 9–62%. In the Feed that is y up to 1091; in the Story, up to 1376.
- The brief's calm zone (from 52% down, x 22–78%, no fingers) does not exist. The Feed card (880–1208) would sit on the fingers.
- The ring sits at 46–52% height, Story y 885–997. The Story card (915–1243) would cover it.
- The only calm area is 72–85% at the bottom, Feed y about 1100–1266. That is 166 px, and the card needs 328. No compliant layout exists.

**Corrected prompt** (refs unchanged: slot 1 `2c3d1209-2571-4e63-95af-807e4650a83a` upright, the authority; slot 2 `702645c3-7920-48ac-afaa-5ce4d51e868a` cube, how the ovals alternate either side of the wave):

> Close editorial hand photograph in a 9:16 vertical frame, 85 mm lens from about 40 degrees above, the frame about 11 cm across at the hand: the left hand of a South Asian person, medium wheatish-brown skin with natural texture, fine knuckle creases and short bare nails, lies palm-down and relaxed on deep cocoa-brown raw silk, lying HORIZONTALLY across the upper part of the frame: the wrist enters from the right edge at about 30% of the frame height, the back of the hand runs to the left, and the four fingers point straight LEFT, side by side and gently apart, the thumb folded under the palm and out of sight; the fingertips stop just inside the left edge. The whole hand stays between 16% and 44% of the frame height; no part of the hand or fingers reaches below 45% of the frame height, and the fingers never point down toward the bottom of the frame. Fresh wedding-season mehendi: the fingertips dipped in deep red-brown henna to the first knuckle and one slim vine of fine henna lines on the back of the hand toward the wrist, the skin around the ring left clear. On the ring finger (the second finger up from the lowest finger), just past the knuckle, the Verdant Eternity Band, exactly as in reference 1: a cool PVD rhodium silver-tone open-back band carrying oval emerald-green cubic zirconia of 5 by 4 mm in 4 claws, about five of them showing across the top of the finger, with ONE slim scalloped S-wave line of tiny clear pavé weaving between them: the wave passes above one oval and below the next, so each oval is cupped by pavé on one side only, alternating top and bottom. It must stay one single wave with the ovals alternating either side of it, never a full pavé halo around each oval, never two pavé lines, never a straight row or plain links, never round or teal stones, and the metal never gold tone. Scale: true size, the band covering the top of the finger from side to side, each green oval about a third of the width of the ring finger's nail, with a faint contact shadow on the skin; the ring sits at about 50% of the frame width and 37% of the frame height, spanning about 16% of the frame width. Scene: everything from 46% of the frame height down to the bottom edge is calm, empty cocoa silk in soft even shade, with no fingers, no hand, no shadow edge and no light pattern in it, for the price card. Light code L4: hard late-afternoon sun through one large opening of a carved stone jaali from the upper left lights the hand and the ring in one clean unbroken patch, so the green stones glow and the pavé sparkles, and throws a crisp lattice of light only onto the silk in the top left corner above and left of the fingertips, never below 30% of the frame height; one soft warm bounce from the right fills the shadows on the skin. No face, no other body parts, no bangles, no other rings or jewellery, no nail polish, no text, no logos, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets.

---

## b01-4 · Woven Gold Hoops · A4 monument macro, claim as proof · dropped

Job `e47d6464-1131-48db-987b-1d4d56899e53`.

**Fidelity: pass, with notes**
- One hoop.
- A many-strand open-wire plait with deep ridge and shadow: not a smooth tube and not a two-strand twist.
- The latch hinge shows at the right.
- Zero stones; rich 18k gold tone.
- Note: the strands are chunkier and fewer than the real piece's fine wires.
- Note: the **disc reads dull and mottled, not polished.**
- No second hoop, no glints, no splash.

**Water: pass**
- Droplets only.
- Those at the hoop's depth are about 2–2.6 mm against a braid of about 5 mm. Two or three are beaded on the braid.
- The large drops in the foreground are nearer the camera.
- Both claims are allowed for Woven (RULINGS §1.1).

**Composition: FAIL**
- The brief asked for about 15° and got about 35–40°; the inside of the hoop shows as a wide oval.
- The hoop fills **29.0–69.0% of the frame height** against the brief's 38–59%. That is Feed y 268–1012 and Story y 553–1297.
- In the Feed, the headline, beat and size tag (y 84–388) need about 300 px above the piece and only about 160 px are free. The card (328 px) needs space below the piece and only about 226 px remain before the safe-area limit at 1266.
- Text would touch the braid in both places.
- Droplets also cover the whole band below 62%, which the brief asked to keep smooth.
- Only the Story twin (wordmark at 300, size tag at 384) would fit. One format alone cannot ship.

**Corrected prompt** (refs unchanged: slot 1 `74ed9a2b-4781-4ab8-b032-fd1b45e847ca` pack, the authority; slot 2 `b77ec5ba-42ce-4a11-99a0-b8aca88138df` detail, braid structure and the flat polished disc latch only):

> Macro product still life in a 9:16 vertical frame, 100 mm macro lens almost at table level, only about 10 degrees above a wet glazed surface, so the hoop lying flat reads as a low, flat ellipse whose total visible height is only about a third of its width; honest shallow macro depth of field with the near side of the braid razor sharp: one hoop of the Woven Gold Hoops pair lies flat on a smooth deep-plum (aubergine) glazed surface, shown monumentally large, its thick braided ring running off the right edge of the frame. The hoop, exactly as in reference 1: a round hoop about 25 mm across made of one thick braid about 5 mm thick of many fine polished 18k PVD gold-tone wires with a deep ridge-and-shadow interlace, a thin hinged latch wire and a small flat mirror-polished disc at the top of the hoop, zero stones; the braid must stay a many-strand plait of fine wires with deep ridges, never a smooth tube, a simple two-strand twist or a few thick ropes, the disc stays bright and mirror-polished, never dull or mottled, and the hoop itself stays round, never oval or larger. Scale: the braid is about a fifth of the hoop's width; the hoop sits with a true contact shadow and a soft reflection in the wet glaze. Placement, which matters most: the whole hoop, including its far edge, the disc and the latch, stays inside the band between 38% and 59% of the frame height; no part of the hoop rises above 37% or falls below 60% of the frame height; it spans about 85% of the frame width, from about 15% of the width to past the right edge, cropped by the right edge only. Water: clear droplets of 1 to 4 mm, each smaller than the braid's 5 mm thickness, only on the glaze close around the hoop between 36% and 62% of the frame height, and a few beaded on the braid itself. Scene: the band from 12% to 36% of the frame height is calm, smooth, softly out-of-focus plum glaze with no droplets at all, for a headline and a size tag, and everything from 62% down to the bottom is calm, smooth, droplet-free plum glaze in soft focus for the price card. Light code L1: one hard low raking spotlight from the left skims across the braid so every wire's ridge and shadow is sculpted and each droplet carries one crisp round highlight and a small shadow; one soft broad fill from the front right at low power keeps the gold tone warm-neutral, never orange, brassy or blown out. No hands, no people, no second hoop, no other jewellery, no props, no text, no logos, no star-shaped glints, no starburst, no lens flare, no splash, no spray, no running water.

---

## b01-5 · Prism Rivière Bracelet · A2 worn flash · dropped

Job `be0bee5a-cfa6-47df-81d2-a839671c22e4`.

**Fidelity: pass**
- Square cushion pastel stones, each in its own pavé halo.
- The order from the left is yellow, aqua, pink, yellow, aqua, pink, aqua: three colours only, and no two neighbours match. No lilac or green.
- Bright silver tone; the clasp is hidden.
- The flash colour is true, the skin is natural with visible hair and texture, and the backdrop carries a hard shadow. No face, no other jewellery.

**Scale: FAIL**
- The wrist is 407 px wide in the source. The centre stone pitch is about 97.5 px and one stone with its halo is about 90 px, so **the pitch is 0.24 of the wrist width**.
- True: 18 cm over about 21 stones gives an 8.6 mm pitch on a wrist about 50–60 mm wide, which is 0.14–0.17.
- So the bracelet reads **about 1.35–1.55× too big**. By the hand-breadth ruler (about 664 px for about 80–90 mm) each link is about 11.7–13 mm against 8.6 mm.
- Only about 7–8 links show across the wrist where about 10 should. The model drew fewer, chunkier links.
- Over the 1.2× limit, so this sells a heavier bracelet than we make.

**Composition: FAIL**
- The bracelet sits at **49–53% height** (Feed y 650–733, Story y 935–1018) against the brief's 28–32%, with its lowest point required at or above 33.5%.
- The brief's Feed headline (y 640–781) would sit on the bracelet. The Story wordmark and headline (772–976) would too.
- The fist fills the top (4–45%) and the forearm skin fills the centre down to 64%, so there is no centred calm band above the sleeve.
- The bracelet spans 31% of the width against 42–52%. That still passes the worn minimum of 12%.
- **The hand is a raised clenched fist** where the brief asked for a relaxed hand. It can read as a protest gesture.

**Corrected prompt** (refs unchanged: slot 1 `f9e23a88-b9d0-47ec-ae01-461a8585a1a9` pack, the authority; slot 2 `8f1ff732-cbc4-47d0-aa07-6d190c0e059e` detail, square halos and the mixed colour order only):

> Editorial flash photograph in a 9:16 vertical frame, 85 mm lens at eye level, the frame about 12 cm across at the wrist: one forearm of a South Asian person with deep brown skin with a cool undertone and natural texture rises straight up from the bottom edge in a fitted matte black crepe sleeve; the sleeve's cuff ends only about 2 cm below the wrist, at about 38% of the frame height, so from 38% down to the bottom edge the frame shows only matte black sleeve and charcoal-black backdrop. The bare wrist is bent back slightly and the hand above it is relaxed and open, fingers loose and softly curled forward, NOT a clenched fist; the top edge of the frame crops across the back of the hand about 6 cm above the wrist, so no knuckles and no fingers are in the frame. On the wrist, at about 30% of the frame height, the Prism Rivière Bracelet, exactly as in reference 1: a slim, delicate single line of small square cushion-cut pastel cubic zirconia about 5 mm, each framed by its own fine square halo of tiny clear pavé so each stone with its halo is only about 7 mm, linked edge to edge in bright PVD rhodium silver tone, about ten stones showing across the front of the wrist, the colours mixing aqua blue, soft pink and pale yellow with no two neighbours the same colour, the fold-over clasp hidden under the wrist; it must stay exactly these three pastel colours, every stone in its own halo, never a fourth colour such as lilac or green, never bare stones, never gold tone. Scale, which matters most: the bracelet band is only about 7 mm tall, about one eighth of the wrist's width, never a quarter of it; the stones are small and delicate against the wrist, never chunky; the wrist spans about 46% of the frame width and the bracelet about 48%, centred, lying flat on the skin with a faint contact shadow. Scene: the bracelet's lowest point is above 33% of the frame height; from 38% down the frame is calm matte black sleeve and backdrop for type and the price card, with nothing bright, no sheen streak and no skin below the cuff; nothing important touches the side edges. Light code L2: one direct on-camera flash, hard and frontal, makes the pastel stones read in true colour with crisp sparkle and throws a short hard shadow of the hand onto the backdrop just behind it; one large soft ambient source from the left at low power gives the skin gentle dimension and keeps its texture. No face, no other body parts, no rings or other jewellery, no nail polish, no text, no logos, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets.

---

## Prompting learnings from b01

1. **Construction locks held; placement did not.**
   - All five pieces kept their countable construction:
     - 4 claws and a single halo;
     - brushed, not mirror;
     - a many-strand braid;
     - haloed pastels with no repeated neighbours;
     - green ovals.
   - The "must stay X, never Y" clause works. Every failure was **composition or scale**, not product identity.
   - The one construction drift was the Verdant pavé closing into a full halo around each oval. Its lock now says "pavé on one side only, never a full halo around each oval".
2. **The model ignores frame percentages and pulls the subject toward the vertical centre, larger than asked.**
   - b01-1 base: 59% where 56% was asked.
   - b01-4: 29–69% where 38–59% was asked.
   - b01-5: 49–53% where 30% was asked.
   - b01-3: the fingers rotated down to 71%.
   - Give placement as **physical geometry** ("lens almost at table level", "the top edge crops the back of the hand 6 cm above the wrist", "the sleeve cuff at 38%", "the fingers point straight left; no part of the hand below 45%"), and state the calm band as a hard negative ("nothing at all below 51%").
3. **A referent is decoration to the model unless the relation is stated as a comparison and the referent sits at the same depth.**
   - The bud moved to the foreground, which made it bigger, and the huggies grew to 1.15× its length.
   - Say "each huggie is clearly SHORTER than the bud" and "at the same distance from the camera, never nearer". Give both sizes as shares of the frame width.
4. **Worn pieces get chunkier.**
   - The model drew fewer, larger links: 7–8 across the wrist instead of about 10, at 1.35–1.55× scale.
   - Lock the count across the body ("about ten stones across the front of the wrist"), the band height against the body ("one eighth of the wrist's width, never a quarter"), and the words "slim, delicate".
   - "Relaxed hand" without "NOT a clenched fist" gave a fist.
5. **Macro camera elevation drifts up.** "About 15 degrees" gave about 35–40°. Ask for "almost at table level, about 10°" and describe the result ("a low flat ellipse whose height is a third of its width").
6. **"No star-shaped glints" does not stop glints on a brilliant-cut CZ under a hard spot.**
   - b01-1 has three.
   - Ask positively for "soft round specular highlights only, no rays", or soften the key light for clear stones.
7. **Budget.**
   - One `nano_banana_pro` 2k picture cost about 3.6 credits, not 2.
   - The shared account fell from 26.46 to 2.46 between generation and verification.
   - Read the balance right before each generate call, and plan regenerations against 3.6 credits each.
8. **Served model.** b01-1 was served as `nano_banana_2` and still had the best fidelity and composition, so the served model does not explain the misses.

---

## Skeptic

Skeptic and rescuer pass, 19 Nov 2026, about 16:15–16:30 UTC. The balance read **202.46** before the regeneration call and **182.46**
after it. Five pictures cost 20 credits, 4 each. Every job was served as `nano_banana_2`, although `nano_banana_pro` was requested.

The regeneration call held five items. One item (b01-2) got a 429 rate-limit at submission and created no job, so it was resubmitted
on its own once the first picture finished. Each picture was regenerated exactly once.

The first tries are kept as `pics/<id>_try1.png`. The second tries are now `pics/<id>.png`. `jobs.json` now holds the new job ids,
with the old ones under `try1`. Zoomed crops are in `tmp/sk_*`, and the contact sheet is `tmp/sk_final_sheet.jpg`.

### Result

| Id | Product | Skeptic verdict | Deciding measurement |
|---|---|---|---|
| b01-1 | Cushion Halo Ring | **refuted, regenerated → pass-with-notes** | Try 1: the head was drawn 1.28–1.40× too big for its own band. Try 2 has the true proportion: band ÷ stone 2.62, against a true 2.44–2.56. |
| b01-2 | Brushed Gold Huggies | **rescued, regenerated → dropped** | The model centred the subject again: the shadows sit at 57.5–62% and the bud at 63.5–69%, under both cards. The pair spans 58% of the width. |
| b01-3 | Verdant Eternity Band | **rescued, regenerated → dropped** | The fingers now point left, but the hand sits at 28–62% and the ring at 45.7–54.5%. The ovals read 1.4–1.6× true size against the finger and the nail. |
| b01-4 | Woven Gold Hoops | **rescued, regenerated → pass-with-notes** | The camera dropped to about 8°. The hoop sits at 37.0–61.2%, Feed y 424–892, so the headline, size tag and card (at 930) all fit. |
| b01-5 | Prism Rivière Bracelet | **rescued, regenerated → dropped** | The bracelet is centred again, at 47.9–51.6% against 28–32% asked. The link pitch is 0.198 of the wrist width, against a true 0.13–0.16, so 1.27–1.38×. |

**b01 now has two shippable pictures, b01-1 and b01-4.** The three dropped slots used their one regeneration. Under RULINGS §1.2,
they are dropped for this batch, not edited.

### Refute: b01-1 (verifier's pass)

**(a) Scale is refuted.** The ring's own band is the referent: it is a finger opening, and a viewer reads the stone against it.

The camera in try 1 looks along the finger axis. The band reads as a near-perfect circle: 485–490 px wide, with its centre near y 1390.
The halo's width matches 12 mm at the stone's scale, so the ring is not turned. The stone and the band are therefore at the same depth
and can be compared directly.

Measured on the 1536 × 2752 source:

| Feature | Measurement | Ratio | True |
|---|---|---|---|
| Stone girdle | 266 px (x 647–913) | | |
| Halo | 390 px (x 577–967) | halo ÷ stone 1.47 | 1.5, so the head is self-consistent |
| Band outer | 485–490 px (x 541–1031 at y 1380–1440) | band ÷ stone **1.82** | 2.44–2.56 (about 20 mm ÷ 8 mm). The macro ref read raw gives 675 ÷ 290 = 2.33, and perspective there still favours the head. |
| Band opening | about 381 px (x 578–959 at y 1380) | opening ÷ stone **1.43** | 1.96–2.36 (adjustable US 5–9, 15.7–18.9 mm) |

So the stone and halo read **1.28–1.40× too large for the band**, and 1.37–1.65× against the finger opening. At the stone's scale,
the opening is about 11.4 mm, which is a child's ring. The frame sells a heavier cocktail stone than the 8 mm we make.

The verifier checked "stone width ÷ ring height = 0.38, same as the upright ref". That compared an end-on view with a 3/4 view in
which the band is foreshortened, so it never tested this proportion.

**(b) Fidelity holds.** The ring has 1 round stone, 4 claws, a single-row halo, pavé shoulders and silver tone.

**The fix in try 2:**
- The proportion is stated as numbers: "the band's outer width is two and a half times the stone's width, the opening twice the
  stone's width, the halo about 60% of the band's outer width; a small 8 mm stone on a full-size band, never a big stone on a small
  band and never a cocktail ring".
- Highlights are asked for as soft round dots, with no star filter.
- The ring is asked for at 32–56% of the frame height.

#### b01-1 try 2 · job `810ed20b-9aff-483f-8f68-715342f70d73` · **pass-with-notes**

**Fidelity** (against `cushion-halo-ring__upright.jpg` and `__macro.jpg`): **pass.**
- One round brilliant clear centre stone in **4 claws**, with all four visible.
- A single row of pavé on a rounded-square (cushion) halo, whose outline now reads from this slightly higher camera.
- Pavé runs down both shoulders for about two thirds of the band. The real piece's runs are about half, which is minor.
- **The open back now shows:** the two overlapping ends are visible on the inside of the band at the bottom (`tmp/sk_b01-1t2_back.png`).
- Cool silver tone with no gold cast. No box, no hands, no text.

**Scale: pass.**

| Feature | Measurement | Ratio | True | Reads at |
|---|---|---|---|---|
| Stone | 186 px (x 682–868) | | | |
| Halo | 287 px (x 628–915) | halo ÷ band 0.59 | 0.6 | |
| Band outer | 488 px (x 527–1015) | band ÷ stone **2.62** | 2.44–2.56 | 0.93–0.98× true |
| Opening | about 398 px | opening ÷ stone 2.14 | 1.96–2.36 | |

- On the 1080 canvas that is 16.3 px/mm, under 19, so **no size tag**.
- The pedestal is 2.56× the ring's width, about 5.4 cm: a believable ring-box cushion.

**Width share: 31.8%** (the ring is 343 px at 1080). That is under the 35% product-only rule, the same shortfall as try 1, and it is
kept as a note. The ring is still the brightest object, and 75–85% of the frame is dark.

**Glints:** one small 4-point sparkle on the back-right claw, with rays of about 7 px at 1080 (Feed about (601, 463)). Try 1 had three
large star glints. This one is minor.

**Calm zones:**
- **Feed** (1080 × 1350):
  - Ring box x 371–714, y 458–840. The contact shadow and the cast shadow on the velvet reach about y 900, at x 150–560.
  - Headline band y 84–300 is dark and empty: mean luminance 16–22, maximum 46. The brief's stagger (72/96, 232/166, beat 232/244
    ending about 290) clears the ring top by about 168 px.
  - **Card at top 900** (ends 1228). From 900 to 1000 is the lit pedestal top (mean 24–55, 95th percentile 57–86). From 1020 down is
    the near-black pedestal front (mean 6–10).
  - Use the brief's scrim (top 760, `rgba(110,31,35,0)` → `.6`). Bone type passes contrast, at about 5.7:1 against the 95th
    percentile, even before the scrim.
  - Keep type out of x 350–735, y 440–860.
- **Story** (1080 × 1920):
  - Ring y 743–1124. Dark, empty band y 270–600 (mean 21).
  - Pedestal top lit at about 1150–1290, then the dark front and floor.
  - The A6 Story twin has no text, so nothing moves.

**Prompt used (try 2)**, with refs `94e89aaa-…` (upright, the authority) and `6b507080-…` (macro, halo construction only):

> Product still life in a 9:16 vertical frame, camera about 15 degrees above the pedestal top, looking straight through the ring's opening, normal 50 mm lens, focus on the ring: the Cushion Halo Ring stands upright on its band on a small low round pedestal about twice the ring's width, wrapped in deep oxblood velvet like the cushion of a ring box, in an otherwise dark oxblood-to-black room. The ring, exactly as in reference 1: one 8 mm round brilliant clear cubic zirconia held by 4 claws inside one single row of small clear pave forming a cushion-shaped (rounded-square) halo about 12 mm across, one row of pave down each shoulder for about half the band's height, the lower band plain, and an open back whose two ends overlap, all in cool PVD rhodium silver tone. Proportion, which matters most: the band is a full-size ring band about 20 mm across on the outside with an opening about 16.5 mm wide, wide enough for a finger, and the centre stone sits small and neat on top of it: the band's outer width is two and a half times the centre stone's width, the opening is twice the stone's width, and the halo is only about 60% of the band's outer width. It must stay a small 8 mm stone on a full-size band, never a big stone on a small band and never a cocktail ring; the halo stays one single row and cushion-shaped, never round and never two rows; the metal stays cool silver tone, never gold tone or yellow. Size and placement in the frame: the whole ring spans about 35% of the frame width, centred; the top of the stone at 32% of the frame height and the bottom of the band resting on the velvet at 56% of the frame height; the pedestal top lies at 56% and its front edge falls into deep shadow by 58%. Empty zones: everything above 31% of the frame height is empty dark oxblood-black for a headline, with only a faint glow in the top right corner and no beam of light crossing it, and everything below 58%, the largest area of the frame, is dark velvet and floor in deep shadow for the price card; nothing touches the frame edges. Light code L1: one hard narrow spotlight from high top right and slightly behind makes a tight pool of light on the pedestal top and the ring only, so the cubic zirconia shows crisp facets with small points of spectral colour inside the stone, and the ring's crisp shadow falls toward the camera and to the left across the velvet; one very soft low fill from the front left at low power keeps the shank's silver tone, the pave and the velvet nap readable. Highlights: every specular highlight on the stone, the claws and the band is a small soft round dot; no rays, no cross-shaped or star-shaped sparkle, no starburst, no star filter, no lens flare. No text, no logos, no ring box, no hands, no people, no other jewellery, no props, no water, no droplets. Reference 1 is the listing photo and the authority on this exact ring and its proportions; ignore its background and light. Reference 2 is the same ring closer: take only the halo construction (one row of pave, cushion shape, 4 claws, pave shoulders).

### Rescue: b01-2 · Brushed Gold Huggies · job `a6b9fc88-6a91-497e-9ac5-24c8a1e783dc` · **dropped**

**What the prompt changed:**
- The bud lies between the shadows, "at exactly the same distance from the camera, never in front of them".
- Each huggie is "clearly SHORTER than the bud, about two thirds of its length".
- Shares of the frame width are given: each huggie 13%, the bud 27%, the pair 40%.
- Placement: the huggies at 31–41%, the shadows and bud at 45–49%, nothing below 50%.
- The largest empty zone is named (50% to the bottom).

**What came back:**
- **Fidelity:** 2 huggies, brushed satin with fine lines, zero stones, warm-neutral gold tone. But the left huggie's broad face is
  337 × 331 px, a width-to-height ratio of **0.98 against the true 0.70**: a fat barrel, not the 9.8 × 14 mm face.
- **Scale against the bud:** huggie height ÷ the bud's total length = 337 ÷ 581 = 0.58 at face value. But the bud again lies **in
  front of** the shadows (src y 1748–1901, against the shadows at 1582–1710), so at equal depth it is nearer about 0.64. That is within
  0.6–0.8; it is not the reason for dropping.
- **Composition: FAIL, the same failure as try 1.**
  - The huggies sit at 37.1–49.3% (Feed y 425–661).
  - The shadows sit at 57.5–62.1% (Feed y 820–910, Story y 1105–1195).
  - The bud sits at 63.5–69.1% (Feed y 936–1044, Story y 1221–1329).
  - Both the Feed card (880–1208) and the Story card (995–1250) would cover the shadows and the referent that carry the levitation
    idea. No card position inside the safe area clears them, because the card needs 328 px and must start by 938.
- **Width share:** the pair spans 57.9% of the width (x 351–1240 on the source), against 40–48%.

Both tries are spent, so the slot is **dropped**. Board note: in both tries the model put the floor objects at 57–72% whatever the
prompt said. A levitation layout for this model has to put the card *above* the pieces, or use a wall-mounted or hanging levitation
with no floor referent.

**Prompt used (try 2)**, with refs `7c95b6c6-…` (pack) and `4c630657-…` (macro, finish and shape only):

> Product still life in a 9:16 vertical frame, everything at true life size, camera low at about 12 degrees above the floor, 100 mm macro lens, the frame about 7.5 cm across at the pieces: a pair of Brushed Gold Huggies hover side by side, 1 cm apart, about 8 mm above a flat matte sky-blue floor that curves up into a sky-blue wall with no horizon line. Directly below each huggie lies its own crisp, soft-edged darker-blue shadow, separated from the piece by a clear gap of clean floor about half a huggie tall. One fresh white jasmine bud, 2 cm long including its short green stem, lies on the floor between the two shadows, on the same line as the shadows and at exactly the same distance from the camera, never in front of them and never nearer the camera. Size relations, which matter most: each huggie is 14 mm tall and 9.8 mm wide, so each huggie is clearly SHORTER than the 2 cm bud, only about two thirds of the bud's length; the bud always reads longer than either huggie, never shorter. Each huggie is only about 13% of the frame width wide and the bud about 27% of the frame width long; the pair together spans about 40% of the frame width, centred. Each huggie, exactly as in reference 1: a chunky huggie with a wide softly domed barrel-shaped band about 6 mm deep, in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, hidden hinge, zero stones; one in three-quarter front view with its broad brushed face to the camera, the other turned a little to show its curved C profile. The finish must stay matte and light-scattering, never mirror-polished, ridged, hammered or stone-set, never a thin hoop and never larger than the bud. Placement: the huggies float between 31% and 41% of the frame height; their shadows and the bud lie between 45% and 49%; nothing at all is below 50% of the frame height. Empty zones: everything from 50% of the frame height down to the bottom edge, the largest area of the frame, is empty, evenly lit sky-blue floor for the price card, and everything from the top edge down to 29% is empty sky-blue wall for a headline; nothing touches the frame edges. Light code L1: one hard spotlight from directly above and slightly in front throws the two shadows straight down; one large soft fill from the front at low power shows the fine brush lines as one broad soft sheen on each band; the gold tone stays warm-neutral against the blue, never orange, brassy or reading as silver tone. Highlights are soft and round only. No hands, no people, no strings, wires, stands, pins or supports of any kind, no text, no logos, no other jewellery, no extra buds or petals, no star-shaped glints, no starburst, no lens flare, no water, no droplets. Reference 1 is the listing photo and the authority on this exact pair; ignore its background and light. Reference 2 is one huggie closer: take only the brushed-satin finish and the barrel shape.

### Rescue: b01-3 · Verdant Eternity Band · job `eca4d860-86f3-4290-8219-75e4a3c537dc` · **dropped**

**What the prompt changed:**
- The verifier's rerun was geometrically impossible: a horizontal hand about 7.5 cm across the fingers is about 41% of a frame
  11 cm wide and 19.6 cm tall, which does not fit inside 16–44% of the height. So the frame went to 12 cm.
- The hand lies horizontally across the TOP, with the fingers pointing straight left and the finger order named, the whole hand inside
  6–42% of the height, and "no finger points down".
- The pavé lock is "one single wave, each oval cupped on one side only, never a full halo".
- The largest empty zone is named (44% to the bottom).

**What came back:**
- **Fidelity: pass.** This fixes the try 1 drift. Four emerald-green ovals show in 4 claws, with **one** scalloped S-wave of clear pavé
  cupping them on alternate sides, matching `__cube.jpg`. The long axis runs along the finger, as in the ref. Cool silver tone with no
  gold. The ring is on the ring finger: from the top, thumb, index, middle, ring (with the ring), little.
- **Styling:** henna-dipped tips and a henna vine, the jaali lattice only at the left edge, natural skin. The thumb shows at the top
  (minor).
- **Scale: FAIL.**
  - Each oval measures 67 × 51 px on the source.
  - The ring-finger nail is about 100 px wide and the ring finger about 155 px wide, just left of the ring.
  - Oval ÷ nail = **0.67, against the brief's ⅓ (true 5 ÷ 12 mm = 0.42)**.
  - On the finger ruler (17–19 mm = 155 px, so 8.2–9.1 px/mm), each oval is 7.4–8.2 × 5.6–6.2 mm, against 5 × 4.
  - The ring's visible span across the finger is 242 px, which is 1.56× the finger's width. A ring wrapping the finger shows at most
    about 1.25×.
  - So the ring reads **1.4–1.6× true size**, over the 1.25× limit.
- **Composition: FAIL.**
  - The model kept the fingers pointing left but placed the hand in the **middle** of the frame: thumb tip 27.8%, little finger to 61.8%
    (Feed y 245–903, Story y 530–1188).
  - The ring sits at 45.7–54.5% (Feed y 592–762, Story y 877–1047), against a lowest point of 41% or higher.
  - The Story card (915–1243) would sit on the ring and the hand.
  - The only calm Story bands are 270–530 (260 px) and 1188–1250, against the card's 328 px.
  - The Feed card would just clear at 930 (27 px under the little finger), but the Story twin cannot ship.

Both tries are spent, so the slot is **dropped**.

**Prompt used (try 2)**, with refs `2c3d1209-…` (upright, the authority) and `702645c3-…` (cube, how the ovals alternate only):

> Close editorial hand photograph in a 9:16 vertical frame, 85 mm lens from about 40 degrees above, the frame about 12 cm across: the left hand of a South Asian person, medium wheatish-brown skin with natural texture, fine knuckle creases and short bare nails, lies flat, palm-down and relaxed on deep cocoa-brown raw silk, lying HORIZONTALLY across the TOP of the frame: the wrist and the back of the hand enter from the right edge, and all four fingers point straight to the LEFT, level, side by side and only slightly apart, the fingertips stopping just inside the left edge; the thumb is folded under the palm and out of sight. From top to bottom the fingers are: the index finger highest, then the middle finger, then the ring finger, then the little finger lowest. The whole hand lies between 6% and 42% of the frame height: the index finger near 10% and the lower edge of the little finger near 41%; no part of the hand, fingers or henna reaches below 43% of the frame height, and no finger points down. Fresh wedding-season mehendi: the fingertips dipped in deep red-brown henna to the first knuckle and one slim vine of fine henna lines on the back of the hand toward the wrist, the skin around the ring left clear. On the ring finger (the second finger up from the bottom), just past the knuckle, the Verdant Eternity Band, exactly as in reference 1: a cool PVD rhodium silver-tone open-back band carrying oval emerald-green cubic zirconia of 5 by 4 mm in 4 claws, about five of them showing across the top of the finger, with ONE slim scalloped S-wave line of tiny clear pave weaving between them: the wave passes on one side of an oval and on the other side of the next, so each oval is cupped by pave on one side only, alternating sides. It must stay one single wave with the ovals alternating either side of it, never a full pave halo around each oval, never two pave lines, never a straight row or plain links, never round or teal stones, and the metal never gold tone. Scale: true size; the band wraps the finger and its visible top runs across the finger from edge to edge, about 1.8 cm, exactly the width of the finger and never wider; each green oval is about a third of the width of the ring finger's nail and about a quarter of the finger's width; a faint contact shadow on the skin; the ring sits at about 45% of the frame width and 33% of the frame height. Empty zone, which matters most: everything from 44% of the frame height down to the bottom edge, more than half of the frame, is calm, empty cocoa silk in soft even shade, with no fingers, no hand, no henna, no shadow edge and no light pattern in it, for the price card. Light code L4: hard late-afternoon sun through one large opening of a carved stone jaali from the upper left lights the hand and the ring in one clean unbroken patch, so the green stones glow and the pave sparkles; a crisp lattice of light falls only on the small patch of silk to the left of the fingertips, never on the hand and never below 40% of the frame height; one soft warm bounce from the right fills the shadows on the skin. No face, no other body parts, no bangles, no other rings or jewellery, no nail polish, no text, no logos, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets. Reference 1 is the listing photo and the authority on this exact ring; ignore its background and light. Reference 2 is the same ring from above: take only how the green ovals alternate on either side of the single pave wave.

### Rescue: b01-4 · Woven Gold Hoops · job `85ffa05a-dbd5-45e2-ad6d-bdacb83e9d5d` · **pass-with-notes**

**What the prompt changed:**
- The camera is "almost at table level, about 8°", described as the result ("a long, low, flat ellipse a third as tall as it is wide").
  At 15°, the hoop's projected height (25 sin θ + 5 cos θ mm) cannot fit the 21% band.
- The latch disc stands at the left end of the hoop, not at the back, so it adds no height.
- Droplets go only on the braid and within 5 mm of it.
- The empty zones are named as the largest part of the frame: the top 38% and the bottom 40%.

**Fidelity** (against `woven-gold-hoops__pack.jpg` and `__detail.jpg`): **pass.**
- One hoop. An open many-wire plait with deep ridge and shadow, the same construction as the detail ref, with wires a touch thicker
  than the ref's.
- The flat disc is now **bright and mirror-polished** (try 1's was dull). Its diameter is about 0.22 of the hoop's width, the same as
  the ref.
- Zero stones; warm 18k gold tone, not blown out.
- Note: the latch is drawn as a small hinge block with a hooked wire, chunkier than the real thin latch wire. It is at the far left
  and reads as hardware.

**Scale:** the hoop is about 1204 px across on the source for 25 mm, which is about 48 px/mm on the source and **34 px/mm on the
1080 canvas**. It is magnified, so **the size tag is required** in Feed and Story, as briefed.
- The braid's vertical extent at the near side is about 248 px, about 5.2 mm, consistent with 5 mm.
- The droplets measure 2–4 mm (about 117–193 px), each no larger than the braid, with several beaded on it.
- There is a true contact shadow and only a faint sheen under the braid.

**Width share:** 85.3% (source x 101–1411, the latch included), within 80–90%. Note: it is **not** cropped by the right edge; the
whole hoop shows, ending at 92%.

**Placement:** source y 1019–1685, which is **37.0–61.2%** of the frame (the brief asked 38–59%). The gold ends at 1660 and the
reflection at 1685. It is close to the brief, and it fits the layout below.

**Calm zones:**
- **Feed** (1080 × 1350):
  - Hoop box x 71–992, y 424–892. The top edge is at y 424 at x 570–590, and at y 446–490 under the size tag's x-range.
  - Headline band y 84–390 is smooth plum: mean luminance 50–72, standard deviation 3–5.
  - The H1 (72/96, ends about 286), the beat (72/292, ends about 341) and the size tag (right 72, top 292, ends 388) clear the hoop by
    82 px at the left and 58 px or more at the right.
  - **Card at top 930** (ends 1258, inside 1266). The brief's 880 would overlap the braid bottom at 892.
  - Feed y 1000–1266 is smooth (mean 75–85, standard deviation 5–9).
  - Two small droplets sit under the wordmark's left edge and centre, at about (365–445, 905–945) and (565–620, 940–960). Use the
    brief's scrim, but start it at **880**, not 760, so it does not dim the braid: `rgba(74,37,64,0)` → `.6`.
- **Story** (1080 × 1920):
  - Hoop y 709–1177.
  - The wordmark (300–356) and the centred size tag (384–480) sit on calm plum: mean 44–50, standard deviation 1.6–3.
  - Below 1240, smooth plum.
- **Where type must not go:** Feed x 60–1000, y 410–905.

**Prompt used (try 2)**, with refs `74ed9a2b-…` (pack) and `b77ec5ba-…` (detail, braid and disc only):

> Macro product still life in a 9:16 vertical frame, 100 mm macro lens with the camera almost at table level, only about 8 degrees above a smooth satin-glazed deep-plum (aubergine) surface, so the hoop lying flat reads as a long, low, flat ellipse whose visible height is only about a third of its visible width; honest shallow macro depth of field with the near side of the braid razor sharp: one hoop of the Woven Gold Hoops pair lies flat, shown monumentally large, its thick braided ring running off the right edge of the frame. The hoop, exactly as in reference 1: a round hoop about 25 mm across made of one thick braid about 5 mm thick of many fine polished 18k PVD gold-tone wires with a deep ridge-and-shadow interlace, a thin hinged latch wire, and a small flat mirror-polished round disc about 6 mm across standing upright at the left end of the hoop, turned toward the camera, its top no higher than the far edge of the braid; zero stones. The braid must stay a many-strand plait of fine wires with deep ridges, never a smooth tube, a simple two-strand twist or a few thick ropes; the disc stays bright and mirror-polished, never dull or mottled; the hoop stays round in plan, never larger. Placement, which matters most: the entire hoop, including its far edge, the disc and the latch, lies inside the band from 40% to 57% of the frame height; no part of the hoop rises above 39% or falls below 58% of the frame height; it spans about 80% of the frame width, from 20% of the width to past the right edge, cropped by the right edge only. Empty zones: the whole top 38% of the frame and the whole bottom 40% of the frame, together most of the frame, are calm, smooth, softly out-of-focus plum glaze with no droplets, no hoop and no highlights, for a headline, a size tag and the price card. Water: clear droplets of 1 to 4 mm, each smaller than the braid's thickness, only on the braid itself and on the glaze touching the hoop, within 5 mm of it; nowhere else on the surface. Scale: the braid's thickness is about a fifth of the hoop's width; the hoop casts a true contact shadow; any reflection in the glaze is only a faint soft sheen right under the braid. Light code L1: one hard low raking spotlight from the left skims across the braid so every wire's ridge and shadow is sculpted and each droplet carries one crisp round highlight and a small shadow; one soft broad fill from the front right at low power keeps the gold tone warm-neutral, never orange, brassy or blown out. No hands, no people, no second hoop, no other jewellery, no props, no text, no logos, no star-shaped glints, no starburst, no lens flare, no splash, no spray, no running water. Reference 1 is the listing photo and the authority on this exact hoop; ignore its background and light. Reference 2 is the same hoop closer: take only the braid structure and the flat polished disc latch.

### Rescue: b01-5 · Prism Rivière Bracelet · job `85160c01-62a8-4e2d-ba9d-a2f37789c0ac` · **dropped**

**What the prompt changed:**
- The sleeve cuff is placed at 38%, and the top edge crops the back of the hand 6 cm above the wrist.
- "Relaxed and open, NOT a fist."
- About ten links across the front, each one eighth of the wrist's width, "never a quarter", "never chunky".
- The largest empty zone is named (38% to the bottom).

**What came back:**
- **Fidelity: pass.**
  - Square cushion stones, each in a double pavé halo, matching `__detail.jpg`.
  - Colours run yellow, aqua, pink, yellow, aqua, pink, yellow: three colours only, no neighbours alike, no lilac or green.
  - Bright silver tone; the clasp is hidden.
  - The hand is open and flat, not a fist. Natural skin texture; no face, no other jewellery.
- **Scale: FAIL, marginally.**
  - The wrist is 490 px wide at the bracelet (source x 517–1007).
  - The centre link pitch is about 97 px, so **pitch ÷ wrist = 0.198**. The true ratio is 8.6 mm over a 55–65 mm wrist, 0.13–0.16.
  - So the links read **1.27–1.38×** true size (1.5× on a 65 mm wrist), over the 1.25× limit.
  - Each link with its halo is about 90 px, 0.18 of the wrist, about 10–12 mm against 7–8 mm.
  - About 7–8 links show, not ten.
  - The model also widened the frame to about 17 cm, so the bracelet spans only 37.8% of the width (source x 473–1053), against 42–52%.
- **Composition: FAIL, the same failure as try 1.**
  - The bracelet sits at **47.9–51.6%** (Feed y 633–706, Story y 918–991), against 28–32%. The brief's Feed headline (640–781) and
    Story lockup (772–976) would sit on it.
  - The cuff is at 56% (Feed y 792, Story y 1077).
  - The knuckles and finger bases show along the top edge.
  - A Feed card-only layout would fit on the sleeve at 880, but the Story card (252–328 px) has only 1077–1250 (173 px) of calm sleeve.

Both tries are spent, so the slot is **dropped**.

**Prompt used (try 2)**, with refs `f9e23a88-…` (pack) and `8f1ff732-…` (detail, halos and colour order only):

> Editorial flash photograph in a 9:16 vertical frame, 85 mm lens at eye level, the frame about 12 cm across at the wrist: one forearm of a South Asian person with deep brown skin with a cool undertone and natural texture rises straight up from the bottom edge, covered in a fitted matte black crepe sleeve whose cuff ends about 1.5 cm below the wrist, at 38% of the frame height. Above the cuff the bare wrist and the back of the hand continue straight up, the back of the hand flat toward the camera, relaxed and open, NOT a fist; the top edge of the frame crops across the back of the hand about 6 cm above the wrist, so no knuckles and no fingers are in the frame. On the bare wrist, high in the frame at 30% of the frame height, the Prism Riviere Bracelet, exactly as in reference 1: a slim, delicate single line of small square cushion-cut pastel cubic zirconia about 5 mm, each in its own fine square halo of tiny clear pave so each link is only about 7 mm, linked edge to edge in bright PVD rhodium silver tone; about ten links show across the front of the wrist; the colours mix aqua blue, soft pink and pale yellow with no two neighbours the same colour; the fold-over clasp is hidden under the wrist. It must stay exactly these three pastel colours, every stone in its own halo, never a fourth colour such as lilac or green, never bare stones, never gold tone. Scale, which matters most: the wrist is about 5.5 cm wide and spans about 46% of the frame width; the bracelet band is only about 7 mm tall, about one eighth of the wrist's width, never a quarter of it; each link is about one eighth of the wrist's width, so about ten fit across the front; small, slim and delicate against the wrist, never chunky; the bracelet spans about 48% of the frame width, centred, lying flat on the skin with a faint contact shadow. Empty zone: everything from 38% of the frame height down to the bottom edge, the largest part of the frame, is calm matte black sleeve and charcoal-black backdrop for type and the price card, with nothing bright, no sheen streak and no skin; the bracelet's lowest point is above 33% of the frame height; nothing important touches the side edges. Light code L2: one direct on-camera flash, hard and frontal, makes the pastel stones read in true colour with crisp sparkle and throws a short hard shadow of the hand onto the backdrop just behind it; one large soft ambient source from the left at low power gives the skin gentle dimension and keeps its texture. No face, no other body parts, no rings or other jewellery, no nail polish, no text, no logos, soft round highlights only with no star-shaped glints, no starburst, no lens flare, no water, no droplets. Reference 1 is the listing photo and the authority on this exact bracelet; ignore its background and light. Reference 2 is the same bracelet closer: take only the square halos and the mixed colour order.

### Skeptic learnings for b02 (for the learnings agent)

1. **The model centres the subject, whatever the percentages say.**
   - Six of the eight placement asks in b01 landed the piece or hand at about 37–62%, including b01-2, b01-3 and b01-5 on their second
     try, even with "nothing below 50%" and the empty zone named as the largest area.
   - The two that passed (b01-1, b01-4) had their pieces centred anyway.
   - **Design b02 layouts around a centred subject:** the piece at about 36–60% of the frame, the headline at 15–33% (Feed y 84–340),
     and the card at Feed 900–938, which is frame 62–80%.
   - Do not brief a piece at 30% height, or a hand along the top edge.
   - For a worn wrist, put the Story lockup above the hand, or use a no-text Story twin.
2. **Proportion locks work for rigid pieces; scene referents do not.**
   - A ratio inside the piece fixed b01-1 completely: "band outer = 2.5 × stone; opening = 2 × stone; never a big stone on a small band".
   - Against body or prop referents (finger, nail, wrist, bud), the piece still came out 1.27–1.6× in three of three worn or prop frames.
   - Where possible, measure scale with a ratio inside the piece (link ÷ clasp, stone ÷ band), and choose camera distances where a
     20–30% overshoot is still honest.
3. **When the model widens the frame, it does not shrink the jewellery with it.** b01-5 asked for 12 cm and got about 17 cm, but kept
   the links large, so the bracelet's width share fell to 38% while its scale rose to 1.3×.
4. **Low camera works when the geometry is spelled out.** "About 8°, a flat ellipse a third as tall as it is wide", with the disc placed
   where it adds no height, fixed b01-4.
5. **Budget and served model.**
   - Each picture cost 4 credits: 202.46 → 182.46 for five.
   - All five were served as `nano_banana_2`.
   - A five-item batch hit a 429 on one item; resubmit only the failed index after the first job completes.
