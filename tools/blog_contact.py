# -*- coding: utf-8 -*-
"""Blue Vertex — contact + blog + article"""

from chrome import head, navbar, footer, palette, TOAST_REGION, scripts

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

# ================================================================ CONTACT
def build_contact(prefix=''):
    p = prefix
    return head(
        'تماس با ما | بلو استودیو',
        'با تیم بلو استودیو در تماس باشید؛ مشاوره فنی رایگان، پشتیبانی فارسی و پاسخ‌گویی در کمتر از ۲۴ ساعت.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_contact', p) + page_hero(
        crumb(p, 'تماس با ما'),
        'گفتگو با <span class="grad-text">تیم بلو استودیو</span>',
        'سؤال فنی دارید؟ به پلن سازمانی فکر می‌کنید؟ فرم را پر کنید — در کمتر از ۲۴ ساعت پاسخ می‌گیرید.') + '''
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info-card" data-reveal>
        <span class="sec-eyebrow">راه‌های ارتباطی</span>
        <h2 class="t-h3 mb-24">مستقیم و بدون واسطه</h2>
        <div class="contact-line"><span class="icon-tile icon-tile-sm"><i data-icon="mail"></i></span><div><b>پست الکترونیک</b> <span class="contact-value ltr" dir="ltr">hello@bluevertex.ir</span></div></div>
        <div class="contact-line"><span class="icon-tile icon-tile-sm icon-tile-green"><i data-icon="phone"></i></span><div><b>تلفن پشتیبانی</b> <span class="contact-value ltr" dir="ltr">021-91001234</span></div></div>
        <div class="contact-line"><span class="icon-tile icon-tile-sm icon-tile-amber"><i data-icon="map-pin"></i></span><div><b>دفتر مرکزی</b> <span class="contact-value">تهران، خیابان ولیعصر، کوچه نور، پلاک ۱۲، طبقه سوم</span></div></div>
        <div class="contact-line"><span class="icon-tile icon-tile-sm icon-tile-violet"><i data-icon="clock"></i></span><div><b>ساعات پاسخ‌گویی</b> <span class="contact-value">شنبه تا چهارشنبه، ۹ تا ۱۸</span></div></div>
        <div class="mt-32">
          <b class="t-sm">پیام‌رسان‌ها</b>
          <div class="flex gap-8 mt-16">
            <a class="btn btn-secondary btn-sm" href="https://t.me/bluevertex_ir" target="_blank" rel="noopener"><i data-icon="send"></i>تلگرام</a>
            <a class="btn btn-secondary btn-sm" href="https://eitaa.com/bluevertex_ir" target="_blank" rel="noopener"><i data-icon="message-circle"></i>ایتا</a>
            <a class="btn btn-secondary btn-sm" href="https://github.com/bluevertex" target="_blank" rel="noopener"><i data-icon="github"></i>گیت‌هاب</a>
          </div>
        </div>
      </div>

      <div class="card card-pad" style="padding:32px" data-reveal>
        <h2 class="t-h3 mb-8">ارسال پیام</h2>
        <p class="t-caption mb-24">فیلدهای ستاره‌دار الزامی هستند. پاسخ از طریق ایمیل یا شماره شما ارسال می‌شود.</p>

        <div class="auth-success-box" data-form-success style="display:none">
          <i data-icon="check-circle-2"></i>
          <div><b>پیام شما با موفقیت ارسال شد.</b><br>تیم بلو استودیو در کمتر از ۲۴ ساعت کاری با شما تماس می‌گیرد. کد پیگیری: <code class="ltr text-electric">tkt-4821</code></div>
        </div>

        <form data-form novalidate data-success-toast="none" data-success-hide="root">
          <div class="grid-2" style="gap:18px">
            <div class="field">
              <label class="field-label" for="cName">نام و نام خانوادگی <span class="req">*</span></label>
              <input class="input" id="cName" name="name" type="text" placeholder="مثلاً: سارا احمدی" required>
              <span class="field-error"></span>
            </div>
            <div class="field">
              <label class="field-label" for="cEmail">ایمیل <span class="req">*</span></label>
              <input class="input" id="cEmail" name="email" type="email" placeholder="you@company.ir" required>
              <span class="field-error"></span>
            </div>
            <div class="field">
              <label class="field-label" for="cMobile">شماره موبایل <span class="req">*</span></label>
              <input class="input" id="cMobile" name="phone" type="tel" placeholder="۰۹۱۲ ۰۰۰ ۰۰۰۰" required>
              <span class="field-error"></span>
            </div>
            <div class="field">
              <label class="field-label" for="cCompany">شرکت</label>
              <input class="input" id="cCompany" name="company" type="text" placeholder="نام شرکت یا تیم شما">
              <span class="field-error"></span>
            </div>
            <div class="field" style="grid-column:1/-1">
              <label class="field-label" for="cSubject">موضوع <span class="req">*</span></label>
              <select class="select" id="cSubject" name="subject" required>
                <option value="">انتخاب کنید…</option>
                <option>مشاوره پیش از خرید</option>
                <option>پشتیبانی فنی</option>
                <option>پلن سازمانی و قرارداد</option>
                <option>گزارش خطا</option>
                <option>همکاری و استخدام</option>
                <option>سایر</option>
              </select>
              <span class="field-error"></span>
            </div>
            <div class="field" style="grid-column:1/-1">
              <label class="field-label" for="cMessage">پیام <span class="req">*</span></label>
              <textarea class="textarea" id="cMessage" name="message" placeholder="پیام خود را بنویسید…" minlength="10" required></textarea>
              <span class="field-error"></span>
              <span class="field-hint">حداقل ۱۰ کاراکتر — توضیح بیشتر یعنی پاسخ دقیق‌تر.</span>
            </div>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;margin-top:22px;flex-wrap:wrap">
            <label class="check"><input type="checkbox" required name="consent"><span class="box"><i data-icon="check"></i></span><span>با <a class="link" href="#" style="font-size:inherit">سیاست حریم خصوصی</a> موافقم.</span></label>
            <button class="btn btn-primary btn-lg" type="submit">ارسال پیام <i data-icon="send"></i></button>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="grid grid-3" style="gap:14px">
      <div class="card card-pad" style="text-align:center;padding:24px"><span class="icon-tile" style="margin:0 auto 14px"><i data-icon="headphones"></i></span><b class="t-h4">پشتیبانی فنی</b><p class="t-caption mt-8">برای مشتریان پلن رشد و سازمانی، پاسخ‌گویی ۲۴/۷</p></div>
      <div class="card card-pad" style="text-align:center;padding:24px"><span class="icon-tile icon-tile-green" style="margin:0 auto 14px"><i data-icon="message-square-code"></i></span><b class="t-h4">کامیونیتی</b><p class="t-caption mt-8">گروه ۴٬۲۰۰ نفره توسعه‌دهندگان فارسی در تلگرام</p></div>
      <div class="card card-pad" style="text-align:center;padding:24px"><span class="icon-tile icon-tile-amber" style="margin:0 auto 14px"><i data-icon="briefcase"></i></span><b class="t-h4">همکاری</b><p class="t-caption mt-8">به <a class="link" href="#" style="font-size:inherit">jobs@bluevertex.ir</a> رزومه بفرستید</p></div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '</body></html>'

# ================================================================ BLOG LIST
POSTS = [
    dict(cat='توسعه نرم‌افزار', catId='dev', icon='code-2', title='چرا مستندات API محصول شما، مهم‌ترین صفحه وب آن است؟', excerpt='مستندات خوب، اولین تجربه توسعه‌دهنده با محصول شماست. در این مقاله از تجربه تیم‌های واقعی می‌گوییم و مدل محتوایی را مرور می‌کنیم.', author='نگار شریفی', read='۷ دقیقه', date='۲ شهریور ۱۴۰۵'),
    dict(cat='API', catId='api', icon='braces', title='طراحی Endpointهایی که توسعه‌دهنده‌ها دوست دارند', excerpt='نام‌گذاری منبع، نسخه‌بندی، صفحه‌بندی و خطاها — هفت اصل طراحی REST که ۸۰٪ تجربه API شما را می‌سازند.', author='رضا موسوی', read='۹ دقیقه', date='۲۸ مرداد ۱۴۰۵'),
    dict(cat='هوش مصنوعی', catId='ai', icon='brain-circuit', title='اندازه‌گیری و سهمیه‌بندی مصرف توکن برای محصولات AI', excerpt='وقتی هر تماس مدل هزینه دارد، شفافیت مصرف برای مشتری یک مزیت رقابتی است؛ نه یک جزئیات.', author='علی رضایی', read='۶ دقیقه', date='۲۰ مرداد ۱۴۰۵'),
    dict(cat='Saas', catId='saas', icon='layout', title='از ۰ به ۱۰۰ توسعه‌دهنده فعال: نقشه راه عرضه API', excerpt='یک چک‌لیست عملی برای ماه‌های اول: چه چیزی بسازیم، چه چیزی را رها کنیم و چه زمانی کنسول توسعه‌دهنده لازم می‌شود.', author='سارا احمدی', read='۱۱ دقیقه', date='۱۲ مرداد ۱۴۰۵'),
    dict(cat='امنیت', catId='sec', icon='shield-check', title='کلیدهای API امن: از Scopes تا چرخش بدون قطعی', excerpt='افشای کلید API رایج‌ترین اشتباه سال‌های اخیر است. الگوی چرخش مرحله‌ای را با مثال کد مرور می‌کنیم.', author='حسین کاظمی', read='۸ دقیقه', date='۴ مرداد ۱۴۰۵'),
    dict(cat='DevOps', catId='devops', icon='server-cog', title='مانیتورینگ API: چه چیزی را اندازه بگیریم؟', excerpt='P50 یا P95؟ نرخ خطا یا نرخ خطای ۵xx؟ راهنمای انتخاب متریک‌های درست برای داشبورد فنی شما.', author='امیر توکلی', read='۱۰ دقیقه', date='۲۶ تیر ۱۴۰۵'),
    dict(cat='توسعه نرم‌افزار', catId='dev', icon='layers', title='آرشیوکتورهای API Gateway: وقتی فقط یک دروازه کافی نیست', excerpt='از Gateway ساده تا Service Mesh؛ کجا باید مرزهای زیرساخت API خود را دوباره طراحی کنید.', author='علی رضایی', read='۱۳ دقیقه', date='۱۸ تیر ۱۴۰۵'),
    dict(cat='Saas', catId='saas', icon='trending-up', title='قیمت‌گذاری API: از رایگان تا سازمانی بدون سردرگمی', excerpt='مدل‌های مصرف، Freemium و سالانه؛ تجربه قیمت‌گذاری که هم مشتری را قانع کند هم درآمد شما را.', author='سارا احمدی', read='۷ دقیقه', date='۹ تیر ۱۴۰۵'),
    dict(cat='امنیت', catId='sec', icon='fingerprint', title='Webhook امن با امضای HMAC: راهنمای کامل', excerpt='چطور امضای هر رویداد را اعتبارسنجی کنید، کلید را بچرخانید و جلوی replay را بگیرید.', author='حسین کاظمی', read='۹ دقیقه', date='۱ تیر ۱۴۰۵'),
]
CATS = [('همه', 'all'), ('توسعه نرم‌افزار', 'dev'), ('API', 'api'), ('هوش مصنوعی', 'ai'), ('SaaS', 'saas'), ('امنیت', 'sec'), ('DevOps', 'devops')]

def post_card(post, prefix, size_idx=0):
    p = prefix
    return f'''<article class="post-card" data-cat="{post['catId']}" data-reveal>
      <div class="post-cover"><i data-icon="{post['icon']}" style="position:relative;z-index:2"></i></div>
      <div class="post-body">
        <div class="post-meta"><span class="badge badge-blue">{post['cat']}</span><span class="t-caption fa-num">{post['date']}</span></div>
        <h3><a href="{p}blog/article.html">{post['title']}</a></h3>
        <p>{post['excerpt']}</p>
        <div class="post-foot">
          <span class="post-author"><span class="avatar avatar-sm">{post['author'][0]}</span>{post['author']}</span>
          <span class="post-read fa-num">{post['read']}</span>
        </div>
      </div>
    </article>'''

def build_blog(prefix=''):
    p = prefix
    chips = ''.join(f'<button class="chip active" data-blog-cat="{cid}">{c}</button>' if i == 0 else f'<button class="chip" data-blog-cat="{cid}">{c}</button>' for i, (c, cid) in enumerate(CATS))
    grid = ''.join(post_card(post, p) for post in POSTS)
    return head(
        'وبلاگ | دیدگاه‌های فنی بلو استودیو',
        'مقالات فارسی درباره توسعه نرم‌افزار، طراحی API، هوش مصنوعی، SaaS، امنیت و DevOps — از تیم بلو استودیو.',
        prefix) + '''<body class="noise"><main>
