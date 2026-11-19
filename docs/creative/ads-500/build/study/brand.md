## Naira Petite: brand codes, production pipeline and lessons learned (read-only study, 19 Nov 2026)

Nothing was written to the repo, Shopify, Meta or Higgsfield. I made test renders in `/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad/branddesign/`:
- `logos.jpg`, `deck.jpg` and `sample1.jpg`: the logo, the deck florals and a sheet of ten finished ads.
- `vtest.jpg` and `lig.jpg`: glyph and ligature tests.

### Short version

1. **Logo.** The logo is the word NAIRA (it never says "Petite") with a tulip as the stem of the I. It comes in four PNGs.
2. **Type.** Headlines are Velista capitals, corrections are Cormorant italic, and spec lines and prices are tracked Jost capitals.
3. **Palette.** Ink #1A1614 on paper #FBF8F3, with sage #99B4AE, blush #FFF8F5 and coral as accents.
4. **Formula.** One piece at true size next to one Indian object that repeats its colour or shape. The headline turns that object into a joke, and a lowercase italic correction states the product truth. Two examples: "Almost edible." / *cubic zirconia, not candy.*, and "Paperclip, promoted."
5. **Kit.** The new kit in `docs/creative/ads-500/kit/` is the only renderer that runs today. The older builders read fonts and plates from scratchpad folders that no longer exist.
6. **Biggest recurring failures:** the model draws pieces 1.5–2.6× too large, type sits on top of the jewellery, props the owner rejected (pantry food, puns, things that read as a face or body), and product names that contradict their listings. A finding from today: **none of the kit fonts has the ₹ sign.**

---

## 1. Brand codes as practised

### Logo
- **Files.** Four PNGs, each 1200×268 RGBA (4.48:1): `logo_ink.png`, `logo_white.png`, `logo_sage.png`, `logo_sage_dark.png`.
  - Byte-identical copies are in `docs/creative/finished-ads/brand/`, `docs/creative/ads-500/kit/` and `docs/creative/three-camps/brand-deck/` (that last folder has no ink version).
- **Design.** NAIRA in a high-contrast display serif. The I's stem is a tulip on a stalk with two leaves (the brand bible's "petal displacing part of the I"). Colours sampled from the files:
  - ink: about #181010;
  - sage: letters about #99B4AE, tulip peach about #F8B8A8;
  - sage_dark: letters about #7A9A92, tulip in the same peach;
  - white: all white.
- **Colour rule as practised:** ink on light photos, white on dark photos. Sage only reads about 2:1 on photos (comment in `build_ads.py`), so it is optional. The brand deck uses white on sage, sage on blush, or black.
- **Placement by layout:**

| Layout | Logo placement |
|---|---|
| deck ("Almost edible.", crazy, rhyme, play) | 40 px tall, bottom-right foot, above the price, with its own height of clear space (`wmpos: top` is the alternative) |
| quiet (Apricot camp) | centred at the top, 44 px tall; 70 px from the top on Feed, 300 px on Story |
| colour and crazy3 (least graphics) | 30 px tall at (76, 84), heading a small block in the shot's own ink. The Story has no text and no logo at all |
| note / silk ("The gold note.", layout v1) | no logo |
| ads-20 and shop-all | one logo per ad, 220–320 px wide, clear of everything |
| three-camps | top bar and foot on every card, white wordmark on sage, nairaflore.com printed on every card |

