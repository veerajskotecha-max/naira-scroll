# Batch b01: creative director's brief (19 Nov 2026)

Five static ads, ids `b01-1` to `b01-5`. Each ad gets its own new Higgsfield picture: no plate, finished ad, listing photo or ads-20 frame is reused, and no two ads share a frame (RULINGS §1.2). Nothing is committed or uploaded by this step.

## 0. Pre-flight

- **Higgsfield balance, read for this batch:** 88.46 credits (basic plan). Cost: 5 pictures × 2 credits = **10 credits**, plus at most one regeneration per ad (up to 10 more). The balance after b01 will be about 68–78.
- **Stock and price** are taken from the RULINGS §2 read of 19 Nov 15:25 UTC. All five products have 20 or more units:
  - Cushion Halo 45, ₹999
  - Brushed 58, ₹699
  - Verdant Eternity 58, ₹1,049
  - Woven 89, ₹1,049
  - Prism 41, ₹2,399
- **Offer:** BUY2 (10% off 2 or more items) and BUY3 (20% off 3 or more). These are codes, not automatic discounts, so the box prints "CODES BUY2 · BUY3".
  - The box is identical on all five ads, so the offer is not a variable in this batch.
  - NAIRA10 and BUY4 are not used. The offer test cell comes in a later batch.
- **Left out:**
  - Cash on delivery: RULINGS §2 does not verify it, so the copy omits it.
  - Shipping offers and compare-at prices: never printed.
- **Claims:** they appear on one ad only, b01-4 Woven. RULINGS §1.1 allows them for Woven.
- **Toggle:** not in this batch.
- **Ledger:** `build/ledger.json` is empty, so this is the first batch of the run.
- **Rotation:** the three heroes lead (slots 1–3). Woven and Prism are the first two of the eleven other products.

## 1. Batch idea

**What it tests.** Every piece is made the brightest and most saturated thing in its frame, each by one honest device:
- a single spotlight (Cushion Halo);
- levitation over a light flat field (Brushed);
- the F2 card on a mehendi hand in jaali sun (Verdant Eternity);
- a monument macro (Woven);
- a flash-lit worn wrist on black (Prism).

The question is whether this beats the F2 and anaar grammar on pieces we are allowed to sell.

**The one new move: the newly allowed claim.** It appears on Woven only:
- as the second beat ("and yes, waterproof.");
- shown by water droplets in the picture;
- never as the headline.

This tests learnings rule 8 directly against our W1 pair. The texture-led W1 with droplets sold 5. The claim-led W1, on the same picture, sold 0 on ₹3,236. The other four ads carry no claim, so any effect can be traced to that one ad.

## 2. What this improves on

There is no earlier ads-500 batch, so b01 answers two things: the study gaps (PLAYBOOK §3), and the §6 brief as RULINGS changes it.

**Gaps from PLAYBOOK §3**

1. **Gap 1: the piece is not the biggest or most colourful thing in the frame.**
   - Product-only pieces fill at least 35% of the width: Cushion about 36%, Brushed about 42%, Woven about 85%.
   - Worn key details fill at least 12%: Verdant Eternity about 16%, Prism about 48%.
   - Every ground lets the piece own the colour:
     - clear and silver tone on oxblood and on black;
     - gold tone on sky and on plum;
     - green on cocoa;
     - pastels on black.
   - No pale piece sits on a pale ground.
2. **Gap 2: worn pictures are rare and all look alike.** There are two new worn frames, each with:
   - its field of view stated in cm;
   - a named skin tone (wheatish; deep brown with a cool undertone);
   - new styling: henna-dipped fingertips on cocoa raw silk in jaali sun, and a black sleeve under flash.

   There is no ivory shirt and no low bun.
3. **Gap 3: nothing honestly surprising.** Two "crazy" ads, the spotlight (A6) and the levitation (A13), both at true size with a referent or a size tag.
4. **Gap 4: fidelity.** Every prompt carries:
   - a countable lock with one "must stay X, never Y" clause;
   - slot 1, the listing packshot;
   - slot 2 only when it is a second view of the same piece.
5. **Gap 5: no verified offer on the image.** The verified BUY2·BUY3 value is on every Feed card.
6. **Gap 6: copy.** First beats are listing truths, or the Cushion video hook that sold 20. There are no concept nouns and no generic occasion lines. The occasion lives in the picture.
7. **Gap 7: one light, one camera.**
   - Lights: L1 ×3, L2, L4 (L7 is not used).
   - Cameras: C2, C3, C4 ×2, C5.
8. **Gap 11: platform.** Pictures are native 9:16, and the calm zones are stated for both formats. Story text sits only inside y 270–1250.

**Changes to §6 as written**

- RULINGS forbids shared frames and existing frames:
  - The S1_04 test of B1-01 against B1-02 (A1 against A2 on one frame) cannot run.
  - S2_06 cannot be reused.
