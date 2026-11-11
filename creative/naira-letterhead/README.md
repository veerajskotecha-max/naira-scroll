# NAIRA letterhead · A4

| File | Use |
|---|---|
| `Naira-Letterhead-A4.pdf` | Print file, 210 × 297 mm, white paper. Every mark sits at least 6.5 mm from the edge, so it prints on any office or inkjet printer without clipping. Logo and florals are vector; Jost and Cormorant are embedded. |
| `Naira-Letterhead-A4-EDITABLE.docx` | Word template. The artwork sits behind the text on every page; margins (top 56 mm, bottom 34 mm, sides 22 mm) keep typing inside the writing area. Body text is Georgia 11 pt. |
| `Naira-Letterhead-A4-preview.jpg` | Preview. |

Header: the card's tulips in the top corners, the NAIRA wordmark in its own sage and blush, "[ 18k gold coated · rhodium coated ]". Footer: nairaflore.com · @nairaflore · WhatsApp +91 95615 57935 · shopatnaira@gmail.com, and "made to stay gold."

Not on it yet: a postal address and GSTIN.

Rebuild: `python3 build/letterhead.py && python3 build/make_docx.py` (paths point at the working scratchpad; the motifs and logo come from `creative/naira-bag/build`).
