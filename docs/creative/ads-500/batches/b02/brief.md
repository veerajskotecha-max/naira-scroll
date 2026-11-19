# b02 brief (19 Nov 2026, written about 17:30 UTC)

Creative director's brief for batch b02: 5 static ads, `b02-1` to `b02-5`. Sources, in order of precedence: `RULINGS.md`,
`PLAYBOOK.md`, `build/study/products.md`, `build/learnings.md`, `build/ledger.json`, `batches/b01/review.md` and
`batches/b01/loop.md`. Nothing has been generated for b02 yet.

## 0. Pre-flight

| Check | Result |
|---|---|
| Higgsfield balance | **56.46 credits at 17:06 UTC; 48.46 at 17:32 UTC.** The 16:55 loop check read 94.46, so about 38 credits went in 11 minutes, then 8 more in the next 26 minutes. b01 jobs do not account for it, so the outside spending continues at a slower rate. |
| Credit rule (loop change 1) | Cost is 2 credits a picture, plus 2 credits reserved per slot for its one regeneration, plus the 10-credit floor. Keep all 5 slots while (balance − 10) ≥ 4 × slots, that is a balance of at least 30. At 17:32 that is 38.46 ≥ 20, so **no cut**. **The generator re-reads the balance right before the single `generate_image_batch` call.** It cuts slots in this order: b02-5 first, then b02-2, b02-4, b02-3. b02-1 (the new move) is cut last. |
| Stock and price (Shopify, read-only, 17:06 UTC) | Stock and price for all 14 products match RULINGS §2. This batch uses: Woven 89 · ₹1,049; Brushed 58 · ₹699; Verdant Circlet 32 · ₹899; Prism 41 · ₹2,399; Verdant Eternity 58 · ₹1,049. All are single-variant SKUs. |
| Offers (Shopify `discountNodes`, 17:08 UTC) | All active, none automatic, no end date: NAIRA10 (10%, no minimum), BUY2 (10%, 2+ items), BUY3 (20%, 3+), BUY4 (30%, 4+). FRIENDSANDFAMILY is internal and not for ads. No free-shipping discount exists. |
| Claims | All five products carry the Waterproof, Tarnish Free and Hypoallergenic tags (RULINGS §1.1). Water appears only in b02-1, as proof. |
| Excluded | Serpentine (gold) and Bold Nocturne: each has exactly 20 units and no headroom (loop change 6). Toggle: not briefed. Cushion: rests this batch because it shipped in b01. |
| Kit (loop change 7) | **Done in this step.** `kit/kit.css` no longer has `.offer small` (`grep -c 'offer small'` returns 0). It now has the `.offer .sep` 9 px lozenge, gold-light on `.dark` pages and coral-deep on light grounds. A test render of `b01-4_feed.html` gives `minFont 26, outside [], fallback []`. b02 pages use `<span class="sep"></span>` with no inline offer CSS. |
| Open zero-credit item (loop change 4) | **The finisher re-renders `b01-4_story.jpg` before any b02 render, but only if critic A's re-score clears b01-4 (loop change 8).** The added text is "BRAIDED HOOPS. / ZERO STONES." (Velista 76), name and ₹1,049 on one line, and the one-line offer. The measured free band is y 270–700, and the hoop starts at y 708. The size tag stays. |

## 1. Batch idea

**Desire through the body, on one composition template built around the model's centring.**
- **Worn frames.** Three are briefed so that at least two ship:
  - b02-1: the Woven pair at the nape;
  - b02-3: the Verdant Circlet on one ear;
  - b02-4: Prism across a wrist.
- **Crazy ads.** Two honest surprises:
  - b02-2: Brushed levitation;
  - b02-3: selective colour, generated directly.
- **Explainer.** One A5 numeral (b02-5: "5–9", one ring fits US 5 to 9) answers the ring-size doubt.
- **The template, on every picture:**
  - the subject's whole extent at 36–61% of the 9:16 frame;
  - calm type zones at 14–34% (Feed headline, all Story text) and 63–80% (Feed card).
- **The one new move** (learnings, loop change 2): **the worn Woven pair with b01-4's on-image copy, card and offer unchanged**. Only the picture changes, from monument to body.

## 2. What b01 lacked, and how b02 answers it

| Layer | Missing or weak in b01 (shipped 2 of 5, mean 7.26) | b02 answer |
|---|---|---|
| Visual / desire | No body, skin or moment. Desire was the lowest dimension at 6.75. Both shipped ads were cold still lifes on dark jewel grounds. | Three worn frames. Each has a named skin tone with texture and one wedding-season detail (zari blouse back, Banarasi zari edge, mehendi). Styling varies: wet hair combed back, loose hair over the ear, a bare forearm on velvet. No ivory shirt, no low bun. |
| Surprise | b01-1's beam rendered as a smear, and the A13 levitation was dropped, so nothing surprising shipped. | b02-2 rebuilds b01-2. Its levitation and detached shadows did render; only placement and the jasmine bud failed. The bud is gone, and the pair plus shadows sit inside 36–61%. b02-3 is a black-and-white frame where the stud is the only colour (board 85). |
| Placement / yield | 3 of 5 dropped because the model centres subjects (37–62%) and oversizes worn pieces (1.27–1.6×). | Every prompt centres the subject on purpose and states placement as physical geometry: camera height, what the hair covers, which edge the arm enters from. Every piece is locked by a ratio inside the piece first, then one body ratio. Worn fields of view are set so true size passes 12% of the width. |
| Product type at 200 px | b01-4's flat hoop read as a bangle. Its Story dropped the headline that fixed this. | Earrings are only worn: the Woven pair with both hoops visible, and the Circlet on the ear. Every Story carries the headline (where the Feed has one), name, price and offer. |
| Camera and light | Both ships were L1 on a tabletop, one cold mood. Variety came only from dropped slots. | Five lights: L5, L1, L2, L3, L7. Four cameras: C2, C4, C1, C5. Grounds: apricot, sky, black-and-white, ink velvet, saffron. No hard spot on a dark ground. |
| Layout | Offer `small` at 20 px; Stories without name or price; b01-1's ring at 31.8% of the width (under the 35% rule). | Fixed bands (§3). The kit offer is one 26 px line. Product-only pieces are briefed at 40–45% of the width, with size tags where magnified. |
| Branding | One card and a 56 px wordmark held. The kit itself was not updated. | Same card in the same place on all five. Kit fixed. The selective-colour ad takes its accent from the stone (playbook §4.0 allows the stone hue). |
| Copy | First beats were truth-led. The bundle and ₹699 never shipped. Meta headlines were cut at 40. | "The ₹699 pair." with the beat "any three pieces, 20% off." "GREEN STONE. / GOLD TONE." Numeral "5–9" with "US SIZES, ONE RING." Woven copy is held fixed. Occasions appear only as a second beat or in the picture. Meta headlines ≤40 characters with the value inside. Descriptions ≤30. Offer ends by character 124 at the latest. |
| Products | Only Cushion and Woven shipped. | Heroes Brushed and Verdant Eternity return. Verdant Circlet appears for the first time. Prism is retried with the wrist geometry fixed. Woven takes its second and last phase-1 slot. |

