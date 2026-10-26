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

### 25 Oct: Bougainvillea flowers brought down to the piece's size

The owner's review note said the flowers on the piece are smaller than in the photos, by about 30%. Measuring against Aditya's photos (`refs/A8_full.jpg`, `A8_det.jpg`, `A9_full.jpg`, `A9_det.jpg`) agreed:

- On the piece the small flowers are about 0.65 of the centre flower, and the centre flower spans about 4.9 of the round joints beside it.
- In the photos the centre flower drew about 1.3× too big. That is about 15 mm on the hero's 17 cm loop. In the worn frames it covers about 30% of the wrist's width, where a real 11 mm flower covers about 22%.
- The small flowers were about 1.2× too big on the wrist, and the right size on the plinth.

`build/retouch.py` fixes the approved takes with no new credits. It warps each image (moving least squares): each flower scales about its own centre, and the joints and leaves beside it slide in with it, so the vine stays joined. The other flowers, the clasp, the plinth edges and the arm's outline are pinned. Only the bare stems and the plain plaster or skin around a flower stretch.

| Take | Centre flower | Small flowers |
|---|---|---|
| Heroes `A8_Hs`, `A9_Hs` | 0.76 | unchanged |
| Worn `A8_W1s` | 0.74 | 0.74; the one on the arm's edge 0.9 |
| Worn `A8_W2s` | 0.77 | 0.82 |
| Worn `A9_W1s` | 0.75 | 0.82 |
| Macros `A8_Ms`, `A9_Ms` | 0.84, from the flower-to-joint ratio in Aditya's close-up | — |

All 7 images were replaced in place on the draft, with the same media ids and order, so each colour option keeps its hero. `shopify/cdn_check.txt` was rerun and all 46 images match. The copy's 7 mm and 11 mm stand.

`export.py` maps those keys and trims a 1.5% inset, which removes the white side strips some worn frames had. It then writes `exports/<handle>-NN.jpg` in listing order. `board.jpg` is the review sheet with one row per product.

Each single-colour product has 4 images. Aquarelle has 7: Royal Blue has hero, worn and macro, and Lavender adds a wrist frame. Bougainvillea also has 7: Fuchsia has 4 and Violet has hero, worn and macro.

Higgsfield cost: 42 generations at 2K, 84 credits. The balance is 116.07.

### 26 Oct: Emerald Carré in four more colours

The owner sent Aditya's photo of the same square-stone tennis line in pink, blue, champagne, green and purple (two of the
green). They asked for each colour as its own listing, with the green listing's photos in that colour, 2 in stock each,
and live.

- **Photos, no new shoot** (Higgsfield had 1.32 credits). `build/recolour_carre.py` recolours only the stones in the four
  Emerald Carré photos. Every pixel at the stones' green hue in CIELab moves to the target colour, keeping its lightness
  and chroma relative to the stones' median, so facets, glints and shadows stay put. Yellow-greens, where a stone shows
  through the gold on the far side of the loop, are split into a gold share and a stone share, so no olive is left. The
  targets were read from Aditya's photo, beside the green under the same light: pale lilac pink, deep sapphire blue, warm
  champagne, violet. Outside the stones the mean change is under 0.5/255 (the JPEG re-save). At most 162 green pixels
  remain in a frame, out of 2 million.
