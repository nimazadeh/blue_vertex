# -*- coding: utf-8 -*-
"""Blue Vertex — Developer Console pages (dashboard/*)"""

from chrome import head, palette, scripts, dash_sidebar, DASH_TOP, TOAST_REGION

def dash_page(title_crumb, active, title, subtitle, content, actions='', charts=False, extra_scripts='', page_title=None, page_desc=None):
    pt = page_title or (title.replace('<br>', ' ') + ' | داشبورد بلو ورتکس')
    pd = page_desc or ('داشبورد توسعه‌دهنده بلو ورتکس — ' + title.replace('<br>', ' '))
    head_html = head(pt, pd, '../')
    crumb = DASH_TOP.replace('>نمای کلی<', f'>{title_crumb}<')
    return head_html + '''<body class="noise">
<div class="dash-shell">
''' + dash_sidebar(active, '../') + crumb + '''
  <main class="dash-main">
    <div class="dash-content">
      <div class="dash-head">
        <div>
          <h1 style="margin:0">''' + title + '''</h1>
          <p class="greet-sub" style="margin:0;margin-top:4px">''' + subtitle + '''</p>
        </div>
        <div class="dash-actions" data-dash-actions>''' + actions + '''</div>
      </div>
      ''' + content + '''
    </div>
  </main>
</div>
''' + palette('../') + TOAST_REGION + scripts('../', charts=charts) + extra_scripts + '''
<script>
(function(){
  var now = new Date();
  var el = document.getElementById('jalaliToday');
  if (el && window.BV) el.textContent = BV.faDateFull(now);
})();
</script>
</body></html>'''

def daterange():
    return f'''<div class="dropdown" data-dd>
  <button class="btn btn-secondary btn-sm" data-dd-toggle data-daterange>
    <i data-icon="calendar"></i>
    <span id="rangeLabel">۷ روز اخیر</span>
    <i data-icon="chevron-down" style="width:13px;height:13px"></i>
  </button>
  <div class="dropdown-menu" style="min-width:190px">
    <div class="menu-title">بازه زمانی</div>
    <button class="menu-item" data-range="24h" data-range-label="۲۴ ساعت اخیر"><i data-icon="clock"></i>۲۴ ساعت اخیر</button>
    <button class="menu-item active" data-range="7d" data-range-label="۷ روز اخیر"><i data-icon="calendar-days"></i>۷ روز اخیر</button>
    <button class="menu-item" data-range="30d" data-range-label="۳۰ روز اخیر"><i data-icon="calendar"></i>۳۰ روز اخیر</button>
    <button class="menu-item" data-range="90d" data-range-label="۹۰ روز اخیر"><i data-icon="calendar-range"></i>۹۰ روز اخیر</button>
  </div>
</div>'''

