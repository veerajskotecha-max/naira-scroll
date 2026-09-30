# NAIRA — D-cut handle bag, 6 × 9.5 × 2 in

Print files for the NAIRA paper bag: cream ground, the website's watercolour leaves as a quiet
repeat, coral tulips in the corners of both faces, the wordmark in its own sage and blush, the
line "[ 18k gold coated · rhodium coated ]", and a QR to nairaflore.com/jewellery on the back.

## Files

| file | use |
|---|---|
| `print/Naira-DCut-Bag-6x9.5x2-EDITABLE.pdf` | send to the manufacturer. Layered vector PDF, live text, page 2 is the print spec |
| `print/Naira-DCut-Bag-6x9.5x2-PRINT-READY.pdf` | same artwork, text converted to outlines (no fonts needed), dieline switched off |
| `print/Naira-Bag-FULL-SHEET-17x11.45in.jpg` | one-file upload for the Kraftix online editor (tap Fit to design) |
| `print/Naira-Bag-FULL-SHEET-17x11.45in-PROOF-cutlines.jpg` | placement proof with cut and fold lines |

Both PDFs are one flat sheet, 16.75 × 11.2 in trim plus 0.125 in bleed (page 17 × 11.45 in, TrimBox
and BleedBox set). Panels left to right: gusset 2 · front 6 · gusset 2 · back 6 · glue 0.75 in.
Handle: D-cut 2.3 × 1.0 in, 1.05 in below the top, centred on each face.

## Layers

1. Background, cream, vector
2. Leaf pattern: the site's two sprigs, 2048 px each (above 850 ppi at size), each instance its own image at 34 %
3. Florals: tulips, leaves and dots, vector
4. Logo: traced to vector from the site's 4000 px footer logo (99.6 % pixel agreement)
5. QR code: vector, with its cream quiet zone
6. Text: live (EDITABLE) or outlined (PRINT-READY)
7. Dieline: cut and fold lines in spot colours `Dieline` and `Fold`, overprint, set not to print

The dieline is reconstructed from the Kraftix 6 × 9.5 × 2 template. Align to your own die before cutting.

## Rebuild

```
cd build
python3 trace_logo.py      # only if the logo changes (needs src/logo_footer_4000.png and potracer)
python3 master.py          # renders each layer with Chromium, stacks them as PDF layers with PyMuPDF
python3 spec.py && python3 master.py assemble   # refresh the spec page, then re-stack
```

Checks run on the last build: page 1 matches the approved raster artwork within 1 level on average;
the QR decodes from the PDF at 300, 100 and 72 dpi; PRINT-READY carries no fonts; the print-ready
dieline renders nothing in the default view.
