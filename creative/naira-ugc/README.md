# NAIRA — UGC teardown, hook library & voiceover reel plan

`NAIRA_UGC_Teardown_Hooks_VO-Reel_Plan.pdf` — 36 pages, A4.

## What this is

A forensic review of `af12f0f3-naira-ugc-final-1.10x-split.mp4` (Riya, 33.4s, 9:16),
a hook bank written against the live Naira Petite catalogue, and the production
plan for the voiceover reel that replaces it.

The reel rates **5.4/10** on a ten-dimension weighted rubric. The earlier gut call of
5/10 was right. Twenty-three defects are logged; sixteen are fixable on the existing
timeline without a reshoot, which is worth roughly **5.4 → 7.6**.

## The measurements (all taken from the file, not estimated)

| | |
|---|---|
| Duration / format | 33.40s · 1080×1920 · 30fps · h264 · AAC 48kHz |
| Shots | 16 · mean 2.09s · median 1.97s · 0.48 cuts/sec |
| Longest shots | 4.57s (hook), 4.60s (ring), 3.30s (end card) |
| Loudness | −13.4 LUFS integrated · −1.0 dBTP · LRA 7.0 |
| Music bed | **none** |
| Tail 30.5–33.4s | **−inf dBFS — true digital silence** |
| VO | 88 words · 0.00–30.16s · ~175 wpm |
| Caption band | y = 1396–1512 of 1920 → **21% bottom clearance** (Meta rec. 35%, BRAND.md 40%) |
| Brand bug contrast | **1.21:1** — functionally invisible |
| Grade spread | mean luma 96–201 · R−B skew +25 to +80 |

## The four findings that matter

1. **The hook anchors at ₹2,500 when the hero is ₹1,199.** The strongest number in the
   catalogue never appears — not spoken, not on screen, not once.
2. **Captions sit inside Instagram's reserved chrome for the whole ad.** Moving them up
   200px is a 30-minute job and the highest return per minute in the document.
3. **No music, no foley, and 2.9s of literal digital silence over a static end card.**
4. **The hook is in the positive-discovery family** — the baseline row of the CAC table.
   Objection-first ran 15–25% lower CAC and direct-contradiction 25–40% lower on cold
   traffic across 52 DTC accounts, and ₹3,000/day is almost entirely cold.

## Compliance items to clear before spend

- No ASCI disclosure label anywhere. A 33s video needs `#Ad` visible for ~11s, in the
  **top third** (Reels chrome covers the bottom). The advertiser carries the liability.
- The end card says **WATERPROOF**; the site FAQ says incidental contact only and
  "remove before swimming". Write *water-resistant*. Strike "Swim in it" from BRAND.md
  territory two for the same reason.
- Once a price is spoken, name the delivered figure — ₹150 insured shipping makes a bare
  "₹1,199" a drip-pricing exposure under the CCPA dark-patterns guidelines.
- Never write "18K gold" for plated stock — always "18K gold-plated". The Woven Gold
  Hoops PDP currently lists Finish as `18k gold`.
- The 2-year plating assurance **is** substantiated on every PDP — but it is missing from
  `/jewellery`, which is where the ad lands.

## Catalogue facts the scripts are built on (verified 17 Sep 2026)

| Piece | Price | Finish | Rating |
|---|---|---|---|
| Cushion Halo Ring | ₹1,199 | Rhodium · brilliant-cut zircone · 4-prong | 4.9★ (51) |
| Woven Gold Hoops | ₹1,799 | 18K gold finish | 4.9★ (50) |
| Prism Rivière Bracelet | ₹2,499 | Rhodium · brilliant-cut zircone | 4.9★ (51) |

All three: 2-year plating assurance · 7-day returns · ₹150 insured shipping · 3–5 days.

## Build

```
pip install playwright pypdfium2
python3 creative/naira-ugc/build/build.py
```

Fonts (Jost, Cormorant Garamond, JetBrains Mono) are vendored in `build/fonts/`;
Velista is the brand display face, copied from `public/fonts/`. Frame stills in
`build/img/` were extracted from the source reel with ffmpeg.

## Not done

The PDF plans the voiceover reel but does not shoot it. The shot list in §09 assumes a
**real** sixty-day wear log — "day sixty" must be true before it is spoken, or the one
angle the brand owns becomes the one that gets it reported.
