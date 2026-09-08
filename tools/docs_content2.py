# -*- coding: utf-8 -*-
"""Blue Vertex — docs: endpoint pages, SDK, examples, errors, limits, faq, concepts"""

from docs_pages import doc_page, code_blocks, rr_viewer, endpoint_block, param_table, CLI_JS, CLI_PY, CLI_PHP, CLI_GO, CLI_CURL

# ================================================================ USERS ENDPOINT
def build_users(prefix=''):
    p = prefix
    content = f'''
<h1>کاربران</h1>
<p class="doc-desc">منبع <code class="inline">users</code> برای مدیریت کاربران نهایی محصول شماست — نه اعضای تیم. برای هر کاربر، مواردی مثل شناسه، نقش و تاریخ ثبت ذخیره می‌شود.</p>
<div class="doc-updated"><i data-icon="clock"></i> نسخه v1 · آخرین به‌روزرسانی: ۲۸ مرداد ۱۴۰۵</div>

<h2 id="object"><span class="hash">#</span>مدل کاربر</h2>
''' + code_blocks([
        ('json', 'json', '''{
  "id": "usr_8f2k1",
  "name": "سارا احمدی",
  "email": "sara@abrino.ir",
  "role": "developer",
  "status": "active",
  "created_at": "2026-08-02T10:14:22Z"
}'''), ('typescript', 'typescript', '''interface User {
  id: string;
  name: string;
  email: string;
  role: 'developer' | 'admin' | 'viewer';
  status: 'active' | 'suspended';
  created_at: string;
}''')], 'json') + '''
<h2 id="list"><span class="hash">#</span>لیست کاربران</h2>
''' + endpoint_block('GET', '/v1/users', 'فهرست همه کاربران با فیلتر و صفحه‌بندی.') + '''
''' + param_table([
        ('page', 'number', False, 'شماره صفحه — پیش‌فرض ۱'),
        ('limit', 'number', False, 'تعداد در هر صفحه، حداکثر ۱۰۰ — پیش‌فرض ۲۰'),
        ('role', 'enum', False, 'فیلتر نقش: <code class="inline">developer</code> | <code class="inline">admin</code> | <code class="inline">viewer</code>'),
        ('status', 'enum', False, 'فیلتر وضعیت: <code class="inline">active</code> | <code class="inline">suspended</code>'),
        ('search', 'string', False, 'جستجوی نام یا ایمیل (حداقل ۲ کاراکتر)'),
    ]) + '''
<div class="callout"><b class="icon-title"><i data-icon="info"></i> نکته</b><p>فیلترها با هم ترکیب می‌شوند (<code class="inline">AND</code>). برای جستجوی پیشرفته از پارامتر <code class="inline">search</code> استفاده کنید.</p></div>

<h2 id="create"><span class="hash">#</span>ساخت کاربر</h2>
''' + endpoint_block('POST', '/v1/users', 'یک کاربر جدید می‌سازد و آن را با کد <code class="inline">201</code> برمی‌گرداند.') + '''
''' + param_table([
        ('name', 'string', True, 'نام کامل کاربر — ۲ تا ۱۲۰ کاراکتر'),
        ('email', 'email', True, 'ایمیل یکتا — در صورت تکرار خطای <code class="inline">already_exists</code>'),
        ('role', 'enum', False, 'نقش کاربر — پیش‌فرض <code class="inline">developer</code>'),
        ('metadata', 'object', False, 'داده دلخواه (JSON) تا ۱۰ کیلوبایت'),
    ]) + '''
''' + code_blocks([
        ('cURL', 'bash', '''curl -X POST https://api.bluevertex.ir/v1/users \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "name": "سارا احمدی",
    "email": "sara@abrino.ir",
    "role": "developer"
  }' '''),
        ('JavaScript', 'javascript', '''const { data } = await bv.users.create({
  name: 'سارا احمدی',
  email: 'sara@abrino.ir',
  role: 'developer',
});
console.log(data.id); // usr_8f2k1'''),
        ('Python', 'python', '''user = bv.users.create(
    name="سارا احمدی",
    email="sara@abrino.ir",
    role="developer",
)
print(user.id)  # usr_8f2k1'''),
        ('PHP', 'php', '''$user = $bv->users->create([
    'name' => 'سارا احمدی',
    'email' => 'sara@abrino.ir',
]);'''),
        ('Go', 'go', '''user, err := client.Users.Create(ctx, bluevertex.CreateUser{
  Name: "سارا احمدی", Email: "sara@abrino.ir",
})'''),
    ], 'cURL') + '''
''' + rr_viewer({
        'req_body': '{\n  "name": "سارا احمدی",\n  "email": "sara@abrino.ir",\n  "role": "developer"\n}',
        'res_status': '201 Created',
        'res_body': '''{
  "data": {
    "id": "usr_8f2k1",
    "name": "سارا احمدی",
    "email": "sara@abrino.ir",
    "role": "developer",
    "status": "active",
    "created_at": "2026-08-30T10:14:22Z"
  },
  "meta": { "request_id": "req_9d41c7" }
}''',
    }) + '''
<p>برای جلوگیری از ساخت تکراری در تلاش‌های مجدد، هدر <code class="inline">Idempotency-Key</code> را ارسال کنید؛ بلو ورتکس درخواست‌های تکراری را با همان پاسخ اولیه برمی‌گرداند:</p>
''' + code_blocks([
        ('cURL', 'bash', 'curl -X POST https://api.bluevertex.ir/v1/users \\\n  -H "Authorization: Bearer $BV_API_KEY" \\\n  -H "Idempotency-Key: 8f2k-41d7-9a01" \\\n  -d \'{"name":"سارا احمدی","email":"sara@abrino.ir"}\''),
    ], 'cURL') + '''
<h2 id="show"><span class="hash">#</span>دریافت کاربر</h2>
''' + endpoint_block('GET', '/v1/users/{id}', 'جزئیات یک کاربر بر اساس شناسه. اگر کاربر وجود نداشته باشد <code class="inline">404</code> برمی‌گردد.') + '''
<h2 id="update"><span class="hash">#</span>ویرایش کاربر</h2>
''' + endpoint_block('PATCH', '/v1/users/{id}', 'ویرایش جزئی: فقط فیلدهای ارسال‌شده تغییر می‌کنند. برای تغییر ایمیل، ایمیل جدید باید یکتا باشد.') + '''
<h2 id="delete"><span class="hash">#</span>حذف کاربر</h2>
''' + endpoint_block('DELETE', '/v1/users/{id}', 'به‌صورت نرم حذف می‌کند؛ کاربر به وضعیت <code class="inline">deleted</code> می‌رود و دیگر در لیست‌ها نمی‌آید. این عملیات قابل بازگشت نیست.') + '''
<div class="callout danger"><b class="icon-title"><i data-icon="alert-triangle"></i> هشدار</b><p>حذف کاربر قابل بازگشت نیست. ابتدا با <code class="inline">status=suspended</code> کاربر را معلق کنید و پس از بررسی، حذف نهایی کنید.</p></div>

<h2 id="errors"><span class="hash">#</span>خطاهای ویژه این منبع</h2>
''' + param_table([
        ('already_exists', '409', True, 'ایمیل قبلاً ثبت شده است — <code class="inline">error.fields.email</code> را چک کنید.'),
        ('invalid_role', '422', True, 'نقش ارسال‌شده مجاز نیست.'),
        ('email_blocked', '422', True, 'دامنه ایمیل در لیست مسدودهاست.'),
    ], 'کد', 'HTTP', 'توضیح') + '''
'''
    return doc_page('api/users.html', prefix, content,
                    [('object', 'مدل کاربر'), ('list', 'لیست'), ('create', 'ساخت'), ('show', 'دریافت'), ('update', 'ویرایش'), ('delete', 'حذف'), ('errors', 'خطاها')],
                    ('docs/api-reference.html', 'مرجع API', 'prev'),
                    ('docs/api/projects.html', 'پروژه‌ها', 'next'), api=True)

