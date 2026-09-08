# -*- coding: utf-8 -*-
"""Blue Vertex — Developer Console pages, part 2"""

from dash import dash_page, daterange, drawer_log

# ================================================================ API KEYS
def build_api_keys(prefix=''):
    keys = [
        ('کلید تولید — اصلی', 'bv_live_9f2k1x7aQw4eRt8zM3vB6n', 'production', 'active', '۸ شهریور ۱۴۰۵', 'همین حالا', ['users.read', 'users.write', 'payments.read'], 'همه'),
        ('کلید وب‌سایت', 'bv_live_4dP7sK2mN8cQ1wE5tR9yU', 'production', 'active', '۲ مرداد ۱۴۰۵', '۵ دقیقه پیش', ['users.read', 'files.write'], 'همه'),
        ('کلید توسعه — محلی', 'bv_test_7hJ3vB6nM2kL9xQ4wE8rT', 'test', 'active', '۲۹ تیر ۱۴۰۵', 'دیروز', ['users.read'], 'همه'),
        ('کلید CI/CD (قدیمی)', 'bv_live_2zX8cV5bN1mK7jH4gF6dS', 'production', 'revoked', '۲۰ خرداد ۱۴۰۵', '۱۲ مرداد ۱۴۰۵', ['users.read'], 'همه'),
    ]
    rows = ''
    for name, full, env, status, created, last, scopes, _ in keys:
        sc = ''.join(f'<span class="badge badge-blue">{s}</span>' for s in scopes[:2])
        st_badge = '<span class="badge badge-green"><span class="dot"></span> فعال</span>' if status == 'active' else '<span class="badge"><i data-icon="x"></i> باطل‌شده</span>'
        env_badge = '<span class="badge badge-amber">تولید</span>' if env == 'production' else '<span class="badge badge-cyan">آزمایش</span>'
        rows += f'''<div class="key-row" data-key-row data-key-name="{name}" data-key-full="{full}" data-status="{status}" data-env="{env}">
      <div class="key-name-block" style="flex:1;min-width:230px">
        <span class="key-name"><i data-icon="key-round"></i>{name}</span>
        <span class="key-created">ساخته‌شده: <span class="fa-num">{created}</span> · آخرین استفاده: <span class="fa-num">{last}</span> · {env_badge}</span>
      </div>
      <div class="key-value">
        <code data-masked="1">{full[:7]}•••••••••••••••</code>
        <span class="kv-actions">
          <button class="kv-btn key-reveal-btn" title="نمایش" aria-label="نمایش کلید"><i data-icon="eye"></i></button>
          <button class="kv-btn" data-copy="{full}" title="کپی" aria-label="کپی کلید"><i data-icon="copy"></i></button>
          <button class="kv-btn" data-rename-key title="تغییر نام" aria-label="تغییر نام"><i data-icon="pencil"></i></button>
          <button class="kv-btn" data-revoke-key title="باطل کردن" aria-label="باطل کردن" {'style="color:var(--red)"' if status == 'active' else 'style="color:var(--text-4)"'}><i data-icon="trash-2"></i></button>
        </span>
      </div>
      <span style="display:flex;gap:6px;flex-wrap:wrap;max-width:280px">{sc} {st_badge}</span>
    </div>'''
    content = f'''
    <div class="security-note">
      <i data-icon="shield-alert"></i>
      <span><b>کلیدهای API مانند رمز عبور شما هستند.</b> هرگز آن‌ها را در کد کلاینت، مخزن عمومی یا چت گروهی قرار ندهید. برای امنیت بیشتر، هر محیط یک کلید مجزا داشته باشد و کلیدهایی که دیگر استفاده نمی‌شوند را فوراً باطل کنید.</span>
    </div>

    <div class="card" style="overflow:hidden;margin-bottom:20px" id="keysTable">
      <div class="card-head">
        <div><h2>کلیدهای API</h2><p class="t-caption" style="margin-top:4px">کلیدهای فضای کاری ابرینو — <b data-key-count class="fa-num">۴</b> کلید</p></div>
        <div style="display:flex;gap:8px">
          <button class="btn btn-ghost btn-sm" id="demoToggleEmpty">پیش‌نمایش حالت خالی</button>
          <button class="btn btn-primary btn-sm" id="createKeyBtn"><i data-icon="plus"></i> ساخت کلید جدید</button>
        </div>
      </div>
      <div>{rows}</div>
    </div>

    <div class="empty-state" id="keysEmpty" style="display:none">
      <span class="es-icon"><i data-icon="key-round"></i></span>
      <h2>هنوز هیچ کلید API ایجاد نکرده‌اید</h2>
      <p>با ساخت اولین کلید، محصول شما به بلو ورتکس متصل می‌شود — کمتر از یک دقیقه طول می‌کشد.</p>
      <button class="btn btn-primary" onclick="document.getElementById('createKeyBtn').click()"><i data-icon="plus"></i> ساخت کلید API</button>
    </div>

    <div class="card card-pad">
      <h2 class="t-h4 mb-16">بهترین روش‌های امنیتی</h2>
      <div class="grid-auto">
        <div class="flex gap-12"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="check"></i></span><span class="t-sm">برای هر سرویس، کلید جداگانه بسازید.</span></div>
        <div class="flex gap-12"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="check"></i></span><span class="t-sm">کلید را فقط در متغیر محیطی نگه دارید.</span></div>
        <div class="flex gap-12"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="check"></i></span><span class="t-sm">کلیدهای آزمایش (test) را از تولید جدا کنید.</span></div>
        <div class="flex gap-12"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="check"></i></span><span class="t-sm">دسترسی‌ها را به کمترین حد لازم محدود کنید.</span></div>
      </div>
    </div>

    <!-- create key modal -->
    <div class="modal-backdrop" id="createKeyModal" role="dialog" aria-modal="true" aria-label="ساخت کلید API">
      <div class="modal">
        <div class="modal-head">
          <div><h2>ساخت کلید API جدید</h2><p id="createKeyStepNote">دسترسی‌ها و محیط کلید را مشخص کنید.</p></div>
          <button class="modal-close" data-modal-close="createKeyModal" aria-label="بستن"><i data-icon="x"></i></button>
        </div>
        <div class="modal-body" id="createKeyStep1">
          <form id="createKeyForm" class="modal-inputs" data-form data-success-toast="none">
            <div class="field">
              <label class="field-label" for="keyName">نام کلید <span class="req">*</span></label>
              <input class="input" id="keyName" type="text" placeholder="مثلاً: وب‌سایت فروشگاه" required data-autofocus>
              <span class="field-error"></span>
            </div>
            <div class="field">
              <label class="field-label">محیط</label>
              <div class="env-tabs">
                <button type="button" class="active">production</button>
                <button type="button" style="color:var(--text-3)">test</button>
              </div>
              <span class="field-hint">کلیدهای test به داده‌های آزمایشی محدودند و هرگز به داده واقعی دسترسی ندارند.</span>
            </div>
            <div class="field">
              <label class="field-label">دسترسی‌ها (Scopes)</label>
              <div class="perm-grid" id="permGrid">
                <label class="perm-opt checked"><input type="checkbox" checked hidden><i data-icon="users"></i> users.read</label>
                <label class="perm-opt"><input type="checkbox" hidden><i data-icon="user-plus"></i> users.write</label>
                <label class="perm-opt checked"><input type="checkbox" checked hidden><i data-icon="credit-card"></i> payments.read</label>
                <label class="perm-opt"><input type="checkbox" hidden><i data-icon="credit-card"></i> payments.write</label>
                <label class="perm-opt"><input type="checkbox" hidden><i data-icon="upload-cloud"></i> files.write</label>
                <label class="perm-opt"><input type="checkbox" hidden><i data-icon="bar-chart-3"></i> analytics.read</label>
              </div>
            </div>
            <div class="field">
              <label class="field-label">انقضا (اختیاری)</label>
              <select class="select" aria-label="مدت اعتبار کلید"><option>بدون انقضا</option><option>۳۰ روز</option><option>۹۰ روز</option><option>۱ سال</option></select>
            </div>
          </form>
        </div>
        <div class="modal-body" id="createKeyStep2" style="display:none;text-align:center">
          <span class="icon-tile icon-tile-green" style="margin:0 auto 14px;width:52px;height:52px"><i data-icon="key-round"></i></span>
          <h2 class="t-h4 mb-8">کلید ساخته شد!</h2>
          <p class="t-caption mb-16">این کلید <b style="color:var(--red)">فقط همین یک‌بار</b> نمایش داده می‌شود. آن را همین حالا کپی و در متغیر محیطی ذخیره کنید.</p>
          <div class="key-reveal-box" style="text-align:left">
            <code id="newKeyValue">bv_live_••••••••</code>
            <button class="btn btn-soft btn-sm" data-copy-target="#newKeyValue"><i data-icon="copy"></i> کپی</button>
          </div>
          <div class="flex gap-12 mt-16" style="justify-content:center">
            <span class="badge" id="newKeyEnv">production</span>
            <span class="badge badge-blue">Scopes: کاربردی</span>
          </div>
        </div>
        <div class="modal-foot" id="mkFoot1">
          <button class="btn btn-ghost" data-modal-close="createKeyModal">انصراف</button>
          <button class="btn btn-primary" type="submit" form="createKeyForm"><i data-icon="key-round"></i> ساخت کلید</button>
        </div>
        <div class="modal-foot" id="mkFoot2" style="display:none">
          <button class="btn btn-primary btn-block" id="doneCreateKey">متوجه شدم، کلید را ذخیره کردم</button>
        </div>
      </div>
    </div>

    <!-- rename modal -->
    <div class="modal-backdrop" id="renameKeyModal" role="dialog" aria-modal="true" aria-label="تغییر نام کلید">
      <div class="modal modal-sm">
        <div class="modal-head"><div><h2>تغییر نام کلید</h2><p>نام فقط برای شما نمایش داده می‌شود؛ عملکرد کلید تغییری نمی‌کند.</p></div>
          <button class="modal-close" data-modal-close="renameKeyModal" aria-label="بستن"><i data-icon="x"></i></button></div>
        <div class="modal-body">
          <div class="field">
            <label class="field-label" for="renameKeyInput">نام جدید <span class="req">*</span></label>
            <input class="input" id="renameKeyInput" type="text" placeholder="نام کلید" data-autofocus>
            <span class="field-error"></span>
          </div>
        </div>
        <div class="modal-foot">
          <button class="btn btn-ghost" data-modal-close="renameKeyModal">انصراف</button>
          <button class="btn btn-primary" id="saveRename">ذخیره تغییر</button>
        </div>
      </div>
    </div>

    <!-- revoke modal -->
    <div class="modal-backdrop" id="revokeKeyModal" role="dialog" aria-modal="true" aria-label="باطل کردن کلید">
      <div class="modal modal-sm">
        <div class="modal-head"><div><h2 style="color:var(--red);display:flex;align-items:center;gap:8px"><i data-icon="alert-triangle" style="width:18px;height:18px"></i> باطل کردن کلید</h2>
          <p>کلید «<b id="revokeKeyName">—</b>» بلافاصله و برای همیشه غیرفعال می‌شود.</p></div>
          <button class="modal-close" data-modal-close="revokeKeyModal" aria-label="بستن"><i data-icon="x"></i></button></div>
        <div class="modal-body">
          <div class="security-note" style="margin:0">
            <i data-icon="shield-alert"></i>
            <span>هر برنامه‌ای که از این کلید استفاده می‌کند از این لحظه پاسخ <code class="inline">401</code> دریافت می‌کند. این عملیات قابل بازگشت نیست.</span>
          </div>
        </div>
        <div class="modal-foot">
          <button class="btn btn-ghost" data-modal-close="revokeKeyModal">انصراف</button>
          <button class="btn btn-danger" id="confirmRevoke">بله، کلید را باطل کن</button>
        </div>
      </div>
    </div>
'''
    actions = '<a class="btn btn-secondary btn-sm" href="endpoints.html"><i data-icon="braces"></i> آزمایش Endpoint</a><button class="btn btn-primary btn-sm" id="createKeyBtn2"><i data-icon="plus"></i> کلید جدید</button>'
    page = dash_page('کلیدهای API', 'dashboard/api-keys.html', 'کلیدهای API', 'مدیریت، ساخت و باطل‌سازی کلیدهای دسترسی فضای کاری ابرینو', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  var b2 = document.getElementById('createKeyBtn2');
  if (b2) b2.addEventListener('click', function(){ document.getElementById('createKeyBtn').click(); });
  document.getElementById('permGrid').addEventListener('click', function(e){
    var opt = e.target.closest('.perm-opt');
    if (!opt) return;
    var cb = opt.querySelector('input');
    cb.checked = !cb.checked;
    opt.classList.toggle('checked', cb.checked);
  });
  document.querySelectorAll('.env-tabs button').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.env-tabs button').forEach(function(x){ x.classList.remove('active'); x.style.color='var(--text-3)'; });
      b.classList.add('active'); b.style.color='';
    });
  });
})();
</script>''')
    return page

# ================================================================ USAGE
def build_usage(prefix=''):
    # stacked daily-usage bars — same data as before, custom markup
    def fa(n):
        return f'{n:,}'.translate(str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')).replace(',', '٬')
    days = [
        ('شنبه', 1180, 60), ('یکشنبه', 1240, 240), ('دوشنبه', 1300, 20),
        ('سه‌شنبه', 1420, 270), ('چهارشنبه', 1490, 355), ('پنجشنبه', 1350, 260), ('جمعه', 1180, 240),
    ]
    _max = max(p + t for _, p, t in days)
    cols, labs = [], []
    for d, prod, test in days:
        tot = prod + test
        h = round(tot / _max * 100, 1)          # bar height vs. busiest day
        sp = round(prod / tot * 100, 1)         # production share of the stack
        st = round(100 - sp, 1)
        cols.append(f'''          <div class="sb-col">
            <b class="sb-total fa-num">{fa(tot)}</b>
            <div class="sb-track" style="--h:{h}">
              <i class="sb-prod" style="height:{sp}%"></i>
              <i class="sb-test" style="height:{st}%"></i>
              <div class="sb-tip" aria-hidden="true">
                <span class="fa-num"><i style="background:#3B82F6"></i>تولید {fa(prod)}</span>
                <span class="fa-num"><i style="background:#38BDF8"></i>آزمایش {fa(test)}</span>
                <b class="fa-num sb-tip-total">مجموع {fa(tot)}</b>
              </div>
            </div>
          </div>''')
        labs.append(f'          <span>{d}</span>')
    sb_chart = f'''      <div class="stack-bars">
        <div class="sb-cols" role="img" aria-label="نمودار میله‌ای انباشته مصرف روزانه درخواست — تولید و آزمایش">
{chr(10).join(cols)}
        </div>
        <div class="sb-days">
{chr(10).join(labs)}
        </div>
      </div>'''
    content = f'''
    <div class="usage-quota">
      <div class="quota-card">
        <div class="quota-head"><b><i data-icon="activity" style="color:var(--blue-300)"></i> درخواست‌های API</b><span class="pct text-blue fa-num">۶۸٪</span></div>
        <div class="quota-nums"><b class="fa-num">۳٬۴۱۰٬۰۰۰</b><span>از ۵٬۰۰۰٬۰۰۰ در ماه</span></div>
        <div class="progress"><i style="width:68%"></i></div>
        <p class="t-caption mt-8 fa-num">باقی‌مانده: ۱٬۵۹۰٬۰۰۰ درخواست · پیش‌بینی اتمام: ۲۵ شهریور</p>
      </div>
      <div class="quota-card">
        <div class="quota-head"><b><i data-icon="cpu" style="color:var(--electric)"></i> توکن‌های مصرفی</b><span class="pct text-electric fa-num">۴۱٪</span></div>
        <div class="quota-nums"><b class="fa-num">۸۲۰ هزار</b><span>از ۲ میلیون در ماه</span></div>
        <div class="progress green"><i style="width:41%"></i></div>
        <p class="t-caption mt-8 fa-num">بیشترین مصرف: Endpoint تحلیل هوش مصنوعی</p>
      </div>
      <div class="quota-card">
        <div class="quota-head"><b><i data-icon="network" style="color:var(--violet)"></i> پهنای باند</b><span class="pct text-violet fa-num">۵۶٪</span></div>
        <div class="quota-nums"><b class="fa-num">۲۸۰GB</b><span>از ۵۰۰GB در ماه</span></div>
        <div class="progress amber"><i style="width:56%"></i></div>
        <p class="t-caption mt-8 fa-num">میانگین روزانه: ۹٫۳GB</p>
      </div>
      <div class="quota-card">
        <div class="quota-head"><b><i data-icon="database" style="color:var(--amber)"></i> ذخیره‌سازی فایل</b><span class="pct text-amber fa-num">۲۳٪</span></div>
        <div class="quota-nums"><b class="fa-num">۴۶GB</b><span>از ۲۰۰GB</span></div>
        <div class="progress"><i style="width:23%"></i></div>
        <p class="t-caption mt-8 fa-num">۴۱۲ فایل · بزرگ‌ترین: ۲۴MB</p>
      </div>
    </div>

    <div class="chart-card" style="margin-bottom:20px">
      <div class="chart-card-head"><div><h2>مصرف روزانه درخواست</h2><p>در بازه انتخابی — با فیلتر محیط و پروژه</p></div>
        <div class="flex gap-8"><span class="badge badge-blue">تولید</span><span class="badge badge-cyan">آزمایش</span></div></div>
      {sb_chart}
      <div class="chart-legend"><span><i style="background:#3B82F6"></i> تولید</span><span><i style="background:#38BDF8"></i> آزمایش</span></div>
      <div class="flex-between status-foot">
        <span class="t-caption">میانگین روزانه <b class="fa-num">۱٬۵۱۵</b> درخواست · اوج: چهارشنبه (<b class="fa-num">۱٬۸۴۵</b>)</span>
        <b class="t-sm fa-num">مجموع هفته: ۱۰٬۶۰۵ درخواست</b>
      </div>
    </div>

    <div class="dash-grid-2e">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>مصرف به تفکیک Endpoint</h2><p>۵ Endpoint پرمصرف — ۷ روز اخیر</p></div></div>
        <div class="table-wrap" style="border:none;border-radius:0">
          <table class="table">
            <thead><tr><th>Endpoint</th><th>درخواست</th><th>سهم</th><th>تغییر</th></tr></thead>
            <tbody>
              <tr><td><code class="inline text-code">GET /v1/users</code></td><td class="fa-num">۴۸٬۲۱۰</td><td style="min-width:120px"><div class="progress thin" style="width:110px"><i style="width:41%"></i></div></td><td class="text-green fa-num">+۱۸٪</td></tr>
              <tr><td><code class="inline text-code">POST /v1/payments</code></td><td class="fa-num">۲۹٬۴۴۰</td><td><div class="progress thin" style="width:110px"><i style="width:25%"></i></div></td><td class="text-green fa-num">+۹٪</td></tr>
              <tr><td><code class="inline text-code">GET /v1/payments/:id</code></td><td class="fa-num">۲۱٬۱۲۰</td><td><div class="progress thin" style="width:110px"><i style="width:18%"></i></div></td><td class="text-red fa-num">−۴٪</td></tr>
              <tr><td><code class="inline text-code">POST /v1/files</code></td><td class="fa-num">۱۲٬۴۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:10%"></i></div></td><td class="text-green fa-num">+۲۲٪</td></tr>
              <tr><td><code class="inline text-code">GET /v1/projects</code></td><td class="fa-num">۸٬۹۹۰</td><td><div class="progress thin" style="width:110px"><i style="width:7%"></i></div></td><td class="fa-num">+۲٪</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>مصرف توکن — ۱۴ روز اخیر</h2><p>بر اساس نوع فراخوانی</p></div></div>
        <div class="chart-holder short">
          <canvas data-chart data-chart-type="line" data-fill="1"
            data-labels='["۱","۲","۳","۴","۵","۶","۷","۸","۹","۱۰","۱۱","۱۲","۱۳","۱۴"]'
            data-values='[22,28,26,35,41,38,47,53,61,58,66,72,69,82]'
            data-colors='["rgb(56,189,248)"]' data-name="هزار توکن" data-unit="هزار توکن"></canvas>
        </div>
        <div class="chart-legend"><span><i style="background:#38BDF8"></i> هزار توکن در روز</span></div>
      </div>
    </div>

    <div class="chart-card">
      <div class="chart-card-head"><div><h2>گزارش مصرف ماهانه</h2><p>جزئیات مصرف هر پروژه به تفکیک — قابل خروجی CSV</p></div>
        <button class="btn btn-secondary btn-sm" data-csv-demo><i data-icon="download"></i> خروجی CSV</button></div>
      <div class="table-wrap" style="border:none;border-radius:0">
        <table class="table">
          <thead><tr><th>پروژه</th><th>درخواست‌ها</th><th>توکن</th><th>باند</th><th>هزینه‌ها</th><th>وضعیت سهمیه</th></tr></thead>
          <tbody>
            <tr><td class="cell-main">پنل مشتریان</td><td class="fa-num">۱٬۸۴۰٬۰۰۰</td><td class="fa-num">۴۱۰K</td><td class="fa-num">۱۲۴GB</td><td class="fa-num">۹۹۰٬۰۰۰ تومان</td><td><span class="badge badge-green">عادی</span></td></tr>
            <tr><td class="cell-main">وب‌سایت</td><td class="fa-num">۱٬۲۱۰٬۰۰۰</td><td class="fa-num">۲۸۰K</td><td class="fa-num">۹۸GB</td><td class="fa-num">۷۲۰٬۰۰۰ تومان</td><td><span class="badge badge-green">عادی</span></td></tr>
            <tr><td class="cell-main">هوش مصنوعی</td><td class="fa-num">۳۶۰٬۰۰۰</td><td class="fa-num">۱۳۰K</td><td class="fa-num">۵۸GB</td><td class="fa-num">۴۱۰٬۰۰۰ تومان</td><td><span class="badge badge-amber">۷۸٪</span></td></tr>
          </tbody>
        </table>
      </div>
    </div>
