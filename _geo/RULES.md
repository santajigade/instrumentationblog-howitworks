# Quick Answer rollout (instrumentationblog.in)

Daily job: add a "Quick Answer" box to the next 40 articles in `_geo/queue.json` (sorted by Google impressions).

## Daily steps
1. `git pull`. Dispatch `.github/workflows/geo-fetch.yml` with input `n=40` and wait for it to finish, then `git pull`.
   It writes `_geo/pages/<slug>.json` (id, title, top search queries, placement plan, article text) for pages still `todo`
   and marks pages that already have a box as `has`.
2. For every `_geo/pages/<slug>.json` that has no file in `_geo/applied/` or `_geo/answers/`, write `_geo/answers/<slug>.json`:
   `{"slug": "...", "question": "...", "body_html": "..."}` following the writing rules below.
3. Commit and push the answers, dispatch `.github/workflows/geo-apply.yml`, wait, `git pull`, and check the new rows in `_geo/log.csv`.
   Failed rows: look at the error, fix the answer file if it was the cause, otherwise leave it for the user.
4. Report: how many applied today, how many failed, how many left in the queue (`status == "todo"`).

## Writing rules
- `question`: the main question people search for this page, phrased as a real search question (What is, How to, Difference between, How does...). Use the page's top query from `queries` where it fits. Title Case, max about 70 characters.
- `body_html`: 50 to 90 words. The first sentence answers the question directly and starts with the topic keyword.
- Use only facts that are in the article text (`text`) or are standard textbook engineering facts. Never invent numbers, standards, product names or claims. If the article gives a formula, include it in `<strong>` with a one line worked example using the article's numbers or simple round numbers.
- For "difference / vs / types / parts" topics, a compact table (3 to 6 rows) is better than prose. For "how to" topics, a short `<ol>` of 4 to 6 steps.
- Allowed tags only: `<p style="margin:0 0 8px;">` (last paragraph `margin:0;`), `<strong>`, `<ol style="margin:0 0 0 20px;">`/`<li>`,
  and tables in this style: `<table style="width:100%;border-collapse:collapse;margin:8px 0 4px;font-size:16px;"><tr style="background:#1a2b4a;color:#fff;"><th style="padding:8px;text-align:left;">...` with body rows alternating `#eef4fb` and `#fff`, cells `<td style="padding:8px;">`.
- No headings (h1 to h6) inside the box. No links. No em dash or en dash characters anywhere (use commas, "to", or the minus sign "−" for maths).
- If a page is not a real article (list page, thin page, unclear topic), do not write an answer: set its queue status to `skip` instead.