# ================================================================ PROJECTS
def build_projects(prefix=''):
    p = prefix
    content = f'''
<h1>پروژه‌ها</h1>
<p class="doc-desc">پروژه (Project) واحد منطقی درون فضای کاری است؛ کلیدها و مصرف به پروژه متصل می‌شوند و هر پروژه سهمیه مستقل دارد.</p>
<div class="doc-updated"><i data-icon="clock"></i> نسخه v1 · آخرین به‌روزرسانی: ۲۵ مرداد 1405</div>

<h2 id="concept"><span class="hash">#</span>مفهوم</h2>
<p>روابط به این شکل است: <strong>فضای کاری</strong> (Workspace) شامل چند <strong>پروژه</strong> است و هر پروژه چند <strong>کلید API</strong> دارد. مصرف هر کلید زیر همان پروژه ثبت و صورتحساب می‌شود.</p>
<div class="callout"><b class="icon-title"><i data-icon="info"></i> چرا مفید است؟</b><p>اگر محصول شما چند ماژول دارد (مثلاً وب، اپ موبایل و پنل ادمین)، هر کدام پروژه خودش را دارد؛ سهمیه و گزارش‌ها کاملاً مجزا می‌شوند.</p></div>

<h2 id="list"><span class="hash">#</span>لیست پروژه‌ها</h2>
''' + endpoint_block('GET', '/v1/projects', 'پروژه‌های فضای کاری فعلی با آمار مصرف هرکدام (درخواست امروز، سهمیه).') + '''
<h2 id="create"><span class="hash">#</span>ساخت پروژه</h2>
''' + endpoint_block('POST', '/v1/projects', 'پروژه جدید با یک کلید پیش‌فرض تولید می‌کند.') + '''
''' + param_table([
        ('name', 'string', True, 'نام پروژه — ۲ تا ۶۰ کاراکتر'),
        ('description', 'string', False, 'توضیح کوتاه'),
        ('region', 'enum', False, 'منطقه داده: <code class="inline">tehran</code> | <code class="inline">istanbul</code> | <code class="inline">frankfurt</code>'),
    ]) + '''
''' + code_blocks([
        ('cURL', 'bash', '''curl -X POST https://api.bluevertex.ir/v1/projects \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -d '{"name":"پنل مشتریان","region":"tehran"}'
'''),
        ('JavaScript', 'javascript', "const project = await bv.projects.create({\n  name: 'پنل مشتریان',\n  region: 'tehran'\n});"),
    ], 'cURL') + '''
<h2 id="keys"><span class="hash">#</span>کلیدهای پروژه</h2>
''' + endpoint_block('GET', '/v1/projects/{id}/keys', 'کلیدهای فعال هر پروژه با وضعیت، Scopes و آخرین استفاده.') + '''
'''
    return doc_page('api/projects.html', prefix, content,
                    [('concept', 'مفهوم'), ('list', 'لیست'), ('create', 'ساخت'), ('keys', 'کلیدها')],
                    ('docs/api/users.html', 'کاربران', 'prev'),
                    ('docs/api/payments.html', 'پرداخت‌ها', 'next'), api=True)

