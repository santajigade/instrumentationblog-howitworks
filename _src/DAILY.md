# Daily batch: 4 new How It Works pages

Followed by the scheduled job every morning. Pages are built on branch `daily`; the GitHub workflow
`publish.yml` merges them into `main` and uploads them at 08:00 IST.

## Steps

1. Start from the latest `main`: `git fetch origin main && git checkout -B daily origin/main`.
2. Take the first 4 lines marked `- [ ]` in `_src/TOPICS.md`. Mix of groups is already arranged; keep the order.
3. For each topic create `_src/pages/<slug>.py` (file name = slug) defining `PAGE` and `SCENE` (see below).
4. Build and verify:
   ```
   python3 _src/build.py
   node _src/snap.js && python3 _src/webp.py
   python3 _src/check.py          # must print OK
   ```
   Fix every FAIL line and rerun until OK. Open the 4 new PNG/WebP diagrams and look at them: labels must not overlap, nothing cut off, markers placed on the right parts.
5. Tick the 4 topics in `_src/TOPICS.md` (`- [x]`).
6. Commit everything (pages, images, site html, sitemap, TOPICS.md) and `git push -f origin daily`. Never push the batch to `main` directly.

## PAGE fields (same as content.py, plus intro/uses/tips)

```python
PAGE = dict(
  slug="plc-scan-cycle", grp="PLC", name="PLC Scan Cycle", kw="How a PLC Scan Cycle Works",
  title="...",            # ≤ 65 chars, contains kw exactly, ends with a real hook (Animated Diagram, Formula, Example)
  desc="...",             # 120 to 160 chars, contains kw exactly, says what the animation shows
  h1="How a PLC Scan Cycle Works", hero="2 sentences telling the reader what to do with the sliders.",
  quick="2 sentence direct answer.",
  intro=[3 paragraphs, max 2 sentences each],
  sliders=[(key, label, min, max, default, step, decimals, unit), ...],   # 1 to 3 sliders
  outs=[(key, label), ...],         # 3 or 4 readouts; upd() fills them with o(key, text)
  legend=[...],                     # names of numbered markers 1..n drawn on the canvas
  steps=[5 steps], formula=[4 or 5 lines; first line is the main formula],
  parts=[(part, what it does) x4 or 5], uses=[(title, one line) x4], pros=[3], cons=[3],
  tips=[4 field tips], faq=[(q, a) x4],
  cal=[("<section>/<calc-slug>", "Name")],   # paths from _src/valid_links.txt starting calculators/
  glo=[("<glossary-slug>", "Name")], cmp=[("<compare-slug>", "Name")],   # may be empty lists
  tool=[("tools/<path>", "Name")],          # optional
  blog=("<slug from the TOPICS line>", "Article title in sentence case"))
```
Every calculators/, glossary/, compare/, tools/ and downloads/ link must exist in `_src/valid_links.txt`
(grep it). Blog slugs must exist in `_src/blog_slugs.txt`. The checker rejects anything else.

## SCENE (canvas JS)

Logical canvas 640 × 360. Define `function upd()`, `function step(dt)`, `function draw()`.
Read slider values from `P.<key>`. Helpers: `L(text,x,y,size,color,align,bold)`, `ln`, `rc`, `ci`, `ar` (arrow),
`mk(n,x,y)` numbered marker, `pipe(x1,x2,cy,R)`, `wave(x1,x2,y,yBottom,color)` liquid surface,
`stream(x,y1,y2)` falling liquid, `sm`, `clamp`, `m(x,dec)` number with real minus sign, `o(key,text)`, `T` time in s.
Copy patterns from `_src/scenes.py` (12 working examples).

Rules: something must move every frame (particles, waves, signals, scan pointer, blinking contacts);
every legend item has a marker `mk(n,...)`; put a short grey note in the top left (y=22) if an effect is exaggerated;
keep text ≥ 11 px and inside 640 × 360; readouts must match a hand calculation; physics and standards
must be correct (cite only well known relations, no invented statistics).

## Writing rules

- No hyphens or dashes anywhere in visible text, alt or title text (write "non contact", "4 to 20 mA", "on off").
  Use the real minus sign U+2212 for negative numbers. Slugs and code may contain hyphens.
- Max 2 sentences per paragraph. Plain, practical engineer to engineer tone for students and engineers in India.
- Vendor neutral. No brand names except standards bodies (ISA, IEC, IEEE, API, ASME, NAMUR).
- Every page carries AdSense and GA4 automatically through the template; do not edit the template files.
