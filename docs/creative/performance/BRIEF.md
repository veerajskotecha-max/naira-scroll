# Naira Petite performance shoot: brief for every shoot worker (22 Oct 2026)

Each high-stock product gets **five different photographs**, one from each of the five formats below. Together they become
50+ Meta ads, 4:5 Feed and 9:16 Story, run as separate campaigns. The formats copy what has actually sold for Naira, not taste.

## What has sold (Meta, main account 903466039148509, read 22 Oct 2026)

| Ad | What the picture is | Result |
|---|---|---|
| E2 fruit plate · Ruby Baguette bracelet · Story 9:16 | ruby tennis bracelet beside a cut pomegranate whose arils are the same red; **no text on the image** | 2.94× ROAS, 4 sales on ₹2,671, 5.5% outbound CTR (ad set 2.75×) |
| Crazy · "The gold note." · Feed 4:5 | Heartbead bracelet alone on draped blush-peach silk, warm light, italic headline bottom-right | 2.38×, 3 sales |
| Catalogue E2 carousel | on-model + product shots of 31 pieces | 2.21×, 5 sales |
| Static · Apricot quiet · Woven Gold Hoops | hoops on a halved apricot over peach linen, centred, NAIRA logo top, name + price bottom | 1.72×, 5 sales |
| "Almost edible." · Prism Rivière (lifetime best seller, 10 sales) | the pastel bracelet in a bowl of sugar-dusted gummy sweets the same colours as its stones | 1.45–1.67× |
| "THE WIDTH." / "Rolling for miles" / "Rangoli, in a line" | witty object-play: calliper, a hoop rolling a track into clay, pigment powders | top outbound CTR in the account |

The common thread: **one piece, shown true to size and sharp, next to one familiar (often Indian, often edible) thing that
repeats its colour or shape, so the eye looks twice.** Plain packshots and type-only ideas did not sell.

## The five formats (one photograph each, per product)

1. **RHYME.** This is the fruit-plate and "Almost edible" winner. The piece lies beside one everyday Indian food, sweet,
   spice or object whose colour or shape repeats the piece. Examples: pomegranate arils for ruby, cardamom for emerald,
   mishri for clear stones, sugar-coated pastel saunf or gummy sweets for the Prism, jalebi for a coil, gold-varq mithai for
   polished gold, motichoor for granules, mogra buds for pearls, ice in nimbu pani for crystal. The surface is pale lime
   plaster, linen, a brass katori or a steel thali. The prop must be real food or object, never jewellery-shaped.
   **No reuse:** do not repeat a pairing already run (pomegranate–ruby bracelet, cardamom–emerald bracelet, mishri–crystal
   bracelet, gummy sweets–Prism, mogra–flower studs, nimbu pani–mint drops, churi–tubogas, rain–droplet cuff, diya–Prism,
   saree stack–Prism, rangoli pigment–Prism).
2. **SILK.** This is "The gold note". The piece alone on softly draped silk or satin in a warm, skin-adjacent colour: blush,
   peach, champagne, rose-beige, or a deep colour if the metal is silver. Long soft folds, one hard specular kicker on the
   metal, and generous calm space in the lower right or upper left for an italic headline.
3. **WORN.** This is the on-model catalogue winner. An editorial close crop on Indian skin, the piece worn exactly as
   designed:
   - earrings: ear and jaw edge;
   - necklace: collarbone and neckline;
   - bracelet: wrist and forearm;
   - ring: hand, relaxed.

   Light is warm and natural, with real skin texture (pores, fine hair) and simple clothing: an ivory shirt, a mulmul kurta
   or a bare shoulder. Vary the skin tone across products (wheatish, dusky, deep, fair-olive). **No face:** no eyes,
   brows, nose, lips or mouth, even at the edge. The crop stops at the jawline or below. Hands have five natural fingers.
   No other jewellery on the body.
4. **QUIET.** This is the Apricot camp. The piece sits on one halved fruit or a single flower whose colour matches the
   piece or the brand camp (apricot, sage and lilac), over a same-colour linen ground. It is centred and symmetrical.
   Calm empty space top and bottom (about 20% each) for the logo above, and the name and price below.
5. **PLAY.** This is "THE WIDTH" or "Rolling for miles". One witty piece of object-play that proves a true fact about the
   piece: its size (a brass calliper or a steel ruler), how it closes (a brass kundi door latch for a toggle), its finish
   (a mirror), its flexibility (draped over a pencil), or its colour line (pigment, thread spools, bangles). It must stay
   physically plausible.

## Composition (every frame)

- **9:16 vertical, generated at 2K**, so each frame serves both a Story and, cropped, a 4:5 Feed post.
- Keep the jewellery and its key prop **inside the middle 70% of the height**. Nothing important goes in the top 15% or the
  bottom 15%: Stories hide those bands under the interface, and the Feed crop removes them.
- Leave one calm copy space inside that middle band, upper-left third by default (QUIET: top and bottom instead).
- One product per frame (Law 1). **Exception:** the Marquise Layering Set and other sets show all of their own parts.
  Earrings show as a pair, except in WORN, where one ear is fine.
- No text, letters, logos, price tags, borders or watermarks in the frame.

## Prompt construction (one flowing paragraph per frame)

