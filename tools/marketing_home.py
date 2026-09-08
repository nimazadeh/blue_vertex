# -*- coding: utf-8 -*-
"""Blue Vertex — page: index.html (home)"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts

def code_js():
    return '''<pre class="line-numbers"><code class="language-javascript">// نصب SDK
import { BlueVertex } from '@bluevertex/sdk';

const bv = new BlueVertex({ apiKey: process.env.BV_API_KEY });

// ایجاد کاربر جدید
const { data } = await bv.users.create({
  name: 'سارا احمدی',
  email: 'sara@abrino.ir',
  role: 'developer',
});

console.log(data.id); // usr_8f2k1</code></pre>'''

def code_bash():
    return '''<pre class="line-numbers"><code class="language-bash">$ npm install @bluevertex/sdk

# یا با پایتون
$ pip install bluevertex

# اولین درخواست
$ curl https://api.bluevertex.ir/v1/users \\\\
  -H "Authorization: Bearer bv_live_••••••••"</code></pre>'''

def code_python():
    return '''<pre class="line-numbers"><code class="language-python">from bluevertex import BlueVertex

bv = BlueVertex(api_key="bv_live_...")

user = bv.users.create(
    name="سارا احمدی",
    email="sara@abrino.ir",
    role="developer",
)
print(user.id)  # usr_8f2k1</code></pre>'''

def build(prefix=''):
    p = prefix
    return head(
        'بلو ورتکس | پلتفرم توسعه‌دهنده فارسی برای API محصول شما',
        'بلو ورتکس؛ پلتفرم کامل توسعه‌دهنده به زبان فارسی — مستندات زنده، کنسول توسعه‌دهنده، مدیریت کلید API، تحلیل مصرف و گزارش درخواست، با تجربه‌ای در سطح استانداردهای جهانی.',
        p,
        extra_meta='<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"بلو ورتکس (Blue Vertex)","url":"https://bluevertex.ir","logo":"https://bluevertex.ir/assets/icons/favicon.svg","sameAs":["https://t.me/bluevertex_ir","https://github.com/bluevertex","https://eitaa.com/bluevertex_ir"]}</script><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"بلو ورتکس","url":"https://bluevertex.ir","inLanguage":"fa-IR"}</script>',
        canonical=p + 'index.html') + '''
<body class="noise">
<main id="top">
''' + navbar('active_home', p) + '''
<!-- ============ HERO ============ -->
<section class="hero">
  <div class="hero-bg bg-grid" aria-hidden="true">
    <div class="glow-1"></div><div class="glow-2"></div><div class="glow-3"></div>
  </div>
  <div class="container hero-content" style="position:relative">
    <span class="hero-badge" data-reveal><i data-icon="sparkles"></i> بلو ورتکس ۲٫۴ منتشر شد — با SDK پایتون</span>
    <h1 data-reveal>زیرساخت توسعه‌دهنده محصول شما،<br><span class="grad-text">تمام‌فارسی و یکپارچه</span></h1>
    <p class="hero-sub" data-reveal>بلو ورتکس هر آنچه برای عرضهٔ یک API حرفه‌ای نیاز دارید در یک پلتفرم گرد هم می‌آورد: مستندات زنده، کنسول توسعه‌دهنده، مدیریت کلید، تحلیل مصرف و گزارش درخواست — با تجربه‌ای در سطح استانداردهای جهانی، به زبان فارسی.</p>
    <div class="hero-cta" data-reveal>
      <a class="btn btn-primary btn-lg" href="auth/register.html">شروع رایگان <i data-icon="arrow-left"></i></a>
      <a class="btn btn-secondary btn-lg" href="docs/index.html">مشاهده مستندات</a>
    </div>
    <div class="hero-meta" data-reveal>
      <span><i data-icon="check-circle-2"></i> بدون نیاز به کارت بانکی</span>
      <span><i data-icon="check-circle-2"></i> راه‌اندازی در ۵ دقیقه</span>
      <span><i data-icon="check-circle-2"></i> آپ‌تایم ۹۹٫۹۸٪</span>
    </div>
  </div>

  <!-- Product preview -->
  <div class="container hero-visual" data-reveal>
    <div class="float-chip fc-1">
      <span class="icon-tile icon-tile-green"><i data-icon="check"></i></span>
      <span><b>HTTP 200</b><span>۴۸ میلی‌ثانیه · POST /v1/users</span></span>
    </div>
    <div class="float-chip fc-2">
      <span class="icon-tile icon-tile-blue"><i data-icon="trending-up"></i></span>
      <span><b>+۳۸٪ رشد مصرف</b><span>۳۰ روز گذشته</span></span>
    </div>
    <div class="window" role="img" aria-label="پیش‌نمایش پلتفرم بلو ورتکس">
      <div class="window-bar">
        <span class="window-dots"><i></i><i></i><i></i></span>
        <span class="window-title"><i data-icon="globe"></i> console.bluevertex.ir</span>
        <span class="badge badge-green" style="position:absolute;inset-inline-end:14px"><span class="dot"></span> production</span>
      </div>
      <div class="window-body">
        <aside class="window-side" aria-hidden="true">
          <span class="win-nav active"><i data-icon="layout-dashboard"></i> نمای کلی</span>
          <span class="win-nav"><i data-icon="key-round"></i> کلیدهای API</span>
          <span class="win-nav"><i data-icon="gauge"></i> مصرف</span>
          <span class="win-nav"><i data-icon="bar-chart-3"></i> تحلیل‌ها</span>
          <span class="win-nav"><i data-icon="scroll-text"></i> گزارش درخواست‌ها</span>
          <span class="win-nav"><i data-icon="braces"></i> Endpointها</span>
        </aside>
        <div class="win-main">
          <div class="win-stats">
            <div class="win-stat"><span>درخواست امروز</span><b class="fa-num">۱۲۴٬۵۸۰</b></div>
            <div class="win-stat"><span>نرخ موفقیت</span><b class="fa-num">۹۹٫۹۸٪</b></div>
            <div class="win-stat"><span>میانگین تأخیر</span><b class="fa-num">۱۴۸ms</b></div>
          </div>
          <div class="win-chart">
            <div class="legend"><span>درخواست‌های ۲۴ ساعت اخیر</span><span class="badge badge-blue">زنده</span></div>
            <div class="mini-chart-holder">
              <canvas data-chart data-chart-type="line" data-fill="1" data-no-rtl="1"
                data-labels='["۰","۳","۶","۹","۱۲","۱۵","۱۸","۲۱"]'
                data-values='[320,410,380,540,620,705,660,590]'
                data-colors='["rgb(59,130,246)"]' data-name="درخواست" data-unit="درخواست"></canvas>
            </div>
          </div>
          <div class="win-chart" style="margin-top:10px">
            <div class="legend"><span>آخرین فعالیت‌ها</span></div>
            <div style="display:flex;flex-direction:column;gap:8px;font-size:.68rem;color:var(--text-3)">
              <div class="flex-between"><span class="ltr">POST /v1/users</span><span class="badge badge-green">200</span></div>
              <div class="flex-between"><span class="ltr">GET /v1/projects</span><span class="badge badge-green">200</span></div>
              <div class="flex-between"><span class="ltr">GET /v1/analytics</span><span class="badge badge-amber">429</span></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ TRUST / LOGOS ============ -->
<section class="logo-strip">
  <div class="container">
    <p class="logos-title">مورد اعتماد تیم‌های فنی شرکت‌های پیشرو</p>
    <div class="logos-row">
      <span class="logo-item"><i data-icon="cloud"></i> ابرینو<span class="en">abrino</span></span>
      <span class="logo-item"><i data-icon="database"></i> داده‌پرداز<span class="en">dps</span></span>
      <span class="logo-item"><i data-icon="brain-circuit"></i> هوشیار<span class="en">hooshyar</span></span>
      <span class="logo-item"><i data-icon="layers"></i> فراز<span class="en">faraz</span></span>
      <span class="logo-item"><i data-icon="shield"></i> فینوا<span class="en">finva</span></span>
      <span class="logo-item"><i data-icon="shopping-bag"></i> بازارینو<span class="en">bazarino</span></span>
    </div>
  </div>
</section>

<!-- ============ DEVELOPER EXPERIENCE ============ -->
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile"><i data-icon="terminal"></i></span>
      <h2>تجربه توسعه‌دهنده‌ای که تیم شما<br>همان‌روز عاشقش می‌شود</h2>
      <p>هر جزئیات — از نمونه‌کد تا کنسول — برای این طراحی شده که توسعه‌دهندگان فارسی محصول شما سریع‌تر و با اعتمادبه‌نفس بیشتر بسازند.</p>
    </div>

    <div class="feature-row" data-reveal>
      <div class="f-body">
        <span class="sec-eyebrow">۰۱ · مستندات زنده</span>
        <h3>مستنداتی که همیشه با کد شما هم‌قدم‌اند</h3>
        <p>مستندات بلو ورتکس از اسکیمای API شما ساخته می‌شود؛ نمونه‌کد، پارامترها و مدل‌های پاسخ همیشه به‌روز می‌مانند. جستجوی فارسی، میان‌بر صفحه‌کلید و کپی با یک کلیک — همه در چند ثانیه.</p>
        <ul class="feature-list">
          <li><i data-icon="check-circle-2"></i> تولید خودکار نمونه‌کد به ۵ زبان (cURL، JavaScript، Python، PHP، Go)</li>
          <li><i data-icon="check-circle-2"></i> جستجوی هوشمند فارسی با پشتیبانی از جستجوهای اخیر</li>
          <li><i data-icon="check-circle-2"></i> مرجع API تعاملی با نمایش درخواست و پاسخ واقعی</li>
        </ul>
      </div>
      <div>
        <div class="code-window" dir="ltr" style="text-align:left">
          <div class="cw-head">
            <span class="window-dots"><i></i><i></i><i></i></span>
            <div class="cw-tabs">
              <button class="cw-tab active">bash</button><button class="cw-tab">js</button><button class="cw-tab">py</button>
            </div>
          </div>
          <div class="cw-body">
            <div class="cw-pane active">''' + code_bash() + '''</div>
            <div class="cw-pane" style="display:none">''' + code_js() + '''</div>
            <div class="cw-pane" style="display:none">''' + code_python() + '''</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feature-row rev" data-reveal>
      <div>
        <div class="window" style="box-shadow:var(--shadow-lg)">
          <div class="window-bar">
            <span class="window-dots"><i></i><i></i><i></i></span>
            <span class="window-title"><i data-icon="bar-chart-3"></i> تحلیل بلادرنگ</span>
          </div>
          <div class="win-main" style="padding:18px">
            <div class="win-stats" style="grid-template-columns:repeat(3,1fr)">
              <div class="win-stat"><span>موفقیت</span><b class="fa-num">۹۹٫۹۸٪</b></div>
              <div class="win-stat"><span>خطای ۴xx</span><b class="fa-num">۰٫۰۴٪</b></div>
              <div class="win-stat"><span>خطای ۵xx</span><b class="fa-num">۰٫۰۱٪</b></div>
            </div>
            <div class="win-chart" style="margin-top:10px">
              <div class="legend"><span>تأخیر صدک‌ها (P50 / P95 / P99)</span></div>
              <div class="mini-chart-holder" style="height:120px">
                <canvas data-chart data-chart-type="line" data-fill="1" data-no-rtl="1"
                  data-labels='["۱","۲","۳","۴","۵","۶","۷","۸","۹","۱۰","۱۱","۱۲"]'
                  data-values='[42,45,41,48,52,50,55,58,54,62,60,66]'
                  data-colors='["rgb(56,189,248)"]' data-name="تأخیر P50" data-unit="ms"></canvas>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="f-body">
        <span class="sec-eyebrow">۰۲ · تحلیل بلادرنگ</span>
        <h3>هر درخواست، هر خطا — زیر ذره‌بین</h3>
        <p>از نرخ موفقیت تا صدک‌های تأخیر، همه‌چیز بلادرنگ و با تاریخ شمسی روی داشبورد شماست. مشکلات را پیش از آن‌که مشتری‌تان ببیند پیدا کنید.</p>
        <ul class="feature-list">
          <li><i data-icon="check-circle-2"></i> فیلتر بر اساس Endpoint، کد وضعیت و محیط (تولید/آزمایش)</li>
          <li><i data-icon="check-circle-2"></i> جزئیات کامل هر درخواست: هدرها، بدنه، زمان‌بندی و آدرس IP</li>
          <li><i data-icon="check-circle-2"></i> هشدار خودکار برای نرخ خطای غیرعادی</li>
        </ul>
      </div>
    </div>

    <div class="feature-row" data-reveal>
      <div class="f-body">
        <span class="sec-eyebrow">۰۳ · کنسول توسعه‌دهنده</span>
        <h3>داشبوردی که توسعه‌دهنده را در خانه خودش حس می‌کند</h3>
        <p>کلیدهای API با دسترسی‌های دقیق، سهمیه مصرف، مدیریت تیم و صورتحساب شفاف — همه در یک کنسول فارسی و روان، با حالت‌های خالی و خطای حرفه‌ای.</p>
        <ul class="feature-list">
          <li><i data-icon="check-circle-2"></i> کلید با دسترسی‌بندی (Scopes) و محیط مجزا</li>
          <li><i data-icon="check-circle-2"></i> مرورگر تعاملی API با شبیه‌سازی درخواست</li>
          <li><i data-icon="check-circle-2"></i> نقش‌های تیمی: مالک، مدیر، توسعه‌دهنده، بیننده</li>
        </ul>
        <a class="link mt-16" href="dashboard/index.html">ورود به دموی داشبورد <i data-icon="arrow-left"></i></a>
      </div>
      <div>
        <div class="window">
          <div class="window-bar">
            <span class="window-dots"><i></i><i></i><i></i></span>
            <span class="window-title"><i data-icon="key-round"></i> کلیدهای API</span>
            <span class="badge badge-blue">۲ فعال</span>
          </div>
          <div class="win-main" style="padding:18px">
            <div style="display:flex;flex-direction:column;gap:10px">
              <div class="flex-between" style="border:1px solid var(--border);border-radius:10px;padding:11px 13px">
                <span style="font-size:.75rem;font-weight:700">تولید — اصلی</span>
                <code class="ltr" style="font-size:.68rem;color:var(--text-3)">bv_live_•••••••••</code>
                <span class="badge badge-green">فعال</span>
              </div>
              <div class="flex-between" style="border:1px solid var(--border);border-radius:10px;padding:11px 13px">
                <span style="font-size:.75rem;font-weight:700">آزمایش — توسعه</span>
                <code class="ltr" style="font-size:.68rem;color:var(--text-3)">bv_test_•••••••••</code>
                <span class="badge badge-green">فعال</span>
              </div>
              <div class="flex-between" style="border:1px solid var(--border);border-radius:10px;padding:11px 13px;opacity:.55">
                <span style="font-size:.75rem;font-weight:700">تولید — قدیمی</span>
                <code class="ltr" style="font-size:.68rem;color:var(--text-3)">bv_live_•••••••••</code>
                <span class="badge">باطل‌شده</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ API / CODE SECTION ============ -->
<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-green"><i data-icon="braces"></i></span>
      <h2>یک API مدرن، با تمام جزئیات حرفه‌ای</h2>
      <p>نسخه‌بندی روشن، خطاهای معنادار فارسی، محدودیت نرخ شفاف و سازگاری کامل با RTL — API شما مثل یک محصول درجه‌یک به نظر می‌رسد.</p>
    </div>
    <div class="grid-2" style="align-items:stretch" data-reveal>
      <div>
        <div class="endpoint-card">
          <div class="ep-line">
            <span class="method method-post">POST</span>
            <span class="ep-url">https://api.bluevertex.ir/v1/users</span>
          </div>
          <div class="ep-flags">
            <span class="badge badge-blue">احراز هویت: Bearer</span>
            <span class="badge">نرخ: ۱۰۰ در دقیقه</span>
            <span class="badge">نسخه v1</span>
          </div>
        </div>
        <div class="code-window" dir="ltr" style="text-align:left">
          <div class="cw-head">
            <span class="window-dots"><i></i><i></i><i></i></span>
            <div class="cw-tabs">
              <button class="cw-tab active">cURL</button><button class="cw-tab">JavaScript</button><button class="cw-tab">Python</button>
            </div>
          </div>
          <div class="cw-body">
            <div class="cw-pane active">''' + code_bash() + '''</div>
            <div class="cw-pane" style="display:none">''' + code_js() + '''</div>
            <div class="cw-pane" style="display:none">''' + code_python() + '''</div>
          </div>
        </div>
      </div>
      <div>
        <div class="window" style="height:100%">
          <div class="window-bar">
            <span class="window-dots"><i></i><i></i><i></i></span>
            <span class="window-title"><i data-icon="server"></i> پاسخ سرور</span>
          </div>
          <div style="direction:ltr;text-align:left">
            <pre class="line-numbers" style="margin:0;background:transparent"><code class="language-json">{
  "data": {
    "id": "usr_8f2k1",
    "name": "سارا احمدی",
    "email": "sara@abrino.ir",
    "role": "developer",
    "created_at": "2026-08-30T10:14:22Z"
  },
  "meta": {
    "request_id": "req_9d41c7",
    "latency_ms": 48
  }
}</code></pre>
          </div>
          <div class="flex" style="gap:8px;padding:12px 18px;border-top:1px solid var(--border)">
            <span class="badge badge-green"><span class="dot"></span> 200 OK</span>
            <span class="badge">۴۸ms</span>
            <span class="badge" style="margin-inline-start:auto">content-type: application/json</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ ARCHITECTURE ============ -->
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-violet"><i data-icon="network"></i></span>
      <h2>معماری مقیاس‌پذیر، از همان روز اول</h2>
      <p>از لبه (Edge) تا پایگاه داده، هر لایه برای بارهای سنگین و رشد ناگهانی طراحی شده است.</p>
    </div>
    <div class="card card-pad" data-reveal>
      <div class="arch-flow">
        <div class="arch-node">
          <span class="icon-tile icon-tile-gray"><i data-icon="smartphone"></i></span><span class="t-caption">کلاینت‌ها</span>
        </div>
        <i class="arch-arrow" data-icon="arrow-left" aria-hidden="true"></i>
        <div class="arch-node">
          <span class="icon-tile"><i data-icon="globe"></i></span><span class="t-caption">لبه و CDN</span>
        </div>
        <i class="arch-arrow" data-icon="arrow-left" aria-hidden="true"></i>
        <div class="arch-node">
          <span class="icon-tile icon-tile-green"><i data-icon="shield-check"></i></span><span class="t-caption">احراز هویت و نرخ</span>
        </div>
        <i class="arch-arrow" data-icon="arrow-left" aria-hidden="true"></i>
        <div class="arch-node">
          <span class="icon-tile icon-tile-amber"><i data-icon="cpu"></i></span><span class="t-caption">هسته API</span>
        </div>
        <i class="arch-arrow" data-icon="arrow-left" aria-hidden="true"></i>
        <div class="arch-node">
          <span class="icon-tile icon-tile-red"><i data-icon="database"></i></span><span class="t-caption">داده و صف</span>
        </div>
      </div>
      <hr class="divider" style="margin:26px 0 20px">
      <div class="grid-auto">
        <div class="flex" style="gap:10px"><i data-icon="zap" style="color:var(--electric)"></i><span class="t-sm">توزیع خودکار بار بین چند منطقه</span></div>
        <div class="flex" style="gap:10px"><i data-icon="refresh-cw" style="color:var(--electric)"></i><span class="t-sm">اختصاص منابع خودکار در پیک ترافیک</span></div>
        <div class="flex" style="gap:10px"><i data-icon="git-branch" style="color:var(--electric)"></i><span class="t-sm">کاناری‌ریلیز و بازگشت آنی نسخه</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ============ SECURITY ============ -->
<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="grid-2" style="align-items:center;gap:56px">
      <div data-reveal>
        <span class="sec-eyebrow">امنیت در عمق</span>
        <h2 class="t-h2" style="margin-bottom:14px">امنیتی که تیم امنیت شما<br>تأیید می‌کند</h2>
        <p class="t-body-lg" style="color:var(--text-2);line-height:2;margin-bottom:28px">امنیت بلو ورتکس یک لایه نیست؛ یک سیستم است. از کلیدهای با دسترسی‌بندی تا گزارش ممیزی کامل، همه‌چیز برای محیط‌های سازمانی جدی طراحی شده است.</p>
        <div class="sec-badges" style="display:flex;gap:12px;flex-wrap:wrap">
          <span class="badge badge-blue"><i data-icon="lock" style="width:12px;height:12px"></i> TLS 1.3</span>
          <span class="badge badge-green"><i data-icon="shield" style="width:12px;height:12px"></i> رمزنگاری AES-256</span>
          <span class="badge badge-violet"><i data-icon="fingerprint" style="width:12px;height:12px"></i> احراز دومرحله‌ای</span>
        </div>
      </div>
      <div class="grid grid-2" style="gap:14px" data-reveal>
        <div class="card card-pad" style="padding:20px">
          <span class="icon-tile icon-tile-sm icon-tile-green mb-16"><i data-icon="key-round"></i></span>
          <h3 class="t-h4 mb-8">دسترسی‌بندی کلیدها</h3>
          <p class="t-caption">هر کلید دقیقاً همان دسترسی‌هایی را دارد که به آن نیاز دارد؛ نه بیشتر.</p>
        </div>
        <div class="card card-pad" style="padding:20px">
          <span class="icon-tile icon-tile-sm icon-tile-amber mb-16"><i data-icon="scroll-text"></i></span>
          <h3 class="t-h4 mb-8">گزارش ممیزی</h3>
          <p class="t-caption">هر تغییر حساس با زمان، کاربر و IP ثبت می‌شود.</p>
        </div>
        <div class="card card-pad" style="padding:20px">
          <span class="icon-tile icon-tile-sm icon-tile-blue mb-16"><i data-icon="webhook"></i></span>
          <h3 class="t-h4 mb-8">Webhook امضاشده</h3>
          <p class="t-caption">امضای HMAC با چرخش کلید — تحویل تضمینی با تلاش مجدد.</p>
        </div>
        <div class="card card-pad" style="padding:20px">
          <span class="icon-tile icon-tile-sm icon-tile-red mb-16"><i data-icon="bell-ring"></i></span>
          <h3 class="t-h4 mb-8">هشدار نفوذ</h3>
          <p class="t-caption">تشخیص فعالیت غیرعادی و هشدار آنی به تیم امنیت.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ ANALYTICS PREVIEW ============ -->
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-cyan"><i data-icon="activity"></i></span>
      <h2>تحلیل‌هایی که به سؤال‌های واقعی جواب می‌دهند</h2>
      <p>نه نمودارهای تزئینی. حجم درخواست، نرخ خطا، تأخیر و پرکاربردترین Endpointهای شما — قابل‌فیلتر با تاریخ شمسی.</p>
    </div>
    <div class="card card-pad" data-reveal style="padding:28px">
      <div class="flex-between mb-16" style="flex-wrap:wrap">
        <div>
          <h3 class="t-h4">حجم درخواست — ۳۰ روز اخیر</h3>
          <p class="t-caption mt-8">مجموع ۱۲۴٫۵۸۰ درخواست · رشد ۳۴٫۵٪</p>
        </div>
        <div class="flex gap-8">
          <span class="badge badge-green">+۳۴٫۵٪ رشد</span>
          <span class="badge">به‌روزرسانی: ۱۰ ثانیه پیش</span>
        </div>
      </div>
      <div class="chart-holder" style="height:300px">
        <canvas data-chart data-chart-type="line" data-fill="1" data-no-rtl="1"
          data-labels='["۱","۵","۹","۱۳","۱۷","۲۱","۲۵","۲۹"]'
          data-values='[3200,4150,3800,5400,6200,7050,6600,8200]'
          data-colors='["rgb(59,130,246)"]' data-name="درخواست" data-unit="درخواست"></canvas>
      </div>
    </div>
  </div>
</section>

<!-- ============ FEATURE BENTO ============ -->
<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container-wide">
    <div class="sec-head" data-reveal>
      <span class="icon-tile"><i data-icon="box"></i></span>
      <h2>همه‌چیز در یک پلتفرم</h2>
      <p>به‌جای ترکیب ده ابزار ناهماهنگ، یک زیرساخت منسجم تحویل بگیرید.</p>
    </div>
    <div class="bento">
      <div class="bento-item" data-reveal>
        <span class="icon-tile"><i data-icon="shield-check"></i></span>
        <h3>احراز هویت حرفه‌ای</h3>
        <p>کلیدهای API با Scopes، نشست‌های OAuth و امکان چرخش بدون توقف سرویس.</p>
      </div>
      <div class="bento-item" data-reveal>
        <span class="icon-tile icon-tile-green"><i data-icon="webhook"></i></span>
        <h3>Webhookهای قابل‌اعتماد</h3>
        <p>تحویل تضمینی با تلاش مجدد تصاعدی، امضای HMAC و صف پیام داخلی.</p>
      </div>
      <div class="bento-item" data-reveal>
        <span class="icon-tile icon-tile-amber"><i data-icon="line-chart"></i></span>
        <h3>تحلیل و مانیتورینگ</h3>
        <p>نرخ موفقیت، صدک تأخیر، توزیع جغرافیایی و مقایسه Endpointها.</p>
      </div>
      <div class="bento-item span-3" data-reveal>
        <span class="icon-tile icon-tile-violet"><i data-icon="users"></i></span>
        <h3>تیم و سطوح دسترسی</h3>
        <p>مالک، مدیر، توسعه‌دهنده و بیننده — با دعوت‌نامه، نقش‌ها و گزارش فعالیت. برای تیم‌های ۲ تا ۲۰۰ نفره.</p>
        <div class="bento-visual flex gap-8">
          <span class="avatar avatar-stack" style="display:flex"><span class="avatar">س</span><span class="avatar" style="background:linear-gradient(135deg,#34D399,#065F46)">ع</span><span class="avatar" style="background:linear-gradient(135deg,#A78BFA,#4C1D95)">م</span><span class="avatar" style="background:linear-gradient(135deg,#FBBF24,#92400E)">+۴</span></span>
          <span class="badge">۷ عضو فعال</span>
          <span class="badge badge-blue">۳ نقش</span>
        </div>
      </div>
      <div class="bento-item span-3" data-reveal>
        <span class="icon-tile icon-tile-cyan"><i data-icon="package"></i></span>
        <h3>SDKهای بومی فارسی</h3>
        <p>جاوااسکریپت، TypeScript، پایتون، PHP و گو — با تایپ کامل، نوار پیشرفت و مستندات داخلی. ارتقا با یک فرمان.</p>
        <div class="bento-visual">
          <div class="code-window" dir="ltr" style="text-align:left">
            <div class="cw-head"><span class="cw-tabs"><span class="cw-tab active">npm</span><span class="cw-tab">pip</span><span class="cw-tab">go get</span></span></div>
            <pre style="margin:0;padding:12px 16px;font-size:.75rem"><code>npm install @bluevertex/sdk</code></pre>
          </div>
        </div>
      </div>
      <div class="bento-item span-3" data-reveal>
        <span class="icon-tile icon-tile-red"><i data-icon="gauge"></i></span>
        <h3>سهمیه‌بندی شفاف</h3>
        <p>محدودیت نرخ در هر Endpoint، هشدار پیش از رسیدن به سقف و گزارش مصرف به تومان.</p>
        <div class="bento-visual">
          <div class="progress"><i style="width:78%"></i></div>
          <div class="flex-between mt-8"><span class="t-caption">سهمیه ماهانه</span><span class="t-caption fa-num">۷۸٪ مصرف‌شده</span></div>
        </div>
      </div>
      <div class="bento-item span-3" data-reveal>
        <span class="icon-tile"><i data-icon="credit-card"></i></span>
        <h3>صورتحساب به تومان</h3>
        <p>پرداخت ریالی با شفافیت کامل: فاکتور دقیق، تاریخ شمسی و فیلتر بر اساس که مصرف کرده است.</p>
        <div class="bento-visual grid grid-3" style="gap:8px">
          <div class="win-stat"><span>ماه جاری</span><b class="fa-num">۹۹۰٬۰۰۰</b></div>
          <div class="win-stat"><span>پیش‌بینی</span><b class="fa-num">۱٬۱۲۰٬۰۰۰</b></div>
          <div class="win-stat"><span>سرانه هر کلید</span><b class="fa-num">۲۴۸٬۰۰۰</b></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ INTEGRATIONS ============ -->
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-green"><i data-icon="plug"></i></span>
      <h2>با ابزارهای تیم شما می‌سازد</h2>
      <p>نه جزیرهٔ جدا. بلو ورتکس در جریان کار روزانه شما می‌نشیند.</p>
    </div>
    <div class="integration-grid" data-reveal>
      <span class="integration-card"><i data-icon="braces"></i>REST</span>
      <span class="integration-card"><i data-icon="terminal"></i>cURL</span>
      <span class="integration-card"><i data-icon="git-branch"></i>GitHub</span>
      <span class="integration-card"><i data-icon="gitlab"></i>GitLab</span>
      <span class="integration-card"><i data-icon="container"></i>Docker</span>
      <span class="integration-card"><i data-icon="database"></i>PostgreSQL</span>
      <span class="integration-card"><i data-icon="server-cog"></i>Kafka</span>
      <span class="integration-card"><i data-icon="webhook"></i>Webhooks</span>
      <span class="integration-card"><i data-icon="web"></i>GraphQL</span>
      <span class="integration-card"><i data-icon="radio"></i>SSE</span>
      <span class="integration-card"><i data-icon="message-square-code"></i>Postman</span>
      <span class="integration-card"><i data-icon="zap"></i>CI/CD</span>
    </div>
  </div>
</section>

<!-- ============ TESTIMONIALS ============ -->
<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-amber"><i data-icon="quote"></i></span>
      <h2>تیم‌های فنی درباره ما چه می‌گویند</h2>
      <p>شرکت‌های نمونه (دمو) که مسیر ساخت API خود را با بلو ورتکس کوتاه‌تر کردند.</p>
    </div>
    <div class="testi-grid">
      <div class="testi-card" data-reveal>
        <div class="testi-stars"><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i></div>
        <p class="testi-quote">مستندات محصول ما قبلاً یک فایل PDF بود که همیشه قدیمی می‌ماند. با بلو ورتکس، مستندات API ما همان‌روز لانچ شد و تیکت‌های پشتیبانی فنی ۴۰٪ کم شد.</p>
        <div class="testi-author">
          <span class="avatar">س</span>
          <span><b>سارا احمدی</b><span>مدیر فنی · ابرینو (دمو)</span></span>
        </div>
      </div>
      <div class="testi-card" data-reveal>
        <div class="testi-stars"><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i></div>
        <p class="testi-quote">گزارش درخواست‌ها همه‌چیز را عوض کرد. الان سه دقیقه بعد از دیپلوی، می‌بینیم کدام Endpoint کند شده — قبل از این‌که مشتری بگوید.</p>
        <div class="testi-author">
          <span class="avatar" style="background:linear-gradient(135deg,#34D399,#065F46)">ع</span>
          <span><b>علی رضایی</b><span>بنیان‌گذار · هوشیار (دمو)</span></span>
        </div>
      </div>
      <div class="testi-card" data-reveal>
        <div class="testi-stars"><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i><i data-icon="star"></i></div>
        <p class="testi-quote">برای اولین بار یک داشبورد توسعه‌دهنده کاملاً فارسی دیدم که نه ترجمه است و نه تقلید. تیم پشتیبانی ما بدون آموزش از آن استفاده کرد.</p>
        <div class="testi-author">
          <span class="avatar" style="background:linear-gradient(135deg,#A78BFA,#4C1D95)">م</span>
          <span><b>مریم کریمی</b><span>مدیر محصول · داده‌پرداز (دمو)</span></span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ============ PRICING PREVIEW ============ -->
<section class="section">
  <div class="container">
    <div class="sec-head" data-reveal>
      <span class="icon-tile"><i data-icon="credit-card"></i></span>
      <h2>قیمت‌گذاری شفاف، به تومان</h2>
      <p>از رایگان برای شروع تا سازمانی برای بارهای سنگین — بدون هزینه پنهان.</p>
    </div>
    <div class="pricing-grid">
      <div class="price-card" data-reveal>
        <span class="price-name"><i data-icon="rocket"></i>رایگان</span>
        <div class="price-amount"><b>۰ تومان</b><span>ماهانه</span></div>
        <p class="price-desc">برای پروژه‌های شخصی و شروع سریع</p>
        <ul class="price-feats">
          <li><i data-icon="check"></i>۱۰ هزار درخواست در ماه</li>
          <li><i data-icon="check"></i>۲ کلید API</li>
          <li><i data-icon="check"></i>۱ عضو تیم</li>
          <li><i data-icon="check"></i>مستندات و مرجع API</li>
          <li class="muted"><i data-icon="x"></i>گزارش درخواست‌های ۳۰ روزه</li>
        </ul>
        <a class="btn btn-outline btn-block" href="auth/register.html">شروع رایگان</a>
      </div>
      <div class="price-card popular" data-reveal>
        <span class="popular-tag">محبوب‌ترین</span>
        <span class="price-name"><i data-icon="zap"></i>توسعه‌دهنده</span>
        <div class="price-amount"><b data-monthly="990000" data-annual="792000">۹۹۰٬۰۰۰ تومان</b></div>
        <p class="price-desc">برای تیم‌های در حال رشد و محصولات جدی</p>
        <ul class="price-feats">
          <li><i data-icon="check"></i>۵۰۰ هزار درخواست در ماه</li>
          <li><i data-icon="check"></i>کلید نامحدود + Scopes</li>
          <li><i data-icon="check"></i>تا ۵ عضو تیم</li>
          <li><i data-icon="check"></i>گزارش درخواست ۳۰ روزه</li>
          <li><i data-icon="check"></i>پشتیبانی ۲۴/۷ تیمی</li>
        </ul>
        <a class="btn btn-primary btn-block" href="auth/register.html">شروع ۱۴ روز رایگان</a>
      </div>
      <div class="price-card" data-reveal>
        <span class="price-name"><i data-icon="building-2"></i>رشد</span>
        <div class="price-amount"><b>۳٬۹۰۰٬۰۰۰ تومان</b><span>ماهانه</span></div>
        <p class="price-desc">برای شرکت‌ها و محصولات پرترافیک</p>
        <ul class="price-feats">
          <li><i data-icon="check"></i>۵ میلیون درخواست در ماه</li>
          <li><i data-icon="check"></i>فضای کاری چندگانه</li>
          <li><i data-icon="check"></i>تیم نامحدود + نقش‌ها</li>
          <li><i data-icon="check"></i>SLA ۹۹٫۹٪ و پشتیبانی اختصاصی</li>
          <li><i data-icon="check"></i>گزارش ممیزی کامل</li>
        </ul>
        <a class="btn btn-outline btn-block" href="auth/register.html">انتخاب پلن رشد</a>
      </div>
    </div>
    <div class="text-center mt-32" data-reveal>
      <a class="link" href="pages/pricing.html">مقایسه کامل همه پلن‌ها <i data-icon="arrow-left"></i></a>
    </div>
  </div>
</section>

<!-- ============ FAQ ============ -->
<section class="section" style="border-block:1px solid var(--border);background:var(--bg-elev)">
  <div class="container faq-wrap">
    <div class="sec-head" data-reveal>
      <span class="icon-tile icon-tile-cyan"><i data-icon="help-circle"></i></span>
      <h2>سوالات متداول</h2>
    </div>
    <div data-reveal>
      <div class="accordion open" data-acc><button class="acc-head">بلو ورتکس دقیقاً چه محصولی است؟<i data-icon="chevron-down"></i></button><div class="acc-body" style="max-height:200px"><div class="acc-inner">بلو ورتکس یک پلتفرم کامل توسعه‌دهنده است: مستندات API، کنسول مدیریت کلید و مصرف، تحلیل بلادرنگ، گزارش درخواست‌ها، مدیریت تیم و صورتحساب — همه در یک محصول فارسی، بدون نیاز به ترکیب چند ابزار.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">آیا برای شروع به کارت اعتباری نیاز است؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">خیر. پلن رایگان بدون هیچ کارت بانکی فعال می‌شود و ۱۰ هزار درخواست ماهانه در اختیار شماست. ارتقای پلن هم کاملاً به تومان و با روش‌های پرداخت داخلی انجام می‌شود.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">مستندات API چگونه تولید می‌شود؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">مستندات از اسکیمای OpenAPI شما به‌صورت خودکار ساخته و به‌روز می‌شود. نمونه‌کد به زبان‌های مختلف، پارامترها، مدل‌های خطا و نمونه پاسخ به‌صورت زنده از همان اسکیما تولید می‌شوند.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">آیا گزارش درخواست‌ها محدودیت دارد؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">در پلن رایگان گزارش ۷ روزه، در پلن توسعه‌دهنده ۳۰ روزه و در پلن‌های رشد و سازمانی ۹۰ روزه نگهداری می‌شود. فیلترها و جزئیات کامل درخواست در همه پلن‌ها فعال است.</div></div></div>
      <div class="accordion" data-acc><button class="acc-head">چطور می‌توانم پلن را تغییر بدهم؟<i data-icon="chevron-down"></i></button><div class="acc-body"><div class="acc-inner">از داشبورد، بخش «صورتحساب»، پلن جدید را انتخاب کنید. تغییرات بلافاصله اعمال و مابه‌التفاوت به‌صورت روزشمار محاسبه می‌شود. امکان بازگشت به پلن پایین‌تر در پایان دوره وجود دارد.</div></div></div>
    </div>
  </div>
</section>

<!-- ============ FINAL CTA ============ -->
<section class="section">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>همین امروز اولین درخواست API خود را ارسال کنید</h2>
      <p>در کمتر از ۵ دقیقه، پلتفرم توسعه‌دهنده محصول شما به زبان فارسی راه می‌افتد. بدون هزینه، بدون کارت بانکی، بدون پیچیدگی.</p>
      <div class="hero-cta">
        <a class="btn btn-primary btn-lg" href="auth/register.html">ایجاد حساب رایگان</a>
        <a class="btn btn-outline btn-lg" href="docs/getting-started.html">مطالعه شروع سریع</a>
      </div>
      <div class="hero-meta" style="margin-top:24px">
        <span><i data-icon="clock"></i> راه‌اندازی: ۵ دقیقه</span>
        <span><i data-icon="headphones"></i> پشتیبانی فارسی ۲۴/۷</span>
      </div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p, prism=True, charts=True) + '''
<!-- demo: marketing code-window tabs -->
<script>
(function(){
  document.querySelectorAll('.code-window').forEach(function(win){
    var tabs = win.querySelectorAll('.cw-tab');
    var panes = win.querySelectorAll('.cw-pane');
    tabs.forEach(function(t, i){
      t.addEventListener('click', function(){
        tabs.forEach(function(x){ x.classList.remove('active'); });
        panes.forEach(function(x){ x.style.display = 'none'; });
        t.classList.add('active');
        if (panes[i]) panes[i].style.display = '';
      });
    });
  });
})();
</script>
</body>
</html>'''
