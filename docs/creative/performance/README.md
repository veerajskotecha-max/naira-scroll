# Naira Petite performance ads (22 Oct 2026)

This folder holds five new photographs for each of 28 products and 268 finished Meta ads built from them. It also has the
plan for four new campaigns that test one format each. The 28 products are every product with 30 or more units in stock on
22 Oct, plus the Heartbead Bracelet.

## What the ads copy, and why

The formats come from the account's own results (Meta, main ad account, 15–22 Oct; lifetime for "Almost edible.").

| Format | Copies | Result | Overlay |
|---|---|---|---|
| rhyme | Edition Two fruit plates; "Almost edible." | Stories 2.75× (ruby anaar 2.94×); best seller, 10 sales | Feed: Velista capitals, italic correction, spec, CTA, price ("Almost edible." / "Sweet On You."). Story: no text |
| silk | "The gold note." | 2.38× on 3 sales | italic headline, two lines, name · price |
| worn | Catalogue E2 on-model carousel | 2.21× on 5 sales | as silk |
| quiet | Apricot camp, Woven Gold Hoops | 1.72× on 5 sales | wordmark above, name and price below |
| play | "THE WIDTH.", "Rolling for miles", "Rangoli, in a line." | highest outbound CTR | as rhyme |

## Contents

- `BRIEF.md`: the shoot brief every worker followed (formats, composition, prompt order, verification).
- `plates/<handle>-<format>.jpg`: 134 verified photographs at 1080×1920, with no text. Six slots are empty after their
  reshoots; their reasons are in the manifests.
- `ads/<handle>-<format>-<feed|story>.jpg`: 268 finished ads, Feed 1080×1350 and Story 1080×1920.
- `build/shots_g*.json` and `build/products_g*.json`: prompts, job IDs, scores, notes, locks and references.
- `build/ad_copy.py`: the copy for every ad. It writes `copy.json` (overlays), `meta.csv` (the upload sheet: primary text,
  headline, CTA, URL with variant and UTMs, campaign, ad set, wave) and `plan.json`.
- `build/perf_ads.py`: renders the ads. A script in each page scores the photograph on a 24 px grid and places the copy
  where it is calmest and reads best: ink or cream type, never across the jewellery.
- `build/review_a.json` and `build/review_b.json`: the two independent full-size reviews of every ad.
- `build/board.py` and `build/board_template.html`: the published page (plan, ads, images, verification board).
- `build/sheet.py` and `build/ads_sheet.py`: the review contact sheets.

## Rebuilding

```
python3 build/ad_copy.py                      # copy.json, meta.csv, plan.json
<venv>/bin/python build/perf_ads.py [prefix]  # ads/
<venv>/bin/python build/board.py              # the page, in <scratchpad>/perf/artifact
```

## Product truth

Every claim follows the live listings: gold tone or silver tone, cubic zirconia, white shell pearl. Never "real",
"diamond", "waterproof" or "tarnish-free". The bundle offer in the primary text uses the live codes BUY2 and BUY3.

Pearl Circlet Studs are held as reserves until someone confirms its listing: the copy says gold tone, but every photo shows
silver tone.
