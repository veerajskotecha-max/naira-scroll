# Aditya, 26 Nov 2026: seven new pieces as Shopify drafts

The owner sent eight supplier photos (IMG_8016 to IMG_8029) of pieces on Aditya's black velvet card, or for the ring on a finger,
each with its price written on it, and asked to list them the way the earlier Aditya pieces were listed: 3.5 × pricing, sizes checked
against the finger and the card, photos, size guides, and Shopify drafts. IMG_8029 is the #57-60-63-58 photo again (the same
piece as IMG_8016), so there are seven pieces.

| Key | Supplier code | Product | SKU | Type | Cost (supplier) | Price (3.5×) | Units | Measured |
|---|---|---|---|---|---|---|---|---|
| K01 | #8 | Lumière Oval Solitaire Pendant | ADT30 | Necklace | ₹275 | ₹963 | 10 | stone 11 × 9 mm set east to west; pendant 17 mm with the bail; rope chain 2 mm |
| K02 | #106-107 | Marquise Solitaire Studs | ADT31 | Earrings | ₹200 | ₹700 | 10 | 13 × 7 mm |
| K03 | #108-109 | Petite Pear Solitaire Studs | ADT32 | Earrings | ₹170 | ₹595 | 10 | 8 × 6 mm (7.6 × 5.7 measured) |
| K04 | #57-60-63-58 | Pear Baguette Duet Studs | ADT33 | Earrings | ₹270 | ₹945 | 10 | 12 × 12 mm; pear 10 × 6.5 mm; baguette 9 × 4.5 mm |
| K05 | #169-170 | Heart Solitaire Drop Studs | ADT34 | Earrings | ₹220 | ₹770 | 10 | 17.5 mm long; heart 7.5 mm; round stone 6 mm |
| K06 | (none; "Adjustable") | Petite Pear Solitaire Ring | ADT35 | Ring | ₹190 | ₹665 | 10 | pear 9 × 6 mm; band 1.5 mm; adjustable, US 5 to 9 |
| K07 | #121-124-125 | Lumière Oval Solitaire Studs | ADT36 | Earrings | ₹200 | ₹700 | 10 | 9 × 7 mm upright |

- **Price** is 3.5 × the price written on each photo, rounded half up (₹275 × 3.5 = ₹962.50 → ₹963). **Cost per item** is the
  supplier price. No compare-at price is set (the 27 Oct Aditya listings went up without one; most live Aditya pieces have since
  had one added, mostly at price ÷ 0.7). That is the owner's call.
- **SKUs** continue the Aditya series after ADT29 (no ADT30+ existed in Shopify on 26 Nov). **Handles** were checked free.
- **Names and sets.** The oval pendant and the oval studs join the live Lumière Oval Solitaire Ring as the Lumière oval line; the
  pear studs and the pear ring join the live Petite Pear Solitaire Necklace. The storefront reads sets from product names.

## Sizes: how they were measured

- **Card scale.** Every velvet card is the same card as the 27 Oct Lotus Pear Drop Studs photo (`../aditya-jewellery/refs/J20_full.jpg`),
  taken as 80 mm across, as in `../aditya-jewellery/README.md` (25 Oct size check; the bracelet wrapped round it gave about
  80 mm). In these screenshots the card is 959 to 984 px wide (12.0 to 12.3 px per mm); in IMG_8026 (K07), a screenshot inside a
  phone frame, it is about 905 px (11.3 px per mm).
- **Finger check.** The thumb at the card's top corner is partly hidden behind the card in all four card photos, so its visible
  depth (100 to 116 px, 8 to 10 mm) is a lower bound. It rules out the 52 mm card reading raised on 25 Oct: at 52 mm the
  thumb would be about 6 mm deep. The ring is measured against the middle finger it is worn on (about 18 mm across where the
  band wraps it, about 13.8 px per mm): the pear is about 122 by 80 px, so about 9 × 6 mm.
- Pixel extents of every piece are in this README's table; the grids used are reproducible from `refs/K0n_src.png`.

## Photos

