# -*- coding: utf-8 -*-
"""Blue Vertex — Developer Console pages, part 3 (sdk / team / billing / notifications / settings)"""

from dash import dash_page, daterange, drawer_log

# ================================================================ SDK
def build_sdk(prefix=''):
    content = '''
    <div class="sec-head start" style="margin-bottom:20px"><h2 class="t-h3">SDKهای نصب‌شده</h2><p>وضعیت نسخه‌ها در فضای کاری شما</p></div>
    <div class="sdk-manage-card">
      <span class="sdk-lang sdk-js">JS</span>
      <div class="sdk-manage-body">
        <h2>@bluevertex/sdk <span class="badge badge-green">به‌روز</span> <span class="badge">v3.2.0</span></h2>
        <p>آخرین به‌روزرسانی: ۱۲ مرداد ۱۴۰۵ · نصب‌شده در ۴ پروژه · حجم: ۴۸KB (gzip)</p>
        <div class="code-block sdk-install" style="margin:0"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
          <pre class="line-numbers"><code class="language-bash">npm install @bluevertex/sdk@latest</code></pre></div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <a class="btn btn-outline btn-sm" href="../docs/sdks.html#js"><i data-icon="book-open"></i> مستندات</a>
        <button class="btn btn-ghost btn-sm" data-sdk-update="JavaScript"><i data-icon="refresh-cw"></i> بررسی نسخه</button>
      </div>
    </div>
    <div class="sdk-manage-card">
      <span class="sdk-lang sdk-py">Py</span>
      <div class="sdk-manage-body">
        <h2>bluevertex <span class="badge badge-amber">نسخه جدید</span> <span class="badge">v1.7.2 → v1.8.0</span></h2>
        <p>نسخه ۱٫۸٫۰: تایپ کامل و بهبود timeouts. ارتقا بی‌خطر است — API تغییری نداشته است.</p>
        <div class="code-block sdk-install" style="margin:0"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
          <pre class="line-numbers"><code class="language-bash">pip install --upgrade bluevertex</code></pre></div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap">
        <a class="btn btn-outline btn-sm" href="../docs/sdks.html#py"><i data-icon="book-open"></i> مستندات</a>
        <button class="btn btn-soft btn-sm" data-sdk-update="Python"><i data-icon="download"></i> ارتقا به ۱٫۸٫۰</button>
      </div>
    </div>

    <div class="sec-head start" style="margin:40px 0 20px"><h2 class="t-h3">SDKهای دیگر</h2><p>نصب در یک فرمان — همه SDKها رفتار یکسان دارند</p></div>
    <div class="grid-2">
      <div class="sdk-card">
        <span class="sdk-lang sdk-php">PHP</span>
        <h2>bluevertex/php</h2>
        <p class="sdk-ver">نسخه پایدار: <code>v2.1.0</code> · PHP 8.1+</p>
        <div class="sdk-meta"><span><i data-icon="star"></i> ۹۶۴</span><span><i data-icon="shield"></i> MIT</span><span><i data-icon="clock"></i> آخرین آپدیت: ۲ هفته پیش</span></div>
        <div class="code-block sdk-install" style="margin-top:0"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
          <pre class="line-numbers"><code class="language-bash">composer require bluevertex/php</code></pre></div>
        <a class="btn btn-outline btn-sm mt-16" href="../docs/sdks.html#php">مستندات PHP <i data-icon="arrow-left"></i></a>
      </div>
      <div class="sdk-card">
        <span class="sdk-lang sdk-go">Go</span>
        <h2>bluevertex-go</h2>
        <p class="sdk-ver">نسخه پایدار: <code>v1.4.0</code> · Go 1.21+</p>
        <div class="sdk-meta"><span><i data-icon="star"></i> ۷۱۲</span><span><i data-icon="shield"></i> MIT</span><span><i data-icon="clock"></i> آخرین آپدیت: ۱ ماه پیش</span></div>
        <div class="code-block sdk-install" style="margin-top:0"><div class="code-head"><span class="code-lang">bash</span><button class="code-copy" aria-label="کپی"><i data-icon="copy"></i></button></div>
          <pre class="line-numbers"><code class="language-bash">go get github.com/bluevertex/bluevertex-go</code></pre></div>
        <a class="btn btn-outline btn-sm mt-16" href="../docs/sdks.html#go">مستندات Go <i data-icon="arrow-left"></i></a>
      </div>
    </div>

    <div class="callout" style="margin-top:28px"><b class="icon-title"><i data-icon="bell-ring"></i> خبر SDK</b><p>بازخورد خود را در مخزن گیت‌هاب ثبت کنید یا در مستندات، بخش نمونه‌ها، کد آماده ببینید.</p></div>
'''
    actions = '<a class="btn btn-secondary btn-sm" href="../docs/sdks.html"><i data-icon="book-open"></i> مستندات SDK</a>'
    return dash_page('SDKها', 'dashboard/sdk.html', 'SDKها', 'مدیریت و وضعیت کتابخانه‌های رسمی بلو ورتکس', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  document.querySelectorAll('[data-sdk-update]').forEach(function(b){
    b.addEventListener('click', function(){
      b.classList.add('btn-loading');
      setTimeout(function(){
        b.classList.remove('btn-loading');
        if (window.BV) BV.toast('success', b.getAttribute('data-sdk-update') + ' به‌روز است', 'آخرین نسخه پایدار نصب شده است. (دمو)');
      }, 1000);
    });
  });
})();
</script>''')

# ================================================================ TEAM
def build_team(prefix=''):
    members = [
        ('سارا احمدی', 'sara@abrino.ir', 'مالک', 'active', 'همین حالا', 'س', 'blue'),
        ('علی رضایی', 'ali@abrino.ir', 'توسعه‌دهنده', 'active', '۱۲ دقیقه پیش', 'ع', 'green'),
        ('مریم کریمی', 'maria@abrino.ir', 'توسعه‌دهنده', 'active', '۲ ساعت پیش', 'م', 'violet'),
        ('رضا موسوی', 'reza@abrino.ir', 'بیننده', 'active', 'دیروز', 'ر', 'amber'),
        ('نگار شریفی', 'negar@abrino.ir', 'مدیر', 'active', '۳ روز پیش', 'ن', 'cyan'),
        ('امیر توکلی', 'amir@abrino.ir', 'توسعه‌دهنده', 'suspended', '۶ روز پیش', 'ا', 'red'),
    ]
    rows = ''
    for name, mail, role, status, last, initial, color in members:
        st = '<span class="badge badge-green"><span class="dot"></span> فعال</span>' if status == 'active' else '<span class="badge"><i data-icon="pause"></i> معلق</span>'
        role_opts = ['مالک', 'مدیر', 'توسعه‌دهنده', 'بیننده']
        sel = f'<select class="select role-select" aria-label="نقش {name}">' + ''.join(
            f'<option {"selected" if r == role else ""} {("disabled" if r == "مالک" and role != "مالک" else "")}>{r}</option>' for r in role_opts) + '</select>'
        rows += f'''<div class="member-row" data-member="{mail}">
      <span class="avatar" style="background:linear-gradient(135deg,{'#3B82F6,#1E3A8A' if color == 'blue' else '#34D399,#065F46' if color == 'green' else '#A78BFA,#4C1D95' if color == 'violet' else '#FBBF24,#92400E' if color == 'amber' else '#22D3EE,#155E75' if color == 'cyan' else '#F87171,#7F1D1D'})">{initial}</span>
      <div class="member-info"><b>{name}</b><span dir="ltr">{mail}</span></div>
      <span class="t-caption fa-num">فعالیت: {last}</span>
      {sel}
      {st}
      <button class="btn btn-ghost btn-sm" data-remove-member="{name}"><i data-icon="user-x" style="width:15px;height:15px"></i> حذف</button>
    </div>'''
    content = f'''
    <div class="invite-box">
      <div class="flex-between" style="flex-wrap:wrap;gap:14px">
        <div style="flex:1;min-width:220px">
          <h2 class="t-h4 mb-8">دعوت عضو جدید</h2>
          <p class="t-caption">ایمیل یا شماره موبایل — دعوت‌نامه با لینک یکتا ارسال می‌شود و ۷ روز اعتبار دارد.</p>
          <div class="flex gap-8 mt-16" style="flex-wrap:wrap">
            <input class="input" id="inviteEmail" type="email" placeholder="you@company.ir" style="max-width:280px" aria-label="ایمیل دعوت">
            <select class="select" style="width:auto;min-width:140px" aria-label="نقش">
              <option>توسعه‌دهنده</option><option>مدیر</option><option>بیننده</option>
            </select>
            <button class="btn btn-primary" id="inviteBtn"><i data-icon="send"></i> ارسال دعوت</button>
          </div>
        </div>
        <span class="badge"><i data-icon="users"></i> ۶ عضو · ۵ فعال</span>
      </div>
    </div>

    <div class="card" style="overflow:hidden">
      <div class="card-head">
        <div><h2>اعضای تیم</h2><p class="t-caption" style="margin-top:4px">نقش‌ها را با فیلد انتخاب تغییر دهید — تغییرات بلافاصله اعمال می‌شوند.</p></div>
        <button class="btn btn-ghost btn-sm" id="toggleTeamEmpty">پیش‌نمایش حالت خالی</button>
      </div>
      <div id="membersList">{rows}</div>
    </div>
    <div class="empty-state" id="teamEmpty" style="display:none">
      <span class="es-icon"><i data-icon="users"></i></span>
      <h2>هنوز عضوی دعوت نکرده‌اید</h2>
      <p>همکاران خود را دعوت کنید تا دسترسی‌ها و مسئولیت‌ها را با هم مدیریت کنید.</p>
      <button class="btn btn-primary" onclick="document.getElementById('inviteEmail').focus()"><i data-icon="user-plus"></i> دعوت عضو</button>
    </div>

    <div class="card card-pad mt-24">
      <h2 class="t-h4 mb-16">ماتریس دسترسی نقش‌ها</h2>
      <div class="table-wrap" style="border:none">
        <table class="table">
          <thead><tr><th>قابلیت</th><th>مالک</th><th>مدیر</th><th>توسعه‌دهنده</th><th>بیننده</th></tr></thead>
          <tbody>
            <tr><td>مشاهده داشبورد</td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td></tr>
            <tr><td>ساخت و باطل‌سازی کلید</td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td></tr>
            <tr><td>مدیریت اعضا</td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td></tr>
            <tr><td>صورتحساب و تنظیمات</td><td><i data-icon="check" class="text-green" style="width:15px;height:15px"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td><td><i data-icon="minus" style="width:15px;height:15px;color:var(--text-4)"></i></td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- remove member confirm -->
    <div class="modal-backdrop" id="removeMemberModal" role="dialog" aria-modal="true" aria-label="حذف عضو">
      <div class="modal modal-sm">
        <div class="modal-head"><div><h2 style="color:var(--red)">حذف عضو از تیم</h2><p>«<b id="removeName">—</b>» دسترسی خود به فضای کاری ابرینو را از دست می‌دهد.</p></div>
          <button class="modal-close" data-modal-close="removeMemberModal" aria-label="بستن"><i data-icon="x"></i></button></div>
        <div class="modal-body">
          <div class="security-note" style="margin:0"><i data-icon="info"></i><span>کلیدهای متعلق به این عضو باطل نمی‌شوند؛ اگر لازم است جداگانه آن‌ها را مدیریت کنید.</span></div>
        </div>
        <div class="modal-foot">
          <button class="btn btn-ghost" data-modal-close="removeMemberModal">انصراف</button>
          <button class="btn btn-danger" id="confirmRemove">حذف عضو</button>
        </div>
      </div>
    </div>
