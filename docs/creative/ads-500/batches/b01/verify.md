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
