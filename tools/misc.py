# -*- coding: utf-8 -*-
"""Blue Vertex — changelog + status pages"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts

def page_hero(breadcrumb, title, lead):
    return f'''<section class="page-hero">
  <div class="hero-bg bg-grid" aria-hidden="true"><div class="glow-1" style="top:-260px"></div></div>
  <div class="container" style="position:relative">
    <nav class="breadcrumb" aria-label="مسیر صفحه">{breadcrumb}</nav>
    <h1 data-reveal>{title}</h1>
    <p data-reveal>{lead}</p>
  </div>
</section>'''

# ================================================================ CHANGELOG
RELEASES = [
    dict(ver='2.4.1', date='۲۹ مرداد ۱۴۰۵', cat='fix', title='نسخه ۲٫۴٫۱', items=[
        ('fix', 'رفع باگ نمایش تأخیر در نمودار صدک‌ها هنگام انتخاب بازه ۹۰ روزه'),
        ('fix', 'اصلاح نمایش اعداد فارسی در فاکتورهای دانلودی PDF'),
        ('imp', 'بهبود سرعت بارگذاری صفحه وضعیت سرویس'),
    ]),
    dict(ver='2.4.0', date='۲۰ مرداد ۱۴۰۵', cat='feat', title='نسخه ۲٫۴٫۰', major=True, items=[
        ('feat', 'SDK پایتون با تایپ کامل (PEP 561) و مستندات inline'),
        ('feat', 'دسته‌بندی گزارش درخواست‌ها بر اساس پروژه'),
        ('imp', 'بازطراحی کامل صفحه تحلیل‌ها با فیلتر تاریخ شمسی'),
        ('sec', 'افزودن هدر امنیتی <code class="inline">x-bv-signature</code> به Webhookها'),
    ]),
    dict(ver='2.3.1', date='۸ مرداد ۱۴۰۵', cat='fix', title='نسخه ۲٫۳٫۱', items=[
        ('fix', 'رفع خطای نادر ۴۰۴ در جستجوی مستندات با عبارات فارسی'),
        ('imp', 'کاهش ۱۸٪ حجم جاوااسکریپت بارگذاری‌شده'),
    ]),
    dict(ver='2.3.0', date='۲۸ تیر ۱۴۰۵', cat='feat', title='نسخه ۲٫۳٫۰', major=True, items=[
        ('feat', 'مرورگر تعاملی API (API Explorer) در داشبورد'),
        ('feat', 'فیلتر گزارش درخواست‌ها بر اساس کد وضعیت و محیط'),
        ('imp', 'جستجوی مستندات با نمایش جستجوهای اخیر'),
        ('imp', 'پشتیبانی کامل از نمایش اعداد فارسی در نمودارها'),
    ]),
    dict(ver='2.2.0', date='۱۰ تیر ۱۴۰۵', cat='feat', title='نسخه ۲٫۲٫۰', major=True, items=[
        ('feat', 'نقش‌های تیمی سفارشی با دسترسی‌های ریزدانه'),
        ('feat', 'گزارش ممیزی (Audit Log) برای همه تغییرات حساس'),
        ('sec', 'ورود دومرحله‌ای TOTP برای همه پلن‌ها'),
        ('fix', 'رفع مشکل همپوشانی منوها در صفحه‌های باریک'),
    ]),
    dict(ver='2.1.4', date='۲۶ خرداد ۱۴۰۵', cat='fix', title='نسخه ۲٫۱٫۴', items=[
        ('fix', 'اصلاح محاسبه اشتراک زمانی صورتحساب در ارتقای میاندوره'),
        ('imp', 'افزایش سرعت ساخت کلید API در داشبورد'),
    ]),
]

def build_changelog(prefix=''):
    p = prefix
    cards = ''
    icon_map = {'feat': ('sparkles', 'ویژگی جدید', 'feat', 'badge-blue'), 'fix': ('bug', 'رفع باگ', 'fix', 'badge-amber'),
                'imp': ('trending-up', 'بهبود', 'imp', 'badge'), 'sec': ('shield-check', 'امنیت', 'sec', 'badge-red')}
    for r in RELEASES:
        items = ''
        for cat, text in r['items']:
            ic, label, cls, badge = icon_map[cat]
            items += f'<li class="{cls}"><i data-icon="{ic}"></i><span>{text}</span></li>'
        major = ' major' if r.get('major') else ''
        clarr = 'tl-item major' if r.get('major') else 'tl-item'
        cards += f'''<div class="changelog-card" data-rel="{r['cat']}" data-reveal>
      <div class="cl-head">
        <span class="ver-chip">{r['ver']}</span>
        <span class="cl-date fa-num">{r['date']}</span>
        <span class="tl-title" style="margin:0;font-size:var(--fs-body)">{r['title']}</span>
      </div>
      <div class="cl-tags">
        <span class="badge {icon_map[r['cat']][3]}">{icon_map[r['cat']][1]}</span>
      </div>
      <ul class="cl-list">{items}</ul>
    </div>'''
    return head(
        'تغییرات | بلو ورتکس',
        'تاریخچه نسخه‌های بلو ورتکس: ویژگی‌های جدید، بهبودها، رفع باگ‌ها و تغییرات امنیتی با تاریخ شمسی.',
        prefix) + f'''<body class="noise"><main>
''' + navbar('active_changelog', prefix) + page_hero(
        f'<a href="../index.html">خانه</a><span class="sep"><i data-icon="chevron-left"></i></span><span class="current">تغییرات</span>',
        'تغییرات <span class="grad-text">بلو ورتکس</span>',
        'هر نسخه، یک قدم به سمت زیرساخت توسعه‌دهنده‌ای بهتر. آخرین تغییرات را دنبال کنید — با تاریخ شمسی.') + '''
<section class="section-sm">
  <div class="container" style="max-width:860px">
    <div class="changelog-head">
      <div class="chip-group">
        <button class="chip active" data-cl-filter="all">همه</button>
        <button class="chip" data-cl-filter="feat">ویژگی جدید</button>
        <button class="chip" data-cl-filter="imp">بهبود</button>
        <button class="chip" data-cl-filter="fix">رفع باگ</button>
        <button class="chip" data-cl-filter="sec">امنیت</button>
      </div>
      <span class="t-caption fa-num">۶ نسخه · ۳ ماه اخیر</span>
    </div>
    <div class="timeline">''' + cards + '''</div>
    <div class="empty-state" style="display:none" id="clEmpty">
      <span class="es-icon"><i data-icon="inbox"></i></span>
      <h2>تغییری در این دسته نیست</h2>
      <p>فیلتر دیگری انتخاب کنید یا همه تغییرات را ببینید.</p>
    </div>
    <div class="text-center mt-32">
      <p class="t-caption">نسخه قدیمی‌تر می‌خواهید؟ <a class="link" href="#" style="font-size:inherit">آرشیو کامل تغییرات را ببینید</a></p>
    </div>
  </div>
</section>
</main>
''' + footer(prefix) + palette(p) + TOAST_REGION + scripts(prefix) + '''
<script>
(function(){
  document.querySelectorAll('[data-cl-filter]').forEach(function(chip){
    chip.addEventListener('click', function(){
      document.querySelectorAll('[data-cl-filter]').forEach(function(c){ c.classList.remove('active'); });
      chip.classList.add('active');
      var f = chip.getAttribute('data-cl-filter');
      var shown = 0;
      document.querySelectorAll('.changelog-card').forEach(function(card){
        var ok = f === 'all' || card.getAttribute('data-rel') === f || card.getAttribute('data-rel') === 'feat' && f === 'imp';
        card.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      var empty = document.getElementById('clEmpty');
      if (empty) empty.style.display = shown ? 'none' : 'flex';
      if (shown && window.BV) BV.toast('info', 'فیلتر اعمال شد', BV.faNum(shown) + ' نسخه نمایش داده می‌شود.');
    });
  });
})();
</script>
</body></html>'''

# ================================================================ STATUS
SYSTEMS = [
    ('API', 'braces', 'green', 'عملکرد عادی', '۹۹٫۹۸٪', '۱۲۴ms', '30d', 99.9),
    ('داشبورد', 'layout-dashboard', 'green', 'عملکرد عادی', '۱۰۰٪', '۴۸ms', '30d', 100),
    ('احراز هویت', 'shield-check', 'green', 'عملکرد عادی', '۹۹٫۹۹٪', '۳۶ms', '30d', 99.99),
    ('پایگاه داده', 'database', 'amber', 'اختلال جزئی', '۹۹٫۷۲٪', '۸ms', '30d', 99.7),
    ('Webhookها', 'webhook', 'green', 'عملکرد عادی', '۹۹٫۹۶٪', '۲۱۰ms', '30d', 99.9),
    ('مستندات', 'book-open', 'green', 'عملکرد عادی', '۱۰۰٪', '۲۸ms', '30d', 100),
]

def build_status(prefix=''):
    p = prefix
    sys_cards = ''
    for i_sys, (name, icon, color, status, uptime, lat, days, health) in enumerate(SYSTEMS):
        # deterministic 30-day uptime bar (amber blocks where incidents happened)
        bad_days = {1: [26, 27], 2: [], 3: [18], 4: [6, 7, 8, 25], 5: [], 6: []}
        blocks = []
        for d in range(30):
            blocks.append('amber' if d in bad_days.get(i_sys, []) else 'ok')
        bar = ''.join(
            f'<i class="{b}" style="flex:1;background:{ "#34D399" if b == "ok" else "#FBBF24"}" title="روز {d + 1}"></i>'
            for d, b in enumerate(blocks))
        st_cls = {'green': 'st-green', 'amber': 'st-amber'}[color]
        sys_cards += f'''<div class="sys-card" data-reveal>
      <div class="sys-head">
        <span class="sys-name"><span class="icon-tile icon-tile-sm icon-tile-{color}"><i data-icon="{icon}"></i></span>{name}</span>
        <span class="status-ind {st_cls}"><span class="pulse"></span>{status}</span>
      </div>
      <div class="uptime-bar" aria-label="آپ‌تایم ۳۰ روز اخیر">{bar}</div>
      <div class="flex-between">
        <span class="t-caption fa-num">آپ‌تایم ۳۰ روز: {uptime}</span>
        <span class="sys-latency"><i data-icon="timer"></i>میانگین: <b class="fa-num">{lat}</b></span>
      </div>
    </div>'''
    incidents = [
        dict(title='اختلال جزئی در پایگاه داده', direction='partial', date='۲۶ مرداد ۱۴۰۵', hours='۱۰:۴۵ — ۱۱:۲۰'),
        dict(title='افزایش تأخیر در تحویل Webhookها', direction='partial', date='۱۸ مرداد ۱۴۰۵', hours='۱۴:۰۲ — ۱۴:۳۵'),
        dict(title='خطای ۵xx پراکنده در API', direction='major', date='۶ تیر ۱۴۰۵', hours='۰۹:۱۲ — ۱۰:۰۴'),
        dict(title='برنامه‌ریزی نگهداری زیرساخت', direction='resolved', date='۲۹ خرداد ۱۴۰۵', hours='۰۲:۰۰ — ۰۲:۴۵'),
        dict(title='اختلال کوتاه سرویس احراز هویت', direction='partial', date='۲۰ خرداد ۱۴۰۵', hours='۱۷:۳۰ — ۱۷:۴۲'),
    ]
    inc_cards = ''
    for inc in incidents:
        inc_cards += f'''<div class="incident-card" data-reveal>
      <div class="incident-head">
        <span class="incident-title">{inc['title']} <span class="direction {inc['direction']}">{'اختلال عمده' if inc['direction'] == 'major' else 'اختلال جزئی' if inc['direction'] == 'partial' else 'برطرف‌شده'}</span></span>
        <span class="t-caption fa-num">{inc['date']}</span>
      </div>
      <div class="incident-timeline">
        <div class="inc-step"><span class="dot" style="background:var(--amber);border-color:var(--amber-line)"></span><div><b>شناسایی مشکل</b><span class="fa-num">{inc['hours']} — تیم عملیات مشکل را تأیید کرد</span></div></div>
        <div class="inc-step"><span class="dot" style="background:var(--amber);border-color:var(--amber-line)"></span><div><b>بررسی و راه‌حل موقت</b><span>بخش‌های آسیب‌دیده ایزوله شدند؛ هیچ داده‌ای از دست نرفت.</span></div></div>
        <div class="inc-step"><span class="dot" style="background:var(--green);border-color:var(--green-line)"></span><div><b>رفع کامل مشکل</b><span>همه سرویس‌ها به حالت عادی بازگشتند.</span></div></div>
      </div>
    </div>'''

    return head(
        'وضعیت سرویس | بلو ورتکس',
        'وضعیت لحظه‌ای سرویس‌های بلو ورتکس: API، داشبورد، احراز هویت، پایگاه داده، Webhook و مستندات — با تاریخچه حوادث.',
        prefix) + f'''<body class="noise">
''' + navbar('active_status', prefix) + '''
<section class="status-hero">
  <div class="hero-bg bg-grid" aria-hidden="true" style="position:absolute;inset:0;z-index:0"></div>
  <div class="container" style="position:relative;z-index:2">
    <nav class="breadcrumb" style="justify-content:center;margin-bottom:22px">
      <a href="../index.html">خانه</a><span class="sep"><i data-icon="chevron-left"></i></span><span class="current">وضعیت سرویس</span>
    </nav>
    <h1 data-reveal>وضعیت سرویس <span class="grad-text-blue">بلو ورتکس</span></h1>
    <div data-reveal>
      <div class="status-overall">
        <span class="status-ind st-green"><span class="pulse"></span> همه سرویس‌ها فعال</span>
        <span style="width:1px;height:18px;background:var(--border)"></span>
        <span class="t-caption fa-num">آپ‌تایم ۹۰ روز: ۹۹٫۹۸٪</span>
      </div>
    </div>
    <p class="t-caption" data-reveal>آخرین به‌روزرسانی: ۷ شهریور ۱۴۰۵ · ۱۲:۰۴ — وضعیت هر ۶۰ ثانیه بررسی می‌شود</p>
    <div class="status-grid">
      ''' + sys_cards + '''
    </div>
    <div class="uptime-legend mt-24" style="justify-content:center">
      <span><i style="background:#34D399"></i> عملکرد عادی</span>
      <span><i style="background:#FBBF24"></i> اختلال جزئی</span>
      <span><i style="background:#F87171"></i> اختلال عمده</span>
      <span class="fa-num">۳۰ روز اخیر · به تفکیک هر روز</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:960px">
    <div class="sec-head start" data-reveal><h2>تاریخچه حوادث</h2><p>شفافیت کامل: هر حادثه با گام‌های زمانی ثبت می‌شود.</p></div>
    <div>''' + inc_cards + '''</div>

    <div class="card card-pad mt-48" data-reveal style="display:flex;align-items:center;gap:18px;flex-wrap:wrap">
      <span class="icon-tile icon-tile-green"><i data-icon="bell-ring"></i></span>
      <div style="flex:1;min-width:220px">
        <h3 class="t-h4">اشتراک وضعیت</h3>
        <p class="t-caption mt-8">با تغییر وضعیت سرویس‌ها، ایمیل یا پیام تلگرام بگیرید.</p>
      </div>
      <input class="input" style="max-width:280px" type="email" placeholder="you@company.ir" aria-label="ایمیل برای اشتراک وضعیت">
      <button class="btn btn-primary" data-status-sub>اشتراک</button>
    </div>

    <div class="grid-3 mt-32" data-reveal>
      <div class="stat"><span class="stat-label">آپ‌تایم ۳۰ روزه</span><b class="stat-value fa-num">۹۹٫۹۸٪</b></div>
      <div class="stat"><span class="stat-label">میانگین پاسخ API</span><b class="stat-value fa-num">۱۲۴ms</b></div>
      <div class="stat"><span class="stat-label">حوادث ۳۰ روز</span><b class="stat-value fa-num">۱</b></div>
    </div>
  </div>
</section>
''' + footer(prefix) + palette(p) + TOAST_REGION + scripts(prefix) + '''
<script>
(function(){
  document.querySelectorAll('[data-status-sub]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var input = btn.parentNode.querySelector('input');
      if (!input || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(input.value)) {
        if (window.BV) BV.toast('error', 'ایمیل معتبر نیست', 'لطفاً ایمیل صحیح وارد کنید.');
        return;
      }
      btn.classList.add('btn-loading');
      setTimeout(function(){
        btn.classList.remove('btn-loading');
        btn.textContent = 'عضو شدید';
        if (window.BV) BV.toast('success', 'اشتراک فعال شد', 'تغییرات وضعیت سرویس به ایمیل شما اطلاع داده می‌شود.');
      }, 900);
    });
  });
})();
</script>
</body></html>'''

def fa_title(i):
    return str(i + 1)
