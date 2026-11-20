# Model bake-off (20 Nov 2026)

Why: in the first four Crazy 100 batches the requested `nano_banana_pro` jobs were all served by `nano_banana_2`, and the
verifiers failed most takes on construction or scale (Woven Gold Hoops: flat ribbon plait, missing or doubled disc, 1.35-1.45x
too big; Toggle Link Chain: sailor ring redesigned; several pieces 1.5-2x too big).

Test 1, Woven Gold Hoops worn from behind, one identical prompt and the same two listing references (refs 01 and 03):

| File | Model (served) | Credits | Braid | Single disc | Latch | Scale | Face rule |
|---|---|---|---|---|---|---|---|
| `pics/nanobanana_2k.png` | nano_banana_pro requested, nano_banana_2 served | 2 | open plait, fair | **missing** | ok | ok | ok |
| `pics/gpt26.png` | gpt_image_2_6, quality high, 2k | 2.75 | open plait, good | yes | yes | true | ok |
| `pics/seedream5.png` | seedream_v5_pro, 2k | 2.5 | open plait, best | yes | yes | slightly large | ok |
| `pics/flux3.png` | flux_3_image, 2k | 3 | good | yes | yes | true | **fail: eye and profile** |
| `pics/minimax.png` | minimax_h3_image, 2k | 3 | chunky | yes | yes | **too large** | ok |

`nano_banana_pro` at 4k was refused ("requires plus plan or higher").

Test 2, the two other hard locks:

| File | Piece | Result |
|---|---|---|
| `pics/ring_gpt26.png` | Verdant Eternity Band on a mehendi hand | true scale; the pave wave reads close to a partial halo |
| `pics/ring_seedream5.png` | same | single S-wave cupping the ovals, closest to the listing |
| `pics/toggle_gpt26.png` | Toggle Link Chain fastened at the nape | sailor ring, spring-gate nub and straight stone bar match the listing |
| `pics/toggle_seedream5.png` | same | ring and bar right, clasp smaller and softer |

Decision: from batch wave 2 on, take A is `gpt_image_2_6` (high, 2k, 2.75 credits) and take B or the redo is `seedream_v5_pro`
(2k, 2.5 credits). Pictures are 1520x2688 or 1536x2720, so the crop rule is now computed from each picture's real size.
Total spent on the bake-off: about 25 credits.