# ================================================================ PAYMENTS
def build_payments(prefix=''):
    p = prefix
    content = f'''
<h1>پرداخت‌ها</h1>
<p class="doc-desc">ایجاد پرداخت، استعلام وضعیت و لیست پرداخت‌ها — همه با پشتیبانی کامل از <strong>قدرت تکرار (Idempotency)</strong> برای محیط‌های مالی.</p>
<div class="doc-updated"><i data-icon="clock"></i> نسخه v1 · آخرین به‌روزرسانی: ۲۴ مرداد ۱۴۰۵</div>

<h2 id="create"><span class="hash">#</span>ایجاد پرداخت</h2>
''' + endpoint_block('POST', '/v1/payments', 'یک پرداخت جدید می‌سازد و لینک پرداخت (URI) در پاسخ برمی‌گرداند.') + '''
''' + param_table([
        ('amount', 'number', True, 'مبلغ به ریال — حداقل ۱٬۰۰۰ ریال'),
        ('currency', 'enum', True, '<code class="inline">IRT</code> (تومان) یا <code class="inline">IRR</code> (ریال)'),
        ('callback_url', 'url', True, 'آدرس بازگشت پس از پرداخت — باید در پنل تأیید شده باشد'),
        ('description', 'string', False, 'توضیح روی فاکتور — تا ۲۵۰ کاراکتر'),
        ('metadata', 'object', False, 'مرجع داخلی شما (شناسه سفارش و…)، تا ۱۰ کیلوبایت'),
    ]) + '''
<div class="callout warn"><b class="icon-title"><i data-icon="shield"></i> مهم برای محیط مالی</b><p>همیشه هدر <code class="inline">Idempotency-Key</code> بفرستید؛ ارسال دوباره همان کلید، پرداخت تکراری نمی‌سازد و پاسخ اولیه را برمی‌گرداند.</p></div>
''' + code_blocks([
        ('cURL', 'bash', '''curl -X POST https://api.bluevertex.ir/v1/payments \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -H "Idempotency-Key: ord-9921-fa" \\
  -d '{
    "amount": 2500000,
    "currency": "IRT",
    "callback_url": "https://shop.ir/api/callback",
    "metadata": { "order_id": "ord-9921" }
  }' '''),
        ('JavaScript', 'javascript', '''const { data } = await bv.payments.create({
  amount: 2500000,
  currency: 'IRT',
  callback_url: 'https://shop.ir/api/callback',
  metadata: { order_id: 'ord-9921' },
}, { idempotencyKey: 'ord-9921-fa' });'''),
        ('Python', 'python', '''payment = bv.payments.create(
    amount=2_500_000,
    currency="IRT",
    callback_url="https://shop.ir/api/callback",
    idempotency_key="ord-9921-fa",
)'''),
    ], 'cURL') + '''
''' + rr_viewer({
        'req_body': '{\n  "amount": 2500000,\n  "currency": "IRT",\n  "callback_url": "https://shop.ir/api/callback"\n}',
        'res_status': '201 Created',
        'res_body': '''{
  "data": {
    "id": "pay_7f31",
    "amount": 2500000,
    "currency": "IRT",
    "status": "pending",
    "payment_uri": "https://pay.bluevertex.ir/p/7f31"
  }
}''',
    }) + '''
<h2 id="show"><span class="hash">#</span>استعلام پرداخت</h2>
''' + endpoint_block('GET', '/v1/payments/{id}', 'وضعیت لحظه‌ای پرداخت: <code class="inline">pending</code> | <code class="inline">paid</code> | <code class="inline">failed</code> | <code class="inline">refunded</code>.') + '''
<p>برای پرداخت‌های در جریان، <strong>polling معکوس</strong> را توصیه می‌کنیم: ابتدا چند ثانیه صبر کنید و بعد استعلام بفرستید. برای اطلاع لحظه‌ای، <a class="link" href="../webhooks.html" style="font-size:inherit">Webhook رویداد payment.updated</a> را مشترک شوید — به‌جای polling.</p>
<h2 id="list"><span class="hash">#</span>لیست پرداخت‌ها</h2>
''' + endpoint_block('GET', '/v1/payments', 'لیست پرداخت‌ها با فیلتر وضعیت و بازه زمانی (پارامترهای <code class="inline">from</code> و <code class="inline">to</code> به ISO-8601).') + '''
'''
    return doc_page('api/payments.html', prefix, content,
                    [('create', 'ایجاد پرداخت'), ('show', 'استعلام'), ('list', 'لیست')],
                    ('docs/api/projects.html', 'پروژه‌ها', 'prev'),
                    ('docs/api/files.html', 'فایل‌ها', 'next'), api=True)

