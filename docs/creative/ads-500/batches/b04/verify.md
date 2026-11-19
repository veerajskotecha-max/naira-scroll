# b04 picture verification (19 Nov 2026, one picture at a time)

Each picture is checked against `brief.md` (the slot's acceptance list), `RULINGS.md` §4 (the sliding-window gate),
`build/study/products.md` and the reference photos in `build/refs/<handle>__*.jpg`. Zoomed crops are in `tmp/`.

**Coordinates.** The source is 1536 × 2752, displayed at 1080 × 1935.
- Feed y = src_y × 0.703125 − T, with T = 5.85 × P. Story y = src_y × 0.703125 − 7.5. x = src_x × 0.703125.

---

## b04-1

**Toggle Link Chain · A2 Worn Editorial (neck-and-collarbone crop) · try 1 · verdict: dropped (failure: scale; the face gate also fails on the chin). Both faults can be fixed. This is not a morph.**

- **Job:** `bc1892af-bf58-48d4-a3e9-3168bb185d1b`, submitted 21:03 UTC.
  - Requested `nano_banana_pro` at 2k and 9:16, with refs clasp then cube as `image_references`. It was served as `nano_banana_2`.
  - Output 1536 × 2752, saved to `pics/b04-1.png`.
  - Cost 2 credits: the balance read 14.46 before and 12.46 after.
- **Zooms:**
  - `tmp/b04-1_full.jpg`, `b04-1_top.jpg`, `b04-1_topleft.jpg`
  - `b04-1_clasp.jpg`, `b04-1_clasp_grid.jpg`, `b04-1_bar_vs_ref.jpg`
  - `b04-1_linksL.jpg`, `b04-1_link_grid.jpg`, `b04-1_throat_grid.jpg`, `b04-1_goldmask.png`
  - `b04-1_feed_P66_boxes.jpg`, `b04-1_story_boxes.jpg`, `b04-1_boxes_sheet.jpg`
  - `b04-1_gate200.png` and `b04-1_gate200_x2.png` (the 200 px gate)

### Measurements (src px unless marked)

- **Faces first: FAIL (fixable).**
  - The underside of the **chin and jaw** fills the top band: src y 0 to about 250 at the centre, and the jawline reaches about 130–180 at the sides.
  - That is Story y −7.5 to about 168: above the logo, under the platform header, but inside the native 9:16 frame.
  - No eye, nose, lips or mouth anywhere in the frame.
  - Every Feed window with P ≥ 31 (T ≥ 180) leaves it out, including the whole valid P range below.
  - A small dark strip of hair shows behind the neck at the top left (x 190–270, y 40–280). It is in the Story only.
  - The prompt's "top edge just below the jaw", taken front-on, drew the jaw's underside.
- **Clasp: PASS. It is a near-exact copy of reference 1.**
  - One thick round spring-gate sailor ring. The slimmer gate wire runs across the top between the two end caps. The collar seam and the push-pin nub are at the right, and a cylindrical bail at the top right carries the chain.
  - One straight bar, threaded on a small jump ring at its upper-left end, lies across the upper left of the ring with its stones to the camera.
  - The pavé of tiny clear stones reads 2–3 across. The ref shows about 2 staggered rows, so this matches the ref, not the lock's "single row".
  - No donut, no lobster clasp, no pendant, no other stones.
  - Sizes:
    - Ring outer: 242 wide (x 657–899) × 236 tall (y 1486–1722), wall about 48.
    - Bar: about 144 long × 18 wide.
  - **Bar ÷ ring 0.59–0.61** (0.6–0.7 asked). The clasp ref itself measures **0.58** (240 ÷ 412), so the render follows the ref.
- **Links: PASS.**
  - Open, elongated paperclip links, alternating face-on and edge-on as in the cube ref.
  - One link is about 139 × 47 (aspect 3.0).
  - Ring ÷ link width is 5.1 (true 5.5). Pitch is about 109.
  - About 8–9 links show on each side.
- **Scale: FAIL (fixable).**
  - The narrowest neck width is **975** (x 280–1255 at y 350–600). The neck is 63% of the width, against the 75% asked.
  - **Ring ÷ neck = 242 ÷ 975 = 0.248** (0.244–0.252 allowing for edge error). The band is 0.17–0.22 and the drop line is 0.24.
  - Cross-checks:
    - The ring is about 1.1× the width of the throat hollow (about 220).
    - The chain hangs short. The clasp centre (y 1604) is 404 px, or 1.67 ring widths (about 37 mm at the ring's scale), below the notch (about y 1200). A 50 cm chain hangs about 60–80 mm below.
    - The strands show 8–9 links a side, where a 50 cm chain shows about 12–13.
  - **Read:** the piece is about 1.2–1.25× on the body, and the chain looks about 42–45 cm.
  - The ring's own proportions are true: ring ÷ link width 5.1 and ring ÷ two link lengths 0.87. So **the whole piece is large against the body**; the ring is not large against the chain.
- **Width share: PASS.**
  - Ring 242 ÷ 1536 = **15.8%** of the Feed width (13–18% asked). The shareLine expected 15.2% at 1.0×.
  - 11.0 src px/mm = **7.7 Feed px/mm**, so no size tag.
- **ΔE76, ring vs the skin behind it: borderline, logged both ways.**
  - Skin inside the ring and below it: Lab 63–65 / 16.5 / 24.5–25.
  - **By mean colour:** the ring is Lab 52 / 11 / 27, which gives **ΔE 13–14**. The mean falls close to the skin because the polished tube averages its dark reflections and white highlights.
  - **Per pixel:** the median is **33.5**, and 72% of ring pixels are at 25 or more.
    - Dark reflections L 24: ΔE 41.
    - Highlights L 95: ΔE 36.
    - Mid gold L 44: ΔE 23.
    - The L 55–75 band (10% of the ring): ΔE 10.
  - The ring reads by value, not by hue. The light-tan chest is what narrows the gap.
- **Gold tone: PASS.** Ring hue 67°, chroma 29 (ref 76°, 26). It is warm and a touch yellower than the ref, never orange or brassy.
- **Skin: texture PASS, depth a note.**
  - Real pores, fine vellus texture, soft creases and a slight sheen. Not waxy.
  - The neck in shade is deep (Lab 37 / 19 / 26). The chest is **medium tan** (Lab 58–65 / 17–19 / 25–28), lighter than the "deep warm brown" asked. That also lowers the ΔE and the card's contrast.
- **Zari-edged silk neckline: PASS.**
  - A narrow, muted gold-tone zari band sits on a scooped plum silk neckline (Lab 18 / 25 / −3).
  - The band runs from src y about 2043 at the edges to 2410–2432 at the centre. In the Feed that is 1436 − T at the edges and 1701.6 − T at the centre.
  - Skin is bare between the clasp and the neckline.
- **Ground: PASS.** Dark plum beside the neck (Lab 10 / 13 / 0), nothing else.
- **Placement gate (RULINGS §4): PASS for A2 (the headline layout). No A1 fallback is needed.**
  - **Clasp extent:** from the jump-ring top to the ring's bottom contact shadow, src y 1455–1734, which is display 1023.0–1219.2. It fits inside Feed 380–930 for T 289.2–643, which is **P 49.4–100**.
  - **Chain vs headline:**
    - The H1 and beat span display x 269–811 (src 383–1153). The chain's highest point inside that span is the right strand at about src y 1150, which is display 808.6.
    - The beat ends at 296, so 296 + 24 needs T ≤ 488.6 (**P ≤ 83.5**). The H1 alone (230 + 24) would allow T ≤ 554.6.
    - Outside that span the strands rise to y about 611 (right, x about 1300–1380) and about 680 (left, x about 190–230). Both sit at display x under 176 or over 914.
  - **Zari centre inside the 1350 window:** T ≥ 352. To show the whole curve, T ≥ 365 (**P ≥ 62.4**).
  - **Valid P 62.4–83.5. Use P 66, T 386.1.**
    - Clasp at Feed **637–833**.
    - The chain's highest point in the text span is at 422.5, which is 102 px below the 320 limit.
    - The zari centre is at Feed 1315.5, below the card's end at about 1252. The zari sides are at about 1050, beside the card's outer corners.
    - The Feed top is src 549, so the chin is out.
- **Calm zones, Feed (P 66):**
  - **Headline zone, Feed 84–330, x 190–890.** Neck skin (Lab 37 / 19 / 26, RGB about 127 / 75 / 46); bone on it is **6.3:1**. The strands sit at x 134–176 and 914–967 in this band.
  - **Card zone, Feed 940–1252, x 177–903.** Chest skin (Lab 58 / 19 / 28, RGB 186 / 126 / 91); bone on it is only **2.95:1**.
    - The brief's radial scrim in sampled deep skin (about RGB 96 / 58 / 38) behind the card is **required** to reach 4.5:1.
    - The zari and silk come in only at the card's outer corners, so no foot scrim is needed.
- **Calm zones, Story (native frame):**
  - Text sits over neck skin between the strands: logo 270–326, H1 346–470, name and price 490–546, offer 564–626.
  - The offer box spans x 177–903. At the box's height the strands are at x 131–162 and 921–971, so the side gap is only **15–18 px**.
  - The chain's highest point inside the offer's x span is at src y about 995, which is Story **692**: 66 px below the box. Pass.
  - The ring is at Story 1037–1212, inside the text band, but no text is planned there.
  - The chin shows at Story 0–168.
- **200 px gate: PASS.** On both the Feed and the Story thumbnails, the gold V and the ring land first; the ring is the brightest, highest-contrast shape. The chin reads at the top of the Story thumbnail.
- **Light rendered:** an L7-like soft warm key from the upper left and front. The kicker shows as crisp specular lines on the ring's top and right and as small points on the pavé. No rays, no star glints.
- **Negatives: PASS.** No text, logos, flare, water, hands or other jewellery. The only stray is the hair strip at the top left (Story only).

### Verdict

**Dropped. Failure: scale** (ring ÷ neck 0.248, past the 0.24 drop line). The face gate also fails on the chin underside, in the Story only.

- Both faults can be fixed, so the slot gets its **one regeneration**, with the corrected prompt below.
- **The clasp held construction**: sailor ring, gate, nub, bail, and a pavé bar at 0.59–0.61 against the ref's 0.58. Under the brief's skip rule, **b04-5 is unlocked**.
- **Lead's call:** try 1 is the closest worn Toggle so far. Both faults are marginal: 1.03× past the drop line, and the chin sits only in Story 0–168, outside every valid Feed window.
- When the regeneration lands, keep this file as `pics/b04-1_try1.png`.

**Corrected prompt (try 2).** Four changes, each a crop, ratio, count or tone clause:
1. **Chin:** the brief's crop fix, word for word: "a crop that starts at the middle of the neck: the jaw and everything above it are outside the picture". "No jaw" is added to the negatives.
2. **Scale (ratio and count clauses), replacing "the ring is about one fifth as wide as the neck, never a third":**
   - The brief's internal clause, as "two links laid end to end". It is already about true (0.87), so it locks the ring to the chain.
   - Clauses that tie the piece to the body:
     - "the neck is about five ring-widths wide, never four, never three"
     - "the ring is narrower than the hollow between the two collarbone heads"
     - "each side shows about twelve paperclip links between the side of the neck and the clasp, never eight"
     - "the clasp hangs about three ring-widths below the hollow of the throat"
   - I do **not** use the brief's "sits inside the hollow". A 50 cm chain cannot rest in the throat notch, and that would contradict the concept's breastbone placement.
3. **Skin depth:** "the chest is the same deep tone as the neck, never lightened". This also raises the ΔE and the card's contrast.
4. Nothing else changes: the concept, refs, fidelity lock, pose, scene, light and other negatives stay as they are.

> Vertical 9:16 photograph, 85 mm lens at collarbone height, front-on: a crop that starts at the middle of the neck: the jaw and everything above it are outside the picture, so the top edge cuts straight across the middle of the neck and there is no jaw, chin, mouth, lips, nose or eyes anywhere in the picture; the shoulders are square to the camera, the head is level, never tilted back, and the hair is pulled back out of the frame. They wear the Toggle Link Chain from the references with the toggle turned to the front: the chain lies around the base of the neck and falls in a soft V onto the upper chest to the clasp, which rests flat on the breastbone below the hollow of the throat, centred in the frame. The clasp is posed exactly as in reference 1: the bar lies across the upper left of the ring with its row of tiny stones facing the camera, the ring hangs below it, and the spring gate with its small push-pin nub sits at the right. Reference 1 is a much closer view than this picture: copy its construction and pose, never its framing or its size. Take the links from reference 2. FIDELITY: A 50cm chain of open elongated paperclip links 4mm wide in polished 18k PVD gold tone, closed by one thick round spring-gate sailor ring about 22mm across (slimmer gate wire, small push-pin nub) with one short straight bar about 15mm long (about 0.6-0.7x the ring) set with a single row of tiny clear cubic zirconia threaded through it; no other stones, no pendant, never cable or curb links, never a lobster clasp. The clasp must match reference 1: a spring-gate sailor ring about 22 mm across and a bar about 0.6 to 0.7 times the ring's width with one row of tiny cubic zirconia; the ring must stay a thick round sailor ring with its gate and nub, never a plain donut, never a lobster clasp, and the bar must stay shorter than the ring, never as long. SCALE, the most important instruction: the necklace is small and fine against the body. The ring is about as wide as two of the paperclip links laid end to end, and each link is about a fifth as wide as the ring; the neck is about five ring-widths wide, never four, never three; the ring is narrower than the hollow between the two collarbone heads; the chain is long: each side shows about twelve paperclip links between the side of the neck and the clasp, never eight, and the clasp hangs about three ring-widths below the hollow of the throat. The neck fills about three quarters of the frame's width and the collarbones run out to both side edges. Everything is true to life size against the neck and collarbones; honest 85 mm depth of field with the clasp and the skin around it tack sharp. SCENE: deep warm brown skin with visible pores, fine natural texture and a soft natural sheen, real and unretouched; the chest is the same deep tone as the neck, never lightened; the collarbones and the hollow of the throat read clearly. The scooped neckline of a deep plum raw-silk blouse, edged with a narrow band of muted gold-tone zari, runs across the lower part of the frame well below the clasp, with bare skin between the clasp and the neckline. Beside the neck on both sides, a plain dark plum seamless background, nothing else. LIGHT: one large soft warm key light from the upper left wraps the neck and collarbones and models the skin gently; plus one small hard kicker from the right at the height of the clasp draws a crisp bright line along the curve of the ring and the bar and makes the tiny stones throw small sharp points of light, never rays. The gold tone stays warm-neutral, never orange or brassy; the skin keeps its depth and is never lightened. NEGATIVES: no text, no logos, no star-shaped glints, no starburst, no lens flare, no other jewellery (no earrings, rings, bangles, second chain or pendant), no water, droplets or wet skin, no eyes, no nose, no lips, no mouth, no chin, no jaw, no hands, no hair on the chest.

**Regeneration acceptance additions (same list as above):**
- Log ring ÷ neck, links per side, the clasp's drop below the notch in ring widths, and the chest skin's L*.
- If the chain drops lower, re-check that the zari stays below the clasp and inside the Feed window.

**Prompting learning.**
- Front-on, "the top edge just below the jaw" still draws the underside of the chin and jaw.
- "The ring is one fifth of the neck" came out as a quarter, with the chain hanging short. Lock worn chain scale with link counts and ring widths against body landmarks, not with a fraction of the neck.
- "Posed exactly as in reference 1", plus "copy its construction, never its framing", reproduced the clasp almost exactly.

Balance after verification: **12.46** credits (read at about 21:13 UTC).