- Cushion Halo keeps its proven video hook ("Looks like a proposal.") on a new A6 spotlight frame, which makes that hook literal.
- The F2-style card with no headline (A1) moves to Verdant Eternity. The A1 spec ranks saturated-stone pieces first, and this keeps §6's wedding-season picture in the batch.
- Brushed levitation moves from oxblood to sky blue. A detached shadow reads only dark on light (board 96). On oxblood it would be dark on dark.
- The §6 "Z[OO]M IN." in-word ad is deferred.
  - The Brushed huggie's front is a closed barrel and its side is a narrow C, so neither reads as an O. That is the A14 failure check.
  - Its slot goes to Woven, which has 89 units and the W1 evidence.
  - The second Cushion slot goes to Prism: ₹2,399, a 3.46x video, but statics lost on pale grounds. Prism gets its first dark-ground static.
  - The batch therefore covers five products, not three.

## 3. Batch matrix

| Id | Product | Archetype | Crazy | Camera | Light | Ground | Body | Price | Board ranks borrowed |
|---|---|---|---|---|---|---|---|---|---|
| b01-1 | Cushion Halo Ring | A6 Single Spotlight | yes | C3 | L1 | oxblood velvet, near-black | product | ₹999 | 3, 166; our Halo 15s B hook |
| b01-2 | Brushed Gold Huggies | A13 Suspended (levitation) | yes | C2 | L1 | sky | product | ₹699 | 96, 1 |
| b01-3 | Verdant Eternity Band | A1 Product Card (no headline), occasion picture | no | C4 | L4 | cocoa raw silk, jaali sun | worn hand | ₹1,049 | our F2; 72, 91, 123 |
| b01-4 | Woven Gold Hoops | A4 Monument Macro + claim as proof | no | C5 | L1 | wet plum glaze | product | ₹1,049 | 26, 42, 95, 190, 4, 55; our W1 pair |
| b01-5 | Prism Rivière Bracelet | A2 Worn Editorial | no | C4 | L2 | black | worn wrist | ₹2,399 | 88, 148, 11; our F2 |

**Checks against the batch rules:**
- 5 archetypes (at least 4 required).
- 5 products, at most 1 ad each.
- 3 lights (L1, L2, L4) and 4 cameras (C2, C3, C4, C5).
- 2 crazy ads.
- 1 occasion picture (mehendi).
- 1 claim, used as proof.
- 0 type-led ads and 0 Anton.

**Pairwise anchors for the batch sheet (§5.3.3):**
- Winner: `build/anchors/win_twenty_f2_tennis_ruby.jpg`.
- Loser: `build/anchors/lose_vks5_prism_close.jpg`, because b01-5 is the direct answer to pale-on-pale Prism.

## 4. Frame geometry (applies to every picture)

- Generate at 9:16, 2K. Normalise to 1080 × 1920 for the Story.
- **Feed** = the central 4:5 crop: y 285–1635 of the 1920 frame, which is 14.8%–85.2%.
  - Conversion: `feed_y = frame_px − 285`.
  - Feed type safe area: x 72–1008, y 84–1266 (frame 19.2%–80.8%).
  - Feed card: y 880–1208 (frame 60.7%–77.8%).
- **Story:** text only between y 270 and 1250 (frame 14.1%–65.1%).
  - The full card with its wordmark is about 328 px tall; without the wordmark, about 252 px.
  - So a Story card without the wordmark sits at top 995, and with the wordmark at top 915 or higher.
- **Where things go in the frame:** the pieces sit in frame bands of about 26%–60%. Type goes in two calm bands:
  - a top band, about 15%–35%;
  - a bottom band, about 52%–80%.

  The exact bands per ad are in each prompt.
- **References:** `generate_image` with `nano_banana_pro`, `resolution: 2k`, `aspect_ratio: 9:16`, 1 image per ad.
  - Slot 1: the listing packshot ("the authority on this exact piece; ignore its background and light").
  - Slot 2: a second view of the same piece, with its role stated.
  - Quote with `estimate_image_cost` first. Judge every output by eye, because the model served can differ from the one requested.

---

## b01-1 · Cushion Halo Ring · A6 Single Spotlight

- **Handle:** `cushion-halo-ring`. ₹999, 45 units. Claims: none used.

**Concept.** The ring stands alone on an oxblood velvet pedestal, like a ring-box cushion, under one hard spotlight in a dark room. The staging makes the proven hook literal: it looks like the moment someone opens the box.

**Borrows**
- Board 3, "Spray it in the evening": one spotlight on black makes the claim literal, and the product is the only lit thing. Also board 166.
- Our Halo 15s B video hook "Looks like a proposal.": ₹5,135, 20 purchases, 2.21x.
- Our F2 card (4.74x).

**Camera and light**
- **C3:** eye level, about 10° above the pedestal top, normal 50 mm lens.
- **L1:** one hard narrow spot from the top right and slightly behind. One very soft, low front-left fill.

**Refs**
1. `94e89aaa-1d35-47ca-853e-da323cc0ac01`, `build/refs/cushion-halo-ring__upright.jpg`. The authority on this exact piece; ignore its background and light.
2. `6b507080-6cf9-4452-83c1-6e5cabddcfa0`, `build/refs/cushion-halo-ring__macro.jpg`. Take only the halo construction: one row of pavé, cushion shape, 4 claws, pavé shoulders.

**Prompt**

