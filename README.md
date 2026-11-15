# instrumentationblog.in: How It Works

Static section published at https://www.instrumentationblog.in/how-it-works/

```
site/how-it-works/     live pages (hub, 12 animated pages, sitemap.xml)
_src/                  generator: content.py (text), scenes.py (canvas animations), build.py
.github/workflows/     auto upload of site/ to public_html on every push to main
```

## Rebuild

```
python3 _src/build.py      # regenerates site/how-it-works/ from _src/
node _src/snap.js          # renders each animation to <slug>-working-diagram.png (needs Playwright)
python3 _src/webp.py       # converts them to <slug>-working-diagram.webp (1560 x 878)
```

Each page carries its diagram image (topic named, for Google Images), og:image / twitter:image for social shares, and a Download diagram button that saves `<slug>-working-diagram.png`.

Edit page text in `_src/content.py` and animations in `_src/scenes.py`, rebuild, commit, push.
The workflow uploads only the files that changed.

## One time setup (GitHub → Settings → Secrets and variables → Actions)

| Secret | Value |
|---|---|
| `FTP_SERVER` | FTP host from cPanel (for example `ftp.instrumentationblog.in`) |
| `FTP_USERNAME` | FTP account user |
| `FTP_PASSWORD` | FTP account password |
| `FTP_SERVER_DIR` | Folder that is public_html, seen from that FTP account, ending in `/` |

`FTP_SERVER_DIR`: if the FTP account opens directly in public_html use `./`; if it opens in the home folder use `public_html/`.

## Site rules

AdSense ca-pub-3931314195561246 (slot 5950781970) and GA4 G-R3NLR1WRYC on every page; title ≤ 65 and description ≤ 160 characters with the keyword in both; no hyphens in visible text, U+2212 for minus; verified data and live blog slugs only; no .htaccess or PHP files.
