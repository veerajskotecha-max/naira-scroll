# Ring sizes, 26 Oct 2026

The owner, 26 Oct: some adjustable rings showed only pre-order on the site. Every adjustable ring fits US 5 to 9. Make every ring's sizes and stock read correctly on the site and in Shopify.

## Why the site showed pre-order

The live site's list of adjustable rings held 10 handles. Asscher Solitaire, Lumière Oval Solitaire and Pavé Zigzag (live), and Cushion Solitaire (draft), were missing from it. Their pages therefore offered US 5, 6 and 7, and sold US 5 and 7 as pre-orders. The rings on the list offered US 5 to 8, and Cushion Halo offered US 5 to 7.

A closed ring's page opened on "US 6 is in stock" whatever its size. Chevron Whisper and Pearl Ribbon are made in US 7, so the size in stock was sold as a pre-order.

## Shopify (done and verified)

- **Tags.** All 15 adjustable rings are tagged `Adjustable`: the 13 live ones, plus Cushion Solitaire and Duet of Dawn, which are drafts.
- **Descriptions.** Each says "US 5 to 9" in the intro and on the Size line, and links its size guide at the new `?v`. Duet of Dawn's "a little play in the fit" became "adjusts to fit US 5 to 9", like Golden Duet. `descriptions.json` keeps the old and new HTML of all 15 for a rollback. The 13 live descriptions read back exactly through the Storefront API, and the 2 drafts through the Admin API.
- **Size guides.** 14 cards were replaced in place, with the same file ids, at `?v=1793001915` (Asscher `?v=1793001916`). The US 8 and US 9 chips are filled and the foot line reads 5 to 9. Duet of Dawn has no card.
- **Stock.** Every ring is tracked and stops selling at zero. An adjustable ring is one stock: the size the shopper picks rides on the order as a note. On 26 Oct: Cushion Halo 60, Verdant Eternity 60, Halo Curve 45, Droplet Open 10 + 10, Golden Duet 9, and 1 to 4 each for the rest.

## Storefront

Another session put the adjustable-ring fix on `main` as `4426bfd`. A ring is adjustable when it is on the list or Shopify tags it `Adjustable`, and every adjustable ring offers US 5 to 9.

Branch `claude/higgfield-12-angles-4j09gn` (`9b062d7`) merges that and adds:

- `stockedSize()`: a closed ring opens on the size it is stocked in (US 7 for Chevron Whisper and Pearl Ribbon, otherwise US 6). That size ships now; the others are pre-orders.
- The jewellery page FAQ, which still said every ring is US 6 in stock with US 5 and 7 on pre-order.
- 56px size chips, so five sizes sit on one row on a 360px phone.
- SEO ring pages updated to US 5 to 9.
- A regenerated catalogue snapshot.

It goes live when it is merged to `main` and Lovable's Publish is pressed.

## Every live ring

| Kind | Rings | The page shows |
|---|---|---|
| Adjustable (13) | Asscher Solitaire, Blush Cluster, Cushion Halo, Droplet Open, Golden Duet, Granule Dome, Halo Curve, Lumière Oval Solitaire, Pavé Zigzag, Petite Pavé, Rose Verdant, Pavé Dome (`silver-dome-ring`), Verdant Eternity | US 5 to 9, every size ships now |
| Sold in sizes (8) | Baguette Eternity, Chain Drop Dome, Crystal Baguette Eternity, Linked Pair (`linked-trio-ring`), Mesh Band, Star Point, Watch Link (US 5 to 8); Roman Numeral Trio (US 6 to 9, US 8 sold out) | Shopify's own size variants and stock |
| Closed, one size (5) | Chevron Whisper and Pearl Ribbon (US 7); Vintage Halo (US 6); Whisper Pavé (about 17 mm, "between US 6 and 7", shown as US 6); Lilac Papillon (tagged pre-order, no size in its copy, shown as US 6) | The stocked size ships now; US 5 to 7 otherwise pre-order |

## Open questions

- Is Trio Bloom Ring (draft) adjustable? Its copy says "an open band", but it is not tagged `Adjustable`.
- Should Whisper Pavé show US 6 or US 6½? What size is Lilac Papillon?