> Product still life in a 9:16 vertical frame, camera at eye level about 10 degrees above the pedestal top, normal 50 mm lens, focus on the ring: the Cushion Halo Ring stands upright on its band, turned three-quarters so the halo faces the camera, on a small low round pedestal about 4 cm across wrapped in deep oxblood velvet like the cushion of a ring box, in an otherwise dark oxblood-to-black room. The ring, exactly as in reference 1: one 8 mm round brilliant clear cubic zirconia held by 4 claws inside one single row of small clear pavé forming a cushion-shaped (rounded-square) halo about 12 mm across, one row of pavé down each shoulder, and a plain open back whose two ends overlap, all in cool PVD rhodium silver tone; the halo must stay one single row and cushion-shaped, never round and never two rows, and the metal must stay cool silver tone, never gold tone or yellow. Scale: the ring keeps its true small size, the halo about half of the ring's overall width and the band's opening about the width of a fingertip; it rests with a true soft contact shadow where the band meets the velvet; the ring spans about 36% of the frame width, centred, its top at about 33% and its base at about 56% of the frame height, inside the central 4:5 window, with the pedestal top at 56% and its front edge falling into deep shadow by 60%. Scene: 70 to 90% of the frame is dark; the band from 15% to 31% of the frame height is empty dark oxblood-black for a headline, with only a faint glow in the top right corner where the light enters, and everything below 60% is dark floor and velvet in shadow for the price card; nothing touches the frame edges. Light code L1: one hard narrow spotlight from high top right and slightly behind makes a tight pool of light on the pedestal top and the ring, so the cubic zirconia throws small points of spectral colour and the ring's long crisp shadow falls toward the camera and to the left across the velvet; one very soft low fill from the front left at low power keeps the shank's silver tone, the pavé and the velvet nap readable. No text, no logos, no ring box, no hands, no people, no other jewellery, no props, no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Acceptance**

*Fidelity*
- One round clear centre stone held by exactly 4 claws.
- One single-row, cushion-shaped (rounded-square) pavé halo. Not round, not two rows.
- One pavé row down each shoulder.
- An open back with overlapping ends, visible or plausibly turned away.
- Metal cool silver tone everywhere: no gold-tone or yellow cast and no brassy reflections.

*Scale and placement*
- Halo about 0.5× the ring's overall width.
- Ring width 35–40% of the frame width (378–432 px at 1080), centred.
- If the ring is wider than 420 px (over 19 px/mm), the Feed carries the size tag.
- Ring top at or below 32% and base at or above 57% of the frame height.
- A true contact shadow on the velvet, and a long shadow falling toward the camera.

*Light*
- The ring is the brightest object.
- 70–90% of the frame is dark.
- The glow appears only in the top-right corner (x over 75%, y under 25%) and is faint.

*Calm zones*
- Frame 15–31% is dark and empty, for the headline.
- Frame below 60% is dark, for the card. No lit pedestal edge under the wordmark.

*Negatives*
- No star-shaped glints, starburst, flare, text, logos, ring box, hands or extra jewellery.

**Layout: Feed** (1080 × 1350, `<body class="dark">`, background `var(--oxblood)`, `.pic` = central 4:5 crop)
- **Headline**, A6 stagger:
  - `.h1` Velista 68 px, `letter-spacing: .12em`, colour `var(--gold-light)`.
  - "LOOKS LIKE" at left 72, top 96.
  - "A PROPOSAL." at left 232, top 166.
  - Widths about 485 and 540 px; ends by x 772.
- **Beat:** `.beat` Cormorant Garamond italic 500, 44 px, `var(--bone)`, left 232, top 244: "priced like a present." It ends near y 290, at least 55 px above the ring.
- **Card:** `.card` top 880:
  - `.wm` `logo_white.png` 56 px;
  - `.name` "Cushion Halo Ring";
  - `.price` "₹999";
  - `.line` "8 mm cubic zirconia · silver tone · adjustable";
  - `.offer` "Buy 2 · 10% off &nbsp;•&nbsp; Buy 3 · 20% off" with `<small>codes BUY2 · BUY3</small>`.
- **Scrim:** none, unless the lit pedestal edge reaches under the wordmark. If it does: `.scrim` top 760, `rgba(110,31,35,0)` → `rgba(110,31,35,.6)`.
- **Size tag:** only if the ring is wider than 420 px. `.sizetag` right 72, top 96, bone: "Shown magnified<br>8 mm centre stone".
- **Count and share:** 2 text elements (3 with the tag). Text share at most 14%; about 8% expected.

**Layout: Story** (1080 × 1920, `<body class="dark story">`, `.pic` full frame)
- No text and no logo: the A6 Story twin, on the anaar pattern.

**Copy**
- **Primary text** (159 characters; the offer ends at character 115): "Looks like a proposal, priced like a present: Cushion Halo Ring, ₹999, 8 mm cubic zirconia. BUY2: 10% off 2 pieces. Silver tone, adjustable, with an open back."
- **Headline:** "Cushion Halo Ring · ₹999 · BUY2: 10% off 2"
- **Description:** "Silver tone · cubic zirconia · adjustable"
- **URL:** `https://www.nairaflore.com/products/cushion-halo-ring?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b01&utm_content={{ad.id}}&utm_term=b01-1_a6_proposal-spotlight`

---

## b01-2 · Brushed Gold Huggies · A13 Suspended (levitation)

- **Handle:** `brushed-gold-huggies`. ₹699, 58 units. Claims: none used.
- The ad leads with bundle value, as PLAYBOOK §3.5 asks for ₹699 SKUs.

