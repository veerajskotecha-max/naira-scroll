# Naira Petite stall posters: Fashion Mantra Exhibition, Emerald Park, Nashik

Seven wall posters for the shell-scheme stall, one per panel.

## Print spec (same for all seven)

| | |
|---|---|
| Trim size | **24 × 36 in (609.6 × 914.4 mm), 2 × 3 ft, portrait** |
| Bleed | **None.** Each PDF is exactly the trim size, with no bleed and no crop marks. Ask the printer to print at 100% with no scaling. |
| Colour | RGB. The printer converts to CMYK. |
| Resolution | Photos are embedded at about 150 ppi at full size, and the type is vector. |
| Stock | Matte, not gloss: the stall has bare bulbs that glare on gloss. 300 gsm matte paper or matte vinyl, mounted on 5 mm sunboard. |
| Mounting | Velcro or double-sided foam tape on the white panels. Put the top edge about 2.0–2.1 m from the floor, so the bottom clears the table displays at about 1.1–1.2 m. Centre each poster on its panel. |

## Which poster goes where

| Wall | Panel | File | Poster |
|---|---|---|---|
| Back (main, faces visitors) | left | `Naira-Stall-back-1-the-wall-24x36in.pdf` | The Wall: every piece on her, coral CATALOGUE badge, QR |
| Back | centre | `Naira-Stall-back-2-now-showing-24x36in.pdf` | Now Showing: CHAMAK film poster, the cast, QR |
| Back | right | `Naira-Stall-back-3-naira-times-24x36in.pdf` | The Naira Times: SHE WORE IT ALL., Nashik edition, QR |
| Left | 1 | `Naira-Stall-left-1-apricot-edit-24x36in.pdf` | APRICOT edit: Woven Gold Hoops, four more pieces |
| Left | 2 | `Naira-Stall-left-2-gifting-24x36in.pdf` | Gift it beautifully: the blush box, prices by category |
| Right | 1 | `Naira-Stall-right-1-lilac-edit-24x36in.pdf` | LILAC edit: Prism Rivière, four more pieces |
| Right | 2 | `Naira-Stall-right-2-catalogue-24x36in.pdf` | See it all: twelve pieces on her, large QR |

Spares, built but not in the set: SAGE edit and About us (`posters.py sage-edit about`).

Every QR opens `nairaflore.com` with `utm_source=stall&utm_medium=poster&utm_campaign=fashion-mantra-nashik`, so stall
traffic shows up separately in Shopify analytics. Prices are the live store prices of 20 Oct 2026.

## Building

- `posters.py`: the side posters.
- `covers_print.py`: the back-wall covers, reusing `../catalogue/covers.py` in its `2x3` layout.
- `upscale.py`: Real-ESRGAN x4, blended 65/35 with Lanczos. It upscales any photo crop that would otherwise print soft.
- `render_print.cjs`: writes the PDF, a 150 ppi JPG and a preview.

The hero photos of the side posters are the 2294×4096 upscaled standee masters. They were taken from the colour-camp
standee PDFs.
