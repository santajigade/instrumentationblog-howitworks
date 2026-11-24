# Fixing self-contradicting articles (approved by Santaji on 24 Nov 2026)

When any daily step finds an article that contradicts itself, fix it on the live site instead of only reporting it.

1. Decide the correct value from the article's own worked example (step by step values win), a standard (ISO, IEC, IEEE, EN) or a textbook fact. If you cannot settle it with confidence, do not edit; report it.
2. Change the smallest wrong sentence so the article agrees with itself. Keep the article's style, never add links or dash characters, and leave correct sentences alone.
3. Write `_anim/fixes/changes/<slug>.json`: `{"slug": "...", "reason": "one line", "pairs": [["exact old text", "new text"], ...]}`.
   The old text must be the exact HTML string in the live Elementor widget (one line, no \r\n). If unsure, probe it first (see `_anim/fixprobe.py`).
4. Commit, push, dispatch `anim-apply.yml` with `inputs[script]=fixapply` (same concurrency group, so never at the same time as another workflow), wait, pull, check `_anim/fixes/log.csv`.
5. List each fix in the daily summary: slug, what changed and why.