**Concept.** The pair hovers about a centimetre above a flat sky-blue floor. Their two detached shadows lie directly below, and a 2 cm jasmine bud on the floor gives the honest scale. The price is the message.

**Borrows**
- Board 96, "Light on weight / big on journeys": levitation with a detached shadow on a light flat field reads in half a second.
- Board 1: one claim, one prop.
- §6 B1-03, with the ground changed from oxblood to sky so the shadow reads dark on light.

**Camera and light**
- **C2:** low hero, about 12° above the floor, 100 mm macro.
- **L1:** one hard spot from directly above and slightly in front. One large soft front fill.

**Refs**
1. `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f`, `build/refs/brushed-gold-huggies__pack.jpg`. The authority on this exact piece; ignore its background and light.
2. `4c630657-80e8-47f5-ad65-1f0938c70900`, `build/refs/brushed-gold-huggies__macro.jpg`. Take only the brushed-satin finish and the barrel shape of one huggie.

**Prompt**

> Product still life in a 9:16 vertical frame, camera low at about 12 degrees above the floor, 100 mm macro lens: a pair of Brushed Gold Huggies hover side by side about 1 cm apart, 1 to 1.5 cm above a flat matte sky-blue floor that curves up into a sky-blue wall with no horizon line; directly below each huggie lies its own crisp, soft-edged darker-blue shadow on the floor, clearly separated from the piece by a gap of clean floor, and one fresh white jasmine bud about 2 cm long lies on the floor just left of the shadows. Each huggie, exactly as in reference 1: a chunky huggie about 14 mm tall and 9.8 mm wide, a wide softly domed barrel-shaped band about 6 mm deep, in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines running from top to bottom across the band, hidden hinge, zero stones; one shown in three-quarter front view with its broad brushed face to the camera, the other turned a little to show its curved C profile. The finish must stay matte and light-scattering, never mirror-polished, ridged, hammered or stone-set, and never a thin or large hoop. Scale: they keep their true small size, each huggie about two thirds of the length of the 2 cm jasmine bud; the pair together spans about 42% of the frame width, centred, its top at about 31% and its bottom at about 42% of the frame height, with the shadows and the bud at about 47% to 50%, all inside the central 4:5 window. Scene: the frame from 15% to 28% of the height is empty sky-blue wall for a headline, and everything below 52% is empty, evenly lit sky-blue floor for the price card; nothing touches the frame edges. Light code L1: one hard spotlight from directly above and slightly in front throws the two shadows straight down and leaves a gentle pool of light on the floor; one large soft fill from the front at low power shows the fine brush lines as one broad soft sheen on each band; the gold tone stays warm-neutral against the blue, never orange, brassy or reading as silver tone. No hands, no people, no strings, wires, stands, pins or supports of any kind, no text, no logos, no other jewellery, no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Acceptance**

*Fidelity*
- Exactly 2 huggies, identical in form.
- Wide barrel-shaped band, zero stones, no visible hinge gap.
- Matte brushed satin with fine parallel lines running top to bottom.
- No mirror reflections, ridges or hammering, and not a thin hoop.
- Gold tone warm-neutral: not orange or brassy, and not reading as silver tone against the blue.

*Scale and placement*
- Each huggie 0.6–0.8× the jasmine bud's length. The bud is one bud, white, about 2 cm.
- The pair spans 40–48% of the frame width. That is about life size (around 16 px/mm), so no size tag is needed.
- If a huggie renders taller than 266 px (over 19 px/mm), add the size tag.

*Levitation*
- One shadow per huggie, directly below.
- A visible gap of clean floor between each piece and its shadow.
- Nothing reads as a wire, pin or stand.

*Calm zones*
- Frame 15–28% is empty wall.
- Frame below 52% is empty floor.
- The shadows and bud end by 51%.

*Negatives*
- No glints, flare, text, extra jewellery or water.

**Layout: Feed** (1080 × 1350, `<body>`, background `var(--sky)`, ink type, accent `var(--coral-deep)`)
- **Headline:** Cormorant Garamond italic 500, 96 px, `var(--ink)`, centred, top 96: "The ₹699 pair."
  - Width about 450 px.
  - The ₹ comes from the Noto Serif italic subset.
  - The headline uses Cormorant, not Velista, because it holds a price (A13 spec).
- **Beat:** `.beat` 44 px, `var(--coral-deep)`, centred, top 212: "brushed, not polished." It ends near y 258. The pair starts near feed y 310.
- **Card:** `.card` top 880, ink:
  - `logo_ink.png`;
  - "Brushed Gold Huggies";
  - "₹699";
  - `.line` "brushed satin, 18k gold tone · about 14 mm";
  - `.offer` "Buy 2 · 10% off &nbsp;•&nbsp; Buy 3 · 20% off" with `<small>codes BUY2 · BUY3</small>`.
- **Size tag:** only if over 19 px/mm. `.sizetag` right 72, top 560, ink: "Shown magnified<br>about 14 mm tall".
- **Share:** at most 18%; about 8% expected.

**Layout: Story** (1080 × 1920, `<body class="story">`, sky)
- `.wm-top` with `logo_ink.png` at top 290.
- Headline 96 px, centred, top 370.
- Beat 44 px, centred, top 480; it ends near 526. The pair starts near 595.
- Card without the wordmark at top 995 (name, price, line, offer). It must end by 1250.

