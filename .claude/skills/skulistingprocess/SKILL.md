---
name: skulistingprocess
description: End-to-end pipeline that turns a batch of Naira Petite demi-fine SKUs into a live Shopify listing — ecom and worn imagery generated in Higgsfield, a name-vs-material compliance audit, Palmonas-style dash-free copy, a reviewable HTML doc, and a batched push to Shopify. Use whenever the user asks to list, publish, onboard, launch or "do the same process" for SKUs, to build a listing doc for Lovable or the ecom dashboard, to shoot PDP or on-body images for products, or to push products with images and descriptions to Shopify.
---

# SKU listing process

Takes raw SKUs with supplier references and produces live, compliant, well-photographed Shopify listings.

## The shape of it

Seven stages. Stages 2 and 3 run in parallel; everything else is ordered.

1. Build the manifest
2. Generate images (agents) ‖ 3. Write copy (agent)
4. Audit names against materials
5. Assemble the review doc
6. Push to Shopify
7. Verify against the supplier photographs, then activate

Never publish before the user has seen the doc. Default every product to Draft.

---

## 1. Manifest

One JSON record per SKU: `sku`, `name`, `cat`, `desc`, `our`, `mrp`, `pal`, `score`, `gid` (Shopify product GID), `product_media` (Higgsfield reference UUID), `product_desc` (the sourcing description of the real object), `existing` (shots already generated).

**`product_desc` is the source of truth for every factual claim.** Not the product title. Titles drift from reality constantly; the sourcing text does not.

Find the Shopify GID by SKU:
```graphql
products(first: 50, query: "vendor:'Naira Petite'") { edges { node { id title variants(first:1){edges{node{sku}}} } } }
```

Existing Higgsfield work lives in generation history, not uploads — page `show_generations` with `type: "image"`, filter for the plinth prompt signature (`IMAGE 2 = the set` / `plaster display block`), and group by `input_images[0].id` to recover one product per reference.

---

## 2. Images

Two mandatory slots per SKU, then extras:

| Slot | Content | Required |
|---|---|---|
| 1 | Ecom shot on the cream plaster plinth | yes |
| 2 | Worn shot, on the body | yes |
| 3+ | Further ecom angles, then editorial | preferred |

Both prompt systems are in `references/prompts.md`. Copy the blocks verbatim — they are the reason 60+ images read as one shoot.

**Ecom.** Product reference first, plinth set reference second. The `REST AND CONTACT` block is non negotiable: without it rings render balanced on a cube edge with the band vanishing, which reads instantly as fake. Rings specifically must stand on the bottom arc of the shank with a real contact shadow (this is the Palmonas convention — check their PDPs).

**Worn.** Model reference first, product reference second. The single most important rule is the crop: **the frame cuts below the nose, no eye in frame**. Full-face renders are where the uncanny valley lives. Luxury jewellery campaigns crop to lips, jaw, neck and collarbone precisely so attention lands on the product. Hold wardrobe, hair, light and lens constant across the whole batch; vary only the pose, drawn from the per-category pose library.

Run generation through Sonnet subagents in batches of ~12 with `generate_image_batch` + `jobs_wait`. Give each a worklist file and `references/agent-generation.md`. Budget ~2 credits per generation and check `balance` first.

---

## 3. Copy

One Opus agent, brief in `references/agent-copy.md`. Two rules dominate:

**No dash characters at all.** Not em dashes, not en dashes, not hyphens. The client's position is that dashes read as AI writing. Reword rather than hyphenate: "18k gold tone plated", "tarnish free", "four claw set". Details use `Key: value`. Verify programmatically before accepting the output — check for `-`, `—`, `–` and every Unicode `Pd` character.

**Material honesty.** Green stones are cubic zirconia, never emerald. Clear stones are cubic zirconia or zircon, never diamond. Silver-coloured pieces are rhodium plated silver tone, never sterling. Pearls are freshwater only where the sourcing says so, otherwise shell pearl.

House style follows Palmonas: short evocative opener, then what the piece is using "features / finished with / set with", then a closing line on when to wear it. Then `STYLING TIP:`, a `Details` list, `Care`, and a closing box line. Pull live examples from `palmonas.com/products.json` if the voice needs recalibrating.

