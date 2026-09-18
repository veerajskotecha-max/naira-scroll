# FINAL — "I almost didn't order it"

`../NAIRA_FINAL_Script_I-Almost-Didnt-Order-It.pdf` — one page, A4. The locked shooting script.

29.0s · 9:16 · 71 words · ~2.7 w/sec · 10 beats · clean room, window light, tripod ·
Western styling, sleeve pushed back · Bold Nocturne Bracelet on the wrist from frame one.

## The offer, integrated rather than appended

Running promotion: **any 2 = 20% off, any 3 = 30% off.**

| | Pays | Per piece | Saves |
|---|---|---|---|
| One | ₹1,999 + ₹150 delivery | ₹1,999 | — |
| Any two | **₹3,198** | ₹1,599 | ₹800 |
| Any three | **₹4,198** | ₹1,399 | ₹1,799 |

(Worked on the ₹1,999 bracelet. A mixed bracelet + chain pair is ₹4,148 → **₹3,318**.)

Bolting `BUY 2 GET 20%` onto the end would undo the script. The whole ad is her admitting she
doubted the price — so the strongest available proof is that **she went back and bought more.**
That is revealed preference, not a claim, and it makes the ladder read as a consequence of the
story rather than a pitch. The offer lands at 20.0s as `"Then I went back for two more."`, and the
percentages follow at 22.6s.

**Strategically this is also the first offer that serves the AOV target.** Two pieces lands at
₹3,198 against an ₹1,800–2,400 goal. A bundle ladder is the one form of discount that raises order
value rather than devaluing the single unit — which is a materially different thing from the
sitewide percentages the BRAND.md competitor audit warns against.

## Why this script

Objection-first: across 52 DTC accounts the family ran 15–25% lower CAC than benefit-led hooks on
cold traffic, and at ₹3,000/day the account is almost entirely cold. It is the only one of the five
that names the catch out loud — `"The catch is it's plated. It's not solid gold and it never said
it was."` — which is exactly why it is believed.

## Two things to confirm before recording

1. **Did Sejal actually buy these?** The script is a first-person purchase story. If the pieces were
   gifted or barter, neither `"I almost didn't order this"` nor `"then I went back for two more"` is
   true. Swap 0.4 to *"I'll be honest, I didn't expect much from this"* and 20.0 to *"And if you're
   getting more than one —"*. Slightly weaker, entirely honest.
2. **Is the ladder really "any two", and does it stack with NAIRA10?** The script says *any*. If it
   is SKU-restricted or the cart won't combine it with the code, the on-screen chips must say so —
   a viewer who hits a different number at checkout is a complaint, not a sale.

## Build

```
python3 -c "
from playwright.sync_api import sync_playwright
import pathlib
src = pathlib.Path('creative/naira-ugc/final-script/one.html').resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                          args=['--no-sandbox','--allow-file-access-from-files'])
    pg = b.new_page(); pg.goto(src, wait_until='networkidle'); pg.wait_for_timeout(2200)
    pg.pdf(path='creative/naira-ugc/NAIRA_FINAL_Script_I-Almost-Didnt-Order-It.pdf',
           format='A4', print_background=True,
           margin={'top':'10mm','bottom':'8mm','left':'12mm','right':'12mm'})
    b.close()"
```

It fits one page with ~1mm to spare. If you add a line, measure before assuming — emulate print
media and compare `documentElement.scrollHeight` against 279mm of usable height, because the screen
layout under-reports by several millimetres.