### Typefaces
- **Velista** (`ads-500/kit/fonts/Velista.ttf`, the same file as the site's `public/fonts/Velista.ttf`; Tailwind maps it as the brand serif).
  - A capitals-only display face: lowercase renders as capitals.
  - Used for headline capitals ("NEVER MELTS.", "TEA STRAINER,") and the quiet layout's product name, tracked .14em.
  - Tested today:
    - It has no ₹, no em dash and no middle dot; those fall back to another font. Its digits are stylised. Keep prices and spec lines in Jost.
    - At letter-spacing 0, Chromium draws a decorative "TS" swash ligature (MELTS turns into MEL plus a swash). The old deck used −.005em, which suppresses it. Set any non-zero tracking or `font-variant-ligatures:none`.
- **Cormorant Garamond italic.** Used for:
  - the lowercase correction line;
  - the italic headline in note, silk, colour and crazy3 ads (64 px);
  - the `h em` counterpoint at 1.12em in the deck.
- **Jost.** Tracked capitals (.2–.24em) for the spec line, price, CTA button and the coral pill tag.
- **Kit additions, never run in a Naira ad:** Bricolage Grotesque 400–800 and Anton, meant for loud poster grounds. The brand bible says Naira is "not loud", so treat these as an experiment.
- **Handwriting faces** (Kalam, Caveat, Marker): only where a lo-fi format calls for them (shop-all build rules).
- **₹ in every font.** The kit fonts, and every Jost build in the repo, lack U+20B9. Chromium falls back to the system font Inter, so every past ad's ₹ has been Inter. It matches Jost but not Cormorant italic or Anton. Fix: add a `unicode-range` @font-face for U+20B9, or keep prices in Jost.

### Palette (hex values)

| Source | Colours |
|---|---|
| Site and ad system | ink #1A1614, paper #FBF8F3 (`build_ads.py` DECK_INK/DECK_PAPER; `kit.css` --ink/--paper). Older ink #1C1C1C; quiet-layout ink #2B2622 |
| Brand bible (in the skill's references) | bone #F4F0E8, blush wash #FBEDE9, dusty rose #F2CFC4, coral #E79C82, sage #A9BCAD, metal #C9A55C→#E4C889 |
| Brand deck | sage #99B4AE, blush #FFF8F5; coral pill #F0A08F |
| Lac & Bone feed | oxblood #6E1A20, near-black #3A0F13, bone plaster #F2EDE4, warm gold #C2A05A |
| night-shift/core.py | #F1EBE1, #1B1512, #6E1E2A, #F2C4BD, #2A0D14, #9AA793, #7A6E66 |
| Per-shot ink (colour and crazy3) | a deep shade of the piece or ground, stored in the `ink` field of `colour50.json` / `crazy3.json` (e.g. #5E4423, #6A4818). Type is tone-on-tone with the photo |
| Kit "loud" grounds (new, unproven) | #B5502F, #E8A33A, #6E1F23, #4A2540, #B9C98A, #9EC3D6 |

Practice has moved past the brand bible in three ways:
- The founder loved night frames on charcoal, aubergine and black, though the bible bans black and grey grounds.
- Rangoli and diya frames won, though the bible says "one iconographic cue max".
- The ads-20 judge found one saturated colour beats beige on beige or pink on pink.

**Fixed rule: gold renders warm-neutral, never brassy or orange.**

### Tone of voice
- **Headline.** 2–5 words, sentence case, a full stop, and a turn in the meaning: "Almost edible.", "Paperclip, promoted.", "RSVP: yes.", "Never melts.", "Tum aur main."
- **Correction.** A lowercase italic "X, not Y" line that carries the product truth: "cubic zirconia, not candy.", "mirror steel, not silver varq.", "a woven mesh ring, not a tea strainer."
- **Hindi.** At most one Hindi word an urban reader needs no gloss for.
- **Spec line.** Listing facts only (size, "18k gold tone", "silver tone", "cubic zirconia").
- **CTA.** "Shop the bracelet". Stories carry no CTA, because Meta adds its own button.
- **Captions.** Follow `docs/creative/shop-all/research/caption_rules.md`:
  - 120–180 characters, hook first;
  - the exact price;
  - the offer sentence last;
  - no emoji, exclamation marks or hashtags;
  - no urgency, scarcity, ratings or counts;
  - COD "on serviceable pincodes", never "across India".
- **Banned beyond the house list:**
  - "Emerald" or other gem names as nouns (the stones are green cubic zirconia);
  - "Fan favourite" (a popularity claim nobody measured);
  - "Straight from the shell" (implies natural pearl);
  - stunning, elevate, must-have, luxury.
- **Brand bible voice:** the tagline "Softly, slowly, worn." and the vocabulary hand-finished, slow-made, atelier, edit, capsule.

### Recurring motifs
- **Colour rhyme:** one piece plus one object that repeats its colour, shape or name (anaar with ruby, paper clips with the paperclip chain, glass choodi with huggies, ghungroo with dome huggies, a kite with marquise stones).
- **Grounds:** matte lime plaster, colour-coded to the piece. Day ads are pale, night ads deep, in pairs.
- **Occasion objects:** invitation, clutch, diya, ladi, a mithai box with a zari bow, a wax-sealed letter.
- **The deck tulips:** `three-camps/brand-deck/deck_tulips_{blush,sage}.png` and `deck_leaves_{blush,sage}.png`, plus the herbarium label and coral tulip stamp.
- **Series names:** the "note" family ("The gold note.", "The aqua note.").

---

## 2. The production pipeline that exists

### a) Product truth (before any frame)
- **Gate.** `docs/creative/verification-doc.md` lists five conditions:
  - the product is ACTIVE in a live query;
  - metal comes from the Plating field, confirmed in at least two images;
  - every countable feature is counted in an image;
  - a stated mm figure exists, or the frame makes no scale claim;
  - every recorded discrepancy is either designed around, or the frame is not shot.
- **Read** (read-only) from Shopify per product: stock (20 or more, not pre-order), price and all 3–6 images.
- **References.** `docs/creative/ads-500/build/refs.json` holds 40 Higgsfield media IDs for the 18 qualifying products: packshot plus macro or detail, and each colour where colour differs.
  - `refs_src.json` maps each ID to its Shopify CDN URL or repo file.
  - Local copies and a sheet are in `<scratchpad>/refs500/` (`_sheet.jpg`).
- **Older locks** (re-verify before reuse):
  - `docs/research/04-sku-fidelity-library.md`;
  - `docs/creative/performance/build/products_g*.json`;
  - `docs/creative/ads-20/build/set*.json`.

### b) Higgsfield generation (MCP, as practised Oct–Nov)
- **Call settings.** `generate_image_batch` (up to 12 per call) with:
  - `model: "nano_banana_pro"`, `resolution: "2k"`;
  - `aspect_ratio: "9:16"` (compose for the Story; the Feed is a 4:5 crop);
  - `medias: [{"value": <id>, "role": "image_references"}]`.
- **Retrieval.** Poll `jobs_wait` at 15 s or less, then curl each result into the scratchpad.
- **Cost and safety.** 2 credits per frame. Never resubmit a job whose outcome is unknown; resolve its job ID first. The served model can differ from the requested one (nano_banana_2 or flash came back), so judge by eye.
- **Helper.** `python3 docs/creative/ads-20/build/prompts.py set4.json [key…]` prints the request JSON from a set file (per-ad shot, lock, scale and skin, plus the set's common light and negatives).
- **Reference slots.**
  - Slot 1 is the approved listing packshot, "the authority on this exact piece; ignore its background and light."
  - Slot 2 is optional and must be a detail of the same piece, with its role stated (e.g. "take only the build of the clasp").
  - Never a second product.
  - `two-slot-system.md`: a setting plate in slot 2 only if its size referent is within about 2–2.5× of the piece; the plate pulls the piece's size toward the referent.
- **Prompt order** (`docs/creative/performance/BRIEF.md`), written as one paragraph:
  1. Shot and scene.
  2. Fidelity lock, with countable facts as digits.
  3. Morph clause: "<part> must stay X, never Y".
  4. Scale test: mm plus a referent, "keeps its true small size… dominates by light and isolation, never by being enlarged", contact shadow, substrate deformation.
  5. Composition: subject between 15% and 85% of the height, copy space in the upper-left third.
  6. Light: soft window light from the upper left plus ONE hard specular kicker from the right, honest macro optics, real texture.
  7. Absence list: worn shots add "no face"; others add "no hands, no people".
- **Exemplar prompt:** the `toggle-link-chain` rhyme entry in `performance/build/shots_g1.json`, including its "Fix from the previous attempt: …" reshoot clause.
- **On-body exemplar:** the `common` block in `ads-20/build/set4.json`. It includes "no star-shaped glints, no starburst, no lens flare" and "Never enlarge the piece; it must look small and true to life on her body", and names the skin tone explicitly per ad.
- **Older Chrome-UI method** (`imagegenerationnaira` SKILL.md): it has a rehydration bug that silently restores the previous prompt and reference. Use the MCP route.

### c) Type over photo
- **The new kit** (self-contained, fonts committed). Checked today:
  - Render: `NODE_PATH=$(npm root -g) node docs/creative/ads-500/kit/render.cjs page.html out.jpg [w h] [page2.html out2.jpg 1080 1920 …]`
    - The default size is 1080×1350.
    - It waits for fonts and images, then prints `{"out", "failed": [urls], "overflow": [data-fit ids]}`.
    - Pages link `../../kit/kit.css`. Tag text boxes with `data-fit="<name>"` to get overflow reports.
  - Contact sheet: `python3 -I docs/creative/ads-500/kit/sheet.py sheet.jpg a.jpg b.jpg …` (5 across, labelled).
- **Older builders.** Use them as layout reference. They do not run as-is, because they read `<scratchpad>/c4/fonts`, `<scratchpad>/perf/...` and `<scratchpad>/ads/...`, all gone.
  - `finished-ads/build_ads.py`:
    - `html_deck()` is the "Almost edible." layout; every parameter is explained in the `note` field of `ads.json`;
    - `extend916`/`extend_mirror` turn a 4:5 frame into 9:16;
    - `glue()` keeps a number and its unit together with a non-breaking space.
  - `performance/build/perf_ads.py`: the deck, note, quiet and plain overlays. Python scores the photo on a 24 px busy/tone grid, and `PLACE_JS` in the page tries every corner and keeps the calmest.
  - `performance/build/colour_ads.py --set crazy3 NN`: the least-graphics block.
  - `performance/build/ad_copy.py`: writes `copy.json`, `meta.csv` and `plan.json`. The `meta.csv` columns are `ad,product,format,placement,variant,reserve,primary_text,headline,cta,url,campaign,adset,wave`. URLs carry `utm_source=meta&utm_medium=paid&utm_campaign=…&utm_content=…`.
  - `night-shift/core.py`: the shared set system. It renders both formats, audits copy numbers against listings and gates stock.
  - `shop-all/research/build_rules.md`: the builder contract.
- **Retouch scripts** (CRAZY3, plaster grounds only): `performance/build/retouch/shrink.py`, `replate.py` and `fakeplate.py`. They set an oversized piece back at true size in post.

### d) Review
- **Frame scoring.** 0–10, pass at 8 or above (8.5 for the colour series), with the outright-fail list in `BRIEF.md`.
  - Reshoot once, naming the fault in the new prompt.
  - A frame at 7.5 runs only as a flagged reserve; otherwise leave the slot empty and say why.
- **Scale check.** A pixel ruler against the referent or body part; reject anything above about 1.2× (ads-20).
- **Ad review.**
  - Two independent full-size reviewers (`performance/build/review_a.json` and `review_b.json`) return `fix` dicts that `ad_copy.py` applies.
  - `finished-ads/sign_review.py review_rN.json [--cfg …]` plus `reviews.py` tie each score to the exact settings that were reviewed.
- **Judges.**
  - ads-20 used one independent judge with 10 weighted criteria (`ads-20/build/scores.json`): stop .15, truth .15, craft .15, desire .10, hierarchy .10, offer .10, brand .05, series .05, platform .05, compliance .10.
  - shop-all used three judges (media buyer, creative director, fact checker), then a re-check by a reviewer who had not seen the ad, plus plain change notes (`changes.json`).
- **Owner sign-off.** Keep or Drop on a handoff page (`performance/handoff/manifest.json`, `ads.csv`, `approved.csv`; the live verdict log is the `verdicts` collection).
- **Before spend.** Turn off the Advantage+ enhancements listed in `docs/research/02-production-craft.md` §8.12.

---

## 3. Lessons already learned

### Product truth
- **Read metal from the Plating field and the photos, never the name.** A colour word in the prompt overrides the reference: "warm gold" turned rhodium Solitaire Whisper Studs gold. Never state a metal without looking at the reference.
- **Titles that lie:**
  - Solitaire Whisper Studs: a cushion pavé halo in rhodium;
  - Pearl Halo Studs: no halo;
  - Star Point Band: gold only;
  - Verdant Circlet: has a shell pearl.
- **Heartbead Bracelet:** silver-tone steel beads with a gold-tone toggle and heart.
- **Two greens:** Verdant Drop is mint turquoise; the others are emerald green. Neither is "emerald".
- **Pearl Circlet Studs are on hold:** the copy says gold, every photo shows silver.
- **Name mechanisms as separate parts:** "toggle clasp" rendered as a push clasp; "a bar through an open ring" rendered correctly.
- **Model habits to prompt against:**
  - brushed finishes come back mirror-polished;
  - steel can read gunmetal;
  - AI starburst glints;
  - orange gold;
  - colour order and stone counts drift (paper boats took 3 rounds; the kite reshoot kept the only frame with all five stones right).
- **Locks and prices from October are stale.**
  - Toggle Link Chain: the ring is about 22 mm and the bar about 15 mm (13 Nov fix; October prompts said a 15 mm ring).
  - Store prices on 13 Nov: Woven Gold Hoops ₹1,049, Brushed Gold Huggies ₹699, Toggle ₹999, Cushion Halo ₹999. `ad_copy.py` still holds the 22 Oct prices.

### Scale
- **Diffusion draws small pieces too large next to props:**
  - 1.5–2.6× in CRAZY3;
  - hoops at 30 or 34 mm against a true 25 mm;
  - a huggie at 22 mm against 15;
  - a disc at 2.1× the shirt buttons beside it.
- The first stud frame came out smaller than a cardamom pod, the inverse of the truth.
- **The Soleil Petal Pendant** came out at 32–34 mm against a true 18 mm in two tries, so it has no worn photo. That is the "generate at true size or leave out" rule in action.
- **Pick the referent to match the piece's size.** Use 2K: 41% of 400 older generations were 1K, too thin for Feed.

### Concepts the founder rejected
- **"Too basic":** the five-format set.
- **"Too weird", and why:**
  - jewellery in a shoe (shoes are impure, gold is Lakshmi);
  - kidney dish and forceps (clinical);
  - nimbu-mirchi (superstition);
  - toy tiger (childish);
  - toothbrush (bathroom);
  - a gulab jamun crease that read as a bottom.
- **Reads as a face or body:** round pairs that look like eyes, cut fruit with a cavity, two quiet frames that read as suggestive.
- **Food:** 31 of the 43 dropped colour shots were pantry or kitchen food (spices, powders, crumbs, broken sweets, jewellery sitting in food).
- **Pun-only props:** harmonium, sewing spool, skipping rope.
- **Flowers in the wrong job:** a puja garland, a gajra that swamped the necklace, a paranda that read as a hair braid.
- **A silk knot read as a necktie** (twice).
- **No real brands:** no IRCTC, Bajaj or Cadbury.

### Concepts the founder loved
- **CRAZY3 07 and 57:** the bracelet on an ivory invitation with baby's breath, and the bracelet beside an ivory satin clutch on aubergine.
- **What they share:**
  - one object from the moment the piece is worn;
  - at most one accent;
  - a tonal matte plaster ground;
  - the jewel as the only sparkle, at true size;
  - ivory, gold and one deep tone.
- **The one-second test:** every prop must answer "why is this here?" in a second. It is either where the piece is worn or given, a true look-alike of its shape, name or material, or a flower or whole fruit in the stones' colour.

### Layout defects reviewers kept catching
- **Text placement.**
  - The auto-placer climbed out of the designed foot, putting the name and price on the prop or the piece.
  - The automatic paper band washed out the hero detail.
  - Text ran across the jewellery or touched the prop.
  - The wordmark landed on the piece.
- **Line breaks.**
  - Headline breaks stranded "but" or "NOT".
  - Hyphen breaks like "GOLD- / TONE". Use `<br>` and `glue()`.
- **Legibility.**
  - Cream type on bright areas: one price was invisible.
  - Type under 26–27 px.
  - Five or six type lines; the cap is four.
  - Cream on cream or pink on pink loses the thumb-stop.
- **Copy.** "GOLD OR SILVER" written without "tone".
- **Story layout.** The subject sat inside the Story foot. Compose the Story first: piece in the upper half, all text between y 270 and 1500.

### Performance evidence on record
Main account `903466039148509`, read 22 Oct (`BRIEF.md`):
- the ruby and anaar Story with no text: 2.94× (4 sales, 5.5% outbound CTR); its ad set 2.75×;
- "The gold note.": 2.38×;
- the E2 carousel: 2.21×;
- the Apricot hoops: 1.72×;
- "Almost edible.": 1.45–1.67×, the most sales of any ad (10).

Later records:
- shop-all: "Almost edible." 6.21% CTR, rangoli 6.10%, Woven Gold Hoops 5.8–6.1%;
- Winners revived: 0.76× (7 days, around 5 Nov);
- ads-20: the new 20 averaged 7.87 against 6.60 for recent Naira ads.

These are recorded figures for deciding what to make. Re-read them before quoting, and never print them in an ad as proof.

---

## 4. Conflicts with the house rules found in the repo (need your or the owner's decision)

1. **"Freshwater"** appears in the skill's `tested-prompts.md` (Quiet Hero prompt). The Lac & Bone Prism "Submerged" shot was justified as "proof of the waterproof claim". Do not reuse either wording.
2. **The Field Spec's synthetic "customer review photos"** (`02-production-craft.md` §8.11) would be invented proof. Do not use them.
3. **Live listings still carry "Waterproof", "Tarnish Free" and "Hypoallergenic" tags** on about 96–99 products (81 of 174 live products carry Waterproof). Ads must not echo them.
   - **Owner decision:** the winners board's water and tarnish claims would be strongest as a water demonstration. Those claims are outside the house rule. Within the rule, the closest honest version is a demonstration that states only listing facts (stainless/surgical steel, PVD where the listing says so) with no water or tarnish claim.
4. **Hand-resizing in post.** CRAZY3 set oversized pieces back at true size with `shrink.py` and `replate.py` (off-body). ads-20 shrank worn pieces with a Higgsfield edit pass. The new rule bans hand edits on body photos. Whether a Higgsfield edit pass counts as "generated directly" needs a ruling.
5. **Face crops disagree.** `BRIEF.md` allows nothing above the jawline. ads-20 used crops from the lips down ("no eyes"), and S1_01 shows lips.
6. **Offer wording disagrees.**
   - `BRIEF.md` says codes BUY2/BUY3 at checkout.
   - shop-all says "applied in your bag", no codes.
   - The live "Almost edible" caption said 20/30% while checkout gave 10/20%.
   - BUY4 and NAIRA10 terms appear nowhere in the repo.
   - `ad_copy.py` says "cash on delivery across India"; the caption rules forbid "across India".

   Verify every offer against the live store before it goes on an image.