''' + navbar('active_blog', p) + page_hero(
        crumb(p, 'وبلاگ'),
        'نوشته‌هایی که در راه <span class="grad-text">ساخت نرم‌افزار خوب</span> خواندیم و نوشتیم',
        'تجربه‌های تیم فنی بلو استودیو درباره API، معماری، محصول و امنیت — به زبان فارسی و با مثال واقعی.') + '''
<section class="section">
  <div class="container">
    <div class="chip-group mb-32" style="justify-content:center" data-reveal>''' + chips + '''</div>
    <div class="sec-head" data-reveal><h2>آخرین مقالات</h2><p>نوشته‌های تیم بلو استودیو درباره ساخت محصولات API و تجربه توسعه‌دهنده — به فارسی.</p></div>
    <div class="blog-grid" id="blogGrid">''' + grid + '''</div>
    <div class="empty-state" id="blogEmpty" style="display:none">
      <span class="es-icon"><i data-icon="file-search"></i></span>
      <h2>مقاله‌ای در این دسته نیست</h2>
      <p>برای این ترکیب فیلتر مقاله‌ای یافت نشد؛ دسته دیگری را امتحان کنید.</p>
      <button class="btn btn-secondary" data-blog-cat="all">نمایش همه</button>
    </div>
    <div class="flex justify-content-center" style="justify-content:center;margin-top:44px" data-reveal>
      <nav class="pagination" aria-label="صفحه‌بندی وبلاگ">
        <button class="page-btn" disabled aria-label="صفحه قبل"><i data-icon="chevron-right"></i></button>
        <button class="page-btn active">۱</button>
        <button class="page-btn">۲</button>
        <button class="page-btn">۳</button>
        <button class="page-btn" aria-label="صفحه بعد"><i data-icon="chevron-left"></i></button>
      </nav>
    </div>
  </div>
