# Creative slate — six concepts

`../NAIRA_Creative-Slate_Six-Concepts.pdf` — 9 pages. A decision document, not a shoot document.

Two hooks were rejected before this ("Green." and "Guess which one."). Rather than guess a third
time, this puts six concepts up and asks for a pick. Once one is chosen the full package —
beat sheet, shot list, read sheet, caption file — gets rebuilt around it.

## Why the first two failed, which turned out not to be a taste question

- **Orlando Wood, *Lemon* (IPA/System1, 200 ads).** Splits ads into *left-brain* features —
  flatness, isolated product features, on-screen text, voiceover, abstraction — and *right-brain*
  features: whole scenes, characters, place, dialogue, humour, expression. The more left-brain
  features, the lower the Star rating, which predicts share growth. Over 80% of ads never clear
  3 stars. Both rejected scripts were the losing list almost item for item.
- **System1 × TikTok × WPP Media, *Creator Effectiveness Playbook* (2026).** 1,217 paid ads,
  8 markets, 182,550 respondents. *Showmanship* (characters, humour, environments) raises
  emotional response; *salesmanship* (on-screen text, hard CTAs, facts and figures) **lowers it
  7–12%**. The second script was wall-to-wall spec chips and price chips.
- **Fluent devices.** A recurring character is worth 2.4 vs 1.9 stars, +37% on share growth,
  +30% on profit growth — and usage has collapsed to ~4% of US ads. Highest-ROI structural
  choice available, and almost abandoned.
- **Ranking signals moved.** DM sends carry ~3–5× the weight of a like for non-follower reach;
  comments have fallen to ~3% of ranking weight from ~15% in 2023. "Guess which one" was
  engineered to farm a signal that has collapsed.

## A correction carried forward

Both earlier scripts were justified partly on "it has to work on mute — most people watch without
sound." **That 85% figure is Facebook-feed-era; Instagram's own data is that ~80% of Reels are
watched with sound ON.** The design rule becomes: the visual gag must land silently, but the line
is the payoff and the audio should not be neutered. `../NAIRA_UGC_Teardown_Hooks_VO-Reel_Plan.pdf`
still carries the old framing in §10 and should be amended when it is next touched.

## The commercial case

A live Meta Ad Library pull (17 Sep 2026) found GIVA running ~423 active ads, Palmonas ~678,
Rubans ~127 — nearly all selling a percentage off. **Entertainment-led paid creative in Indian
jewellery is an empty lane.** Even brands with funny organic voices run boring paid ads.

## The six

| | Concept | Device | Note |
|---|---|---|---|
| 01 | Okay, that's how these ads usually go | category parody, then the real demo | **Recommended to shoot first** — crazy with a floor under it |
| 02 | The Bracelet Committee | recurring character, saas-bahu, rule of three | **Recommended to build** — the campaign, not the ad |
| 03 | Types of people who ask where you got it | native Indian "types of…" fast-cut | Lowest execution risk |
| 04 | One problem | Bernbach flaw-admission | Most elegant; lowest brand risk |
| 05 | Because we have a problem | true fact, deadpan, register drop | Uses the best unused fact in the catalogue |
| 06 | Since March | bathos; positioning as a joke | Only one that leads with the chain |

## Two things the slate establishes regardless of the pick

1. **The bracelet leads, not the chain.** Product photography was finally examined: the Bold
   Nocturne is chunky, gold, paperclip-linked and reads like a ₹10,000 piece. The gap between how
   it looks and what it costs *is* the idea. Both earlier scripts led with the chain.
2. **Emotional creative is a split, not a replacement.** Binet & Field: emotional campaigns show
   very large effects on new customers in 31% of cases vs 5% for rational — but their prescription
   is to run both. The existing demonstration script should run alongside, not be deleted.

## Build

```
python3 -c "
from playwright.sync_api import sync_playwright
import pathlib
src = pathlib.Path('creative/naira-ugc/slate/slate.html').resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                          args=['--no-sandbox','--allow-file-access-from-files'])
    pg = b.new_page(); pg.goto(src, wait_until='networkidle'); pg.wait_for_timeout(2500)
    pg.pdf(path='creative/naira-ugc/NAIRA_Creative-Slate_Six-Concepts.pdf', format='A4',
           print_background=True,
           margin={'top':'16mm','bottom':'14mm','left':'14mm','right':'14mm'})
    b.close()"
```

Fonts resolve from `../script-card/fonts/` via `fonts.css`; copy that directory alongside if
building elsewhere.
