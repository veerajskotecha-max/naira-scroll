# Verification Doc — the pre-flight gate for every campaign

Built 7 Sep 2026. **No frame is generated until its SKU has a row here.**

Every row is checked three ways: the listing's **Details block**, **all 3–6 website images**
including on-body shots, and the **live Shopify status**. Where the three disagree, the disagreement
is recorded rather than resolved silently.

## Why all the images, not just the hero

The hero shot alone is not enough. Three of the findings below are only visible when you look at
the whole set:

- **Cut** shows in the macro shot, not the catalogue square.
- **Metal tone** is most reliable across several frames — a single warm-lit shot can make rhodium
  look gold, which is exactly the mistake that pulled a usable SKU out of the last campaign.
- **True scale** only reads on the on-body shot. A plinth shot tells you nothing about size.

---

## The verified set

| SKU | Piece | Status | Metal — **verified from images** | Stones, counted | Size | Images |
|---|---|---|---|---|---|---|
| `B00681C` | Prism Rivière Bracelet | ACTIVE | Rhodium / silver tone ✓ 6 images agree | Cushion pastel CZ ~5mm, each in a fine pavé halo; aqua → pink → pale yellow repeating | 18cm, fold-over clasp | 6 ✓ |
| `WR23024K` | Verdant Eternity Band | ACTIVE | **Rhodium / white ✓ confirmed across 5 images** | Oval green CZ 5×4mm claw-set all round, scalloped pavé between | Adjustable US 6–8, **open back** | 5 ✓ |
| `FE02847B` | Verdant Circlet Studs | ACTIVE | 18k gold tone ✓ | Cushion green CZ ~10mm above; open circlet of clear CZ + gold points; **white shell pearl ~6mm inside the circle** | 20mm tall | 4 ✓ |
| `E21572E1` | Verdant Drop Earrings | ACTIVE | Silver tone, **copper alloy body + 925 silver posts** — not steel | One cushion CZ ~9mm in **vivid mint turquoise**, 4 plain claws, open basket, **no halo**; curved top bar of tiny clear CZ | 25mm drop | 5 ✓ |
| `E16075B` | Ribbon Bow Earrings | ACTIVE | 18k gold tone ✓ | Pear-cut + tapered clear CZ in fine gold claws, read as one continuous bow | 15mm wide | 6 ✓ |
| `E20997C` | Pearl Blossom Earrings | ACTIVE | Rhodium / silver tone ✓ | Pavé bow above; round shell pearl ~9mm cradled in an open pavé circle | 18mm tall | 2 |
| `JDB0103317-PK` | Blush Station Bracelet | ACTIVE | 18k gold tone ✓ | Large pale-rose stations ~14mm alternating with round pink CZ ~3mm, individual gold bezels | 19cm + 5cm extender | 2 |
| `WR10914B2` | Blush Cluster Ring | ACTIVE | 18k gold tone ✓ | Round pink CZ ~5mm centre, **10** pink CZ ~2.5mm around, 1 more on the shoulder | Fixed US 7 | **1 only** |
| `R18345A1` | Rose Verdant Band | ACTIVE | **Rose gold tone** ✓ 4 images agree | 4 parallel bands; **4** round green CZ ~4mm at staggered points | Open back, adjusts a little | 4 ✓ |
| `YF5215` | Heartbead Bracelet | ACTIVE | **Silver-tone strand + gold toggle and gold heart** | Polished silver-tone steel spheres ~6mm, mirror bright; gold toggle bar + ring; one puffed gold heart ~15mm | — | 5 ✓ |
| `JDE0110042` | Molten Bloom Hoops | ACTIVE | 18k gold tone ✓ | **None** | 21 × 19mm, band 4.7mm | 6 ✓ |
| `JDE0201327` | Clover Trio Edit | ACTIVE | 18k gold tone ✓ | Clear CZ throughout | Huggie 10.2mm · clover charm 8.5mm drop · clover stud 6.2mm · solitaire 3.7mm | 5 ✓ |

---

## Discrepancies found — recorded, not resolved

| # | SKU | Listing says | Images show | Call |
|---|---|---|---|---|
| 1 | `JDB0103317-PK` Blush Station | "**Marquise cut** pale rose CZ station, approximately 14mm" | Stations read **round / oval**, not pointed marquise | **Images win.** Do not brief a marquise. Re-check against the supplier photo before the copy is trusted. |
| 2 | `R18345A1` Rose Verdant | "each one pave set… **all four** pave across the front" | Reads closer to **alternating** pavé and plain bands | Unresolved. Shoot at an angle where the count is not the subject, or verify against supplier. |
| 3 | `E20997C` Pearl Blossom | Pearl in "a warm **champagne** tone" | Pearl reads near-**white** in both images | Minor. Brief as a warm white rather than champagne. |
| 4 | `WR10914B2` Blush Cluster | 10 surround stones + 1 on the shoulder | **Only one image exists**, and it is on-body at distance — the count cannot be verified | **Gate: do not shoot a stone-count-critical frame on this SKU** until a macro image exists. |

---

## Two corrections to my own earlier audit

**1. Heartbead Bracelet — I was wrong.** I told you frame R09 of The Red Room was an error because
"the listing states 18k gold tone only." It does not. The full listing reads *"Silver tone strand
with 18k gold tone clasp and charm,"* and all five images confirm it: grey-silver mirror beads, a
gold toggle, a gold heart. I was reading a compressed summary table instead of the listing itself.
The real defect in R09 is narrower — it mixed **gold beads into the strand**, and the strand should
be entirely silver-tone.

**2. Verdant Eternity Band was pulled for nothing.** I held it out of The Bench because its hero
image "looked warm" against a listing that says rhodium. Across five images it is unambiguously
white metal. Over-cautious. It is back in.

---

## Two greens, and they are not the same

A recurring trap in this range:

- **Verdant Drop Earrings** — *vivid mint turquoise*, bright, cool, almost aqua.
- **Verdant Eternity Band · Verdant Circlet Studs · Rose Verdant Band** — *emerald green*, deep and warm-leaning.

Briefing "Verdant green" without saying which produces the wrong stone. Name the colour, never the
product family.

## And none of them is an emerald

Three listings carry the line *"Green cubic zirconia, not emerald"* in their own Details block. Four
frames across the three previous campaigns used the word **Emerald** in the title. That word does
not go in a caption, a headline or a file name.

---

## The gate

A frame may be generated only when all five are true:

1. SKU is `ACTIVE` in a live query, not draft.
2. Metal is taken from the **Plating** field and confirmed across at least two images.
3. Every countable feature has been counted **in an image**, not read from copy.
4. A stated mm figure exists, or the frame does not attempt a scale claim.
5. Any discrepancy above is either designed around, or the frame is not shot.
