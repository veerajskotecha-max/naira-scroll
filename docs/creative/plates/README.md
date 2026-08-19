# Setting plates and control frames

## Plates — Higgsfield reference slot 2

Seven reusable empty scenes. Each contains **no jewellery**; the product arrives from slot 1.
Generated once at 2K, 4:5. See `../two-slot-system.md` for the method.

| File | Scene | Principal referent | Size class it serves |
|---|---|---|---|
| `S1-plinth.jpg` | lime plaster block, chipped, raking light | 60mm block | 30–100mm |
| `S2-khadi.jpg` | undyed khadi, fine weave, one empty dent | thread ≈0.5mm | no strong anchor |
| `S3-water.jpg` | glass tumbler, waterline, clinging bubbles | tumbler ≈70mm | 30–100mm |
| `S4-skin.jpg` | bare Indian neck, collarbone, ear | earlobe ≈15mm | on-body, any |
| `S5-clay.jpg` | raw clay tile, cardamom pods, peppercorns | pod 8–10mm | 5–18mm |
| `S6-box.jpg` | open empty gift box, blush tissue, dried petal | box ≈80mm | 20–100mm |
| `S7-midscale.jpg` | khadi with a matchstick and a shirt button | match 45mm, button 11mm | 15–45mm |

S2 and S3 are second passes. S2 first rendered as jute over a box form — too brown, too coarse, and
the hard edge underneath read as a plinth. S3 put the glass on yellow wood, which breaks the
palette. S7 was added after the control test exposed a gap in the 15–45mm band.

## Control frames — the A/B that justified the system

Same prompt, same product reference, same target image; the only variable is whether a plate
occupies slot 2. Ratios measured in pixels off a coordinate grid.

| File | Product : referent | rendered / true | accuracy |
|---|---|---|---|
| `ctrl-stud-1slot.jpg` | 12 : 9mm described | 0.84 / 1.33 | 63% — **inverted** |
| `ctrl-stud-2slot.jpg` | 12 : 9mm shown | 1.18 / 1.33 | 89% |
| `ctrl-hoop-1slot.jpg` | 25 : 9mm described | 2.37 / 2.78 | 85% |
| `ctrl-hoop-2slot-S5.jpg` | 25 : 9mm shown | 1.87 / 2.78 | 67% — compressed |
| `ctrl-hoop-2slot-S7.jpg` | 25 : 11mm shown | 1.98 / 2.27 | 87% — recovered |

The plate compresses the size range toward its own referent. Size-match the referent to the piece
and it holds at 87–89%; mismatch it and accuracy collapses. One-slot is erratic: 63% on the small
piece, and inverted so the earring read smaller than a cardamom pod.
