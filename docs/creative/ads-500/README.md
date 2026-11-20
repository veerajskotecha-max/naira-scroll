# Ads 500: static Meta ads made on Higgsfield (19–20 Nov 2026)

The owner asked for crazy, perfect static ads in batches of five, each batch better than the last, only for pieces with 20 or
more in stock, until the Higgsfield credits ran out. This folder is that run: the study of our winning ads, the kit, four
batches, a zero-credit pass after the credits ended, and the records. **Nothing has been uploaded to Meta.**

Review board (Feed and Story for every ad, scores, Meta text): __BOARD_URL__

## Where it ended

__RESULT_SUMMARY__

## The batches

| Batch | Pictures (credits) | Ads shipped | Fix target | New move | What it taught |
|---|---|---|---|---|---|
| b01 | 10 (20) | 1: b01-1 (b01-4 held on re-score) | first batch | Five archetypes on five SKUs (A6, A13, A1, A4, A2) | Generated pieces drift to the centre; a sliding Feed crop (RULINGS §4) replaced fixed positions. Construction locks held on all five pictures. |
| b02 | 10 (20) | 2: b02-1, b02-5 | desire | The worn Woven pair, camera behind (b02-1) | Worn frames lift desire, but hair and body compete with the piece at 200 px; scale must be built (referent, contact shadow). |
| b03 | 7 (14) | 4: b03-1, b03-2, b03-3, b03-5 | stop power, through the piece | Brushed A4 monument on a plum glaze (b03-1) | The magnified product-only hero on a dark or saturated ground is our strongest frame (b03-1 7.99, b03-2 7.96). |
| b04 | 7 (14) | 4: b04-0, b04-1, b04-3, b04-4 | desire | A worn neck-and-collarbone crop (b04-1, Toggle) | Pictures one at a time with the last credits; the worn crop shipped, and b04-3 (selective colour) is the best b04 ad. |
| zero credit | 0 | none new; b04-1 improved | the hand-off | Story offer, headline variants, Prism rescue, single-winner re-test | See below. |

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
`build/meta_upload.csv` from the ledger. Only rows whose verdict starts with "ship" are included. A headline variant (`<id>h`)
names its ad in the `variant_of` column.

## Before anything goes to Meta

- Nothing is uploaded. Upload only after the owner says so.
- Re-read stock and the discount codes on the day: every shown variant must still have 20 or more. Serpentine Whisper Chain
  Silver (23) and Monochrome Enamel Hoops (24) are close to the floor.
- Upload the Feed (1080 × 1350) and Story (1080 × 1920) of each ad as one ad with placement-specific images. A headline
  variant goes in as a second creative of its ad, so Meta splits them; it is never a separate ad.
- The URLs carry UTM tags only (`utm_content={{ad.id}}` is filled by Meta).

## Credits

- This run generated 34 pictures at 2 credits each: 68 credits (b01 10, b02 10, b03 7, b04 7, plus one refused job that was
  refunded).
- The account's balance also fell by about 154 credits between 16:40 and 17:07 UTC on 19 Nov through generations that were not
  part of this run (another session or user on the same account). The balance is now 0.46.

## The zero-credit pass and the clean blind re-test

__ZERO_CREDIT__

## What the next credits should buy

__NEXT__