'''
    actions = '<button class="btn btn-primary btn-sm" id="inviteBtnTop"><i data-icon="user-plus"></i> دعوت عضو</button>'
    return dash_page('تیم', 'dashboard/team.html', 'تیم', 'اعضا، نقش‌ها و دسترسی‌های فضای کاری ابرینو', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  var topBtn = document.getElementById('inviteBtnTop');
  if (topBtn) topBtn.addEventListener('click', function(){ document.getElementById('inviteEmail').focus(); });
  document.getElementById('inviteBtn').addEventListener('click', function(){
    var input = document.getElementById('inviteEmail');
    if (!input.value || !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(input.value)) {
      if (window.BV) BV.toast('error', 'ایمیل معتبر نیست', 'لطفاً ایمیل عضو را درست وارد کنید.');
      return;
    }
    var b = document.getElementById('inviteBtn');
    b.classList.add('btn-loading');
    setTimeout(function(){
      b.classList.remove('btn-loading');
      input.value = '';
      if (window.BV) BV.toast('success', 'دعوت‌نامه ارسال شد', 'لینک دعوت به ' + input.value + ' ایمیل شد. (دمو)');
    }, 1000);
  });
  var removeTarget = null;
  document.querySelectorAll('[data-remove-member]').forEach(function(b){
    b.addEventListener('click', function(){
      removeTarget = b.closest('.member-row');
      document.getElementById('removeName').textContent = b.getAttribute('data-remove-member');
      if (window.BV) BV.openModal('removeMemberModal');
    });
  });
  document.getElementById('confirmRemove').addEventListener('click', function(){
    var btn = this;
    btn.classList.add('btn-loading');
    setTimeout(function(){
      btn.classList.remove('btn-loading');
      if (removeTarget) removeTarget.style.display = 'none';
      if (window.BV) { BV.closeModal('removeMemberModal'); BV.toast('success', 'عضو حذف شد', 'دسترسی عضو به‌صورت آنی قطع شد. (دمو)'); }
    }, 900);
  });
  document.querySelectorAll('.role-select').forEach(function(sel){
    sel.addEventListener('change', function(){
      if (window.BV) BV.toast('success', 'نقش تغییر کرد', 'نقش جدید «' + sel.value + '» اعمال شد. (دمو)');
    });
  });
  document.getElementById('toggleTeamEmpty').addEventListener('click', function(){
    var list = document.getElementById('membersList');
    var empty = document.getElementById('teamEmpty');
    var hidden = list.style.display === 'none';
    list.style.display = hidden ? '' : 'none';
    empty.style.display = hidden ? 'none' : 'flex';
  });
  document.querySelectorAll('.member-row .role-select').forEach(function(sel){
    if (sel.value === 'مالک') sel.disabled = true;
  });
})();
</script>''')