### Loop changes, one by one

1. **Credits.** Balance read at 17:06 with the reserve and the cut order (§0). The generator writes `submitted_at` and `credits` per job into `jobs.json` from the `transactions` rows. The learnings agent corrects the three "4 credits a picture" lines to 2.
2. **Fix target desire.** Three worn frames are briefed. The new move is b02-1, held to b01-4's copy, card and offer, with a named skin tone and a zari blouse edge. Woven is now at its phase-1 cap of 2; b03–b10 brief no Woven unless it unlocks.
3. **Template.** Every prompt puts the whole subject (piece, shadows, nothing else) at 36–61% of the frame:
   - Feed: y 406–887.
   - Story: y 691–1171.
   - Fixed bands: Feed headline, beat and size tag in y 84–370; Feed card top at 940, ending by 1258; Story text in y 270–650.
   - Light is described by its visible result.
   - The verifier measures each subject's extent first and drops anything outside 35–62%.
4. **Earrings and Stories.**
   - Woven is shown as a worn pair, both hoops visible.
   - The Circlet is worn on one ear. The listing itself says "a wedding function where one bold ear is enough", and an ear crop names the type at 200 px. A single loose or flat earring is a reject.
   - Every Story carries name, price and the 26 px offer (plus the headline where the Feed has one), all inside y 270–650.
   - The b01-4 Story fix is assigned to the finisher (§0).
5. **Variety.**
   - Five different lights, L7 once.
   - Four cameras. The worn slots are C2, C4 and C1, not all C4.
   - Three light or flat saturated grounds (apricot, sky, saffron). No hard spot on a dark ground.
   - The gold-tone pair on sky is tilted about 15°. It is not cropped by an edge: cropping would hide the detached shadows that prove the float, and change 6 asks for the pair at about 40% of the width.
6. **₹699 slot.**
   - b02-2: Brushed, product-only, the pair at about 40% of the width, with the bundle value in the beat. A size tag goes on only if the render passes 19 px/mm.
   - Fresh Shopify read with timestamps (§0).
   - Zero-headroom SKUs left out.
   - Four SKUs b01 did not ship: Brushed, Circlet, Prism, Verdant Eternity.
7. **Kit.** Applied (§0).
8. **Scoring.**
   - Critics score the final Feed and Story JPGs, at full size and at 200 px.
   - A script computes the §7 weighted means.
   - The truth floor of 8 applies to each critic.
   - `review.md` and the ledger carry `scoredFile` and its modification time.
   - The verifier logs one ratio inside each piece; each spec's acceptance list names it.
   - Critic A re-scores `b01-4` before b02-1 is compared with it. If b01-4 is held, b02-1 is read against W1 "Woven, not cast".

**Queued for b03, not b02** (one new move per batch):
- NAIRA10 on single-product ads (loop "Queued").
- Products still to appear: Halo Curve, Pearl Double Halo, Monochrome, Serpentine Silver, Ribbon. Cushion returns.

## 3. Shared layout system for b02

- **Picture.** 9:16, 2K. The Feed is the central 4:5 crop. Conversion: Feed y = (f − 0.148) / 0.704 × 1350; Story y = f × 1920.
- **Feed bands.**
  - Headline, beat and size tag: y 84–370 (frame 19–34%).
  - Subject: y 406–887.
  - Card: top 940 → about 1236, centred on x 540. Card stack: wordmark 56 px, name Jost 500 26 .2em, price Cormorant 500 56, line Jost 400 26, offer one 26 px line.
  - Offer text on every ad: `Code BUY2 · 10% off <span class="sep"></span> BUY3 · 20% off`.
- **Story block (all text inside y 270–650).**
  - Wordmark: 270–326.
  - Headline: Velista 76, two lines, 340–489, or the ad's own headline face at the size given in its spec.
  - Name and price on one line, baseline-aligned, 24 px gap: about 501–557.
  - Offer: about 571–633.
  - The Feed beat is dropped in the Story unless the spec keeps it.
  - Nothing is placed over the subject at y 691–1171.
- **Type.** Bone on dark, ink on light. Accent gold-light on dark, coral-deep on light. Velista lines carry no digits, ₹, middle dots or dashes. Floor 26 px, except the A5 footnote at 22 px.
- **Render gates.** `failed [] · overflow [] · fallback [] · outside []`, `minFont ≥ 26` (A5 footnote 22), and text share within each archetype's target.

## 4. The five ads

