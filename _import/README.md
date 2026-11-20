# Article import (drafts)
Per batch: put `<slug>.json` ({payload, html}) plus `<slug>.webp` (featured poster) in `_upload/ibtmp-<hex>/`.
From 21 Nov 2026 the zips also contain 3 article figures per post (`<name>.webp`, referenced as `{{IMG:<name>.webp}}` in the HTML):
copy every `*.webp` from the zip into the same folder. `import.py` uploads them, sets alt/title/caption from the img alt, and swaps the placeholders.
Then dispatch `article-import.yml`; publish later with `article-publish.yml` (ids).
