# New article animations (instrumentationblog.in)

Daily: draw 5 NEW animations for articles in `_anim/queue.json` (status `todo`, in order) and embed them. The user approved publishing directly.

## Setup (fresh session)
`pip install --break-system-packages pillow` if missing. Playwright: `node -e "require('playwright')"`; if it fails, `npm i -g playwright && npx playwright install chromium` (or `npm i playwright` in /tmp/anim). Fonts are the system defaults.

## For each article (take the next `todo` items until 5 are done)
1. Read the article first: dispatch nothing, just open `https://www.instrumentationblog.in/<slug>/` with WebFetch, or use `_p2/pages/<slug>.json` if it exists (it has the article text).
   If the topic is not a physical, electrical or logical process that motion makes clearer (course lists, software lists, MCQs, documents, certificates, formula lists), set status `skip` and move on.
2. Write `_anim/scenes/<slug>.js`: a canvas scene in the same style as `_anim/scenes/reed-switch.js`, `pwm.js`, `half-adder.js` and the scenes in `_src/scenes.py`.
   - Logical canvas 640 × 360. Define `upd()`, `step(dt)`, `draw()`. Helpers: `L, ln, rc, ci, ar, mk, sm, clamp, m, pipe, wave, stream, T`. Do not use `P` (no sliders).
   - The loop must repeat every 4.8 s exactly (60 frames × 80 ms): drive motion from a phase `ph=(ph+dt)%4.8` so the first and last frames match. Scrolling or rotating parts must also complete whole cycles in 4.8 s.
   - Something moves every frame. Show the real working principle correctly (textbook physics or logic only). Short grey note at top left (y=22, 11 px) if anything is simplified or slowed down.
   - 4 to 6 numbered markers `mk(n,x,y)` on the right parts, never covering text or other markers. Text ≥ 11 px, nothing outside 640 × 360. No hyphens or dashes in visible text; use "−" for negative numbers.
3. Build and record:
   ```
   python3 _anim/tools/build.py <slug> "How <Topic> Works"
   node _anim/tools/rec.js <slug> 60 80
   python3 _anim/tools/mk.py <slug> _anim/<slug>-animation.webp 800 65
   ```
   Keep the WebP under 600 KB (lower quality to 55, or width 720, if needed).
4. LOOK at frames 0, 20 and 40 (`/tmp/anim/frames/<slug>/f000.png` etc.) with the Read tool. Fix overlaps, cut text, markers on wrong parts, and record again until clean.
5. Write `_anim/todo/<slug>.json`: `{"blog": "<slug>", "file": "<slug>-animation.webp", "alt": "x", "html": "<figure ...>"}`.
   Copy the figure HTML pattern from a file in `_anim/done/` made for reed switch, PWM or half adder (img with `{{IMG}}`, `draggable="false" oncontextmenu="return false"`, figcaption with "<strong>Name animation.</strong> Numbered parts:" and an `<ol>` listing the markers 1 to n in order). alt and title are replaced automatically by the focus keyword.
6. After all 5: commit (scenes, webp, todo json, queue.json), push, dispatch `anim-apply.yml` with `inputs[script]=apply`, wait, pull, check the last rows of `_anim/log.csv`. Mark queue items `done`.
   If a post has no Elementor data (error 404), dispatch again with `inputs[script]=classic`.
   If WordPress answers 403 (Cloudflare), wait 60 s and dispatch once more.
7. Check placement with WebFetch on each article: the figure must sit under a section that explains the working or the concept, never under FAQ, video, references or downloads. If it is wrong, edit `MOVES` in `_anim/move.py` (`{"<slug>": ("<exact H2 text>", "after" or "before")}`) and dispatch with `inputs[script]=move`.
