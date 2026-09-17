# "Green." — shooting script

**Naira Petite · paid social · 9:16 · 28.0s · creator: Sejal**

| | |
|---|---|
| Pieces | Bold Nocturne Bracelet ₹1,999 (`YF5144-BRA`) · Charm Box Chain ₹2,149 (`YF5146`) |
| Spoken | 52 words · ~2.65 words/sec · ~20s of speech |
| Silent | 2 proof gaps, ~3s each |
| Shots | 13 · mean ~2.0s |
| Deliver | MP4 · H.264 · 1080×1920 · 30fps · AAC 128kbps · −14 LUFS · −1.0 dBTP |

---

## The voiceover, continuous

> "Green. Every single one of these. And it was never the gold. It's what's underneath the gold.
> These two are surgical steel underneath the gold. *[twist — no voice]* Square links. They hold
> their shape. *[tap — no voice]* Anti-tarnish sealed. Two years on the plating. Bracelet nineteen
> ninety-nine. Chain twenty-one forty-nine. Seven-day returns. COD if you want it. Tap Shop Now."

Delivery: flat and slightly annoyed for the first two lines, then normal. Not performed.

---

## Beat sheet

| In | Out | Voiceover | Picture |
|---|---|---|---|
| 0.0 | 0.5 | *silent* | Hand tips the dish — dead, blackened jewellery clatters onto a hard table. Top-down, close. **Nocturne worn on the hand that tips it.** |
| 0.5 | 2.6 | "Green. Every single one of these." | Stay on the pile, slight push in. |
| 2.6 | 4.6 | "And it was never the gold." | Hard cut — Sejal, both pieces on, neutral. |
| 4.6 | 7.0 | "It's what's underneath the gold." | Macro on a dead chain from her own pile: the link that has gapped open or kinked. |
| 7.0 | 10.2 | "These two are surgical steel underneath the gold." | Macro, box chain square links, rotating. **Match the framing of the dead link exactly.** |
| 10.2 | 13.4 | *silent — music out* | **PROOF ONE — THE TWIST. One unbroken take.** Dead chain twisted, stays kinked → box chain twisted, springs back straight. Same hands, same frame, no cut. |
| 13.4 | 15.6 | "Square links. They hold their shape." | Chain drapes over the fingers and settles. |
| 15.6 | 18.0 | *silent — water only* | **PROOF TWO — THE TAP. One unbroken take.** Wrist under running water, 3s, out, one shake, to camera still wet. |
| 18.0 | 20.4 | "Anti-tarnish sealed. Two years on the plating." | Lobster clasp closing, macro, with the click. Then light across the flat faces as the wrist turns. |
| 20.4 | 23.2 | "Bracelet nineteen ninety-nine. Chain twenty-one forty-nine." | Both pieces worn — wrist and neck in one frame. |
| 23.2 | 25.4 | "Seven-day returns. COD if you want it." | Natural light, small smile. |
| 25.4 | 27.8 | "Tap Shop Now." | Point at the button. Then 1.3s end card **over live footage of the chain**, music resolving. Loops. |

---

## Graphics track

Separate from the captions in `green-captions.srt`. Never more than one graphic on screen with a caption.

| In | Out | Element | Placement |
|---|---|---|---|
| 0.0 | 9.0 | `#Ad` | **Top third.** Nine seconds = one third of runtime (ASCI). |
| 2.6 | 4.4 | `₹1,999` · `₹2,149` | Price chips, beside the pieces in frame |
| 4.6 | 6.6 | `LOOK AT THE LINK` | Top third |
| 7.0 | 9.4 | `SURGICAL STEEL BASE` | Top third |
| 10.2 | 13.4 | `NO CUTS. ONE TAKE.` | Top third |
| 13.4 | 15.2 | `SQUARE LINKS` | Top third |
| 18.0 | 20.4 | `ANTI-TARNISH SEALED` · `2-YEAR PLATING ASSURANCE` | Top third, stacked |
| 20.4 | 23.2 | `₹1,999` · `₹2,149` · `+ ₹150 INSURED DELIVERY` | Beside the pieces |
| 23.2 | 25.4 | `7-DAY RETURNS` · `COD AVAILABLE` | Top third |
| 25.4 | 27.8 | `↓ SHOP NOW` → `NAIRA PETITE · nairaflore.com/jewellery` | Lower, above the caption band |

