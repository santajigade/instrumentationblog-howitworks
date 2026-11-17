# Title and meta CTR rewrite (instrumentationblog.in)

Queue: `_seo/ctr_queue.json` (pages in Google top 10 with CTR under 1%, sorted by impressions).

## Daily steps
1. Dispatch `.github/workflows/seo-fetch.yml` with `n=30`, wait, `git pull`. It writes `_seo/pages/<slug>.json` with the current
   Rank Math title, meta, focus keyword, top search queries, headings and article text.
2. For each page in `_seo/pages/` with no file in `_seo/applied/` or `_seo/changes/`, write `_seo/changes/<slug>.json`:
   `{"slug": "...", "rank_math_title": "...", "rank_math_description": "..."}`.
3. Commit, push, dispatch `.github/workflows/seo-apply.yml`, wait, pull, check `_seo/log.csv` (it rejects titles over 60 or metas outside 120 to 160).

## Writing rules (from the site's Oct 2026 CTR rules)
- The FIRST focus keyword (before the first comma in `focus_keyword`) must appear unchanged in both title and meta. The meta starts with it.
- Title: 60 characters or less. Prefer to start with the focus keyword; if the top search query is a different wording that contains it
  (for example "AI AO DI DO signals in instrumentation"), lead with the query wording as long as the focus keyword stays intact.
- Add ONE click hook the article really has: Diagram, Pin Diagram, Truth Table, Calculator, Solved Example, Formula, Chart, Comparison Table, Wiring Diagram.
- Use "&" instead of "and" between hooks, "vs" for comparisons. No "Complete Guide", "Explained", "Best Practices", "Everything You Need".
- Meta: 140 to 155 characters. Start with the focus keyword, then the concrete things inside (formulas, values, diagram, table, calculator, example).
  Only facts that are in the article text.
- If the current title and meta already follow these rules and match the top query, keep the title and improve only the meta.
- No em dash or en dash characters. Use "−" only as a maths minus sign.