Use the house order, proven across Edition One and Edition Two (see `docs/creative/finished-ads/e2_frames.py`):

1. **Shot type and scene.** One or two sentences: what photograph this is, the surface, the prop and where everything sits.
2. **Fidelity lock** (it comes before any styling). "IMAGE 1 is our approved product photograph and the authority on this
   exact piece: its construction, size, metal colour and stone colour; ignore its background and light." If you add a
   second reference for construction detail, say what to take from it. Then the countable facts, as digits.
3. **The morph clause.** "<the part that will morph> must stay <what it is>, never <what AI turns it into>."
4. **Scale test.** The size in mm with a body-part or referent equivalent, plus "The jewellery keeps its true small size
   against the referent; it dominates by light and isolation, never by being enlarged." Add contact shadow and substrate
   deformation where it fits.
5. **Composition.** The 9:16 safe band and the copy space.
6. **Light.** "Soft large window light from the upper left, one soft natural shadow, plus ONE small hard specular kicker
   from the right, so the metal shows a crisp bright edge and a dark rolled edge on every curve and every stone carries
   internal sparkle and one pure-white catchlight." Add honest macro optics and real texture.
7. **Absence list.** "No text, no letters, no logo, no watermark, no price tag. No second piece of jewellery. No border,
   no vignette."
   - WORN adds: "No face: nothing above the jawline; no eyes, nose, lips."
   - Non-WORN adds: "No hands, no people."

Product truth in prompts: the metal is **gold tone** or **silver tone** (rhodium), and the stones are **cubic zirconia**. Never
write "real gold", "diamond" or "waterproof". Read the metal from the reference photograph, never from the product name.

## Higgsfield mechanics (MCP)

- Model `nano_banana_pro`, `resolution: "2k"`, `aspect_ratio: "9:16"`.
- References go in `medias` as `{"value": <media_id>, "role": "image_references"}`. Slot 1 is the product, and you may
  add an optional slot 2 for a construction detail. Never more than one product.
- Submit with `generate_image_batch` (up to 12 per call), then poll `jobs_wait` (≤ 15 s per call; repeat). Download each
  result URL with curl into your work folder.
- The cost is 2 credits per frame. **Your cap is 100 credits** (35 first-pass frames plus up to 15 reshoots). Never retry a
  submission whose outcome is unknown; resolve the job ID first.
- References come from:
  - Edition Two listing SKUs: `<scratchpad>/listing/skus.json` (lock, neg, scale per key) and `<scratchpad>/listing/ref_ids.json`
    (Higgsfield media IDs), plus `<scratchpad>/listing/approved.json`;
  - Edition One: `docs/creative/edition-one/build/skus.json`, `media_ids.json` and `refs/<key>/`;
  - `docs/research/04-sku-fidelity-library.md`: locks for 45 older SKUs;
  - `docs/creative/toggle-link/build/` for the Toggle Link Chain;
  - the live Shopify listing images, which you can query read-only and import with `media_import_url`.

  **Look at the reference image before writing the lock.** The metal and stone colours come from the picture.
  `<scratchpad>` = `/tmp/claude-0/-home-user-naira-scroll/81f6e48f-a340-5398-99b2-f7e22fb69d37/scratchpad`.

## Verification (look at every frame at full size, then at phone size)

Score each frame 0–10 and **pass at 8 or above**. A frame fails outright if it shows any of these:
- the product misrepresented: the wrong construction, link type or stone count, colour order or cut, the wrong metal
  colour, extra stones, or detail melted at phone size;
- wrong scale: costume-sized against the body or referent;
- a second piece of jewellery;
- any face part, or broken hands or fingers;
- text, logos or watermarks;
- the key subject outside the middle 70% band;
- an implausible prop.

Reshoot a failed slot once, with the fault named in the new prompt ("…the links must stay paperclip links; the previous
attempt drew cable links"). If the reshoot also fails, take the better attempt only if it scores at least 7.5 and flag it.
Otherwise leave the slot empty and say why.

## Output contract

- Final passed frames: `docs/creative/performance/plates/<key>-<format>.jpg`, resized to **1080×1920**, JPEG quality 90.
  `<key>` is the product handle; `<format>` is one of rhyme, silk, worn, quiet, play.
- Keep the full-size originals in `<scratchpad>/perf/<group>/`.
- Manifest: `docs/creative/performance/build/shots_<group>.json`, a list with one entry per frame (passed or not):

  ```json
  {"key": "<handle>", "title": "...", "format": "rhyme", "file": "plates/<key>-rhyme.jpg" | null,
   "job_id": "...", "attempts": 1, "score": 8.5, "pass": true,
   "notes": "what is in the frame; any doubt",
   "prop": "pomegranate", "copy_space": "tl" | "tr" | "bl" | "br" | "top+bottom",
   "tone": "light" | "dark", "subject_y": [0.38, 0.72],
   "prompt": "<the exact prompt>", "refs": ["<media_id>", ...]}
  ```

  `subject_y` is the fraction of the 9:16 height the jewellery occupies.
- Products: `docs/creative/performance/build/products_<group>.json`, one entry per product with the title, handle, live
  price, stock, metal, lock and neg (as used), the reference media IDs, and the local reference path.
- Do not touch Shopify or Meta (read-only queries only). Do not commit; the lead commits.