**The owner's rules (26 Nov):** four photos per listing, like the other Aditya listings: the packshot on the cream plaster
cube (H), worn (W1), worn close (W2) and one zoomed macro (M), then the size chart last. No palm photo. Nothing placed or
resized by hand in a photo (no composites, pinches or cut-and-paste): a frame whose size is wrong is regenerated. A 10/10
finish that does not look AI.

The prompt builder is `build/build.py` (a copy of `../stock-2nov/build/build.py`, GPT Image 2.6 at quality medium, faithful in the
20 Nov bake-off). Its scale, light and finish blocks follow the Naira image skill (`imagegenerationnaira`, `references/tested-prompts.md`):
one product per picture; two lights, one large soft and one small hard specular so the metal reads as metal; CRITICAL SCALE in mm
with a body-part equivalent; a contact shadow; honest shallow depth of field; fine film grain, real texture and believable
imperfection; no plastic skin, no CGI gloss, no drawn sparkle stars; warm-neutral gold, never brassy; cream grounds, never sand
or beige. IMAGE 1 is a crop of the supplier photo (`refs/K0n_full.jpg`), IMAGE 2 a close crop (`refs/K0n_det.jpg`) or, for worn
and macro frames, the approved packshot; IMAGE 3 is the house plate (the cube, or the model), so every listing looks like the
others. Specs are `build/skus.json`.

- **Approved packshots:** K01, K03, K04 and K05, each checked against the supplier photo (K05 by an independent checker,
  `build/verify/K05_H.md`). K02's packshot has a small drawn sparkle star on one stone tip (an AI tell) and is to be reshot.
- **Higgsfield stopped generating** after five pictures on 26 Nov: "You've reached the daily generation limit for your grace
  period. Try again after the limit resets or update your plan to continue generating." The balance is 73.96 credits, and
  GPT Image 2.6 costs 1.75 credits a picture in the grace period (1 on 20 Nov). Still to shoot: 48 frames (K02 H again;
  K01 to K05 W1, W2, M; K06 to K13 H, W1, W2, M), about 84 credits at 1.75, more than the balance, and about ten days at five a
  day. Renewing the Higgsfield plan lifts the cap.

## Shopify

Created as DRAFTS in one mutation (`build/ship_26nov.py` → `shopify/ship_26nov.graphql` and `.json`): vendor Naira Petite,
product type, taxonomy category, tags (type, Demi Fine, Naira Petite, Aditya, 18k Gold Tone Plated, Cubic Zirconia, and Adjustable
for the ring), the house description (intro, STYLING TIP, Details, size guide, plain Care line, box line), SEO title and
description, the Google and Facebook category metafields, tracked inventory with 10 units each (the owner: "All we got 10 each") at Forest Colony Parijat Nagar and
inventory policy DENY, price and cost per item, and the gallery so far. autoPublish was set on for the six sales channels around
the creates and set back off (all six were off before), so each piece is on every channel when the owner sets it Active.

Copy follows the 27 Oct Aditya listings: no PVD, anti-tarnish, waterproof or hypoallergenic lines. Most older Aditya listings
carry the owner's two PVD lines ("Plating: PVD 18K gold coating, anti-tarnish" and the PVD-vs-plating line); they are left off
here until the owner confirms these seven are PVD.

## Open items

1. Photos still to shoot when Higgsfield allows (see above), then a productSet per product by handle with the full gallery, passing
   each size card as `{"id": <MediaImage id>}` so its filename (which the description links) is not renamed.
2. K07 has no size card yet (its card is drawn on its packshot). Its description has no size-guide image until then.
3. The pendant's chain length is not measured (the chain runs behind the card). A tape measure on one piece settles it.
4. PVD lines and compare-at prices, if the owner wants them as on the older Aditya listings.

## Scripts (run from `build/` with `python3 -I`)

`build.py` (requests), `fetch.py` (downloads), `putrefs.py` / `put.py` (Higgsfield uploads: reference crops / exports and cards),
`export.py` (1288×1600 exports by `chosen.json`), `sizecards.py` (cards via `../aditya-jewellery/build/sizeguide.py`, callouts in
`photocards.json`), `ship_26nov.py` (the Shopify mutation).