---

## Caption spec

Import `green-captions.srt`, then set:

- **68–76 px**, weight 700–900, one geometric sans, one weight throughout
- White with a **3–5 px dark stroke** plus soft shadow (y 2–4 px, 30–40%, blur 8–12). **No box.**
- **Fixed band, y = 1150–1330.** Never lower — below y=1420 is Instagram's own chrome on a paid Reel.
- Max 2 lines, ≤32 characters per line
- Hard cut-in on the beat. **No per-word wobble, bounce or scale** — that is the preset tell.

Safe zones for every element, paid Reel, 1080×1920: **top 260 px · bottom 500 px · right 150 px below y≈600 · left 60 px.** Preview on a real phone before export.

---

## Audio

| | |
|---|---|
| Music | 85–105 BPM, **no vocal**, licensed for paid use — Meta Sound Collection, Epidemic or Artlist. **Never Instagram's trending audio in a paid ad.** |
| Ducking | 12–16 dB under VO · attack 20 ms · release 400 ms |
| Bed level | −26 to −30 dBFS under speech, rising to −16/−18 dBFS in the two proof gaps |
| Foley | Pile clatter (0.0) · twist rustle (10.2) · water (15.6, live) · clasp click (18.0). −18 to −22 dBFS, ducking music a further 3–6 dB for 300 ms around each hit |
| VO chain | HPF 70–80 Hz → denoise → EQ → comp 3:1, atk 5–10 ms, rel 60–100 ms, 4–6 dB GR → de-ess 5–8 kHz → limiter |
| Master | −14 LUFS integrated, −1.0 dBTP |
| Silence | **None.** Music resolves under the end card. |

Turn **off** Advantage+ *Music* and *Image animation* at ad level — Meta enables them by default and will lay an unbriefed bed over the voiceover.

---

## Grade

Correct, don't style. Neutralise every shot to one white balance → match exposure **on skin** → match black level → one light shared look, trimmed per shot.

- **Gold:** pull saturation out of the *orange* range while holding *yellow*; roll highlights to near-white rather than clipping orange.
- **Skin:** Indian skin sits slightly *below* the standard vectorscope skin line. Grade to that. No global warm push.
- **Targets:** shot-to-shot mean luminance within ±15, R−B skew within ±8.
- No film emulation, no halation, no heavy vignette, no teal shadows.

---

## Hard rules

1. **Neither proof take may be cut.** An edit between the twist and the release, or between the water and the reveal, makes the proof worthless.
2. **If the box chain doesn't actually spring back on camera, stop.** Tell us; the script changes. Never fake a proof.
3. **A tap — never a pool, bath or sea.** The FAQ allows incidental contact only.
4. **Never say "waterproof."** Never say "18K gold" — these are 18K gold-**plated** over steel.
5. **No wear-log claim.** Sejal has just received the pieces. The construction is the proof, not time.
6. **Any spoken price carries delivery on the chip** (`+ ₹150 insured delivery`).
7. **"Tap Shop Now"** — never "link in bio."
8. No competitor named, no false urgency, no personal attributes, no outcome guarantee.

---

## Files

- `green-script.md` — this document
- `green-captions.srt` — burned-in captions, timed, import-ready (CapCut / Premiere / Resolve)
- `green-teleprompter.pdf` — one page, large type, words and timings only, for the read
- `../NAIRA_Green_Script-Card_Sejal.pdf` — the full creator brief, kit list and shot list
