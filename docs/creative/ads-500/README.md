# Ads 500: static Meta ads made on Higgsfield (19–20 Nov 2026)

The owner asked for crazy, perfect static ads in batches of five, each batch better than the last, only for pieces with 20 or
more in stock, until the Higgsfield credits ran out. This folder is that run: the study of our winning ads, the kit, four
batches, a zero-credit pass after the credits ended, and the records. **Nothing has been uploaded to Meta.**

Review board (Feed and Story for every ad, scores, Meta text): https://claude.ai/artifact/5KyJcJ1XJMj6VswYQB8g9F (private until the owner shares it). Rebuild it with the command below.

## Where it ended

**7 ads are ready**, each with a Feed (1080 × 1350), a Story (1080 × 1920) and Meta text, from 34 pictures across four
batches. All 7 passed the ship rule (PLAYBOOK §7) on the files that ship, scored by fresh critics who never saw a key or an
earlier score (`build/retest/REPORT.md`):

| Ad | Product | Price | Fresh audit mean |
|---|---|---|---|
| b04-3h | Verdant Circlet Studs | ₹899 | **8.19** (best) |
| b03-1 | Brushed Gold Huggies | ₹699 | 8.16 |
| b01-1 | Cushion Halo Ring | ₹999 | 8.12 |
| b03-2 | Cushion Halo Ring | ₹999 | 7.88 |
| b02-5 | Verdant Eternity Band | ₹1,049 | 7.78 |
| b04-0 | Monochrome Enamel Hoops | ₹999 | 7.74 |
| b03-3 | Halo Curve Ring | ₹899 | 7.51 |

Mean 7.91. Held after the audit: b02-1 (worn hoops oversized, with an invented loop), b04-1 (the worn Toggle chain is lost at
feed size; strong at full size, the owner may test it), b03-5 (the pearl renders pink), b04-4 / b04-4h (abstract headline,
then an extra jump ring). b04-3h replaced b04-3, whose headline read as "wear one".

## The batches

| Batch | Pictures (credits) | Ads shipped | Fix target | New move | What it taught |
|---|---|---|---|---|---|
| b01 | 10 (20) | 1: b01-1 (b01-4 held on re-score) | first batch | Five archetypes on five SKUs (A6, A13, A1, A4, A2) | Generated pieces drift to the centre; a sliding Feed crop (RULINGS §4) replaced fixed positions. Construction locks held on all five pictures. |
| b02 | 10 (20) | 2: b02-1, b02-5 | desire | The worn Woven pair, camera behind (b02-1) | Worn frames lift desire, but hair and body compete with the piece at 200 px; scale must be built (referent, contact shadow). |
| b03 | 7 (14) | 4: b03-1, b03-2, b03-3, b03-5 | stop power, through the piece | Brushed A4 monument on a plum glaze (b03-1) | The magnified product-only hero on a dark or saturated ground is our strongest frame (b03-1 7.99, b03-2 7.96). |
| b04 | 7 (14) | 4: b04-0, b04-1, b04-3, b04-4 | desire | A worn neck-and-collarbone crop (b04-1, Toggle) | Pictures one at a time with the last credits; the worn crop shipped, and b04-3 (selective colour) is the best b04 ad. |
| zero credit | 0 | none new | the hand-off and the audit | Story offers, headline variants, clean blind re-test, fresh audit, fix round z2 | See below. The final audit holds b02-1, b03-5, b04-1 and b04-4, and swaps b04-3 for b04-3h, so 7 ads ship. |

Pictures that never shipped are kept in each batch's `pics/` and explained in its `verify.md` and `review.md`. Every ledger
row says why it shipped, was held, dropped or rejected (`build/ledger.json`).

## Folders

- `RULINGS.md`: the rules in force (owner decisions on claims and new pictures, stock and offers read live, the crop rule,
  headline variants). It overrides `PLAYBOOK.md` where they differ.