</section>

<section class="section" style="border-top:1px solid var(--border);background:var(--bg-elev)">
  <div class="container">
    <div class="cta-band" data-reveal>
      <h2>خبرنامه فنی بلو استودیو</h2>
      <p>هر دو هفته یک ایمیل؛ خلاصه بهترین مطالب API و DevOps، بدون اسپم. همین حالا عضو شوید.</p>
      <div class="hero-cta" style="max-width:440px;margin-inline:auto">
        <input class="input" type="email" placeholder="you@company.ir" aria-label="ایمیل" style="flex:1">
        <button class="btn btn-primary btn-lg" data-form-simple>عضویت</button>
      </div>
    </div>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p) + '''
<script>
(function(){
  document.querySelectorAll('[data-blog-cat]').forEach(function(chip){
    chip.addEventListener('click', function(){
      var cat = chip.getAttribute('data-blog-cat');
      document.querySelectorAll('[data-blog-cat]').forEach(function(c){ c.classList.remove('active'); });
      chip.classList.add('active');
      var shown = 0;
      document.querySelectorAll('.post-card').forEach(function(post){
        var ok = cat === 'all' || post.getAttribute('data-cat') === cat;
        post.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      var empty = document.getElementById('blogEmpty');
      if (empty) empty.style.display = shown ? 'none' : 'flex';
      if (shown && window.BV) BV.toast('info', 'دسته «' + chip.textContent + '»', 'نمایش ' + BV.faNum(shown) + ' مقاله');
    });
  });
  document.querySelectorAll('[data-form-simple]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var input = btn.parentNode.querySelector('input');
      if (!input.value || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(input.value)) {
        if (window.BV) BV.toast('error', 'ایمیل معتبر نیست', 'لطفاً یک ایمیل صحیح وارد کنید.');
        return;
      }
      btn.classList.add('btn-loading');
      setTimeout(function(){
        btn.classList.remove('btn-loading');
        btn.textContent = 'عضو شدید';
        if (window.BV) BV.toast('success', 'عضویت موفق', 'خوش آمدید! اولین خبرنامه دو هفته دیگر می‌رسد.');
      }, 900);
    });
  });
})();
</script>
</body></html>'''