# ================================================================ FILES
def build_files(prefix=''):
    p = prefix
    content = f'''
<h1>فایل‌ها</h1>
<p class="doc-desc">بارگذاری فایل با دو روش: آپلود مستقیم با <code class="inline">multipart/form-data</code> یا آپلود غیرمستقیم با لینک — برای فایل‌های بزرگ.</p>
<div class="doc-updated"><i data-icon="clock"></i> نسخه v1 · آخرین به‌روزرسانی: ۲۰ مرداد ۱۴۰۵</div>

<h2 id="create"><span class="hash">#</span>بارگذاری فایل</h2>
''' + endpoint_block('POST', '/v1/files', 'فایل را بارگذاری و متادیتای آن را برمی‌گرداند. حداکثر حجم: ۵۰ مگابایت.') + '''
''' + param_table([
        ('file', 'file', True, 'فایل — با روش multipart ارسال می‌شود'),
        ('purpose', 'enum', False, '<code class="inline">document</code> | <code class="inline">avatar</code> | <code class="inline">backup</code>'),
        ('visibility', 'enum', False, '<code class="inline">private</code> (پیش‌فرض) یا <code class="inline">public</code>'),
    ]) + '''
''' + code_blocks([
        ('cURL', 'bash', '''curl -X POST https://api.bluevertex.ir/v1/files \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -F "file=@report.pdf" \\
  -F "purpose=document"'''),
        ('JavaScript', 'javascript', '''const form = new FormData();
form.append('file', fileInput.files[0]);
form.append('purpose', 'document');

const { data } = await bv.files.create(form);
console.log(data.url); // signed url'''),
        ('Python', 'python', '''with open("report.pdf", "rb") as f:
    file = bv.files.create(
        file=f,
        purpose="document",
    )
print(file.url)'''),
    ], 'cURL') + '''
<div class="callout"><b class="icon-title"><i data-icon="info"></i> آپلود بزرگ</b><p>برای فایل‌های بالای ۵۰ مگابایت از روش لینک استفاده کنید: با <code class="inline">POST /v1/files/upload-url</code> لینک موقت بگیرید و فایل را مستقیم به آن بفرستید.</p></div>

<h2 id="show"><span class="hash">#</span>دریافت متادیتا</h2>
''' + endpoint_block('GET', '/v1/files/{id}', 'متادیتای فایل: حجم، نوع MIME، وضعیت و لینک دانلود امضاشده (در صورت مجاز بودن).') + '''
<p>لینک دانلود امضاشده است و تا ۱۵ دقیقه معتبر — مثل هر URL امضاشده‌ای، آن را در سمت کلاینت کَش نکنید.</p>
'''
    return doc_page('api/files.html', prefix, content,
                    [('create', 'بارگذاری'), ('show', 'دریافت متادیتا')],
                    ('docs/api/payments.html', 'پرداخت‌ها', 'prev'),
                    ('docs/sdks.html', 'SDKها', 'next'), api=True)

# ================================================================ SDKS
def build_sdks(prefix=''):
    p = prefix
    return doc_page('sdks', prefix, f'''
<h1>SDKهای رسمی</h1>
<p class="doc-desc">چهار SDK رسمی با تایپ کامل، مدیریت خودکار نرخ و مستندات فارسی. همه SDKها از نظر رفتاری یکسان‌اند — یک‌بار یاد بگیرید، در هر زبانی استفاده کنید.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۹ مرداد ۱۴۰۵ · همه SDKها نسخه پایدار دارند</div>

<h2 id="js"><span class="hash">#</span>JavaScript / TypeScript</h2>
<div class="sdk-card" style="margin-bottom:28px">
  <div class="flex-between" style="flex-wrap:wrap;gap:14px">
    <div><span class="sdk-lang sdk-js">JS</span>
      <h3>@bluevertex/sdk <span class="badge badge-blue">v3.2.0</span></h3>
      <p class="sdk-ver" style="margin-top:6px"><i data-icon="star" style="width:12px;height:12px;color:var(--amber)"></i> ۲٬۳۴۱ ستاره · MIT · سازگار با Node 18+ و مرورگرها</p>
    </div>
    <a class="btn btn-soft" href="examples.html">متنوه‌های استفاده <i data-icon="arrow-left"></i></a>
  </div>
  <div class="code-block sdk-install"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
    <pre class="line-numbers"><code class="language-bash">npm install @bluevertex/sdk</code></pre></div>
</div>

<h2 id="py"><span class="hash">#</span>Python</h2>
<div class="sdk-card" style="margin-bottom:28px">
  <div class="flex-between" style="flex-wrap:wrap;gap:14px">
    <div><span class="sdk-lang sdk-py">Py</span>
      <h3>bluevertex <span class="badge badge-blue">v1.8.0</span></h3>
      <p class="sdk-ver" style="margin-top:6px"><i data-icon="star" style="width:12px;height:12px;color:var(--amber)"></i> ۱٬۹۸۷ ستاره · MIT · سازگار با Python 3.9+ · تایپ کامل (PEP 561)</p>
    </div>
    <a class="btn btn-soft" href="examples.html">متنوه‌های استفاده <i data-icon="arrow-left"></i></a>
  </div>
  <div class="code-block sdk-install"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
    <pre class="line-numbers"><code class="language-bash">pip install bluevertex</code></pre></div>
</div>

<h2 id="php"><span class="hash">#</span>PHP</h2>
<div class="sdk-card" style="margin-bottom:28px">
  <div class="flex-between" style="flex-wrap:wrap;gap:14px">
    <div><span class="sdk-lang sdk-php">PHP</span>
      <h3>bluevertex/php <span class="badge badge-blue">v2.1.0</span></h3>
      <p class="sdk-ver" style="margin-top:6px"><i data-icon="star" style="width:12px;height:12px;color:var(--amber)"></i> ۹۶۴ ستاره · MIT · PHP 8.1+ · PSR-18</p>
    </div>
    <a class="btn btn-soft" href="examples.html">متنوه‌های استفاده <i data-icon="arrow-left"></i></a>
  </div>
  <div class="code-block sdk-install"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
    <pre class="line-numbers"><code class="language-bash">composer require bluevertex/php</code></pre></div>
</div>

<h2 id="go"><span class="hash">#</span>Go</h2>
<div class="sdk-card">
  <div class="flex-between" style="flex-wrap:wrap;gap:14px">
    <div><span class="sdk-lang sdk-go">Go</span>
      <h3>bluevertex-go <span class="badge badge-blue">v1.4.0</span></h3>
      <p class="sdk-ver" style="margin-top:6px"><i data-icon="star" style="width:12px;height:12px;color:var(--amber)"></i> ۷۱۲ ستاره · MIT · Go 1.21+ · بدون وابستگی خارجی</p>
    </div>
    <a class="btn btn-soft" href="examples.html">متنوه‌های استفاده <i data-icon="arrow-left"></i></a>
  </div>
  <div class="code-block sdk-install"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
    <pre class="line-numbers"><code class="language-bash">go get github.com/bluevertex/bluevertex-go</code></pre></div>
</div>

<h2 id="policy"><span class="hash">#</span>سیاست نگهداری</h2>
<p>هر SDK از <strong>سیاست N-2</strong> پیروی می‌کند: دو نسخه مایور آخر پشتیبانی می‌شوند. نسخه‌های ناپایدار با پیش‌وند <code class="inline">beta</code> اعلام می‌شوند و هرگز روی API اصلی اثر نمی‌گذارند.</p>
''', [('js', 'JavaScript'), ('py', 'Python'), ('php', 'PHP'), ('go', 'Go'), ('policy', 'سیاست نگهداری')],
        ('docs/api/files.html', 'فایل‌ها', 'prev'),
        ('docs/examples.html', 'نمونه‌ها', 'next'))

