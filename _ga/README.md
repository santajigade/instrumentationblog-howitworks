# GA4 snippet for all static pages (from 24 Nov 2026)

Every static page on instrumentationblog.in (calculators, tools, downloads, glossary, compare,
unit-converters, how-it-works and any new section) must use this GA4 code, not the plain gtag snippet.

GA4 has a data filter "Only verified IB visits" (Include only, traffic_type = ib_verified).
Fake hits sent straight to Google (Singapore ghost traffic) do not carry the marker, so a page
still on the old plain snippet loses its real visits from reports once the filter is Active.

```html
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}(function(){var z="";try{z=Intl.DateTimeFormat().resolvedOptions().timeZone||""}catch(e){}if(z==="Asia/Singapore"||navigator.webdriver)return;gtag("js",new Date());gtag("config","G-R3NLR1WRYC",{traffic_type:"ib_verified"});var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id=G-R3NLR1WRYC";document.head.appendChild(s)})();</script>
```

WordPress pages: WPCode > Header & Footer uses the same logic with
`gtag('config', 'G-R3NLR1WRYC', {traffic_type: 'ib_verified'});`

- `ga_rewrite.py` converts the old snippet to this one (python3 _ga/ga_rewrite.py <folder>).
- `.github/workflows/ga-tag.yml` downloads static sections over FTP, backs them up, rewrites, uploads (dry=yes first).
- `.github/workflows/static-inventory.yml` lists public_html folders and html counts (read only).

## Microsoft Clarity (from 26 Nov 2026)

Static pages also carry Clarity (project u4fdvm7fxj) right after the GA4 snippet, with the same Singapore/bot skip.
`clarity_add.py` inserts it; `.github/workflows/clarity-add.yml` applies it to the live static sections.

## GA4 and Clarity gate (26 Nov 2026)
Bots from cloud servers load the page through one address but their asset and GA4 requests come from blocked
Singapore servers, so GA4 still counted them. GA4 and Clarity now wait for the first-party file `/assets/ib-ok.js`
(source: `site/assets/ib-ok.js`). Cloudflare blocks that request for those bots, so they never fire analytics.
Static pages: `_ga/gate_add.py` (workflow "Static sections GA4 gate"). Templates in `_src` already use the gated snippet,
and `_src/check.py` fails a page without it. WordPress: same pattern in WPCode Header & Footer.
