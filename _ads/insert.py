# Add manual ad slots to published posts that have none (status "noads" in _ads/queue.json).
# Ads go before top-level H2 headings: IB_Top after the intro, IB_Mid1/IB_Mid2 in the middle, IB_End near the end,
# plus a Multiplex unit before the closing quote when the article has one. Never two ads next to each other.
import json, os, sys, re, base64, urllib.request, urllib.error, csv, datetime, time, html as H
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-ads/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None, method='POST' if data is not None else 'GET', headers=h)
    for k in range(4):
        try:
            with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 403 and k < 3: time.sleep(60); continue
            raise
C = 'ca-pub-3931314195561246'
TOP, MID1, MID2, END, MULTI = '7215194230', '6552849252', '7839764783', '5046401284', '3541747929'
def block(slot, multi=False):
    fmt = 'data-ad-format="autorelaxed"' if multi else 'data-ad-format="auto" data-full-width-responsive="true"'
    return ('<div class="whc-ad" style="margin:28px 0;text-align:center"><div style="font-size:11px;letter-spacing:.12em;color:#9ca3af;text-transform:uppercase;margin-bottom:6px">Advertisement</div>'
            f'<ins class="adsbygoogle" style="display:block" data-ad-client="{C}" data-ad-slot="{slot}" {fmt}></ins>'
            '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>\n')
def pplan(html):
    """fallback when headings are unusable: insert after plain body paragraphs at about 25%, 55% and 85%"""
    ps = [m.group(0) for m in re.finditer(r'<p>(?:(?!</p>).){80,}?</p>', html, flags=re.S)]
    ps = [x for x in ps if html.count(x) == 1]
    if len(ps) < 4: return []
    words = len(re.sub(r'<[^>]+>', ' ', html).split())
    fr = [0.25, 0.55, 0.85] if words >= 700 else [0.3, 0.75]
    slots = [TOP, MID1, END] if len(fr) == 3 else [TOP, END]
    out, used = [], set()
    for f, sl in zip(fr, slots):
        i = min(len(ps) - 1, max(1, round(f * (len(ps) - 1))))
        if i in used or i - 1 in used or i + 1 in used: continue
        used.add(i); out.append(('AFTER', ps[i], sl))
    return out
def plan(html):
    """return list of (h2_tag, slot) to insert before"""
    hs = []
    for m in re.finditer(r'<h2\b[^>]*>.*?</h2>', html, flags=re.S):
        pre = html[:m.start()]
        depth = len(re.findall(r'<div\b', pre)) - len(re.findall(r'</div>', pre))
        txt = H.unescape(re.sub(r'<[^>]+>', '', m.group(0))).strip()
        hs.append((m.group(0), depth, txt))
    if len(hs) < 2: return pplan(html)
    d0 = min(h[1] for h in hs)
    hs = [h for h in hs if h[1] == d0 and html.count(h[0]) == 1]
    words = len(re.sub(r'<[^>]+>', ' ', html).split())
    n = len(hs)
    if n < 2: return pplan(html)
    want = 4 if (words >= 900 and n >= 6) else 3 if (words >= 600 and n >= 4) else 2
    # end slot: before FAQ / Related / References / Conclusion heading if present, else last h2
    endi = next((i for i, h in enumerate(hs) if i > 1 and re.search(r'faq|frequently|related|reference|conclusion|summary|what we learn', h[2], re.I)), n - 1)
    picks = [1]
    mids = [MID1, MID2][:max(0, want - 2)]
    for k, s in enumerate(mids):
        t = round(1 + (endi - 1) * (k + 1) / (len(mids) + 1))
        picks.append(t)
    picks.append(endi)
    out, used = [], set()
    slots = [TOP] + mids + [END]
    for i, s in zip(picks, slots):
        if i in used or (i - 1) in used or (i + 1) in used or i <= 0 or i >= n + 0: continue
        used.add(i); out.append((hs[i][0], s))
    return out
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10
DRY = len(sys.argv) > 2 and sys.argv[2] == 'dry'
ONLY = sys.argv[3].split(',') if len(sys.argv) > 3 and sys.argv[3] else None
Q = '_ads/queue.json'; q = json.load(open(Q))
SWAP = len(sys.argv) > 4 and sys.argv[4] == 'swap'
todo = [x for x in q if (x['status'] in ('hasads', 'swapfail') if SWAP else x['status'] in ('noads', 'noplace', 'insfail')) and (not ONLY or str(x['id']) in ONLY)][:N]
OLD2 = 'data-ad-slot="5109630877"'
def order(n):
    if n <= 0: return []
    if n == 1: return [TOP]
    return [TOP] + [MID1 if i % 2 == 0 else MID2 for i in range(n - 2)] + [END]
