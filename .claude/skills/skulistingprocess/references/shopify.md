# Shopify push

Store: `nairaflore.com`, INR, Basic plan. Products already exist as Draft, so **update, never create** — creating duplicates SKUs.

## Find products by SKU

```graphql
query($cursor: String) {
  products(first: 50, after: $cursor, query: "vendor:'Naira Petite'") {
    pageInfo { hasNextPage endCursor }
    edges { node { id title status productType variants(first:1){edges{node{id sku}}} } }
  }
}
```

Build a `sku -> gid` map once and cache it.

## Images

Local files have no public URL, so staged upload is the only route.

**1. Get targets** (batch ~50 per call):
```graphql
mutation stage($input: [StagedUploadInput!]!) {
  stagedUploadsCreate(input: $input) {
    stagedTargets { url resourceUrl }
    userErrors { field message }
  }
}
```
with `[{resource: "IMAGE", filename: "SKU_1_main.jpg", mimeType: "image/jpeg", httpMethod: "PUT"}]`

**2. Upload** from bash, parallel:
```bash
curl -s -X PUT -H "Content-Type: image/jpeg" --upload-file "$LOCAL" "$SIGNED_URL"
```
Expect HTTP 200. Pair targets to files by asserting `basename(resourceUrl) == filename` — never rely on array order alone.

**3. Attach**, 8 products per call via aliases:
```graphql
mutation media($p0: ID!, $md0: [CreateMediaInput!]!, ...) {
  m0: productCreateMedia(productId: $p0, media: $md0) { mediaUserErrors { message } }
  m1: ...
}
```
`media` entries are `{originalSource: <resourceUrl>, alt: <title>, mediaContentType: "IMAGE"}`. Order in the array becomes display order, so main first, worn second.

Keep `alt` ASCII. Accented characters in variables have caused encoding trouble; set the accented title via `productUpdate` instead.

## Product fields

```graphql
mutation upd($id: ID!, $t: String!, $d: String!, $ty: String!, $tg: [String!], $st: ProductStatus!) {
  productUpdate(product: {id: $id, title: $t, descriptionHtml: $d, productType: $ty, tags: $tg, status: $st}) {
    product { status } userErrors { message }
  }
}
```

Description HTML:
```html
<p>{description}</p>
<p><strong>STYLING TIP:</strong> {styling_tip}</p>
<p><strong>Details</strong></p><ul><li>Key: value</li></ul>
<p><strong>Care</strong></p><p>{care}</p>
<p>You will receive your piece in a Naira Petite box.</p>
```

Tags: brand, category, `Demi Fine`, `Waterproof`, `Tarnish Free`, `Hypoallergenic`, plus plating and stone. **Branch the plating tag on the actual metal** — silver-tone and rose-gold pieces must not inherit `18k Gold Tone Plated`.

## Execution

Write each batch to `media_batch_<n>.json` / `update_batch_<n>.json` as `{query, variables}`, then hand the list to a Sonnet agent that reads each file and calls `graphql_mutation` with the contents unchanged. This keeps very long payloads out of the main context. Tell it explicitly which batches are already done, and that it must never alter a `status` value.

Run all media batches before any update batch, since updates flip products live.

## Status is not the same as published

**`status: ACTIVE` does not put a product on the storefront.** It only makes it
eligible. A product also has to be published to the Online Store *publication*,
and `productUpdate` never touches that. Fifty two products once sat ACTIVE with
every image and description correct while exactly two were actually reachable
on the web, because the rest had been published to Point of Sale, Google, Meta
and the headless channels but never to Online Store.

Check both, always:

```graphql
active:  productsCount(query: "vendor:'Naira Petite' AND status:active") { count }
onstore: productsCount(query: "vendor:'Naira Petite' AND status:active AND published_status:published") { count }
```

If those two numbers differ, the gap is your live catalogue. Fix it with
`publishablePublish`, aliased 25 per call:

```graphql
mutation pub($chan: ID!, $p0: ID!, ...) {
  x0: publishablePublish(id: $p0, input: {publicationId: $chan}) { userErrors { message } }
}
```

Get the publication id from `publications(first: 10) { edges { node { id name } } }`
and pick the one named **Online Store**. Publishing is additive and idempotent,
so re running it is harmless.

Make this the last step of every push, and re check it after any bulk activation.

## Verify afterwards

```graphql
query {
  active: productsCount(query: "vendor:'Naira Petite' AND status:active") { count }
  draft:  productsCount(query: "vendor:'Naira Petite' AND status:draft") { count }
  products(first: 50, query: "vendor:'Naira Petite' AND status:active") {
    edges { node { title productType mediaCount { count } description } }
  }
}
```

Check: active count equals published-to-Online-Store count, every product at 3+ media, no product over its intended image count (a pipeline test can leave a duplicate — remove with `productDeleteMedia`), and no dash characters in any description.

Renaming does **not** change the handle. Products renamed after going live keep the old URL slug; fix handles and add redirects before driving traffic.

## Deactivating a group

```graphql
products(first: 25, query: "vendor:'Naira Petite' AND status:active AND product_type:Ring")
```
then aliased `productUpdate(product: {id: $x, status: DRAFT})`. Status-only changes leave images, copy and tags intact, so nothing needs rebuilding when the product returns.
