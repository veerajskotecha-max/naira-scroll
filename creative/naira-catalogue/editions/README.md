# NAIRA PETITE — The Catalogue, three camp editions

Sixteen A4 pages, made three times. The camp pages take every photograph from ONE of the Colour Camps shot
in Higgsfield, so nothing is mixed: Apricot, Lilac or Sage. The price list and the index are the same in all
three: every Naira Petite piece in stock on nairaflore.com on 26 October 2026, at that day's prices. That is
94 pieces: 25 earrings, 25 rings, 18 necklaces and 26 bracelets.

Left out: the 14 pieces open for pre-order (they can be ordered but are not in stock) and the 10 that are
sold out.

| Edition | World | Cover | Screen | Print |
|---|---|---|---|---|
| Apricot | raw apricot silk, a halved apricot, an almond; gold | Brushed Gold Huggies | `apricot/naira-petite-apricot-edition.pdf` | `apricot/…-PRINT-3mm-bleed.pdf`, `apricot/…-PRINT-5mm-bleed.pdf` |
| Lilac | deckled lilac paper, lavender, lilac linen; silver | Pearl Blossom Earrings | `lilac/naira-petite-lilac-edition.pdf` | `lilac/…-PRINT-3mm-bleed.pdf`, `lilac/…-PRINT-5mm-bleed.pdf` |
| Sage | a celadon crackle-glaze dish, sage leaves, sage linen; gold | Granule Dome Ring | `sage/naira-petite-sage-edition.pdf` | `sage/…-PRINT-3mm-bleed.pdf`, `sage/…-PRINT-5mm-bleed.pdf` |

Each folder also has a one-image preview of all sixteen pages.

## Pages (all three editions)

1. Cover: the PETITE masthead with the cover piece cut out and laid back over the letters
2. About Naira: the house, the Petite promise and the collection in numbers
3. Camp · I: the camp itself (a tall on-model hero and two still lifes)
4. Camp · II · Up close: five macro photographs on the camp colour
5. Camp · III: three tall still lifes and one flat lay
6. Camp · IV: one full-bleed still life with a worn inset
7–8. Earrings (14 + 11)
9–10. Rings (12 + 13), with the ring size guide
11–12. Necklaces (7 + 11)
13–14. Bracelets (11 + 15), with the care note
15. The index: all 94 pieces by family and price, with keep dry and the page each one is on
16. Back cover: how to order (nairaflore.com, WhatsApp +91 95615 57935), QR code, care, and the date of the prices

Each price-list card shows the Shopify plinth photograph, the name, the coating and stones, keep dry where it
applies, the price, and the sizes, stones or colours the piece comes in. The feature photograph on each family's
opening page comes from the edition's camp.

## What was checked

- In stock means: vendor Naira Petite, at least one variant available, and not tagged pre-order.
- Every claim on a card comes from the listing:
  - the coating, from the Metal option, the tags or the Plating line;
  - the stones, from the tags;
  - waterproof, from the tag (every other piece is marked keep dry);
  - hypoallergenic, from the tag or the description.
- The promise on page 02 gives counts rather than claiming every piece is waterproof or hypoallergenic:
  - waterproof: 71;
  - keep dry: 23;
  - listed as hypoallergenic: 74.
- Ring sizes:
  - 8 rings have a Size option (US 5 to 8, or 6 to 9), shown beside the price.
  - 4 are made in one fixed size, taken from the listing's Details: Vintage Halo Ring US 6, Pearl Ribbon Ring US 7, Chevron Whisper Ring US 7, and Whisper Pavé Band about US 6½ (17 mm).
  - The other 13 are tagged Adjustable.
- "from" appears only where an option changes the price. The Roman Numeral Trio Ring is ₹1,899, and ₹1,900 in US 9.
- Each card uses the product's first Shopify photograph, checked by eye. The Rivière Eternal Bracelet's shop photographs show it worn and on a size card, so its card uses a Higgsfield plinth frame of the same bracelet instead.
- The rings opener's hero is now a 66 mm band (it was 74 mm). The Lilac crop moved down so the Halo Curve Ring's stones stay in frame; the 74 mm crop had cut them.
- Every build runs an automatic check:
  - no card text overflows its box;
  - nothing runs into the folio;
  - every font loads and is embedded (Velista, Jost, Cormorant, and Poppins for ₹).
- The camp photographs are the ones already checked for the earlier editions:
  - the Lilac Vintage Halo Ring plates stay out, as they show the wrong stone;
  - the Apricot rings page opens on the Woven Gold Hoops with the fruit;
  - the plain T-bar Toggle Link Chain alternates stay out.

## Print notes

- The TrimBox is exactly 210 × 297 mm, with a BleedBox 3 or 5 mm all round.
- Chromium rounds a PDF page to whole points, so the page is rounded up: 216.2 × 303.0 mm for 3 mm bleed and 220.1 × 307.3 mm for 5 mm. The extra fraction of a millimetre lies outside the bleed.
- Images are RGB, cropped to their placed size at up to 300 dpi and never upscaled.

## Rebuild

`build/instock/` holds this edition's scripts:

| Script | What it does |
|---|---|
| `fetch.py` | downloads the photographs |
| `library.py` | turns the live Shopify feed into `library.json` (the 94-piece snapshot used here is committed) |
| `build.py` | writes the HTML (`THEME=apricot`, plus `BLEED=3` or `BLEED=5` for print) |
| `render.py <theme> [bleed]` | prints the PDF, sets the boxes and runs the checks |

`build.py` reads the camps (image ids, crops and copy) from `build/build_theme.py`, and the photographs from
the session scratchpad, so the scripts are kept here for reference.

`build_theme.py` and `render_theme.py` built the earlier ten-page edition (38 pieces, prices of 1 October
2026). The cover cut-outs still use the BiRefNet mattes in `build/mattes/`.