# ================================================================ EXAMPLES
def build_examples(prefix=''):
    p = prefix
    return doc_page('examples', prefix, f'''
<h1>نمونه‌های کاربردی</h1>
<p class="doc-desc">سناریوهای واقعی با کد آماده کپی — از اعتبارسنجی Webhook تا مدیریت خطا. همه نمونه‌ها از مستندات زنده تولید شده‌اند.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۶ مرداد ۱۴۰۵</div>

<h2 id="verify-webhook"><span class="hash">#</span>اعتبارسنجی Webhook</h2>
<p>هر رویداد با هدر <code class="inline">x-bv-signature</code> (امضای HMAC-SHA256) می‌آید. اعتبارسنجی در پایتون:</p>
''' + code_blocks([
        ('Python', 'python', '''import hmac, hashlib

secret = os.environ["BV_WEBHOOK_SECRET"]

def verify(payload: bytes, signature: str) -> bool:
    expected = hmac.new(
        secret.encode(), payload, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

# در هندلر:
if not verify(await request.body(), request.headers["x-bv-signature"]):
    raise HTTPException(401, "امضای نامعتبر است")'''),
        ('JavaScript', 'javascript', '''import crypto from 'node:crypto';

export function verifyWebhook(payload, signature) {
  const expected = crypto
    .createHmac('sha256', process.env.BV_WEBHOOK_SECRET)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(expected), Buffer.from(signature));
}'''),
    ], 'Python') + '''
<h2 id="pagination"><span class="hash">#</span>صفحه‌بندی با حلقه</h2>
''' + code_blocks([
        ('JavaScript', 'javascript', '''let page = 1;
const all = [];

while (true) {
  const { data, meta } = await bv.users.list({ page, limit: 100 });
  all.push(...data);
  if (page >= meta.total_pages) break;
  page += 1;
}
console.log(all.length); // ۱۲۴۰'''),
        ('Python', 'python', '''users = []
page = 1

while True:
    batch, meta = bv.users.list(page=page, limit=100)
    users.extend(batch)
    if page >= meta.total_pages:
        break
    page += 1

print(len(users))  # ۱۲۴۰'''),
    ], 'JavaScript') + '''
<h2 id="errors"><span class="hash">#</span>مدیریت خطا</h2>
''' + code_blocks([
        ('JavaScript', 'javascript', '''try {
  await bv.users.create({ name: '', email: 'bad' });
} catch (err) {
  if (err.code === 'validation_error') {
    // خطای ورودی: جزئیات هر فیلد
    console.error(err.fields.email);
  } else if (err.code === 'rate_limited') {
    // محدودیت نرخ: چند ثانیه صبر کن
    await sleep(err.retryAfter * 1000);
  } else {
    console.error('x-request-id:', err.requestId);
  }
}'''),
        ('Python', 'python', '''try:
    bv.users.create(name="", email="bad")
except bv.errors.ValidationError as e:
    print(e.fields)      # {'email': 'قالب ایمیل نامعتبر است'}
except bv.errors.RateLimitError as e:
    time.sleep(e.retry_after)
except bv.errors.ApiError as e:
    print(e.request_id)  # req_...  برای پیگیری با پشتیبانی'''),
    ], 'JavaScript') + '''
<h2 id="idempotency"><span class="hash">#</span>درخواست امن با Idempotency</h2>
''' + code_blocks([
        ('cURL', 'bash', '''curl -X POST https://api.bluevertex.ir/v1/payments \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -H "Idempotency-Key: pay-$(date +%s)" \\
  -d '{"amount": 2500000, "currency": "IRT"}' '''),
    ], 'cURL') + '''
<div class="callout warn"><b class="icon-title"><i data-icon="alert-triangle"></i> نکته</b><p>کلید Idempotency باید برای هر عملیات <strong>یکتا و ثابت</strong> باشد؛ اگر تلاش مجدد شد، همان کلید قبلی را دوباره بفرستید.</p></div>
''', [('verify-webhook', 'اعتبارسنجی Webhook'), ('pagination', 'صفحه‌بندی'), ('errors', 'مدیریت خطا'), ('idempotency', 'Idempotency')],
        ('docs/sdks.html', 'SDKها', 'prev'),
        ('docs/errors.html', 'خطاها', 'next'))

