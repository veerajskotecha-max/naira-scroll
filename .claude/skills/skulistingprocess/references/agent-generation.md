# Generation agent instructions — Naira Petite listing shots

You are generating ecommerce PDP images in Higgsfield for a jewellery listing doc.

## Your worklist
A JSON array. Each item has: `idx`, `sku`, `cat`, `tag`, `prompt`, `media` (product reference UUID), `set_ref` (plaster-block set reference UUID).

## How to run each item
Use `mcp__higgfield__generate_image_batch` with up to 12 requests per call.
For each item build one request:

```
{ "index": <idx>,
  "params": {
    "model": "nano_banana_2",
    "prompt": <prompt verbatim, do not edit or shorten>,
    "aspect_ratio": "3:4",
    "medias": [
      {"role": "image", "value": "<media>"},
      {"role": "image", "value": "<set_ref>"}
    ],
    "use_unlim": false
  } }
```

Order matters: product reference FIRST, set reference SECOND. The prompt refers to them as IMAGE 1 and IMAGE 2.

Then poll with `mcp__higgfield__jobs_wait` (max 12 jobs, timeout_seconds 15) until `all_terminal`.
Do NOT call `show_generations`. Do NOT call `job_display` per job.

## Recording results — REQUIRED
After each batch is terminal, append a JSON file to `/tmp/naira_work/listing/gen_log/` named `<yourname>_<batchnumber>.json`:

```
[{"sku":"...","tag":"...","job_id":"...","status":"completed","url":"<result url>"}, ...]
```

Take the result URL from the jobs_wait response. If a job failed or was rejected, record `"status":"failed"` and re-submit that one item once with the same prompt. If it fails twice, record it and move on.

## Rules
- Never edit the prompt text. It carries a product lock that keeps the piece accurate.
- Do not skip items. Work through the whole list.
- If `generate_image_batch` returns `unlim_choice`, re-call with `use_unlim: false`.
- If you run out of credits, stop, write what you completed to the log, and report the shortfall.
- Report at the end: how many completed, how many failed, and the log filenames.
