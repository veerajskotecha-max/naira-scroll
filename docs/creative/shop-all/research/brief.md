# Naira · Shop All campaign brief (4 Nov 2026)

## The job
One Meta campaign that sends people to **all of Naira's jewellery**, not one product: the Shop All page.
Budget ₹1,000 a day. The founder wants 40 creatives made (20 concepts, each a Feed and a Story), edited down to the best 10 to run.
They must be eye-catching ("crazy"), on brand, and honest. They are built ONLY from existing, approved Naira photos (the pool),
because there are no image credits. Layout, type, graphics, cut-outs and crops are allowed; repainting a product is not.

## Naira
Indian demi-fine jewellery: gold-tone and silver-tone pieces set with cubic zirconia, ₹599 to ₹2,399, for urban Indian women
(20-40) who buy for themselves and for the women around them. It talks like a sharp friend, not a showroom: short, exact, warm,
a little wry. It names real Indian things (anaar, rangoli, pheni, a potli, Mummy's saree) instead of adjectives. Never shouts:
no exclamation marks, no ALL-CAPS screaming except a single short word, no "SALE SALE".

## Facts you may use (all verified on 4 Nov 2026)
- Shop All page: https://nairaflore.com/jewellery ("All pieces"); /shop and /collections/all redirect there.
- **135 jewellery pieces in stock**, priced **₹599 to ₹2,399**. Say "130+ pieces" and "from ₹599" (stock moves).
- Filters on the page: Rings, Bracelets, Earrings, Necklaces; Under ₹999, ₹999-1,499, ₹1,500+.
- **Buy 2, get 10% off. Buy 3, get 20% off.** The site banner says "BUY 2 GET 10% OFF · BUY 3 GET 20% OFF"; the bag applies it (say "applied in your bag"; do not mention codes).
- **Free insured shipping. Delivery in 3-5 working days. 7-day returns.** Cash on delivery on serviceable pincodes. Every piece arrives in the Naira gift box.
- "Most loved" on the site: Prism Rivière Bracelet, Woven Gold Hoops, Bold Nocturne Chain.
- Our own Meta data: the pieces/photos in the pool are the account's most-clicked ads (see pool.json "proof"). It is true to say "our most-clicked pieces" for the pool heroes.
- Prices per product are in pool.json. Use them exactly (₹ sign, Indian comma: ₹1,199).

## Never say / never show
- Never: real, diamond, gold (as a material - always "gold tone"), silver (always "silver tone"), waterproof, tarnish-free, anti-tarnish, tarnish, freshwater, hypoallergenic, stunning, elevate, must-have, luxury, "limited time", fake urgency, fake scarcity, fake reviews, fake follower/order counts, percent-off against compare-at prices, any competitor's name.
- Pearls are "shell pearl". Stones are "cubic zirconia" (or just the colour: ruby red, emerald green).
- Never show: anything that imitates a real brand or a real document (receipt, Aadhaar, bank SMS), fake UI of a real app with real logos, fake comments, religious objects, food being eaten.
- Never change the jewellery in a photo (no recolouring, no repainting, no warping). Crops and cut-outs are fine.

## What wins for Naira (Meta, lifetime)
1. A familiar Indian thing in the stone's colour, named and turned: "Rangoli, in a line." 6.10%, "Almost edible." 6.21%, "Anaar, pre-peeled." 5.49% (15 sales, 3.63x).
2. Craft truths as "X, not Y": "Poured, not made." 7.25%, "Woven, not cast." 5.81%.
3. One piece, one ground, lots of air. Stories beat Feeds every time the same picture ran both ways.
4. The best seller had NO words on the picture: the picture sells, the line earns the stop.
5. The best converters by purchases are catalogue carousels of the on-model listing photos (Bestsellers 5.45% CTR, 33 purchases, 2.72x; Edition Two 4.37%, 41 purchases, 2.60x). So "show many pieces, on her" works for a Shop All.
6. Generic occasion lines ("RSVP: yes.", "Plans tonight?") stayed under 2.2%. Lines that could sell anything sell nothing.
7. Research: lo-fi / meme / platform-native statics fail least; comparison-vs-rival fails most; discount hooks are saturated in India (so the offer belongs low in the hierarchy or as the twist, not the headline shout).

## Formats
- Feed 1080x1350 (4:5). Margins at least 60 px. Text must be legible at phone size (smallest text 26 px, body 30+).
- Story 1080x1920 (9:16). ALL text and the logo between y=270 and y=1500 (the top bar and the bottom CTA/reply bar cover the rest). The photo may run full bleed.
- Meta adds its own "Shop now" button under Feed ads and on Stories, so an on-image CTA is optional; if used keep it small.
- Keep overlay text under about 20% of the area unless the format itself is text (a post, a note, a list).

## Kit (`kit/`)
- `kit.css`: fonts (Velista brand serif caps, Cormorant Garamond regular/italic as CG/CGI, Jost tracked caps, Inter, Kalam and Caveat handwriting, Anton, Permanent Marker as Marker, Old Standard as OldStd/OldStdI) and colour tokens (--ink #1A1614, --paper #FBF8F3, --cream, --gold #9A6B2F, --sage #99B4AE, --blush, --marker red). Link it with `<link rel="stylesheet" href="file:///…/shopall/kit/kit.css">` and use `<body class="feed">` or `<body class="story">`.
- Logos (1200x268 PNG, transparent): `logo_ink.png` (dark, for light grounds), `logo_white.png`, `logo_sage.png`. Use width 220-320 px. Always show the NAIRA logo once.
- Render: write a jobs JSON `[{"html":"/abs/path.html","out":"/abs/path.jpg","w":1080,"h":1350}]` and run `node /…/shopall/kit/render.cjs jobs.json`. Image paths in HTML must be absolute `file://` URLs.
- Look at every render with the Read tool before you call it done.
