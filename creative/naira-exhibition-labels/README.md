# NAIRA PETITE — flat-price labels for the exhibition table

There are two A4 print files with the same four sheets:

| Page | Sheet |
|---|---|
| 1 | FLAT ₹999 in light sage |
| 2 | FLAT ₹999 in light blush |
| 3 | FLAT ₹1,299 in light sage |
| 4 | FLAT ₹1,299 in light blush |

Print whichever pages you need, as many times as you need.

| File | Labels per sheet |
|---|---|
| `naira-flat-price-labels-horizontal-A4.pdf` | All horizontal, 14 per sheet: one table sign 198 × 90 mm, four tray strips 99 × 50 mm, nine small strips 66 × 31.7 mm |
| `naira-flat-price-labels-mixed-A4.pdf` | Horizontal and square, 9 per sheet: one table sign 198 × 90 mm, two squares 99 × 99 mm (fit a 4 inch square acrylic stand), two tray strips 102 × 48 mm, four minis 48 × 48 mm |

Where each label goes:
- **Table sign:** at the front of the table.
- **Tray strips:** at the front edge of a tray.
- **Small strips and minis:** on small trays, ring boxes and the bracelet bars.

The table sign carries the logo, DEMI-FINE JEWELLERY and nairaflore.com, then FLAT, the price and "any piece here."

## Printing

- Print at **100 % / Actual size**, not "Fit to page", so the sizes stay true.
- Use A4 card (250 to 300 gsm, matt or silk). Any print shop can run it on a digital press.
- Labels sit edge to edge and share cut lines. Cut along the fine hairlines with a ruler and craft knife, or a paper trimmer, full-width cuts first.
- The colour runs 3 mm past the outer cut line, so a cut slightly off the line never leaves a white edge.
- Each label has its own fine inner frame.

## Design

- Light grounds from the house palette:
  - light sage #CFDFD9;
  - light blush #F9E1D8;
  - deep sage type #3F5B52.
- The NAIRA logo is in sage (#4A6A60), with its flower in coral.
- The price is set in Velista, the face of the PETITE masthead on the catalogue. Velista has no rupee sign, so the ₹ comes from Laila Light. It was chosen from seven serif fonts with a ₹ because it matches Velista's thin–thick contrast.
- FLAT is set in tracked Jost, and "any piece here." in Cormorant italic.
- All fonts are embedded, and there are no exclamation marks.
- An automatic check confirms that every word and logo sits at least 1.2 mm inside its label's frame.

The first version (deep sage and blush, ₹999 and ₹1,199) is in the history at commit 85cb8b9.

`build/build.py` writes both files with Chromium. It reads the fonts from the session scratchpad and the logo from
`creative/naira-bag/build/assets/naira-logo-vector.json`.
