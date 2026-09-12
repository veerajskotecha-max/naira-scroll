# NAIRA — 21 paid-social creatives (4:5)

Built from the two HD plate campaigns: **VIII Lilac Hour** (9 plates) and **VI Soft Matter**
(10 plates). Nothing here has been uploaded anywhere.

## What this is

Twenty-one creatives in **twenty-one different constructions**. The set before this one ran a
single layout — image, eyebrow, display line top-left, wordmark bottom-left — across 38 files.
That is a template, not a campaign, and no amount of re-ragging the line fixes it. What holds this
set together is the brand, not the layout: Velista 400 display, Jost 300 support, the house
palette, one wordmark, a 6% side-safe strip.

| | id | construction | role | rating |
|---|---|---|---|---|
| Lilac Hour | N01 | specimen sheet | brand · craft proof | 8.6 |
| | N02 | angled field on the photograph's own diagonal | brand | 9.0 |
| | N03 | deep band anchored to a dark in frame | brand + proof | 9.0 |
| | N04 | commerce tray | direct response | 9.2 |
| | N05 | circle window | brand | 8.7 |
| | N06 | vertical climbing line | brand | 9.3 |
| | N07 | swap grid, two cells | demonstration | 8.5 |
| | N08 | whisper | brand (quiet beat) | 7.8 |
| | N09 | overprint at poster scale | thumbstop | 9.4 |
| Soft Matter | N10 | margin column | brand · editorial | 8.4 |
| | N11 | coral top band | demonstration | 9.1 |
| | N12 | ticker strips | brand · craft proof | 8.9 |
| | N13 | zoom pair | actual size | 8.8 |
| | N14 | diptych | range | 8.6 |
| | N15 | side panel | brand + price | 8.3 |
| | N16 | arch window | brand + price | 9.0 |
| | N17 | floating card | direct response | 8.7 |
| | N18 | radial rules | brand | 8.8 |
| Brand | N19 | type poster | brand poster | 9.0 |
| | N20 | price ladder | direct response · anti-discount | 9.2 |
| | N21 | giant numeral | direct response · price floor | 9.3 |

Average 8.84. Four are built to sell directly (N04, N17, N20, N21); five more carry a price.
Twelve carry no offer at all, which is the position: in 498 live competitor creatives the brand
that discounts in 0% of its copy holds the best median impression rank of six, and the one that
discounts in 80% ranks second worst.

## Files

- `1080x1350/` — upload-ready JPEG, quality 92, **4:4:4** (no chroma subsampling)
- `contact/` — the two labelled review sheets
- `build/` — the compositor, the QA harness and the specs

## Build

```
python3 build/studio.py build/ads.json out --bare     # renders, plus a type-hidden pass for QA
python3 build/qa2.py   build/ads.json out ads_bare    # contrast, safe area, clipped marks
python3 build/fit.py   build/ads.json                 # every line measured against its own box
```

Masters render at 1080×1350 with `device_scale_factor` 4/3, i.e. 1440×1800.

## Verification

`qa2.py` renders each creative twice — once normally, once with every glyph set transparent —
and differences the two. Grounds, rules, borders and chips are identical in both passes, so the
difference is exactly the marks and the ground under them. Marks are then grouped into blocks and
split by polarity, and each block is measured once: its nominal ink against the ground it sits on.

This matters because three earlier versions of the check were wrong and all three said the work
was failing when it was not:

1. Hiding elements with `visibility:hidden` also removed a CTA chip's own ink ground, so cream
   type was measured against the cream tray behind the chip — 1.5:1 for a run that is 15:1.
2. Testing pixels individually counts antialiased glyph edges, which are a blend of ink and paper
   and measure about 2:1 against the paper by arithmetic alone, however black the type is.
3. Grouping a cream-on-ink chip with the ink-on-cream caption 26px above it and averaging the two
   gives mid-grey against mid-grey.

Current state: **21/21 clean** — every block ≥ 4.5:1, every mark inside the 6% strip except the
two creatives that declare a bleed (N09's poster-scale line, N12's marquee), nothing clipped.

Two things the checks cannot see, and a human should: whether the line is *true* of the picture it
sits on, and whether the crop of a detail is the detail the caption names. Both were wrong here at
least once (N13's inset cropped blank chalk under a caption reading "the wavy ring") and both were
found by looking, not by measuring.

## Not done

These are 4:5 masters only. 1:1 and 9:16 are **not** auto-croppable from them — that is exactly
what produced the last set's failures, where a centre crop guillotined left-aligned type and a 1:1
crop dropped the wordmark. Those placements need their own layouts.