- `PLAYBOOK.md`: the study of our winning and losing ads, the archetypes (A1–A15), the scoring rubric (§7) and the ship rule.
- `kit/`: the ad kit (Velista, Cormorant Garamond and Jost; the F2 card; offer and size-tag styles) and `render.cjs`, which
  renders each HTML page to JPG and fails on font fallback, overflow or text outside the safe area.
- `build/`: the ledger, `learnings.md` (rules and notes carried from batch to batch), the anchors (tested winners and losers
  used in the blind sheets), product references and the board builder.
- `batches/bNN/`: per batch, `brief.md`, `jobs.json` (the Higgsfield prompts), `pics/` (the generated pictures),
  `verify.md` (construction and true-size checks), `review.md` (both critics), `loop.md` (the changes for the next batch), and
  every ad as `<id>_feed.html/.jpg`, `<id>_story.html/.jpg` and `<id>.copy.json` (Meta text, landing URL with UTMs, scores).

## Rebuild the board and the Meta sheet

```
cd docs/creative/ads-500
python3 -I build/board/make_board.py <out_dir>
```

This writes `<out_dir>/index.html` with web copies of every shipped Feed and Story in `<out_dir>/img/`, and rewrites
`build/meta_upload.csv` from the ledger. Only rows whose verdict starts with "ship" are included. The sheet carries both the
batch critics' mean (`score_mean`) and the fresh audit mean (`audit_mean`). A live headline variant would name its ad in
`variant_of`; none is live now (b04-3h replaced its control and ships as the ad itself).

## Before anything goes to Meta

- Nothing is uploaded. Upload only after the owner says so.
- Re-read stock and the discount codes on the day: every shown variant must still have 20 or more. Monochrome Enamel Hoops
  (24 on 20 Nov) is closest to the floor.
- Upload the Feed (1080 × 1350) and Story (1080 × 1920) of each ad as one ad with placement-specific images. A headline
  variant, if one is ever made live, goes in as a second creative of its ad, so Meta splits them; it is never a separate ad.
- The URLs carry UTM tags only (`utm_content={{ad.id}}` is filled by Meta).

## Credits

- This run generated 34 pictures at 2 credits each: 68 credits (b01 10, b02 10, b03 7, b04 7, plus one refused job that was
  refunded).
- The account's balance also fell by about 154 credits between 16:40 and 17:07 UTC on 19 Nov through generations that were not
  part of this run (another session or user on the same account). The balance is now 0.46.

## The zero-credit pass and the clean blind re-test

After the credits ran out (balance 0.46):

1. **b04 loop changes at zero credits** (`batches/b04/zero-credit.md`): an offer in every Story, three headline variants, a
   Prism rescue (rejected) and a single-winner anchor re-test.
2. **That re-test's blind was compromised** (the critics' prompts named the anchors), so it was run again with coded sheets
   and fresh critics. The clean read reversed it: our product-led ads beat both winning anchors at 200 px. The same critics
   put the winners near the bottom although both sold, so this read is a craft check, not a sales forecast.
3. **A fresh audit** of every live creative (two critics, two runs each, neutral codes) found truth faults the batches had
   passed and two headlines that failed copy. **Fix round z2** changed words and text placement only (size lines, card-line
   hooks), each change checked by an independent verifier, and **round 2** re-scored the shipped files.

The full method, every table and the raw scores are in `build/retest/`.

## What the next credits should buy

Each picture is 2 credits. In order:

1. **Replace the held pictures**: a true-size Woven worn frame without the loop; a Pearl Double Halo frame with a warm-white
   pearl; a Serpentine pendant with the bail straight on the basket; a Toggle frame where the clasp is at least 15% of the width.
2. **Loop changes 5–8** in `batches/b04/loop.md`: Toggle paperclips on a light A3 ground, the Brushed Huggies float, one
   Prism try, and a named device in every brief slot.
3. **Keep the base grammar** that won every blind read: the magnified product-only hero on a dark or saturated ground, with a
   size line and a headline the picture proves (`build/learnings.md`, rules 11 and 15–17).
4. **Run the 7 live ads with real spend** before trusting any critic ranking against the winners.