# ================================================================ ERRORS
def build_errors(prefix=''):
    p = prefix
    rows = [
        ('ERR_NO_KEY', '401', 'هدر Authorization ارسال نشده'),('ERR_INVALID_KEY', '401', 'کلید نامعتبر، منقضی یا باطل‌شده'),
        ('ERR_SCOPE_DENIED', '403', 'کلید مجوز این عملیات را ندارد'),('ERR_NOT_FOUND', '404', 'منبع وجود ندارد یا دسترسی ندارید'),
        ('ERR_CONFLICT', '409', 'تضاد با وضعیت فعلی داده'),('ERR_RATE_LIMIT', '429', 'از محدودیت نرخ عبور کرده‌اید'),
        ('ERR_IDEMPOTENCY', '422', 'کلید Idempotency تکراری با بدنه متفاوت'),('ERR_VALIDATION', '422', 'ورودی نامعتبر — جزئیات در error.fields'),
        ('ERR_INTERNAL', '500', 'خطای داخلی سرور'),('ERR_UNAVAILABLE', '503', 'سرویس موقتاً در دسترس نیست'),
    ]
    tbl = ''
    for code, http, desc in rows:
        cls = 'http-2xx' if http[0] == '2' else 'http-3xx' if http[0] == '3' else 'http-4xx' if http[0] == '4' else 'http-5xx'
        tbl += (f'<tr><td><code class="inline text-code">{code}</code></td>'
                f'<td><span class="http-chip {cls}" title="کد وضعیت HTTP"><i></i>{http}</span></td>'
                f'<td>{desc}</td></tr>')
    return doc_page('errors', prefix, f'''
<h1>خطاها و کدهای وضعیت</h1>
<p class="doc-desc">همه خطاها ساختار یکسان دارند: یک کد ثابت (<code class="inline">error.code</code>) که برای ماشین است و یک پیام فارسی (<code class="inline">error.message</code>) برای انسان.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۵ مرداد ۱۴۰۵</div>

<h2 id="shape"><span class="hash">#</span>ساختار خطا</h2>
''' + code_blocks([
        ('json', 'json', '''{
  "error": {
    "code": "ERR_VALIDATION",
    "message": "ورودی نامعتبر است.",
    "fields": {
      "email": "قالب ایمیل نامعتبر است."
    },
    "doc": "https://docs.bluevertex.ir/errors#validation"
  },
  "meta": { "request_id": "req_9d41c7" }
}'''),
    ], 'json') + '''
<p>همیشه <code class="inline">meta.request_id</code> را در لاگ نگه دارید؛ با این شناسه می‌توانیم هر درخواست را دقیق پیگیری کنیم.</p>

<h2 id="list"><span class="hash">#</span>فهرست خطاها</h2>
<div class="table-wrap"><table class="table param-table">
  <thead><tr><th>کد</th><th>HTTP</th><th>توضیح فارسی</th></tr></thead>
  <tbody>''' + tbl + '''</tbody>
</table></div>

<h2 id="retry"><span class="hash">#</span>چه زمانی Retry کنیم؟</h2>
<p>این جدول را به خاطر بسپارید:</p>
<ul>
  <li><strong>هرگز</strong>: <code class="inline">ERR_VALIDATION</code>، <code class="inline">ERR_SCOPE_DENIED</code>، <code class="inline">ERR_CONFLICT</code> — با اصلاح ورودی حل می‌شوند.</li>
  <li><strong>با تأخیر تصاعدی</strong>: <code class="inline">ERR_RATE_LIMIT</code> (به <code class="inline">Retry-After</code> احترام بگذارید) و <code class="inline">ERR_UNAVAILABLE</code>.</li>
  <li><strong>بله، فقط یک‌بار</strong>: <code class="inline">ERR_INTERNAL</code> — فقط برای درخواست‌های خواندنی.</li>
</ul>
<div class="callout"><b class="icon-title"><i data-icon="info"></i> بهترین روش</b><p>برای درخواست‌های نوشتاری، <code class="inline">idempotency_key</code> را همراه retry ارسال کنید تا نتیجه تکراری نسازید.</p></div>
''', [('shape', 'ساختار خطا'), ('list', 'فهرست خطاها'), ('retry', 'زمان Retry')],
        ('docs/examples.html', 'نمونه‌ها', 'prev'),
        ('docs/limits.html', 'محدودیت‌ها', 'next'))

# ================================================================ LIMITS
def build_limits(prefix=''):
    p = prefix
    return doc_page('limits', prefix, f'''
<h1>محدودیت‌ها و نرخ</h1>
<p class="doc-desc">هر کلید در هر دقیقه سقف درخواست دارد. با عبور از سقف، پاسخ <code class="inline">429</code> همراه هدر <code class="inline">Retry-After</code> برمی‌گردد — درخواست شما هرگز بی‌سروصدا رها نمی‌شود.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۴ مرداد ۱۴۰۵</div>

<h2 id="limits"><span class="hash">#</span>سقف نرخ هر پلن</h2>
<div class="table-wrap"><table class="table param-table">
  <thead><tr><th>پلن</th><th>درخواست در دقیقه</th><th>درخواست در ماه</th><th>پاسخ‌های هم‌زمان</th></tr></thead>
  <tbody>
    <tr><td class="cell-main">رایگان</td><td>۶۰</td><td>۱۰ هزار</td><td>۱۰</td></tr>
    <tr><td class="cell-main">توسعه‌دهنده</td><td>۳۰۰</td><td>۵۰۰ هزار</td><td>۵۰</td></tr>
    <tr><td class="cell-main">رشد</td><td>۱٬۰۰۰</td><td>۵ میلیون</td><td>۲۰۰</td></tr>
    <tr><td class="cell-main">سازمانی</td><td>سفارشی</td><td>سفارشی</td><td>سفارشی</td></tr>
  </tbody>
</table></div>

<h2 id="headers"><span class="hash">#</span>هدرهای نرخ</h2>
<p>هر پاسخ شامل این هدرهاست:</p>
''' + code_blocks([
        ('json', 'json', '''x-ratelimit-limit: 300
x-ratelimit-remaining: 299
x-ratelimit-reset: 42
retry-after: 7   # فقط در پاسخ 429'''),
    ], 'json') + '''
<h2 id="handle"><span class="hash">#</span>مدیریت پاسخ 429</h2>
''' + code_blocks([
        ('JavaScript', 'javascript', '''if (res.status === 429) {
  const wait = Number(res.headers.get('retry-after')) * 1000;
  await sleep(wait);
  return fetch(url, { headers });
}'''),
        ('Python', 'python', '''if resp.status_code == 429:
    wait = int(resp.headers["retry-after"])
    time.sleep(wait)
    return client.get(url)'''),
    ], 'JavaScript') + '''
<div class="callout"><b class="icon-title"><i data-icon="info"></i> حرفه‌ای‌تر</b><p>در SDKها این کار به‌صورت خودکار انجام می‌شود؛ اما حداکثر ۳ تلاش مجدد — بعد از آن خطای <code class="inline">rate_limited</code> می‌گیرید.</p></div>
''', [('limits', 'سقف هر پلن'), ('headers', 'هدرها'), ('handle', 'مدیریت 429')],
        ('docs/errors.html', 'خطاها', 'prev'),
        ('docs/faq.html', 'سوالات متداول', 'next'))