| Id | Product (stock · price) | Archetype | Light | Camera | Ground | Worn | Crazy | Cut order |
|---|---|---|---|---|---|---|---|---|
| b02-1 | Woven Gold Hoops (89 · ₹1,049) | A2 Worn Editorial (new move) | L5 | C2 | apricot | yes (nape, pair) | no | last |
| b02-2 | Brushed Gold Huggies (58 · ₹699) | A13 Suspended | L1 | C2 | sky | no | yes | 2nd |
| b02-3 | Verdant Circlet Studs (32 · ₹899) | A2 Worn Editorial, selective colour | L2 | C4 | black and white | yes (ear) | yes | 4th |
| b02-4 | Prism Rivière Bracelet (41 · ₹2,399) | A1 Product Card (F2 grammar) | L3 | C1 | ink velvet | yes (wrist) | no | 3rd |
| b02-5 | Verdant Eternity Band (58 · ₹1,049) | A5 Truth Split (numeral) | L7 | C5 | saffron | no | no | 1st |

- Archetypes: A1, A2, A5, A13 (4). Lights: 5. Cameras: 4. Products: 5, one ad each.
- Type-led ads: 1 (A5). Anton: none.

---

### b02-1 · Woven Gold Hoops · A2 Worn Editorial · L5 · C2 · the one new move

- **Concept.** b01-4's exact words, card and offer over a new picture:
  - the braided pair worn at the back of a wet-haired head before a wedding function;
  - water beads on the nape and hoops as the proof;
  - a gold zari edge on the blouse back.
  - Live results against b01-4 show whether the body beats the monument.
- **Borrows.**
  - From our account: F2 (warm skin, the piece as the warm accent, the card); the Apricot quiet winner (warm apricot world, the upright pair); W1 "Woven, not cast" (texture headline); b01-4 (copy held fixed).
  - From the board: rank 88 (big type over a close-up), rank 70 (piece and body read as one unit), rank 1 (backlit glow).
- **Refs.**
  - Slot 1: `74ed9a2b-4781-4ab8-b032-fd1b45e847ca`, `build/refs/woven-gold-hoops__pack.jpg`. "The authority on this exact piece; ignore its background and light."
  - Slot 2: `b77ec5ba-42ce-4a11-99a0-b8aca88138df`, `build/refs/woven-gold-hoops__detail.jpg`. "Take only the many-strand braid and the thin latch wire with its small flat disc."
- **Prompt.**
  > Vertical 9:16 beauty photograph, 85 mm lens, low hero angle: the camera is behind the woman and about 30 degrees to her left, about 10 cm below her earlobes and tilted up about 12 degrees, framing only the back of her head, both earlobes, her nape and the top of her shoulders, about 17 cm across; her face is turned fully away, so no eye, nose or lips is anywhere in the frame. FIDELITY: she wears the pair of Woven Gold Hoops from the reference, one in each earlobe: each a round hoop about 25 mm across made of one thick braid of many fine polished 18k gold-tone strands, about 5 mm thick, with deep ridge-and-shadow interlace, a thin hinged latch wire and a small flat polished round disc at the top, zero stones. The braid must stay a many-strand braid with deep ridges, never a smooth tube or a simple two-strand twist; each hoop must stay round, never oval and never larger; the latch stays a thin wire, never a chunky hinge block. Both hoops hang open-face to the camera so each reads as a full round ring: the near one whole and sharp beside the near side of her neck, the far one fully visible beside the far side of her neck. SCALE: each hoop's diameter is five times its braid thickness and about one quarter of the width of her neck, never a third; its lowest point hangs level with the angle of her jaw, never below it; each hoop rests against the skin with a faint soft contact shadow. SCENE: her hair is wet, dark and combed straight back, smooth and sleek over the tops of both ears and up into a high knot that sits above the top edge of the frame, so only the earlobes show below the hair; warm medium-brown skin with visible pores and fine texture; a few clear water droplets of 2 to 3 mm on her nape and the side of her neck and one tiny bead on the lower curve of each hoop, as after a bath before a wedding function; at the bottom of the frame the back neckline of a deep oxblood raw-silk blouse with a fine gold zari edge; behind her a plain seamless warm apricot backdrop. PLACEMENT: the two hoops hang across the middle of the frame, their tops at the earlobes at about 44% and their lowest points at about 53% of the frame height, the whole subject inside the central 4:5 window; from the top of the window down to about 36% the frame shows only her smooth dark wet hair filling the width, a calm area for type; below the hoops her nape and neck run down to the zari edge at about 76%, and the band from 62% to 80% is calm smooth skin and plain silk for the card. LIGHT, L5 backlit rim with bloom: one hard warm backlight from beyond her head, aimed toward the camera, draws a thin bright rim along her neck, jaw edge and earlobes, rims each hoop's braid and makes the droplets sparkle as small round points, with a soft warm bloom where it meets the apricot backdrop; plus one large soft fill from behind the camera that shows the skin texture of the nape and the ridge-and-shadow of each braid. Gold tone stays warm-neutral, never orange or brassy. NEGATIVES: no face, no eye, no nose, no lips, no text, no logos, no other jewellery (no hair pins, no chains, no second piercings), no star-shaped glints, no starburst, no lens flare, no tattoos.
