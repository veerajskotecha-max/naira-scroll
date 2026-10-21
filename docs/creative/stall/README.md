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
| Back (main, faces visitors) | left | `Naira-Stall-back-1-apricot-24x36in.pdf` | APRICOT colour camp: the standee poster |
| Back | centre | `Naira-Stall-back-2-sage-24x36in.pdf` | SAGE colour camp: the standee poster |
| Back | right | `Naira-Stall-back-3-lilac-24x36in.pdf` | LILAC colour camp: the standee poster |
| Left | 1 | `Naira-Stall-left-1-apricot-edit-24x36in.pdf` | APRICOT edit: Ribbon Bow Earrings, four more pieces |
| Left | 2 | `Naira-Stall-left-2-gifting-24x36in.pdf` | Gift it beautifully: the blush box, prices by category |
| Right | 1 | `Naira-Stall-right-1-lilac-edit-24x36in.pdf` | LILAC edit: Serpentine Whisper Chain, four more pieces |
| Right | 2 | `Naira-Stall-right-2-catalogue-24x36in.pdf` | See it all: twelve pieces on her, large QR |

The colours run apricot → apricot · sage · lilac → lilac around the stall (`previews/00-wall-order.jpg`,
`previews/01-walls-to-scale.jpg`). The side heroes were chosen so no photo repeats one on the back wall.

Spares, built but not in the set: SAGE edit and About us (`posters.py sage-edit about`). The catalogue-cover back
wall (The Wall, Now Showing, The Naira Times; `covers_print.py`) was replaced by the colour-camp standees.

### What changed on the standees

The back wall uses the 4 × 6 ft colour-camp standee PDFs from `../colour-camps`. Each one is already 2:3, so it is placed
at half size with its vectors intact. Before that, patches matched to the original type update it to the live store:

- Brushed Gold Huggies sticker: ₹1,099 → **₹999**.
- No "waterproof" anywhere: the Apricot taped strip, the Sage and Lilac footers, and the Lilac side facts.
- "Gold" → **gold-tone** on the Sage spec lines (Heartbead, Granule Dome).
- Sage QR: it was ivory on green, which most phones cannot read. It is now green on an ivory tile, like Apricot and Lilac.
- The 12 cm stand base (now 6 cm at poster size) carries one line: NAIRA PETITE · SOFTLY, SLOWLY, WORN.

Every QR on the side posters, and the Sage standee's, opens `nairaflore.com/?utm_source=stall`, so stall traffic shows up
separately in Shopify analytics. The link is kept short so the codes have large modules and scan from a distance. The
Apricot and Lilac standees keep their original links (`utm_source=standee`, with the camp as `utm_campaign`). Prices are the live store prices of 20 Oct 2026.

## Building

- `posters.py`: the side posters.
- `standees_print.py`: the back wall. It patches the three colour-camp standees and fits them to 24 × 36 in.
- `elevation.py`: the stall walls to scale, and (`--lineup`) the seven posters side by side.
- `covers_print.py`: the earlier catalogue-cover back wall, kept as a spare. It reuses `../catalogue/covers.py` in its `2x3` layout.
- `upscale.py`: Real-ESRGAN x4, blended 65/35 with Lanczos. It upscales any photo crop that would otherwise print soft.
- `render_print.cjs`: writes the PDF, a 150 ppi JPG and a preview.

The hero photos of the side posters are the 2294×4096 upscaled standee masters. They were taken from the colour-camp
standee PDFs.
