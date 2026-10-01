# NAIRA PETITE — The Catalogue, three camp editions

The same ten A4 pages as Volume One (cover, About Naira, four camp pages, four price-list pages), made three
times. Each edition takes every photograph from ONE of the Colour Camps shot in Higgsfield, so nothing is
mixed: Apricot, Lilac or Sage. The price list is identical in all three: the 38 in-stock pieces on the same
Shopify plinth photographs, at their nairaflore.com prices on 1 October 2026.

| Edition | World | Cover | Screen | Print (3 mm bleed) |
|---|---|---|---|---|
| Apricot | raw apricot silk, a halved apricot, an almond; gold | Brushed Gold Huggies | `apricot/naira-petite-apricot-edition.pdf` | `apricot/naira-petite-apricot-edition-PRINT-3mm-bleed.pdf` |
| Lilac | deckled lilac paper, lavender, lilac linen; silver | Pearl Blossom Earrings | `lilac/naira-petite-lilac-edition.pdf` | `lilac/naira-petite-lilac-edition-PRINT-3mm-bleed.pdf` |
| Sage | a celadon crackle-glaze dish, sage leaves, sage linen; gold | Granule Dome Ring | `sage/naira-petite-sage-edition.pdf` | `sage/naira-petite-sage-edition-PRINT-3mm-bleed.pdf` |

Each folder also has a one-image preview of all ten pages.

## Pages (all three editions)

1. Cover: the PETITE masthead with the cover piece cut out and laid back over the letters
2. About Naira: same copy as Volume One, with an on-model photograph from the camp
3. Camp · I: the camp itself (a tall on-model hero and two still lifes)
4. Camp · II · Up close: five macro photographs on the camp colour
5. Camp · III: three tall still lifes and one flat lay ("On raw silk", "On paper", "On celadon")
6. Camp · IV: one full-bleed still life with a worn inset ("Stone fruit", "Lavender", "In the dish")
7. Earrings (14) · 8. Rings (12) · 9. Necklaces (7) · 10. Bracelets (5), care and how to order.
   The feature photograph on each of these pages comes from the edition's camp.

## What was checked

- Every camp photograph was compared with the product's Shopify photograph and its written build notes
  before it was used.
- The Lilac camp's Vintage Halo Ring photographs were dropped. They show a large oval stone in a closed
  halo, but the real ring has a small round stone in a knotted halo. The Lilac rings page therefore uses
  the Lilac Hour plate of the Halo Curve Ring (in stock, the same pale lilac).
- The Apricot camp has no ring, so its rings page opens on the Woven Gold Hoops with the fruit.
- On-model Toggle Link Chain alternates that show a plain T-bar were not used. The real clasp is a sailor
  clasp with a bar of stones.
- No font falls back: Velista, Jost, Cormorant and Poppins (for ₹) are embedded throughout.

## Print notes

- 216 × 303 mm with 3 mm bleed, with the TrimBox set to A4. Images are RGB, cropped to their placed size at
  up to 300 dpi and never upscaled.
- The Higgsfield originals are 1856 × 2304 (4:5) and 1536 × 2752 (9:16). Most placements print at or above
  250 dpi. The full-bleed pages (cover, page 06) and the half-page hero on page 03 print at 186 to 197 dpi,
  which is fine for soft photographic grounds at A4.

## Rebuild

`build/build_theme.py` holds the three camps (image ids, crops and copy). `THEME=apricot python3
build_theme.py` writes the HTML, and `python3 render_theme.py apricot` prints the PDF. Add `BLEED=3` and
`--bleed` for the print master. The cover cut-outs use the BiRefNet mattes in `build/mattes/`, made with
`rembg` from the same crop. The scripts read the Higgsfield originals and the product library from the
session scratchpad, so they are kept here for reference.
