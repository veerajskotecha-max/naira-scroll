# Shop All, the aesthetic ten (7 Nov 2026)

The ask: "Make more aesthetic Shop All ads using existing high CTR creatives. Be creative and make 10."

Same job as the first ten in `../` (send people to every piece, https://nairaflore.com/jewellery), same pool of photos
Naira has already run or listed, but quiet and editorial instead of loud: one proven photo with room around it, one calm
line that opens the door to the rest of the shop, type and colours taken from the photo, and the offer left for the caption.
No new photos were generated. Nothing has been created on Meta or changed on Shopify.

## The board

Published as a private artifact: https://claude.ai/artifact/2ffJxDVLpi13HuoGHk537S (share it from the page's Share menu).
The first ten are at https://claude.ai/artifact/EennScYjuLekNowJ6nqvv3.

## How it was made

1. **Brief** (`research/aesthetic_brief.md`, `research/caption_rules.md`): what "aesthetic" means here (one dominant image,
   a third of the frame quiet, editorial serif type, palette from the photo, text under about 12%, no stickers), how each
   ad still sells the whole shop, the photos with the best Meta results, and the first ten's formats, which were not reused.
2. **Concepts** (`research/concepts.json`): three creative directors (editorial and print, colour and still life,
   minimal and cinematic) wrote 18 concepts; three judges scored them; a curator chose 12 and wrote build specs
   (`research/specs.json`).
3. **Build**: each of the 12 was built in HTML over the pool photos as a Feed (1080x1350) and a Story (1080x1920), with at
   least three render-and-look rounds at full size and at phone width. Jewellery is never enlarged past its photo size,
   recoloured or repainted.
4. **Judging** (`research/judging.json`): an art director (0.4), a media buyer (0.4) and a fact checker (0.2) scored all 12;
   a head of creative picked 10 as a set and merged each pick's fix list. Each pick was fixed and then checked again by a
   reviewer who had not seen it. All ten passed.
5. **Captions** (`research/captions.json`): primary text, headline and description per ad, written and then corrected by a
   separate copy chief and fact checker (prices and names from Shopify via the pool, count-free range wording, the exact
   offer sentence, banned words).
6. **Plan** (`plan.json`, from `build/make_plan.py`): run them as a second ad set beside the first ten and split the
   ₹1,000 a day ₹500 / ₹500 for a week, judged on purchases; rules, sources and things to know.

## The ten (`ads/`)

| # | Ad | On the image | Photo |
|---|---|---|---|
| 1 | A01 | One link leads to another. | Bold Nocturne Chain close-up (on-model listing photo) |
| 2 | A09 | Slip, model's own. Everything else, from ₹599. | Marquise Drop Choker and Silk Mesh Cuff, worn |
| 3 | A03 | The Everything Issue (a NAIRA cover) | Woven Gold Hoops on persimmon |
| 4 | A02 | Sold. The rest are on view. | The sold-out ruby bracelet with anaar, framed, with a red Sold dot |
| 5 | A07 | Anaar, at the throat. / Elaichi, around the wrist. / Rangoli, for ears. | Ruby necklace with anaar |
| 6 | A05 | The rangoli's done. Come in. | Prism Rivière Bracelet over a rangoli (Diwali week only) |
| 7 | A08 | Fig. 1: Rangoli you can wear. Fig. 2 onwards: everything else, from ₹599. | Prism Cluster Studs with rangoli cones |
| 8 | A12 | Set in gold tone. | Kiss Knot Bangle on an envelope |
| 9 | A10 | Twisted. Knotted. Polished. (the gold-tone edit) | Torsade Huggies, Kiss Knot Bangle, Bold Dome Huggies |
| 10 | A04 | – I got you these. – Cute. I'll get the rest myself. | Woven Gold Hoops in his hand |

`ads/other/` holds A06 ("Left ear, right ear.") and A11 ("Hang at ear height."), made but not picked; `research/judging.json`
says why. `research/changes.json` is the plain note of what changed in each ad after review.

## Rebuilding the board

```
python3 build/make_plan.py                 # writes plan.json
python3 build/board.py <out_dir>           # writes <out_dir>/index.html
```

The board expects web-sized copies in `<out_dir>/ads/` (the ten) and `<out_dir>/thumbs/` (the two not picked).
`build/src/<ad>/` keeps the final Feed and Story HTML. Their image paths point at the session's working folder, so they
document the layouts rather than rebuild offline.

## Waiting on the owner

- Approval to create anything on Meta (nothing has been created), and whether to run these beside the first ten as a split
  test or on their own.
- The first board's open questions: what "10:10" meant, and whether to pause Winners revived (0.76x) to fund Shop All.