**Copy**
- **Primary text** (154 characters; the offer ends at character 122): "The ₹699 pair: Brushed Gold Huggies, about 14 mm, in brushed-satin 18k gold tone. BUY2: 10% off 2 pieces, BUY3: 20% off 3. Brushed, never mirror polished."
- **Headline:** "Brushed Gold Huggies · ₹699 · BUY2: 10% off 2"
- **Description:** "Brushed satin · 18k gold tone · about 14 mm"
- **URL:** `https://www.nairaflore.com/products/brushed-gold-huggies?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b01&utm_content={{ad.id}}&utm_term=b01-2_a13_699-pair-levitation`

---

## b01-3 · Verdant Eternity Band · A1 Product Card (no headline), wedding-season picture

- **Handle:** `verdant-eternity-band`. ₹1,049, 58 units. Claims: none used.

**Concept.** This is the F2 grammar on an eligible saturated stone:
- a worn hand on a warm dark ground;
- the piece's green as the only saturated colour;
- the centred card;
- no headline.

The occasion lives in the picture: fresh mehendi on the fingertips, and late-afternoon sun through a jaali.

**Borrows**
- Our F2: a worn crop on cocoa, the centred card, no headline; 4.74x.
- ads-20 S2_06, the Verdant mehendi hand: judged 8.20 and never run.
- Board 72, 91 and 123: hard window sun with patterned shadows.

**Camera and light**
- **C4:** 85 mm worn, about 40° above the hand, field of view about 11 cm across at the hand.
- **L4:** hard sun through a jaali, plus a soft warm bounce.

**Refs**
1. `2c3d1209-2571-4e63-95af-807e4650a83a`, `build/refs/verdant-eternity-band__upright.jpg`. The listing packshot that shows the whole construction: the authority on this exact piece; ignore its background and light.
2. `702645c3-7920-48ac-afaa-5ce4d51e868a`, `build/refs/verdant-eternity-band__cube.jpg`. The same ring from above: take only how the green ovals alternate on either side of the pavé wave.

**Prompt**

> Close editorial hand photograph in a 9:16 vertical frame, 85 mm lens from about 40 degrees above, the frame about 11 cm across at the hand: the left hand of a South Asian person, medium wheatish-brown skin with natural texture, fine knuckle creases and short bare nails, lies palm-down and relaxed on deep cocoa-brown raw silk; the wrist enters from the right edge near the top right corner and the fingers point left and a little down, gently apart, the thumb tucked out of sight under the palm, the little-finger tip ending inside the left fifth of the frame at about 52% of the frame height and the index and middle fingertips just past the left edge. Fresh wedding-season mehendi: the fingertips dipped in deep red-brown henna to the first knuckle and one slim vine of fine henna lines on the back of the hand toward the wrist, the skin around the ring left clear. On the ring finger, just past the knuckle, the Verdant Eternity Band, exactly as in reference 1: a cool PVD rhodium silver-tone open-back band carrying oval emerald-green cubic zirconia of 5 by 4 mm in 4 claws, about five of them showing across the top of the finger, set alternately just above and just below one slim scalloped S-wave of tiny clear pavé that weaves between them; it must stay ovals alternating either side of one wave, never a straight row, never plain links, never round or teal stones, and the metal never gold tone. Scale: true size, the band covering the top of the finger from side to side, each green oval about a third of the width of the ring finger's nail, with a faint contact shadow on the skin; the ring sits at about 56% of the frame width and 36% of the frame height, inside the central 4:5 window, spanning about 16% of the frame width. Scene: the hand fills the upper right of the frame; the whole lower centre and lower right of the frame from about 52% down is calm cocoa silk in soft shade with no fingers in it, for the price card; the top left corner above the fingers carries only the light pattern on the silk. Light code L4: hard late-afternoon sun through one large opening of a carved stone jaali from the upper left lights the hand and the ring in one clean unbroken patch, so the green stones blaze and the pavé sparkles, and throws a crisp lattice of light only onto the silk in the top left corner; one soft warm bounce from the right fills the shadows on the skin. No face, no other body parts, no bangles, no other rings or jewellery, no nail polish, no text, no logos, no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Acceptance**

*Fidelity*
- About 5 green ovals showing across the top of the finger.
- The ovals alternate above and below one scalloped S-wave of clear pavé.
- Not a straight row, not plain links, not round or teal stones.
- Metal cool silver tone, with no gold-tone cast.

*True size*
- The band covers the finger top from side to side.
- Each oval is about 1/3 of the ring finger's nail width.
- Within 1.2× of true size by pixel ruler.
- The ring spans 14–18% of the frame width, which passes the worn metric of at least 12%.

*Styling*
- Henna-dipped fingertips and one slim henna vine; the skin around the ring is clear.
- No bangles and no other jewellery.
- Natural skin texture, not plastic.
- No face.

*Light*
- The hand and ring sit in one clean patch of sun, with no lattice shadow across the ring.
- The lattice falls only in the top-left corner.

*Calm zones*
- From 52% down, the lower centre (x 22–78%) is calm cocoa silk with no fingers in it.
- The ring's lowest point is at or above 41% of the frame height, so it clears the Story card (top 915) by at least 120 px.

*Negatives*
- No glints, flare, text or water.