# ================================================================ FAQ
def build_faq(prefix=''):
    p = prefix
    faqs = [
        ('آیا بلو ورتکس برای بازار ایران ساخته شده است؟', 'بله؛ بلو ورتکس یک محصول فارسی‌اول است: رابط کاربری، مستندات، پشتیبانی و حتی نمونه‌کدها برای توسعه‌دهندگان فارسی طراحی شده‌اند. تاریخ‌ها شمسی و پرداخت‌ها به تومان است.'),
        ('تفاوت فضای کاری، پروژه و کلید چیست؟', 'فضای کاری بالاترین سطح است (معمولاً هر شرکت یک فضای کاری). پروژه‌ها واحدهای منطقی داخل فضای کاری‌اند و کلیدها به پروژه متصل می‌شوند. مصرف هر کلید زیر پروژه‌اش ثبت می‌شود.'),
        ('اگر پایگاه داده من PostgreSQL است، سازگارید؟', 'بله. داده‌های شما از طریق REST یا Webhook منتقل می‌شوند و با هر پایگاه داده‌ای سازگارند. در پلن سازمانی امکان استقرار روی زیرساخت خودتان هم هست.'),
        ('آیا محدودیت حجم بدنه درخواست دارم؟', 'حداکثر حجم JSON درخواست ۱ مگابایت است. برای فایل، حداکثر ۵۰ مگابایت با آپلود مستقیم و بیشتر با آپلود لینکی.'),
        ('چطور مصرف خود را کنترل کنم؟', 'بخش «مصرف» داشبورد، مصرف لحظه‌ای و سهمیه باقی‌مانده را نشان می‌دهد و ۸۰٪ سهمیه هشدار می‌دهد. همچنین می‌توانید مصرف هر پروژه را جداگانه ببینید.'),
        ('پشتیبانی چگونه است؟', 'در پلن‌های توسعه‌دهنده به بالا پشتیبانی تیمی ۲۴/۷ داریم؛ پاسخ‌گویی آنلاین از طریق تیکت، تلگرام و تماس تلفنی. در پلن سازمانی مهندس همراه اختصاصی است.'),
        ('آیا داده‌های من داخل ایران می‌ماند؟', 'بله؛ امکان انتخاب منطقه داده (تهران، استانبول یا فرانکفورت) در ساخت پروژه وجود دارد و داده‌ها در همان منطقه ذخیره و پردازش می‌شوند.'),
        ('چطور از مستندات API خودم استفاده کنم؟', 'بلو ورتکس به‌عنوان پلتفرم، مستندات API را از اسکیمای OpenAPI شما تولید و نگهداری می‌کند؛ خروجی یک مرجع تعاملی فارسی با نمونه‌کد چندزبانه است.'),
    ]
    acc = ''
    for i, (q, a) in enumerate(faqs):
        op = ' open' if i == 0 else ''
        mh = '200px' if i == 0 else '0px'
        acc += f'<div class="accordion{op}" data-acc><button class="acc-head">{q}<i data-icon="chevron-down"></i></button><div class="acc-body" style="max-height:{mh}"><div class="acc-inner">{a}</div></div></div>'
    return doc_page('faq', prefix, f'''
<h1 id="faq">سوالات متداول</h1>
<p class="doc-desc">پاسخ پرسش‌های رایج توسعه‌دهندگان و تیم‌های محصول درباره بلو ورتکس. پاسخ سؤال خود را پیدا نکردید؟ از <a class="link" href="{p}pages/contact.html" style="font-size:inherit">پشتیبانی</a> بپرسید.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۳ مرداد ۱۴۰۵</div>

<div class="mt-32">''' + acc + '''</div>

<div class="callout mt-32"><b class="icon-title"><i data-icon="message-square"></i> سؤال دیگری دارید؟</b><p>تیم پشتیبانی بلو استودیو در کمتر از ۲۴ ساعت پاسخ می‌دهد — <a class="link" href="../pages/contact.html" style="font-size:inherit">تماس بگیرید</a>.</p></div>
''', [('faq', 'سوالات متداول')],
        ('docs/limits.html', 'محدودیت‌ها', 'prev'),
        ('docs/api-reference.html', 'مرجع API', 'next'))