- **Acceptance.**
  - **Placement (checked first).** Both hoops lie within 36–61% of the frame height (Feed y 406–887); drop if outside 35–62%.
  - **Face.** No eye, nose or lips visible.
  - **The pair.** Both hoops are visible and read as round rings. The near hoop is whole and sharp. The far hoop is visible beside the far side of the neck. Ellipse ratio ≥ 0.75. A single hoop or a flat hoop is a reject.
  - **Construction.** A many-strand braid with deep ridges, never a tube or a two-strand twist. Zero stones. A thin latch wire, not a hinge block. A small flat disc at the top. Warm-neutral gold, not orange.
  - **Ratio inside the piece (log it).** Hoop diameter ÷ braid thickness = 4.5–5.5.
  - **Body ratio.** Hoop diameter ÷ neck width = 0.20–0.30 (true about 0.24). The lowest point is not below the jaw angle. Anything over 1.2× true is a drop.
  - **Size.** The near hoop is ≥ 12% of the frame width (at 17 cm it is 14.7% at true size).
  - **Calm zones.** At 14–34% the frame is dark, smooth hair across x 72–800, with no ear tops and no bright backdrop under the headline. At 63–80% there is calm nape or silk. The zari edge is visible inside the 4:5 window.
  - **Water.** Droplets 2–3 mm on the skin, at most one tiny bead per hoop. They read as water, not sweat.
  - **Skin.** Warm medium-brown with pores, not plastic.
  - **Negatives.** No other jewellery, no star glints, no flare streaks.
- **Layout.**
  - **Feed.** b01-4's type held fixed so only the picture changes. `body.dark`.
    - `.h1` "Braided hoops.<br>Zero stones." Velista 92 px, letter-spacing .01em, nowrap, bone, left 72, top 88 (ends about 270).
    - `.beat` "and yes, waterproof." Cormorant Garamond italic 500, 48 px, gold-light, left 72, top 296.
    - No size tag (worn at about 6.4 px/mm, below life size).
    - `.card` top 940: `logo_white` 56; "Woven Gold Hoops"; "₹1,049"; line "hoop earrings · 18k gold tone PVD"; one-line offer with `.sep`. Ends ≤ 1258.
    - `.scrim`: linear in the picture's own dark oxblood-brown, 0 at y 860 to .55 at 1350. Add a radial pool in the hair's tone behind the headline only if any bright backdrop sits under the type.
    - If the hair does not fill x 72–800 at y 84–370, centre both lines at the same sizes.
    - Text share ≤ .18 (b01-4 was .173; the A2 cap is .22).
  - **Story.**
    - `logo_white` at 270–326.
    - "BRAIDED HOOPS. / ZERO STONES." Velista 76, centred, 340–489.
    - "WOVEN GOLD HOOPS" and "₹1,049" on one line, 501–557.
    - Offer 571–633.
    - No beat: the water is in the picture. Nothing below 650.
- **Copy.**
  - **Primary text** (157 characters; offer ends at 119; identical to b01-4): "Braided hoops, zero stones: Woven Gold Hoops, ₹1,049, about 25 mm across, in 18k gold tone PVD. BUY2: 10% off 2 pieces. And yes, waterproof and tarnish-free."
  - **Headline** (37): "Woven Gold Hoops · ₹1,049 · 10% off 2"
  - **Description** (30): "18k gold tone PVD · waterproof"
  - **URL:** `https://www.nairaflore.com/products/woven-gold-hoops?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b02&utm_content={{ad.id}}&utm_term=b02-1_a2_woven-worn-nape`

---

### b02-2 · Brushed Gold Huggies · A13 Suspended (levitation) · L1 · C2

- **Concept.** The ₹699 pair floats over a sky-blue field, with each huggie's own detached shadow on the floor as the honest proof. The headline is the price, the beat the bundle value. This is b01-2's picture, which did render the float, rebuilt for a centred subject without the oversized bud.
- **Borrows.** Board 96 (levitation with a detached shadow, two-weight headline), boards 26 and 42 (one flat saturated field), PLAYBOOK B1-03 copy, b01-2's working float.
- **Refs.**
  - Slot 1: `7c95b6c6-b5a1-4886-82e7-69c1c6a3940f`, `build/refs/brushed-gold-huggies__pack.jpg`. "The authority on this exact piece; ignore its background and light."
  - Slot 2: `4c630657-80e8-47f5-ad65-1f0938c70900`, `build/refs/brushed-gold-huggies__macro.jpg`. "Take only the brushed-satin finish and the wide band."
- **Prompt.**
  > Product still life in a vertical 9:16 frame, 100 mm macro feel, camera low at about 12 degrees above the floor (low hero): a pair of Brushed Gold Huggies hover side by side about 3 cm above a flat matte sky-blue floor that curves up into a sky-blue wall with no horizon line, each tilted about 15 degrees off vertical, the left one turned so its broad brushed front face shows, the right one turned three-quarters so its round opening shows, about 8 mm apart. FIDELITY: each huggie is the piece in the reference: a chunky huggie about 14 mm by 9.8 mm, a wide flat band about 6 mm deep in soft brushed-satin 18k PVD gold tone with very fine parallel brush lines, a hidden hinge, zero stones; the two are identical. The finish must stay matte and light-scattering with one broad soft sheen, never mirror-polished, never ridged, hammered or stone-set, and never a large thin hoop. SCALE: each band's depth is about four tenths of its height and the pair together spans about 40% of the frame width; directly below each huggie on the floor lies its own crisp, soft-edged shadow of the same shape, separated from the piece by a clear gap of blue floor about one huggie-height tall, so the pair visibly floats; honest macro depth of field. SCENE: nothing else, only the sky-blue seamless. PLACEMENT: the pair floats on the vertical centre line with its top at about 40% and its bottom at about 49% of the frame height, the two shadows on the floor at about 53% to 59%, all inside the central 4:5 window; the frame above 36% is empty, evenly lit sky-blue wall, a calm area for type, and the floor below 62% is empty sky blue, calm for the card. LIGHT, L1: one hard warm spotlight from directly above and slightly in front casts the two shadows straight down and gives each band one broad satin sheen; plus one soft white bounce card low in front that lifts the underside of each band. The gold tone stays warm-neutral against the blue, never orange or brassy and never reading as silver. NEGATIVES: no hands, no people, no strings, wires, stands, pins or supports of any kind, no props, no flowers, no text, no logos, no other jewellery, no star-shaped glints, no starburst, no lens flare, no water, no droplets.
