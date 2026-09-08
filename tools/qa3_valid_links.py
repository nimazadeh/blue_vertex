# -*- coding: utf-8 -*-
"""Master QA — phase 3: HTML validity + internal links/fragments."""
import os, re
import html5lib

ROOT = '/home/user/blue-vertex'
PAGES = sorted([os.path.join(r, f) for r, _, fs in os.walk(ROOT) for f in fs if f.endswith('.html')])

bad_html = []
bad_links = []
for f in PAGES:
    src = open(f, encoding='utf-8').read()
    p = html5lib.HTMLParser(strict=False)
    p.parse(src)
    errs = [str(e) for e in p.errors if any(k in str(e) for k in
            ('duplicate', 'Unexpected', 'Stray end', 'Unclosed', 'Expected'))]
    if errs:
        bad_html.append((os.path.relpath(f, ROOT), errs[:3]))
    # ids for fragment check
    ids = set(re.findall(r'id="([^"]+)"', src))
    for m in re.findall(r'(?:href)="([^"#]+)?#([^"]+)"', src):
        target, frag = m
        if target and not target.endswith('.html'):
            continue
        base = os.path.normpath(os.path.join(os.path.dirname(f), target or os.path.basename(f)))
        if not os.path.exists(base) and not target:
            continue
        # read target file ids (may not exist → skip)
        try:
            tsrc = open(base, encoding='utf-8').read()
        except Exception:
            continue
        tids = set(re.findall(r'id="([^"]+)"', tsrc))
        if frag not in tids:
            bad_links.append((os.path.relpath(f, ROOT), '#' + frag, base.replace(ROOT, '')))
    # plain internal hrefs without fragment
    for h in re.findall(r'href="([^"]+)"', src):
        if h.startswith(('http', 'mailto:', 'tel:', '#', 'javascript')) or not h:
            continue
        path = h.split('#')[0].split('?')[0]
        full = os.path.normpath(os.path.join(os.path.dirname(f), path))
        if not os.path.exists(full):
            bad_links.append((os.path.relpath(f, ROOT), h, 'MISSING FILE'))

print('== HTML validity ==')
for x in bad_html: print(' ', x[0], x[1])
print(' issues:', len(bad_html))
print('== links/fragments ==')
for x in bad_links: print(' ', x)
print(' issues:', len(bad_links))
