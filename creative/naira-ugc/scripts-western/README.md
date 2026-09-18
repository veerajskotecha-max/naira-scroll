# Five scripts — Western register (Sejal)

`../NAIRA_Five-Scripts_Western_Sejal.pdf` — 9 pages. Five complete scripts, written out
line by line with timecodes, not concepts.

## What changed

A reference photo of the creator arrived: beige co-ord, cropped bolero, thigh-slit column skirt,
chunky black boots, travertine hotel corridor, low moody light, mirror selfie.

**That killed the previous six concepts.** `../slate/` was built on broad desi comedy — three
aunties in dupattas convening a committee, a mock courtroom with a wooden spoon, an aunty grabbing
a wrist at a wedding. Those are written for a creator whose act is playing Indian family
archetypes. This creator's act is taste. The concepts would have read as a brand handing a script
to someone it doesn't watch.

## What the photo gives instead

1. **A specific place.** Travertine, low light, a hotel corridor at night. Sense of place is one of
   the highest-value right-brain features in the effectiveness research and most UGC has none.
2. **Bad light, which is usable.** Gold that still reads well under a hard yellow hotel downlight
   is a genuine quality signal. Nobody in the category has made that the test.
3. **Styling that wants the bracelet.** Beige, cream, black boots, bare arm. Bold Nocturne is the
   best thing in the catalogue against that palette; the Charm Box Chain nearly disappears on it.

## The five

| | Script | Device | Length |
|---|---|---|---|
| 01 | **The bad lighting test** | the location becomes the proof; reusable as a series | 27s |
| 02 | Downstairs | bathos — total overcommitment to nothing | 26s |
| 03 | I remember | withholding, then caving; fashion gatekeeping | 24s |
| 04 | The ones that didn't make it | elimination; the reveal is that it was on the whole time | 28s |
| 05 | Not a decision | the getting-ready truth; the versatility case | 24s |

**Recommendation:** shoot 01 as episode one of a series (lift, restaurant, auto at night, club
bathroom — the premise survives repetition and episodes 2–10 cost almost nothing). Shoot 03 the
same afternoon; it is two setups in the same corridor. Hold 05 for retargeting, where warm
audiences want reassurance rather than a joke.

## Research carried over unchanged

- Character, place, dialogue, humour — the features that separate ads that work from ads that
  don't. The character here is her, played straight, rather than an archetype.
- Showmanship over salesmanship: on-screen text, hard CTAs and fact stacks lower emotional
  response 7–12%, so the specs sit inside the lines rather than in chips.
- Written for sound ON (~80% of Reels), not for mute.
- Built for the DM forward, not the comment.
- Deadpan, never mean — all the comedy is self-directed.

## Open question flagged in the doc

Script 04 uses "it has been on since March" and a piece of her own jewellery that discoloured in
April. Both are the best beats in that script and **both are only usable if literally true.**
The elimination structure survives without them but loses its two strongest lines.

## Build

```
python3 -c "
from playwright.sync_api import sync_playwright
import pathlib
src = pathlib.Path('creative/naira-ugc/scripts-western/west.html').resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
                          args=['--no-sandbox','--allow-file-access-from-files'])
    pg = b.new_page(); pg.goto(src, wait_until='networkidle'); pg.wait_for_timeout(2500)
    pg.pdf(path='creative/naira-ugc/NAIRA_Five-Scripts_Western_Sejal.pdf', format='A4',
           print_background=True,
           margin={'top':'16mm','bottom':'14mm','left':'14mm','right':'14mm'})
    b.close()"
```
