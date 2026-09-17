# "Guess which one." — shooting script

**Naira Petite · paid social · 9:16 · 28.0s · creator: Sejal**

| | |
|---|---|
| Pieces | Charm Box Chain ₹2,149 (`YF5146`) · Bold Nocturne Bracelet ₹1,999 (`YF5144-BRA`) |
| Spoken | 56 words · ~2.75 words/sec · ~20.4s of speech |
| Silent | Hook demo 1.8s · tap 2.6s · end card 1.2s |
| Shots | 12 · mean ~2.3s |
| Deliver | MP4 · H.264 · 1080×1920 · 30fps · AAC 128kbps · −14 LUFS · −1.0 dBTP |

---

## The hook is not a sentence

Frame one is a **test being run**, not a face and not a claim. Two gold chains lie side by side,
near-identical. One hand twists both. One kinks and stays kinked; the box chain springs back
straight. The only words on screen are **"ONE OF THESE IS ₹2,149."**

Then: *"Guess which one."*

The viewer has to answer a question before they can leave. That is the whole device — and because
it is a physical demonstration rather than a spoken claim, it works with the sound off, which is
how most of the audience will see it.

---

## The voiceover, continuous

> *[twist — no voice]* "Guess which one. In a photo you genuinely cannot tell. The difference is
> the link. That one's open. This one's a box chain. Square links, so it holds its shape.
> *[tap — no voice]* Surgical steel underneath the gold. Anti-tarnish sealed. Two years on the
> plating. Chain twenty-one forty-nine. Bracelet nineteen ninety-nine. Seven-day returns. COD.
> Tap Shop Now."

Delivery: curious, not salesy. "Guess which one" is a real question — leave a beat after it.

---

## Beat sheet

| In | Out | Voiceover | Picture |
|---|---|---|---|
| 0.0 | 1.8 | *silent* | **THE HOOK — one unbroken take.** Two chains side by side on a plain surface, both gold, visually near-identical. One hand twists both at once. The cheap one kinks and stays. The box chain springs back straight. Foley: the twist, live. |
| 1.8 | 3.4 | "Guess which one." | Hold on the two chains, still. Let the question sit. |
| 3.4 | 6.2 | "In a photo you genuinely cannot tell." | Both chains flat and still, lit and shot **like a product photo** — this is the shot where they look identical. That is the point. |
| 6.2 | 8.4 | "The difference is the link." | Macro on the cheap chain's link: stamped, open, gapped. |
| 8.4 | 11.4 | "That one's open. This one's a box chain." | Cut between the two links in **matched framing** so the eye compares without being told to. |
| 11.4 | 14.2 | "Square links, so it holds its shape." | Box chain draping over the fingers, settling. |
| 14.2 | 16.8 | *silent — water only* | **THE TAP — one unbroken take.** Wrist with the bracelet, chain at the neck, under running water, 3s, out, one shake, to camera still wet. |
| 16.8 | 19.6 | "Surgical steel underneath the gold. Anti-tarnish sealed." | Macro, bracelet's flat curb faces catching light as the wrist turns. |
| 19.6 | 21.6 | "Two years on the plating." | Lobster clasp closing, macro, with the click. |
| 21.6 | 24.4 | "Chain twenty-one forty-nine. Bracelet nineteen ninety-nine." | Both pieces worn — wrist and neck in one frame. |
| 24.4 | 26.8 | "Seven-day returns. COD. Tap Shop Now." | Natural light, small smile, point at the button. |
| 26.8 | 28.0 | *music resolves* | 1.2s end card **over live footage of the chain**, not a flat colour. Loops. |

---

## Graphics track

Separate from the captions in `guess-captions.srt`. Never more than one graphic on screen with a caption.

| In | Out | Element | Placement |
|---|---|---|---|
| 0.0 | 9.0 | `#Ad` | **Top third.** Nine seconds = one third of runtime (ASCI). |
| 0.2 | 1.8 | `ONE OF THESE IS ₹2,149` | Upper-middle, over the demo. **The price is on screen at 0.2s.** |
| 6.2 | 8.2 | `LOOK AT THE LINK` | Top third |
| 8.4 | 11.4 | `OPEN` → `BOX CHAIN · SQUARE LINKS` | Top third, one per link as they cut |
| 14.2 | 16.8 | `NO CUTS. ONE TAKE.` | Top third |
| 16.8 | 19.6 | `SURGICAL STEEL BASE` · `ANTI-TARNISH SEALED` | Top third, stacked |
| 19.6 | 21.6 | `2-YEAR PLATING ASSURANCE` | Top third |
| 21.6 | 24.4 | `₹2,149` · `₹1,999` · `+ ₹150 INSURED DELIVERY` | Beside the pieces in frame |
| 24.4 | 26.8 | `7-DAY RETURNS` · `COD` · `↓ SHOP NOW` | Lower, above the caption band |
| 26.8 | 28.0 | `NAIRA PETITE · nairaflore.com/jewellery` | Over live footage |

