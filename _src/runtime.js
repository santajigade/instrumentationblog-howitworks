// Loads every page, checks there are no JS errors, readouts are filled and the canvas animates.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const SITE = path.resolve(__dirname, '..', 'site', 'how-it-works');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.route(/^https?:\/\//, r => r.abort());
  let bad = 0, cur = '';
  p.on('pageerror', e => { bad++; console.log('JS error', cur, e.message); });
  for (const s of fs.readdirSync(SITE)) {
    const f = path.join(SITE, s, 'index.html');
    if (!fs.existsSync(f)) continue;
    cur = s;
    await p.goto('file://' + f);
    await p.evaluate(() => document.getElementById('hw-cv').scrollIntoView({ block: 'center' }));
    await p.waitForTimeout(700);
    const a = await p.evaluate(() => document.getElementById('hw-cv').toDataURL());
    await p.waitForTimeout(450);
    const c = await p.evaluate(() => document.getElementById('hw-cv').toDataURL());
    if (a === c) { bad++; console.log('STATIC canvas', s); }
    const empty = await p.evaluate(() => [...document.querySelectorAll('.ibuc-o b')].filter(x => !x.textContent.trim() || x.textContent.trim() === '…' || /NaN|undefined|Infinity/.test(x.textContent)).length);
    if (empty) { bad++; console.log('readouts not filled', s, empty); }
    const blank = await p.evaluate(() => { const cv = document.getElementById('hw-cv'), x = cv.getContext('2d').getImageData(0, 0, cv.width, cv.height).data; let n = 0; for (let i = 3; i < x.length; i += 40) if (x[i] > 0) n++; return n; });
    if (blank < 50) { bad++; console.log('canvas nearly empty', s); }
  }
  await b.close();
  process.exit(bad ? 1 : 0);
})();
