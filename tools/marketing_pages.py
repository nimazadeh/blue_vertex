# -*- coding: utf-8 -*-
"""Blue Vertex — marketing inner pages"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts

PREFIX = ''  # resolved per page

def page_hero(breadcrumb, title, lead, eyebrow=None):
    eb = f'<span class="sec-eyebrow" style="margin-bottom:20px">{eyebrow}</span>' if eyebrow else ''
    return f'''<section class="page-hero">
  <div class="hero-bg bg-grid" aria-hidden="true"><div class="glow-1" style="top:-260px"></div></div>
  <div class="container" style="position:relative">
    <nav class="breadcrumb" aria-label="مسیر صفحه">{breadcrumb}</nav>
    {eb}
    <h1 data-reveal>{title}</h1>
    <p data-reveal>{lead}</p>
  </div>
</section>'''

def crumb(prefix, current):
    return f'<a href="{prefix}index.html">خانه</a><span class="sep"><i data-icon="chevron-left"></i></span><span class="current">{current}</span>'

# ================================================================ FEATURES
def build_features(prefix=''):
    p = prefix
    f = lambda x: x
    features_sec = ''
    FEATS = [
        ('api', 'API نسخه‌بندی‌شده', 'braces', 'blue',
         'یک API مدرن با نسخه‌بندی شفاف (v1)، محدودیت نرخ هر Endpoint و کدهای خطای معنادار. نمونه‌کد خودکار برای پنج زبان.',
         ['نسخه‌بندی semver با سازگاری عقب‌رو', 'محدودیت نرخ و سهمیه‌بندی شفاف', 'خطاهای فارسی با کد، پیام و راهنمای رفع'],
         'code_visual'),
        ('security', 'امنیت سازمانی', 'shield-check', 'green',
         'TLS 1.3 در همه ارتباطات، رمزنگاری AES-256 در حالت سکون و گزارش ممیزی کامل برای هر تغییر حساس.',
         ['کلیدهای دارای Scopes و تاریخ انقضا', 'تشخیص فعالیت غیرعادی و هشدار آنی', 'مطابق با اصول SOC 2 و ISO 27001'],
         'list_visual'),
        ('auth', 'احراز هویت', 'key-round', 'amber',
         'از کلید API ساده تا OAuth 2.0 کامل. چرخش کلید بدون قطعی، نشست‌های امن و ورود دومرحله‌ای برای تیم شما.',
         ['API Key ،OAuth 2.0 و JWT', 'چرخش کلید با دوره هم‌پوشانی', 'ورود دومرحله‌ای TOTP'],
         'auth_visual'),
        ('webhooks', 'Webhookهای قابل‌اعتماد', 'webhook', 'violet',
         'تحویل تضمینی رویدادها با تلاش مجدد تصاعدی، امضای HMAC و مشاهده تاریخچه تحویل در داشبورد.',
         ['امضای HMAC-SHA256 و چرخش کلید امضا', 'صف داخلی با تضمین at-least-once', 'تست Webhook با ارسال نمونه'],
         'code_visual'),
        ('analytics', 'تحلیل و مانیتورینگ', 'line-chart', 'cyan',
         'حجم درخواست، نرخ خطا، تأخیر P50/P95/P99 و توزیع جغرافیایی — بلادرنگ و با تاریخ شمسی.',
         ['فیلتر بر اساس Endpoint و محیط', 'مقایسه نسخه‌های API با هم', 'خروجی CSV برای تحلیل‌های بیشتر'],
         'chart_visual'),
        ('monitoring', 'پایش و هشدار', 'activity', 'red',
         'نظارت خودکار بر سلامت سرویس و هشدار از طریق Telegram، ایمیل یا Webhook شما هنگام بروز مشکل.',
         ['هشدار نرخ خطا و تأخیر', 'صفحه وضعیت عمومی برای مشتریان', 'تاریخچه حوادث با گام‌های زمانی'],
         'code_visual'),
        ('sdk', 'SDKهای بومی', 'package', 'blue',
         'جاوااسکریپت/TypeScript، پایتون، PHP و گو با تایپ کامل، نمونه‌های فارسی و نصب با یک فرمان.',
         ['تایپ اسکریپت و تایپ‌های کامل', 'مدیریت خودکار نرخ درخواست', 'ارتقای امن و هشدار EOL'],
         'sdk_visual'),
        ('team', 'تیم و دسترسی‌ها', 'users', 'green',
         'دعوت اعضا، نقش‌های دقیق (مالک، مدیر، توسعه‌دهنده، بیننده) و گزارش فعالیت هر عضو.',
         ['نقش‌های آماده + نقش سفارشی', 'دعوت با لینک یا ایمیل', 'گزارش فعالیت و ممیزی اعضا'],
         'team_visual'),
        ('billing', 'صورتحساب شفاف', 'credit-card', 'amber',
         'فاکتور دقیق به تومان، تاریخ شمسی، فیلتر مصرف بر اساس کلید و دانلود فاکتور PDF.',
         ['پرداخت ریالی و بدون کارت خارجی', 'هشدار پیش از رسیدن به سقف هزینه', 'گزارش هزینه به تفکیک پروژه'],
         'billing_visual'),
    ]
    for i, (id, title, icon, color, desc, points, visual) in enumerate(FEATS):
        ptags = ''.join(f'<li><i data-icon="check-circle-2"></i>{x}</li>' for x in points)
        if visual == 'code_visual':
            vis = f'''<div class="code-window" dir="ltr" style="text-align:left">
              <div class="cw-head"><span class="window-dots"><i></i><i></i><i></i></span><span class="cw-tabs"><span class="cw-tab active">bash</span></span></div>
              <pre style="margin:0;padding:18px 20px;font-size:.8rem"><code class="language-bash">curl https://api.bluevertex.ir/v1/users \\
  -H "Authorization: Bearer $BV_KEY" \\
  -d '{{"name":"سارا احمدی","email":"sara@abrino.ir"}}'</code></pre>
            </div>'''
        elif visual == 'chart_visual':
            vis = '''<div class="window"><div class="window-bar"><span class="window-dots"><i></i><i></i><i></i></span><span class="window-title"><i data-icon="activity"></i> نرخ موفقیت</span></div>
              <div class="win-main"><div class="mini-chart-holder" style="height:150px">
                <canvas data-chart data-chart-type="line" data-fill="1" data-no-rtl="1" data-labels='["۱","۲","۳","۴","۵","۶","۷","۸"]' data-values='[99.7,99.8,99.9,99.85,99.95,99.92,99.98,99.97]' data-colors='["rgb(52,211,153)"]' data-name="نرخ موفقیت" data-unit="٪"></canvas>
              </div></div></div>'''
        elif visual == 'auth_visual':
            vis = '''<div class="window"><div class="window-bar"><span class="window-dots"><i></i><i></i><i></i></span><span class="window-title"><i data-icon="key-round"></i> کلید API</span></div>
              <div class="win-main">
                <div class="field" style="margin-bottom:10px"><span class="field-label">کلید تولید جدید</span>
                  <div class="key-reveal-box" style="margin:0"><code id="fDemoKey">bv_live_9f2k1x7aQw4eRt8z</code>
                  <button class="btn btn-soft btn-sm" data-copy-target="#fDemoKey" data-copy="bv_live_9f2k1x7aQw4eRt8z">کپی</button></div>
                </div>
                <div class="flex gap-8" style="flex-wrap:wrap"><span class="badge badge-blue">scopes: users.read</span><span class="badge badge-blue">users.write</span><span class="badge">انقضا: ۹۰ روز</span></div>
              </div></div>'''
        elif visual == 'sdk_visual':
            vis = '''<div class="grid grid-2" style="gap:12px">
              <div class="sdk-card" style="padding:20px"><span class="sdk-lang sdk-js">JS</span><h3 class="t-h4 mb-8">TypeScript</h3><p class="t-caption">نسخه ۳٫۲٫۰ — ۴۸KB</p><div class="code-window" style="margin-top:12px"><pre style="margin:0;padding:10px 14px;font-size:.7rem"><code class="language-bash">npm i @bluevertex/sdk</code></pre></div></div>
              <div class="sdk-card" style="padding:20px"><span class="sdk-lang sdk-py">Py</span><h3 class="t-h4 mb-8">Python</h3><p class="t-caption">نسخه ۱٫۸٫۰ — سازگار ۳٫۹+</p><div class="code-window" style="margin-top:12px"><pre style="margin:0;padding:10px 14px;font-size:.7rem"><code class="language-bash">pip install bluevertex</code></pre></div></div>
            </div>'''
        elif visual == 'team_visual':
            vis = '''<div class="window"><div class="window-bar"><span class="window-dots"><i></i><i></i><i></i></span><span class="window-title"><i data-icon="users"></i> اعضای تیم</span></div>
              <div class="win-main" style="display:flex;flex-direction:column;gap:10px">
                <div class="flex gap-12"><span class="avatar">س</span><span style="flex:1"><b class="t-sm" style="display:block">سارا احمدی</b><span class="t-caption">سارا@abrino.ir</span></span><span class="badge badge-blue">مالک</span></div>
                <div class="flex gap-12"><span class="avatar" style="background:linear-gradient(135deg,#34D399,#065F46)">ع</span><span style="flex:1"><b class="t-sm" style="display:block">علی رضایی</b><span class="t-caption">علی@abrino.ir</span></span><span class="badge">توسعه‌دهنده</span></div>
                <div class="flex gap-12"><span class="avatar" style="background:linear-gradient(135deg,#A78BFA,#4C1D95)">م</span><span style="flex:1"><b class="t-sm" style="display:block">مریم کریمی</b><span class="t-caption">مریم@abrino.ir</span></span><span class="badge">بیننده</span></div>
              </div></div>'''
        elif visual == 'billing_visual':
            vis = '''<div class="window"><div class="window-bar"><span class="window-dots"><i></i><i></i><i></i></span><span class="window-title"><i data-icon="receipt"></i> فاکتور مرداد ۱۴۰۵</span></div>
              <div class="win-main">
                <div class="flex-between mb-16"><span class="t-caption">پلن رشد</span><b class="fa-num">۳٬۹۰۰٬۰۰۰ تومان</b></div>
                <div class="flex-between mb-16"><span class="t-caption">مازاد مصرف (۴۲ هزار درخواست)</span><b class="fa-num">۱۴۷٬۰۰۰ تومان</b></div>
                <div class="flex-between" style="border-top:1px solid var(--border);padding-top:12px"><b>جمع</b><b class="fa-num">۴٬۰۴۷٬۰۰۰ تومان</b></div>
              </div></div>'''
        else:
            vis = '''<div class="card card-pad"><div class="flex gap-12 mb-16"><span class="icon-tile icon-tile-green icon-tile-sm"><i data-icon="lock"></i></span><b>TLS 1.3</b></div>
              <div class="flex gap-12 mb-16"><span class="icon-tile icon-tile-blue icon-tile-sm"><i data-icon="shield"></i></span><b>AES-256</b></div>
              <div class="flex gap-12"><span class="icon-tile icon-tile-amber icon-tile-sm"><i data-icon="fingerprint"></i></span><b>2FA</b></div></div>'''
        rev = ' rev' if i % 2 else ''
        features_sec += f'''<div class="feature-row{rev}" id="{id}" data-reveal>
        <div class="f-body">
          <span class="sec-eyebrow">{'۰' + str(i+1)} · {title}</span>
          <h3 style="margin-bottom:14px">{title}</h3>
          <p>{desc}</p>
          <ul class="feature-list">{ptags}</ul>
          <a class="link mt-16" href="{p}docs/api-reference.html">مشاهده در مرجع API <i data-icon="arrow-left"></i></a>
        </div>
        <div>{vis}</div>
      </div>'''
    feat_head = '<div class="sec-head" data-reveal style="margin-bottom:8px"><h2>همه امکانات، با جزئیات</h2><p>هر قابلیت را با نمونه واقعی، امنیتی که پشت آن است و راهی که به داشبورد شما می‌رسد ببینید.</p></div>'
    return head(
        'امکانات | پلتفرم توسعه‌دهنده بلو ورتکس',
        'هر آنچه برای ساخت یک API حرفه‌ای نیاز دارید: امنیت سازمانی، احراز هویت، Webhook، تحلیل بلادرنگ، SDK بومی، تیم و صورتحساب شفاف.',
        prefix) + '''<body class="noise">
<main>
''' + navbar('active_products', p) + page_hero(
        crumb(p, 'امکانات'),
        'امکاناتی که یک پلتفرم توسعه‌دهنده<br><span class="grad-text">واقعی را می‌سازد</span>',
        'هر ویژگی بلو ورتکس برای یک نیاز واقعی تیم‌های محصول و API طراحی شده است — نه برای پر کردن صفحه.') + '''
<section class="section-sm">
  <div class="container">
    <div class="grid-auto chip-grid" style="margin-bottom:48px" data-reveal>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#api"><span class="icon-tile icon-tile-sm"><i data-icon="braces"></i></span><b>API</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#security"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="shield-check"></i></span><b>امنیت</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#auth"><span class="icon-tile icon-tile-sm icon-tile-amber"><i data-icon="key-round"></i></span><b>احراز هویت</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#webhooks"><span class="icon-tile icon-tile-sm icon-tile-violet"><i data-icon="webhook"></i></span><b>Webhooks</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#analytics"><span class="icon-tile icon-tile-sm icon-tile-cyan"><i data-icon="line-chart"></i></span><b>Analytics</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#monitoring"><span class="icon-tile icon-tile-sm icon-tile-red"><i data-icon="activity"></i></span><b>Monitoring</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#sdk"><span class="icon-tile icon-tile-sm"><i data-icon="package"></i></span><b>SDK</b></a>
      <a class="card card-pad card-hover" style="display:flex;align-items:center;gap:12px" href="#team"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="users"></i></span><b>تیم</b></a>
    </div>
    ''' + feat_head + features_sec + '''
  </div>
</section>

<section class="section" style="border-top:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>همه این امکانات، در دموی زنده</h2>
      <p>بهترین راه برای شناخت بلو ورتکس، دیدن آن است — وارد داشبورد نمونه شوید.</p>
      <div class="hero-cta"><a class="btn btn-primary btn-lg" href="../dashboard/index.html">باز کردن دموی داشبورد</a><a class="btn btn-outline btn-lg" href="../pages/pricing.html">مشاهده قیمت‌ها</a></div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p, prism=True, charts=True) + '</body></html>'

# ================================================================ SOLUTIONS
def build_solutions(prefix=''):
    p = prefix
    SOLS = [
        ('استارتاپ‌ها', 'rocket', 'blue', 'از ایده تا اولین کاربران، سریع و بدون زیرساخت‌بندی. مستندات حرفه‌ای محصول شما از روز اول آماده است و تیم شما روی محصول تمرکز می‌کند، نه ابزارها.', ['راه‌اندازی زیر ۵ دقیقه', 'پلن رایگان سخاوتمندانه', 'مستندات آماده برای جذب توسعه‌دهنده']),
        ('شرکت‌های سازمانی', 'building-2', 'green', 'SLA تضمینی، گزارش ممیزی، نقش‌های دقیق و پشتیبانی اختصاصی — همان چیزی که تیم‌های سازمانی در قرارداد خود می‌خواهند.', ['SLA ۹۹٫۹۹٪ با جریمه', 'SSO و احراز هویت سازمانی', 'قرارداد و فاکتور رسمی']),
        ('هوش مصنوعی', 'brain-circuit', 'violet', 'برای محصولات AI که با توکن سروکار دارند: مصرف توکن را دقیق اندازه بگیرید، سقف بگذارید و به کاربران گزارش شفاف بدهید.', ['سنجش مصرف توکن در لحظه', 'سهمیه‌بندی per-key و per-project', 'انکارپوینت‌های استریمی سازگار با SSE']),
        ('فین‌تک', 'credit-card', 'amber', 'امنیت در فین‌تک مذاکره‌پذیر نیست. کلیدهای Scoped، گزارش ممیزی کامل و رمزنگاری در حالت سکون، زیرساخت شما را آماده ممیزی می‌کند.', ['ممیزی کامل و گزارش حساس', 'کلیدهای مجزا برای هر سرویس', 'محیط آزمایش ایزوله و امن']),
        ('سلامت دیجیتال', 'heart-pulse', 'red', 'داده‌های حساس سلامت، حساس‌ترین داده‌ها هستند. کنترل دسترسی دقیق، لاگ کامل و رمزنگاری، آرامش خاطر تیم شما را تأمین می‌کند.', ['کنترل دسترسی سطح رکورد', 'لاگ کامل و غیرقابل‌تغییر', 'پشتیبانی از استانداردهای داده سلامت']),
        ('تجارت الکترونیک', 'shopping-bag', 'cyan', 'پیک‌های ترافیکی جشنواره‌ها را بدون دردسر مدیریت کنید: مقیاس خودکار، محدودیت نرخ هوشمند و گزارش بلادرنگ خطا.', ['مقیاس خودکار در پیک', 'Webhook برای سفارش و پرداخت', 'مونیتورینگ درگاه پرداخت']),
        ('تیم‌های توسعه نرم‌افزار', 'code-2', 'blue', 'یک پلتفرم برای همه تیم‌های داخلی: API مشترک با مستندات مشترک، منابع مشترک و دسترسی‌های مجزا برای هر محصول.', ['فضای کاری چند پروژه‌ای', 'نقش‌ها و دسترسی‌های داخلی', 'تغییرات مشترک (Changelog)']),
    ]
    cards = ''
    for i, (title, icon, color, desc, points) in enumerate(SOLS):
        pts = ''.join(f'<span class="badge">{x}</span>' for x in points)
        cards += f'''<div class="solution-card" data-reveal>
        <span class="sol-num fa-num">{i+1:02d}</span>
        <span class="icon-tile icon-tile-{color}"><i data-icon="{icon}"></i></span>
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="solution-tags">{pts}</div>
      </div>'''
    return head(
        'راهکارها | بلو ورتکس برای هر نوع کسب‌وکار',
        'راهکارهای بلو ورتکس برای استارتاپ‌ها، سازمان‌ها، فین‌تک، هوش مصنوعی، سلامت دیجیتال، تجارت الکترونیک و تیم‌های توسعه.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_products', p) + page_hero(
        crumb(p, 'راهکارها'),
        'برای هر کسب‌وکاری،<br><span class="grad-text">مسیری که می‌شناسد</span>',
        'بلو ورتکس فقط یک ابزار نیست؛ الگویی است که با نیازهای واقعی تیم‌های ایرانی تنظیم شده است.') + '''
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal><h2>راهکارها به تفکیک نیاز</h2><p>از استارتاپ تازه‌تأسیس تا سازمان چندصد نفره — بلو ورتکس برای هر وضعیتی آماده است.</p></div>
    <div class="grid-2" style="gap:20px">''' + cards + '''</div>
  </div>
</section>

<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="grid-4">
      <div class="stat"><span class="stat-label">کاهش زمان عرضه مستندات</span><b class="stat-value fa-num">×۸</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> میانگین مشتریان</span></div>
      <div class="stat"><span class="stat-label">کاهش تیکت پشتیبانی فنی</span><b class="stat-value fa-num">۴۰٪</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> در ۳ ماه نخست</span></div>
      <div class="stat"><span class="stat-label">زمان تشخیص خطا</span><b class="stat-value fa-num">۳ دقیقه</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> با هشدارهای زنده</span></div>
      <div class="stat"><span class="stat-label">رضایت توسعه‌دهندگان</span><b class="stat-value fa-num">۹۲٪</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> نظرسنجی ۱۴۰۵</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>راهکار شما را با هم بسازیم</h2>
      <p>اگر سناریوی خاصی در ذهن دارید، با تیم ما صحبت کنید — پاسخ‌گویی فارسی و مشاوره رایگان است.</p>
      <div class="hero-cta"><a class="btn btn-primary btn-lg" href="contact.html">درخواست مشاوره</a><a class="btn btn-outline btn-lg" href="pricing.html">دیدن پلن‌ها</a></div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '</body></html>'

# ================================================================ PRICING
def build_pricing(prefix=''):
    p = prefix
    features_list = [
        ('درخواست در ماه (هزار)', '۱۰', '۵۰۰', '۵٬۰۰۰', 'سفارشی', False, True),
        ('کلید API', '۲', 'نامحدود', 'نامحدود', 'نامحدود', False, True),
        ('اعضای تیم', '۱', '۵', 'نامحدود', 'نامحدود', False, True),
        ('گزارش درخواست‌ها', '۷ روز', '۳۰ روز', '۹۰ روز', '۹۰ روز + آرشیو', False, True),
        ('Webhook امضاشده', False, True, True, True, True, True),
        ('نقش‌های تیمی', False, 'پایه', 'کامل + سفارشی', 'کامل + SSO', True, True),
        ('گزارش ممیزی', False, False, True, True, True, True),
        ('SLA تضمینی', False, False, '۹۹٫۹٪', '۹۹٫۹۹٪', True, True),
        ('پشتیبانی', 'انجمن', '۲۴/۷ تیمی', 'اختصاصی', 'مهندس همراه', True, True),
        ('احراز هویت سازمانی (SSO)', False, False, False, True, True, True),
    ]
    rows = ''
    for row in features_list:
        name, vals = row[0], row[1:5]
        cells = ''
        for v in vals:
            if isinstance(v, bool):
                cells += ('<td><span class="yes"><i data-icon="check"></i></span></td>' if v else '<td><span class="no"><i data-icon="minus"></i></span></td>')
            else:
                cells += f'<td>{v}</td>'
        rows += f'<tr><td>{name}</td>{cells}</tr>'
    plan_cards = '''
    <div class="price-card" data-reveal>
      <span class="price-name"><i data-icon="rocket"></i>رایگان</span>
      <div class="price-amount"><b data-monthly="0" data-annual="0">۰ تومان</b><span class="price-period">ماهانه</span></div>
      <p class="price-desc">برای شروع سریع و پروژه‌های شخصی</p>
      <ul class="price-feats">
        <li><i data-icon="check"></i>۱۰ هزار درخواست در ماه</li>
        <li><i data-icon="check"></i>۲ کلید API</li>
        <li><i data-icon="check"></i>۱ عضو تیم</li>
        <li><i data-icon="check"></i>مستندات و مرجع API کامل</li>
        <li><i data-icon="check"></i>گزارش درخواست ۷ روزه</li>
        <li class="muted"><i data-icon="x"></i>Webhook امضاشده</li>
        <li class="muted"><i data-icon="x"></i>نقش‌های تیمی</li>
      </ul>
      <a class="btn btn-outline btn-block" href="../auth/register.html">شروع رایگان</a>
    </div>
    <div class="price-card popular" data-reveal>
      <span class="popular-tag">محبوب‌ترین</span>
      <span class="price-name"><i data-icon="zap"></i>توسعه‌دهنده</span>
      <div class="price-amount"><b data-monthly="990000" data-annual="792000">۹۹۰٬۰۰۰ تومان</b><span class="price-period">ماهانه</span></div>
      <p class="price-desc">برای تیم‌های در حال رشد</p>
      <ul class="price-feats">
        <li><i data-icon="check"></i>۵۰۰ هزار درخواست در ماه</li>
        <li><i data-icon="check"></i>کلید نامحدود</li>
        <li><i data-icon="check"></i>تا ۵ عضو تیم</li>
        <li><i data-icon="check"></i>گزارش درخواست ۳۰ روزه</li>
        <li><i data-icon="check"></i>Webhook امضاشده</li>
        <li><i data-icon="check"></i>پشتیبانی ۲۴/۷ تیمی</li>
        <li class="muted"><i data-icon="x"></i>گزارش ممیزی</li>
      </ul>
      <a class="btn btn-primary btn-block" href="../auth/register.html">شروع ۱۴ روز رایگان</a>
    </div>
    <div class="price-card" data-reveal>
      <span class="price-name"><i data-icon="building-2"></i>رشد</span>
      <div class="price-amount"><b data-monthly="3900000" data-annual="3120000">۳٬۹۰۰٬۰۰۰ تومان</b><span class="price-period">ماهانه</span></div>
      <p class="price-desc">برای شرکت‌ها و محصولات پرترافیک</p>
      <ul class="price-feats">
        <li><i data-icon="check"></i>۵ میلیون درخواست در ماه</li>
        <li><i data-icon="check"></i>فضای کاری چندگانه</li>
        <li><i data-icon="check"></i>تیم نامحدود + نقش‌ها</li>
        <li><i data-icon="check"></i>گزارش ممیزی کامل</li>
        <li><i data-icon="check"></i>SLA ۹۹٫۹٪</li>
        <li><i data-icon="check"></i>پشتیبانی اختصاصی</li>
        <li class="muted"><i data-icon="x"></i>SSO سازمانی</li>
      </ul>
      <a class="btn btn-outline btn-block" href="../auth/register.html">انتخاب پلن رشد</a>
    </div>
    <div class="price-card" data-reveal>
      <span class="price-name"><i data-icon="briefcase"></i>سازمانی</span>
      <div class="price-amount"><b>توافقی</b><span>بر اساس نیاز</span></div>
      <p class="price-desc">برای زیرساخت‌های حیاتی و قراردادهای بلندمدت</p>
      <ul class="price-feats">
        <li><i data-icon="check"></i>درخواست نامحدود (منصفانه)</li>
        <li><i data-icon="check"></i>SLA ۹۹٫۹۹٪ با جریمه</li>
        <li><i data-icon="check"></i>SSO و احراز هویت سازمانی</li>
        <li><i data-icon="check"></i>مهندس همراه اختصاصی</li>
        <li><i data-icon="check"></i>قرارداد و فاکتور رسمی</li>
        <li><i data-icon="check"></i>استقرار روی زیرساخت شما</li>
        <li><i data-icon="check"></i>آموزش تیم</li>
      </ul>
      <a class="btn btn-secondary btn-block" href="contact.html">گفتگو با فروش</a>
    </div>'''
    return head(
        'قیمت‌گذاری | پلن‌های بلو ورتکس به تومان',
        'پلن‌های شفاف بلو ورتکس به تومان: رایگان، توسعه‌دهنده، رشد و سازمانی. بدون هزینه پنهان، با پرداخت ریالی.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_products', p) + page_hero(
        crumb(p, 'قیمت‌گذاری'),
        'قیمت‌گذاری که <span class="grad-text">با رشد شما رشد می‌کند</span>',
        'همه پلن‌ها شامل مستندات کامل، داشبورد فارسی و مرجع تعاملی API هستند. پرداخت ریالی، فاکتور رسمی و بدون هزینه پنهان.') + '''
<section class="section-sm">
  <div class="container" style="max-width:1060px">
    <div class="billing-toggle" data-reveal>
      <div class="segmented" data-billing>
        <button class="active" data-billing="monthly">ماهانه</button>
        <button data-billing="annual">سالانه</button>
      </div>
      <span class="save-tag">۲۰٪ تخفیف سالانه</span>
    </div>
    <div style="position:relative">
      <div class="pricing-grid">''' + plan_cards + '''</div>
    </div>
    <p class="text-center t-caption mt-24" data-reveal>مبالغ به تومان و بدون مالیات است. <a class="link" href="contact.html" style="font-size:inherit">قیمت‌گذاری سازمانی</a> بر اساس حجم و توافق.</p>
  </div>
</section>

<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="sec-head" data-reveal><h2>مقایسه کامل امکانات</h2><p>هر ردیف را با نیاز واقعی تیم خود مقایسه کنید.</p></div>
    <div class="compare-wrap" data-reveal>
      <table>
        <caption class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden">مقایسه پلن‌ها</caption>
        <thead><tr><th>امکانات</th><th>رایگان</th><th class="pop-col">توسعه‌دهنده</th><th>رشد</th><th>سازمانی</th></tr></thead>
        <tbody>''' + rows + '''</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:860px">
    <div class="sec-head" data-reveal><h2>سوالات متداول قیمت‌گذاری</h2></div>
    <div data-reveal>
      <div class="accordion open" data-acc><button class="acc-head">اگر از سقف درخواست عبور کنم چه می‌شود؟<i data-icon="chevron-down"></i></button><div class="acc-body" style="max-height:200px"><div class="acc-inner">درخواست‌های مازاد متوقف نمی‌شوند؛ به‌صورت خودکار با تعرفه مصرف‌به‌مصرف (Per-use) محاسبه می‌شوند و پیش از عبور، با ایمیل و اعلان داشبورد مطلع می‌شوید. در پلن رایگان، رسیدن به سقف به معنی توقف تا ماه بعد است.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">تخفیف سالانه چطور محاسبه می‌شود؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">با انتخاب دوره سالانه، ۲۰٪ تخفیف روی مبلغ پایه اعمال می‌شود؛ مثلاً پلن توسعه‌دهنده از ۹۹۰٬۰۰۰ به ۷۹۲٬۰۰۰ تومان در ماه می‌رسد. مبلغ به‌صورت سالانه کسر می‌شود.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">آیا می‌توانم پلن را در وسط دوره عوض کنم؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">بله؛ ارتقا فوری اعمال می‌شود و مابه‌التفاوت روزشمار محاسبه می‌گردد. کاهش پلن از ابتدای دوره بعدی اعمال خواهد شد.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">روش‌های پرداخت چیست؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">پرداخت ریالی از طریق درگاه‌های داخلی و کارت‌های شتاب. فاکتور رسمی برای شرکت‌ها صادر می‌شود و امکان پرداخت از طریق حساب بانکی شرکت نیز وجود دارد.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">در پلن رایگان چه محدودیتی وجود دارد؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">۱۰ هزار درخواست ماهانه، ۲ کلید API، ۱ عضو تیم و گزارش ۷ روزه. مستندات و مرجع API بدون محدودیت در دسترس است.</div></div></div>
    </div>
  </div>
</section>

<section class="section" style="border-top:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>به یک پلن سازمانی اختصاصی فکر می‌کنید؟</h2>
      <p>تیم فروش بلو استودیو در کمتر از ۲۴ ساعت با شما تماس می‌گیرد؛ مشاوره فنی رایگان است.</p>
      <div class="hero-cta"><a class="btn btn-primary btn-lg" href="contact.html">درخواست مشاوره سازمانی</a></div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '</body></html>'

# ================================================================ CUSTOMERS
def build_customers(prefix=''):
    p = prefix
    stories = [
        dict(name='ابرینو', icon='cloud', tag='اتوماسیون ابری',
             quote='قبل از بلو ورتکس، مستندات API ما یک PDF قدیمی بود. حالا مرجع API زنده داریم و تیکت‌های فنی ۴۰٪ کم شده.',
             author='سارا احمدی', role='مدیر فنی', avatar='س',
             metrics=[('۶ هفته', 'زمان راه‌اندازی'), ('×۲', 'رشد ترافیک'), ('۴۰٪', 'کاهش تیکت فنی')]),
        dict(name='هوشیار', icon='brain-circuit', tag='هوش مصنوعی',
             quote='مصرف توکن‌ها را دقیق می‌بینیم و سهمیه‌بندی per-key داریم. کاربران سازمانی ما عاشق گزارش شفافند.',
             author='علی رضایی', role='بنیان‌گذار', avatar='ع',
             metrics=[('۱۲ ماه', 'سابقه همکاری'), ('۹۹٫۹۸٪', 'آپ‌تایم'), ('×۳', 'مشتریان سازمانی')]),
        dict(name='داده‌پرداز', icon='database', tag='زیرساخت داده',
             quote='مونیتورینگ بلادرنگ به ما گفت کدام Endpoint کند شده، قبل از این‌که مشتری بگوید.',
             author='مریم کریمی', role='مدیر محصول', avatar='م',
             metrics=[('۲۰ نفر', 'تیم توسعه'), ('۳ دقیقه', 'زمان تشخیص خطا'), ('۲۴/۷', 'پایش زنده')]),
        dict(name='فراز', icon='layers', tag='تجارت الکترونیک',
             quote='پیک جشنواره با ۱۱ برابر ترافیک را بدون یک خطای ۵xx رد کردیم. مقیاس خودکار بلو ورتکس واقعاً کار می‌کند.',
             author='رضا موسوی', role='مدیر فنی', avatar='ر',
             metrics=[('۱۱×', 'ترافیک پیک'), ('۰', 'خطای ۵xx'), ('۱٬۲۰۰', 'درخواست در ثانیه')]),
    ]
    cards = ''
    for s in stories:
        metrics = ''.join(
            f'<div class="story-metric"><b class="fa-num">{v}</b><span>{lbl}</span></div>' for v, lbl in s['metrics'])
        cards += f'''<div class="story-card" data-reveal>
      <div class="story-top">
        <span class="story-logo"><i data-icon="{s['icon']}"></i>{s['name']}<span class="badge" style="margin-inline-start:8px">{s['tag']}</span></span>
        <div class="story-metrics">{metrics}</div>
      </div>
      <div class="story-body">
        <blockquote>{s['quote']}</blockquote>
        <div class="story-author"><span class="avatar">{s['avatar']}</span><span><b>{s['author']}</b><span>{s['role']} · {s['name']} (شرکت نمونه)</span></span></div>
      </div>
    </div>'''
    return head(
        'مشتریان | داستان موفقیت با بلو ورتکس',
        'داستان شرکت‌های نمونه (دمو) که با بلو ورتکس API خود را حرفه‌ای عرضه کردند؛ نتایج، نقل‌قول‌ها و کاربردهای واقعی.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_products', p) + page_hero(
        crumb(p, 'مشتریان'),
        'داستان‌هایی که <span class="grad-text">با اعداد روایت می‌شوند</span>',
        'همه شرکت‌های این صفحه نمونه (Demo) هستند و برای نمایش سناریوهای واقعی استفاده از محصول ساخته شده‌اند.') + '''
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal><h2>راهکارها به تفکیک نیاز</h2><p>از استارتاپ تازه‌تأسیس تا سازمان چندصد نفره — بلو ورتکس برای هر وضعیتی آماده است.</p></div>
    <div class="grid-2" style="gap:20px">''' + cards + '''</div>
  </div>
</section>

<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="sec-head" data-reveal><h2>نتایج در یک نگاه</h2><p>میانگین نتایج گزارش‌شده توسط مشتریان نمونه.</p></div>
    <div class="grid-4">
      <div class="stat"><span class="stat-label">کاهش تیکت فنی</span><b class="stat-value fa-num">۴۰٪</b></div>
      <div class="stat"><span class="stat-label">سرعت عرضه مستندات</span><b class="stat-value fa-num">۸×</b></div>
      <div class="stat"><span class="stat-label">زمان تشخیص خطا</span><b class="stat-value fa-num">۳ دقیقه</b></div>
      <div class="stat"><span class="stat-label">رضایت توسعه‌دهنده</span><b class="stat-value fa-num">۹۲٪</b></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal><h2>استفاده‌های واقعی</h2><p>سناریوهایی که مشتریان نمونه با بلو ورتکس پیاده کرده‌اند.</p></div>
    <div class="grid-auto">
      <div class="card card-pad card-hover" data-reveal><span class="icon-tile icon-tile-sm icon-tile-green mb-16"><i data-icon="book-open"></i></span><h3 class="t-h4 mb-8">پورتال عمومی API</h3><p class="t-sm" style="color:var(--text-3)">ابرینو برای ۴۰ شریک خارجی خود پورتال API با مستندات زنده و کلید خودسرویس راه‌اندازی کرد.</p></div>
      <div class="card card-pad card-hover" data-reveal><span class="icon-tile icon-tile-sm icon-tile-amber mb-16"><i data-icon="cpu"></i></span><h3 class="t-h4 mb-8">سهمیه‌بندی مدل AI</h3><p class="t-sm" style="color:var(--text-3)">هوشیار مصرف توکن هر مشتری سازمانی را جداگانه اندازه‌گیری و هزینه می‌کند.</p></div>
      <div class="card card-pad card-hover" data-reveal><span class="icon-tile icon-tile-sm icon-tile-blue mb-16"><i data-icon="line-chart"></i></span><h3 class="t-h4 mb-8">مونیتورینگ درگاه</h3><p class="t-sm" style="color:var(--text-3)">فراز سلامت درگاه پرداخت را بلادرنگ پایش و هشدار را به تلگرام تیم فنی می‌فرستد.</p></div>
      <div class="card card-pad card-hover" data-reveal><span class="icon-tile icon-tile-sm icon-tile-violet mb-16"><i data-icon="shield"></i></span><h3 class="t-h4 mb-8">ممیزی سازمانی</h3><p class="t-sm" style="color:var(--text-3)">داده‌پرداز گزارش ممیزی کامل هر تغییر را برای بازرسان امنیتی تولید می‌کند.</p></div>
    </div>
  </div>
</section>

<section class="section" style="border-top:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>داستان بعدی، داستان تیم شماست</h2>
      <div class="hero-cta"><a class="btn btn-primary btn-lg" href="../auth/register.html">شروع رایگان</a><a class="btn btn-outline btn-lg" href="contact.html">گفتگو با ما</a></div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '</body></html>'

# ================================================================ ABOUT
def build_about(prefix=''):
    p = prefix
    team = [
        ('سارا احمدی', 'بنیان‌گذار و مدیر عامل', 'پیش‌تر مدیر محصول در یک استارتاپ فین‌تک؛ باور دارد محصول فارسی هم می‌تواند جهانی باشد.'),
        ('علی رضایی', 'هم‌بنیان‌گذار و CTO', 'معمار زیرساخت؛ ۱۲ سال تجربه در سیستم‌های توزیع‌شده و علاقه‌مند به سیستم‌های فارسی‌اول.'),
        ('مریم کریمی', 'مدیر طراحی محصول', 'طراحی رابط کاربری برای محصولات فنی؛ از اصول «فناوری آرام» به‌عنوان مرجع کارش استفاده می‌کند.'),
        ('رضا موسوی', 'مهندس ارشد پلتفرم', 'متخصص Go و Rust؛ مسئول عملکرد و مقیاس‌پذیری هسته API.'),
        ('نگار شریفی', 'مدیر مستندات', 'نویسنده فنی؛ باور دارد مستندات خوب، نصف پشتیبانی است.'),
        ('امیر توکلی', 'مهندس SDK', 'سازنده SDKهای پایتون و PHP؛ عاشق تایپ‌های سخت‌گیرانه.'),
        ('لیلا نادری', 'مدیر موفقیت مشتری', '۱۶ سال تجربه؛ پل میان نیاز مشتریان و نقشه راه محصول.'),
        ('حسین کاظمی', 'مهندس امنیت', 'متخصص امنیت API و ممیزی؛ هر خط کد را با چشم مهاجم می‌خواند.'),
    ]
    team_cards = ''
    for name, role, bio in team:
        team_cards += f'''<div class="team-card" data-reveal><span class="avatar">{name[0]}</span><b>{name}</b><span>{role}</span><p>{bio}</p></div>'''
    timeline = [
        ('تیر ۱۴۰۲', 'نقطه شروع', 'بلو استودیو با یک سؤال ساده شکل گرفت: چرا هیچ پلتفرم توسعه‌دهنده‌ای برای بازار فارسی وجود ندارد؟'),
        ('آبان ۱۴۰۲', 'نسخه ۰٫۱', 'مفهوم اولیه بلو ورتکس؛ مستندات زنده و مرجع API. اولین ۱۰ توسعه‌دهنده آزمایشی به ما پیوستند.'),
        ('خرداد ۱۴۰۳', 'نسخه ۱٫۰', 'انتشار عمومی؛ داشبورد توسعه‌دهنده، کلیدهای API و اولین پلن پولی.'),
        ('بهمن ۱۴۰۳', 'نسخه ۱٫۵', 'گزارش درخواست‌ها و تحلیل بلادرنگ؛ ۵۰۰ تیم فعال.'),
        ('مهر ۱۴۰۴', 'نسخه ۲٫۰', 'بازطراحی کامل رابط کاربری، Webhook امضاشده و نقش‌های تیمی.'),
        ('مرداد ۱۴۰۵', 'نسخه ۲٫۴', 'SDK پایتون با تایپ کامل، ۳٬۰۰۰+ تیم فعال و راه‌اندازی صفحه وضعیت عمومی.'),
    ]
    tl = ''
    for date, title, desc in timeline:
        tl += f'''<div class="tl-item"><span class="tl-date">{date}</span><h3 class="tl-title">{title}</h3><div class="tl-desc">{desc}</div></div>'''
    return head(
        'درباره ما | بلو استودیو و بلو ورتکس',
        'داستان بلو استودیو، مأموریت ما در ساخت پلتفرم توسعه‌دهنده فارسی، ارزش‌ها، تیم و فلسفه فنی بلو ورتکس.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_products', p) + page_hero(
        crumb(p, 'درباره ما'),
        'ما بلو استودیو هستیم؛<br><span class="grad-text">سازندگان بلو ورتکس</span>',
        'تیمی از مهندسان و طراحان ایرانی که باور دارند بازار فارسی سزاوار زیرساخت‌های در سطح جهانی است.') + '''
<section class="section">
  <div class="container">
    <div class="grid-2" style="gap:56px;align-items:center">
      <div data-reveal>
        <span class="sec-eyebrow">داستان ما</span>
        <h2 class="t-h2" style="margin-bottom:16px">از یک سؤال ساده شروع شد</h2>
        <p class="t-body-lg" style="color:var(--text-2);line-height:2.1">«چرا باید برای داشتن مستندات API خوب، ابزارهای خارجی را ترجمه کنیم؟» این سؤال، تیم ما را کنار هم گذاشت. ما دیدیم که تیم‌های ایرانی محصولات عالی می‌سازند، اما زیرساخت توسعه‌دهنده‌شان همیشه یک ترجمه یا یک قالب آماده است — نه چیزی که برای زبان و فرهنگ فارسی طراحی شده باشد.</p>
        <p class="t-body-lg" style="color:var(--text-2);line-height:2.1;margin-top:16px">بلو ورتکس پاسخ ماست: یک پلتفرم فارسی‌اول که در آن هر تایپوگرافی، هر تاریخ شمسی، هر نمونه‌کد و هر Empty State با دقت طراحی شده است.</p>
      </div>
      <div class="card card-pad" data-reveal>
        <div class="flex gap-16 mb-24"><span class="icon-tile"><i data-icon="target"></i></span><div><h3 class="t-h4">مأموریت ما</h3><p class="t-sm" style="color:var(--text-3);margin-top:6px">قدرت‌مند کردن هر تیم ایرانی برای عرضه محصولات API در سطح جهانی، به زبان خودشان.</p></div></div>
        <div class="flex gap-16 mb-24"><span class="icon-tile icon-tile-green"><i data-icon="heart-handshake"></i></span><div><h3 class="t-h4">ارزش ما</h3><p class="t-sm" style="color:var(--text-3);margin-top:6px">اعتماد مهم‌تر از سرعت است. ما هر تصمیم طراحی را از دریچه اعتماد و سادگی می‌بینیم.</p></div></div>
        <div class="flex gap-16"><span class="icon-tile icon-tile-violet"><i data-icon="lightbulb"></i></span><div><h3 class="t-h4">فلسفه فنی</h3><p class="t-sm" style="color:var(--text-3);margin-top:6px">قدرتمند اما آرام (Calm Technology). فناوری خوب وقتی دیده می‌شود که کارش را بی‌صدا انجام دهد.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container" style="max-width:760px">
    <div class="sec-head" data-reveal><h2>مسیر ما تا امروز</h2></div>
    <div class="timeline" data-reveal>''' + tl + '''</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal><h2>تیم بلو استودیو</h2><p>مهندسان، طراحان و نویسندگانی که بلو ورتکس را می‌سازند (اعضای نمونه).</p></div>
    <div class="team-grid">''' + team_cards + '''</div>
  </div>
</section>

<section class="section" style="border-top:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="grid-2" style="gap:32px;align-items:center">
      <div data-reveal>
        <span class="sec-eyebrow">تکنولوژی</span>
        <h2 class="t-h2" style="margin-bottom:14px">فلسفه فنی ما</h2>
        <p class="t-body" style="color:var(--text-2);line-height:2.1">ما از تکنولوژی‌های اثبات‌شده استفاده می‌کنیم و از مد روزهای زودگذر فاصله می‌گیریم. هر پیکسل که در بلو ورتکس می‌بینید حاصل یک تصمیم آگاهانه است: RTL واقعی، نه آینه‌شدن؛ تایپوگرافی فارسی اصیل، نه ترجمه؛ و کارایی، نه تزئین.</p>
      </div>
      <div class="grid grid-2" style="gap:14px" data-reveal>
        <div class="card card-pad"><b class="t-h4 mb-8">RTL بومی</b><p class="t-caption">از پایه برای راست‌به‌چپ نوشته شده، نه تبدیل‌شده.</p></div>
        <div class="card card-pad"><b class="t-h4 mb-8">بدون وابستگی</b><p class="t-caption">قالب کاملاً آفلاین و بدون نیاز به اینترنت کار می‌کند.</p></div>
        <div class="card card-pad"><b class="t-h4 mb-8">عملکرد</b><p class="t-caption">کتابخانه‌های سبک و جاوااسکریپت بهینه.</p></div>
        <div class="card card-pad"><b class="t-h4 mb-8">استاندارد وب</b><p class="t-caption">HTML معنایی، ARIA و پشتیبانی از حرکات کم‌حجم.</p></div>
      </div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '</body></html>'