lw = csv.writer(open('_ads/insert_log.csv', 'a', newline=''))
for it in todo:
    pid = it['id']
    try:
        try:
            w = call(f'/ib/v1/widgets/{pid}')['widgets']; mode = 'el'; html = ''.join(str(x['content']) for x in w)
        except urllib.error.HTTPError as e:
            if e.code != 404: raise
            html = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']; mode = 'classic'
        NEW = (TOP, MID1, MID2, END, MULTI, '6904203044')
        if SWAP:
            tags = [m.group(0) for m in re.finditer(r'<ins\b[^>]*class="adsbygoogle"[^>]*>\s*</ins>', html, flags=re.S)]
            tags = [t for t in tags if not any(f'"{n}"' in t for n in NEW)]
            k = len(tags); note = f'{mode} swap x{k} ' + ','.join(sorted(set(re.findall(r'data-ad-slot="(\d+)"', ' '.join(tags)))))
            if k and not DRY:
                new = [f'<ins class="adsbygoogle" style="display:block" data-ad-client="{C}" data-ad-slot="{x}" data-ad-format="auto" data-full-width-responsive="true"></ins>' for x in order(k)]
                if mode == 'el':
                    r = call('/ib/v1/patch', {'id': pid, 'ops': [{'find': t, 'mode': 'replace', 'html': n} for t, n in zip(tags, new)]})
                    bad = [x for x in r['report'] if not x.get('applied', True)]
                    if bad: raise Exception('not applied %s' % bad)
                else:
                    for t, n in zip(tags, new): html = html.replace(t, n, 1)
                    call(f'/wp/v2/posts/{pid}', {'content': html})
            if not DRY: it['status'] = 'swapped' if k else 'hasads-none'
        elif 'adsbygoogle' in html: it['status'] = 'hasads'; note = 'already has ad code'
        elif False:
            k = html.count(OLD2); note = f'{mode} swap old unit x{k}'
            if not DRY:
                if mode == 'el':
                    r = call('/ib/v1/patch', {'id': pid, 'ops': [{'find': OLD2, 'mode': 'replace', 'html': f'data-ad-slot="{x}"'} for x in order(k)]})
                    bad = [x for x in r['report'] if not x.get('applied', True)]
                    if bad: raise Exception('not applied %s' % bad)
                else:
                    it_ = iter(order(k)); call(f'/wp/v2/posts/{pid}', {'content': re.sub(re.escape(OLD2), lambda m: f'data-ad-slot="{next(it_)}"', html)})
                it['status'] = 'swapped'
        elif 'adsbygoogle' in html: it['status'] = 'hasads-other'; note = 'other ad code'
        else:
            p = plan(html)
            multi = '<div class="dcp-quote">' in html
            p = [x if len(x) == 3 else ('BEFORE',) + tuple(x) for x in p]
            note = f'{mode} ads={len(p)}{"+multi" if multi else ""} :: ' + ' | '.join(f'{w[0][0]}{s[-4:]}<{H.unescape(re.sub("<[^>]+>","",t))[:40]}' for w, t, s in [(x[0], x[1], x[2]) for x in p])
            if not p: it['status'] = 'noplace'
            elif not DRY:
                if mode == 'el':
                    ops = [{'find': t, 'mode': 'before' if w == 'BEFORE' else 'after', 'html': block(s)} for w, t, s in p]
                    if multi: ops.append({'find': '<div class="dcp-quote">', 'mode': 'before', 'html': block(MULTI, True)})
                    r = call('/ib/v1/patch', {'id': pid, 'ops': ops})
                    bad = [x for x in r['report'] if not x.get('applied', True)]
                    if bad: raise Exception('not applied %s' % bad)
                else:
                    for w, t, s in p: html = html.replace(t, (block(s) + t) if w == 'BEFORE' else (t + block(s)), 1)
                    if multi: html = html.replace('<div class="dcp-quote">', block(MULTI, True) + '<div class="dcp-quote">', 1)
                    call(f'/wp/v2/posts/{pid}', {'content': html})
                it['status'] = 'inserted'
    except Exception as e:
        note = 'ERR ' + str(e)[:150]
        if not DRY: it['status'] = 'swapfail' if SWAP else 'insfail'
    if not DRY: lw.writerow([datetime.date.today().isoformat(), it['slug'], pid, it['status'], note])
    print(pid, it['slug'][:45], '|', note[:260])
if not DRY: json.dump(q, open(Q, 'w'), indent=0)
print('left', sum(x['status'] == 'noads' for x in q))
