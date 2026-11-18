# Page-2 boost (instrumentationblog.in)

Queue: `_p2/queue.json`, articles with Semrush India keywords at positions 11 to 20, sorted by total search volume.
Each item lists the page-2 keywords (`kw`, `pos`, `vol`, `kd`).

## Daily steps
1. Dispatch `.github/workflows/p2-fetch.yml` with `n=40`, wait, `git pull`. It writes `_p2/pages/<slug>.json`
   (id, title, focus keyword, keywords, existing H2 list, placement plan, article text). Items that are not WordPress posts become `notpost`.
2. For each page in `_p2/pages/` with no file in `_p2/applied/` or `_p2/changes/`, write `_p2/changes/<slug>.json`:
   `{"slug": "...", "targets": ["keyword", ...], "html": "..."}`. A good helper pattern is in `p2_batch1` style:
   H2 with inline style `font-size:24px;font-weight:700;color:#0186e0;margin:34px 0 16px;`, optional H3 `font-size:19px;font-weight:700;color:#1a2b4a;margin:20px 0 10px;`,
   tables `width:100%;border-collapse:collapse;margin:14px 0;font-size:16px;` wrapped in `<div style="overflow-x:auto;">`, header cells blue `#0186e0` with white text, cells `border:1px solid #cfe3f5;padding:8px 10px;text-align:left;`.
3. Commit, push, dispatch `.github/workflows/p2-apply.yml`, wait, pull, check `_p2/log.csv`.

## Writing rules
- Write ONE new section (150 to 300 words) that targets the page-2 keywords the article does not already answer well.
- The H2 must contain the highest volume keyword exactly (or a natural question form of it). Use the other keywords naturally in the text.
- Do not repeat an existing H2 (check `h2s`). Add what is missing: a direct definition, a quick reference table, a formula table,
  a spec table, step by step working, types table, examples table or a range/dimension table.
- Start the first paragraph with the keyword in bold and answer it directly.
- Only standard textbook engineering facts or facts in the article text. Never invent product claims, prices or standards clauses.
- No em dash or en dash characters. No links. No images.
- Skip pages that are not real articles (MCQ lists, download lists): set queue status `skip`.