# ================================================================ ARTICLE
def build_article(prefix=''):
    p = prefix
    related = POSTS[1:4]
    rel = ''.join(f'''<article class="post-card" data-reveal>
      <div class="post-cover"><i data-icon="{post['icon']}" style="position:relative;z-index:2"></i></div>
      <div class="post-body">
        <div class="post-meta"><span class="badge badge-blue">{post['cat']}</span></div>
        <h3><a href="article.html">{post['title']}</a></h3>
        <p>{post['excerpt']}</p>
        <div class="post-foot"><span class="post-read fa-num">{post['read']} مطالعه</span></div>
      </div>
    </article>''' for post in related)
    return head(
        'مستندات API خوب، مهم‌ترین صفحه وب محصول شما | وبلاگ بلو استودیو',
        'چرا مستندات API مهم‌ترین صفحه وب محصول شماست؟ بررسی تجربه توسعه‌دهنده، مدل محتوا و چک‌لیست عملی مستندات خوب.',
        prefix, og_type='article') + '''<body class="noise"><main>
''' + navbar('active_blog', p) + '''
<section class="section-sm">
  <div class="container article-wrap">
    <nav class="breadcrumb" aria-label="مسیر صفحه">
      <a href="../index.html">خانه</a><span class="sep"><i data-icon="chevron-left"></i></span>
      <a href="../pages/blog.html">وبلاگ</a><span class="sep"><i data-icon="chevron-left"></i></span>
      <span class="current">مستندات API</span>
    </nav>
    <header class="article-head">
      <div class="flex gap-12" style="flex-wrap:wrap">
        <span class="badge badge-blue">توسعه نرم‌افزار</span>
        <span class="badge"><i data-icon="clock" style="width:12px;height:12px"></i> ۷ دقیقه مطالعه</span>
        <span class="badge fa-num">۲ شهریور ۱۴۰۵</span>
      </div>
      <h1>چرا مستندات API محصول شما، مهم‌ترین صفحه وب آن است؟</h1>
      <p class="lead">توسعه‌دهنده‌ای که مستندات را نمی‌فهمد، هرگز مشتری نمی‌شود. در این مقاله از تجربه واقعی تیم‌ها می‌گوییم و یک مدل عملی برای مستندات خوب پیشنهاد می‌دهیم.</p>
    </header>

    <article class="article-body">
      <p>هر محصول API دو مشتری دارد: مشتری نهایی و <strong>توسعه‌دهنده‌ای که با آن محصول می‌سازد</strong>. تجربهٔ توسعه‌دهنده (DX) دقیقاً همان چیزی است که باعث می‌شود تیم‌های فنی بعد از اولین ادغام، دومین هم بمانند.</p>
      <blockquote>«مستندات خوب، نصف پشتیبانی است.» — این جمله را بارها شنیده‌ایم؛ اما در عمل، مستندات بد حتی از پشتیبانی هم بدتر است: هزینه دارد و هم‌زمان اعتماد را از بین می‌برد.</blockquote>

      <h2 id="why">اولین برخورد، برخورد با متن است</h2>
      <p>قبل از اینکه توسعه‌دهنده اولین درخواست را بفرستد، اولین چیزی که می‌خواند یک پاراگراف معرفی، یک نمونه‌کد و یک خطا است. این سه عنصر در چند ثانیه تصمیم «می‌مانم یا نمی‌مانم» را می‌سازند:</p>
      <ul>
        <li><strong>نمونه‌کد در بالای صفحه:</strong> توسعه‌دهنده باید بدون جستجو، یک نمونه کپی‌کردنی ببیند.</li>
        <li><strong>خطاهای معنادار:</strong> پیام خطا باید بگوید چه چیزی خراب است و چطور درست شود.</li>
        <li><strong>زبان بومی:</strong> برای بازار فارسی، مستندات فارسی با نمونه‌های حفظ‌شدهٔ LTR یک مزیت رقابتی واقعی است.</li>
      </ul>

      <h2 id="anatomy">آناتومی یک مستندات خوب</h2>
      <p>در بلو استودیو مستندات را با این چارچوب می‌سنجیم — هر بخش را می‌توانید در <a class="link" href="../docs/index.html" style="font-size:inherit">مستندات بلو ورتکس</a> زنده ببینید:</p>
      <div class="table-wrap" style="margin:24px 0">
        <table class="table">
          <thead><tr><th>بخش</th><th>سؤال توسعه‌دهنده</th><th>معیار موفقیت</th></tr></thead>
          <tbody>
            <tr><td class="cell-main">شروع سریع</td><td>«چطور شروع کنم؟»</td><td>اولین درخواست در کمتر از ۵ دقیقه</td></tr>
            <tr><td class="cell-main">احراز هویت</td><td>«کلیدم را کجا بگذارم؟»</td><td>نمونه برای ۳+ زبان</td></tr>
            <tr><td class="cell-main">مرجع API</td><td>«این Endpoint چه ورودی می‌گیرد؟»</td><td>پارامتر + نمونه پاسخ واقعی</td></tr>
            <tr><td class="cell-main">خطاها</td><td>«این خطا یعنی چه؟»</td><td>کد، پیام و راه‌حل</td></tr>
          </tbody>
        </table>
      </div>

      <h2 id="checklist">چک‌لیست عملی</h2>
      <p>قبل از انتشار مستندات، این شش مورد را قطعاً بررسی کنید:</p>
      <ol>
        <li><strong>نمونه‌کد واقعاً اجرا شود</strong> — نه کپی از یک وبلاگ خارجی.</li>
        <li><strong>یک پایه URL ثابت</strong> با نسخه‌بندی روشن (<code class="inline">/v1</code>).</li>
        <li><strong>صفحه‌بندی، فیلتر و مرتب‌سازی</strong> در همهٔ لیست‌ها یکدست باشد.</li>
        <li><strong>پیام خطا فارسی</strong> با کد خطای انگلیسی ثابت (مثلاً <code class="inline">unauthorized</code>).</li>
        <li><strong>محدودیت نرخ</strong> در هدر پاسخ اعلام شود.</li>
        <li><strong>جستجوی مستندات</strong> با میان‌بر صفحه‌کلید کار کند.</li>
      </ol>

      <div class="callout warn">
        <b class="icon-title"><i data-icon="alert-triangle"></i> نکته مهم</b>
        <p>مستندات را «پروژهٔ بعدی» نگذارید. همین امروز یک شیت سادهٔ Google Docs هم که باشد شروع کنید؛ بعداً به سیستم تولید خودکار مهاجرت کنید.</p>
      </div>

      <h2 id="tools">ابزارها در بلو ورتکس</h2>
      <p>بلو ورتکس مستندات زنده را از اسکیمای OpenAPI شما می‌سازد؛ یعنی نمونه‌کد و مدل پاسخ همیشه با کد شما هم‌قدم‌اند. نمونه‌ی یک Endpoint را ببینید:</p>
      <div class="code-block">
        <div class="code-head"><span class="code-lang"><span class="dot-bar"><i></i><i></i><i></i></span>curl</span><button class="code-copy" data-copy-target="#demoCurl" aria-label="کپی"><i data-icon="copy"></i></button></div>
        <pre id="demoCurl" class="line-numbers"><code class="language-bash">curl -X POST https://api.bluevertex.ir/v1/users \\
  -H "Authorization: Bearer $BV_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{"name": "سارا احمدی", "email": "sara@abrino.ir"}'</code></pre>
      </div>
      <p>پاسخ تا حدی که در کد سرور تعریف شده، همین‌جا مستند می‌شود و اگر رابط کاربری تغییر کند، مستندات هم در همان دیپلوی به‌روز می‌شود.</p>
    </article>

    <div class="author-box" data-reveal>
      <span class="avatar avatar-lg">ن</span>
      <div style="flex:1">
        <b>نگار شریفی</b>
        <p class="t-caption" style="margin-top:4px">مدیر مستندات بلو استودیو — ده سال تجربه در نوشتن فنی برای محصولات API. <span class="ltr text-electric">@negar_dev</span></p>
      </div>
      <a class="btn btn-outline btn-sm" href="../pages/blog.html">مقاله‌های بیشتر</a>
    </div>

    <nav class="doc-pager" aria-label="مقاله‌های مرتبط" style="margin-top:40px">
      <a class="pager-card prev" href="article.html"><span class="pager-label"><i data-icon="arrow-right"></i> مقاله قبلی</span><b>طراحی Endpointهایی که توسعه‌دهنده‌ها دوست دارند</b></a>
      <a class="pager-card next" href="article.html"><span class="pager-label">مقاله بعدی <i data-icon="arrow-left"></i></span><b>اندازه‌گیری و سهمیه‌بندی مصرف توکن</b></a>
    </nav>

    <section class="mt-48">
      <div class="flex-between mb-24"><h2 class="t-h3">مقاله‌های مرتبط</h2><a class="link" href="../pages/blog.html">همه مقالات <i data-icon="arrow-left"></i></a></div>
      <div class="blog-grid">''' + rel + '''</div>
    </section>
  </div>
</section>
</main>
''' + footer(p) + palette(p) + TOAST_REGION + scripts(p, prism=True) + '</body></html>'
