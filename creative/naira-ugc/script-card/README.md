# "Guess which one." — creator script card (Sejal)

`../NAIRA_Guess_Script-Card_Sejal.pdf` — 9 pages, A4, print- and phone-readable.

The shootable script that follows from the teardown in `../NAIRA_UGC_Teardown_Hooks_VO-Reel_Plan.pdf`.

## The two SKUs it is written against

| | Price | MRP | Construction | Base |
|---|---|---|---|---|
| Bold Nocturne Bracelet `YF5144-BRA` | ₹1,999 | ₹3,999 | 18cm thick flat curb link · lobster clasp + extender | surgical stainless steel |
| Charm Box Chain `YF5146` | ₹2,149 | ₹3,309 | fine box chain, square links · CZ charm | surgical stainless steel |

Both: 18K gold-**plated** · anti-tarnish sealed · 2-year plating assurance · 7-day returns ·
₹150 insured shipping · 3–5 working days · 4.9★ (50 / 51).

## The hook is a test, not a sentence

Frame one is a demonstration being run. Two gold chains lie side by side, near-identical. One hand
twists both; one kinks and stays kinked, the box chain springs back straight. The only words on
screen are **"ONE OF THESE IS ₹2,149"** — then: *"Guess which one."*

It opens a loop the viewer has to close before they can scroll, it survives the mute because it is
a picture rather than a claim, and the price is on screen at **0.2s**. An earlier version opened on
a pile of blackened jewellery; it was rejected as too ugly for the brand, and the nearest thing to
it — "No Green Skin. Just Gold." — is already running in the category.

## Why it works without a wear log

Sejal has just received the pieces, so no "I've worn this for months" claim is available. Two facts
in Naira's **own product copy** replace it, and both can be filmed today:

- *"surgical stainless steel"* — the base metal is why plated jewellery fails, and these are built
  on steel. The mechanism the category never explains.
- *"square links that hold their shape and resist twisting"* — a physical, testable claim, which is
  what makes it usable as a hook rather than an adjective.

So the reel carries **two unbroken takes**: the twist at 0.0 and the tap at 14.2. Neither may be
edited in the middle. If the box chain does not spring back on camera the hook does not exist —
the card says so, and carries a fallback (the drop test, leaning on the bracelet's own
*"weight, worn plainly"*).

## Shape

28.0s · 56 spoken words · ~2.75 words/sec · 12 shots · product in frame at 0.0s ·
price on screen at 0.2s · proof acts at 0% and 51% · spoken CTA at 24.4s.

## Compliance baked in

- `#Ad` top third, from 0:00, held 9s (one-third of runtime, per ASCI; gifted counts as paid).
- The comparison chain is Sejal's own old one. No brand named, no logo in frame.
- Never "waterproof" — the site FAQ allows incidental contact only. A tap, never a pool.
  Note the product schema on both PDPs still carries the word `waterproof` in its material
  string; that contradicts the FAQ and should be reconciled on the site.
- Never "18K gold" — always "18K gold-plated". These are plated over steel.
- The price chip carries `+ ₹150 insured delivery` so a spoken figure is never one the
  checkout beats (drip pricing, CCPA dark-patterns guidelines).
- No competitor named, no false urgency, no personal attributes, no outcome guarantee.

## Build

```
python3 -c "
from playwright.sync_api import sync_playwright
import pathlib
src = pathlib.Path('creative/naira-ugc/script-card/card.html').resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                          args=['--no-sandbox','--allow-file-access-from-files'])
    pg = b.new_page(); pg.goto(src, wait_until='networkidle'); pg.wait_for_timeout(2500)
    pg.pdf(path='creative/naira-ugc/NAIRA_Guess_Script-Card_Sejal.pdf', format='A4',
           print_background=True,
           margin={'top':'16mm','bottom':'14mm','left':'14mm','right':'14mm'})
    b.close()"
```

Fonts resolve from `../build/fonts/` and `../build/Velista.ttf`; `card.css` imports
`fonts.css` from this directory, so copy those two paths alongside if building elsewhere.

Typography follows `creative/naira-ads/build/BRAND.md` — Velista display in sentence case,
Jost for support, Cormorant Garamond for quoted script, the house palette — except that body
weight is Jost 400 rather than 300, because this is read on a phone on a shoot rather than
set over an image.

## Files

| | |
|---|---|
| `../NAIRA_Guess_Script-Card_Sejal.pdf` | the creator brief — pieces, kit, script, shot list |
| `../guess-teleprompter.pdf` | one page, large type, words and timings only, for the read |
| `guess-script.md` | shooting script: beat sheet, graphics track, caption/audio/grade specs |
| `guess-captions.srt` | burned-in captions, timed, import-ready |
| `card.html` · `card.css` · `teleprompter.html` | sources |
