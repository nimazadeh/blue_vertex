# -*- coding: utf-8 -*-
"""Blue Vertex — documentation platform pages"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts, docs_sidebar, api_sidebar, SEARCH_OVERLAY, SEARCH_DATA_JS

DOCS_META = {
    'getting-started': ('شروع سریع | مستندات بلو ورتکس', 'شروع کار با بلو ورتکس در کمتر از ۵ دقیقه: ساخت حساب، تولید کلید API و ارسال اولین درخواست.'),
    'authentication': ('احراز هویت | مستندات بلو ورتکس', 'احراز هویت با کلید API در بلو ورتکس: ساخت کلید، Scopes، هدر Authorization، چرخش و خطاهای متداول.'),
    'api-reference': ('مرجع API | مستندات بلو ورتکس', 'مرجع کامل API بلو ورتکس نسخه ۱ — احراز هویت، صفحه‌بندی، کدهای وضعیت و تمام Endpointها.'),
    'sdks': ('SDKها | مستندات بلو ورتکس', 'جواسکریپت، پایتون، PHP و گو — نصب، نگارش، مستندات و نمونهٔ استفاده از SDKهای بلو ورتکس.'),
    'examples': ('نمونه‌ها | مستندات بلو ورتکس', 'نمونه‌های کاربردی بلو ورتکس: احراز هویت، Webhook امن، صفحه‌بندی و مدیریت خطا به چند زبان.'),
    'errors': ('خطاها | مستندات بلو ورتکس', 'فهرست کامل کدهای خطای بلو ورتکس با توضیح فارسی، کد HTTP و راه‌حل هر خطا.'),
    'limits': ('محدودیت‌ها | مستندات بلو ورتکس', 'محدودیت نرخ درخواست و سهمیه هر پلن بلو ورتکس به‌همراه مدیریت پاسخ 429.'),
    'faq': ('سوالات متداول | مستندات بلو ورتکس', 'پاسخ سوالات رایج توسعه‌دهندگان درباره بلو ورتکس: کلیدها، مصرف، صورتحساب و پشتیبانی.'),
    'projects': ('پروژه‌ها | مستندات بلو ورتکس', 'مفهوم پروژه (Project) در بلو ورتکس و تفاوت آن با فضای کاری و کلید API.'),
    'webhooks': ('Webhookها | مستندات بلو ورتکس', 'رویدادها، امضای HMAC، تلاش مجدد و مدیریت Webhook در بلو ورتکس.'),
    'api/users.html': ('کاربران | مرجع API بلو ورتکس', 'Endpointهای کاربران: لیست، ساخت، دریافت، ویرایش و حذف — با پارامترها، نمونه کد و پاسخ.'),
    'api/projects.html': ('پروژه‌ها | مرجع API بلو ورتکس', 'Endpointهای پروژه‌ها: لیست و ساخت پروژه به‌همراه کلیدهای هر پروژه.'),
    'api/payments.html': ('پرداخت‌ها | مرجع API بلو ورتکس', 'Endpointهای پرداخت: ایجاد، استعلام و لیست — با پشتیبانی کامل Idempotency.'),
    'api/files.html': ('فایل‌ها | مرجع API بلو ورتکس', 'Endpointهای فایل: بارگذاری مستقیم و با لینک، و دریافت متادیتا.'),
}

# ---------------------------------------------------- building blocks

def code_blocks(snippets, active='curl'):
    """snippets: list of (lang_label, lang_class, code_text)"""
    tabs = ''
    panels = ''
    for i, (label, lang, code) in enumerate(snippets):
        act = ' active' if label == active else ''
        tabs += f'<button class="code-tab{act}" data-lang="{label}">{label}</button>'
        actp = ' active' if label == active else ''
        panels += (f'<div class="code-tab-panel{actp}" data-lang-panel="{label}">'
                   f'<div class="code-block"><div class="code-head"><span class="code-lang">{label}</span>'
                   f'<button class="code-copy" data-copy-target="#cb_{i}" aria-label="کپی"><i data-icon="copy"></i></button></div>'
                   f'<pre id="cb_{i}" class="line-numbers"><code class="language-{lang}">{code}</code></pre></div></div>')
    return f'<div data-code-tabs><div class="code-tabs">{tabs}</div>{panels}</div>'

def rr_viewer(examples, active='req'):
    """examples: dict with 'req': (headers_html, body_text), 'res': (status_line, header_lines, body_text)"""
    req_headers = examples.get('req_headers', '')
    req_body = examples.get('req_body', '')
    res_status = examples.get('res_status', '200 OK')
    res_headers = examples.get('res_headers', '')
    res_body = examples.get('res_body', '')
    js_req = f'''<pre class="line-numbers" style="margin:0;background:transparent;border:none"><code class="language-json">{req_body}</code></pre>'''
    js_res = f'''<pre class="line-numbers" style="margin:0;background:transparent;border:none"><code class="language-json">{res_body}</code></pre>'''
    return f'''<div class="rr" id="expRR" data-tabs-scope>
  <div class="rr-tabs" data-tabs>
    <button class="rr-tab active" data-tab="req"><i data-icon="arrow-up-circle"></i> درخواست</button>
    <button class="rr-tab" data-tab="res"><i data-icon="arrow-down-circle"></i> پاسخ</button>
    <button class="rr-tab" data-tab="headers"><i data-icon="list"></i> هدرها</button>
  </div>
  <div class="rr-panel active" data-panel="req"><div class="code-block">{js_req}</div></div>
  <div class="rr-panel" data-panel="res">
    <div class="rr-meta">
      <div class="rr-meta-item"><span>وضعیت</span><b class="ltr">{res_status}</b></div>
      <div class="rr-meta-item"><span>تأخیر</span><b class="fa-num">۴۸ms</b></div>
      <div class="rr-meta-item"><span>اندازه</span><b class="fa-num">۸۴۲ بایت</b></div>
      <div class="rr-meta-item"><span>Request ID</span><b class="ltr" style="font-size:.7rem">req_9d41c7</b></div>
    </div>
    <div class="code-block"><div class="code-head"><span class="code-lang">json</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>{js_res}</div>
  </div>
  <div class="rr-panel" data-panel="headers">
    <div class="kv-group-title">هدرهای درخواست</div>
    <table class="kv-table"><tbody>
      <tr><td>Authorization</td><td>Bearer bv_live_••••••••</td></tr>
      <tr><td>Content-Type</td><td>application/json</td></tr>
      <tr><td>Idempotency-Key</td><td>8f2k-41d7-9a01</td></tr>
    </tbody></table>
    <div class="kv-group-title">هدرهای پاسخ</div>
    <table class="kv-table"><tbody>
      <tr><td>content-type</td><td>application/json</td></tr>
      <tr><td>x-request-id</td><td>req_9d41c7</td></tr>
      <tr><td>x-ratelimit-remaining</td><td>9991</td></tr>
      <tr><td>x-ratelimit-limit</td><td>10000</td></tr>
    </tbody></table>
  </div>
</div>'''

def endpoint_block(method, url, desc, params_html='', body_note=''):
    return f'''<div class="endpoint-card" id="{url.strip('/').replace('/', '_')}">
  <div class="ep-line"><span class="method method-{method.lower()}">{method}</span><span class="ep-url">{url}</span></div>
  <p class="ep-desc">{desc}</p>
  {params_html}
</div>'''

def param_table(rows, required_title='پارامتر', type_title='نوع', desc_title='توضیح'):
    body = ''
    for name, typ, req, desc in rows:
        req_html = '<span class="param-required">الزامی</span>' if req else '<span class="param-optional">اختیاری</span>'
        body += f'<tr><td><code class="inline">{name}</code></td><td><span class="t-caption ltr">{typ}</span></td><td>{req_html}</td><td>{desc}</td></tr>'
    return f'''<div class="table-wrap" style="margin:16px 0"><table class="table param-table">
  <thead><tr><th>{required_title}</th><th>{type_title}</th><th>وضعیت</th><th>{desc_title}</th></tr></thead>
  <tbody>{body}</tbody></table></div>'''

def doc_page(key, prefix, content, toc, prev, next_, api=False, extra_sidebar=''):
    title, desc = DOCS_META[key]
    toc_html = ''.join(f'<a class="toc-link" href="#{cid}">{t}</a>' for cid, t in toc)
    pager = ''
    for card in (prev, next_):
        if not card:
            pager += '<div class="pager-card" style="opacity:.4;pointer-events:none"><span class="pager-label">—</span></div>'
        else:
            lbl = 'قبلی' if card[2] == 'prev' else 'بعدی'
            cls = ' prev' if card[2] == 'prev' else ' next'
            arr = 'arrow-right' if card[2] == 'prev' else 'arrow-left'
            pager += (f'<a class="pager-card{cls}" href="{prefix}{card[0]}"><span class="pager-label">'
                      f'<i data-icon="{arr}"></i> {lbl}</span><b>{card[1]}</b></a>')
    sidebar = docs_sidebar(key if not api else 'docs/api/users.html', prefix) if not api else api_sidebar(key, prefix)
    shell_cls = 'api-shell api-shell-notoc' if api else 'docs-shell'
    main_cls = 'api-main' if api else 'docs-main'
    canon_url = ('docs/' + key) if key.endswith('.html') else ('docs/' + key + '.html')
    return head(title, desc, prefix, canonical=prefix + canon_url) + f'''<body class="noise">
''' + navbar('active_docs', prefix) + f'''
<div class="{shell_cls}">
  {sidebar}
  <main class="{main_cls}">
    <div class="docs-search-sticky">
      <button class="docs-searchbox w-full" data-search-open aria-label="جستجو در مستندات" style="width:100%">
        <i data-icon="search"></i>
        <span style="color:var(--text-4);font-size:var(--fs-sm)">جستجو در مستندات، API و راهنماها…</span>
        <span class="kbd">Ctrl K</span>
      </button>
    </div>
    <nav class="breadcrumb" aria-label="مسیر صفحه">
      <a href="{prefix}docs/index.html">مستندات</a><span class="sep"><i data-icon="chevron-left"></i></span>
      <span class="current">{toc[0][1] if toc else ''}</span>
    </nav>
    <div class="doc-article">
    {content}
    </div>
    <div class="doc-pager">{pager}</div>
  </main>
  <aside class="docs-toc" aria-label="فهرست مطالب" style="display:{'none' if api else ''}">
    <div class="toc-title"><i data-icon="list"></i> در این صفحه</div>
    <nav class="toc-list" id="tocList">{toc_html}</nav>
    <div class="mt-32">
      <div class="toc-title"><i data-icon="life-buoy"></i> کمک بگیرید</div>
      <a class="btn btn-outline btn-sm btn-block" href="{prefix}pages/contact.html">تماس با پشتیبانی</a>
      <a class="btn btn-ghost btn-sm btn-block mt-8" href="{prefix}status/index.html"><i data-icon="activity"></i> وضعیت سرویس</a>
    </div>
  </aside>
</div>
''' + SEARCH_OVERLAY + SEARCH_DATA_JS.replace('{p}', prefix) + palette(prefix) + TOAST_REGION + scripts(prefix, prism=True) + '''
<script>window.BV_DOCS_PAGE = ''' + ('true' if api else 'true') + ''';</script>
</body></html>'''

CLI_JS = '''const bv = new BlueVertex({ apiKey: 'bv_live_...' });
const users = await bv.users.list({ limit: 20, page: 1 });
console.log(users.data);'''

CLI_PY = '''from bluevertex import BlueVertex

bv = BlueVertex(api_key="bv_live_...")
users = bv.users.list(limit=20, page=1)
print(users.data)'''

CLI_PHP = '''<?php
require 'vendor/autoload.php';

$bv = new BlueVertex\\Client('bv_live_...');
$users = $bv->users->list(['limit' => 20]);'''

CLI_GO = '''client := bluevertex.New("bv_live_...")
users, err := client.Users.List(ctx, 20, 1)
if err != nil { log.Fatal(err) }'''

CLI_CURL = '''curl https://api.bluevertex.ir/v1/users \\
  -H "Authorization: Bearer bv_live_..." \\
  -G --data-urlencode "limit=20"'''
