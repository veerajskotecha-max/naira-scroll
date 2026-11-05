# The Naira Ten · concept ads (November 2026)

Ten Meta ads for Naira's wedding season. Each one uses a different technique borrowed from award-winning print and outdoor work. Each is built on a piece with 32 to 80 units in stock on 4 November 2026. Every card carries a tab in its collection's colour, so the feed reads as one system.

| Colour | Collection | Link |
|---|---|---|
| Haldi yellow `#F2B705` | Earrings | /collections/earrings |
| Sindoor red `#C1272D` | Rings | /collections/rings |
| Neelam blue `#1D3C8F` | Necklaces | /collections/necklaces |
| Rani pink `#C2185B` | Bracelets | /collections/bracelets |
| Mehendi green `#2F6B3A` | Shop all | /collections/shop-all |

| # | Hook | Technique | Piece · price · stock | Layer |
|---|---|---|---|---|
| A01 | I do. Say it with a ring that adjusts. | Typographic swap: the ring is the O | Cushion Halo Ring · ₹1,099 · 58 | Desire |
| A02 | Repeat the hoops. Not the outfit. | Pop-art repetition, nine function colourways | Woven Gold Hoops · ₹1,199 · 56 | Desire |
| A03 | The Periodic Table of Naira | Information design, colour-coded | Ten pieces · from ₹799 · 121 in stock | Inform |
| A04 | Anatomy of a compliment. | Craft proof as an engineering drawing | Verdant Circlet Studs · ₹1,099 · 80 | Inform |
| A05 | The dance floor is 18 cm long. | Miniature world | Prism Rivière Bracelet · ₹2,399 · 63 | Desire |
| A06 | Pick your shade. | Paint-chip swatches | Baguette Tennis Necklace · ₹2,099 · 69 | Desire |
| A07 | This is 50 cm. | Seamless panorama carousel with a tape | Toggle Link Chain · ₹1,199 · 79 | Inform |
| A08 | Hugs and kisses, on one wrist. | Visual pun on a chalk board | Kiss Knot Bangle · ₹1,199 · 36 | Desire |
| A09 | Two peas in a pod. | Visual idiom with the Buy 2 maths | Verdant Eternity Band · ₹1,099 · 58 | Convert |
| A10 | ₹799. The pair. | Knockout type, price made of the material | Brushed Gold Huggies · ₹799 · 32 | Convert |

## Folders

- `ads/` holds the 22 upload files. Each ad has a 1080×1350 feed card and a 1080×1920 story; A07 has three carousel cards. JPEG 92 with no chroma subsampling. `A07_pano.jpg` is the 3240×1350 source the three cards are cut from.
- `data/deck.json` has every ad's headline, primary text, description, button, UTM link, technique, edit notes and reasoning, plus the campaign plan.
- `sources/` has the six new Higgsfield generations used and the three cut-outs. `prompts.md` lists all twelve prompts of the round, which ones were used, and the library images.
- `sheets/` has review sheets of all feeds and all stories.
- `build/` holds the scripts as run. `kit.py` is the shared renderer (fonts, logo, collection tabs, Chromium screenshots with overflow and story safe-zone checks), `ad01.py` to `ad10.py` build each ad, `pop.py` is the screenprint pipeline for A02, `a9bg.py` extends the A09 story's paper, `deck.py` writes the copy and `gen_page.py` the review page. Paths point at the working scratchpad (fonts, the image library and the stock snapshot).

## Rules kept

- Prices, sizes and materials come from the live listings. The Buy 2 figure on A09 is 2 × ₹1,099 = ₹2,198, less 10% = ₹1,978.
- One product per generated frame, fidelity-checked against the shop photo. One render that invented a halo around a pea was rejected.
- No exclamation marks, no emojis, no invented scarcity. Story text stays inside the 14% to 80% safe zone.
- Links: `https://nairaflore.com/collections/{collection}?utm_source=meta&utm_medium=paid&utm_campaign=naira-ten-nov26&utm_content={id}`.
