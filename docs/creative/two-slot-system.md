# E — The Two-Slot Prompt System

Set by the brand, 19 Aug 2026: *"prompting is always done by giving reference image in higgfield
and then giving setting image reference."*

Every generation from here uses **two reference images**, not one.

| Slot | Carries | Source | Governs |
|---|---|---|---|
| **1 — PRODUCT** | the piece itself | the SKU's Shopify CDN `_1_main.png` | metal, stone count, link type, structure, proportions |
| **2 — SETTING** | an empty scene | one of the locked plates below | surface, palette, light direction and quality, depth of field, grade |

Slot 2 contains **no jewellery**. That is what makes it a setting and not a second product.

---

## 1. This contradicted an existing rule, so it was tested

The image skill's **Law 1** — and the Lac & Bone production doc's own "Law 1" — say the opposite:
*only one reference image goes into generation; the other slots stay empty*, because
*"multi-reference destroyed scale before, and the rings came out costume-sized."*

That same document prescribes the remedy: *"if the multi-reference approach must be tested at all,
run one controlled A/B test on a single tile, not risk it across a whole batch."*

Two controlled pairs were run. Same prompt, same product reference, same target image; the only
variable is whether a setting plate occupies slot 2. Ratios measured in pixels off a coordinate
grid, not estimated by eye.

| SKU | Referent in plate | True ratio | One-slot | Two-slot |
|---|---|---|---|---|
| Solitaire Whisper Studs — 12mm head | cardamom pod, 8–10mm | 1.2 – 1.5 | **0.84** ✗ inverted | **1.18** ✓ |
| Woven Gold Hoops — 25mm across | cardamom pod, 8–10mm | 2.5 – 3.1 | **2.37** ✓ | **1.87** ✗ under |

### What this actually shows

Neither "always two-slot" nor "never two-slot" survives the data. The plate **compresses the size
range toward its own referent**: it pulled the 12mm stud *up* from 0.84 to 1.18, and pulled the
25mm hoop *down* from 2.37 to 1.87. Both products moved toward pod-size.

The mechanism is legible. With one reference the model has only the millimetre figures in the text,
which it under-weights — hence the stud rendering smaller than a cardamom pod, the exact inversion
that ruined the first V3 build. With a setting plate it has a *photographed* object of fixed size
and anchors to that instead, which is stronger than the text but indiscriminate: it anchors whether
or not the referent is an appropriate ruler for the piece.

### The working rule

> **Size-match the plate's referent to the product.** Keep the plate's principal referent within
> roughly 2× of the product's largest dimension. Inside that band the plate helps; outside it, the
> plate compresses the piece toward the referent and the one-slot path is more accurate.

Stud 12mm vs pod 9mm = 1.3× apart → inside the band → two-slot won.
Hoop 25mm vs pod 9mm = 2.8× apart → outside the band → two-slot lost.

**Status: working rule from two controlled pairs, not a law.** It predicts that re-shooting the
hoop against a size-matched plate recovers the ratio. That prediction is being tested.

---

## 2. The plates

Generated once, reused across all SKUs. This is what produces the palette lock the competitor
research found in every brand that reads as a brand — *"you could identify any of these accounts
from a thumbnail with the logo removed."*

| Plate | Scene | Principal referent | Size class it serves | Territory |
|---|---|---|---|---|
| **S1** | lime-plaster plinth, chipped, raking light | 60mm block | 30–100mm | the craft proof |
| **S2** | undyed khadi, fine weave, one empty dent | thread ≈0.5mm | any — no strong anchor | substrate deformation |
| **S3** | glass tumbler, waterline, clinging bubbles | tumbler ≈70mm | 30–100mm | the demonstration |
| **S4** | bare Indian neck, collarbone, ear — no jewellery | earlobe ≈15mm, body | on-body, any | on Indian skin |
| **S5** | raw clay tile, 3 cardamom pods, peppercorns | pod 8–10mm | 5–18mm | actual size |
| **S6** | open empty gift box, blush tissue, dried petal | box ≈80mm | 20–100mm | the box as product |
| **S7** | khadi with a matchstick and a shirt button | match 45mm, button 11mm | 15–45mm | the mid-scale gap |

S7 exists because the two-pair test exposed a gap: nothing in S1–S6 rules the 15–45mm band where
hoops, statement studs and pendant drops live.

**S2's empty dent and S6's empty tissue hollow are deliberate** — negative space the product will
occupy, pre-deformed, so substrate deformation is inherited rather than requested.

Two plates needed a second pass. **S2** first rendered as jute draped over a box form — too brown,
too coarse, and the hard edge underneath read as a plinth. **S3** put the glass on yellow wood,
which breaks the palette outright. Both re-shot and corrected; the versions in the table are the
corrected ones.

---

## 3. The prompt, seven blocks

With one reference the prompt invented the whole world. With two, its first job is **assigning
roles** — otherwise the model blends the frames: it renders the product's supplier plinth *inside*
the new scene, or treats the plaster block in the plate as an object to decorate.

```
[1 SHOT TYPE]        what kind of photograph this is
[2 REFERENCE ROLES]  ← NEW — which reference supplies what, and what to ignore in each
[3 FIDELITY LOCK]    what must not change about the piece
[4 SCALE]            mm + referent + substrate deformation
[5 PLACEMENT]        where in the set it sits and how it touches
[6 LIGHT + GRADE]    inherited from reference 2; both sources named anyway
[7 NEGATIVES]        now including "no second piece of jewellery"
```

### Block 2 — Reference Roles (verbatim, reusable across every SKU)

> Reference 1 is the PRODUCT and reference 2 is the SET. Take from reference 1 only the piece of
> jewellery itself — its metal, its stones, its structure and its proportions — and ignore
> reference 1's background, its plinth, its lighting and its colour grade completely. Take from
> reference 2 only the environment — the surface, the palette, the direction and quality of the
> light, and the depth of field — and understand that reference 2 contains no jewellery and
> contributes no object. The finished photograph is the single piece from reference 1,
> photographed on the set from reference 2.

### Block 7 — the negatives the one-slot system never needed

> no second piece of jewellery, no duplicate of the product, nothing from reference 1's original
> background, no cream plinth, no white cyclorama

---

## 4. What held and what slipped in the four test frames

**Held in all four:** metal colour (rhodium stayed rhodium, gold stayed gold); the morph-risk
feature named by name — the cushion halo stayed a rounded square and never became a circle, the
pavé stayed separate stones and never became a smooth rim, the woven braid stayed a braid of
countable strands; one piece per frame, never the pair; the palette; shallow macro depth of field;
contact shadow.

**Slipped:** substrate deformation was weaker in the two-slot frames than the one-slot ones — the
one-slot stud pressed a clean crenellated negative imprint into the clay, the two-slot version
mostly did not. The plate supplies a surface that already looks settled, so the model treats it as
finished rather than deformable. Where the imprint is the point of the shot, keep the deformation
clause and consider the one-slot path.

**Watch:** the hoop's gold reads slightly orange against the brand rule that warm-neutral gold is
correct and *"orange gold is the #1 tell of cheap AI jewellery."* The supplier reference is itself
quite yellow, so this is inherited, not invented — but it needs a grade correction at the type
layer or an explicit "warm-neutral, never orange" repeat in block 6.
