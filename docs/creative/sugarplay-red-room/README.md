# Sugarplay & The Red Room — ten crazier options

Two earlier camps, re-dressed. The best shots from each were verified at full resolution against the listing
photographs before anything was drawn on them; the overlays then behave like the picture rather than like a
catalogue page. Feed 1080×1350 and story 1080×1920 for every card; names and prices read from Shopify at build
time; every figure on a card exists in that SKU's listing.

Artifact: (link in the session message)

| Set | Card | Device | Plate | Stock |
|---|---|---|---|---|
| Sugarplay | S1 Pick 'n' Mix | candy-stripe counter band, four round price stickers | pl02 verified | 77 |
| Sugarplay | S2 The Big Call | screenplay page, HER / YOU | pl03 verified | 77 |
| Sugarplay | S3 Sweetheart | four conversation hearts stamped with the spec | pl06 verified | 29 |
| Sugarplay | S4 Hop to Your Size | chalk hopscotch, squares 6·7·8 filled (the ring's sizes) | pl04 re-shot plate | 4 |
| Sugarplay | S5 Pick a Number | paper fortune teller, a listing fact under every flap | pl05 verified | 4 |
| Red Room | R1 Look Closer | three water-drop loupes magnifying the plate | archive #1536 | 77 |
| Red Room | R2 Twice | headline reflected like the lacquer | listing hero, wordmark cropped | 77 |
| Red Room | R3 Cloakroom | cloakroom ticket numbered with the price | listing hero | 29 |
| Red Room | R4 The List | wine list: body 12g, nose none, finish non tarnish | generated tonight | 80 |
| Red Room | R5 Red Light | darkroom contact sheet, frame seven circled | generated tonight | 16 |

Each set folder holds `feed/`, `story/`, two contact sheets and `build/` (the set module and its notes).
The shared build system lives in `../night-shift/core.py`; `artifact.py` here builds this page.

## What was verified, and what was rejected
- Sugarplay pl02, pl03, pl06 inspected at full resolution: cushion pastel stones in pavé halos with a fold-over clasp;
  the plait on the ear with no stones; mirror steel spheres, gold toggle, one gold heart. pl08 Marbles passed over:
  its signature drop pearl does not read.
- Red Room: only one of the original ten frames survives on the live listings with a red ground and hero stock
  (the hoops on the wet dome); its full-resolution twin was found in the archive (#1536) and used instead of the
  896px listing file. Archive #1497 was rejected: the pavé link belongs to a different chain.
- Two frames generated to complete the room (the chain over lacquer, the huggies before red glass), both checked
  against the listings.