---

## Caption spec

Import `guess-captions.srt`, then set:

- **68–76 px**, weight 700–900, one geometric sans, one weight throughout
- White with a **3–5 px dark stroke** plus soft shadow (y 2–4 px, 30–40%, blur 8–12). **No box.**
- **Fixed band, y = 1150–1330.** Never lower — below y=1420 is Instagram's own chrome on a paid Reel.
- Max 2 lines, ≤32 characters per line
- Hard cut-in on the beat. **No per-word wobble, bounce or scale.**

Safe zones, paid Reel, 1080×1920: **top 260 px · bottom 500 px · right 150 px below y≈600 · left 60 px.** Preview on a real phone before export.

---

## Audio

| | |
|---|---|
| Music | 85–105 BPM, **no vocal**, licensed for paid use — Meta Sound Collection, Epidemic or Artlist. **Never Instagram's trending audio in a paid ad.** |
| Hook | Music enters **on the spring-back**, not at 0.0. The first sound is the twist itself. |
| Ducking | 12–16 dB under VO · attack 20 ms · release 400 ms |
| Bed level | −26 to −30 dBFS under speech, rising to −16/−18 dBFS in the two silent gaps |
| Foley | Twist + spring-back (0.0, live) · water (14.2, live) · clasp click (19.6). −18 to −22 dBFS, ducking music a further 3–6 dB for 300 ms around each hit |
| VO chain | HPF 70–80 Hz → denoise → EQ → comp 3:1, atk 5–10 ms, rel 60–100 ms, 4–6 dB GR → de-ess 5–8 kHz → limiter |
| Master | −14 LUFS integrated, −1.0 dBTP |
| Silence | **None.** Music resolves under the end card. |

Turn **off** Advantage+ *Music* and *Image animation* at ad level — Meta enables them by default and will lay an unbriefed bed over the voiceover.

---

## Grade

Correct, don't style. Neutralise every shot to one white balance → match exposure **on skin** → match black level → one light shared look, trimmed per shot.

- **Critical for this script:** the two chains in the hook must be graded **identically**. If one reads warmer or brighter than the other, the "you can't tell them apart" beat collapses and the ad has no hook.
- **Gold:** pull saturation out of the *orange* range while holding *yellow*; roll highlights to near-white rather than clipping orange.
- **Skin:** Indian skin sits slightly *below* the standard vectorscope skin line. Grade to that. No global warm push.
- **Targets:** shot-to-shot mean luminance within ±15, R−B skew within ±8.
- No film emulation, no halation, no heavy vignette, no teal shadows.

---

## Hard rules

1. **The hook take and the tap take may not be cut.** An edit inside either one makes the proof worthless.
2. **If the box chain doesn't actually spring back on camera, stop.** The hook depends on it. Tell us and use the fallback below. Never fake a proof.
3. **The comparison chain is Sejal's own old one.** No brand named, no packaging or logo in frame.
4. **A tap — never a pool, bath or sea.** The FAQ allows incidental contact only.
5. **Never say "waterproof."** Never say "18K gold" — these are 18K gold-**plated** over steel.
6. **No wear-log claim.** She has just received the pieces. The construction is the proof, not time.
7. **Any spoken price carries delivery on the chip** (`+ ₹150 insured delivery`).
8. **"Tap Shop Now"** — never "link in bio."
9. No false urgency, no personal attributes, no outcome guarantee.

---

## Fallback hook, if the twist doesn't perform

**The drop.** The bracelet's own product copy opens *"Weight, worn plainly."* Drop both chains onto
a hard surface from about 15cm, in one take. The cheap one tinkles and skitters; the Nocturne lands
with a dull, solid sound and stays put. Same on-screen line — `ONE OF THESE IS ₹2,149` — same
"Guess which one." Everything from 3.4s onward is unchanged.

This version leans harder on sound, so keep the on-screen text doing the work for muted viewers.

---

## Files

- `guess-script.md` — this document
- `guess-captions.srt` — burned-in captions, timed, import-ready (CapCut / Premiere / Resolve)
- `guess-teleprompter.pdf` — one page, large type, words and timings only, for the read
- `../NAIRA_Guess_Script-Card_Sejal.pdf` — the full creator brief, kit list and shot list
