# Final audit: clean blind re-test, fresh audit and fix round z2 (20 Nov 2026)

No Higgsfield credits were used (balance 0.46). This replaces the anchor results of `batches/b04/zero-credit.md`, whose blind
was compromised: the critics' prompts named which tile was which anchor.

## What ships

**7 live ads**, each passing PLAYBOOK §7 on the files that ship, with fresh critics who never saw a key or an earlier score:

| Ad | Product | Fresh audit A / B | Mean | Blind 200 px |
|---|---|---|---|---|
| b04-3h | Verdant Circlet Studs, ₹899 | 8.38 / 8.00 | **8.19** | beats both winners and both losers with both critics |
| b03-1 | Brushed Gold Huggies, ₹699 | 8.21 / 8.11 | 8.16 | beats both winners and both losers with both critics |
| b01-1 | Cushion Halo Ring, ₹999 | 8.25 / 7.99 | 8.12 | beats apricot and both losers with both critics (F2 with B) |
| b03-2 | Cushion Halo Ring, ₹999 | 7.88 / 7.89 | 7.88 | beats both winners and both losers with both critics |
| b02-5 | Verdant Eternity Band, ₹1,049 | 7.88 / 7.67 | 7.78 | beats both winners and both losers with both critics |
| b04-0 | Monochrome Enamel Hoops, ₹999 | 7.84 / 7.65 | 7.74 | beats both winners and both losers with both critics |
| b03-3 | Halo Curve Ring, ₹899 | 7.55 / 7.47 | 7.51 | beats apricot and both losers with both critics (F2 with B) |

Mean of the 7: **7.91**. Every other creative of the run is held, replaced, rejected or dropped, each with its reason in
`build/ledger.json`.

**Held or replaced in this audit:**
- **b02-1** (Woven worn): all four audit runs measured the hoops at about 1.4–1.5× their listed 25 mm and saw a small loop at
  the bottom of each hoop that the real piece does not have (truth A 0 / B 3). A picture fault.
- **b04-1** (Toggle worn neck crop): strong at full size (8.20), but on the blind 200 px sheets it beats no loser with both
  critics; all four ranked it in their bottom three because the thin chain is lost on skin at feed size. The owner may still
  choose to run it as a test of the worn frame.
- **b04-3** → replaced by **b04-3h**: "ONE BOLD EAR IS ENOUGH." sits over a pair and reads as "wear one" (copy 5.25 / 5.75).
- **b04-4** → replaced by **b04-4h**, which is also held: an added jump ring between bail and basket that both listing photos
  lack, and the card names the chain without "Silver" at the silver variant's ₹899 (truth B 7.25).
- **b03-5** (Pearl Double Halo): the pearl renders blush-mauve against the listing's warm white, and the pavé reads frosted
  (truth B 7.50 in round 2, 7.75 in round 1). A picture fault.

## How it was run

1. **Clean blind 200 px re-test.** Four coded sheets of 200 × 250 tiles: each held our creatives plus one winning and one losing
   anchor (sheet 1 apricot + p2, sheet 2 F2 + sa08), in a different order for each critic, with random two-character codes. Four
   fresh critics (A twice, B twice) saw only their sheet. The key never left the lead's session until the scores were in. A tile
   beats an anchor when its score is higher; a tie goes to the anchor. `beatsWinner` / `beatsLoser` need both critics to beat
   the same anchor.
2. **Fresh audit, round 1.** The 13 live creatives (11 ads and 2 headline variants) were copied to neutral codes with their Meta
   text and listing pointers. Critic A ran twice and critic B twice; each scored every ad alone on the §7 rubric, without access
   to the ledger, reviews or earlier scores. Dimension means of the two runs give each critic's score.
3. **Fix round z2.** Nine creatives got one change each to words or text placement, never to a picture; three fixers, each
   checked by an independent verifier (renders, contrast, px/mm, lint, diff). "Shown magnified" is printed only at 19+ Feed px
   per listed mm; below that the size is stated plainly. b04-0's headline could not go on the Feed (the hoops and shadows are
   700 px tall against the 550 px gate), so the lead put the hook in its card line.
