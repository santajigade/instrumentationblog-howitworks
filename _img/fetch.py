# python3 _img/fetch.py N : fetch the next N todo posts (text, H2 list, existing images) into _img/pages/<slug>.json
import json, os, re, sys, base64, urllib.request, urllib.parse, html
B = 'https://www.instrumentationblog.in/wp-json'
AUTH = 'Basic ' + base64.b64encode(f"{os.environ['U']}:{os.environ['P']}".encode()).decode()
def get(path):
    req = urllib.request.Request(B + path, headers={'Authorization': AUTH, 'User-Agent': 'ib-img/1.0'})
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read())
def text(h):
    h = re.sub(r'<(style|script|svg)[\s\S]*?</\1>', ' ', h)
    h = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|tr|div|td|th)>', '\n', h)
    return re.sub(r'\n\s*\n+', '\n', re.sub(r'[ \t]+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h)))).strip()
n = int(sys.argv[1]); queue = json.load(open('_img/queue.json')); done = 0
for item in queue:
    if done >= n: break
    if item['status'] != 'todo' or os.path.exists(f"_img/pages/{item['slug']}.json"): continue
    try:
        posts = get('/wp/v2/posts?slug=' + urllib.parse.quote(item['slug']) + '&_fields=id,title')
        if not posts: item['status'] = 'notpost'; continue
        pid = posts[0]['id']; seo = get(f'/ib/v1/seo/{pid}')
        try: w = get(f'/ib/v1/widgets/{pid}'); widgets = w.get('widgets', []); mode = 'elementor'
        except Exception:
            c = get(f'/wp/v2/posts/{pid}?context=edit&_fields=content')['content']['raw']; widgets = [{'path': '0', 'type': 'classic', 'content': c}]; mode = 'classic'
    except Exception as e:
        item['status'] = 'error'; item['err'] = str(e)[:120]; continue
    allc = ' '.join(str(x['content']) for x in widgets)
    h2s = []
    for x in widgets:
        c = str(x['content'])
        if x['type'] in ('html', 'text-editor', 'classic'):
            for m in re.finditer(r'<h2[^>]*>([\s\S]*?)</h2>', c):
                h2s.append({'text': text(m.group(1)), 'unique': c.count(m.group(0)) == 1 and allc.count(m.group(0)) == 1, 'where': x['type']})
        elif x['type'] == 'heading':
            h2s.append({'text': text(c), 'unique': True, 'where': 'heading', 'section': int(x['path'].split('.')[0])})
    json.dump({'id': pid, 'slug': item['slug'], 'mode': mode, 'title': html.unescape(posts[0]['title']['rendered']),
               'focus': (seo.get('rank_math_focus_keyword') or '').split(',')[0], 'queries': item['queries'], 'h2s': h2s,
               'has_ib_img': 'ib-img' in allc, 'images_now': len(re.findall(r'<img\b', allc)), 'text': text(allc)[:16000]},
              open(f"_img/pages/{item['slug']}.json", 'w'), indent=1)
    done += 1
json.dump(queue, open('_img/queue.json', 'w'), indent=0)
print('fetched', done)
