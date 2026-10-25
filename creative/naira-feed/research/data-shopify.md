# Naira Petite: Shopify data for the feed (pulled 25 Oct 2026, read-only)

Store "Naira" (nc5eti-gp.myshopify.com, primary domain www.nairaflore.com), Basic plan, INR, IST.
One stock location: Forest Colony, Parijat Nagar (Nashik).
Companion file: `roster.json` (117 ACTIVE Naira Petite pieces, every field the feed needs, incl. all image URLs with
alt text and a shot-type tag per image). `roster-all-incl-drafts.json` adds the 31 drafts (148 total).

## Sources and their limits
- Products: Admin GraphQL, every product with vendor `Naira Petite` (148: 117 ACTIVE, 31 DRAFT). Live prices are as of today.
- Sales 120 days: ShopifyQL `FROM sales` (window 27 Jun to 25 Oct). No orders exist before August: the jewellery line went live in early Aug 2026, so "120 days" is really ~11 weeks.
- Orders detail: Admin GraphQL `orders`. The app can only see the last 60 days (27 Aug to 25 Oct, 131 orders, 2 cancelled). Payment mix, items per order, cities, timing and repeat buyers come from these 129 live orders.
- Market scores: the owner's "Naira Market Index" artifact (rated 21 Oct vs GIVA IXIA + Palmonas steel), merged into roster as `market_score_21oct`, `market_closest_twin`, `market_why`.
- Units/revenue fields in roster: `units_120d` + `revenue_120d` = ShopifyQL net items and net sales (ex-tax, after discounts and returns). `units_60d_orders` + `revenue_60d_orders_incl_tax` = from order line items.

## Headline numbers
| Metric | Value |
|---|---|
| Orders, 120d (ShopifyQL) | 141 (Aug 26, Sep 58, Oct 57 to date) |
| Total sales, 120d | Rs 4,06,565 (incl. Rs 88,461 of 5 custom/offline "rakhi sale"/draft line items that are not catalogue jewellery) |
| Net items sold, 120d | 207 |
| Jewellery-only AOV (60d, 124 orders, incl. tax + shipping) | mean Rs 2,304, median Rs 1,926 |
| Items per order | 1.50; 69% of orders are a single piece (86 of 124); 2 pieces 21; 3 pieces 14 |
| Payment (online orders, n=120) | COD 57.5% (69), prepaid Razorpay 42.5% (51). Plus 4 offline cash/manual |
| Discount codes used (124 orders) | none 75; NAIRA10 14; FRIENDSANDFAMILY 13; BUY2 13; BUY3 9 |
| Repeat buyers | ShopifyQL 120d: 118 customers, returning-customer rate 5.1% (6). 60d: 111 unique customers, 4 ordered twice in-window |
| Returns | Rs 13,548 reversed over 120d (~3.6% of gross) |
| Pace since Edition Two launch (16 Oct) | 37 orders in ~9.5 days (~3.9/day) vs ~1.5/day before |