'''
    actions = daterange() + '<button class="btn btn-secondary btn-sm" data-export><i data-icon="download"></i> خروجی</button>'
    return dash_page('مصرف', 'dashboard/usage.html', 'مصرف', 'سهمیه‌ها، مصرف و گزارش تفکیکی فضای کاری ابرینو — <span class="fa-num">مرداد ۱۴۰۵</span>', content, actions=actions, charts=True,
                     extra_scripts='''<script>
(function(){
  doc = document;
  ['data-export','data-csv-demo'].forEach(function(attr){
    doc.querySelectorAll('[' + attr + ']').forEach(function(b){
      b.addEventListener('click', function(){
        if (!window.BV) return;
        if (attr === 'data-csv-demo') BV.toast('success', 'خروجی آماده شد', 'فایل usage-report.csv دانلود شد (نسخه دمو).');
        else BV.toast('info', 'در حال آماده‌سازی خروجی…', 'گزارش مصرف در حال تولید است.');
      });
    });
  });
})();
</script>''')

# ================================================================ ANALYTICS
def build_analytics(prefix=''):
    content = f'''
    <div class="stats-grid">
      <div class="stat"><span class="stat-label">حجم درخواست</span><b class="stat-value fa-num">۱۲۴٬۵۸۰</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> ۱۲٫۴٪</span></div>
      <div class="stat"><span class="stat-label">نرخ موفقیت</span><b class="stat-value fa-num">۹۹٫۹۸٪</b><span class="stat-delta delta-up"><i data-icon="arrow-up"></i> ۰٫۰۳٪</span></div>
      <div class="stat"><span class="stat-label">نرخ خطا</span><b class="stat-value fa-num">۰٫۰۴٪</b><span class="stat-delta delta-down"><i data-icon="arrow-down"></i> ۰٫۰۱٪</span></div>
      <div class="stat"><span class="stat-label">تأخیر میانگین</span><b class="stat-value fa-num">۱۴۸ms</b><span class="stat-delta delta-down"><i data-icon="arrow-down"></i> ۱۲ms</span></div>
    </div>

    <div class="charts-grid">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>نرخ موفقیت و تعداد خطا</h2><p>پوشش بازه ۳۰ روزه — دو محور مقایسه</p></div>
          <select class="select" aria-label="فیلتر Endpoint" style="width:auto;padding:6px 30px 6px 10px;font-size:var(--fs-caption)"><option>همه Endpointها</option><option>پرداخت‌ها</option><option>کاربران</option></select></div>
        <div class="chart-holder">
          <canvas data-chart data-chart-type="line" data-fill="1"
            data-labels='["۱","۵","۹","۱۳","۱۷","۲۱","۲۵","۲۹"]'
            data-values='[99.7,99.8,99.9,99.85,99.95,99.92,99.98,99.97]'
            data-colors='["rgb(52,211,153)"]' data-name="نرخ موفقیت" data-unit="٪"></canvas>
        </div>
        <div class="chart-legend"><span><i style="background:#34D399"></i> نرخ موفقیت (٪)</span></div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>خطاها بر اساس کد</h2><p>۳۰ روز اخیر</p></div></div>
        <div class="status-dist">
          <div class="status-donut">
            <svg viewBox="0 0 140 140" role="img" aria-label="نمودار توزیع خطاها بر اساس کد: ۳۹٫۹٪ احراز هویت، ۲۷٪ محدودیت نرخ، ۱۵٫۶٪ یافت نشد، ۱۱٫۸٪ داده نامعتبر، ۵٫۷٪ خطای سرور">
              <circle cx="70" cy="70" r="54" fill="none" style="stroke:var(--track)" stroke-width="16"/>
              <g transform="rotate(-90 70 70)">
                <circle cx="70" cy="70" r="54" fill="none" stroke="rgb(248,113,113)" stroke-width="16" pathLength="100" stroke-dasharray="39.9 100" stroke-dashoffset="0"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="rgb(251,191,36)" stroke-width="16" pathLength="100" stroke-dasharray="27 100" stroke-dashoffset="-39.9"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="rgb(167,139,250)" stroke-width="16" pathLength="100" stroke-dasharray="15.6 100" stroke-dashoffset="-66.9"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="rgb(56,189,248)" stroke-width="16" pathLength="100" stroke-dasharray="11.8 100" stroke-dashoffset="-82.5"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="rgb(34,211,238)" stroke-width="16" pathLength="100" stroke-dasharray="5.7 100" stroke-dashoffset="-94.3"/>
              </g>
              <text x="70" y="66" text-anchor="middle" class="status-donut-main">۷٬۱۲۰</text>
              <text x="70" y="86" text-anchor="middle" class="status-donut-sub">خطا</text>
            </svg>
          </div>
          <div class="status-legend">
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:rgb(248,113,113)"></span>
                <span class="t-caption">401 · احراز هویت</span>
                <b class="t-sm fa-num">۲٬۸۴۰</b>
                <span class="fa-num">۳۹٫۹٪</span>
              </div>
              <div class="st-track"><i style="width:39.9%;background:rgb(248,113,113)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:rgb(251,191,36)"></span>
                <span class="t-caption">429 · محدودیت نرخ</span>
                <b class="t-sm fa-num">۱٬۹۲۰</b>
                <span class="fa-num">۲۷٪</span>
              </div>
              <div class="st-track"><i style="width:27%;background:rgb(251,191,36)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:rgb(167,139,250)"></span>
                <span class="t-caption">404 · یافت نشد</span>
                <b class="t-sm fa-num">۱٬۱۱۰</b>
                <span class="fa-num">۱۵٫۶٪</span>
              </div>
              <div class="st-track"><i style="width:15.6%;background:rgb(167,139,250)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:rgb(56,189,248)"></span>
                <span class="t-caption">422 · داده نامعتبر</span>
                <b class="t-sm fa-num">۸۴۰</b>
                <span class="fa-num">۱۱٫۸٪</span>
              </div>
              <div class="st-track"><i style="width:11.8%;background:rgb(56,189,248)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:rgb(34,211,238)"></span>
                <span class="t-caption">5xx · خطای سرور</span>
                <b class="t-sm fa-num">۴۱۰</b>
                <span class="fa-num">۵٫۷٪</span>
              </div>
              <div class="st-track"><i style="width:5.7%;background:rgb(34,211,238)"></i></div>
            </div>
          </div>
        </div>
        <div class="status-seg" role="img" aria-label="نوار توزیع خطاها: ۳۹٫۹٪ احراز هویت، ۲۷٪ محدودیت نرخ، ۱۵٫۶٪ یافت نشد، ۱۱٫۸٪ داده نامعتبر، ۵٫۷٪ خطای سرور">
          <i style="width:39.9%;background:rgb(248,113,113)"></i><i style="width:27%;background:rgb(251,191,36)"></i><i style="width:15.6%;background:rgb(167,139,250)"></i><i style="width:11.8%;background:rgb(56,189,248)"></i><i style="width:5.7%;background:rgb(34,211,238)"></i>
        </div>
        <div class="flex-between status-foot">
          <span class="t-caption">مجموع خطاها — ۳۰ روز اخیر</span>
          <b class="t-sm fa-num">۷٬۱۲۰ خطا</b>
        </div>
      </div>
    </div>

    <div class="charts-grid">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>تأخیر صدک‌ها (P50 / P95 / P99)</h2><p>میلی‌ثانیه — زمان پاسخ خالص سرور</p></div></div>
        <div class="chart-holder">
          <canvas data-chart data-chart-type="bar"
            data-labels='["GET /v1/users","POST /v1/payments","GET /v1/payments/:id","POST /v1/files","GET /v1/projects"]'
            data-values='[[88,142,116,280,64],[210,318,265,470,150],[390,520,480,690,260]]'
            data-colors='["rgb(59,130,246)","rgb(56,189,248)","rgb(167,139,250)"]'
            data-ds-names='["P50","P95","P99"]' data-unit="ms"></canvas>
        </div>
        <div class="chart-legend"><span><i style="background:#3B82F6"></i> P50</span><span><i style="background:#38BDF8"></i> P95</span><span><i style="background:#A78BFA"></i> P99</span></div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>عملکرد Endpointها</h2><p>نمره سلامت ترکیبی</p></div></div>
        <div class="chart-holder">
          <canvas data-chart data-chart-type="bar"
            data-labels='["کاربران","پروژه‌ها","پرداخت‌ها","فایل‌ها","تحلیل‌ها"]'
            data-values='[98,99,94,91,97]'
            data-colors='["rgb(52,211,153)"]' data-name="سلامت" data-unit="٪"></canvas>
        </div>
        <div class="chart-legend"><span><i style="background:#34D399"></i> نمره سلامت ترکیبی (٪)</span></div>
      </div>
    </div>

    <div class="dash-grid-2">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>توزیع جغرافیایی</h2><p>بر اساس IP درخواست‌ها — ۳۰ روز اخیر</p></div></div>
        <div class="table-wrap" style="border:none;border-radius:0">
          <table class="table">
            <thead><tr><th>شهر / منطقه</th><th>درخواست</th><th>سهم</th><th>تأخیر میانگین</th></tr></thead>
            <tbody>
              <tr><td class="cell-main">تهران</td><td class="fa-num">۴۸٬۲۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:78%"></i></div></td><td class="latency-cell fa-num">۸۴ms</td></tr>
              <tr><td class="cell-main">اصفهان</td><td class="fa-num">۱۸٬۴۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:30%"></i></div></td><td class="latency-cell fa-num">۹۶ms</td></tr>
              <tr><td class="cell-main">شیراز</td><td class="fa-num">۱۴٬۱۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:23%"></i></div></td><td class="latency-cell fa-num">۱۰۲ms</td></tr>
              <tr><td class="cell-main">مشهد</td><td class="fa-num">۱۱٬۸۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:19%"></i></div></td><td class="latency-cell fa-num">۱۱۸ms</td></tr>
              <tr><td class="cell-main">خارج از کشور</td><td class="fa-num">۴٬۹۰۰</td><td><div class="progress thin" style="width:110px"><i style="width:8%"></i></div></td><td class="latency-cell fa-num">۲۱۰ms</td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>پلتفرم و کلاینت</h2><p>بر اساس User-Agent</p></div></div>
        <div class="chart-card-head" style="margin-bottom:6px"><div><h2 style="font-size:var(--fs-sm)">دستگاه</h2></div></div>
        <table class="kv-table">
          <tbody>
            <tr><td>API / سرویس</td><td class="fa-num">۶۲٪</td></tr>
            <tr><td>وب (مرورگر)</td><td class="fa-num">۲۱٪</td></tr>
            <tr><td>اندروید</td><td class="fa-num">۱۲٪</td></tr>
            <tr><td>iOS</td><td class="fa-num">۵٪</td></tr>
          </tbody>
        </table>
        <div class="chart-card-head" style="margin:14px 0 6px"><div><h2 style="font-size:var(--fs-sm)">کتابخانه</h2></div></div>
        <table class="kv-table">
          <tbody>
            <tr><td>@bluevertex/sdk</td><td class="fa-num">۵۸٪</td></tr>
            <tr><td>bluevertex (Python)</td><td class="fa-num">۲۶٪</td></tr>
            <tr><td>cURL / سایر</td><td class="fa-num">۱۶٪</td></tr>
          </tbody>
        </table>
      </div>
    </div>