def drawer_log():
    return '''<div class="drawer-backdrop" id="logDrawerBackdrop"></div>
<aside class="drawer" id="logDrawer" role="dialog" aria-modal="true" aria-label="جزئیات درخواست">
  <div class="drawer-head">
    <div>
      <div class="flex gap-8">
        <h2 class="t-h4">جزئیات درخواست</h2>
        <span class="badge" id="ldStatusBadge">HTTP 200</span>
      </div>
      <code class="ltr t-caption" id="ldRequestId" style="color:var(--text-3)">req_9d41c7</code>
    </div>
    <button class="modal-close" data-drawer-close="logDrawer" aria-label="بستن"><i data-icon="x"></i></button>
  </div>
  <div class="drawer-body">
    <div class="rr-meta" style="grid-template-columns:repeat(2,1fr)">
      <div class="rr-meta-item"><span>Endpoint</span><b class="ltr" style="font-size:.7rem" id="ldPath">/v1/users</b></div>
      <div class="rr-meta-item"><span>متد</span><b class="ltr" id="ldMethod">POST</b></div>
      <div class="rr-meta-item"><span>زمان</span><b id="ldTime" style="font-size:.72rem">—</b></div>
      <div class="rr-meta-item"><span>تأخیر</span><b id="ldMs">—</b></div>
      <div class="rr-meta-item"><span>آدرس IP</span><b class="ltr" style="font-size:.78rem" id="ldIp">—</b></div>
      <div class="rr-meta-item"><span>محیط</span><b id="ldEnv">production</b></div>
    </div>
    <div class="drawer-section">
      <h3 class="drawer-h"><i data-icon="list"></i> هدرهای درخواست</h3>
      <table class="kv-table"><tbody>
        <tr><td>authorization</td><td>Bearer bv_live_••••••</td></tr>
        <tr><td>content-type</td><td>application/json</td></tr>
        <tr><td>user-agent</td><td>okhttp/4.12 · Android 14</td></tr>
        <tr><td>x-request-id</td><td id="ldReqIdHeader">req_9d41c7</td></tr>
      </tbody></table>
    </div>
    <div class="drawer-section">
      <h3 class="drawer-h"><i data-icon="arrow-up-circle"></i> بدنه درخواست</h3>
      <div class="code-block"><div class="code-head"><span class="code-lang">json</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
        <pre class="line-numbers"><code class="language-json" id="ldReqBody">{
  "name": "سارا احمدی",
  "email": "sara@abrino.ir",
  "role": "developer"
}</code></pre></div>
    </div>
    <div class="drawer-section">
      <h3 class="drawer-h"><i data-icon="arrow-down-circle"></i> بدنه پاسخ</h3>
      <div class="code-block"><div class="code-head"><span class="code-lang">json</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
        <pre class="line-numbers"><code class="language-json" id="ldResBody">{
  "data": { "id": "usr_8f2k1", "name": "سارا احمدی" },
  "meta": { "request_id": "req_9d41c7" }
}</code></pre></div>
    </div>
    <div class="drawer-section">
      <h3 class="drawer-h"><i data-icon="activity"></i> متادیتا</h3>
      <table class="kv-table"><tbody>
        <tr><td>region</td><td>tehran</td></tr>
        <tr><td>auth_scopes</td><td>users.write</td></tr>
        <tr><td>rate_remaining</td><td>9<span class="fa-num" data-fa-note></span>991</td></tr>
      </tbody></table>
    </div>
  </div>
  <div class="drawer-foot">
    <button class="btn btn-secondary" data-drawer-close="logDrawer">بستن</button>
    <button class="btn btn-soft" data-copy-target="#ldRequestId" data-copy="req_9d41c7"><i data-icon="copy"></i> کپی Request ID</button>
  </div>
</aside>'''

