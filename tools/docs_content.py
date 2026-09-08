# -*- coding: utf-8 -*-
"""Blue Vertex — documentation content pages (uses helpers from docs_pages)"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts, SEARCH_OVERLAY, SEARCH_DATA_JS
from docs_pages import doc_page, code_blocks, rr_viewer, endpoint_block, param_table, CLI_JS, CLI_PY, CLI_PHP, CLI_GO, CLI_CURL

def build_docs_index(prefix=''):
    p = prefix
    cats = ''
    CATS = [
        ('شروع کار', 'rocket', 'blue', 'معرفی، شروع سریع و نصب SDK', [('شروع سریع', 'getting-started.html'), ('احراز هویت', 'authentication.html'), ('نصب SDK', 'sdks.html')]),
        ('مفاهیم', 'lightbulb', 'green', 'پروژه‌ها، کلیدها و Webhookها', [('پروژه‌ها', 'projects.html'), ('کلیدهای API', 'authentication.html#keys'), ('Webhookها', 'webhooks.html')]),
        ('مرجع API', 'braces', 'violet', 'همه Endpointهای نسخه ۱', [('معرفی API', 'api-reference.html'), ('کاربران', 'api/users.html'), ('پرداخت‌ها', 'api/payments.html')]),
        ('SDK رسمی', 'package', 'amber', 'چهار زبان، یک تجربه', [('JavaScript', 'sdks.html#js'), ('Python', 'sdks.html#py'), ('PHP و Go', 'sdks.html#php')]),
        ('راهنما', 'help-circle', 'cyan', 'نمونه‌ها، خطاها و محدودیت‌ها', [('نمونه‌ها', 'examples.html'), ('کدهای خطا', 'errors.html'), ('محدودیت‌ها', 'limits.html')]),
        ('پشتیبانی', 'headphones', 'red', 'وقتی به کمک نیاز دارید', [('سوالات متداول', 'faq.html'), ('وضعیت سرویس', '../status/index.html'), ('تماس با ما', '../pages/contact.html')]),
    ]
    for title, icon, color, desc, links in CATS:
        ls = ''.join(f'<a href="{p}docs/{h}">{t}</a>' for t, h in links)
        cats += f'''<div class="docs-cat-card" data-reveal>
        <span class="icon-tile icon-tile-{color} icon-tile-sm" style="margin-top:2px"><i data-icon="{icon}"></i></span>
        <div><h3>{title}</h3><p>{desc}</p><div class="links">{ls}</div></div>
      </div>'''
    return head(
        'مستندات | بلو ورتکس',
        'مستندات فارسی بلو ورتکس: شروع سریع، احراز هویت، مرجع API، SDKها، نمونه‌ها، خطاها و سوالات متداول.',
        prefix) + f'''<body class="noise">
''' + navbar('active_docs', prefix) + '''
<section class="page-hero" style="text-align:center;padding-bottom:56px">
  <div class="hero-bg bg-grid" aria-hidden="true"><div class="glow-1" style="top:-300px"></div></div>
  <div class="container" style="position:relative;max-width:780px">
    <nav class="breadcrumb" style="justify-content:center">
      <a href="../index.html">خانه</a><span class="sep"><i data-icon="chevron-left"></i></span><span class="current">مستندات</span>
    </nav>
    <h1 style="font-size:clamp(1.8rem,3.6vw,2.5rem);font-weight:800;line-height:1.4;margin-bottom:12px">مستندات <span class="grad-text-blue">بلو ورتکس</span></h1>
    <p style="color:var(--text-2);font-size:var(--fs-body-lg);max-width:56ch;margin:0 auto 30px;line-height:2">هر آنچه برای اتصال به API بلو ورتکس نیاز دارید — به فارسی، با نمونه‌کد آماده و مرورگر تعاملی.</p>
    <button class="docs-searchbox" data-search-open aria-label="جستجو در مستندات" style="width:100%;max-width:560px;margin:0 auto;padding:14px 18px">
      <i data-icon="search"></i>
      <span style="flex:1;text-align:start;color:var(--text-4)">جستجو در مستندات… (مثلاً «کلید API»)</span>
      <span class="kbd">Ctrl K</span>
    </button>
    <p class="t-caption" style="margin-top:14px">یا از میان‌بر صفحه‌کلید <span class="kbd">⌘K</span> / <span class="kbd">Ctrl K</span> استفاده کنید</p>
  </div>
</section>

<section class="section-sm">
  <div class="container">
    <div class="quickstart-card" data-reveal>
      <span class="icon-tile" style="width:56px;height:56px;border-radius:16px"><i data-icon="rocket"></i></span>
      <div class="txt">
        <h2 style="font-size:1.25rem;font-weight:800;margin-bottom:6px">شروع در ۵ دقیقه</h2>
        <p style="color:var(--text-2);font-size:var(--fs-sm);line-height:1.9;margin:0">حساب بسازید، کلید API تولید کنید و اولین درخواست را ارسال کنید — با راهنمای گام‌به‌گام.</p>
        <div class="kbd-strip"><span class="kbd">۱</span><span class="kbd">۲</span><span class="kbd">۳</span><span class="kbd wide">بدون نصب پیش‌نیاز</span></div>
      </div>
      <a class="btn btn-primary btn-lg" href="getting-started.html">شروع سریع <i data-icon="arrow-left"></i></a>
    </div>

    <div class="docs-home-grid mt-32">
      ''' + cats + '''
    </div>

    <div class="sec-head mt-64" data-reveal style="margin-bottom:32px"><h2>جدیدترین مستندات</h2></div>
    <div class="grid-3" data-reveal>
      <a class="card card-pad card-hover" href="api/users.html"><span class="method method-post mb-16" style="margin-bottom:12px">POST</span><h3 class="t-h4 mb-8">ساخت کاربر</h3><p class="t-caption">نمونه کامل درخواست، پارامترها و پاسخ</p></a>
      <a class="card card-pad card-hover" href="webhooks.html"><span class="badge badge-blue mb-16" style="margin-bottom:12px">راهنما</span><h3 class="t-h4 mb-8">اعتبارسنجی Webhook</h3><p class="t-caption">امضای HMAC و بررسی replay</p></a>
      <a class="card card-pad card-hover" href="errors.html"><span class="badge badge-red mb-16" style="margin-bottom:12px">مرجع</span><h3 class="t-h4 mb-8">کدهای خطا</h3><p class="t-caption">رفع خطاهای 401، 429 و 5xx</p></a>
    </div>
  </div>
</section>
''' + footer(prefix) + SEARCH_OVERLAY + SEARCH_DATA_JS.replace('{p}', prefix) + palette(p) + TOAST_REGION + scripts(prefix, prism=True) + '</body></html>'

# ================================================================ GETTING STARTED
def build_getting_started(prefix=''):
    p = prefix
    content = f'''
<h1>شروع سریع</h1>
<p class="doc-desc">در کمتر از پنج دقیقه حساب بلو ورتکس را بسازید، کلید API تولید کنید و اولین درخواست خود را ارسال کنید.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۹ مرداد ۱۴۰۵ · نسخه ۲٫۴٫۰</div>

<h2 id="prereq"><span class="hash">#</span>پیش‌نیازها</h2>
<p>برای دنبال کردن این راهنما فقط به این‌ها نیاز دارید:</p>
<ul>
  <li>یک حساب بلو ورتکس (ثبت‌نام رایگان است و نیاز به کارت بانکی ندارد)</li>
  <li>علاقه به ارسال اولین درخواست — همین!</li>
</ul>

<h2 id="account"><span class="hash">#</span>مرحله ۱ — ساخت حساب</h2>
<div class="step-item"><span class="step-num">۱</span><div><h3 class="step-title">به <a class="link" href="{p}auth/register.html" style="font-size:inherit">صفحه ثبت‌نام</a> بروید</h3><p>ایمیل کاری و یک رمز عبور قوی کافی است. بدون کارت اعتباری.</p></div></div>
<div class="step-item"><span class="step-num">۲</span><div><h3 class="step-title">فضای کاری خود را تأیید کنید</h3><p>نام فضای کاری را انتخاب کنید؛ مثلاً <code class="inline">abrino</code>. این نام مانند دامنه هویت شما عمل می‌کند.</p></div></div>

<h2 id="keys"><span class="hash">#</span>مرحله ۲ — تولید کلید API</h2>
<p>از داشبورد، بخش <a class="link" href="{p}dashboard/api-keys.html" style="font-size:inherit">کلیدهای API</a>، یک کلید جدید در محیط <code class="inline">production</code> بسازید. کلید فقط یک‌بار نمایش داده می‌شود؛ آن را در <strong>متغیر محیطی</strong> نگه دارید و هرگز در کلاینت قرار ندهید:</p>
''' + code_blocks([
        ('bash', 'bash', 'export BV_API_KEY="bv_live_9f2k1x7aQw4eRt8z"'),
        ('dotenv', 'bash', 'BV_API_KEY=bv_live_9f2k1x7aQw4eRt8z'),
    ], 'bash') + f'''
<div class="callout warn"><b class="icon-title"><i data-icon="alert-triangle"></i> امنیت</b><p>کلید شما هویت شماست. اگر در مخزن عمومی لو رفت، فوراً آن را در داشبورد باطل و کلید جدید بسازید.</p></div>

<h2 id="install"><span class="hash">#</span>نصب SDK</h2>
<p>SDKهای رسمی بلو ورتکس همان API را با تایپ کامل و مدیریت خودکار نشست در اختیارتان می‌گذارند. نصب در یک فرمان:</p>
''' + code_blocks([
        ('npm', 'bash', 'npm install @bluevertex/sdk'),
        ('pip', 'bash', 'pip install bluevertex'),
        ('composer', 'bash', 'composer require bluevertex/client'),
        ('go', 'bash', 'go get github.com/bluevertex/sdk-go'),
    ], 'bash') + '''
<p>جزئیات هر SDK (نمونه‌ها، TypeScript و اشکال‌زدایی) در <a class="link" href="sdks.html" style="font-size:inherit">مرجع SDKها</a> آمده است. بدون SDK هم همه‌چیز با <code class="inline">cURL</code> یا هر کلاینتی کار می‌کند — کافی است هدر <code class="inline">Authorization</code> را بفرستید.</p>

<h2 id="first-req"><span class="hash">#</span>مرحله ۳ — اولین درخواست</h2>
<p>همه درخواست‌ها به پایه آدرس <code class="inline">https://api.bluevertex.ir</code> ارسال می‌شوند و هدر <code class="inline">Authorization</code> الزامی است:</p>
''' + code_blocks([
        ('cURL', 'bash', CLI_CURL),
        ('JavaScript', 'javascript', CLI_JS),
        ('Python', 'python', CLI_PY),
        ('PHP', 'php', CLI_PHP),
        ('Go', 'go', CLI_GO),
    ], 'cURL') + '''
<p>پاسخ موفق، یک شیء JSON با بدنه <code class="inline">data</code> و متادیتای <code class="inline">meta</code> است. هر پاسخ همیشه هدرهای <code class="inline">x-ratelimit-*</code> را همراه دارد.</p>
''' + rr_viewer({
        'req_body': '{\n  "limit": 20,\n  "page": 1\n}',
        'res_status': '200 OK',
        'res_body': '{\n  "data": [\n    {\n      "id": "usr_8f2k1",\n      "name": "سارا احمدی",\n      "email": "sara@abrino.ir"\n    }\n  ],\n  "meta": { "total": 1, "page": 1 }\n}',
    }) + '''
<h2 id="next"><span class="hash">#</span>گام بعدی</h2>
<p>حالا که اولین درخواست شما پاسخ گرفت:</p>
<ul>
  <li><a class="link" href="authentication.html" style="font-size:inherit">مدیریت کلیدها و Scopes</a> را کامل یاد بگیرید.</li>
  <li><a class="link" href="api/users.html" style="font-size:inherit">مرجع Endpoint کاربران</a> را ببینید.</li>
  <li>برای رویدادهای بلادرنگ، <a class="link" href="webhooks.html" style="font-size:inherit">مستندات Webhook</a> را بخوانید.</li>
</ul>
'''
    return doc_page('getting-started', prefix, content,
                    [('prereq', 'پیش‌نیازها'), ('account', 'ساخت حساب'), ('keys', 'تولید کلید'), ('install', 'نصب SDK'), ('first-req', 'اولین درخواست'), ('next', 'گام بعدی')],
                    None,
                    ('docs/authentication.html', 'احراز هویت', 'next'))

# ================================================================ AUTHENTICATION
def build_authentication(prefix=''):
    p = prefix
    content = f'''
<h1>احراز هویت</h1>
<p class="doc-desc">همه درخواست‌ها به یک کلید API نیاز دارند. در این صفحه یاد می‌گیرید کلید بسازید، دسترسی‌ها را محدود کنید و با خیال راحت آن را بچرخانید.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۷ مرداد ۱۴۰۵</div>

<h2 id="how"><span class="hash">#</span>چطور کار می‌کند</h2>
<p>کلید API را در هدر <code class="inline">Authorization</code> با پیشوند <code class="inline">Bearer</code> ارسال کنید. کلیدهای بلو ورتکس با پیشوند <code class="inline">bv_live_</code> (تولید) و <code class="inline">bv_test_</code> (آزمایش) مشخص می‌شوند:</p>
''' + code_blocks([
        ('cURL', 'bash', 'curl https://api.bluevertex.ir/v1/users \\\n  -H "Authorization: Bearer $BV_API_KEY"'),
        ('JavaScript', 'javascript', "const res = await fetch('https://api.bluevertex.ir/v1/users', {\n  headers: { Authorization: `Bearer ${process.env.BV_API_KEY}` }\n});"),
        ('Python', 'python', "import os\nimport bluevertex\n\nbv = bluevertex.Client(api_key=os.environ['BV_API_KEY'])"),
    ], 'cURL') + '''
<h2 id="keys"><span class="hash">#</span>ساخت کلید</h2>
<p>کلیدها در بخش <a class="link" href="../dashboard/api-keys.html" style="font-size:inherit">کلیدهای API داشبورد</a> ساخته می‌شوند. هنگام ساخت، دو تصمیم مهم دارید:</p>
''' + param_table([
        ('environment', 'enum', True, 'محیط کلید: <code class="inline">production</code> یا <code class="inline">test</code> — داده‌ها و سهمیه مجزا دارند.'),
        ('scopes', 'array', False, 'دسترسی‌های مجاز. بدون انتخاب، کلید فقط دسترسی‌های خواندنی دارد.'),
        ('expires_in', 'number', False, 'انقضا به روز؛ برای کلیدهای موقت مثل CI/CD عالی است.'),
    ], 'ویژگی', 'نوع', 'توضیح') + '''
<h2 id="scopes"><span class="hash">#</span>دسترسی‌ها (Scopes)</h2>
<p>Scopes کوچک‌ترین واحد مجوز هستند. اصل را رعایت کنید: <strong>کمترین دسترسی لازم</strong>.</p>
<div class="table-wrap"><table class="table"><thead><tr><th>Scope</th><th>اجازه</th></tr></thead><tbody>
<tr><td><code class="inline">users.read</code></td><td>خواندن کاربران</td></tr>
<tr><td><code class="inline">users.write</code></td><td>ساخت، ویرایش و حذف کاربران</td></tr>
<tr><td><code class="inline">payments.read</code></td><td>مشاهده پرداخت‌ها</td></tr>
<tr><td><code class="inline">payments.write</code></td><td>ایجاد پرداخت و استعلام</td></tr>
<tr><td><code class="inline">files.write</code></td><td>بارگذاری فایل</td></tr>
<tr><td><code class="inline">analytics.read</code></td><td>خواندن گزارش‌ها و تحلیل‌ها</td></tr>
</tbody></table></div>

<h2 id="rotate"><span class="hash">#</span>چرخش امن کلید</h2>
<p>چرخش کلید نباید باعث قطعی شود. الگوی پیشنهادی:</p>
<ol>
  <li>کلید جدید با همان Scopes بسازید — هر دو کلید هم‌زمان فعال‌اند.</li>
  <li>اپلیکیشن را به کلید جدید منتقل کنید (Canary یا کامل).</li>
  <li>کلید قبلی را در داشبورد باطل کنید. درخواست‌هایی که هنوز با کلید قدیمی می‌آیند، <code class="inline">401</code> می‌گیرند.</li>
</ol>

<h2 id="errors"><span class="hash">#</span>خطاهای احراز هویت</h2>
''' + param_table([
        ('ERR_NO_KEY', '401', True, 'هدر Authorization ارسال نشده است.'),
        ('ERR_INVALID_KEY', '401', True, 'کلید نامعتبر، منقضی یا باطل‌شده است.'),
        ('ERR_SCOPE', '403', True, 'کلید معتبر است اما دسترسی این Scope را ندارد.'),
        ('ERR_TEST_KEY', '403', True, 'کلید آزمایش روی Endpoint تولیدی استفاده شده است.'),
    ], 'کد', 'HTTP', 'توضیح') + '''
<div class="callout"><b class="icon-title"><i data-icon="info"></i> نکته</b><p>خطاهای احراز هویت هرگز جزئیات داخلی سرور را لو نمی‌دهند؛ پیام‌ها یکدست و قابل اعتمادند.</p></div>
'''
    return doc_page('authentication', prefix, content,
                    [('how', 'چطور کار می‌کند'), ('keys', 'ساخت کلید'), ('scopes', 'دسترسی‌ها'), ('rotate', 'چرخش کلید'), ('errors', 'خطاها')],
                    ('docs/getting-started.html', 'شروع سریع', 'prev'),
                    ('docs/api-reference.html', 'مرجع API', 'next'))

# ================================================================ API REFERENCE INDEX
def build_api_reference(prefix=''):
    p = prefix
    groups = [
        ('کاربران', 'users', [
            ('GET', '/v1/users', 'لیست کاربران با فیلتر و صفحه‌بندی'),
            ('POST', '/v1/users', 'ساخت کاربر جدید'),
            ('GET', '/v1/users/{id}', 'دریافت یک کاربر'),
            ('PATCH', '/v1/users/{id}', 'ویرایش جزئی کاربر'),
            ('DELETE', '/v1/users/{id}', 'حذف کاربر'),
        ]),
        ('پروژه‌ها', 'projects', [
            ('GET', '/v1/projects', 'لیست پروژه‌های فضای کاری'),
            ('POST', '/v1/projects', 'ساخت پروژه جدید'),
            ('GET', '/v1/projects/{id}/keys', 'کلیدهای هر پروژه'),
        ]),
        ('پرداخت‌ها', 'payments', [
            ('POST', '/v1/payments', 'ایجاد پرداخت (با Idempotency-Key)'),
            ('GET', '/v1/payments/{id}', 'استعلام وضعیت پرداخت'),
            ('GET', '/v1/payments', 'لیست پرداخت‌ها'),
        ]),
        ('فایل‌ها', 'files', [
            ('POST', '/v1/files', 'بارگذاری فایل (multipart یا URL)'),
            ('GET', '/v1/files/{id}', 'دریافت متادیتای فایل'),
        ]),
    ]
    g_html = ''
    for gtitle, slot, eps in groups:
        rows = ''
        for m, path, desc in eps:
            rows += (f'<tr class="clickable" onclick="location.href=\'{p}docs/api/{slot}.html\'">'
                     f'<td><span class="method method-{m.lower()}">{m}</span></td>'
                     f'<td><code class="inline text-code">{path}</code></td><td>{desc}</td>'
                     f'<td><a class="link" href="{p}docs/api/{slot}.html" aria-label="مشاهده"><i data-icon="arrow-left" style="width:13px;height:13px"></i></a></td></tr>')
        g_html += f'''<div class="endpoint-card">
      <div class="flex-between mb-16" style="flex-wrap:wrap"><h3 class="t-h4">{gtitle}</h3><a class="link" href="{p}docs/api/{slot}.html" style="font-size:var(--fs-caption)">مشاهده کامل <i data-icon="arrow-left"></i></a></div>
      <div class="table-wrap" style="border:none"><table class="table"><tbody>{rows}</tbody></table></div>
    </div>'''
    content = f'''
<h1>مرجع API</h1>
<p class="doc-desc">پایگاه آدرس همه درخواست‌ها <code class="inline">https://api.bluevertex.ir</code> و نسخه فعلی <code class="inline">v1</code> است. همه Endpointها به هدر <code class="inline">Authorization: Bearer</code> نیاز دارند.</p>
<div class="doc-updated"><i data-icon="clock"></i> نسخه v1 · آخرین به‌روزرسانی: ۲۹ مرداد ۱۴۰۵</div>

<div class="endpoint-card">
  <div class="ep-line"><span class="method method-get">GET</span><span class="ep-url">https://api.bluevertex.ir/v1</span></div>
  <p class="ep-desc">نمای کلی: نسخه، وضعیت و محدودیت نرخ هنر فضای کاری.</p>
  <div class="ep-flags"><span class="badge badge-blue">احراز هویت: Bearer</span><span class="badge">نرخ: ۶۰ در دقیقه</span></div>
</div>

<h2 id="pagination"><span class="hash">#</span>صفحه‌بندی و فیلتر</h2>
<p>همه لیست‌ها با پارامترهای <code class="inline">page</code> و <code class="inline">limit</code> (حداکثر ۱۰۰) صفحه‌بندی می‌شوند و متادیتا در <code class="inline">meta</code> برمی‌گردد:</p>
''' + code_blocks([
        ('cURL', 'bash', 'curl "https://api.bluevertex.ir/v1/users?page=2&limit=25&role=developer" \\\n  -H "Authorization: Bearer $BV_API_KEY"'),
        ('JavaScript', 'javascript', "const { data, meta } = await bv.users.list({ page: 2, limit: 25 });\nconsole.log(meta.total, meta.page);"),
    ], 'cURL') + '''
<h2 id="status"><span class="hash">#</span>کدهای وضعیت</h2>
''' + param_table([
        ('200', 'OK', True, 'درخواست موفق — بدنه داده در <code class="inline">data</code>'),
        ('201', 'Created', True, 'منبع جدید ساخته شد (Endpointهای POST)'),
        ('400', 'Bad Request', True, 'ورودی نامعتبر — جزئیات در <code class="inline">error.fields</code>'),
        ('401', 'Unauthorized', True, 'کلید نامعتبر یا غایب'),
        ('403', 'Forbidden', True, 'دسترسی Scope مجاز نیست'),
        ('404', 'Not Found', True, 'منبع وجود ندارد'),
        ('409', 'Conflict', True, 'تضاد با وضعیت فعلی (مثلاً ایمیل تکراری)'),
        ('429', 'Too Many Requests', True, 'محدودیت نرخ — هدر <code class="inline">Retry-After</code> را ببینید'),
        ('500', 'Server Error', True, 'خطای داخلی — با <code class="inline">x-request-id</code> پیگیری کنید'),
    ], 'کد', 'نام', 'توضیح') + '''
<h2 id="explorer"><span class="hash">#</span>مرورگر تعاملی</h2>
<p>در <a class="link" href="../dashboard/endpoints.html" style="font-size:inherit">بخش Endpointهای داشبورد</a> می‌توانید هر Endpoint را با داده نمونه آزمایش کنید — بدون نیاز به کلید واقعی.</p>
''' + g_html
    return doc_page('api-reference', prefix, content,
                    [('pagination', 'صفحه‌بندی'), ('status', 'کدهای وضعیت'), ('explorer', 'مرورگر تعاملی')],
                    ('docs/authentication.html', 'احراز هویت', 'prev'),
                    ('docs/api/users.html', 'کاربران', 'next'), api=True)