# ================================================================ BILLING
def build_billing(prefix=''):
    content = '''
    <div class="plan-card">
      <div class="flex-between" style="flex-wrap:wrap;gap:20px;position:relative;z-index:2">
        <div>
          <span class="badge badge-blue">پلن فعال: رشد</span>
          <h2 class="t-h2 mt-16" style="font-size:1.5rem">۳٬۹۰۰٬۰۰۰ تومان <span class="t-caption" style="font-weight:500">/ ماهانه</span></h2>
          <p class="t-caption mt-8" style="max-width:46ch">دوره فعلی: ۱ مرداد تا ۱ شهریور ۱۴۰۵ · تمدید خودکار فعال است. <a class="link" href="#" style="font-size:inherit">غیرفعال‌سازی</a></p>
        </div>
        <div style="text-align:end">
          <p class="t-caption" style="margin-bottom:8px">پرداخت بعدی: <b class="text-1">۱ شهریور ۱۴۰۵</b></p>
          <div class="flex gap-8" style="justify-content:flex-end;flex-wrap:wrap">
            <button class="btn btn-outline" data-upgrade-panel><i data-icon="arrow-up-circle"></i> تغییر پلن</button>
            <button class="btn btn-ghost" data-invoice-demo><i data-icon="receipt"></i> فاکتور این ماه</button>
          </div>
        </div>
      </div>
    </div>

    <div class="plan-usage-summary">
      <div class="quota-card"><div class="quota-head"><b><i data-icon="activity"></i>درخواست</b></div><div class="quota-nums"><b class="fa-num">۳٫۴M</b><span>/ ۵M</span></div><div class="progress"><i style="width:68%"></i></div><p class="t-caption mt-8">هزینه تخمینی ماه: ۳٬۹۰۰٬۰۰۰ تومان</p></div>
      <div class="quota-card"><div class="quota-head"><b><i data-icon="cpu"></i>توکن</b></div><div class="quota-nums"><b class="fa-num">۸۲۰K</b><span>/ ۲M</span></div><div class="progress green"><i style="width:41%"></i></div><p class="t-caption mt-8">در پلن رشد لحاظ شده</p></div>
      <div class="quota-card"><div class="quota-head"><b><i data-icon="database"></i>ذخیره‌سازی</b></div><div class="quota-nums"><b class="fa-num">۴۶GB</b><span>/ ۲۰۰GB</span></div><div class="progress"><i style="width:23%"></i></div><p class="t-caption mt-8">هزینه: لحاظ‌شده</p></div>
    </div>

    <div class="bill-grid">
      <div class="chart-card">
        <div class="chart-card-head"><div><h2>صورتحساب‌ها</h2><p>دانلود فاکتور رسمی به تومان — با تاریخ شمسی</p></div></div>
        <div class="table-wrap" style="border:none;border-radius:0">
          <table class="table">
            <thead><tr><th>شماره</th><th>دوره</th><th>مبلغ</th><th>وضعیت</th><th></th></tr></thead>
            <tbody>
              <tr><td><code class="inline text-code">INV-1405-008</code></td><td class="fa-num">مرداد ۱۴۰۵</td><td class="fa-num">۴٬۰۴۷٬۰۰۰</td><td><span class="badge badge-green">پرداخت‌شده</span></td><td><button class="btn btn-ghost btn-sm" data-invoice="INV-1405-008"><i data-icon="download"></i> فاکتور</button></td></tr>
              <tr><td><code class="inline text-code">INV-1405-007</code></td><td class="fa-num">تیر ۱۴۰۵</td><td class="fa-num">۳٬۹۸۱٬۰۰۰</td><td><span class="badge badge-green">پرداخت‌شده</span></td><td><button class="btn btn-ghost btn-sm" data-invoice="INV-1405-007"><i data-icon="download"></i> فاکتور</button></td></tr>
              <tr><td><code class="inline text-code">INV-1405-006</code></td><td class="fa-num">خرداد ۱۴۰۵</td><td class="fa-num">۳٬۹۰۰٬۰۰۰</td><td><span class="badge badge-green">پرداخت‌شده</span></td><td><button class="btn btn-ghost btn-sm" data-invoice="INV-1405-006"><i data-icon="download"></i> فاکتور</button></td></tr>
              <tr><td><code class="inline text-code">INV-1405-005</code></td><td class="fa-num">اردیبهشت ۱۴۰۵</td><td class="fa-num">۳٬۷۲۰٬۰۰۰</td><td><span class="badge badge-green">پرداخت‌شده</span></td><td><button class="btn btn-ghost btn-sm" data-invoice="INV-1405-005"><i data-icon="download"></i> فاکتور</button></td></tr>
            </tbody>
          </table>
        </div>
      </div>
      <div>
        <div class="chart-card" style="margin-bottom:16px">
          <div class="chart-card-head"><div><h2>روش پرداخت</h2><p>پرداخت ریالی — کارت شتاب</p></div></div>
          <div class="payment-method">
            <span class="pm-icon"><i data-icon="credit-card"></i></span>
            <div style="flex:1"><b class="t-sm">کارت به نام سارا احمدی</b><p class="t-caption ltr" dir="ltr" style="margin-top:2px">•••• ۴۴۲۱ — شتاب</p></div>
            <button class="btn btn-ghost btn-sm" id="pmChange">تغییر</button>
          </div>
          <button class="btn btn-outline btn-block btn-sm" id="pmAdd"><i data-icon="plus"></i> افزودن روش پرداخت</button>
        </div>
        <div class="card card-pad" style="padding:18px 20px">
          <div class="flex-between mb-16"><span class="t-caption">مصرف این دوره</span><b class="t-sm fa-num">۷۸٪</b></div>
          <div class="progress amber" style="margin-bottom:14px"><i style="width:78%"></i></div>
          <p class="t-caption">در این نرخ، دوره در <b class="text-1">۲۵ شهریور</b> تمام می‌شود. پلن سازمانی را در نظر بگیرید.</p>
          <button class="btn btn-primary btn-sm btn-block mt-16" data-upgrade-panel>مشاوره ارتقا</button>
        </div>
      </div>
    </div>

    <!-- upgrade modal -->
    <div class="modal-backdrop" id="upgradeModal" role="dialog" aria-modal="true" aria-label="تغییر پلن">
      <div class="modal modal-lg">
        <div class="modal-head"><div><h2>تغییر پلن</h2><p>ارتقا فوری با محاسبه روزشمار؛ کاهش پلن از دوره بعد.</p></div>
          <button class="modal-close" data-modal-close="upgradeModal" aria-label="بستن"><i data-icon="x"></i></button></div>
        <div class="modal-body">
          <div class="grid-3" style="gap:12px;margin-bottom:18px">
            <div class="price-card" style="padding:18px"><span class="price-name">توسعه‌دهنده</span><div class="price-amount"><b class="fa-num" style="font-size:1.3rem">۹۹۰٬۰۰۰</b><span>تومان/ماه</span></div><a class="btn btn-outline btn-sm btn-block mt-8" data-pick-plan="توسعه‌دهنده">انتخاب</a></div>
            <div class="price-card popular" style="padding:18px"><span class="popular-tag" style="top:-9px">پلن فعلی</span><span class="price-name">رشد</span><div class="price-amount"><b class="fa-num" style="font-size:1.3rem">۳٬۹۰۰٬۰۰۰</b><span>تومان/ماه</span></div><a class="btn btn-secondary btn-sm btn-block mt-8" disabled>فعال</a></div>
            <div class="price-card" style="padding:18px"><span class="price-name">سازمانی</span><div class="price-amount"><b>توافقی</b></div><a class="btn btn-soft btn-sm btn-block mt-8" data-pick-plan="سازمانی">گفتگو با فروش</a></div>
          </div>
          <div class="security-note"><i data-icon="info"></i><span>در نسخه دمو، انتخاب پلن فقط نمایش داده می‌شود — هیچ پرداختی انجام نمی‌شود و هیچ داده‌ای ارسال نمی‌گردد.</span></div>
        </div>
        <div class="modal-foot"><button class="btn btn-ghost" data-modal-close="upgradeModal">بستن</button></div>
      </div>
    </div>
'''
    actions = '<span class="badge badge-blue" id="planBadge">پلن رشد</span><button class="btn btn-primary btn-sm" data-upgrade-panel><i data-icon="arrow-up-circle"></i> ارتقا</button>'
    return dash_page('صورتحساب', 'dashboard/billing.html', 'صورتحساب', 'پلن، پرداخت‌ها و فاکتورهای فضای کاری ابرینو — به تومان', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  document.querySelectorAll('[data-upgrade-panel]').forEach(function(b){
    b.addEventListener('click', function(){ if (window.BV) BV.openModal('upgradeModal'); });
  });
  document.querySelectorAll('[data-pick-plan]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', b.getAttribute('data-pick-plan'), 'درخواست شما ثبت شد؛ این یک نسخه دمو است.');
    });
  });
  document.querySelectorAll('[data-invoice], [data-invoice-demo]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', 'فاکتور آماده شد', 'فایل PDF فاکتور دانلود شد (نسخه دمو).');
    });
  });
  document.getElementById('pmChange').addEventListener('click', function(){
    if (window.BV) BV.toast('info', 'تغییر کارت', 'در نسخه دمو، مدیریت کارت شبیه‌سازی می‌شود.');
  });
  document.getElementById('pmAdd').addEventListener('click', function(){
    if (window.BV) BV.toast('info', 'روش پرداخت جدید', 'روش‌های افزودن: کارت شتاب، حواله بانکی (دمو).');
  });
})();
</script>''')

# ================================================================ NOTIFICATIONS
def build_notifications(prefix=''):
    items = [
        dict(unread=1, cat='security', icon='shield-alert', color='amber', title='کلید API جدید ساخته شد', body='مریم کریمی کلید «توسعه — محلی» را در محیط test ساخت.', time='۱۰ دقیقه پیش'),
        dict(unread=1, cat='billing', icon='credit-card', color='blue', title='فاکتور مرداد ۱۴۰۵ صادر شد', body='فاکتور INV-1405-008 به مبلغ ۴٬۰۴۷٬۰۰۰ تومان آماده دانلود است.', time='۲ ساعت پیش'),
        dict(unread=1, cat='api', icon='alert-triangle', color='red', title='نرخ خطای غیرعادی در GET /v1/payments/:id', body='نرخ خطای ۴xx در ۱۵ دقیقه اخیر به ۲٫۱٪ رسید (آستانه: ۱٪).', time='۳ ساعت پیش'),
        dict(unread=0, cat='system', icon='server-cog', color='green', title='نگهداری برنامه‌ریزی‌شده انجام شد', body='نگهداری زیرساخت در ۶ تیر با موفقیت و بدون قطعی انجام شد.', time='دیروز'),
        dict(unread=0, cat='api', icon='gauge', color='violet', title='هشدار مصرف: ۷۸٪ سهمیه ماهانه', body='با این روند، سقف ۵ میلیون درخواست در ۲۵ شهریور پر می‌شود.', time='دیروز'),
        dict(unread=0, cat='security', icon='log-in', color='blue', title='ورود جدید به حساب', body='ورود موفق از دستگاه جدید (Chrome · تهران) — اگر شما نبودید، رمز را عوض کنید.', time='۲ روز پیش'),
        dict(unread=0, cat='system', icon='package', color='green', title='SDK پایتون نسخه ۱٫۸٫۰ منتشر شد', body='نسخه جدید با تایپ کامل در دسترس است: pip install --upgrade bluevertex', time='۳ روز پیش'),
        dict(unread=0, cat='billing', icon='receipt', color='amber', title='یادآوری: پرداخت اختیاری سالانه', body='با پرداخت سالانه ۲۰٪ صرفه‌جویی کنید — تا پایان دوره فرصت دارید.', time='۵ روز پیش'),
    ]
    rows = ''
    for it in items:
        rows += f'''<div class="notif-item{' unread' if it['unread'] else ''}" data-cat="{it['cat']}">
      <span class="icon-tile icon-tile-sm icon-tile-{it['color']}"><i data-icon="{it['icon']}"></i></span>
      <div style="flex:1;min-width:0"><b>{it['title']}</b><p>{it['body']}</p></div>
      <time class="fa-num">{it['time']}</time>
      <button class="btn btn-ghost btn-sm" data-notif-read aria-label="علامت‌گذاری به‌عنوان خوانده‌شده"><i data-icon="check" style="width:14px;height:14px"></i></button>
    </div>'''
    content = f'''
    <div class="card" style="overflow:hidden">
      <div class="card-head" style="align-items:center;flex-wrap:wrap">
        <div class="tabs" data-tabs style="border:none;margin:0">
          <button class="tab-btn active" data-tab="all">همه <span class="count">۸</span></button>
          <button class="tab-btn" data-tab="unread">نخوانده <span class="count">۳</span></button>
          <button class="tab-btn" data-tab="security">امنیت</button>
          <button class="tab-btn" data-tab="billing">صورتحساب</button>
          <button class="tab-btn" data-tab="api">API</button>
          <button class="tab-btn" data-tab="system">سیستم</button>
        </div>
        <button class="btn btn-ghost btn-sm" id="markAllRead" style="margin-inline-start:auto"><i data-icon="check-check"></i> خواندن همه</button>
      </div>
      <div id="notifList">{rows}</div>
    </div>
    <div class="empty-state" id="notifEmpty" style="display:none">
      <span class="es-icon"><i data-icon="bell-off"></i></span>
      <h2>اعلانی در این دسته نیست</h2>
      <p>اعلان‌های جدید امنیتی، صورتحساب و API این‌جا نمایش داده می‌شوند.</p>
    </div>

    <div class="card card-pad mt-24">
      <h2 class="t-h4 mb-8">ترجیحات اعلان</h2>
      <p class="t-caption mb-16">از طریق داشبورد، ایمیل یا تلگرام — کنترل کامل با شماست.</p>
      <div class="setting-row"><div><b>خطاهای API</b><p>هشدار نرخ خطای بالای ۱٪ در ۱۵ دقیقه</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
      <div class="setting-row"><div><b>صورتحساب</b><p>صدور فاکتور، یادآوری پرداخت</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
      <div class="setting-row"><div><b>هشدارهای امنیتی</b><p>ورود جدید، ساخت کلید، تغییر دسترسی</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
    </div>