# ================================================================ PROJECTS CONCEPT
def build_projects_concept(prefix=''):
    p = prefix
    return doc_page('projects', prefix, '''
<h1>پروژه‌ها و فضای کاری</h1>
<p class="doc-desc">مفاهیم پایه سازمان‌دهی در بلو ورتکس و تفاوت‌شان با یکدیگر.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۵ مرداد ۱۴۰۵</div>

<h2 id="ws"><span class="hash">#</span>فضای کاری (Workspace)</h2>
<p>بالاترین سطح سازمان‌دهی — معمولاً معادل شرکت یا تیم شماست. هر فضای کاری پلن، صورتحساب و اعضای مخصوص خودش را دارد. اعضای تیم در داشبورد دعوت می‌شوند و نقش می‌گیرند.</p>
<h2 id="project"><span class="hash">#</span>پروژه (Project)</h2>
<p>داخل هر فضای کاری می‌توانید چند پروژه بسازید؛ مثلاً «وب‌سایت»، «اپ موبایل» و «هوش مصنوعی». مصرف، سهمیه و کلیدهای هر پروژه مستقل است و گزارش مصرف به تفکیک پروژه در صورت‌حساب می‌آید.</p>
<h2 id="key"><span class="hash">#</span>کلید API</h2>
<p>کلید، واحد احراز هویت است و همیشه به یک پروژه تعلق دارد. با Scopes محدودش کنید؛ ساخت کلید مستقیم در <a class="link" href="../dashboard/api-keys.html" style="font-size:inherit">داشبورد</a> انجام می‌شود.</p>
<div class="callout"><b class="icon-title"><i data-icon="lightbulb"></i> تشبیه</b><p>فضای کاری = ساختمان، پروژه = طبقه، کلید = سوییچ هر اتاق. هر سوییچ فقط برای اتاق خودش کار می‌کند.</p></div>
''', [('ws', 'فضای کاری'), ('project', 'پروژه'), ('key', 'کلید API')],
        ('docs/authentication.html', 'احراز هویت', 'prev'),
        ('docs/webhooks.html', 'Webhookها', 'next'))

# ================================================================ WEBHOOKS
def build_webhooks(prefix=''):
    p = prefix
    return doc_page('webhooks', prefix, f'''
<h1>Webhookها</h1>
<p class="doc-desc">رویدادها را هم‌زمان با وقوع دریافت کنید؛ بدون polling. بلو ورتکس با تلاش مجدد تصاعدی و امضای HMAC تحویل تضمینی می‌دهد.</p>
<div class="doc-updated"><i data-icon="clock"></i> آخرین به‌روزرسانی: ۲۲ مرداد ۱۴۰۵</div>

<h2 id="events"><span class="hash">#</span>رویدادها</h2>
<div class="table-wrap"><table class="table param-table">
<thead><tr><th>رویداد</th><th>وقتی می‌آید</th></tr></thead><tbody>
<tr><td><code class="inline text-code">user.created</code></td><td>کاربر جدید ساخته شد</td></tr>
<tr><td><code class="inline text-code">user.updated</code></td><td>اطلاعات کاربر تغییر کرد</td></tr>
<tr><td><code class="inline text-code">payment.updated</code></td><td>وضعیت پرداخت عوض شد (موفق/ناموفق)</td></tr>
<tr><td><code class="inline text-code">file.completed</code></td><td>پردازش فایل تمام شد</td></tr>
<tr><td><code class="inline text-code">quota.warning</code></td><td>مصرف از ۸۰٪ سهمیه گذشت</td></tr>
</tbody></table></div>

<h2 id="verify"><span class="hash">#</span>بررسی امضا</h2>
<p>هر درخواست Webhook دو هدر امنیتی دارد: <code class="inline">x-bv-signature</code> و <code class="inline">x-bv-delivery</code>. امضا از <code class="inline">HMAC-SHA256</code> روی <strong>بدنه خام</strong> ساخته می‌شود:</p>
''' + code_blocks([
        ('Python', 'python', '''import hmac, hashlib, json

def verify_and_parse(body: bytes, signature: str, secret: str):
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise PermissionError("امضای Webhook نامعتبر است")
    delivery_id = request.headers["x-bv-delivery"]
    # بعد از پردازش موفق، کد 200 برمی‌گردانید تا تلاش مجدد نشود
    return json.loads(body)'''),
        ('JavaScript', 'javascript', '''export function verify(body, signature) {
  const expected = createHmac('sha256', SECRET)
    .update(body).digest('hex');
  return timingSafeEqual(Buffer.from(expected), Buffer.from(signature));
}'''),
    ], 'Python') + '''
<h2 id="retry"><span class="hash">#</span>تلاش مجدد</h2>
<p>اگر کد <code class="inline">2xx</code> برنگردانید، بلو ورتکس با تأخیر <strong>۱، ۵، ۲۵، ۱۲۵ دقیقه</strong> و سپس هر ۶ ساعت تا ۷۲ ساعت تلاش می‌کند. هر تلاش، <code class="inline">x-bv-delivery</code> جدید دارد.</p>
<h2 id="manage"><span class="hash">#</span>مدیریت از داشبورد</h2>
<p>در <a class="link" href="../dashboard/settings.html#panel-webhooks" style="font-size:inherit">تنظیمات Webhook</a> می‌توانید آدرس، رویدادها و کلید امضا را مدیریت، و با «ارسال نمونه» پیام آزمایشی بفرستید. تاریخچه تحویل همیشه در دسترس است.</p>
''', [('events', 'رویدادها'), ('verify', 'بررسی امضا'), ('retry', 'تلاش مجدد'), ('manage', 'مدیریت')],
        ('docs/projects.html', 'پروژه‌ها', 'prev'),
        ('docs/examples.html', 'نمونه‌ها', 'next'))
