# Edition Two listings

Listing kit (artifact): https://claude.ai/artifact/2U2vuzrqeQHcKymDdc4e64. The machine-readable version is `kit/listing.json`.

Shopify listing kit for the Notion photo set (N01–N25) and the Foshan Yiss Fera quotation of 2026-09-22 (59 lines, 923 pcs, US$3,476.59).

- `build/products.json` is the handoff: 34 new products, one per design, with metal, stone colour, ring size and birth month as variants. Each variant carries its SKU, price, PI line, quantity and image. It also lists the 8 live listings the PI restocks or extends.
- `build/pi_lines.json` maps every PI line to the product or variant it became; `pi_lines.py` fails loudly if a line is uncovered.
- `build/approved.json` maps each approved shot to its Higgsfield job (`out/<key>.png` downloads from it); `jobs.json` is every job submitted, including rejects.
- `pi-refs/` holds the single-product crops cut from the PI thumbnails (`pi_extract.py`, `pi_crops.py`), which were the supplier references.

## Image recipe (the live Edition One format, 1288×1600)

1. Hero: the piece on a cream plaster cube (`build.py … H`, plate `8cf120d5`).
2. Worn: the saffron-camisole model, cropped above the upper lip (`W1`, then `W2` for a close detail).
3. Macro on the cube top (`M`).

Worn and macro frames pass the approved hero as IMAGE 2, so size and finish carry over. Metal and stone-colour variants are edits of the approved hero (`make_queue.py`).

`export.py` applies the per-key fixes: a tighter crop for small rings, a ruby hue correction (`DEEPEN`), and one warm-gold correction (`WARM`). `export_all.py` then writes `exports/<handle>-NN.jpg`, and `make_page.py` builds the artifact page and `listing.json`.

Scripts expect to run from this folder's layout, with `out/` beside them, and use `python3 -I`.

## What is in the kit

- 34 new products and 96 variants, every one with 4 to 12 verified images (161 in total).
- Each image is hosted at a public URL, listed in `build/url_map.json` and in `kit/listing.json` per product, with alt text and the variant it belongs to.
- The same 1288×1600 files are in `exports/`.
- Prices are set at 3.7 to 6 times landed cost (PI price × ₹83, plus about 20% freight and duty) and rounded to the store's x99 steps.
- 21 points need the owner's confirmation before publishing; each one shows as "Confirm" on its product.
- 8 live listings get restocks or new variants: Star Point Band (add silver), Rivière Eternal Bracelet (re-activate), Marquise Layering Set, Bold Nocturne Chain and Bracelet, Baroque Shell Bracelet, Halo Curve Ring and Ribbon Bead Bracelet.