4. **Round 2.** The nine fixed creatives went through the same blind sheets (new codes, new orders) and the same audit, with
   the house size rule added to the audit brief, which round 1 had left out.

## What the blind test can and cannot say

On a truly blind read, fresh critics put our product-led ads above both winning anchors, and put the winners themselves near
the bottom: apricot 5.5 / 2.5 and F2 5.5 / 5.5 in round 1, apricot 4 / 4 and F2 5.5 / 4.5 in round 2. The 19 Nov compromised
read said the opposite. Both winners sold in real spend, so a 200 px critic read clearly does not predict sales on its own: it
rewards a large, bright piece and punishes a prop or body that leads. Treat "beats a winner" as a craft signal, not a forecast.
Only live spend can rank these ads against the winners.

## Evidence

Raw and mapped scores, the coded sheets and the keys are in this folder: `blind_raw_20nov.json`, `blind_mapped_20nov.json`,
`audit1_raw_20nov.json`, `audit1_mapped_20nov.json`, `round2_raw_20nov.json`, `round2_mapped_20nov.json`, `blind_s1-4.jpg`,
`blind2_t1-4.jpg`, `keys.json`. The mapping scripts are `blind_map.py`, `audit_map.py` and `round2_map.py`.

### Round 1 blind (pre-fix files; anchors: apricot A 5.5 / B 2.5, F2 5.5 / 5.5, p2 4.0 / 4.0, sa08 4.5 / 4.0)

| Ad | Thumbs A | Thumbs B | Apricot A/B | F2 A/B | p2 A/B | sa08 A/B |
|---|---|---|---|---|---|---|
| b03-2 | 7.5, 8.5 | 8.5, 8.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b02-5 | 7, 8 | 8, 7.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b03-1 | 8.5, 6.5 | 7, 8 | yes / yes | yes / yes | yes / yes | yes / yes |
| b04-0 | 6.5, 7.5 | 7.5, 7.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b03-5 | 7, 7 | 6.5, 6.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b04-3h | 8, 6.5 | 5.5, 7 | yes / yes | yes / yes | yes / yes | yes / yes |
| b01-1 | 6.5, 7 | 6, 7 | yes / yes | yes / yes | yes / yes | yes / yes |
| b04-3 | 7.5, 6 | 5.5, 6.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b03-3 | 6, 5.5 | 5, 5.5 | yes / yes | tie / tie | yes / yes | yes / yes |
| b04-4h | 6, 5 | 4.5, 6 | yes / yes | no / yes | yes / yes | yes / yes |
| b04-4 | 5.5, 5 | 4.5, 5.5 | tie / yes | no / tie | yes / yes | yes / yes |
| b02-1 | 5, 5 | 3, 4.5 | no / yes | no / no | yes / no | yes / yes |
| b04-1h | 5, 4 | 3.5, 4.5 | no / yes | no / no | yes / no | no / yes |
| b04-1 | 4.5, 4 | 3.5, 5 | no / yes | no / no | yes / no | no / yes |

### Round 1 fresh audit (pre-fix files)