# ================================================================ OVERVIEW
def build_index(prefix=''):
    content = f'''
    <div class="stats-grid">
      <div class="stat">
        <span class="stat-label"><i data-icon="activity" style="width:13px;height:13px"></i> درخواست‌های API</span>
        <b class="stat-value fa-num">۱۲۴٬۵۸۰</b>
        <span class="stat-delta delta-up"><i data-icon="arrow-up"></i> ۱۲٫۴٪ نسبت به دوره قبل</span>
      </div>
      <div class="stat">
        <span class="stat-label"><i data-icon="gauge" style="width:13px;height:13px"></i> مصرف سهمیه</span>
        <b class="stat-value fa-num">۶۸٪</b>
        <span class="stat-delta" style="color:var(--text-3)">از ۵ میلیون درخواست ماهانه</span>
      </div>
      <div class="stat">
        <span class="stat-label"><i data-icon="check-circle-2" style="width:13px;height:13px"></i> نرخ موفقیت</span>
        <b class="stat-value fa-num">۹۹٫۹۸٪</b>
        <span class="stat-delta delta-up"><i data-icon="arrow-up"></i> ۰٫۰۳٪ بهبود</span>
      </div>
      <div class="stat">
        <span class="stat-label"><i data-icon="timer" style="width:13px;height:13px"></i> میانگین زمان پاسخ</span>
        <b class="stat-value fa-num">۱۴۸ms</b>
        <span class="stat-delta delta-down"><i data-icon="arrow-down"></i> ۱۲ms بهبود</span>
      </div>
    </div>

    <div class="charts-grid">
      <div class="chart-card">
        <div class="chart-card-head">
          <div><h2>درخواست‌ها در طول زمان</h2><p>مجموع درخواست‌های موفق و ناموفق</p></div>
          <span class="badge badge-green"><span class="dot"></span> زنده</span>
        </div>
        <div class="chart-holder">
          <canvas data-chart data-chart-type="line" data-fill="1" data-no-rtl="1" data-rangeable="1"
            data-labels='["شنبه","یکشنبه","دوشنبه","سه‌شنبه","چهارشنبه","پنجشنبه","جمعه"]'
            data-values='[1240,1480,1320,1690,1845,1610,1420]'
            data-colors='["rgb(59,130,246)"]' data-name="درخواست" data-unit="درخواست"></canvas>
        </div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>توزیع وضعیت</h2><p>۲۴ ساعت اخیر</p></div></div>
        <div class="status-dist">
          <div class="status-donut">
            <svg viewBox="0 0 140 140" role="img" aria-label="نمودار توزیع وضعیت درخواست‌ها: ۹۶٫۳٪ موفق، ۳٫۱٪ خطای کلاینت، ۰٫۶٪ خطای سرور">
              <circle cx="70" cy="70" r="54" fill="none" style="stroke:var(--track)" stroke-width="16"/>
              <g transform="rotate(-90 70 70)">
                <circle cx="70" cy="70" r="54" fill="none" stroke="var(--green)" stroke-width="16" pathLength="100" stroke-dasharray="96.3 100" stroke-dashoffset="0"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="var(--amber)" stroke-width="16" pathLength="100" stroke-dasharray="3.1 100" stroke-dashoffset="-96.3"/>
                <circle cx="70" cy="70" r="54" fill="none" stroke="var(--red)" stroke-width="16" pathLength="100" stroke-dasharray="0.6 100" stroke-dashoffset="-99.4"/>
              </g>
              <text x="70" y="66" text-anchor="middle" class="status-donut-main">۹۶٫۳٪</text>
              <text x="70" y="86" text-anchor="middle" class="status-donut-sub">موفق</text>
            </svg>
          </div>
          <div class="status-legend">
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:var(--green)"></span>
                <span class="t-caption">موفق</span>
                <b class="t-sm fa-num">۱۱٬۷۸۰</b>
                <span class="fa-num">۹۶٫۳٪</span>
              </div>
              <div class="st-track"><i style="width:96.3%;background:var(--green)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:var(--amber)"></span>
                <span class="t-caption">خطای کلاینت</span>
                <b class="t-sm fa-num">۳۸۱</b>
                <span class="fa-num">۳٫۱٪</span>
              </div>
              <div class="st-track"><i style="width:3.1%;background:var(--amber)"></i></div>
            </div>
            <div class="st-row">
              <div class="st-row-head">
                <span class="st-dot" style="background:var(--red)"></span>
                <span class="t-caption">خطای سرور</span>
                <b class="t-sm fa-num">۷۱</b>
                <span class="fa-num">۰٫۶٪</span>
              </div>
              <div class="st-track"><i style="width:0.6%;background:var(--red)"></i></div>
            </div>
          </div>
        </div>
        <div class="status-seg" role="img" aria-label="نوار توزیع: ۹۶٫۳٪ موفق، ۳٫۱٪ خطای کلاینت، ۰٫۶٪ خطای سرور">
          <i style="width:96.3%;background:var(--green)"></i><i style="width:3.1%;background:var(--amber)"></i><i style="width:0.6%;background:var(--red)"></i>
        </div>
        <div class="flex-between status-foot">
          <span class="t-caption">مجموع ۲۴ ساعت اخیر</span>
          <b class="t-sm fa-num">۱۲٬۲۳۲ درخواست</b>
        </div>
      </div>
    </div>

    <div class="dash-grid-2">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>فعالیت‌های اخیر</h2><p>آخرین رویدادهای فضای کاری</p></div><a class="link" style="font-size:var(--fs-caption)" href="logs.html">همه گزارش‌ها <i data-icon="arrow-left"></i></a></div>
        <div class="activity-list">
          <div class="activity-item"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="check"></i></span><div><b>کلید «تولید — اصلی» استفاده شد</b><p>POST /v1/users · ۲۰۰ OK · ۴۸ms</p></div><time>۲ دقیقه پیش</time></div>
          <div class="activity-item"><span class="icon-tile icon-tile-sm icon-tile-amber"><i data-icon="alert-triangle"></i></span><div><b>خطای نرخ 429 در Endpoint پرداخت</b><p>GET /v1/payments · بیش از حد مجاز</p></div><time>۱۸ دقیقه پیش</time></div>
          <div class="activity-item"><span class="icon-tile icon-tile-sm"><i data-icon="key-round"></i></span><div><b>کلید «آزمایش — توسعه» ساخته شد</b><p>توسط مریم کریمی · محیط test</p></div><time>۲ ساعت پیش</time></div>
          <div class="activity-item"><span class="icon-tile icon-tile-sm icon-tile-red"><i data-icon="shield-alert"></i></span><div><b>هشدار نرخ خطا در Webhook</b><p>payment.updated · ۳ تلاش ناموفق</p></div><time>۵ ساعت پیش</time></div>
          <div class="activity-item"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="user-plus"></i></span><div><b>عضو جدید دعوت شد</b><p>علی رضایی · نقش توسعه‌دهنده</p></div><time>دیروز</time></div>
        </div>
      </div>
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>دسترسی سریع</h2><p>کارهای پرتکرار شما</p></div></div>
        <div class="quick-actions">
          <a class="qa-btn" href="api-keys.html"><i data-icon="key-round"></i> ساخت کلید جدید</a>
          <a class="qa-btn" href="logs.html"><i data-icon="scroll-text"></i> بررسی گزارش‌ها</a>
          <a class="qa-btn" href="endpoints.html"><i data-icon="braces"></i> آزمایش Endpoint</a>
          <a class="qa-btn" href="billing.html"><i data-icon="credit-card"></i> مشاهده فاکتور</a>
        </div>
        <hr class="divider" style="margin:18px 0">
        <div class="flex-between mb-8"><span class="t-caption">سهمیه درخواست ماهانه</span><b class="t-caption fa-num">۳٫۴M / ۵M</b></div>
        <div class="progress"><i style="width:68%"></i></div>
        <div class="flex-between mt-16"><span class="t-caption">سهمیه باند</span><b class="t-caption fa-num">۲۸۰GB / 500GB</b></div>
        <div class="progress green"><i style="width:56%"></i></div>
      </div>
    </div>

    <div class="chart-card">
      <div class="chart-card-head"><div><h2>Endpointهای پرکاربرد</h2><p>۵ Endpoint برتر بر اساس تعداد درخواست</p></div><a class="link" style="font-size:var(--fs-caption)" href="endpoints.html">مدیریت Endpointها <i data-icon="arrow-left"></i></a></div>
      <div class="table-wrap" style="border:none;border-radius:0">
        <table class="table">
          <thead><tr><th>Endpoint</th><th>درخواست‌ها</th><th>نرخ موفقیت</th><th>تأخیر P50</th></tr></thead>
          <tbody>
            <tr><td><code class="inline text-code">GET /v1/users</code></td><td class="fa-num">۴۸٬۲۱۰</td><td><span class="badge badge-green">۹۹٫۹٪</span></td><td class="latency-cell">۸۸ms</td></tr>
            <tr><td><code class="inline text-code">POST /v1/payments</code></td><td class="fa-num">۲۹٬۴۴۰</td><td><span class="badge badge-green">۹۹٫۸٪</span></td><td class="latency-cell">۱۴۲ms</td></tr>
            <tr><td><code class="inline text-code">GET /v1/payments/:id</code></td><td class="fa-num">۲۱٬۱۲۰</td><td><span class="badge badge-amber">۹۸٫۹٪</span></td><td class="latency-cell">۱۱۶ms</td></tr>
            <tr><td><code class="inline text-code">POST /v1/files</code></td><td class="fa-num">۱۲٬۴۰۰</td><td><span class="badge badge-green">۹۹٫۵٪</span></td><td class="latency-cell">۲۸۰ms</td></tr>
            <tr><td><code class="inline text-code">GET /v1/projects</code></td><td class="fa-num">۸٬۹۹۰</td><td><span class="badge badge-green">۹۹٫۹٪</span></td><td class="latency-cell">۶۴ms</td></tr>
          </tbody>
        </table>
      </div>
    </div>
'''
    actions = f'<span id="jalaliToday" class="badge" style="font-weight:500"></span>' + daterange() + '<a class="btn btn-primary btn-sm" href="api-keys.html"><i data-icon="key-round"></i> کلید جدید</a>'
    return dash_page('نمای کلی', 'dashboard/index.html', 'سلام سارا 👋', 'نمای کلی فضای کاری ابرینو — آخرین به‌روزرسانی: چند لحظه پیش',
                     content, actions=actions, charts=True)
