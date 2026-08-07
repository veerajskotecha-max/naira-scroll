# Source verification — does the listing match the supplier photo?

Run this **before activating anything**. It catches a class of error no image
gate can: the picture is beautiful and the copy is fluent, and both describe a
product the factory is not shipping.

The failure mode is inheritance. A sourcing description misreads the object
once, the copy repeats it, the generation prompt repeats it again, and the
error is now baked into three artefacts that all agree with each other. The
only thing that breaks the loop is the manufacturer's own photograph.

## Where supplier photos come from

In order of quality:

1. `input_images[].url` in the Higgsfield generation record. These are the
   actual reference photos and are the best source.
2. Images embedded in a supplier workbook. Extract them with the drawing
   anchors so each one is tied to its row, and therefore to a SKU:
   ```python
   z = zipfile.ZipFile(xlsx)
   root = ET.fromstring(z.read('xl/drawings/drawing1.xml'))
   # xdr:from/xdr:row gives the spreadsheet row for each xdr:twoCellAnchor
   ```
   Never map images to SKUs by array order.
3. Order screenshots and quotations. Low resolution, but they carry the thing
   nothing else does: **which variant was actually bought**. A colourway or
   style code in the order line settles arguments the product photo cannot.

## Build one comparison sheet per SKU

Supplier photo on the left labelled in red, published images to its right, SKU
and the first five copy detail lines underneath. One image per SKU that an
agent can judge in a single look. Mark sheets with no reference
`NO SUPPLIER REF` and report them `unverifiable`, never as pass or fail.

## The check order

Ignore the written description. It is the thing under suspicion.

1. **Metal colour.** Which parts are gold, silver, rose, two tone. A gold clasp
   on a silver strand is two tone and must not render all gold. Most common
   failure by a wide margin.
2. **Stone colour.** Deep emerald, mint aqua and teal are different products.
3. **Stone count and size** relative to the piece. Count them.
4. **Setting type.** Claws, bezel, pave, halo. An added halo is a different ring.
5. **Material character.** Pearl against polished metal bead against enamel.
6. **Form.** Link shape, hoop against stud, charm shape, clasp type.
7. **Extra or missing parts.** A charm, an extender, a second piece.

Then read the detail lines and check them against the photo too. A correct
image with wrong copy is still a fail.

## Verdict schema

```json
{"sku":"","verdict":"pass|fail|unverifiable","severity":"none|minor|major",
 "what_is_wrong":"","fix":"image|copy|both|none"}
```

Name the colour in the supplier photo and the colour in the listing. "Colour
looks off" is not usable.

## What each verdict means for the store

| Verdict | Action |
|---|---|
| pass | Activate |
| fail, `fix: copy` | Correct the copy, then activate. Copy is cheap. |
| fail, `fix: image` or `both` | Stays Draft until reshot. Deactivate if already live. |
| unverifiable | Do not claim it verified. Report it and let the client decide. |

Split the work across three Opus agents of about twenty SKUs each. Sonnet is
not reliable enough here: the judgement is a fine visual discrimination, and
the cost of a false pass is a customer receiving a different object.

## Things this has caught

- A bracelet whose beads were all polished silver with gold only on the toggle,
  sold as grey pearly beads strung with gold ones.
- A gold granulated dome described as pave set, because its **silver sister SKU**
  is pave set and the copy was written from the wrong sibling.
- A tennis bracelet listed against a supplier photo of a plain cable chain with
  one small pave circle. Different product, full stop.
- A charm assortment of five plain hammered styles sold as a single pave clover
  pendant on a chain that was never ordered.
- Halos, lilac stones and pave bars invented by the image model and then
  written into the copy as if real.
- Tags inheriting the wrong metal: a gold ring filed under Silver Tone.
