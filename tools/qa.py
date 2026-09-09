# -*- coding: utf-8 -*-
"""Blue Vertex — release QA gate.
Run: python3 tools/qa.py  (after python3 tools/build.py)
"""
import os, re, sys, io, glob, html.parser

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SITE = 'https://bluevertex.ir/'
PAGES = [p for p in sorted(glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True))
         if 'node_modules' not in p and 'tools/shots' not in p]

FORBIDDEN = ['TODO', 'FIXME', 'Lorem ipsum', 'lorem ipsum', 'coming soon', 'Coming soon', 'PLACEHOLDER', 'به‌زودی']
errors, warnings, ok = [], [], []

def rel(target):
    return os.path.normpath(os.path.join(ROOT, target))

ATTRS = ['href', 'src', 'srcset', 'poster', 'action']
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Checker(html.parser.HTMLParser):
    def __init__(self, page):
        super().__init__(convert_charrefs=True)
        self.page = page
        self.stack = []
        self.hrefs = []
        self.counts = {}
        self.has_main = False
        self.title = ''
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == 'title':
            self.in_title = True
        if tag == 'main':
            self.has_main = True
        for a in ATTRS:
            v = d.get(a)
            if v:
                self.hrefs.append((a, v))
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            # tolerate <p> auto-close quirks & <li> hoisting
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                if self.stack:
                    self.stack.pop()
            else:
                errors.append(f'{self.page}: stray </{tag}>')
    def handle_data(self, data):
        if self.in_title:
            self.title += data
    def handle_startendtag(self, tag, attrs):
        for a in ATTRS:
            v = dict(attrs).get(a)
            if v:
                self.hrefs.append((a, v))

def check_page(path):
    with io.open(path, encoding='utf-8') as f:
        src = f.read()
    page = os.path.relpath(path, ROOT).replace(os.sep, '/')
    pdir = os.path.dirname(path)
    # DOCTYPE — first line must be exactly <!DOCTYPE html>
    first = src.lstrip('\ufeff').splitlines()[0].strip() if src.strip() else ''
    if first != '<!DOCTYPE html>':
        errors.append(f'{page}: bad DOCTYPE → {first!r}')
    # canonical — every indexable page must self-canonical; 404 must have none
    if page == '404.html':
        if 'rel="canonical"' in src:
            errors.append(f'{page}: 404 page must not have a canonical')
        if 'noindex' not in src:
            errors.append(f'{page}: 404 page must be noindex')
    else:
        want = SITE + page
        m = re.search(r'rel="canonical" href="([^"]+)"', src)
        if not m:
            errors.append(f'{page}: missing canonical')
        elif m.group(1) != want:
            errors.append(f'{page}: wrong canonical {m.group(1)} (expected {want})')
    # forbidden tokens
    for tok in FORBIDDEN:
        if tok in src:
            errors.append(f'{page}: contains forbidden token «{tok}»')
    # lang/dir
    if '<html lang="fa" dir="rtl">' not in src:
        errors.append(f'{page}: missing <html lang="fa" dir="rtl">')
    # title + description
    if '<meta name="description"' not in src:
        warnings.append(f'{page}: no meta description')
    # body close
    if '</body>' not in src or '</html>' not in src:
        errors.append(f'{page}: missing </body> or </html>')
    # links
    c = Checker(page)
    try:
        c.feed(src)
    except Exception as e:
        errors.append(f'{page}: parser exception {e}')
        return
    if c.stack:
        leftovers = set(c.stack)
        errors.append(f'{page}: unclosed tags → {sorted(leftovers)[:8]}')
    for attr, v in c.hrefs:
        v = v.strip()
        if not v or v.startswith(('#', 'http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:',
                                 'about:', 'blob:', 'chrome:')):
            continue
        if v.startswith('//'):
            continue
        target = v.split('#')[0].split('?')[0]
        if not target:
            continue
        candidate = os.path.normpath(os.path.join(pdir, target))
        if not os.path.exists(candidate):
            errors.append(f'{page}: broken {attr} → {v}')
    # ensure no empty key headings
    for m in re.finditer(r'<h([12])[^>]*>\s*(?:<[^>]+>\s*)*</h\1>', src):
        errors.append(f'{page}: empty heading found')

def check_sitemap():
    sp = os.path.join(ROOT, 'sitemap.xml')
    if not os.path.exists(sp):
        errors.append('sitemap.xml: missing')
        return
    with io.open(sp, encoding='utf-8') as f:
        s = f.read()
    locs = re.findall(r'<loc>([^<]+)</loc>', s)
    for l in sorted({x for x in locs if locs.count(x) > 1}):
        errors.append(f'sitemap.xml: duplicate <loc> {l}')
    for l in locs:
        if not os.path.exists(os.path.join(ROOT, l.replace(SITE, ''))):
            errors.append(f'sitemap.xml: {l} → file not found')
    for p in PAGES:
        page = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if page == '404.html' or page.startswith(('admin/', 'dashboard/', 'auth/')):
            continue
        if SITE + page not in locs:
            errors.append(f'sitemap.xml: missing public page {page}')

def main():
    for p in PAGES:
        check_page(p)
    check_sitemap()
    print(f'pages checked: {len(PAGES)}')
    print(f'errors: {len(errors)}   warnings: {len(warnings)}')
    uniq = sorted(set(errors))
    for e in uniq:
        print('  [ERR]', e)
    for w in sorted(set(warnings)):
        print('  [WARN]', w)
    return 0 if not uniq else 1

if __name__ == '__main__':
    sys.exit(main())
