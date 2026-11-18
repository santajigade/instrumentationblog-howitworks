import json, os, re, sys, base64, urllib.request, urllib.parse, html
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(path):
    req = urllib.request.Request(B + path, headers={'Authorization': AUTH, 'User-Agent': 'ib-p2/1.0'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
def text(h):
    h = re.sub(r'<(style|script)[\s\S]*?</\1>', ' ', h)
    h = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|tr|div)>', '\n', h)
    return re.sub(r'\n\s*\n+', '\n', re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))).strip()
END = re.compile(r'(faq|frequently|conclusion|summary|final thoughts|key takeaways)', re.I)
os.makedirs('_p2/pages', exist_ok=True)
n = int(sys.argv[1]); queue = json.load(open('_p2/queue.json')); done = 0
for item in queue:
    if done >= n: break
    if item['status'] != 'todo' or os.path.exists(f"_p2/pages/{item['slug']}.json"): continue
    try:
        posts = get('/wp/v2/posts?slug=' + urllib.parse.quote(item['slug']) + '&_fields=id,title')
        if not posts: item['status'] = 'notpost'; continue
        pid = posts[0]['id']; w = get(f'/ib/v1/widgets/{pid}'); seo = get(f'/ib/v1/seo/{pid}')
    except Exception as e:
        item['status'] = 'error'; item['err'] = str(e)[:120]; continue
    widgets = w.get('widgets', []); allc = ' '.join(str(x['content']) for x in widgets)
    h2s = [text(m) for m in re.findall(r'<h2[^>]*>([\s\S]*?)</h2>', allc)]
    plan = None
    for x in widgets:
        c = str(x['content'])
        for m in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>', c):
            if END.search(text(m.group(1))):
                tag = m.group(0); find = tag if c.count(tag) == 1 and allc.count(tag) == 1 else None
                if find: plan = {'mode': 'before', 'find': find}
                break
        if plan: break
        if x['type'] in ('heading',) and END.search(text(c)):
            plan = {'new_section': int(x['path'].split('.')[0])}; break
    if not plan:
        last = max([int(x['path'].split('.')[0]) for x in widgets if x['type'] in ('text-editor', 'html') and len(str(x['content'])) > 1500] or [0])
        plan = {'new_section': last + 1}
    json.dump({'id': pid, 'slug': item['slug'], 'title': html.unescape(posts[0]['title']['rendered']), 'focus': seo.get('rank_math_focus_keyword'),
               'keywords': item['keywords'], 'h2s': h2s, 'plan': plan, 'text': text(allc)[:14000]}, open(f"_p2/pages/{item['slug']}.json", 'w'), indent=1)
    done += 1
json.dump(queue, open('_p2/queue.json', 'w'), indent=1)
print('fetched', done)