---

## 4. Audit

Compare every title against its `product_desc` and produce a change list in four tiers:

1. **Compliance** — a named material the product does not contain. Gemstone names on simulants and "pearl" on imitation are the two that matter under the Consumer Protection Act 2019.
2. **Wrong object** — the name describes a different piece entirely (studs that are hoops, a "set" that is one item, a "heart" with no heart).
3. **Wrong category** — breaks dashboard filters and collection membership.
4. **Minor** — defensible but imprecise.

Fix categories before titles: moving a product between collections after it has traffic loses the URL. Renaming regenerates the handle, so set a redirect unless the product is still Draft.

---

## 5. Review doc

`references/build_doc.py` is the generator. It emits three things, because a document alone is not usable:

- a self-contained HTML doc, auto-tuned under 10MB
- `assets/<SKU>_<n>_<main|worn|alt|editorial>.jpg` at full resolution
- `products.csv` and `products.json` as a feed

Send it and wait. This is the checkpoint.

---

## 6. Push to Shopify

Images need staged uploads, since locally processed files have no public URL:

1. `stagedUploadsCreate` with `resource: IMAGE, httpMethod: PUT` — batch ~50 inputs per call
2. `curl -X PUT --upload-file` each one (parallel, from bash)
3. `productCreateMedia` with the `resourceUrl` values
4. `productUpdate` for title, `descriptionHtml`, `productType`, `tags`, `status`

Batch 8 products per call using GraphQL aliases (`m0:`, `m1:` …), which turns ~200 calls into ~12. Write each batch to a file and hand execution to a Sonnet agent — it keeps the long payloads out of the main context.

**Any SKU whose data is internally contradictory stays Draft**, regardless of image quality. A price that assumes two pieces on a single-piece product, or a metal spec that contradicts the site-wide claim, is not something to publish and fix later.

Verify against the store afterwards rather than trusting the agent's report: count active products, check `mediaCount` per product, and read back a description to confirm it is dash free.

---

## 7. Verify against source, then activate

Everything above checks the listing against itself. This stage checks it
against the factory. Full brief in `references/agent-source-verify.md`.

Build one comparison sheet per SKU (supplier photo beside the published
images), split them across three Opus agents, and judge metal colour first
since that is where most failures are. Then act on the verdicts: pass goes
Active, a copy only failure gets its copy fixed and goes Active, an image
failure stays or returns to Draft until reshot, and unverifiable is reported
rather than quietly passed.

Run this even on SKUs that are already live. The first pass over a live
catalogue of sixty found twenty four mismatches, four of them on products
that had been active for a day.

## Things that go wrong

- **Rings floating.** The most common and most damaging failure. Always include the rest-and-contact block.
- **Background removal.** `rembg` with `isnet-general-use` runs locally at zero credit cost, but a cutout on plain white can look worse than the plinth shot — always show the user before publishing. Downscale to ~1400px first or it is very slow; skip `alpha_matting` unless edges genuinely need it.
- **NSFW refusals** on worn shots usually trace to a "chest-up" instruction colliding with a leftover "no model" clause inherited from the plinth prompt. Strip the contradiction and reframe as a closed-collar neck crop.
- **Sibling SKUs that contradict each other** (necklace says paperclip, matching bracelet says curb). Resolve toward whichever the images and the parent agree on, and flag it for supplier confirmation.
- **Low contrast.** Ivory garment on ivory ground with warm skin gives gold nothing to separate against. A saturated ochre silk fixes it.
- **Tag inheritance.** Silver and rose-gold pieces silently keep an "18k Gold Tone Plated" tag unless the tag builder branches on plating.
- **MCP responses over ~50k characters** are written to a file instead of returned. That is useful: request extra fields to force it, then drive the follow-up work from bash.

## Files

- `references/prompts.md` — the ecom and worn prompt systems, plus pose libraries
- `references/agent-generation.md` — brief for generation subagents
- `references/agent-copy.md` — brief for the copy agent
- `references/agent-verify.md` — brief for the image verification gate
- `references/build_doc.py` — doc, assets and feed generator
- `references/agent-source-verify.md` — brief for the supplier photo verification gate
- `references/shopify.md` — mutations, batching and verification queries
