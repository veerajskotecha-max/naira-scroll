# Ring sizes, 26 Oct 2026

The owner, 26 Oct: some adjustable rings showed only pre-order on the site. Every adjustable ring fits US 5 to 9. Make every ring's sizes and stock read correctly on the site and in Shopify.

## Why the site showed pre-order

The live site's list of adjustable rings held 10 handles. Asscher Solitaire, Lumière Oval Solitaire and Pavé Zigzag (live), and Cushion Solitaire (draft), were missing from it. Their pages therefore offered US 5, 6 and 7, and sold US 5 and 7 as pre-orders. The rings on the list offered US 5 to 8, and Cushion Halo offered US 5 to 7.

A closed ring's page opens on "US 6 is in stock". Chevron Whisper and Pearl Ribbon's copy said a fixed US 7, but the owner has since said (26 Oct) that they and Whisper Pavé are US 6, and another session changed their copy on Shopify and `main` (`7fa32e5`). So US 6 is right for every closed ring.

## Shopify (done and verified)

- **Tags.** All 15 adjustable rings are tagged `Adjustable`: the 13 live ones, plus Cushion Solitaire and Duet of Dawn, which are drafts.
- **Descriptions.** Each says "US 5 to 9" in the intro and on the Size line, and links its size guide at the new `?v`. Duet of Dawn's "a little play in the fit" became "adjusts to fit US 5 to 9", like Golden Duet. `descriptions.json` keeps the old and new HTML of all 15 for a rollback. The 13 live descriptions read back exactly through the Storefront API, and the 2 drafts through the Admin API.
- **Size guides.** 14 cards were replaced in place, with the same file ids, at `?v=1793001915` (Asscher `?v=1793001916`). The US 8 and US 9 chips are filled and the foot line reads 5 to 9. Duet of Dawn has no card.
- **Stock.** Every ring is tracked and stops selling at zero. An adjustable ring is one stock: the size the shopper picks rides on the order as a note. On 26 Oct: Cushion Halo 60, Verdant Eternity 60, Halo Curve 45, Droplet Open 10 + 10, Golden Duet 9, Pavé Zigzag 9, Asscher Solitaire and Lumière Oval 8 each (the owner added 5 to each that afternoon), and 1 to 5 each for the rest.
- **Photos.** A photo that shows the back of the band now shows it open: the Asscher hero and the Pavé Zigzag hero and macro were patched, and Lumière Oval has a new upright hero (`../aditya-jewellery/README.md`, "26 Oct: the adjustable rings show their open back"). The house rings already showed theirs: Cushion Halo, Rose Verdant, Granule Dome, Pavé Dome, Petite Pavé, Verdant Eternity and Droplet Open. Blush Cluster and the two toi et moi duets open at the front by design.

## Storefront

Another session put the adjustable-ring fix on `main` as `4426bfd`. A ring is adjustable when it is on the list or Shopify tags it `Adjustable`, and every adjustable ring offers US 5 to 9.

Branch `claude/higgfield-12-angles-4j09gn` (`9b062d7`, last merged with `main` in `f2c3317`) merges that and adds:

- The jewellery page FAQ, which said every ring is US 5 to 7. It now says adjustable rings fit US 5 to 9 and ship in every size, rings sold in sizes show their stock, and a closed ring is US 6 with US 5 and 7 on pre-order.
- The older detail page (`JewelDetail.tsx`) offers adjustable rings in US 5 to 9.
- 56px size chips, so five sizes sit on one row on a 360px phone.
- SEO ring pages updated to US 5 to 9.
- A regenerated catalogue snapshot.

Publish in Lovable puts `main` live. Lovable's sync branches are all inside `main`, so it is following `main`. The branch's extras need a merge to `main` first.

## Every live ring

| Kind | Rings | The page shows |
|---|---|---|
| Adjustable (14) | Asscher Solitaire, Blush Cluster, Cushion Halo, Cushion Solitaire (live from 26 Oct afternoon), Droplet Open, Golden Duet, Granule Dome, Halo Curve, Lumière Oval Solitaire, Pavé Zigzag, Petite Pavé, Rose Verdant, Pavé Dome (`silver-dome-ring`), Verdant Eternity | US 5 to 9, every size ships now |
| Sold in sizes (8) | Baguette Eternity, Chain Drop Dome, Crystal Baguette Eternity, Linked Pair (`linked-trio-ring`), Mesh Band, Star Point, Watch Link (US 5 to 8); Roman Numeral Trio (US 6 to 9, US 8 sold out) | Shopify's own size variants and stock |
| Closed, one size (5) | Chevron Whisper, Pearl Ribbon, Whisper Pavé and Vintage Halo (US 6, the owner, 26 Oct); Lilac Papillon (tagged pre-order, no size in its copy, shown as US 6) | US 6 ships now; US 5 and 7 are pre-orders |

## Open questions

- Is Trio Bloom Ring (draft) adjustable? Its copy says "an open band", but it is not tagged `Adjustable`.
- What size is Lilac Papillon?
