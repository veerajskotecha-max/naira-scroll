# Shop All: "Never just one" (5 Nov 2026)

The ask: rate the competitor screenshots and the Naira Twenty ads out of 10, compare GIVA and Palmonas captions with
Naira's, then make a Shop All campaign from Naira's own high-CTR creatives: 40 creatives, the best 10 picked and fixed,
with captions, headlines and the Shop now button, at ₹1,000 a day, linking to Shop All.

Nothing here has been created on Meta or changed on Shopify.

## The link

Shop All is `https://nairaflore.com/jewellery` (the live "All pieces" page; `/shop` and `/collections/all` redirect there).
Each ad adds `utm_source=meta&utm_medium=paid&utm_campaign=shopall_nov26&utm_content=<ad>` so it can be read in Shopify.

## What was done

1. **Ratings** (`research/competitor_ratings.json`, `research/naira_twenty_ratings.json`): the 16 screenshots (GIVA,
   Palmonas, Snitch, Lenskart) and the 20 Naira Twenty ads, each rated out of 10 for clicks from a cold scroll, with
   what Naira should take from each.
2. **Captions** (`research/captions_comparison.json`, `research/caption_rules.md`): GIVA and Palmonas captions against
   Naira's, and the rules the new captions follow. The Meta Ad Library tool returns each ad's headline but not its
   caption, and the snapshot pages refused automated access, so no competitor caption was invented: the comparison uses
   their real headlines, keyword counts across their live ads (codes, warranty, waterproof, Diwali Sale) and the earlier
   competitor study in `docs/research/01-competitor-corpus.md`. Opening the snapshot links in a signed-in browser would
   give the full captions.
3. **Photo pool** (`research/pool.json`): only photos Naira has already run or listed, chosen by their Meta results
   ("Almost edible." 6.21%, rangoli 6.10%, Woven Gold Hoops 5.8-6.1%, the catalogue carousels' on-model photos). Sold-out
   winners (the Ruby tennis bracelet, Molten Bloom Hoops) and pieces with 3-4 units left were kept out. No new photos.
4. **40 creatives** (`research/concepts.json`, `research/brief.md`, `research/build_rules.md`): 20 concepts, each a Feed
   (1080x1350) and a Story (1080x1920), built in HTML over the pool photos and rendered.
5. **Judging** (`research/judging.json`): three independent judges (a media buyer, a creative director, a fact checker)
   scored all 40 images; a creative director picked 10 as a set; each pick was fixed and then checked again by a
   reviewer who had not seen it. All ten passed on the first re-check (7.5-8 out of 10 for cold-scroll clicks).
6. **Captions for the ten**: primary text, headline and description per ad, checked for banned words, prices against
   Shopify, the "130+ pieces from ₹599" fact and the exact offer wording.
7. **Plan** (`plan.json`, from `build/make_plan.py`): campaign setup, rules for the first two weeks, the live account
   snapshot and the things to know before spending.

## The ten (`ads/`)

| # | Ad | Hook on the image | Role |
|---|---|---|---|
| 1 | C17 | Unpopular opinion: Repeat the lehenga. Never the earrings. | Native text post, five priced earrings |
| 2 | C18 | Nobody wears one choodi. | Three bracelets add up to the Buy 3 |
| 3 | C02 | Rangoli, sorted by price. | The 6.10% rangoli photo as the site's price filters |
| 4 | C07 | Masala dabba, restocked. | Seven priced pieces in a spice tin |
| 5 | C12 | Q7. Didi's sangeet. Which one? (d) All of the above | Exam question; the answer is the Buy 3 |
| 6 | C10 | Solah shringar, weekday edit. | Five on-model pieces, ear to finger |
| 7 | C03 | Mummy's saree. My chain. | Bold Nocturne Chain plus three priced pieces |
| 8 | C19 | Teen patti. Deal yourself any three. | Card night; the only one that says COD |
| 9 | C01 | Almost edible. | The account's proven 6.21% photo |
| 10 | C11 | Kisko kya. | A gifting list: Mummy, Didi, me |

`ads/fallback/` holds C19 with the headline "Card night." in case Meta's review objects to the card game.
`ads/other/` holds the ten that were made but not picked; `research/judging.json` says why each sat out.

## The board

Published as a private artifact: https://claude.ai/artifact/EennScYjuLekNowJ6nqvv3 (share it from the page's Share menu).
`research/changes.json` holds the plain-English note of what changed in each ad after review, written by comparing the
before and after images. After the re-check, the C01 Story photo was lifted so the whole bracelet clears Meta's Shop now
button.

## Rebuilding the board

```
python3 build/make_plan.py                 # writes plan.json
python3 build/board.py <out_dir>           # writes <out_dir>/index.html
```

The board expects web-sized copies in `<out_dir>/ads/`, `<out_dir>/thumbs/` and `<out_dir>/screens/`.
`build/src/<ad>/` keeps the final Feed and Story HTML of the ten. Their image paths point at the session's working folder
(the pool photos and a few cut-outs made from them), so they document the layouts rather than rebuild offline.

## Round two: the aesthetic ten

Ten quieter, editorial Shop All ads from the same photo pool are in `aesthetic/` (board: https://claude.ai/artifact/2ffJxDVLpi13HuoGHk537S).

## Waiting on the owner

- Approval to create the campaign on Meta (nothing has been created).
- What "10:10" meant: a 10:10 AM start, or ten ads at ₹100 each (the plan covers both).
- Whether to pause Winners revived (0.76x ROAS, last 7 days) to fund this without raising total spend.