**Layout: Feed** (1080 × 1350, `<body class="dark">`, background `var(--cocoa)`)
- Card only, `.card` top 880:
  - `logo_white.png`;
  - "Verdant Eternity Band";
  - "₹1,049";
  - `.line` "emerald-green cubic zirconia · adjustable US 5 to 9";
  - `.offer` "Buy 2 · 10% off &nbsp;•&nbsp; Buy 3 · 20% off" with `<small>codes BUY2 · BUY3</small>`.
- Bone type.
- No headline, no size tag (worn, true size).
- **Scrim:** only if lattice light or a fingertip reaches under the card. `.scrim` top 760, `rgba(59,38,32,0)` → `rgba(59,38,32,.6)`.
- **Share:** at most 15%; about 5% expected.

**Layout: Story** (1080 × 1920, `<body class="dark story">`)
- The full card, with its wordmark, at top 915. It ends near 1243 and must end by 1250.
- No other text.

**Copy**
- **Primary text** (155 characters; the offer ends at character 116): "Emerald-green cubic zirconia on both sides of a wave of pavé. Verdant Eternity Band, ₹1,049. BUY2: 10% off 2 pieces. Adjustable, US 5 to 9, in silver tone."
- **Headline:** "Verdant Eternity Band · ₹1,049 · BUY2: 10% off 2"
- **Description:** "Emerald-green cubic zirconia · adjustable"
- **URL:** `https://www.nairaflore.com/products/verdant-eternity-band?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b01&utm_content={{ad.id}}&utm_term=b01-3_a1_mehendi-card`

---

## b01-4 · Woven Gold Hoops · A4 Monument Macro, with the claim as proof (the batch's one new move)

- **Handle:** `woven-gold-hoops`. ₹1,049, 89 units. Claims: allowed (RULINGS §1.1).
- The claim appears only as the second beat, and is shown by the droplets.

**Concept.** One hoop lies on wet plum glaze, shot so low and so large that the braid becomes a monument running off the right edge. The headline is texture; the proof is water. This rebuilds the W1 pair correctly: the texture-led W1 with droplets sold 5, and the claim-led W1 on the same picture sold 0.

**Borrows**
- Board 26 and 42: a monument crop on one field.
- Board 95: an abstract crop plus a two-word claim.
- Board 190: "shown magnified".
- Board 4 and 55: two-beat headlines ("Bold Lashes. Zero Smudge.").
- Our W1 "Woven, not cast." (5 sales) against W1 "Waterproof" (0 sales).

**Camera and light**
- **C5:** 100 mm macro, low at about 15° above the surface.
- **L1:** a hard low raking spot from the left, plus a soft front-right fill.

**Refs**
1. `74ed9a2b-4781-4ab8-b032-fd1b45e847ca`, `build/refs/woven-gold-hoops__pack.jpg`. The authority on this exact piece; ignore its background and light.
2. `b77ec5ba-42ce-4a11-99a0-b8aca88138df`, `build/refs/woven-gold-hoops__detail.jpg`. Take only the braid structure and the flat polished disc latch.

**Prompt**

> Macro product still life in a 9:16 vertical frame, 100 mm macro lens low at about 15 degrees above a wet glazed surface, honest shallow macro depth of field with the near side of the braid razor sharp: one hoop of the Woven Gold Hoops pair lies flat on a smooth deep-plum (aubergine) glazed surface beaded with clear water droplets, shown monumentally large, its thick braided ring curving away from the camera in a wide oval that runs off the right edge of the frame. The hoop, exactly as in reference 1: a round hoop about 25 mm across made of one thick braid about 5 mm thick of many fine polished 18k PVD gold-tone strands with a deep ridge-and-shadow interlace, a thin hinged latch wire and a small flat polished disc at the top of the hoop, zero stones; the braid must stay a many-strand plait with deep ridges, never a smooth tube or a simple two-strand twist, and the hoop itself stays round, never oval or larger. Scale: the braid is about a fifth of the hoop's width and the opening about three fifths; the water droplets are 1 to 4 mm, each smaller than the braid's 5 mm thickness, a few beaded on the braid itself; the hoop sits with a true contact shadow and a soft reflection in the wet glaze; it spans about 85% of the frame width, cropped by the right edge only, its farthest and nearest edges at about 38% and 59% of the frame height, inside the central 4:5 window. Scene: the band from 15% to 35% of the frame height is calm, smooth, softly out-of-focus plum glaze with almost no droplets, for a headline and a size tag, and everything below 62% is calm smooth plum glaze in soft focus for the price card; droplets gather only around the hoop. Light code L1: one hard low raking spotlight from the left skims across the braid so every strand's ridge and shadow is sculpted and each droplet carries one crisp highlight and a small shadow; one soft broad fill from the front right at low power keeps the gold tone warm-neutral, never orange, brassy or blown out. No hands, no people, no second hoop, no other jewellery, no props, no text, no logos, no star-shaped glints, no starburst, no lens flare, no splash, no spray, no running water.

**Acceptance**

*Fidelity*
- One hoop.
- A many-strand braid with a deep ridge-and-shadow interlace: not a smooth tube, not a two-strand twist.
- A flat polished disc latch at the top.
- Zero stones.
- Round in plan; only perspective makes it oval.
- Gold tone warm-neutral, with no blown highlights.

*Scale*
- The braid is about 1/5 of the hoop's width.
- Droplets are 1–4 mm, each smaller than the braid's thickness, with several on the braid.
- A true contact shadow and a reflection.

