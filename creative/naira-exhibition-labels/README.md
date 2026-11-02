# NAIRA PETITE — flat-price labels for the exhibition table

`naira-flat-price-labels-A4.pdf` has two A4 sheets:
- **Page 1:** FLAT ₹999, on deep sage with cream type.
- **Page 2:** FLAT ₹1,199, on blush with deep sage type.

The two colours let shoppers and staff tell the two tables apart at a glance. Print whichever page you need, as many times as you need.

Each sheet holds nine labels in four sizes:

| Label | Size | Per sheet | Use |
|---|---|---|---|
| Table sign | 198 × 90 mm | 1 | front of the table or the tray stack. Logo, DEMI-FINE JEWELLERY and nairaflore.com on the left; FLAT, the price and "any piece here." on the right |
| Square | 99 × 99 mm | 2 | a 4 inch square acrylic stand or a mini easel |
| Tray strip | 102 × 48 mm | 2 | the front edge of a tray |
| Mini square | 48 × 48 mm | 4 | small trays, ring boxes, the bracelet bars |

## Printing

- Print at **100 % / Actual size**, not "Fit to page", so the sizes stay true.
- Use A4 card (250 to 300 gsm, matt or silk). Any print shop can run it on a digital press.
- Labels sit edge to edge and share cut lines. Cut along the fine hairlines with a ruler and craft knife, or a paper trimmer:
  1. Cut the three full-width cuts first.
  2. Then cut the short cuts.
- The colour runs 3 mm past the outer cut line. A cut slightly off the line never leaves a white edge.
- Each label carries its own fine inner frame, so the edge still looks finished by hand.

## Design

- The house palette from the pop-up posters: deep sage #5A766D, blush #F2CFC4, cream #FBF5F0, ink #4A645B.
- The NAIRA logo in its vector form. The flower is blush on sage and coral #C27560 on blush.
- The price is set in Velista, the face of the PETITE masthead on the catalogue. Velista has no rupee sign, so the ₹ comes from Laila Light, chosen from seven serif fonts with a ₹ because it matches Velista's thin–thick contrast.
- FLAT is in tracked Jost, and the line "any piece here." is in Cormorant italic.
- All fonts are embedded. No exclamation marks.
- An automatic check confirms that every word and logo sits at least 1.2 mm inside each label's frame.

`build/build.py` writes the HTML and prints the PDF with Chromium. It reads the fonts from the session scratchpad and
the logo from `creative/naira-bag/build/assets/naira-logo-vector.json`.