'''
    actions = '<button class="btn btn-secondary btn-sm" data-notif-test><i data-icon="bell"></i> اعلان آزمایشی</button>'
    return dash_page('اعلان‌ها', 'dashboard/notifications.html', 'اعلان‌ها', 'اعلان‌های سیستم، امنیت، صورتحساب و API', content, actions=actions,
                     extra_scripts='''<script>
(function(){
  var tabs = document.querySelector('.tabs[data-tabs]');
  var list = document.getElementById('notifList');
  var empty = document.getElementById('notifEmpty');
  tabs.querySelectorAll('.tab-btn').forEach(function(tab){
    tab.addEventListener('click', function(){
      var target = tab.getAttribute('data-tab');
      var shown = 0;
      list.querySelectorAll('.notif-item').forEach(function(item){
        var cat = item.getAttribute('data-cat');
        var unread = item.classList.contains('unread');
        var ok = target === 'all' || (target === 'unread' && unread) || cat === target;
        item.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      empty.style.display = shown ? 'none' : 'flex';
    });
  });
  document.querySelectorAll('[data-notif-test]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('info', 'اعلان آزمایشی', 'اگر این پیام را می‌بینید، همه‌چیز درست کار می‌کند :)');
    });
  });
})();
</script>''')

# ================================================================ SETTINGS
def build_settings(prefix=''):
    content = '''
    <div class="settings-layout">
      <nav class="settings-nav" aria-label="تنظیمات">
        <a href="#panel-general" class="active" data-settings-nav="general"><i data-icon="settings"></i>عمومی</a>
        <a href="#panel-workspace" data-settings-nav="workspace"><i data-icon="building-2"></i>فضای کاری</a>
        <a href="#panel-security" data-settings-nav="security"><i data-icon="shield"></i>امنیت</a>
        <a href="#panel-notif" data-settings-nav="notif"><i data-icon="bell"></i>اعلان‌ها</a>
        <a href="#panel-webhooks" data-settings-nav="webhooks"><i data-icon="webhook"></i>Webhookها</a>
        <a href="#panel-api" data-settings-nav="api"><i data-icon="braces"></i>API</a>
        <a href="#panel-members" data-settings-nav="members"><i data-icon="users"></i>اعضا</a>
        <a href="#panel-appearance" data-settings-nav="appearance"><i data-icon="palette"></i>ظاهر</a>
        <a href="#panel-danger" data-settings-nav="danger" style="color:var(--red)"><i data-icon="alert-triangle" style="color:var(--red)"></i>منطقه خطر</a>
      </nav>

      <div style="min-width:0">
        <!-- GENERAL -->
        <section class="settings-panel active" id="panel-general">
          <h2>عمومی</h2>
          <p class="panel-desc">اطلاعات حساب و پروفایل شما.</p>
          <div class="card card-pad" style="margin-bottom:18px">
            <div class="avatar-upload">
              <span class="avatar">س</span>
              <div style="flex:1">
                <b class="t-sm">عکس پروفایل</b>
                <p class="t-caption" style="margin-top:2px">PNG یا JPG — حداکثر ۲ مگابایت</p>
                <div class="flex gap-8 mt-16">
                  <button class="btn btn-secondary btn-sm" data-upload-demo>آپلود عکس جدید</button>
                  <button class="btn btn-ghost btn-sm">حذف</button>
                </div>
              </div>
            </div>
          </div>
          <div class="card card-pad">
            <form data-form data-success-title="ذخیره شد" data-success-msg="تغییرات پروفایل ذخیره شد." novalidate>
              <div class="grid-2" style="gap:16px">
                <div class="field"><label class="field-label" for="setName">نام و نام خانوادگی</label><input id="setName" class="input" value="سارا احمدی" required></div>
                <div class="field"><label class="field-label" for="setTitle">عنوان شغلی</label><input id="setTitle" class="input" value="مدیر فنی"></div>
                <div class="field"><label class="field-label" for="setEmail">ایمیل</label><input id="setEmail" class="input ltr" dir="ltr" type="email" value="sara@abrino.ir" required></div>
                <div class="field"><label class="field-label" for="setMobile">شماره موبایل</label><input id="setMobile" class="input ltr" dir="ltr" type="tel" value="09120000000"></div>
              </div>
              <div class="flex gap-12 mt-16"><button class="btn btn-primary" type="submit">ذخیره تغییرات</button><span class="t-caption" style="align-self:center">آخرین ویرایش: ۱۴۰۵/۰۶/۰۲</span></div>
            </form>
          </div>
        </section>

        <!-- WORKSPACE -->
        <section class="settings-panel" id="panel-workspace">
          <h2>فضای کاری</h2>
          <p class="panel-desc">اطلاعات فضای کاری ابرینو و تنظیمات آن.</p>
          <div class="card card-pad" style="margin-bottom:18px">
            <div class="flex gap-16" style="flex-wrap:wrap">
              <span class="ws-avatar" style="width:52px;height:52px;border-radius:14px;font-size:1.1rem">ا</span>
              <form style="flex:1;min-width:240px" data-form data-success-title="ذخیره شد" data-success-msg="اطلاعات فضای کاری ذخیره شد." novalidate>
                <div class="grid-2" style="gap:16px">
                  <div class="field"><label class="field-label" for="setWs">نام فضای کاری</label><input id="setWs" class="input" value="ابرینو" required></div>
                  <div class="field"><label class="field-label" for="setSlug">شناسه</label><input id="setSlug" class="input ltr" dir="ltr" value="abrino" readonly><span class="field-hint">در پایه URL استفاده می‌شود — قابل تغییر نیست.</span></div>
                  <div class="field"><label class="field-label" for="setRegion">منطقه داده</label><select id="setRegion" class="select"><option>تهران (tehran)</option><option>استانبول</option><option>فرانکفورت</option></select></div>
                  <div class="field"><label class="field-label" for="setDesc">توضیح</label><input id="setDesc" class="input" value="زیرساخت API محصولات ابرینو"></div>
                </div>
                <button class="btn btn-primary mt-16" type="submit">ذخیره</button>
              </form>
            </div>
          </div>
          <div class="setting-row"><div><b>حذف فضای کاری</b><p>به بخش «منطقه خطر» مراجعه کنید.</p></div><a class="btn btn-danger-soft btn-sm" href="#panel-danger" data-goto-danger>رفتن به منطقه خطر</a></div>
        </section>

        <!-- SECURITY -->
        <section class="settings-panel" id="panel-security">
          <h2>امنیت</h2>
          <p class="panel-desc">ورود دومرحله‌ای، نشست‌ها و رمز عبور.</p>
          <div class="card card-pad" style="margin-bottom:18px;background:linear-gradient(135deg,rgba(52,211,153,.07),var(--bg-elev) 60%)">
            <div class="flex-between" style="flex-wrap:wrap;gap:16px">
              <div class="flex gap-16">
                <span class="icon-tile icon-tile-green"><i data-icon="shield-check"></i></span>
                <div><b class="t-h4">ورود دومرحله‌ای (2FA)</b><p class="t-caption" style="margin-top:4px;max-width:44ch">با کد TOTP هر ۳۰ ثانیه — برای محافظت از حساب شما فعال است.</p></div>
              </div>
              <span class="badge badge-green"><span class="dot"></span> فعال</span>
            </div>
            <div class="flex gap-8 mt-16" style="flex-wrap:wrap">
              <button class="btn btn-outline btn-sm" data-2fa-sim><i data-icon="key-round"></i> بررسی کد</button>
              <button class="btn btn-ghost btn-sm" data-2fa-disable>غیرفعال‌سازی</button>
            </div>
          </div>
          <div class="card card-pad" style="margin-bottom:18px">
            <h2 class="t-h4 mb-8">تغییر رمز عبور</h2>
            <form data-form data-success-title="رمز تغییر کرد" data-success-msg="از ورودی بعدی با رمز جدید وارد شوید." novalidate style="max-width:420px">
              <div class="field" style="margin-bottom:14px"><label class="field-label" for="curPw">رمز فعلی</label><div class="input-wrap"><input class="input" type="password" id="curPw" required minlength="8" placeholder="••••••••"><button type="button" class="icon-btn" data-pw-toggle="curPw" aria-label="نمایش رمز عبور"><i data-icon="eye"></i></button></div></div>
              <div class="field" style="margin-bottom:14px"><label class="field-label" for="newPw">رمز جدید</label><div class="input-wrap"><input class="input" type="password" id="newPw" required minlength="8" placeholder="حداقل ۸ کاراکتر"><button type="button" class="icon-btn" data-pw-toggle="newPw" aria-label="نمایش رمز عبور"><i data-icon="eye"></i></button></div></div>
              <button class="btn btn-primary" type="submit">تغییر رمز</button>
            </form>
          </div>
          <div class="card card-pad">
            <h2 class="t-h4 mb-8">نشست‌های فعال</h2>
            <table class="kv-table"><tbody>
              <tr><td>Chrome · تهران</td><td class="fa-num">همین حالا <span class="badge badge-green" style="margin-inline-start:6px">این دستگاه</span></td></tr>
              <tr><td>VS Code · تهران</td><td class="fa-num">۲ ساعت پیش</td></tr>
              <tr><td>iPhone · اصفهان</td><td class="fa-num">دیروز</td></tr>
            </tbody></table>
            <button class="btn btn-danger-soft btn-sm mt-16" data-session-kill>خروج از همه دستگاه‌های دیگر</button>
          </div>
        </section>

        <!-- NOTIFICATIONS -->
        <section class="settings-panel" id="panel-notif">
          <h2>اعلان‌ها</h2>
          <p class="panel-desc">کدام رویدادها و از چه کانالی اطلاع بگیرید.</p>
          <div class="card card-pad">
            <div class="setting-row"><div><b>هشدار نرخ خطا</b><p>آستانه ۱٪ در بازه ۱۵ دقیقه</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
            <div class="setting-row"><div><b>هشدار مصرف</b><p>در ۸۰٪ سهمیه ماهانه</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
            <div class="setting-row"><div><b>رویدادهای امنیتی</b><p>ورود جدید و تغییرات حساس</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
            <div class="setting-row"><div><b>خبرنامه محصول</b><p>نسخه‌های جدید SDK و امکانات</p></div><label class="switch"><input type="checkbox"><span class="track"></span></label></div>
            <div class="setting-row"><div><b>ارسال به تلگرام</b><p>اتصال ربات بلو ورتکس</p></div><button class="btn btn-outline btn-sm" data-notif-test>اتصال</button></div>
          </div>
        </section>

        <!-- WEBHOOKS -->
        <section class="settings-panel" id="panel-webhooks">
          <h2>Webhookها</h2>
          <p class="panel-desc">رویدادها را به سیستم خودتان بفرستید — با امضای HMAC.</p>
          <div class="webhook-card">
            <div class="wk-head">
              <div style="flex:1;min-width:0"><b class="t-sm">پرداخت و کاربران</b><span class="badge badge-green" style="margin-inline-start:8px"><span class="dot"></span> فعال</span></div>
              <div class="flex gap-8"><button class="btn btn-ghost btn-sm" data-wk-test><i data-icon="send"></i> ارسال نمونه</button><button class="btn btn-ghost btn-sm" data-wk-edit aria-label="ویرایش وب‌هوک"><i data-icon="pencil"></i></button></div>
            </div>
            <div class="wk-url">https://api.abrino.ir/webhooks/bluevertex</div>
            <div class="wk-events"><span class="badge badge-blue">payment.updated</span><span class="badge badge-blue">user.created</span><span class="badge badge-blue">user.updated</span></div>
            <div class="wk-stats"><span>۳۲۰ تحویل</span><span>موفقیت: ۹۹٫۴٪</span><span>آخرین: ۱۲ دقیقه پیش</span></div>
          </div>
          <button class="btn btn-primary btn-sm" data-wk-add><i data-icon="plus"></i> Webhook جدید</button>
        </section>

        <!-- API -->
        <section class="settings-panel" id="panel-api">
          <h2>API</h2>
          <p class="panel-desc">تنظیمات عمومی API: نسخه، محدودیت‌ها و آدرس‌های پایه.</p>
          <div class="card card-pad">
            <div class="setting-row"><div><b>پایه آدرس</b><p>آدرس پایه همه Endpointها</p></div><code class="inline text-code ltr">https://api.bluevertex.ir/v1</code></div>
            <div class="setting-row"><div><b>حداکثر نرخ پیش‌فرض</b><p>برای کلیدهای بدون تنظیم خاص</p></div><select class="select" aria-label="حداکثر نرخ پیش‌فرض" style="width:auto"><option>۶۰ در دقیقه</option><option>۳۰۰ در دقیقه</option><option selected>۱٬۰۰۰ در دقیقه</option></select></div>
            <div class="setting-row"><div><b>زمان‌بندی timeout</b><p>پیش‌فرض برای همه درخواست‌ها</p></div><select class="select" aria-label="زمان‌بندی timeout" style="width:auto"><option>۱۰ ثانیه</option><option selected>۳۰ ثانیه</option><option>۶۰ ثانیه</option></select></div>
            <div class="setting-row"><div><b>اعلان تغییرات API</b><p>در صورت خروجی breaking</p></div><label class="switch"><input type="checkbox" checked><span class="track"></span></label></div>
          </div>
        </section>

        <!-- MEMBERS -->
        <section class="settings-panel" id="panel-members">
          <h2>اعضا و دسترسی‌ها</h2>
          <p class="panel-desc">خلاصه دسترسی‌های تیم — مدیریت کامل در صفحه «تیم».</p>
          <div class="card card-pad">
            <div class="flex gap-12 mb-16" style="flex-wrap:wrap">
              <span class="avatar-stack" style="display:flex"><span class="avatar">س</span><span class="avatar" style="background:linear-gradient(135deg,#34D399,#065F46)">ع</span><span class="avatar" style="background:linear-gradient(135deg,#A78BFA,#4C1D95)">م</span><span class="avatar" style="background:linear-gradient(135deg,#FBBF24,#92400E)">ر</span></span>
              <span class="badge">۶ عضو</span><span class="badge">۳ نقش</span>
            </div>
            <a class="btn btn-outline btn-sm" href="team.html">مدیریت اعضای تیم <i data-icon="arrow-left"></i></a>
          </div>
        </section>

        <!-- APPEARANCE -->
        <section class="settings-panel" id="panel-appearance">
          <h2>ظاهر</h2>
          <p class="panel-desc">حالت نمایش و رنگ سازمانی کنسول.</p>
          <div class="card card-pad">
            <div class="setting-row"><div><b>حالت نمایش</b><p>حالت تیره برای کار طولانی؛ حالت روشن برای محیط‌های پرنور</p></div>
              <div class="segmented" data-theme-seg>
                <button data-theme-opt="dark" class="active"><i data-icon="moon"></i> تیره <span class="badge badge-blue" style="font-size:.6rem">پیش‌فرض</span></button>
                <button data-theme-opt="light"><i data-icon="sun"></i> روشن</button>
              </div></div>
            <div class="setting-row" style="align-items:flex-start"><div><b>رنگ سازمانی</b><p>رنگ تاکیدی کنسول — روی همه بخش‌ها اعمال می‌شود</p></div>
              <div class="flex gap-8" id="accentPicker">
                <button class="color-swatch" data-accent="blue" title="آبی" aria-label="رنگ آبی" style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,#3B82F6,#1D4ED8);border:2px solid var(--bg)"></button>
                <button class="color-swatch" data-accent="sky" title="آبی آسمانی" aria-label="رنگ آبی آسمانی" style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,#38BDF8,#0284C7);border:2px solid transparent"></button>
                <button class="color-swatch" data-accent="violet" title="بنفش" aria-label="رنگ بنفش" style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,#A78BFA,#6D28D9);border:2px solid transparent"></button>
                <button class="color-swatch" data-accent="emerald" title="سبز" aria-label="رنگ سبز" style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,#34D399,#047857);border:2px solid transparent"></button>
              </div></div>
            <div class="setting-row"><div><b>تراکم اطلاعات</b><p>فاصله‌های جدول‌ها و کارت‌ها</p></div>
              <div class="segmented" data-density>
                <button>فشرده</button><button class="active">راحت</button>
              </div></div>
          </div>
        </section>

        <!-- DANGER -->
        <section class="settings-panel" id="panel-danger">
          <div class="danger-zone">
            <h2><i data-icon="alert-triangle"></i> منطقه خطر</h2>
            <p>این عملیات‌ها غیرقابل بازگشت هستند. قبل از هر اقدام، مطمئن شوید و در صورت نیاز با پشتیبانی هماهنگ کنید.</p>
            <div class="setting-row" style="border-color:var(--red-line)"><div><b>انتقال مالکیت</b><p>به یک عضو دیگر — شما به نقش مدیر منتقل می‌شوید.</p></div><button class="btn btn-outline btn-sm">انتقال</button></div>
            <div class="setting-row" style="border-color:var(--red-line)"><div><b>حذف فضای کاری</b><p>همه داده‌ها، کلیدها و گزارش‌ها برای همیشه حذف می‌شوند.</p></div><button class="btn btn-danger-soft btn-sm" id="dangerDelete">حذف فضای کاری</button></div>
          </div>
        </section>
      </div>
    </div>

    <div class="modal-backdrop" id="dangerModal" role="dialog" aria-modal="true" aria-label="حذف فضای کاری">
      <div class="modal modal-sm">
        <div class="modal-head"><div><h2 style="color:var(--red)">حذف فضای کاری «ابرینو»</h2><p>این عملیات غیرقابل بازگشت است.</p></div>
          <button class="modal-close" data-modal-close="dangerModal" aria-label="بستن"><i data-icon="x"></i></button></div>
        <div class="modal-body">
          <div class="field"><label class="field-label">برای تأیید، عبارت <code class="inline">حذف ابرینو</code> را بنویسید</label>
            <input class="input ltr" dir="ltr" id="dangerConfirm" placeholder="حذف ابرینو"></div>
        </div>
        <div class="modal-foot">
          <button class="btn btn-ghost" data-modal-close="dangerModal">انصراف</button>
          <button class="btn btn-danger" id="dangerConfirmBtn" disabled>حذف کامل</button>
        </div>
      </div>
    </div>
