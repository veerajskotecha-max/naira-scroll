# Clover Garland Bracelet and Rivière Classique Necklace (30 Oct 2026)

The owner sent two photos of a clover-link bracelet, one of the sky blue, pink, red and clear strands in their sleeves
(`refs/colours_full.jpg`) and one of the clear strand in hand (`refs/white_in_hand.jpg`). They asked for it in blue, pink
and white, 5 of each, with prices, the stone size checked against a finger, and listing photos the way the store lists. A
second message added a classic tennis necklace from a shop photo (`../tennis-necklace/refs/albyluxe_screenshot.jpg`), 10
each in white and gold, with size cards for everything sent that day. Both are live on Shopify, each with 4 photos per
colour or metal and a size card. The board is `board_30oct.jpg`.

| Listing | Option | SKU | Units | Price | Admin |
|---|---|---|---|---|---|
| Clover Garland Bracelet | Sky Blue / Pink / White | CLG-SB / CLG-PK / CLG-WH | 5 each | ₹1,299 against ₹2,500 | [open](https://admin.shopify.com/store/nc5eti-gp/products/10374743261346) |
| Rivière Classique Necklace | Silver / Gold | RCN-S / RCN-G | 10 each | ₹1,499 against ₹2,800 | [open](https://admin.shopify.com/store/nc5eti-gp/products/10374743294114) |

Prices follow the house lines: the clover is priced like the Carré and Clarté bracelets, the necklace like the Lumière Oval
Necklace. No cost per item was given, so none is set.

## Sizes

These are estimates from the owner's photos. Nothing was measured with a ruler.

- **Clover bracelet.** The thumb in `refs/white_in_hand.jpg` is about 96 px across. Taken as about 16 to 17 mm, that is
  roughly 5.5 to 6 px per mm. The lobster clasp (about 60 px) and the round tag (about 42 px) agree with that.
  - Each clover is about 65 to 70 px tip to tip, so about 10 to 12 mm across. The listing says 10 mm. Each round stone is
    about 3.5 mm, with a small clear stone at the centre.
  - The strand has 15 clovers. The clovers sit about 1.4 clover-widths apart, which puts the full strand at roughly 20 to
    22 cm with the clasp and extender. The listing and card say about 17 cm, adjustable to about 21 cm with the extender.
  - The clovers link petal tip to petal tip with a single small ring (`refs/blue_strand.jpg`, the blue strand turned
    level). Each petal sits in a cup with a beaded rim.
- **Tennis necklace.** In the shop photo the line spans about 13 cm across the base of the neck, about 4 px per mm. The
  stones repeat every 12 to 13 px, so they are about 3 mm. It sits at the base of the neck, so it is about 40 cm.
  - The store's Rivière Eternal has a buckle station at the front, so this plain line is a new listing. It takes the name
    of the Rivière Classique Bracelet draft, which is the same plain round-stone line.
- **Worth a tape measure:** the clover's length and clover width, and the necklace length. Correct the copy and
  `build/sizecards.py` if they differ.

## Photos

The recipe is the house one (`build/build.py`, from `../aditya-bracelets/build/build.py`): hero on the cream plaster cube,
worn on the saffron-camisole model, a second worn frame, and a macro. Nano Banana Pro at 2K, 19 jobs, 38 credits; 382.32 left.

- **Clover, Sky Blue (shot).** IMAGE 1 is the blue strand turned level (`refs/blue_strand.jpg`) and IMAGE 2 a close detail.
  - Hero take A joined the clovers with two-link chains and was dropped. Take B (`C1_H_b`) has the single rings and was kept.
  - The first worn frame came back with an old-photo border and was reshot. The reshoot had a thin border too, so the clean
    picture inside it was cropped to 4:5 (`C1_W1c`).
- **Clover, Pink and White (no new shoot).** `build/recolour.py` changes only the petal stones in the four blue photos, so
  the strand, its size and the model are identical in all three colours.
  - The blue sits at CIELab hue 200 to 250 degrees; the gold, skin and camisole sit at 40 to 90.
  - The petals' dark edges, the macro's out-of-focus clovers and a zone around the bracelet in the worn frames are handled
    as the script describes. In the worn frames, nothing more than about 80 px from the bracelet changes.
  - Pink is a soft rose (L 68, C 24, hue 8). White maps lightness onto a clear stone's.
- **Necklace, Silver (shot).**
  - The first two heroes coiled it like a bracelet with chunky stones. It was reshot draped over the cube; take C was kept.
  - The first worn frames drew the line about 5 mm wide. They were reshot with the line thinner than the camisole strap
    and come out about 4 mm.
- **Necklace, Gold.** Higgsfield edits of the four approved silver frames that change only the metal. The worn frames read
  mostly white at listing size, because the stones cover the claws.
- `build/export.py` writes the 1288×1600 exports after the house 1.5% inset. `build/out/` (the raw frames) is not
  committed; `build/jobs.json` and `../tennis-necklace/build/jobs.json` hold every job id.

## Size cards

`build/sizecards.py` draws both cards with the house generators (`../size-cards/build/cards.py`). Both say the length is
approximate.

- The clover gets the bracelet ruler card: adjustable 17–21 cm, fits wrists about 14.5–19.5 cm.
- The necklace gets the neck card at 40 cm, stones 3 mm.

## Shopify (one approval)

`build/ship_30oct.py` builds `shopify/ship_30oct.graphql` and `shopify/ship_30oct.json`. `build/put.py` put the exports on
Higgsfield's store for public URLs (`build/url_map.json`).

- **The mutation.** It turned `autoPublish` on for the six sales channels, ran a `productSet` for each listing (ACTIVE,
  with variants, stock, photos, each variant's hero, the size card as the last photo under its linked name, the metafields
  and SEO), then turned `autoPublish` off again. No user errors.
- **Copy.** The copy says gold tone and silver tone and cubic zirconia, with the plain care line. It makes no waterproof,
  tarnish-free or PVD claims, as the plating is not confirmed. The clover says stainless steel because its sleeve card does.
- **Verified (31 Oct, 00:30 UTC).**
  - Both listings are ACTIVE on all 6 channels with stock of 15 and 20. All 22 media are READY. Each variant's image is its
    own hero.
  - All 22 CDN copies match the exports, with a mean difference of 0.27 to 2.34 out of 255. Each matches its own colour or
    metal far better than a sibling's.
  - The Storefront API reads both as available, every variant buyable, the size card last in the gallery and in the
    description.
- **Storefront.** The snapshot was regenerated (Lovable repo, same branch, `4057dd6`; 117 pieces) and its 275 tests pass.
  `shopify/pushed.json` has the ids.
- **Not done.** No Meta ad was changed. The red strand in the photo was not listed. The "same necklace" in the first
  message was not listed as a clover necklace: no photo of one was sent. The store's Clover Charm Necklace is a different
  clover, with plain rims and a gold bead centre.