*Width share*
- The hoop spans 80–90% of the frame width and is cropped by the right edge only.
- It displays magnified (about 35 px/mm), so the size tag is required in both Feed and Story.

*Placement*
- The hoop's far edge is at or below 37%, and its near edge at or above 60%, of the frame height.

*Calm zones*
- Frame 15–35% is smooth soft plum with few droplets.
- Frame below 62% is smooth.

*Water*
- Droplets only, on the surface and the hoop: no splash, spray or pouring.

*Negatives*
- No glints, flare, text, second hoop or extra jewellery.

**Layout: Feed** (1080 × 1350, `<body class="dark">`, background `var(--plum)`)
- **Headline:** `.h1` Velista 96 px, `.02em`, bone, left-aligned, left 72, top 96: "Loud texture.<br>Zero stones." Widths about 704 and 624 px.
- **Beat:** `.beat` Cormorant italic 500, 48 px, `var(--gold-light)`, left 72, top 292: "and yes, waterproof." Width about 340 px.
- **Size tag:** `.sizetag` bone, right 72, top 292: "Shown magnified<br>about 25 mm across". The box is about 410 × 96 and ends near y 388. The hoop starts near feed y 445.
- **Card:** `.card` top 880:
  - `logo_white.png`;
  - "Woven Gold Hoops";
  - "₹1,049";
  - `.line` "braided, about 25 mm · 18k gold tone PVD";
  - `.offer` "Buy 2 · 10% off &nbsp;•&nbsp; Buy 3 · 20% off" with `<small>codes BUY2 · BUY3</small>`.
- **Scrim:** only if droplets reach under the card. `.scrim` top 760, `rgba(74,37,64,0)` → `rgba(74,37,64,.6)`.
- **Count and share:** 3 text elements. Text share at most 18%; about 16% expected. If the render reads over 18%, drop the H1 to 96 px with `.01em` tracking. Never drop the beat, because it carries the claim.

**Layout: Story** (1080 × 1920, `<body class="dark story">`)
- The A4 Story twin: `.wm-top` with `logo_white.png` at top 300.
- `.sizetag` centred (`left:50%; transform:translateX(-50%)`) at top 384.
- Nothing else. The picture's droplets carry the claim.

**Copy**
- **Primary text** (156 characters; the offer ends at character 118): "Loud texture, zero stones: Woven Gold Hoops, ₹1,049, about 25 mm of braided 18k gold tone PVD. BUY2: 10% off 2 pieces. And yes, waterproof and tarnish-free."
- **Headline:** "Woven Gold Hoops · ₹1,049 · BUY2: 10% off 2"
- **Description:** "Braided 18k gold tone PVD · waterproof"
- **URL:** `https://www.nairaflore.com/products/woven-gold-hoops?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b01&utm_content={{ad.id}}&utm_term=b01-4_a4_texture-waterproof`

---

## b01-5 · Prism Rivière Bracelet · A2 Worn Editorial

- **Handle:** `prism-riviere-bracelet`. ₹2,399, 41 units. Claims: none used.

**Concept.** Pastel stones are the only colour in a black frame. A deep-brown wrist rises from a black sleeve and is lit by a direct on-camera flash, so the aqua, pink and pale yellow read true and every stone shows its own halo. This is the dark-ground answer to the Prism statics that lost on pale grounds: 26 ads, ₹28.9k, 0.55x; VK S5 pale on pale sold 0.

**Borrows**
- Board 88: giant lower-third type over a close-up.
- Board 148: the piece at the body with one line.
- Board 11: product plus proof.
- Our F2: worn on a dark ground, the card below the piece.

**Camera and light**
- **C4:** 85 mm worn, eye level, field of view about 12 cm across at the wrist.
- **L2:** a direct on-camera flash, plus a large soft ambient source.

**Refs**
1. `f9e23a88-b9d0-47ec-ae01-461a8585a1a9`, `build/refs/prism-riviere-bracelet__pack.jpg`. The authority on this exact piece; ignore its background and light.
2. `8f1ff732-cbc4-47d0-aa07-6d190c0e059e`, `build/refs/prism-riviere-bracelet__detail.jpg`. Take only the square halos and the mixed colour order.

**Prompt**

> Editorial flash photograph in a 9:16 vertical frame, 85 mm lens at eye level, the frame about 12 cm across at the wrist: one forearm of a South Asian person with deep brown skin with a cool undertone and natural texture rises from the bottom edge in a fitted matte black crepe sleeve that ends about 4 cm below the wrist; the bare wrist is bent back slightly and the hand above it is relaxed with the fingers softly curled forward, the back of the hand toward the camera, partly cropped by the top edge, against a matte charcoal-black backdrop close behind the arm. On the wrist, running across the frame, the Prism Rivière Bracelet, exactly as in reference 1: a single line of square cushion-cut pastel cubic zirconia about 5 mm, each framed by its own fine square halo of tiny clear pavé, linked edge to edge in bright PVD rhodium silver tone, about eight stones showing across the top of the wrist, the colours mixing aqua blue, soft pink and pale yellow with no two neighbours the same colour, the fold-over clasp hidden under the wrist; it must stay exactly these three pastel colours, every stone in its own halo, never a fourth colour such as lilac or green, never bare stones, never gold tone. Scale: true size, each stone with its halo about 7 mm, about an eighth of the wrist's width, lying flat on the skin with a faint contact shadow; the bracelet spans about 48% of the frame width and sits at about 30% of the frame height, inside the central 4:5 window. Scene: from about 37% of the frame height down to the bottom the frame is calm matte black sleeve and charcoal-black backdrop for type and the price card, with nothing bright below the bracelet; nothing important touches the side edges. Light code L2: one direct on-camera flash, hard and frontal, makes the pastel stones read in true colour with crisp sparkle and throws a short hard shadow of the hand onto the backdrop just behind it; one large soft ambient source from the left at low power gives the skin gentle dimension and keeps its texture. No face, no other body parts, no rings or other jewellery, no nail polish, no text, no logos, no star-shaped glints, no starburst, no lens flare, no water, no droplets.

