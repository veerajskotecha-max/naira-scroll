# Naira catalogue ads

Women's on-model catalogue ads, in the style of the Palmonas catalogue carousels: three covers to lead the carousel and three cards for every in-stock piece. Everything is cut from the store's own listing photos; no new photos were shot (Higgsfield had 0.07 credits on 20 Oct 2026).

## What is here

- `out/covers/`: three cover options, each at 1:1 (1080×1080), 4:5 (1080×1350) and 9:16 (1080×1920).
  - **The Wall.** Every piece, on her, in one dense wall, with a coral badge and marker circles on favourites.
  - **Now Showing.** A Bollywood film poster with CHAMAK in gold-tone 3D type, the cast of pieces and a billing block.
  - **The Naira Times.** A tabloid front page with the headline SHE WORE IT ALL., a lead photo and side stories.
- `out/cards/<handle>-A|B|C.jpg`: 1080×1080 cards for all 91 in-stock products.
  - **A, Worn.** The on-model photo cropped round the piece, with NAIRA on top and the name and price below.
  - **B, Detail.** The worn photo and a close-up side by side, with a cream name plate.
  - **C, Zoom.** A second on-model photo, or a wider crop, with the close-up in a magnifier that points at the piece.
  - **No model photo.** Nine pieces have none in the store, so their cards use product shots.
- `out/naira-catalogue-links.csv`: every card file with its product, price and link, set to the colour in the photo.

## How it is built

1. `thumbs.py`, then `picks.py`: contact sheets of every in-stock product's photos, and the on-model and close-up photo picked by eye for each.
2. `fetch_full.py`, `alts.py` and `variants.py`:
   - full-size photos;
   - second on-model photos;
   - the colour each photo shows, with that variant's price and link.
3. `gridsheets.py`: gridded sheets of the on-model photos. The box round each piece is read off them into `boxes.txt` as fractions: x0 y0 x1 y1, then optionally the focus box.
4. `cards.py`: crops round the boxes, places text clear of the piece, then renders through `render.cjs` (Chromium).
5. `covers.py`: builds the three covers in three sizes.
6. `page.py`: builds the artifact page from `page_template.html`.

The scripts read and write under the session scratchpad (`SP` in `cards.py`) and use the fonts in `<scratchpad>/cat/fonts`:

- Jost, Cormorant Garamond and Velista (the brand fonts);
- Anton, Permanent Marker and Old Standard TT (the covers).
