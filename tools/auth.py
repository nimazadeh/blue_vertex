# -*- coding: utf-8 -*-
"""Blue Vertex — auth: login / register / forgot-password"""

from chrome import head, palette, scripts

def auth_shell(title, brand_link, inner, prefix='../'):
    return head(
        title[0], title[1], '../') + f'''<body class="noise">
<button class="fixed-theme-toggle" data-theme-toggle aria-label="تغییر حالت نمایش" title="حالت روشن"><i data-icon="sun"></i></button>
<div class="auth-wrap">
  <aside class="auth-side" aria-hidden="true">
    <div class="glow"></div><div class="glow two"></div>
    <a class="brand" href="../index.html" style="position:relative;z-index:2">
      <span class="brand-mark"><i data-icon="zap"></i></span>
      <span class="brand-name">بلو ورتکس<small>BLUE VERTEX</small></span>
    </a>
    <div class="auth-quote">
      <blockquote>«بالاخره یک داشبورد توسعه‌دهنده که نه ترجمه است، نه تقلید؛ واقعاً فارسی فکر شده.»</blockquote>
      <footer><span class="avatar">س</span><span><b>سارا احمدی</b><br>مدیر فنی · ابرینو</span></footer>
    </div>
    <div class="flex gap-24" style="position:relative;z-index:2;flex-wrap:wrap">
      <span class="status-ind st-green"><span class="pulse"></span> همه سرویس‌ها فعال</span>
      <span class="t-caption fa-num">آپ‌تایم ۳۰ روز: ۹۹٫۹۸٪</span>
    </div>
  </aside>
  <main class="auth-main">
    <div class="auth-box">
      <a class="auth-logo" href="../index.html"><span class="brand-mark"><i data-icon="zap"></i></span><span class="brand-name">بلو ورتکس<small>BLUE VERTEX</small></span></a>
      {inner}
    </div>
    <div class="auth-footer">
      <span>© ۱۴۰۵ بلو استودیو · Blue Studio — <a href="../pages/contact.html">پشتیبانی</a></span>
    </div>
  </main>
</div>
''' + palette(prefix) + scripts(prefix, extra='')

LOGIN_BODY = '''
<h1 class="auth-title">ورود به کنسول</h1>
<p class="auth-sub">به فضای توسعه‌دهنده خود خوش آمدید.</p>

<div class="auth-error-box" id="loginError" role="alert">
  <i data-icon="alert-circle"></i>
  <span><b>ورود ناموفق بود.</b><br>ایمیل یا رمز عبور اشتباه است. (نسخه دمو: هر ایمیل و رمز با ۸+ کاراکتر پذیرفته می‌شود)</span>
</div>

<form data-form data-redirect="../dashboard/index.html" data-success-title="ورود موفق" data-success-msg="در حال انتقال به داشبورد…" novalidate>
  <div class="field" style="margin-bottom:16px">
    <label class="field-label" for="loginEmail">ایمیل <span class="req">*</span></label>
    <input class="input" id="loginEmail" name="email" type="email" placeholder="you@company.ir" required autocomplete="email" data-autofocus>
    <span class="field-error"></span>
  </div>
  <div class="field">
    <label class="field-label" for="loginPw">رمز عبور <span class="req">*</span></label>
    <div class="input-wrap">
      <input class="input" id="loginPw" name="password" type="password" placeholder="••••••••" required minlength="8" autocomplete="current-password">
      <button type="button" class="icon-btn" data-pw-toggle="loginPw" aria-label="نمایش رمز"><i data-icon="eye"></i></button>
    </div>
    <span class="field-error"></span>
  </div>
  <div class="auth-options">
    <label class="check"><input type="checkbox" name="remember" checked><span class="box"><i data-icon="check"></i></span><span>مرا به خاطر بسپار</span></label>
    <a class="link" href="forgot-password.html" style="font-size:var(--fs-caption)">فراموشی رمز عبور؟</a>
  </div>
  <button class="btn btn-primary btn-lg btn-block" type="submit">ورود به کنسول <i data-icon="arrow-left"></i></button>
  <div class="or-divider" style="margin:22px 0"><span>یا</span></div>
  <div class="grid-2" style="gap:10px">
    <button class="btn btn-outline" type="button" data-oauth="google"><i data-icon="globe"></i> گوگل</button>
    <button class="btn btn-outline" type="button" data-oauth="github"><i data-icon="github"></i> گیت‌هاب</button>
  </div>
  <p class="text-center t-sm" style="margin-top:26px;color:var(--text-3)">حساب ندارید؟ <a class="link" href="register.html">ثبت‌نام رایگان</a></p>
</form>
'''