'''
    actions = daterange() + '<button class="btn btn-secondary btn-sm" data-export><i data-icon="download"></i> خروجی گزارش</button>'
    return dash_page('تحلیل‌ها', 'dashboard/analytics.html', 'تحلیل‌ها', 'تحلیل عملکرد API، خطاها و تأخیر — فضای کاری ابرینو', content, actions=actions, charts=True,
                     extra_scripts='''<script>
(function(){
  document.querySelectorAll('[data-export]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', 'گزارش آماده شد', 'فایل analytics.xlsx دانلود شد (نسخه دمو).');
    });
  });
})();
</script>''')

# ================================================================ LOGS
LOG_ROWS = [
    ('req_9d41c7', '۱۲:۰۴:۲۲', 'POST', '/v1/users', '201', '48', '5.120.44.18', 'prod'),
    ('req_9d41c6', '۱۲:۰۴:۱۹', 'GET', '/v1/payments/7f31', '200', '112', '185.94.10.2', 'prod'),
    ('req_9d41b2', '۱۲:۰۴:۰۳', 'GET', '/v1/users?page=2', '200', '64', '5.120.44.18', 'prod'),
    ('req_9d4199', '۱۲:۰۳:۵۸', 'POST', '/v1/payments', '429', '8', '91.99.4.7', 'prod'),
    ('req_9d4190', '۱۲:۰۳:۴۴', 'GET', '/v1/files/9f2', '404', '22', '185.94.10.2', 'prod'),
    ('req_9d4178', '۱۲:۰۳:۳۱', 'POST', '/v1/files', '201', '312', '5.120.44.18', 'prod'),
    ('req_9d4163', '۱۲:۰۳:۱۲', 'GET', '/v1/analytics/geo', '200', '180', '10.0.4.12', 'test'),
    ('req_9d4151', '۱۲:۰۲:۵۸', 'DELETE', '/v1/users/77a2', '204', '38', '91.99.4.7', 'prod'),
    ('req_9d4140', '۱۲:۰۲:۴۱', 'POST', '/v1/users', '401', '9', '151.240.8.90', 'prod'),
    ('req_9d4132', '۱۲:۰۲:۲۶', 'GET', '/v1/projects', '200', '52', '5.120.44.18', 'prod'),
    ('req_9d4120', '۱۲:۰۲:۰۹', 'POST', '/v1/payments', '500', '1240', '185.94.10.2', 'prod'),
    ('req_9d4111', '۱۲:۰۱:۵۴', 'GET', '/v1/users/8f2k1', '200', '71', '10.0.4.12', 'test'),
]

def build_logs(prefix=''):
    rows = ''
    for rid, time, method, path, status, ms, ip, env in LOG_ROWS:
        s = int(status)
        cls = 'log-status" style="color:' + ('var(--green)' if s < 400 else 'var(--amber)' if s < 500 else 'var(--red)')
        env_b = 'prod'
        rows += f'''<tr data-row data-search="{rid} {path} {ip} {method}" data-status="{s}" data-method="{method}" data-env="{env}"
      data-log-id="{rid}" data-log-time="{time}" data-log-method="{method}" data-log-path="{path}"
      data-log-status="{status}" data-log-ms="{ms}" data-log-ip="{ip}" data-log-env="{env}">
      <td><code class="ltr text-code" style="font-size:.72rem">{rid}</code></td>
      <td><span class="fa-num">{time}</span></td>
      <td><span class="method method-{method.lower()}">{method}</span></td>
      <td><code class="inline text-code">{path}</code></td>
      <td><span class="{cls}"><i></i>{status}</span></td>
      <td class="latency-cell">{ms}ms</td>
      <td><code class="ltr" style="font-size:.72rem;color:var(--text-3)">{ip}</code></td>
      <td><span class="badge {'badge-amber' if env == 'prod' else 'badge-cyan'}">{'تولید' if env == 'prod' else 'آزمایش'}</span></td>
    </tr>'''
    content = f'''
    <div class="filter-bar" id="logScope" data-table-scope>
      <div class="search-input">
        <i data-icon="search"></i>
        <input class="input" data-filter="text" placeholder="جستجوی Request ID، Endpoint یا IP…" aria-label="جستجو در گزارش‌ها">
      </div>
      <select class="select" data-filter="status" aria-label="فیلتر وضعیت">
        <option value="">همه وضعیت‌ها</option><option value="2">موفق (2xx)</option><option value="4">خطای کلاینت (4xx)</option><option value="5">خطای سرور (5xx)</option>
      </select>
      <select class="select" data-filter="method" aria-label="فیلتر متد">
        <option value="">همه متدها</option><option>GET</option><option>POST</option><option>DELETE</option>
      </select>
      <select class="select" data-filter="env" aria-label="فیلتر محیط">
        <option value="">همه محیط‌ها</option><option value="prod">تولید</option><option value="test">آزمایش</option>
      </select>
      <button class="btn btn-ghost btn-sm" data-log-refresh><i data-icon="refresh-cw"></i> به‌روزرسانی</button>
      <span class="filter-count" data-filter-count>نمایش ۱۲ مورد از ۱۲</span>
    </div>

    <div class="card" style="overflow:hidden">
      <div class="card-head" style="align-items:center">
        <div><h2>درخواست‌های اخیر</h2><p class="t-caption" style="margin-top:4px">برای مشاهده جزئیات، روی هر ردیف کلیک کنید</p></div>
        <span class="badge badge-green"><span class="dot"></span> ضبط زنده</span>
      </div>
      <div class="table-wrap" style="border:none;border-radius:0">
        <table class="table">
          <thead><tr><th>Request ID</th><th>زمان</th><th>متد</th><th>Endpoint</th><th>وضعیت</th><th>تأخیر</th><th>IP</th><th>محیط</th></tr></thead>
          <tbody>
            {rows}
          </tbody>
        </table>
        <div class="empty-state" data-filter-empty style="display:none">
          <span class="es-icon"><i data-icon="search-x"></i></span>
          <h2>درخواستی با این فیلتر پیدا نشد</h2>
          <p>فیلترها را تغییر دهید یا عبارت دیگری جستجو کنید.</p>
        </div>
        <div class="table-footer">
          <span class="fa-num">صفحه ۱ از ۴۲</span>
          <nav class="pagination" aria-label="صفحه‌بندی گزارش‌ها">
            <button class="page-btn" disabled aria-label="صفحه قبل"><i data-icon="chevron-right"></i></button>
            <button class="page-btn active">۱</button><button class="page-btn">۲</button><button class="page-btn">۳</button>
            <button class="page-btn" aria-label="صفحه بعد"><i data-icon="chevron-left"></i></button>
          </nav>
        </div>
      </div>
    </div>
