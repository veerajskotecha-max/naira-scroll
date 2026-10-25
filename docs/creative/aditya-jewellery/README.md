# Aditya jewellery (phase 2)

Sixteen photos Aditya sent after the bracelets (phase 1, [`../aditya-bracelets`](../aditya-bracelets/README.md)) became 18 Shopify products on 24 and 25 Oct 2026: ADT09 to ADT26, one SKU each, listed with 5 units each. Together with phase 1 (8 products, 10 SKUs) that is 26 products and 28 SKUs.

| SKU | Ref | Product | Type | Cost | Price | Units | Status | Set on the site | Admin |
|---|---|---|---|---|---|---|---|---|---|
| ADT09 | J01 | Clover Drop Pendant Necklace | Necklace | ₹250 | ₹875 | 3 | **Active** | Clover (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353568645282) |
| ADT10 | J02 | Clover Drop Earrings | Earrings | ₹290 | ₹1015 | 4 | **Active** | Clover (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353568678050) |
| ADT11 | J03 | Clover Chain Bracelet | Bracelet | ₹140 | ₹800 | 4 | Draft | Clover (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353569661090) |
| ADT12 | J04 | Clover Station Bracelet | Bracelet | ₹250 | ₹875 | 5 | Draft | Clover (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353626185890) |
| ADT13 | J05 | Twin Heart Necklace | Necklace | ₹240 | ₹999 | 1 | **Active** | Twin Heart (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353626218658) |
| ADT14 | J06 | Twin Heart Studs | Earrings | ₹260 | ₹910 | 1 | **Active** | Twin Heart (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353627136162) |
| ADT15 | J07 | Bow Pear Drop Necklace | Necklace | ₹250 | ₹999 | 5 | **Active** | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353627332770) |
| ADT16 | J08 | Petite Blossom Bracelet | Bracelet | ₹175 | ₹613 | 5 | Draft | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353627365538) |
| ADT17 | J09 | Open Heart Layered Bracelet | Bracelet | ₹160 | ₹560 | 5 | Draft | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353627398306) |
| ADT18 | J10 | Watch Link Bracelet | Bracelet | ₹300 | ₹1050 | 5 | Draft | Watch Link (new) | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628479650) |
| ADT19 | J11 | Molten Wave Ear Cuff | Earrings | ₹140 | ₹490 | 4 | Draft | Molten | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628512418) |
| ADT20 | J12 | Asscher Solitaire Ring | Ring | ₹200 | ₹700 | 3 | **Active** | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628545186) |
| ADT21 | J13 | Cushion Solitaire Ring | Ring | ₹210 | ₹735 | 5 | Draft | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628577954) |
| ADT22 | J14 | Pavé Zigzag Ring | Ring | ₹180 | ₹630 | 4 | **Active** | — | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353729405090) |
| ADT23 | J15 | Lumière Oval Solitaire Ring | Ring | ₹180 | ₹699 | 3 | **Active** | Lumière | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628610722) |
| ADT24 | J16 | Prism Pear Drop Necklace | Necklace | — | — | 5 | Draft | Prism | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353729437858) |
| ADT25 | J17 | Prism Pear Drop Hoops | Earrings | — | — | 5 | Draft | Prism | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353729470626) |
| ADT26 | J18 | Pearl Heart Layered Necklace | Necklace | — | ₹999 | 3 | **Active** | Pearl | [open](https://admin.shopify.com/store/nc5eti-gp/products/10353628643490) |

Snapshot of 25 Oct 2026, 14:48 UTC (`shopify/pushed.json`), after the size check below; units, prices and statuses include the owner's own edits from Shopify Mobile. The review page with every phase 1 and phase 2 piece and the owner's approve, changes, go-live, price and notes controls is https://claude.ai/artifact/4CU1RH5ixQMpq4VzLCtZKj. Its answers are stored in the page's `reviews` collection, one document per handle.

## Prices

Price is 3.5 × the supplier price written on the call photos (the owner's rule for phase 2). Cost per item is that supplier price. ADT24 and ADT25 had no price on their photo, so price and cost are empty. ADT26 had none either; the owner set it to ₹999 in Shopify, and its cost is still empty.

## Sets

The storefront reads sets from the product name (`src/lib/pairings.ts` in the Lovable repo). Three new set lines and four adjustable rings are on the Lovable branch `claude/higgfield-12-angles-4j09gn` (commit 46cb97b):

- **Clover**: the pendant necklace, drop earrings, chain bracelet and station bracelet, beside the live Clover Charm Necklace and Clover Trio Edit.
- **Twin Heart**: the necklace and the studs.
- **Watch Link**: the bracelet, beside the live Watch Link Ring.
- **Adjustable, US 5 to 8**: Asscher Solitaire Ring, Cushion Solitaire Ring, Pavé Zigzag Ring and Lumière Oval Solitaire Ring (`src/data/ringFit.ts`).

Lines that already existed pick up the rest by name: Prism (the pear drop necklace and hoops), Lumière (the oval ring, with the phase 1 Lumière Solitaire Bracelet), Pearl and Molten. The branch passes 425 tests, `tsc` and `vite build`. It needs a merge to main and a Publish in Lovable before the site shows the new sets.

## Images (the house listing format, 1288×1600)

The recipe is the aditya-bracelets one (`build/build.py`): a hero on the cream plaster cube (`H`), one worn frame on the saffron-camisole model (`W1`) and a macro (`M`). Worn and macro frames pass the approved hero as IMAGE 2. `approved.json` holds the job of every frame in use. `export.py` maps reshot keys to their takes, trims a 1.5% inset and writes `exports/<handle>-NN.jpg`. `board.jpg` is the review sheet.

`sizeguide.py` draws the 1600×1600 size-guide cards in `shopify/sizeguides/`: the ring card for the four rings, and a photo card with measurement bars for the clover drops, the twin heart studs, the ear cuff and the pear drop hoops. Necklaces and bracelets have no card because their chain lengths are not known.

### 25 Oct reshoot

- **Heart and pear sets 30% smaller.** The owner said the twin heart necklace and studs (J05, J06) and the prism pear necklace and hoops (J16, J17) are about 30% smaller than they were shot. The heroes were redone (`J05_Hf`, `J06_He`, `J16_Hg1`, `J17_Hs`). The worn frames were shrunk by repeated edits (`J05_W1e2`, `J06_W1e2`, `J16_W1r2`, `J17_W1h2`); `J16_W1r2` also re-hangs the pears as one vertical drop after an edit had set them side by side. The copy and size guides now read 8.5 mm across for the hearts, a 12 mm drop for the necklace and 21 mm with an 8.5 mm huggie for the hoops. The worn pear drop frames still read about 1.3 to 1.4 times long against the body; the image model would not draw them smaller.
- **Zigzag ring.** J14 was shot as a V and listed as the Pavé Wishbone Ring. It is now the Pavé Zigzag Ring (`pave-zigzag-ring`), reshot as a zigzag with eight stones on the middle stroke and plain arms (`J14_Hn`, `J14_W1z`, `J14_Mn`). The supplier's bends look squarer; two tries at square bends (`J14_Hq`, `J14_Hr`) did not hold the design.
- Higgsfield cost of the reshoot: 76 credits (202.07 to 126.07).

### 25 Oct size check

Every worn frame was measured against the body it is on (a mouth is about 48 mm wide, an ear about 58 mm tall, a wrist about 52 mm across, a finger about 16.5 mm), and every supplier photo against Aditya's own hand. Ten worn photos read too big or wrong and were brought to their listed size:

| SKU | Piece | Listed | Worn photo read | Now | How |
|---|---|---|---|---|---|
| ADT09 | Clover Drop Pendant Necklace | drop 17 mm | 29 mm | 18 mm | pinch, `J01_W1p` |
| ADT10 | Clover Drop Earrings | 19 mm long | 38 mm | 20 mm | cut and scaled, blended on Higgsfield, `J02_W1c` |
| ADT11 | Clover Chain Bracelet | clover 9 mm | 14 mm | 9 mm | pinch, `J03_W1p` |
| ADT13 | Twin Heart Necklace | 8.5 mm across | 13 mm | 8.5 mm | pinch, `J05_W1p` |
| ADT14 | Twin Heart Studs | 8.5 mm across | 7.5 mm, hearts drawn pavé | 8 mm | the packshot's heart cut stud swapped in, `J06_W1s` |
| ADT15 | Bow Pear Drop Necklace | bow 10 mm | 19 mm | 11 mm | pinch, `J07_W1p` |
| ADT16 | Petite Blossom Bracelet | flower 8.5 mm | 12 mm | 8.5 mm | pinch, `J08_W1p` |
| ADT19 | Molten Wave Ear Cuff | 15 × 12 mm | removed | 15 mm | new take on the rim, pinched, `J11_W1qp` |
| ADT24 | Prism Pear Drop Necklace | drop 12 mm | 21 mm | 12.5 mm | cut and scaled, `J16_W1d` |
| ADT25 | Prism Pear Drop Hoops | 21 mm long | 29 mm | 21 mm | cut and scaled, `J17_W1d` |

- `build/retouch.py` makes every retouched frame from its source take. A *pinch* scales the ellipse round the piece about its centre and eases back to full size, so a chain stays joined to it. *Cut and scaled* clone-stamps the area with plain skin or hair and pastes the piece back smaller from its bail or piercing. The swap cuts the packshot's stud and sets it on a cleaned lobe.
- Plain shrink edits on Higgsfield came back the same size, and blends of the cut composites redrew three pendants large or added parts, so J02 is the only model output kept (`build/fix_requests.py`). The ear cuff took six takes; every one put the cuff on the lower half of the ear, and the one kept hugs the outer rim above a bare lobe. Higgsfield cost: 22 credits (120.07 to 98.07).
- On size and left alone: the clover station, open heart, watch link and zigzag photos, the pearl hearts (about 9 mm against 7 mm), and all eight phase 1 bracelets, whose stone counts across the wrist match their 3 to 6 mm stones.
- Copy: the ear cuff now reads 15 mm across and 12 mm tall (it said 15 mm tall). Against Aditya's thumb it is about 15 to 16 mm across and 12 mm tall.
- Open, copy left as it is: (1) the owner's 30% note puts the velvet card at about 52 mm, but Aditya's thumb and the bracelets wrapped round it put it at about 80 mm, which would make the hearts and pears about 1.5 times what the copy now says; a ruler on one Twin Heart stud settles it. (2) Against his fingers the ring stones are bigger than listed: Asscher about 10 mm (8), cushion about 16 × 10 mm (12 × 8), oval about 10 × 8 mm (7 × 5), and the Lumière Solitaire Bracelet's centre stone about 9 to 10 mm (7). The worn ring photos agree with the supplier photos.

## Shopify

Verified on 25 Oct 2026 (`shopify/pushed.json`, `shopify/cdn_check.txt`):

- 18 products with vendor Naira Petite, the product category, the Google and Facebook category metafields, tracked inventory at Forest Colony Parijat Nagar, and the house description (intro, styling tip, details, size guide where there is one, care, box line).
- All 18 are attached to the same 6 sales channels as the live jewellery: Online Store, Point of Sale, Facebook & Instagram, Google & YouTube, Naira Headless and Lovable (25 Oct, 12:46 UTC).
- 9 are Active, all set by the owner from Shopify Mobile: ADT20, ADT22, ADT23 and ADT26 first, then ADT09, ADT10, ADT13, ADT14 and ADT15 (25 Oct, about 13:22 UTC). The other 9 are drafts.
- The owner also changed units on most pieces and some prices (ADT11 ₹800, ADT13 ₹999, ADT15 ₹999, ADT23 ₹699, ADT26 ₹999), and removed the worn photos of ADT09, ADT10, ADT11, ADT14, ADT15 and ADT19. Those edits are kept. The size check added corrected worn photos back to those six as image 2 and replaced ADT13, ADT16, ADT24 and ADT25's in place; nothing else on the listings changed except the ear cuff's size line.
- `build/cdn_compare.py` downloaded all 54 listing images and 8 size guides back from the Shopify CDN (`shopify/cdn_check.txt`, 14:40 UTC): each matches its local export, and no image is closer to another export.
- `pave-wishbone-ring-size-guide.jpg` (gid://shopify/MediaImage/46555948023970) is still in Shopify Files from before the rename. Nothing uses it.

The care copy is the plain line, with no waterproof, tarnish-free or hypoallergenic claims, because the base metal is unknown for every piece except the ear cuff, whose card says stainless steel. Stones are described as cubic zirconia in gold tone settings.

## Before publishing

1. **Prices**: ADT24 and ADT25 have no price or cost. ADT26 has no cost.
2. **Sizes**: a ruler on one Twin Heart stud and one ring settles the two open size questions under the size check.
3. **Storefront claims**: the Lovable site prints "surgical stainless steel · waterproof, anti-tarnish" under every live jewellery piece (`src/hooks/useLiveJewellery.ts`) and shows an Anti-Tarnish badge (`JewelTrustStrip`, `ProductDetails`). That now includes the nine live Aditya pieces. Confirm the base metal with Aditya, or drop the claim for Aditya pieces.
4. **Lengths**: the necklaces (ADT09, ADT13, ADT15, ADT24, ADT26) and bracelets (ADT11, ADT12, ADT16, ADT17, ADT18) need chain lengths for the copy and a size guide.
5. **Pearl material**: the supplier called ADT26's stones "white heart shaped pearls". The copy calls them pearls; confirm shell, glass or plastic.
6. Phase 1 still needs prices, its 15 to 19 cm question and its overlap checks (`../aditya-bracelets/README.md`).

Scripts run from `build/` with `python3 -I`: `build.py` (requests), `fetch.py` (downloads), `export.py`, `sizeguide.py OUTDIR`, `shopify_payload.py` (productSet inputs in `shopify/payloads/`), `put_exports.py` (public URLs for Shopify, `url_map.json`), `cdn_compare.py PRODUCTS_QUERY_JSON DOWNLOAD_DIR`, `board.py`, `retouch.py` (the size-check retouches) and `fix_requests.py` (the size-check Higgsfield requests). `build/out/` holds the raw 1856×2304 frames (565 MB) and is not committed; `fetch.py` downloads them again from `results.json`.
