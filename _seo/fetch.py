import json, os, re, sys, base64, urllib.request, urllib.parse, html
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(path):
    req = urllib.request.Request(B + path, headers={'Authorization': AUTH, 'User-Agent': 'ib-seo/1.0'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
def text(h):
    h = re.sub(r'<(style|script)[\s\S]*?</\1>', ' ', h)
    h = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|tr|div)>', '\n', h)
    return re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()
os.makedirs('_seo/pages', exist_ok=True)
n = int(sys.argv[1]); queue = json.load(open('_seo/ctr_queue.json')); done = 0
for item in queue:
    if done >= n: break
    if item['status'] != 'todo' or os.path.exists(f"_seo/pages/{item['slug']}.json"): continue
    try:
        posts = get('/wp/v2/posts?slug=' + urllib.parse.quote(item['slug']) + '&_fields=id')
        if not posts: item['status'] = 'notpost'; continue
        pid = posts[0]['id']; seo = get(f'/ib/v1/seo/{pid}'); w = get(f'/ib/v1/widgets/{pid}')
    except Exception as e:
        item['status'] = 'error'; item['err'] = str(e)[:120]; continue
    body = text(' '.join(str(x['content']) for x in w.get('widgets', [])))
    heads = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', ' '.join(str(x['content']) for x in w.get('widgets', [])), re.S)
    json.dump(dict(id=pid, slug=item['slug'], impr=item['impr'], ctr=item['ctr'], pos=item['pos'], queries=item['queries'],
                   title=seo['title'], rank_math_title=seo['rank_math_title'], rank_math_description=seo['rank_math_description'],
                   focus_keyword=seo['rank_math_focus_keyword'], headings=[re.sub('<[^>]+>', '', h).strip()[:90] for h in heads][:25],
                   text=body[:3000]), open(f"_seo/pages/{item['slug']}.json", 'w'), indent=1)
    done += 1
json.dump(queue, open('_seo/ctr_queue.json', 'w'), indent=0)
print('fetched', done)
