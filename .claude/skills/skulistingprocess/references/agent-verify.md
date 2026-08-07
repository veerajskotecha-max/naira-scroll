# Website-readiness verification — final gate before publishing

These images are about to be published on a live ecommerce store, nairaflore.com. Your job is to catch anything a customer would look at and think "that's fake" or "that's broken". You are the last check.

## Inputs
- `/tmp/naira_work/listing/verdicts.json` — every slotted image with its `sku`, `file`, `slot`, `angle`.
- `/tmp/naira_work/listing/MANIFEST.json` — the 42 SKUs with `product_desc`, the sourcing description of the real object.

## Look at every image
Use the Read tool on each file. Build labelled per-SKU contact sheets with PIL first if that is faster, but open any image full size where you are not certain. Do not judge from filenames.

## Fail an image for any of these

**Looks AI / uncanny**
- A hand or ear with wrong anatomy: six fingers, four fingers, fused or bent-wrong digits, a thumb in the wrong place, two left hands, a second limb that does not belong.
- Skin that is plastic, waxy, poreless or smeared.
- Hair that melts into the skin or the background, or a strand that passes through the ear or the jewellery.
- Jewellery that merges into the skin instead of sitting on it.
- Any visible eye. These are meant to be cropped below the nose.

**Physically wrong**
- The piece floats, hovers, or balances impossibly with no contact and no contact shadow. Ring cutouts on white are exempt from needing a plinth, but must still sit on their own soft shadow rather than hang in space.
- Part of the product is cut off by the prop, sunk into it, or dissolves at the edge.
- A chain, clasp or extender that ends in nothing, or a link that does not connect.

**Half-finished**
- Any part of the piece that is blurred into mush, unresolved, or clearly unfinished.
- A cutout with a halo, a hard jagged edge, a chewed-away shank, or leftover background fragments.
- Stones that render as a smear rather than separate stones.

**Wrong product**
- Compare against that SKU's `product_desc`. Wrong stone colour, wrong stone count, wrong metal tone, wrong link type, a different design, or extra pieces or extra jewellery in frame.

**Unpublishable**
- Text, watermark, printed measurements, supplier card or brand wordmark anywhere in frame.

## Output

Write `/tmp/naira_work/listing/webready.json`:

```json
{"images":[{"file":"<absolute path>","sku":"...","pass":true,"reason":""}],
 "skus":[{"sku":"...","ready":true,"passing_images":4,"blockers":[]}]}
```

- `pass:false` needs a specific one-line `reason`. Not "looks off" — say what is wrong and where.
- A SKU is `ready:true` only if it has **at least 3 passing images**, one of which is the slot-1 ecom shot and one of which is a worn shot.
- `blockers` lists the reasons a SKU is not ready.

Be strict. Everything you pass goes live on a real store today.