### Where buyers are (60d, shipping city)
Mumbai 23 (+2 Mumbai Suburban) · Nashik 24 (21 + 3 spelled "Nasik"); 120d ShopifyQL: Mumbai 25, Nashik 29 · Pune 8 · Bengaluru 11 · Delhi NCR ~19 (South, South West, Central, West, New Delhi, Gurugram, Gautam Buddha Nagar) · Chennai 6 · Hyderabad + Ranga Reddy + Medchal ~7 · Ahmedabad 2 · Indore 2.
By state: Maharashtra 59 of 129 (46%), Delhi 15, Karnataka 14, Tamil Nadu 9, Telangana 8, UP 5, Haryana 4.
Read: a Mumbai + Nashik home base (Nashik is the studio's own city) plus metro India. Copy can be pan-Indian; Marathi/Mumbai references land with ~half the buyers.

### When they buy (IST)
- Day: Sunday is the biggest day by far (38 of 129 in 60d; ShopifyQL 120d also 38 of 141, ~27%). Then Friday/Thursday. Wednesday and Monday are weakest.
- Hour: 12:00 to 21:00 carries 78%. Peaks at 18:00 (17 orders), 21:00 (12) and 12:00 (13).
- Posting window suggestion: Sun noon or Fri/Sun 18:00 to 21:00.
- Spikes: 20 Oct had 10 orders (largest day); 18 to 25 Oct ran 3 to 5/day after the Edition Two drop.

## Bestsellers
120 days (ShopifyQL net units, net sales ex-tax):
| # | Piece | Units | Net sales | Live price | Stock | Market score |
|---|---|---|---|---|---|---|
| 1 | Woven Gold Hoops | 20 | Rs 25,694 | 1,299 (MRP 2,769) | 63 | 9 |
| 2 | Prism Rivière Bracelet | 14 | Rs 27,649 (top by revenue) | 2,399 (MRP 4,200) | 67 | 9 |
| 3 | Baguette Tennis Bracelet (Ed. Two, launched 16 Oct) | 13 | Rs 17,710 | 1,699 | 57 | 8 |
| 4 | Heartbead Bracelet | 11 | Rs 11,930 | 1,299 | 25 | 9 |
| 5 | Molten Bloom Hoops | 9 | Rs 8,814 | 1,300 | **0, sold out** | 9 |
| 6 | Roman Numeral Trio Ring (Ed. Two) | 8 | Rs 12,714 | 1,899 (MRP 3,500) | **3 left, one per size 6/7/8** | n/a |
| 7 | Brushed Gold Huggies | 8 | Rs 8,913 | 999 (MRP 1,799) | 35 | 9 |
| 8 | Cushion Halo Ring (silver) | 6 | Rs 5,536 | 1,199 | 60 | 7 |
| 9 | First Light Set | 5 | Rs 4,913 | 1,199 | **0** | 8 |
| 10 | Serpentine Whisper Chain | 5 | Rs 6,998 | 1,299 | 20 | 7 |
| 10 | Toggle Link Chain | 5 | Rs 7,538 | 1,299 | 79 | n/a |
| 10 | Bold Nocturne Bracelet | 5 | Rs 6,132 | 1,599 | 49 | 7 |
| 10 | Baguette Huggies (Ed. Two) | 5 | Rs 4,268 | 1,199 | 57 | 7 |
Then 4 each: Lumière Oval Bracelet, Rivière of Light Bracelet (sold out), Blush Station Bracelet (sold out), Pearl Reverie Bracelet, Charm Box Chain, Baguette Eternity Band, Lumière Oval Necklace (sold out), Rose Verdant Band (1 left).

Last 30 days (orders): Prism Rivière 13, Woven Gold Hoops 13, Baguette Tennis Bracelet 13, Roman Numeral Trio Ring 8.
Since 16 Oct: Baguette Tennis Bracelet 13 (Ruby 8, Emerald 4, Crystal 1) and Roman Numeral Trio Ring 8 lead. **Ruby is the hero stone colour** (Baguette Huggies also sold Ruby 3 of 3 in orders; Baguette Eternity Band Ruby).
By category (120d): Bracelets 68 units / Rs 88.6k; Earrings 63 / Rs 75.8k; Rings 38 / Rs 43.6k; Necklaces 28 / Rs 40.0k; Set 5.

Bought together (multi-piece orders): Woven Gold Hoops + Brushed Gold Huggies; Woven + Molten Bloom Hoops; Baguette Tennis Bracelet + Baguette Huggies; Baguette Eternity Band + Baguette Huggies; Lumière Oval Necklace + Bracelet; Baroque Pearl Lariat + Pearl Reverie Bracelet; Charm Box Chain + Heartbead Bracelet; full Bold Nocturne trio (chain + bracelet + drops) in one BUY3 order (#1134).

## Hero candidates (sell AND photograph well)
Visual check done on 16 pieces' Shopify images (contact sheets in `raw/thumbs_sheet_0.jpg`, `_1.jpg`). House look of the library: warm cream limewash plaster plinth on a peach/beige sweep; on-model crops of one South-Asian model in a mustard/ochre satin camisole, face cropped at the lips; tight macros. A few editorial frames: Prism Rivière on navy velvet and on oxblood with water drops; Woven Gold Hoops on oxblood with "NAIRA" wordmark; Heartbead on a burgundy roll and on sage. Files named `hf_…` (and most on-model shots) are Higgsfield AI generations, not a real shoot. No pure-white packshots: cut-outs need background removal from the cream plinth (low contrast with gold; doable but needs care on fine chain).
1. **Woven Gold Hoops**: #1 by units, 9/10 market score, 63 in stock, braided texture reads at thumbnail size. Images: plinth, oxblood "NAIRA" editorial, on-ear (2).
2. **Prism Rivière Bracelet**: #1 by revenue, 67 in stock, pastel multi-stone = the most colourful piece in the range (pink, mint, lemon, aqua, lilac), strongest graphic potential. 9 images incl. navy velvet + oxblood editorials.
3. **Baguette Tennis Bracelet + Baguette Tennis Necklace + Baguette Huggies + Baguette Eternity Band**: the Edition Two baguette family in Ruby / Emerald / Crystal (+ Amethyst on huggies and band). Best-photographed set in the store: 12 + 11 + 8 + 7 images, every stone colour on the plinth and on model, wrist+neck sets. Necklace has 70 in stock, 0 sold yet: the obvious "complete the set" push.
4. **Heartbead Bracelet**: grey pearls + puffed gold heart on a toggle; 9/10; Palmonas twins sold out. Strong gifting story.
5. **Brushed Gold Huggies**: Rs 999 entry piece, 9/10, chunky satin dome.
6. **Roman Numeral Trio Ring**: tri-tone stacked ring, 8 sold in 9 days, but only 3 units left (one each in 6/7/8). Feature only with care (scarcity is real; do not drive traffic it cannot fulfil).
7. **Bold Nocturne trio (chain 53, bracelet 49, drops 19)**: chunky paperclip with one pavé link; strong macro; deep stock; already bought as a set.
8. **Silk Mesh Cuff / Kiss Knot Bangle** (40 each, gold + silver), **Toggle Link Chain** (79): deep stock, good on-model and macro, few sales so far: content can move them.
9. **Birthstone Heart Necklace** (Rs 699, 12 months, 12 colour stills): perfect for a "find your month" carousel, but only 1 unit per month in stock.

## Deep stock (20+ units, safe to push)
toggle-link-chain 79, baguette-tennis-necklace 70, prism-riviere-bracelet 67, woven-gold-hoops 63, cushion-halo-ring 60, verdant-eternity-band 60, baguette-tennis-bracelet 57, baguette-huggies 57, bold-nocturne-chain 53, bold-nocturne-bracelet 49, halo-curve-ring 45, marquise-layering-set 40, silk-mesh-cuff 40, kiss-knot-bangle 40, brushed-gold-huggies 35, ribbon-bead-bracelet 34, riviere-eternal-bracelet 34, baguette-eternity-band 30 (but 1 to 3 per stone/size), KAVNAR Edition One pre-order pieces 17 to 30 each, heartbead-bracelet 25, baroque-shell-bracelet 23, serpentine-whisper-chain-silver 23, linked-trio-ring 22, chain-drop-dome-ring 22, Edition Two pieces at 20 (serpentine, charm box, coil bangle, marquise coil cuff, droplet ring + cuff, north star bangle, mint pear drops, duo link bracelet, fine tennis, petal flower studs, marquise drop choker, emerald square ear cuff).
Note the site's `DEEP_STOCK` list in `src/lib/pairings.ts` (18 Oct counts) still matches closely; it omits rings by design.

## Sold out / nearly gone (do NOT feature as shoppable)
Sold out (ACTIVE, 0 stock): Molten Bloom Hoops, Blush Station Bracelet, First Light Set, Lumière Oval Necklace, Baroque Pearl Lariat, Rivière of Light Bracelet, Solitaire Whisper Studs, Rivière Eternal Necklace, Petite Pearl Chain, Triple Dawn Cuff, Baroque Bloom Cuff, Clover Charm Necklace.
1 to 3 left: Roman Numeral Trio Ring 3, Rose Verdant Band 1, Baguette Arc Hoops 1, Teardrop Lariat 1, Pearl Point Studs 2, Twin Heart Necklace 1, Twin Heart Studs 1, Clover Trio Edit 3, Filigree Bloom Studs 3, Pearl Reverie Bracelet 3, Textured Gold Hoops 3, Verdant Drop Earrings 3, Blush Cluster Ring 3, Whisper Pavé Band 3.
Several of these (Molten Bloom, First Light, Lumière Oval Necklace, Baroque Pearl Lariat) appeared in the earlier Sept/Oct grids and ads; avoid re-using them.

## Edition Two (tag `Edition Two`, created 16 Oct): 33 active pieces
Baguette Tennis Bracelet 1,699 (Crystal 29 / Ruby 12 / Emerald 16 in stock) · Baguette Tennis Necklace 2,300 (Ruby 20 / Crystal 30 / Emerald 20) · Baguette Huggies 1,199 (Ruby/Crystal/Emerald/Amethyst) · Baguette Eternity Band 1,299 (Ruby/Emerald/Amethyst x US 5 to 8) · Crystal Baguette Eternity Ring 1,299 · Roman Numeral Trio Ring 1,899 · Watch Link Ring 1,199 · Linked Pair Ring 1,399 · Chain Drop Dome Ring 1,199 · Mesh Band Ring 699 · Droplet Open Ring 1,299 (adjustable) · Silk Mesh Cuff 1,499 · Kiss Knot Bangle 1,199 · Triple Coil Wrap Bangle 1,499 (gold and silver both 1,499 today; CLAUDE.md's 1,899/1,799 is stale) · Marquise Coil Cuff 1,499 · North Star Bangle 999 · Tile Stone Bangle 999 · Garnet Cable Cuff 1,399 · Pear Point Open Cuff 1,499 · Droplet Open Cuff 1,599 · Duo Link Necklace 1,299 · Duo Link Bracelet 999 · Fine Tennis Bracelet 1,299 · Marquise Drop Choker 1,199 · Birthstone Heart Necklace 699 (12 months) · Bold Nocturne Drops 1,299 · Mint Pear Drop Earrings 1,199 · Petal Flower Studs 999 · Emerald Halo C-Hoops 1,199 · Emerald Deco Hoops 1,249 · Emerald Square Ear Cuff 999 · Crystal Pear Ear Cuff 999 · Pearl Nugget Hoops 1,099.
Draft: Tubogas Dome Ring (21 units, draft).
Edition Two is the season's story: metal choice (gold + silver on 12 pieces), stone colour (ruby/emerald/amethyst/crystal), and the first real bangle/cuff range.

## KAVNAR Edition One (tags `KAVNAR`, `Edition One`, `pre-order`, created 18 Sep): 14 active
Bold Dome Huggies 999 · Quatrefoil Éclat Studs 1,299 · Verdant Cushion Studs 1,199 · Baguette Halo Drops 1,499 · Torsade Huggies 1,299 · Petite Square Huggies 999 · Pearl Circlet Studs 1,899 · Petite Bow Studs 1,099 · Rivière Hoops Silver 1,499 · Torsade Pearl Cuff 1,399 · Molten Panel Bracelet 1,299 · Prism Cluster Studs 1,499 · Aqua Heart Drops 1,499 · Lilac Papillon Ring 1,299. Drafts: Rivière Eternal Bracelet (KAVNAR copy), Deco Ribbon Hoops, Pearl Crossover Ring.
Caveats: these carry NO material tags (no "18k Gold Tone Plated"/"Hypoallergenic"), so do not state material for them without checking the listing. The site never one-tap-adds pre-order pieces; pre-orders are booked on WhatsApp. Only Torsade Huggies has sold (1). Stock reads 17 to 30 each even though they are tagged pre-order: confirm with the owner whether they are physically in hand before calling them "in stock" or "pre-order" on a post.

## New "Aditya" batch (tag `Aditya`, created 24 to 25 Oct, i.e. today/yesterday)
Active (thin stock, 1 to 5 each): Clover Drop Pendant Necklace 875, Clover Drop Earrings 1,015, Clover Chain Bracelet 800, Twin Heart Necklace 999, Twin Heart Studs 910, Bow Pear Drop Necklace 999, Petite Blossom Bracelet 999, Molten Wave Ear Cuff 490, Asscher Solitaire Ring 700 (adj.), Lumière Oval Solitaire Ring 699 (adj.), Pearl Heart Layered Necklace 999, Pavé Zigzag Ring 630 (adj.).
Drafts at price 0 (not yet priced): Clarté Baguette, Sorbet Rivière, Emerald Carré, Rivière Classique, Midnight Rivière, Aquarelle Rivière, Bougainvillea Vine, Lumière Solitaire (all tennis-type bracelets), Prism Pear Drop Necklace + Hoops, plus Clover Station Bracelet, Open Heart Layered Bracelet, Watch Link Bracelet, Cushion Solitaire Ring.
Only 3 images each and odd prices (875, 1,015, 910, 630): these look mid-listing. Not feed-ready; at most a "coming soon" tease. There is an artifact "Aditya Listing Review" updated today.

## Sets / lines with 3+ pieces ("complete the set" posts)
From the site's `LINES` regex (pairings.ts) applied to active pieces:
- **Baguette (8)**: Tennis Bracelet, Tennis Necklace, Huggies, Eternity Band, Crystal Baguette Eternity Ring, Baguette Éclat Bracelet, Baguette Halo Drops (KAVNAR), Baguette Arc Hoops (1 left). Best set in the store: same stones, same three colours, all photographed. Ruby set = bracelet 1,699 + necklace 2,300 + huggies 1,199 = Rs 5,198; BUY3 (20%) brings it to Rs 4,158.
- **Pearl (15)**: Heartbead (pearl tag), Baroque Shell Bracelet, Pearl Circlet Studs, Torsade Pearl Cuff, Pearl Legacy Necklace, Pearl Blossom Earrings, Pearl Ribbon Ring, Pearl Nugget Hoops, Pearl Drop Studs, Pearl Point Studs (2), Filigree Bloom Studs (3), Pearl Reverie Bracelet (3), Pearl Heart Layered Necklace (3). Pearl motif is near-neutral in the market (lift ~0.9 to 1.0).
- **Verdant / emerald (8)**: Verdant Eternity Band (60 in stock), Emerald Halo C-Hoops, Verdant Cushion Studs, Emerald Square Ear Cuff, Emerald Deco Hoops, Verdant Circlet Studs, Verdant Drop Earrings (3), Rose Verdant Band (1). Green over-indexes at Palmonas (lift 1.67) and IXIA (1.5).
- **Rivière (5)**: Prism Rivière Bracelet, Rivière Eternal Bracelet, Rivière Hoops Silver; (Rivière of Light and Eternal Necklace sold out).
- **Whisper (5)**: Serpentine Whisper Chain (gold + silver), Whisper Pavé Band, Chevron Whisper Ring; Solitaire Whisper Studs sold out.
- **Bold Nocturne (3)**: Chain, Bracelet, Drops. All in stock (53/49/19). Already bought as a trio.
- **Marquise (3)**: Layering Set 40, Coil Cuff 20, Drop Choker 20.
- **Molten (3)**: Molten Panel Bracelet (KAVNAR), Molten Wave Ear Cuff (Aditya, 4); Molten Bloom Hoops sold out.
- **Lumière (3)**: Oval Bracelet 10, Oval Solitaire Ring 3; necklace sold out.
- 2-piece sets: Duo Link (necklace + bracelet, two-tone), Torsade (huggies + pearl cuff), Droplet (open ring + open cuff), Mesh (cuff + band ring), Prism (bracelet + cluster studs), Blush (bracelet sold out).
- Motif families worth a post: bloom/clover/flower (12), heart (7), link/chain (6), pear drop (6), halo (5), bow/ribbon (5), dome (4), pavé (4), oval (4).

## Price bands (live lead prices, 117 active)
<= Rs 999: 29 · 1,000 to 1,299: 42 · 1,300 to 1,599: 28 · 1,600 to 1,999: 14 · 2,000+: 4 (Prism Rivière 2,399, Baguette Tennis Necklace 2,300, Teardrop Lariat 2,749, Triple Dawn Cuff 2,299 sold out).
Range Rs 490 to 2,749; the core sits at Rs 999 to 1,499, exactly the competitor median (IXIA bestseller median 1,199; Palmonas steel 1,199).
Compare-at "MRP" set on 91 of 117; implied discounts: 40 to 49% on 31 pieces, 50 to 59% on 37, 60%+ on 8, 30 to 39% on 14. 26 pieces have no compare-at (most Edition Two + Aditya).
**IMPORTANT, CLAUDE.md is out of date on price:** it says pieces are Rs 24,000 to 44,000. Live Naira Petite prices are Rs 490 to 2,749. (The Rs 24k to 67k figures belong to the couture/apparel side and custom orders.)
**Prices changed in the last 4 days:** 42 active pieces are cheaper today than in the 21 Oct market index (e.g. Woven Gold Hoops 1,499 to 1,299; Serpentine Whisper 1,849 to 1,299; Verdant Eternity Band 1,899 to 1,099; Halo Curve Ring 2,049 to 1,299; Bold Dome Huggies 1,649 to 999). Orders as late as 20 Oct were charged the old prices. Any price on a post must come from `roster.json` (today), and should be re-checked on posting day.

## Offers to reference (from src/lib/promo.ts, all live codes)
- Buy 2 = 10% off (BUY2, applied automatically in the bag), Buy 3 = 20% off (BUY3). Single code only, nothing stacks.
- NAIRA10 = 10% off anything, typed, any customer (the announcement bar carries it).
- FRIENDSANDFAMILY 20% exists (13 uses) but is not a public offer: keep it off posts.
- COD available; COD fee shown in the bag (5% of post-discount total, waived if prepaid). Delivery promise on site: 3 to 5 working days. Gift box (blush box with black velvet bed) ships with every piece.

## Gift-friendly pieces (no sizing, in stock 5+, not pre-order): 48
Top by sales: Woven Gold Hoops, Prism Rivière Bracelet, Baguette Tennis Bracelet, Heartbead Bracelet, Brushed Gold Huggies, Toggle Link Chain, Baguette Huggies, Bold Nocturne Bracelet, Serpentine Whisper Chain, Charm Box Chain, Lumière Oval Bracelet, Ribbon Bead Bracelet (799), Bold Nocturne Chain, Baroque Shell Bracelet, Duo Link Necklace, Marquise Layering Set, Rivière Eternal Bracelet, Serpentine Whisper Silver, Garnet Cable Cuff, Pear Point Open Cuff, Bold Nocturne Drops, Baguette Éclat, Emerald Halo C-Hoops, Baguette Tennis Necklace, Silk Mesh Cuff, Kiss Knot Bangle, Triple Coil Wrap Bangle, Marquise Coil Cuff, Droplet Open Ring (adjustable), North Star Bangle.
Under Rs 1,000 gifting shelf: Brushed Gold Huggies 999, Ribbon Bead Bracelet 799, North Star Bangle 999, Duo Link Bracelet 999, Petal Flower Studs 999, Emerald Square Ear Cuff 999, Crystal Pear Ear Cuff 999, Tile Stone Bangle 999, Birthstone Heart Necklace 699, Pearl Reverie Bracelet 899 (3 left).
Rings need a size (US 5 to 8) except adjustable/open ones (Droplet Open Ring, Aditya solitaires).

## Market context (from the owner's Market Index, 21 Oct)
- Naira 9/10 pieces: Woven Gold Hoops, Prism Rivière Bracelet, Molten Bloom Hoops (sold out), Heartbead Bracelet, Brushed Gold Huggies. 8/10: Baguette Tennis Bracelet, Fine Tennis Bracelet, Lumière Oval Bracelet, Charm Box Chain, Golden Duet Ring, Petite Pavé Band, Birthstone Heart Necklace, Pearl Reverie, First Light Set, Baroque Pearl Lariat, Rivière of Light.
- Motifs that over-index among competitor bestsellers (lift = share of bestsellers / share of range): tennis/rivière (IXIA 4.5x), bangle (IXIA 3.9x, Palmonas 1.9x), ruby/red (IXIA 3.9x), clover (IXIA 9x, tiny base; Palmonas 2.5x), snake/herringbone (IXIA 3x), paperclip (2.6x), pear/teardrop (2.25x), chain/link (1.6x), charm (1.25 to 1.7x), layered (1.4 to 1.8x), twist/rope (1.4 to 1.6x), huggie (1.6x), emerald/green (1.5 to 1.7x), choker (2 to 3x). Under-index: cuff (0.4x), initial/name (0.05 to 0.5x), geometric, enamel, mesh.
- Competitor voice is discount-led ("Buy 1 Get 2 Free", "Festive Sale: Buy 2 Get 1 Free"); Palmonas steel is 42% sold-out across the range.

## Notable / risks for the creative team
1. Material claims: use the listing words "18k gold tone plated" / "rhodium plated" (or the site box copy "18K gold tone & rhodium plated"). Never "18k gold", "gold", "silver" (as metal), "sterling", "handmade" or "artisan-made" for Petite: pieces are 18k gold-tone PVD over surgical stainless steel with CZ, sourced from Yiwu J&D, KAVNAR and Foshan Yiss Fera (see data-drive-notion.md). Pearls are shell/imitation pearl; one piece is mother-of-pearl ("polished shell, not a pearl"). The prior 12-tile caption doc used "18k gold-coated".
2. Tags claim "Waterproof", "Tarnish Free", "Hypoallergenic" on most core and Edition Two pieces (not on KAVNAR or Aditya pieces, and not on Garnet Cable Cuff, Tile Stone Bangle, Pearl Nugget Hoops, Emerald Halo C-Hoops, Emerald Deco Hoops, Birthstone Heart Necklace, Pearl Legacy, Baroque Shell). Only state these per-piece where the tag exists.
3. The "Last 24 hours: N pieces sold" strip on the PDP is a hash, not data (CLAUDE.md). Never quote it. Real numbers above are safe to paraphrase but small (e.g. "13 sold in 9 days" is true for Baguette Tennis Bracelet).
4. Do not lead with Roman Numeral Trio Ring, Rose Verdant Band, or anything in the sold-out list.
5. On-model imagery is largely AI-generated (Higgsfield) of a consistent model in an ochre camisole; it gives a coherent "Naira girl" but is not a real person.
6. Order tags show Fastrr/Shiprocket checkout with RTO prediction; COD is the majority: prepaid nudges ("COD fee waived if you pay online") are commercially useful.
7. Product types: 38 earrings, 29 bracelets, 26 rings, 23 necklaces, 1 set. Metals: 72 gold-only, 16 silver-only, 12 offered in both, 4 two/tri-tone, 1 rose-gold, 11 untagged (KAVNAR).
