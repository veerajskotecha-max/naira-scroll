# Rewrite product copy in Palmonas house style, with zero dashes

This copy goes live on nairaflore.com today. Accuracy first, style second.

## Input
`/tmp/naira_work/listing/COPY_INPUT.json` — 42 SKUs. Each has:
- `title` (already corrected, use it verbatim), `category`, `price`, `mrp`
- `sourcing_description` — the description of the REAL object. This is the source of truth for every fact.
- `current_details`, `current_description` — an earlier draft. Accurate but written in a different voice.
- `audit_note` — where the old name was wrong and why.

## THE HARD RULE: NO DASH CHARACTERS AT ALL

Not one em dash, en dash or hyphen anywhere in your output. Not in the description, not in the details, not in the styling tip.

- `—` and `–` are banned outright. Rewrite the sentence.
- Hyphens are banned too. Write "18k gold tone plated" not "gold-plated". "tarnish free" not "tarnish-free". "four claw setting" not "four-claw setting". "silver tone" not "silver-tone". "rose gold plated" not "rose-gold plated". "cushion cut" not "cushion-cut". "18cm" not "18 cm" is fine either way, just never a dash.
- In the details list use a colon, never a dash: `Length: 18cm`.
- If a compound genuinely needs joining, use a space or reword. Never reach for a hyphen.

Run a final check over your own output for the characters `-`, `—`, `–` before you write the file. Any hit means fix it.

## House style (matched to Palmonas)

Their pattern, which you are following:

> A little shimmer can change the whole mood. These earrings feature sleek silver tone hoops finished with radiant crystal drop accents that move beautifully with you. Elegant yet minimal, they are designed to add effortless sparkle to your everyday jewellery collection without feeling too bold.
>
> STYLING TIP: Pair them with a silver bracelet and a satin outfit for a refined evening look.

So, for each SKU:

1. **`description`** — 55 to 85 words in three or four sentences.
   - Sentence one: a short evocative opening. No product name in it.
   - Middle: what the piece actually is, using the real facts from `sourcing_description`. Use "features", "finished with", "set with", "designed to". Warm, simple, confident Indian ecommerce English.
   - Last sentence: why you would wear it, or the occasion.
   - Do not use "stunning", "must have", "elevate your look", "exquisite", "unleash". No exclamation marks.
2. **`styling_tip`** — one sentence, 12 to 20 words, starting with "Pair it with" or "Wear it with" or "Layer it with".
3. **`details`** — 5 to 7 `"Key: value"` strings, drawn only from `sourcing_description`. Typical keys: Size, Length, Stone, Plating, Colour, Material, Closure, Fit. Always include:
   - `Plating: 18k gold tone plated` (or `Rhodium plated silver tone` for the silver ones, `Rose gold tone plated` for R18345A1)
   - `Material: Surgical stainless steel`
   - Omit any spec the sourcing description does not state. Never invent a measurement.
4. **`care`** — one sentence, identical across all 42: `Waterproof and tarnish free, so daily wear and water are fine. Keep it away from perfume and harsh chemicals, wipe with a soft dry cloth and store it flat in its pouch.`

## Material honesty, non negotiable

The brand has a live compliance audit on exactly this. Follow it:
- Green stones are **cubic zirconia**, never emerald. Write "emerald green cubic zirconia".
- Clear stones are **cubic zirconia** or **zircon**, never diamond.
- Where `audit_note` says imitation or shell pearl, write "shell pearl". Where the sourcing says freshwater, write "freshwater pearl".
- Silver coloured pieces are **rhodium plated silver tone**, never sterling silver.
- YF PeachHoop style enamel is **enamel**, never a stone.

## Output

Write `/tmp/naira_work/listing/COPY_FINAL.json`:

```json
{"SKU": {"description":"...", "styling_tip":"...", "details":["Key: value", ...], "care":"..."}}
```

All 42 SKUs. Then verify: no `-`, `—` or `–` anywhere in the file, every SKU present, every details list 5 to 7 entries. Report the counts and confirm the dash check passed.
