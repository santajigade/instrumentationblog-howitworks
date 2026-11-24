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