REGISTER_BODY = '''
<h1 class="auth-title">ساخت حساب رایگان</h1>
<p class="auth-sub">پلتفرم توسعه‌دهنده خود را در ۲ دقیقه بسازید.</p>

<div class="auth-success-box" data-form-success style="display:none">
  <i data-icon="check-circle-2"></i>
  <span><b>حساب شما ساخته شد!</b><br>در حال آماده‌سازی فضای کاری شما…</span>
</div>

<form data-form data-redirect="../dashboard/index.html" data-success-title="ثبت‌نام موفق" data-success-msg="خوش آمدید؛ فضای کاری شما آماده شد." novalidate>
  <div class="field" style="margin-bottom:16px">
    <label class="field-label" for="regName">نام و نام خانوادگی <span class="req">*</span></label>
    <input class="input" id="regName" type="text" placeholder="مثلاً: سارا احمدی" required data-autofocus>
    <span class="field-error"></span>
  </div>
  <div class="field" style="margin-bottom:16px">
    <label class="field-label" for="regCompany">نام شرکت (اختیاری)</label>
    <input class="input" id="regCompany" type="text" placeholder="مثلاً: ابرینو">
  </div>
  <div class="field" style="margin-bottom:16px">
    <label class="field-label" for="regEmail">ایمیل کاری <span class="req">*</span></label>
    <input class="input" id="regEmail" type="email" placeholder="you@company.ir" required autocomplete="email">
    <span class="field-error"></span>
  </div>
  <div class="grid-2" style="gap:14px;margin-bottom:16px">
    <div class="field">
      <label class="field-label" for="regPw">رمز عبور <span class="req">*</span></label>
      <div class="input-wrap">
        <input class="input" id="regPw" type="password" placeholder="حداقل ۸ کاراکتر" required minlength="8" autocomplete="new-password">
        <button type="button" class="icon-btn" data-pw-toggle="regPw" aria-label="نمایش رمز"><i data-icon="eye"></i></button>
      </div>
      <span class="field-error"></span>
    </div>
    <div class="field">
      <label class="field-label" for="regPw2">تکرار رمز <span class="req">*</span></label>
      <input class="input" id="regPw2" name="password2" type="password" placeholder="همان رمز بالا" required>
      <span class="field-error"></span>
    </div>
  </div>
  <div class="security-note" style="margin:0 0 18px">
    <i data-icon="shield-check"></i>
    <span>رمز شما با الگوریتم bcrypt هش می‌شود و هرگز به‌صورت خام ذخیره نمی‌شود. برای امنیت بیشتر بعد از ثبت‌نام، ورود دومرحله‌ای را فعال کنید.</span>
  </div>
  <label class="check" style="margin-bottom:22px"><input type="checkbox" required><span class="box"><i data-icon="check"></i></span><span><a class="link" href="#" style="font-size:inherit">قوانین و حریم خصوصی</a> را می‌پذیرم.</span></label>
  <button class="btn btn-primary btn-lg btn-block" type="submit">ایجاد حساب <i data-icon="arrow-left"></i></button>
  <p class="text-center t-sm" style="margin-top:22px;color:var(--text-3)">حساب دارید؟ <a class="link" href="login.html">وارد شوید</a></p>
</form>
'''

FORGOT_BODY = '''
<h1 class="auth-title">بازیابی رمز عبور</h1>
<p class="auth-sub">ایمیل خود را وارد کنید؛ لینک بازیابی برایتان می‌فرستیم.</p>

<div class="auth-success-box" data-form-success style="display:none">
  <i data-icon="mail-check"></i>
  <span><b>ایمیل بازیابی ارسال شد.</b><br>لینک بازیابی تا ۳۰ دقیقه معتبر است. پوشه اسپم را هم چک کنید.</span>
</div>

<form data-form data-success-toast="none" novalidate>
  <div class="field" style="margin-bottom:22px">
    <label class="field-label" for="fpEmail">ایمیل <span class="req">*</span></label>
    <input class="input" id="fpEmail" type="email" placeholder="you@company.ir" required data-autofocus>
    <span class="field-error"></span>
  </div>
  <button class="btn btn-primary btn-lg btn-block" type="submit">ارسال لینک بازیابی</button>
  <div class="or-divider" style="margin:22px 0"><span>به خاطر آوردید؟</span></div>
  <a class="btn btn-outline btn-block" href="login.html">بازگشت به ورود</a>
</form>
'''

def build_login(prefix='../'):
    return auth_shell(('ورود به کنسول | بلو ورتکس', 'ورود به کنسول توسعه‌دهنده بلو ورتکس'), None, LOGIN_BODY) + '''
<script>
(function(){
  var form = document.querySelector('form[data-form]');
  var errBox = document.getElementById('loginError');
  form.addEventListener('bv:form-success', function(){
    errBox.classList.remove('show');
  });
  document.querySelectorAll('[data-oauth]').forEach(function(b){
    b.addEventListener('click', function(){
      b.classList.add('btn-loading');
      setTimeout(function(){ b.classList.remove('btn-loading'); }, 1200);
      if (window.BV) BV.toast('info', 'ورود با ' + b.textContent.trim(), 'در نسخه دمو، ورود OAuth شبیه‌سازی می‌شود.');
    });
  });
})();
</script>
</body></html>'''

def build_register(prefix='../'):
    return auth_shell(('ثبت‌نام رایگان | بلو ورتکس', 'ساخت حساب رایگان در پلتفرم توسعه‌دهنده بلو ورتکس'), None, REGISTER_BODY) + '</body></html>'

def build_forgot(prefix='../'):
    return auth_shell(('فراموشی رمز عبور | بلو ورتکس', 'بازیابی رمز عبور حساب بلو ورتکس'), None, FORGOT_BODY) + '</body></html>'