'''
    actions = daterange() + '<button class="btn btn-primary btn-sm" data-export><i data-icon="download"></i> خروجی CSV</button>'
    return dash_page('گزارش درخواست‌ها', 'dashboard/logs.html', 'گزارش درخواست‌ها', 'لاگ زنده همه درخواست‌های API — با فیلتر و جزئیات کامل', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  document.querySelectorAll('[data-log-refresh]').forEach(function(b){
    b.addEventListener('click', function(){
      b.classList.add('btn-loading');
      setTimeout(function(){
        b.classList.remove('btn-loading');
        if (window.BV) BV.toast('success', 'گزارش‌ها به‌روزرسانی شد', '۱۲ درخواست جدید نمایش داده می‌شود.');
      }, 900);
    });
  });
  document.querySelectorAll('[data-export]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', 'خروجی آماده شد', 'فایل logs.csv با فیلتر فعلی دانلود شد (دمو).');
    });
  });
})();
</script>''') + drawer_log()

# ================================================================ ENDPOINTS + EXPLORER
def build_endpoints(prefix=''):
    eps = [
        ('GET', '/v1/users', 'green', '۴۸٬۲۱۰', '88ms', '0.01٪', [40, 62, 50, 78, 66, 90, 74]),
        ('POST', '/v1/users', 'green', '۹٬۳۲۰', '142ms', '0.04٪', [20, 34, 28, 45, 38, 52, 44]),
        ('GET', '/v1/users/:id', 'green', '۲۱٬۱۲۰', '116ms', '0.02٪', [30, 42, 36, 50, 44, 58, 48]),
        ('GET', '/v1/projects', 'green', '۸٬۹۹۰', '64ms', '0.00٪', [12, 20, 16, 26, 22, 30, 24]),
        ('POST', '/v1/projects', 'green', '۱٬۲۴۰', '158ms', '0.08٪', [6, 9, 8, 12, 10, 14, 11]),
        ('POST', '/v1/payments', 'amber', '۲۹٬۴۴۰', '142ms', '0.6٪', [50, 70, 62, 88, 76, 95, 80]),
        ('GET', '/v1/payments/:id', 'green', '۲۱٬۱۰۰', '116ms', '0.1٪', [30, 44, 38, 52, 46, 60, 50]),
        ('GET', '/v1/payments', 'green', '۶٬۸۰۰', '124ms', '0.2٪', [10, 16, 13, 20, 17, 24, 19]),
        ('POST', '/v1/files', 'green', '۱۲٬۴۰۰', '280ms', '0.3٪', [8, 12, 10, 15, 13, 18, 14]),
        ('GET', '/v1/files/:id', 'green', '۵٬۲۰۰', '98ms', '0.05٪', [5, 8, 6, 10, 8, 12, 9]),
    ]
    rows = ''
    for m, path, col, count, lat, err, spark in eps:
        bars = ''.join(f'<i style="height:{v}%"></i>' for v in spark)
        rows += f'''<tr data-row data-search="{path} {m}" data-status="{path}" data-method="{m}" data-env="prod">
      <td><span class="method method-{m.lower()}">{m}</span></td>
      <td><code class="ep-path">{path}</code></td>
      <td class="fa-num">{count}</td>
      <td><span class="mini-bars" aria-hidden="true">{bars}</span></td>
      <td class="latency-cell fa-num">{lat}</td>
      <td><span class="badge badge-{col}">{err}</span></td>
      <td><button class="btn btn-ghost btn-sm" data-ep-doc="{path.strip('/').replace('/', '_').replace(':', 'id')}">مستندات</button></td>
    </tr>'''
    content = f'''
    <div class="filter-bar" id="epFilterBar" data-table-scope>
      <div class="search-input">
        <i data-icon="search"></i>
        <input class="input" data-filter="text" placeholder="جستجوی Endpoint یا مسیر…" aria-label="جستجوی Endpoint">
      </div>
      <select class="select" data-filter="method" aria-label="فیلتر متد">
        <option value="">همه متدها</option><option>GET</option><option>POST</option>
      </select>
      <span class="filter-count" data-filter-count>نمایش ۱۰ Endpoint</span>
    </div>

    <div class="card" style="overflow:hidden;margin-bottom:20px">
      <div class="card-head"><div><h2>Endpointهای فضای کاری</h2><p class="t-caption" style="margin-top:4px">عملکرد ۷ روز اخیر — کلیک روی «مستندات» برای مرجع کامل</p></div>
        <a class="btn btn-ghost btn-sm" href="../docs/api-reference.html"><i data-icon="book-open"></i> مرجع API</a></div>
      <div class="table-wrap" style="border:none;border-radius:0">
        <table class="table ep-table">
          <thead><tr><th>متد</th><th>Endpoint</th><th>درخواست‌ها</th><th>روند</th><th>تأخیر P50</th><th>نرخ خطا</th><th></th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        <div class="empty-state" data-filter-empty style="display:none">
          <span class="es-icon"><i data-icon="search-x"></i></span>
          <h2>Endpointی پیدا نشد</h2><p>عبارت جستجو را تغییر دهید.</p>
        </div>
      </div>
    </div>

    <div class="explorer">
      <div class="explorer-head">
        <div style="flex:1;min-width:200px">
          <h2 class="t-h4">مرورگر تعاملی API <span class="badge badge-blue">شبیه‌سازی</span></h2>
          <p class="t-caption" style="margin-top:4px">درخواست نمونه بسازید و پاسخ شبیه‌سازی‌شده ببینید — هیچ درخواست واقعی ارسال نمی‌شود.</p>
        </div>
        <div class="flex gap-8"><span class="badge">پایه: api.bluevertex.ir</span></div>
      </div>
      <div class="explorer-body">
        <form id="expForm" class="modal-inputs" novalidate>
          <div class="grid-2" style="gap:14px">
            <div class="field">
              <label class="field-label" for="expEndpoint">Endpoint</label>
              <select class="select ltr" id="expEndpoint" dir="ltr">
                <option>GET /v1/users</option>
                <option>POST /v1/users</option>
                <option>GET /v1/projects</option>
                <option>POST /v1/payments</option>
                <option>POST /v1/files</option>
                <option>GET /v1/users/nonexistent</option>
              </select>
            </div>
            <div class="field">
              <label class="field-label">پارامترها و هدرها</label>
              <div class="flex gap-12" style="flex-wrap:wrap;height:44px;align-items:center">
                <label class="check"><input type="checkbox" id="expAuth" checked><span class="box"><i data-icon="check"></i></span><span>ارسال کلید API</span></label>
                <label class="check"><input type="checkbox" checked><span class="box"><i data-icon="check"></i></span><span>Content-Type: JSON</span></label>
              </div>
            </div>
          </div>
          <div class="field">
            <label class="field-label" for="expBody">بدنه درخواست (JSON)</label>
            <textarea class="textarea ltr" id="expBody" dir="ltr" rows="5" spellcheck="false"></textarea>
          </div>
          <div class="flex gap-12" style="margin-top:6px">
            <button class="btn btn-primary" type="submit" id="expSend"><i data-icon="send"></i> ارسال درخواست (شبیه‌سازی)</button>
            <button class="btn btn-ghost" type="button" id="expClear">پاک کردن</button>
            <span class="t-caption" style="align-self:center">پاسخ پس از ~۱٫۳ ثانیه نمایش داده می‌شود</span>
          </div>
        </form>
        <div class="explorer-response" id="expResponse">
          <div class="explorer-stats">
            <span class="exp-stat ok" data-exp-stat><span class="dot"></span> HTTP 200 — موفق</span>
            <span class="exp-stat"><i data-icon="timer" style="width:12px;height:12px"></i> <span data-exp-time>۲۲۰ms</span></span>
            <span class="exp-stat"><i data-icon="file" style="width:12px;height:12px"></i> حجم: <span data-exp-size>سازگار</span></span>
            <span class="exp-stat"><i data-icon="hash" style="width:12px;height:12px"></i> Request ID: <span class="ltr">req_<span data-exp-rid>demo</span></span></span>
          </div>
          <div class="code-block">
            <div class="code-head"><span class="code-lang">json</span><button class="code-copy" data-copy-target="#expBodyResult" aria-label="کپی"><i data-icon="copy"></i></button></div>
            <pre id="expBodyResult" style="margin:0;padding:16px 20px;overflow-x:auto"><code class="language-json">{{}}</code></pre>
          </div>
        </div>
      </div>
    </div>
'''
    actions = '<a class="btn btn-secondary btn-sm" href="logs.html"><i data-icon="scroll-text"></i> گزارش‌ها</a>'
    return dash_page('Endpointها', 'dashboard/endpoints.html', 'Endpointها', 'فهرست Endpointها، عملکرد و مرورگر تعاملی — فضای کاری ابرینو', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  document.getElementById('expClear').addEventListener('click', function(){
    document.getElementById('expBody').value = '';
    document.getElementById('expResponse').classList.remove('show');
  });
  document.querySelectorAll('[data-ep-doc]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('info', 'باز کردن مستندات', 'در نسخه دمو، به مرجع API هدایت می‌شوید.');
      setTimeout(function(){ window.location.href = '../docs/api-reference.html'; }, 700);
    });
  });
})();
</script>''')
