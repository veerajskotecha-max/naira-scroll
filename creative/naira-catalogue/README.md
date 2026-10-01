# NAIRA PETITE — The Catalogue, Volume One (festive 2026)

A4 portrait, 10 pages. Built from the Higgsfield library (only images checked as faithful to the real
piece), the Shopify plinth photographs and NAIRA's own type, palette and vector wordmark.

| File | Use |
|---|---|
| `naira-petite-catalogue.pdf` | Screen, WhatsApp and email (A4, 210 × 297 mm) |
| `naira-petite-catalogue-PRINT-3mm-bleed.pdf` | Print shop: 216 × 303 mm with 3 mm bleed, TrimBox set to A4, RGB images at up to 300 dpi |

## Pages

1. Cover: Baroque Pearl Lariat, worn
2. About Naira: the house, the Petite promise, materials, the collection at a glance
3. Camp I · The Long Afternoon
4. Camp II · Sage
5. Camp III · Steel & Gold
6. Camp IV · The Red Room
7. Earrings (14) · 8. Rings (12) · 9. Necklaces (7) · 10. Bracelets (5), care and how to order

## Facts used

- All 38 in-stock pieces at their live nairaflore.com prices on 1 October 2026.
- Materials from each product's tags, worded as the founder approved: "18k gold coated" / "rhodium coated"
  (plus one rose gold coated band and the two-tone Heartbead Bracelet).
- Hypoallergenic is on every piece. Tarnish-free and waterproof are on all but three; the Pearl Legacy
  Necklace, Baroque Shell Bracelet and Verdant Drop Earrings are marked "keep dry".
- Contact: nairaflore.com and the WhatsApp number used across the site (+91 95615 57935, Mon–Sat
  10 am–7 pm IST). No email is printed because the site lists three different addresses.

## Rebuild

`build/build.py` writes the HTML (and crops every image to its placed size at 300 dpi);
`build/render.py` prints it to PDF in Chromium and sets metadata. `BLEED=3 python3 build.py` then
`python3 render.py --bleed` makes the print master. The scripts read the working library from the
session scratchpad, so they are kept here for reference.
