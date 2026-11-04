# The Guest List · Naira wedding-season Meta campaign (November 2026)

One invitation suite, ten ads, three layers. Every card is a wedding function in its dress-code colour, carrying the deepest-stocked piece in its collection and linking to that collection. ₹1,000 a day, campaign budget, launch at 10:10 IST.

| Layer | Ad | Links to | Hero (units in stock on 4 Nov 2026) |
|---|---|---|---|
| Inform | I1 carousel · Every function. One guest list. | Shop All, then one collection per card | 9 tiles, 45 to 80 units each |
| Inform | I2 · Shower in it. Sleep in it. Still gold. | Shop All | Brushed Gold Huggies ₹799 (32) |
| Desire | D1 Mehendi · Greener than the mehendi. | Earrings | Verdant Circlet Studs ₹1,099 (80) |
| Desire | D2 Haldi · Only the haldi washes off. | Earrings | Woven Gold Hoops ₹1,199 (56) |
| Desire | D3 Sangeet · Dress code: all of them. | Bracelets | Prism Rivière Bracelet ₹2,399 (63) |
| Desire | D4 Engagement · Fits every finger at the table. | Rings | Cushion Halo Ring ₹1,099 (58) |
| Desire | D5 Reception · One line of light for the last dance. | Necklaces | Baguette Tennis Necklace ₹2,099 (69) |
| Convert | C1 trio · Any three pieces, 20% off. | Shop All | Studs, chain and tennis bracelet, ₹3,797 → ₹3,038 |
| Convert | C2 RSVP · Arrives before the wedding does. | Necklaces | Toggle Link Chain ₹1,199 (79) |
| Convert | C3 grid · Forty-two pieces under ₹1,000. | Shop All | 9 tiles, 12 to 34 units each |

## Folders

- `ads/` — the 24 upload files: one 1080×1350 feed card and one 1080×1920 story card per ad, plus the five carousel cards. JPEG 92, no chroma subsampling.
- `photos/` — the 14 source photographs behind the photo cards (13 new Higgsfield generations locked to the product photos, plus the library images carried over).
- `data/deck.json` — every ad's copy, links with UTM, hook drafts and files, as it goes into Ads Manager. `data/analysis.json` — the competitor ratings, the Meta account read and the notes kept from the Naira Twenty. `data/stock-4-nov-2026.json` — the Shopify stock sheet the heroes were chosen from.
- `build/spec.py` — the campaign spec: links, offer, colours, the ten ads, the 40 hook drafts, the plan. `build/build.py` — composes the cards with Chromium (needs the fonts in the scratchpad labels folder and the photo library). `build/gen_page.py` — builds the campaign page. `build/prompts.md` — the thirteen image prompts.

## Rules baked into the spec

- A hero piece needs at least 30 units in stock; a tile in a grid or carousel at least 10. The build refuses to run otherwise.
- Prices are the live nairaflore.com prices on the build date. Offer on every card: Buy 2, 10% off · Buy 3, 20% off (codes BUY2 and BUY3).
- Links: `https://nairaflore.com/collections/{shop-all|earrings|rings|necklaces|bracelets}?utm_source=meta&utm_medium=paid&utm_campaign=guest-list-nov26&utm_content={ad id}`.
- No exclamation marks, no emojis, no invented scarcity. One fact per card.

## Rebuild

```
cd build && python3 build.py && python3 gen_page.py
```