- **Check.** `carre_colours.jpg`: each row starts with Aditya's photo of that colour, then the four listing photos.
- **Listings** (`shopify/carre_colours.json`, `build/carre_payloads.py`, `shopify/payloads/`), live on all 6 channels, 2
  each, ₹1,299 against ₹2,500 like the green:

  | SKU | Product | Admin |
  |---|---|---|
  | ADT03-BL | Blush Carré Bracelet (pale pink) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10354825658530) |
  | ADT03-SA | Sapphire Carré Bracelet (blue; the copy says "not sapphire") | [open](https://admin.shopify.com/store/nc5eti-gp/products/10354825691298) |
  | ADT03-CH | Champagne Carré Bracelet | [open](https://admin.shopify.com/store/nc5eti-gp/products/10354825724066) |
  | ADT03-AM | Amethyst Carré Bracelet (violet; the copy says "not amethyst") | [open](https://admin.shopify.com/store/nc5eti-gp/products/10354825756834) |

  The copy is Emerald Carré's with the colour swapped. It keeps the green's live PVD lines. Each listing has its own
  size-guide card (`shopify/sizeguides/`, Shopify Files). The Storefront API reads all four as available, and the CDN
  copies of the 16 photos match the exports.
- **Emerald Carré** (green, ADT03) is still a draft with 5 units, as it was.
- **Catalogue ad.** All five Carré ids are in the ₹500/day New 12 product set (`../aditya-jewellery/README.md`). The four
  new ones show now; the green joins if it goes live.

## Shopify

- `shopify/listing.json` is the copy: title, handle, tagline, body, styling tip and details for each product.
- `build/shopify_payload.py` turns it into `shopify/payloads/<handle>.json` in the store's description format: intro, STYLING TIP, Details, size guide, Care and the box line.
- `build/sizeguide.py` draws the size-guide cards in `shopify/sizeguides/`. They are uploaded to Shopify Files and embedded in each description.

Verified after the push (`shopify/pushed.json`):

- All 8 products are DRAFT with vendor Naira Petite and type Bracelet.
- 10 variants with SKUs ADT01–ADT08, each tracked with 5 available at Forest Colony Parijat Nagar.
- 38 images, all READY. Each colour option has its own hero attached.
- Google and Facebook category metafields are set (191, Apparel & Accessories > Jewelry > Bracelets).
- The product category is set to Apparel & Accessories > Jewelry > Bracelets (`aa-6-3`), added 2026-10-25.
- The vendor and type rules already place all 8 in the Shop All and Bracelets collections.
- Since 2026-10-25 each product is attached to the same 6 sales channels as the live bracelets: Online Store, Point of Sale, Facebook & Instagram, Google & YouTube, Naira Headless and Lovable. Shopify shows nothing on a channel while a product is DRAFT, so each reads "not published" there until it is switched to Active.

`build/cdn_compare.py` downloads every image and size guide back from the Shopify CDN and matches it to its local export. All 46 match, each in the right position (`shopify/cdn_check.txt`).

Care copy is the plain line, with no waterproof, tarnish-free or hypoallergenic tags. The base metal is unknown for every piece except ADT04, whose card says stainless steel. The coloured stones are described as cubic zirconia, "not emerald" and "not sapphire".

## Before publishing

1. **Prices.** Every variant is at 0.00, left for the owner. Set the price before switching a product to Active: it goes live on all 6 channels at that moment. Cost per item is also empty; the live bracelets carry one, which feeds the margin reports.
2. **Adjustable lengths.** Every listing says "Approximately 17cm" because no slider or extender shows in the photos. For the pieces that adjust from 15 to 19 cm, `sizeguide.py` takes an adjust range, and the Length line should change to match.
3. **Overlaps with live products** (see `shopify/overlaps.jpg`):
   - ADT01 matches Baguette Éclat Bracelet (live, 15 units) and the Crystal option of Baguette Tennis Bracelet (live, 58).
   - ADT03 is close to Verdant Rivière Bracelet (draft, 5) and the Emerald option of Baguette Tennis Bracelet. Those use rectangular stones; ADT03's are square.
   - ADT04 joins four round clear gold lines already in the store: Rivière Eternal (live, 34), the KAVNAR Rivière Eternal (draft, 20), Rivière of Light (live, 0 units) and Fine Tennis (live, 20).
4. **Violet centre flower.** It is shot with all lilac petals. Some petals look clear in Aditya's photo, which is probably glare; check it against the piece when the stock arrives.
5. **Lumière size (ADT08).** It was checked against Aditya's photo on 25 Oct, after the owner's review note "Check with real one once" (go live: no). The design matches: crosswise ovals, one round centre stone in claws and a box clasp. The size does not:
   - On the piece the line is about 5 mm wide, the slim ovals sit about 3 mm apart and the centre stone is about 8 to 9 mm.
   - The wrist photos draw the line about 1.3× too big: about 6.5 to 7 mm wide, with fewer and rounder ovals, and a centre of about 10.5 to 11 mm.
   - The hero is closer: its centre is about 8.7 mm, but its line is about 6 mm wide.

   A tennis line can't be warped smaller without changing its stone count, so the fix is a reshoot of all 4 photos, about 8 credits a try. It waits for the owner's go-ahead. The copy's 7 mm centre may also be a little small: Aditya's photo suggests about 8 mm, so check it with a ruler.

Scripts run from this folder's layout with `python3 -I`. `build/out/` (the raw frames) and the Higgsfield upload response, which holds presigned URLs, are not committed (see `.gitignore`).