- **Acceptance.**
  - **Placement (checked first).** Huggies and both shadows within 36–61%; drop if outside 35–62%.
  - **Float.** A clear floor gap between each huggie and its own shadow of at least 0.5× the huggie height. Shadows directly below and the same shape. No support of any kind.
  - **Finish.** Brushed satin with fine parallel lines and one broad sheen, never mirror. Both identical. Zero stones. Not a thin large hoop.
  - **Ratio inside the piece (log it).** Band depth ÷ height = 0.35–0.5.
  - **Width.** The pair spans 35–45% of the frame width; each huggie is tilted 10–20°.
  - **Scale.** Measure px/mm on the 1080 Feed. Over 19 px/mm, add the size tag.
  - **Colour.** Warm-neutral gold, not orange and not reading silver on blue.
  - **Calm zones.** 14–34% empty wall; 63–80% empty floor.
  - **Negatives.** No glints, no props, no bud.
- **Layout.**
  - **Feed.** Light ground: `body` (not `.dark`), ink type, accent coral-deep.
    - `.h1`-position headline "The ₹699 pair." in Cormorant Garamond italic 500, 96 px, ink, centred, top 104. A13 allows Cormorant 96 when the headline holds a price. ₹ comes from the Noto Serif subset.
    - `.beat` "any three pieces, 20% off." Cormorant italic 500, 52 px, coral-deep, centred, top 226.
    - Size tag only if the render is over 19 px/mm: "Shown magnified / about 14 mm tall", right 72, top 292.
    - `.card` top 940: `logo_ink`; "Brushed Gold Huggies"; "₹699"; line "soft brushed satin, not mirror polished"; offer with an ink hairline and coral-deep `.sep`.
    - No scrim on the flat sky. Text share ≤ .18.
  - **Story.**
    - `logo_ink` at 270–326.
    - "The ₹699 pair." Cormorant italic 80, centred, 342–424.
    - Beat 52 coral-deep, 436–489.
    - Name and price, 501–557.
    - Offer 571–633.
    - If a size tag is needed, it replaces the beat in the Story.
- **Copy.**
  - **Primary text** (158; offer ends at 119): "The ₹699 pair: Brushed Gold Huggies, about 14 mm, in soft brushed satin 18k gold tone. Any 3 pieces with BUY3: 20% off. Never mirror polished, and waterproof."
  - **Headline** (39): "Brushed Gold Huggies · ₹699 · 20% off 3"
  - **Description** (29): "Brushed satin · 18k gold tone"
  - **URL:** `https://www.nairaflore.com/products/brushed-gold-huggies?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b02&utm_content={{ad.id}}&utm_term=b02-2_a13_brushed-699-levitation`

---

### b02-3 · Verdant Circlet Studs · A2 Worn Editorial, selective-colour variant · L2 · C4

- **Concept.**
  - A black-and-white flash portrait of one ear at a wedding function. The stud's emerald-green stone and gold tone are the only colour in the frame, generated directly with no grade or edit.
  - The headline names the two colours, and its keyword takes the stone's hue (board 85).
  - This is the first appearance of Verdant Circlet in ads-500.