**Acceptance**

*Fidelity*
- Square cushion pastel stones, each in its own square pavé halo.
- Only aqua, pink and pale yellow; no two neighbours the same colour; no lilac or green.
- About 8 stones across the wrist top.
- Bright silver-tone links. The clasp is hidden.

*True size*
- Each stone with its halo is about 1/8 of the wrist's width.
- Within 1.2× of true size.
- The bracelet spans 42–52% of the frame width.

*Placement*
- The bracelet is centred at 28–32% of the frame height.
- Its lowest point is at or above 33.5% (y 643), which clears the Story wordmark at 772 and the Feed headline at feed y 640 by at least 120 px.

*Calm zones*
- From 37% down: black sleeve and backdrop, with no sheen streak under the headline or card.

*Flash honesty*
- True colours.
- Skin natural with texture, not plastic or over-smoothed.
- A hard shadow behind the hand.

*Negatives*
- No face, rings, glints, flare, text or water.

**Layout: Feed** (1080 × 1350, `<body class="dark">`, background `var(--ink)`)
- **Headline:** `.h1` Velista 72 px, `.02em`, bone, centred, top 640: "Every stone<br>in its own halo." Widths about 452 and 608 px; ends near 781.
- **Beat:** `.beat` Cormorant italic 500, 44 px, `var(--gold-light)`, centred, top 792: "in aqua, pink and pale yellow." Ends near 837.
- **Card:** `.card` top 880:
  - `logo_white.png`;
  - "Prism Rivière Bracelet";
  - "₹2,399";
  - `.line` "18 cm · fits 15 to 19 cm wrists · silver tone";
  - `.offer` "Buy 2 · 10% off &nbsp;•&nbsp; Buy 3 · 20% off" with `<small>codes BUY2 · BUY3</small>`.
- **Size tag:** none (worn, true size).
- **Share:** at most 22%; about 11% expected.

**Layout: Story** (1080 × 1920, `<body class="dark story">`)
- `.wm-top` with `logo_white.png` at top 772. The top of the Story is the hand, so the lockup stacks below the bracelet.
- `.h1` Velista 64 px, centred, top 850: "Every stone<br>in its own halo." Ends near 976.
- Card without the wordmark at top 995, ending by 1250.
- The beat is dropped in the Story to fit.

**Copy**
- **Primary text** (157 characters; the offer ends at character 125): "Every stone in its own halo: aqua, pink and pale yellow. Prism Rivière Bracelet, ₹2,399, silver tone. BUY2: 10% off 2 pieces. 18 cm, fits 15 to 19 cm wrists."
- **Headline:** "Prism Rivière Bracelet · ₹2,399 · BUY2: 10% off 2"
- **Description:** "Aqua, pink and pale yellow · silver tone"
- **URL:** `https://www.nairaflore.com/products/prism-riviere-bracelet?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b01&utm_content={{ad.id}}&utm_term=b01-5_a2_halo-flash`

---

## 5. Notes for the builder and verifier

- **Velista lines** carry no digits, ₹, middle dots or dashes. Set them with `font-variant-ligatures: none`; the kit's `.h1` already does this.
- **The renderer must report:**
  - `fallback: []`;
  - `outside: []`;
  - `minFont` of 26 or more (22 only for footnotes, and there are none in this batch);
  - text share inside each archetype target.
- **A failed picture** is regenerated once at most, with the fix written into the prompt (RULINGS §1.2). If it fails again, the slot is dropped for this batch, not edited.
- **Worn frames** are measured at 100% against the true-size rules above. A frame over 1.2× is discarded, never edited.

**The b02 critic must answer**
1. Which ad reads first at 200 px, and which beat the F2 anchor?
2. Does the levitation on sky read as honest at once, and does the Cushion spotlight read as "proposal" without the headline (Story)?
3. Does the Woven claim, as a beat, sit as proof rather than the message?
4. Does the flash skin on b01-5 look photographed or generated?
5. Which dimension scored lowest? That becomes the b02 fix target.
6. Once live: does the A1 card with no headline (b01-3) earn add-to-carts comparable to the headline ads? This is confounded by product; the clean same-frame test waits for a later batch.

**Queued for later batches**
- Cushion: an A1/A2 pair on separate frames.
- Brushed: A9 day/night.
- Verdant Circlet: A8 callouts.
- Halo Curve: A4 cane gobo.
- Serpentine Silver: A7.
- Monochrome: A13 on saffron. No claims.