'''
    return dash_page('تنظیمات', 'dashboard/settings.html', 'تنظیمات', 'پروفایل، فضای کاری، امنیت و ترجیحات — فضای کاری ابرینو', content,
                     extra_scripts='''<script>
(function(){
  var navs = document.querySelectorAll('[data-settings-nav]');
  navs.forEach(function(a){
    a.addEventListener('click', function(e){
      e.preventDefault();
      navs.forEach(function(x){ x.classList.remove('active'); });
      a.classList.add('active');
      var target = a.getAttribute('data-settings-nav');
      document.querySelectorAll('.settings-panel').forEach(function(p){
        p.classList.toggle('active', p.id === 'panel-' + target);
      });
      if (window.BV) window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  });
  var goto = document.querySelector('[data-goto-danger]');
  if (goto) goto.addEventListener('click', function(e){
    e.preventDefault();
    document.querySelectorAll('[data-settings-nav]').forEach(function(x){ x.classList.remove('active'); });
    document.querySelector('[data-settings-nav="danger"]').classList.add('active');
    document.querySelectorAll('.settings-panel').forEach(function(p){ p.classList.remove('active'); });
    document.getElementById('panel-danger').classList.add('active');
  });
  document.getElementById('dangerDelete').addEventListener('click', function(){
    if (window.BV) BV.openModal('dangerModal');
  });
  var inp = document.getElementById('dangerConfirm');
  var btn = document.getElementById('dangerConfirmBtn');
  inp.addEventListener('input', function(){
    btn.disabled = inp.value.trim() !== 'حذف ابرینو';
  });
  btn.addEventListener('click', function(){
    btn.classList.add('btn-loading');
    setTimeout(function(){
      btn.classList.remove('btn-loading');
      if (window.BV) { BV.closeModal('dangerModal'); BV.toast('error', 'عملیات دمو', 'در نسخه دمو، حذف فضای کاری شبیه‌سازی و لغو شد.'); }
    }, 1000);
  });
  document.querySelectorAll('[data-upload-demo], [data-wk-add]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('info', 'در نسخه دمو', 'این عملیات شبیه‌سازی می‌شود.');
    });
  });
  document.querySelectorAll('[data-2fa-sim]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', 'کد صحیح است', 'ورود دومرحله‌ای بدون مشکل کار می‌کند. (دمو)');
    });
  });
  document.querySelectorAll('[data-2fa-disable], [data-session-kill]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('warning', 'تأیید لازم است', 'این عملیات حساس نیاز به تأیید دومرحله‌ای دارد. (دمو)');
    });
  });
  document.querySelectorAll('[data-wk-test], [data-wk-edit]').forEach(function(b){
    b.addEventListener('click', function(){
      if (window.BV) BV.toast('success', 'Webhook', 'در نسخه دمو: ارسال نمونه / ویرایش شبیه‌سازی شد.');
    });
  });
  /* accent color */
  var accents = {
    blue:   { '--blue-600': '#1D4ED8', '--blue-500': '#2563EB', '--blue-400': '#3B82F6', '--blue-300': '#60A5FA', '--electric': '#38BDF8', '--blue-soft': 'rgba(37,99,235,.14)', '--blue-line': 'rgba(59,130,246,.35)', '--blue-glow': 'rgba(56,189,248,.22)', '--border-focus': 'rgba(59,130,246,.55)' },
    sky:    { '--blue-600': '#0284C7', '--blue-500': '#0EA5E9', '--blue-400': '#38BDF8', '--blue-300': '#7DD3FC', '--electric': '#22D3EE', '--blue-soft': 'rgba(14,165,233,.14)', '--blue-line': 'rgba(56,189,248,.35)', '--blue-glow': 'rgba(34,211,238,.2)', '--border-focus': 'rgba(56,189,248,.55)' },
    violet: { '--blue-600': '#6D28D9', '--blue-500': '#7C3AED', '--blue-400': '#A78BFA', '--blue-300': '#C4B5FD', '--electric': '#A78BFA', '--blue-soft': 'rgba(124,58,237,.16)', '--blue-line': 'rgba(167,139,250,.35)', '--blue-glow': 'rgba(167,139,250,.22)', '--border-focus': 'rgba(167,139,250,.55)' },
    emerald:{ '--blue-600': '#047857', '--blue-500': '#059669', '--blue-400': '#34D399', '--blue-300': '#6EE7B7', '--electric': '#34D399', '--blue-soft': 'rgba(5,150,105,.14)', '--blue-line': 'rgba(52,211,153,.35)', '--blue-glow': 'rgba(52,211,153,.2)', '--border-focus': 'rgba(52,211,153,.5)' }
  };
  document.querySelectorAll('.color-swatch').forEach(function(s){
    s.addEventListener('click', function(){
      var a = accents[s.getAttribute('data-accent')];
      if (!a) return;
      for (var k in a) document.documentElement.style.setProperty(k, a[k]);
      document.querySelectorAll('.color-swatch').forEach(function(x){ x.style.borderColor = 'transparent'; });
      s.style.borderColor = '#fff';
      if (window.BV) BV.toast('success', 'رنگ سازمانی تغییر کرد', 'تم کنسول با موفقیت به‌روزرسانی شد. (دمو)');
    });
  });
  var dseg = document.querySelector('[data-density]');
  dseg.querySelectorAll('button').forEach(function(b){
    b.addEventListener('click', function(){
      dseg.querySelectorAll('button').forEach(function(x){ x.classList.remove('active'); });
      b.classList.add('active');
      if (window.BV) BV.toast('info', b.textContent, 'تراکم در نسخه دمو ثبت شد.');
    });
  });
  /* anchor deep-link: #security */
  var hash = location.hash.replace('#', '').replace(/^panel-/, '');
  if (hash && ['general','workspace','security','notif','webhooks','api','members','appearance','danger'].indexOf(hash) > -1) {
    var target = document.querySelector('[data-settings-nav="' + hash + '"]');
    if (target) target.click();
  }
})();
</script>''')