- **Borrows.** Board 85 (selective colour; the keyword in the product's colour), F2 (the card, a close crop of the body), board 70 (the piece and the body read as one unit), the idea bank's "Banarasi ear" (ads-20 S2_10).
- **Refs.**
  - Slot 1: `ef075ae6-abb2-4efd-9108-a4c2ef76b4ee`, `build/refs/verdant-circlet-studs__pack.jpg`. "The authority on this exact piece; ignore its background and light."
  - Slot 2: `d7f77110-55db-4cd1-9ef0-215aab296b41`, `build/refs/verdant-circlet-studs__detail.jpg`. "Take only the open circlet's construction: small clear stones, two gold stars, two pearls, the open centre."
- **Prompt.**
  > Vertical 9:16 black-and-white beauty photograph with selective colour, 85 mm lens at ear height, eye level: a tight side profile of a woman's left ear, jaw line and the side of her neck, about 11 cm across, her head turned about 10 degrees away from the camera past profile; the crop is so tight, with the ear at the centre, that her cheek runs out of the left edge long before her eye, so no eye, nose or lips is anywhere in the frame. FIDELITY: in her earlobe one Verdant Circlet Stud from the reference, its face toward the camera: about 16.8 mm tall in 18k PVD gold tone; one cushion-cut emerald-green cubic zirconia about 10 mm sits at the top, overlapping the upper edge of an open circlet about 10 mm across; the circlet is made of about five small claw-set clear cubic zirconia, two small four-point gold stars, one white shell pearl about 6 mm on its side and one small pearl near its bottom, and its centre is open so the skin shows through. The green stone must stay at the top, never centred inside the circle; the circlet must stay open, never closed into a disc; exactly two pearls and two stars. SCALE: the whole stud is about a quarter of the height of her ear and about as tall as her earlobe, never taller than a third of the ear; the green stone's width is about six tenths of the stud's height; a faint crisp contact shadow on the lobe beneath the circlet. SCENE: smooth, dark, loose hair falls over the upper two thirds of her ear and is tucked behind the rest, so only the lobe and the lowest part of the ear are bare; dusky warm-olive skin with visible pores and fine downy texture along the jaw; at the bottom of the frame the shoulder edge of a Banarasi silk blouse with a woven zari border; a plain seamless backdrop. COLOUR: the whole photograph is black and white, rich grey tones in the skin, hair, blouse, its zari border and the backdrop, except the stud: its emerald-green stone stays vivid green and its gold-tone metal stays warm gold, the only colour in the picture; the pearls stay white. PLACEMENT: the stud sits at the middle of the frame, between about 44% and 53% of the frame height, slightly right of centre, inside the central 4:5 window; from the top of the window down to about 36% the frame shows only her smooth dark hair, a calm area for type; below the stud the jaw line and the side of her neck run down to the blouse border at about 78%, and the band from 62% to 80% is calm smooth neck and plain silk for the card. LIGHT, L2: one direct on-camera flash, hard and frontal, gives the skin a crisp glossy editorial look and throws a short hard drop shadow of the stud and lobe onto the neck behind, the cubic zirconia sparkling as small round points; plus one soft ambient fill so the hair keeps its detail. NEGATIVES: no eye, no nose, no lips, no text, no logos, no other jewellery, no second piercing, no colour anywhere except the stud, no star-shaped glints, no starburst, no lens flare, no water.
- **Acceptance.**
  - **Placement (checked first).** The stud within 36–61% of the height; drop if outside 35–62%.
  - **Colour.** Black and white everywhere except the stud (green stone and gold-tone metal). Any colour in the skin, lips, blouse, zari or backdrop is a reject.
  - **Face.** No eye, nose or lips.
  - **Construction.**
    - one cushion-cut green stone at the top, overlapping the circlet;
    - the circlet open, with skin visible through its centre;
    - about 5 small clear claw-set stones;
    - exactly 2 four-point gold stars;
    - exactly 2 pearls, one about 6 mm on the side and one small.
    - The green is never centred inside the circle, and the circlet is never closed.
  - **Ratio inside the piece (log it).** Green stone width ÷ stud height = 0.5–0.7.
  - **Body ratio.** Stud height ÷ visible ear height = 0.22–0.33 (true about 0.28). Anything over 1.2× true is a drop.
  - **Size.** Stud width ≥ 12% of the frame width (about 12.7% at true size at 11 cm).
  - **Calm zones.** 14–34% smooth dark hair (the bare ear starts below about 34%); 63–80% calm neck or silk.
  - **Skin.** Dusky warm-olive with pores in grey tones.
  - **Light.** Flash speculars are small round points, no rays.
  - **The stud reads as an earring at 200 px.**
- **Layout.**
  - **Feed.** `body.dark`.
    - `.h1` "Green stone.<br>Gold tone." Velista 80 px, .02em, left 72, top 96, two lines.
    - "GREEN STONE." is set in the stone hue sampled from the render's mid-green (start #2E9E68; keep 4.5:1 contrast on the hair). "GOLD TONE." is set in gold-light. This is board 85's keyword-in-the-product's-colour device, and §4.0 allows the stone hue as an accent.
    - `.beat` "for every function this season." Cormorant italic 500, 48 px, bone, left 72, top 278.
    - `.card` top 940: `logo_white`; "Verdant Circlet Studs"; "₹899"; line "about 16.8 mm · emerald-green cubic zirconia"; offer.
    - `.scrim`: neutral black (the picture's own grey, never a coloured token, which would break the selective colour), 0 at y 860 to .55 at 1350.
    - Text share ≤ .22.
  - **Story.**
    - `logo_white` at 270–326.
    - Headline, same colours, Velista 76, left 72, 340–489.
    - Name and price, 501–557.
    - Offer 571–633.
- **Copy.**
  - **Primary text** (166; offer ends at 122): "Green stone, gold tone: Verdant Circlet Studs, ₹899, about 16.8 mm tall, with a white shell pearl. BUY2: 10% off 2 pieces. For a wedding where one bold ear is enough."
  - **Headline** (40): "Verdant Circlet Studs · ₹899 · 10% off 2"
  - **Description** (28): "Emerald-green cubic zirconia"
  - **URL:** `https://www.nairaflore.com/products/verdant-circlet-studs?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b02&utm_content={{ad.id}}&utm_term=b02-3_a2sel_circlet-green-gold`

---

### b02-4 · Prism Rivière Bracelet · A1 Product Card (F2 grammar, no headline) · L3 · C1

- **Concept.**
  - F2's grammar on our highest-ticket piece: a bare forearm across ink velvet, seen from directly above, with the pastel line as the only colour.
  - No headline: the card, and a wedding-guest mehendi hand.
  - This retries b01-5, which was dropped. It fixes b01-5's three failures:
    - the horizontal forearm makes the centred subject the intended placement;
    - the stone count across the wrist locks scale;
    - "never a clenched fist".
- **Borrows.** F2 (no headline, the card, the piece the only saturated thing), our anaar winner (the piece's colour is the loudest thing in a quiet frame), board 107 (constant sign-off), board 11 (body fragment serving the product).
- **Refs.**
  - Slot 1: `f9e23a88-b9d0-47ec-ae01-461a8585a1a9`, `build/refs/prism-riviere-bracelet__pack.jpg`. "The authority on this exact piece; ignore its background and light."
  - Slot 2: `8f1ff732-cbc4-47d0-aa07-6d190c0e059e`, `build/refs/prism-riviere-bracelet__detail.jpg`. "Take only the pavé halo around each cushion stone and the three pastel colours."
- **Prompt.**
  > Overhead photograph in a vertical 9:16 frame, the camera pointing straight down at 90 degrees, about 16 cm across: a woman's bare left forearm lies flat and horizontal across the middle of the frame on deep ink-blue velvet, entering from the right edge where the elbow side is cut by the frame, and running left to her hand, which rests relaxed and palm down with the fingers gently curved and their tips touching the velvet, never a clenched fist, the fingers running out of the left edge; the hand is no wider than about one and a third times the forearm. FIDELITY: on her wrist the Prism Rivière Bracelet from the reference: one continuous single line of square cushion-cut pastel cubic zirconia about 5 mm each in aqua blue, soft pink and pale yellow mixed along the line with no two neighbours the same colour, each stone framed by its own fine halo of tiny clear pavé, linked edge to edge in bright PVD rhodium silver tone, the fold-over clasp hidden under the wrist. It must stay three pastel colours, never a fourth colour such as lilac, green or white, never bare stones without halos, never gold. SCALE: about ten haloed stones fill the visible arc across the top of the wrist; each haloed stone is about one seventh of the wrist's width, never one fifth; a slim, delicate line lying flat on the skin with a fine contact shadow along both edges. SCENE: deep brown skin with visible pores and fine wrist creases; a fine traditional mehendi pattern on the back of the hand only, ending before the wrist bone, so the bracelet sits on bare skin; the velvet is plain. PLACEMENT: the forearm crosses the frame between about 40% and 58% of the frame height and the hand stays between about 37% and 61%, inside the central 4:5 window, with the bracelet at the horizontal centre; from the top of the window down to about 36% the frame is plain ink velvet, a calm area for type, and from about 62% down plain ink velvet, calm for the card. LIGHT, L3 two-colour gel rim on a dark ground: one large soft white light from directly above keeps the stones' true aqua, pink and yellow and shows the skin texture; one hard low rim light from the far side, split-gelled aqua and soft pink, draws a thin coloured edge along the top contour of the forearm and the hand only, never on the stones; the pavé sparkles as small round points. NEGATIVES: no face, no other jewellery (no rings, no bangles, no watch), no nail art, no text, no logos, no star-shaped glints, no starburst, no lens flare, no water, no droplets.
- **Acceptance.**
  - **Placement (checked first).** The forearm and bracelet within 36–61%; drop if outside 35–62%. The hand stays inside 35–62%.
  - **Colours.** Aqua blue, soft pink and pale yellow, with no two neighbours the same and no fourth colour. The gel rims do not tint the stones.
  - **Construction.** Every stone has its own pavé halo; the stones are linked edge to edge; bright silver tone, never gold.
  - **Ratio inside the piece (log it).** Haloed-stone pitch ÷ stone width = 1.4–1.7 (5 mm stone in about 7.5 mm pitch).
  - **Body ratio.** Pitch ÷ wrist width = 0.12–0.17 (true about 0.14; b01-5 failed at 0.198). 8–11 stones visible across the wrist.
  - **Hand.** Relaxed, palm down, not a fist. Correct anatomy for any fingers shown. Mehendi only on the back of the hand.
  - **Size.** The visible bracelet is ≥ 12% of the width (expected about 35%).
  - **Calm zones.** 14–34% and 63–80% plain velvet.
  - **Skin.** Deep brown with pores.
  - **Negatives.** No other jewellery.
- **Layout.**
  - **Feed.** `body.dark`, A1, no headline.
    - `.card` top 940: `logo_white`; "Prism Rivière Bracelet"; "₹2,399"; line "aqua blue, soft pink, pale yellow · silver tone"; offer.
    - `.scrim` in the velvet's ink only if the hand reaches below 880.
    - Nothing in the top band. Text share ≤ .15.
  - **Story.** Over plain velvet.
    - `logo_white` at 270–326.
    - Name 344–375.
    - Price 389–445.
    - Line 459–490.
    - Offer 506–568.
- **Copy.**
  - **Primary text** (166; offer ends at 122): "Colour in one straight line: Prism Rivière Bracelet, ₹2,399, pastel cubic zirconia in silver tone. BUY2: 10% off 2 pieces. Fits wrists of 15 to 19 cm, and waterproof."
  - **Headline** (34): "Prism Rivière · ₹2,399 · 10% off 2"
  - **Description** (23): "Pastel CZ · silver tone"
  - **URL:** `https://www.nairaflore.com/products/prism-riviere-bracelet?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b02&utm_content={{ad.id}}&utm_term=b02-4_a1_prism-wrist-card`

---

### b02-5 · Verdant Eternity Band · A5 Truth Split (listing numeral) · L7 · C5

- **Concept.**
  - The hero ring standing on a saffron (marigold) field, its open back with two looped tips visible as the proof.
  - A flat type zone in the deep shade of the ground carries the listing numeral "5–9" with "US SIZES, ONE RING."
  - This answers the first doubt about buying a ring online, its size.
- **Borrows.** Boards 11, 22 and 88 (number first), Arata 2/7/41/119 (numeral, label, footnote system), boards 22 and 57 (hard two-zone split), board 190 ("shown magnified · actual size" tag).
- **Refs.**
  - Slot 1: `702645c3-7920-48ac-afaa-5ce4d51e868a`, `build/refs/verdant-eternity-band__cube.jpg`. "The authority on this exact piece; ignore its background and light."
  - Slot 2: `2c3d1209-2571-4e63-95af-807e4650a83a`, `build/refs/verdant-eternity-band__upright.jpg`. "Take only the open back with its two looped tips and the scalloped pavé wave between the green ovals."
- **Prompt.**
  > Product still life in a vertical 9:16 frame, 100 mm macro, camera about 20 degrees above the floor: one Verdant Eternity Band stands on edge on a flat matte saffron-marigold floor that curves up into a saffron wall with no horizon line, its circle turned about 20 degrees from facing the camera so the front arc of green stones faces the lens, and the open back, two small looped tips with a narrow gap between them, shows clearly at the lower right where the band meets the floor. FIDELITY: the ring from the reference: a cool PVD rhodium silver-tone open-back band about 16.5 mm inside, carrying oval emerald-green cubic zirconia of about 5 by 4 mm, each in 4 claws, set alternately either side of one slim scalloped S-wave of tiny clear pavé that weaves between them, about seven green ovals along the visible front arc. It must stay alternating green ovals on either side of one pavé wave, never a straight row, never a full pavé halo around each oval, never round or teal stones, never gold. SCALE: each green oval is about three tenths of the ring's inner opening across, never half; the band rests on the floor with a crisp short contact shadow where it touches; honest macro depth of field. PLACEMENT: the ring stands on the vertical centre line, its top at about 38% and its base at about 59% of the frame height, spanning about 44% of the frame width, inside the central 4:5 window; above 36% the frame is empty, evenly lit saffron wall, a calm area for type, and below 62% empty saffron floor, calm for the card. LIGHT, L7: one large soft directional window light from the upper left wraps the silver tone and keeps the green deep and true; plus one small hard specular kicker from the right that gives the clear pavé small round points of light, never rays. Silver tone stays cool and bright. NEGATIVES: no hands, no people, no props, no flowers, no other jewellery, no text, no logos, no star-shaped glints, no starburst, no lens flare, no water, no droplets.
- **Acceptance.**
  - **Placement (checked first).** The ring and its shadow within 36–61%; drop if outside 35–62%.
  - **Construction.**
    - green ovals (oval, not round; emerald green, not teal), each in 4 claws;
    - set alternately either side of one scalloped pavé S-wave;
    - not a straight row, and no full halo around each oval;
    - 6–8 ovals visible on the front arc.
  - **Open back.** Visible: two small looped tips with a gap.
  - **Colour.** Cool silver tone, never gold.
  - **Ratio inside the piece (log it).** Oval length ÷ inner opening = 0.25–0.35.
  - **Width and scale.** The ring spans 40–48% of the frame width. Measure px/mm. Expected about 22 px/mm, so the size tag is required.
  - **Contact.** A true contact shadow; the ring does not float.
  - **Calm zones.** 14–34% empty wall (under the type panel); 63–80% empty floor.
  - **Negatives.** Soft round speculars only, no rays; no props.
- **Layout.**
  - **Feed type zone.** A flat panel at full width, y 0–372, in the deep shade of the ground (start #7A3E0E, sampled darker from the render's floor). It is a flat graphic on top, with nothing of the product under it. Bone type inside it:
    - `.numeral` "5–9", Jost 300, 260 px, −.02em, left 72, top 84 (about 420 px wide).
    - `.label` "US sizes,<br>one ring." Jost 500, 30 px caps, .14em, left 530, top 112.
    - `.sizetag` "Shown magnified<br>about 16.5 mm inside", 30 px, 2 px hairline, bone, left 530, top 206 (about 480 × 96).
    - `.foot` "*As listed: the open back adjusts to fit US 5 to 9. PVD rhodium, silver tone." Jost 400, 22 px, left 72, top 322.
  - **Feed card.** Photo zone from y 372: ring at 406–887. `.card` top 940 on the saffron floor in ink: `logo_ink`; "Verdant Eternity Band"; "₹1,049"; line "emerald-green cubic zirconia · silver tone"; offer with an ink hairline and coral-deep `.sep`.
  - **Feed checks.** Text elements: the numeral system, the size tag and the card (3). Text share .25–.35 (A5).
  - **Story.** A panel y 0–660 in the same deep shade:
    - `logo_white` at 270–326.
    - "5–9" Jost 300, 120 px, with "US SIZES, ONE RING." Jost 30 caps to its right at cap height, 336–438.
    - Name and price in bone, 450–506.
    - Offer 518–580.
    - Size tag on one line, "SHOWN MAGNIFIED · ABOUT 16.5 MM INSIDE", Jost 500, 26 px, hairline, 592–647.
    - The footnote is Feed-only.
- **Copy.**
  - **Primary text** (153; offer ends at 124): "US 5 to 9, one ring: Verdant Eternity Band, ₹1,049, emerald-green cubic zirconia, open back adjusts. BUY2: 10% off 2 pieces. Silver tone, and waterproof."
  - **Headline** (37): "Verdant Eternity · ₹1,049 · 10% off 2"
  - **Description** (20): "Adjustable US 5 to 9"
  - **URL:** `https://www.nairaflore.com/products/verdant-eternity-band?utm_source=meta&utm_medium=paid&utm_campaign=ads500_b02&utm_content={{ad.id}}&utm_term=b02-5_a5_verdant-us5-9`
- **Deviation noted.** A5 asks for the piece at ≥ 50% of the photo zone's width. A standing ring at 50% would be about 540 px tall and break the 36–61% subject band (481 px). The band wins: 44% width, about 22 px/mm, with the size tag declaring it.

---

## 5. Notes for the next steps

- **Generator.**
  - One `generate_image_batch` call: `nano_banana_pro`, 2K, 9:16, one image per slot, refs as listed (slot 1 first).
  - Read the balance immediately before the call and apply the cut order in §0.
  - Log `submitted_at`, `credits` and `served_model` per job from `transactions`.
  - On a 429, resubmit only the failed item, after the first job completes.
  - One regeneration at most per slot, with the fix written into the prompt.
- **Verifier.**
  - First, measure each subject's extent and drop anything outside 35–62%.
  - Then log the one ratio inside each piece named in its acceptance, the body ratio for worn frames, the px/mm on the 1080 Feed, and the key detail's share of the width.
  - Check for any eye in b02-1 and b02-3, and for any colour outside the stud in b02-3.
- **Finisher.**
  - b02 pages use the kit classes only.
  - Sample the b02-3 green and the b02-5 panel shade from the renders.
  - Every render passes the §3 gates.
  - `copy.json` follows b01's shape with `utm_campaign=ads500_b02`.
- **Critics.**
  - Score the final JPGs (loop change 8).
  - The anchor pair for the 200 px sheet: winner `win_twenty_f2_tennis_ruby` (b02-4 tests its grammar). Loser `lose_vks5_prism_close`: b02-4 answers its pale-on-pale failure, and it differs from b01's loser.
  - Read b02-1 against b01-4 if critic A clears b01-4, else against `win_w1_woven_red_story`.
- **b02 is better than b01 only if:** it ships at least 3 of 5, at least 2 of them worn; the desire mean is above 6.75; one Brushed ad ships; and at least one ad beats the winner anchor with both critics.