| Ad | A | B | Mean | Truth A/B | Copy A/B | Under 6 | Compliance |
|---|---|---|---|---|---|---|---|
| b03-1 | 8.20 | 8.36 | 8.28 | 8.75 / 8.75 | 8.50 / 8.75 | none | pass |
| b04-1 | 8.10 | 8.30 | 8.20 | 8.75 / 9.00 | 7.75 / 8.50 | none | pass |
| b01-1 | 8.19 | 8.16 | 8.18 | 8.00 / 7.75 | 8.50 / 8.50 | none | pass |
| b04-3h | 8.21 | 8.05 | 8.13 | 8.75 / 8.00 | 8.00 / 7.75 | none | pass |
| b03-5 | 8.09 | 8.11 | 8.10 | 7.25 / 7.75 | 8.25 / 8.25 | none | pass |
| b03-2 | 7.81 | 8.04 | 7.92 | 8.50 / 9.00 | 7.00 / 7.25 | none | pass |
| b02-5 | 7.85 | 7.88 | 7.86 | 9.00 / 9.00 | 7.25 / 7.25 | none | pass |
| b04-4h | 7.61 | 7.88 | 7.74 | 7.75 / 9.00 | 7.25 / 7.75 | none | pass |
| b04-0 | 7.75 | 7.65 | 7.70 | 8.75 / 8.00 | 6.75 / 6.75 | none | pass |
| b04-3 | 7.64 | 7.62 | 7.63 | 8.75 / 8.00 | 5.25 / 5.75 | A copy 5.25, B copy 5.75 | pass |
| b04-4 | 7.36 | 7.60 | 7.48 | 7.75 / 9.00 | 6.00 / 5.75 | B copy 5.75 | pass |
| b03-3 | 7.30 | 7.47 | 7.39 | 7.00 / 7.50 | 8.25 / 8.25 | none | pass |
| b02-1 | 6.47 | 7.06 | 6.77 | 0.00 / 3.00 | 7.75 / 8.00 | A truth 0.00, B truth 3.00 | fail (2 runs) |

### Round 2 blind (shipped files; anchors: apricot A 4 / B 4, F2 5.5 / 4.5, p2 3 / 3, sa08 3.5 / 3.5)

| Ad | Thumbs A | Thumbs B | Apricot A/B | F2 A/B | p2 A/B | sa08 A/B |
|---|---|---|---|---|---|---|
| b03-1 | 8, 8 | 8.5, 8 | yes / yes | yes / yes | yes / yes | yes / yes |
| b02-5 | 7.5, 8.5 | 8, 7.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b04-3h | 8.5, 7 | 7, 7 | yes / yes | yes / yes | yes / yes | yes / yes |
| b03-2 | 7, 6.5 | 6.5, 8.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b04-0 | 6.5, 7.5 | 7.5, 6.5 | yes / yes | yes / yes | yes / yes | yes / yes |
| b03-5 | 6, 6 | 6, 6 | yes / yes | yes / yes | yes / yes | yes / yes |
| b01-1 | 5.5, 5 | 5.5, 5.5 | yes / yes | no / yes | yes / yes | yes / yes |
| b03-3 | 5, 4.5 | 5, 5 | yes / yes | no / yes | yes / yes | yes / yes |
| b04-4h | 4.5, 4 | 4.5, 4 | yes / yes | no / no | yes / yes | yes / yes |

### Round 2 fresh audit (shipped files)

| Ad | A | B | Mean | Truth A/B | Copy A/B | Lowest dimension | Ship rule |
|---|---|---|---|---|---|---|---|
| b04-3h | 8.38 | 8.00 | 8.19 | 9.00 / 8.25 | 8.25 / 7.50 | B fit 6.00 | pass |
| b03-1 | 8.21 | 8.11 | 8.16 | 8.50 / 8.50 | 8.50 / 8.50 | A fit 7.00 | pass |
| b03-5 | 8.35 | 7.94 | 8.14 | 9.00 / 7.50 | 8.50 / 8.25 | B desire 7.25 | fail: truth B under 8 |
| b01-1 | 8.25 | 7.99 | 8.12 | 8.50 / 8.00 | 8.75 / 8.50 | B stop 7.50 | pass |
| b03-2 | 7.88 | 7.89 | 7.88 | 8.50 / 8.75 | 7.25 / 7.25 | B desire 7.00 | pass |
| b02-5 | 7.88 | 7.67 | 7.78 | 9.00 / 8.75 | 7.25 / 7.50 | A fit 6.50 | pass |
| b04-0 | 7.84 | 7.65 | 7.74 | 8.75 / 8.25 | 7.00 / 7.00 | B fit 6.75 | pass |
| b04-4h | 7.76 | 7.55 | 7.66 | 8.50 / 7.25 | 8.00 / 8.00 | A fit 6.75 | fail: truth B under 8 |
| b03-3 | 7.55 | 7.47 | 7.51 | 8.50 / 8.50 | 8.25 / 8.25 | A message 6.00 | pass |

