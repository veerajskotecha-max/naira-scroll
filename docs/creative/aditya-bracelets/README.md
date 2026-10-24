# Aditya bracelets

Ten bracelets Aditya showed on a WhatsApp video call: nine photos, then a tenth sent separately. On 2026-10-24 they became 8 Shopify **drafts** with 10 SKUs, 5 units each and no prices yet.

| SKU | Product | Option | Stones | Clasp | Finish | Admin |
|---|---|---|---|---|---|---|
| ADT01 | Clarté Baguette Bracelet | — | Clear baguettes, about 6 × 3 mm, set crosswise; band about 6 mm wide | Fold-over | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353404903586) |
| ADT02 | Sorbet Rivière Bracelet | — | Round, about 3 mm; baby pink, pale lime and lilac blue mixed along the line | Fold-over | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353404936354) |
| ADT03 | Emerald Carré Bracelet | — | Square princess cut green, about 4 mm | Fold-over | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353404969122) |
| ADT04 | Rivière Classique Bracelet | — | Round clear, about 3.5 mm | Box | Gold tone; card says stainless steel | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353405001890) |
| ADT05 | Midnight Rivière Bracelet | — | Round navy blue, about 4 mm | Fold-over | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353413259426) |
| ADT06-RB / ADT06-LV | Aquarelle Rivière Bracelet | Royal Blue / Lavender | Round, about 3 mm | Fold-over | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353413292194) |
| ADT07-FU / ADT07-VI | Bougainvillea Vine Bracelet | Fuchsia / Violet | Vine with 5 flowers: four five-petal flowers, about 7 mm, and one six-petal centre flower, about 11 mm (ruby red on Fuchsia, lilac on Violet); clear pavé leaves | Fold-over tongue into a D ring | Silver tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353413324962) |
| ADT08 | Lumière Solitaire Bracelet | — | Clear ovals, about 5 × 3 mm, set crosswise, with one round centre stone of about 7 mm | Box | Gold tone | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353413357730) |

Reference keys A1–A10 follow the photo order. A6 and A7 are the two colours of one design, as are A8 and A9. The single-bracelet crops are in `refs/`: `_full` is the whole piece and `_det` is a close crop.

Stone sizes are measurements, not supplier figures. `build/pitch.py` traces the line of stones in a photo and finds their spacing by autocorrelation. That spacing, scaled to the stated 17 cm length, gives the size of each stone.

## Images (the house listing format, 1288×1600)

The recipe is the Edition Two one (`build/build.py`, copied from `edition-two-listings`):

1. Hero on the cream plaster cube (`H`).
2. Worn on the saffron-camisole model (`W1`), then a close wrist frame (`W2`).
3. Macro (`M`).

Worn and macro frames pass the approved hero as IMAGE 2. Image 1 is the supplier photo. The prompt tells the model to ignore the plastic sleeve, the card, the rubber band and the hands.

There were four reshoots or fixes:

- **A5 hero** first came out draped over the cube edge. It was reshot lying flat on the cube top (`A5_H2`).
- **A6 hero** had stones that were too chunky. It was rebuilt as an edit of the Lavender hero, then deepened to the photo's royal blue with `colour.py` (`A6_Hc`).
- **A9 hero** first showed three flowers. It was rebuilt as an edit of the Fuchsia hero with the colours changed (`A9_H2`).
- **A4 worn shot** (`A4_W1`) had a paper border and was reshot.

`export.py` maps those keys and trims a 1.5% inset, which removes the white side strips some worn frames had. It then writes `exports/<handle>-NN.jpg` in listing order. `board.jpg` is the review sheet with one row per product.

Each single-colour product has 4 images. Aquarelle has 7: Royal Blue has hero, worn and macro, and Lavender adds a wrist frame. Bougainvillea also has 7: Fuchsia has 4 and Violet has hero, worn and macro.

Higgsfield cost: 42 generations at 2K, 84 credits. The balance is 116.07.

## Shopify

- `shopify/listing.json` is the copy: title, handle, tagline, body, styling tip and details for each product.
- `build/shopify_payload.py` turns it into `shopify/payloads/<handle>.json` in the store's description format: intro, STYLING TIP, Details, size guide, Care and the box line.
- `build/sizeguide.py` draws the size-guide cards in `shopify/sizeguides/`. They are uploaded to Shopify Files and embedded in each description.

Verified after the push (`shopify/pushed.json`):

- All 8 products are DRAFT with vendor Naira Petite and type Bracelet.
- 10 variants with SKUs ADT01–ADT08, each tracked with 5 available at Forest Colony Parijat Nagar.
- 38 images, all READY. Each colour option has its own hero attached.
- Google and Facebook category metafields are set (191, Apparel & Accessories > Jewelry > Bracelets).

`build/cdn_compare.py` downloads every image and size guide back from the Shopify CDN and matches it to its local export. All 46 match, each in the right position (`shopify/cdn_check.txt`).

Care copy is the plain line, with no waterproof, tarnish-free or hypoallergenic tags. The base metal is unknown for every piece except ADT04, whose card says stainless steel. The coloured stones are described as cubic zirconia, "not emerald" and "not sapphire".

## Before publishing

1. **Prices.** Every variant is at 0.00, left for the owner.
2. **Adjustable lengths.** Every listing says "Approximately 17cm" because no slider or extender shows in the photos. For the pieces that adjust from 15 to 19 cm, `sizeguide.py` takes an adjust range, and the Length line should change to match.
3. **Overlaps with live products** (see `shopify/overlaps.jpg`):
   - ADT01 matches Baguette Éclat Bracelet (live, 15 units) and the Crystal option of Baguette Tennis Bracelet (live, 58).
   - ADT03 is close to Verdant Rivière Bracelet (draft, 5) and the Emerald option of Baguette Tennis Bracelet. Those use rectangular stones; ADT03's are square.
   - ADT04 joins four round clear gold lines already in the store: Rivière Eternal (live, 34), the KAVNAR Rivière Eternal (draft, 20), Rivière of Light (live, 0 units) and Fine Tennis (live, 20).
4. **Violet centre flower.** It is shot with all lilac petals. Some petals look clear in Aditya's photo, which is probably glare; check it against the piece when the stock arrives.

Scripts run from this folder's layout with `python3 -I`. `build/out/` (the raw frames) and the Higgsfield upload response, which holds presigned URLs, are not committed (see `.gitignore`).
