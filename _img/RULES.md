# Article images backfill (3 original figures per existing post)

Approved by Santaji on 21 Nov 2026: 20 posts a day, publish directly. Queue: `_img/queue.json` (posts ordered by Google impressions).

## Daily steps
1. `pip install --break-system-packages cairosvg pillow` if missing.
2. Dispatch `img-fetch.yml` with n=20, wait, `git pull`. Each `_img/pages/<slug>.json` has id, focus keyword, search queries, the H2 list (exact text), current image count and the article text.
3. For each fetched page without a file in `_img/changes/` or `_img/applied/`, write `_img/changes/<slug>.json`:
   `{"slug": "...", "figs": [ {name, alt, caption, after_h2, svg} x3 ]}`. Use the helper `_img/svglib.py` (class S: head, box, dia, ar, pl, ln, t, raw) like `_img/example_figs_pilot.py`.
4. Render every SVG to PNG with cairosvg (800 px wide) and LOOK at each one with the Read tool. Fix overlaps, text running outside boxes, labels on lines, wrong wiring or wrong numbers. Only then commit.
5. Commit, push, dispatch `img-apply.yml`, wait, pull, check `_img/log.csv`. If WordPress answers 403 (Cloudflare), wait 60 s and dispatch once more.

## What to draw (per article)
- a) Diagram: construction, cross section, circuit, wiring, loop or block diagram of the article's subject.
- b) Flowchart: working sequence, procedure, calculation steps or troubleshooting decision flow from the article.
- c) Infographic: formula card with the article's own worked example, comparison or selection chart, key numbers, or a labelled graph.
- Every number, label and claim must come from the article text or be standard textbook fact. If the article has a worked example, reuse its numbers exactly. If the article contradicts itself, use the step by step values and fix the article text as `_anim/fixes/RULES.md` explains.
- Different layouts and colours per article (pick an accent colour per post). White background, viewBox 800 wide, height 380 to 600, text 17 px or more (titles 24), heading at top.
- No dash characters in any SVG text or caption (write "minus", "to"). No external images or fonts.

## name, alt, caption, after_h2
- name: lowercase words with single hyphens, max 70 chars, starts with the focus keyword in slug form, ends with the figure type (diagram, flowchart, infographic, chart). Unique across the site.
- alt: 6 to 16 words describing what the image shows the way people search; one of the 3 alts contains the focus keyword. No quotes.
- caption: one sentence of 12 to 35 words starting "Diagram by Instrumentation Blog".
- after_h2: the exact H2 text from the page JSON where the figure belongs (never FAQ, video, references, "What we learn today" or related posts). The 3 figures go under 3 different H2s.
- Skip pages that are not technical articles (news, lists of courses or software, MCQ only): set queue status "skip".
