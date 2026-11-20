# b04 zero-credit pass (19 Nov 2026, 23:35 UTC)

The Higgsfield balance is 0.46, so no picture was generated. The pass ran b04 loop changes 1, 2, 3, 4 and 7a on existing
pictures, and wrote change 8 into the rules. The records keeper changed no ad page or JPG. Sheets: `sheet_zero.jpg` (the four
new Feeds) and `sheet_zero_story.jpg` (their Stories plus b04-1's new Story).

## What ships now

- **11 live ads, the same 11 as before.** No headline arm and no rescue clears its gate.
- **b04-1** now ships with the offer in its Story. Its mean rose from 7.73 to 7.84.
- **b04-0** ships with A's grammatical Meta primary text.
- **b04-3** ships with the neutral primary-text opener the fixer put in both its arms (Meta only, not re-scored).
- **b04-4 is flagged.** On this re-test it no longer beats a loser anchor with both critics. Its verdict stays ship for the
  lead to decide.

## What each change did

| Change | What was done | Result |
|---|---|---|
| 1. One winner per sheet | Both critics read all 15 Feeds (11 live, 3 arms, 1 rescue) blind at 200 px. Sheet 1 held apricot + p2; sheet 2 held F2 + sa08. In the ledger, `beatsWinnerBy` and `beatsLoserBy` are now maps keyed by anchor file, and the old lists are kept as `beatsWinnerByB04Sheet`. | No ad beats apricot or F2 with either critic. Rule 11 is back to **Note (provisional)**, with its A3 scope sentence. |
| 2. Hand-off matches the files | Each of the 11 ship rows has a `final` block in its `copy.json` (A, B, mean, scored files, the two maps, verdict). Older review blocks are marked `superseded`. `build/meta_upload.csv` was rebuilt from the ledger. | 11 CSV rows; Meta text and means equal the ledger and the `copy.json` files. |
| 3. An offer in every Story | b04-1's Story prints "Code BUY2 · 10% off 2 pieces" on the plum fill at top 640, 72/76 px clear of both strands. | Cues: A 7.5 → 8, B 7 → 8. Both critics prefer the new Story blind. Mean 7.725 → 7.84. |
| 4. Headline arms; b04-0 text | Three one-H1 arms (b04-1h, b04-3h, b04-4h). b04-0 primary text replaced. | None of the arms ships (table below). b04-0's text is 157 characters, with the offer ending at character 122. |
| 7a. Prism rescue | b02-4 try 2 laid out as b04-8 at P 30. After round 1, the fixer added the Story's headline to the Feed and aligned the UTMs. | **Reject.** B's stop is 5.5, and with B the arm lands before the bracelet. Prism goes to 7b when credits come. |
| 8. Device rule | Written into `learnings.md` as starting rule 14. Rules 12 (one winner and one loser per sheet) and 13 (an offer in every Story except a named control) were added with it. | Applies from the next brief. |

## Anchor re-test (11 live ads, blind 200 px)

Thumb scores: A gave the winners 7.5 and the losers 5.0. B gave the winners 7, p2 5 and sa08 4. A tie goes to the anchor.

| Ad | Thumb A / B | Apricot A | Apricot B | F2 A | F2 B | Beats p2 | Beats sa08 |
|---|---|---|---|---|---|---|---|
| b01-1 | 6.5 / 7 | no | tie | no | tie | A, B | A, B |
| b02-1 | 7.0 / 7 | no | tie | no | tie | A, B | A, B |
| b02-5 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b03-1 | 7.0 / 7 | no | tie | no | tie | A, B | A, B |
| b03-2 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b03-3 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b03-5 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b04-0 | 6.0 / 5 | no | no | no | no | A (B ties) | A, B |
| b04-1 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b04-3 | 6.0 / 6 | no | no | no | no | A, B | A, B |
| b04-4 | 5.0 / 5 | no | no | no | no | neither (both tie) | B (A ties) |

**Shares:**
- Beat apricot with both critics: 0 of 11. With either critic: 0.
- Beat F2: the same, 0 with both and 0 with either.
- Beat p2 with both critics: 9 of 11.
- Beat sa08 with both critics: 10 of 11.

On the b04 two-winner sheet, three ads "beat the winner with both critics". Every one of those wins was over vkf18.

**Both critics say the blind was compromised:** their prompts named the anchor letters and the pair sides. A clean re-run
needs prompts without the sheet key.

## Arms and rescue against their controls

Each arm ships only if all of these hold:
- PLAYBOOK §7 passes;
- copy is 8 or more with both critics;
- its mean is at least the control's ledger mean;
- for b04-3h only, fit is 7.5 or more with both critics.

| Creative | Scored round | A | B | Mean | Control mean | Copy A / B | Fit A / B | Beats both losers | Blind pair prefers | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| b04-1h "CLOSES WITH A TURN, / NOT A CATCH." | 2 (Feed 00:16:12, fixed beat) | 7.75 | 7.825 | 7.79 | b04-1 7.84 | 8 / 8 | 8 / 8 | A, B | A: arm by a hair; B: control | **held**: mean under the control's (layout 7 vs 7.5; the H1 drops to Velista 64) |
| b04-3h "THE ONLY COLOUR / IN THE ROOM." | 1 | 7.9 | 8.275 | 8.09 | b04-3 7.91 | **7.5** / 8 | 8 / 8 | A, B | both: arm | **held**: A's copy is 7.5 on record. A said copy becomes 8 once the neutral opener is in. It now is, but A has not re-scored. |
| b04-4h "ONE STONE. / ONE SMOOTH LINE." | 1 | 7.6 | 7.775 | 7.69 | b04-4 7.58 | 8 / 8 | 7 / 7 | **B only** (A ties both) | both: arm | **held**: does not beat the loser with both critics (§7) |
| b04-8 Prism rescue | 2 (Feed 00:16:12, headline added) | 7.225 | 6.975 | 7.10 | none (rescue) | 7.5 / 7.5 | 6 / 6.5 | round 2: sa08 with both; p2 A only | n/a | **reject**: B's stop 5.5 < 6; loop 7a fails with B |

Round 1 for b04-8 was A 7.05 and B 6.7 (mean 6.875). Its blind thumb was 4.0 with both critics, the lowest tile on both
sheets.

## Stock and codes (read-only Shopify GraphQL, 20 Nov 2026, 00:27 UTC)

Each product has one variant (Default Title). No shown variant is under 20, so nothing is flagged "do not launch".

| Product | Stock | Price | Ads |
|---|---|---|---|
| Toggle Link Chain | 77 | ₹999 | b04-1 (b04-1h held) |
| Woven Gold Hoops | 89 | ₹1,049 | b02-1 |
| Brushed Gold Huggies | 58 | ₹699 | b03-1 |
| Verdant Eternity Band | 58 | ₹1,049 | b02-5 |
| Cushion Halo Ring | 45 | ₹999 | b01-1, b03-2 |
| Prism Rivière Bracelet | 39 | ₹2,399 | b04-8 (rejected) |
| Verdant Circlet Studs | 32 | ₹899 | b04-3 (b04-3h held) |
| Halo Curve Ring | 29 | ₹899 | b03-3 |
| Pearl Double Halo Studs | 25 | ₹1,199 | b03-5 |
| Monochrome Enamel Hoops | 24 | ₹999 | b04-0 (4 over the floor) |
| Serpentine Whisper Chain — Silver | 23 | ₹899 | b04-4 (3 over the floor) |

Codes: BUY2 (10% off 2 or more), BUY3 (20% off 3 or more), BUY4 (30% off 4 or more) and NAIRA10 (10% off, no minimum) are
active, matching RULINGS §2. Every price matches.

## Loop tests (all run after the edits)

| Test | Result |
|---|---|
| Every ship row's `scoredFile` and `scoredStory` equal the JPG's `stat -c %y` (11 of 11). New rows match too. | pass |
| C1: every live row has `beatsWinnerBy` keyed by anchor file, with apricot and F2 (and `beatsLoserBy` with p2 and sa08) | pass |
| C1: `beatsWinner` is true only when both critics beat the same winner | pass (false on all rows) |
| C1: rule 11's status matches the re-test (`**Note (provisional)**`), and its text contains "A3" and the loop's scope sentence | pass |
| C1: each re-test sheet holds exactly one `win_` file (sheet 1: apricot; sheet 2: F2) | pass |
| C2: the CSV holds exactly the 11 ship ids | pass |
| C2: CSV primary text, headline, description and URL equal each `copy.json` `meta`; `score_mean` equals (A + B) ÷ 2 to 2 decimals | pass |
| C2: each ship row's `final.mean`, A, B, scored files and verdict equal the ledger; old review blocks are superseded | pass |
| C3: b04-1 Story render is clean (failed, overflow, fallback and outside empty; minFont 26; textShare .065) | pass |
| C3: B's cues are 7.5 or more (8), and A's did not fall (7.5 → 8) | pass |
| C3: every live `*_story.html` except b01-1's contains `class="offer"` | pass |
| C4: arms render clean within their limits: b04-1h .133 (A2 .22), b04-3h .176 (A4 .18), b04-4h .137 (A6 .14); all minFont 26 | pass |
| C4: both critics scored each arm beside its control on single-winner sheets and blind pairs | pass (blind compromised, as noted) |
| C4: the ship gate is applied to each arm | pass (all three held) |
| C4: b04-0 carries A's text: 157 characters, offer ends at 122, no claim word | pass |
| Lint: no signed URL in the records; no banned word in any shipping Meta text | pass |

The records keeper re-rendered every new page into the scratchpad. All are pixel-identical to the shipped JPGs, with clean
lint.

## Open for the lead

- **b04-4:** keep it live or hold it. A ties it with both losers and B ties it with p2. A asks the lead and B to decide.
- **b04-3h:** one A confirmation of copy on the new primary text would release it. Its mean of 8.09 would be the best
  creative in the run.
- **b04-3's live primary text** changed after scoring (Meta only). The scored JPGs are unchanged.
- **Not applied:**
  - b04-8: utm_term `a1` → `a2` (A only), and the ink scrim at .75 (A only).
  - b04-4 / b04-4h: A's thumb-read re-layout (A only).
  - b04-1h: the "A TURN, / NOT A CATCH." H1 (next run).
- **Records:**
  - b04-8 was relabelled "A2 grammar: headline plus card, no beat", as both critics asked.
  - Its scale range (1.09x / 1.19x / 1.28x) is in the ledger.
  - b02-4 stays dropped.
- **Scratch folders deleted as ordered:** `batches/b04/tmp/` was removed, along with the ledger backup inside it. Git HEAD
  holds the pre-pass ledger. Notes in `verify.md` and the b04 `copy.json` files that cite `tmp/` paths now point at deleted
  working files.
- **Nothing was committed.**
