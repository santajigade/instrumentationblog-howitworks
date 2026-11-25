# Contextual backlinks from instrumentationblog.in articles to zentacalculator.com (plan: Zenta_Backlink_Plan.xlsx).
# Each run handles N queue rows: finds the most relevant body paragraph and appends one helpful sentence with a normal followed link.
import json, os, sys, re, base64, random, hashlib, html as H, urllib.request, urllib.error, csv, datetime
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def call(path, data=None):
    h = {'Authorization': AUTH, 'User-Agent': 'ib-bl/1.0', 'Content-Type': 'application/json'}
    rq = urllib.request.Request(B + path, data=json.dumps(data).encode() if data is not None else None, method='POST' if data is not None else 'GET', headers=h)
    with urllib.request.urlopen(rq, timeout=120) as r: return json.loads(r.read())
N = int(sys.argv[1]) if len(sys.argv) > 1 else 15
DRY = len(sys.argv) > 2 and sys.argv[2] == 'dry'
EXACT = ["To check your own numbers quickly, try the free {a}.",
         "If you want to skip the manual math, use this {a}.",
         "You can verify the result in seconds with the {a}.",
         "For a fast answer with your own values, the {a} does the math for you.",
         "Before you finalise the figures, run them through the {a}."]
GENERIC = ["You can <a>work it out here</a> with your own values.",
           "To save time, <a>try this calculator</a> with your plant data.",
           "Plug your own figures into <a>this free calculator</a> to check the result.",
           "If you prefer not to do it by hand, <a>use this online calculator</a>."]
STOP = set('the a an of and or to for in on with by calculator calc online free tool'.split())
def words(t): return set(w for w in re.findall(r'[a-z0-9]+', t.lower()) if w not in STOP and len(w) > 1)
def link(url, text): return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
def sentence(it):
    r = random.Random(hashlib.md5((it['article'] + it['target']).encode()).hexdigest())
    if r.random() < 0.65:
        a = it['anchor']; a = a[0].lower() + a[1:] if not a[:2].isupper() else a
        return r.choice(EXACT).format(a=link(it['target'], a))
    s = r.choice(GENERIC); t = re.search(r'<a>(.*?)</a>', s).group(1)
    return s.replace(f'<a>{t}</a>', link(it['target'], t))
def paragraphs(html):
    out = []
    for m in re.finditer(r'<p(?:\s[^>]*)?>(.*?)</p>', html, flags=re.S):
        tag = m.group(0)
        if re.match(r'<p\s[^>]*class=', tag): continue          # styled boxes (excerpt, quote...)
        inner = m.group(1); txt = H.unescape(re.sub(r'<[^>]+>', ' ', inner))
        if len(txt) < 140 or 'zentacalculator.com' in inner or 'Hello everyone' in txt: continue
        out.append((m.start(), tag, txt))
    return out
Q = '_bl/queue.json'; q = json.load(open(Q)); used = {}
lw = csv.writer(open('_bl/log.csv', 'a', newline=''))
for it in [x for x in q if x['status'] == 'todo'][:N]:
    slug = it['article'].rstrip('/').rsplit('/', 1)[-1]
    try:
        posts = call(f'/wp/v2/posts?slug={slug}&_fields=id')
        if not posts: raise Exception('post not found')
        pid = posts[0]['id']
        try:
            w = call(f'/ib/v1/widgets/{pid}')['widgets']; mode = 'el'; html = ''.join(str(x['content']) for x in w)
        except urllib.error.HTTPError as e:
            if e.code != 404: raise
            html = call(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']; mode = 'classic'
        if it['target'] in html: it['status'] = 'exists'; note = 'already linked'; raise StopIteration
        ps = paragraphs(html)
        ps = [p for p in ps if p[1] not in used.get(pid, set())]
        if not ps: raise Exception('no suitable paragraph')
        kw = words(it['anchor'] + ' ' + it['target'].rstrip('/').rsplit('/', 1)[-1].replace('-', ' '))
        n = len(ps)
        best = max(range(n), key=lambda i: (len(kw & words(ps[i][2])), -abs(i - n * 0.45)))
        tag = ps[best][1]
        if html.count(tag) != 1: raise Exception('paragraph not unique')
        new = tag[:-4].rstrip() + ' ' + sentence(it) + '</p>'
        note = f'{mode} p{best+1}/{n} overlap={len(kw & words(ps[best][2]))} :: {re.sub("<[^>]+>","",new)[-170:]}'
        if not DRY:
            if mode == 'el':
                r = call('/ib/v1/patch', {'id': pid, 'ops': [{'find': tag, 'mode': 'replace', 'html': new}]})
                bad = [x for x in r['report'] if not x.get('applied', True)]
                if bad: raise Exception('not applied %s' % bad)
            else:
                call(f'/wp/v2/posts/{pid}', {'content': html.replace(tag, new, 1)})
            it['status'] = 'done'; it['date'] = datetime.date.today().isoformat()
        used.setdefault(pid, set()).add(tag)
    except StopIteration:
        pass
    except Exception as e:
        if not DRY: it['status'] = 'failed'
        note = 'ERR ' + str(e)[:150]
    if not DRY: lw.writerow([datetime.date.today().isoformat(), it['row'], it['article'], it['target'], it['status'], note])
    print(it['row'], slug, '->', it['target'].split('.com')[1], '|', note)
if not DRY: json.dump(q, open(Q, 'w'), indent=0)
print('left', sum(x['status'] == 'todo' for x in q))
