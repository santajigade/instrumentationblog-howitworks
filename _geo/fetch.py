import json, os, re, sys, base64, urllib.request, urllib.parse, html
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(path):
    req = urllib.request.Request(B + path, headers={'Authorization': AUTH, 'User-Agent': 'ib-geo/1.0'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
def text(h):
    h = re.sub(r'<(style|script)[\s\S]*?</\1>', ' ', h)
    h = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|tr|div)>', '\n', h)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
n = int(sys.argv[1]); queue = json.load(open('_geo/queue.json')); done = 0
for item in queue:
    if done >= n: break
    if item['status'] != 'todo' or os.path.exists(f"_geo/pages/{item['slug']}.json"): continue
    try:
        posts = get('/wp/v2/posts?slug=' + urllib.parse.quote(item['slug']) + '&_fields=id,title,link')
        if not posts: item['status'] = 'notpost'; continue
        pid = posts[0]['id']; w = get(f'/ib/v1/widgets/{pid}')
    except Exception as e:
        item['status'] = 'error'; item['err'] = str(e)[:120]; continue
    widgets = w.get('widgets', []); allc = ' '.join(str(x['content']) for x in widgets)
    if 'Quick Answer' in allc: item['status'] = 'has'; continue
    plan = None
    htmlw = [x for x in widgets if x['type'] == 'html' and len(str(x['content'])) > 3000]
    if w.get('sections', 0) <= 3 and htmlw:
        c = htmlw[0]['content']; hi = re.search(r'Hello everyone', c, re.I)
        start = hi.end() if hi else 0
        m = re.compile(r'<h2[^>]*>').search(c, start)
        if m: plan = {'mode': 'before', 'find': m.group(0) if c.count(m.group(0)) == 1 else c[m.start():m.start() + 80]}
    if not plan:
        idx = 1
        for x in widgets:
            sec = int(x['path'].split('.')[0])
            if x['type'] == 'text-editor': idx = sec + 1; break
        plan = {'new_section': idx}
    body = text(allc)
    json.dump({'id': pid, 'slug': item['slug'], 'title': html.unescape(posts[0]['title']['rendered']), 'queries': item.get('queries', []),
               'plan': plan, 'text': body[:6000]}, open(f"_geo/pages/{item['slug']}.json", 'w'), indent=1)
    done += 1
json.dump(queue, open('_geo/queue.json', 'w'), indent=0)
print('fetched', done)
