"""Builds the BiswaPath static site into ./site (English at /, Bengali at /bn/).
Run: python3 build.py   — then everything in ./site is ready to publish."""
import os, html, urllib.parse

SITE = os.path.join(os.path.dirname(__file__), "site")
YEAR = "2026"

T = {  # interface text
 "en": dict(lang="en", other="bn", other_label="বাংলা", skip="Skip to content",
   nav=[("School", "/#school"), ("Universities", "/universities/"), ("Compare systems", "/education-systems/"), ("FAQ", "/faq/"), ("Statistics", "/statistics/"), ("Study abroad", "/#abroad"), ("Research & PhD", "/#research"), ("About", "/about/"), ("Contribute", "/contribute/")],
   foot_nav=[("Education systems compared", "/education-systems/"), ("FAQ", "/faq/"), ("Statistics", "/statistics/"), ("About", "/about/"), ("Contribute", "/contribute/"), ("Editorial policy", "/editorial-policy/"), ("Privacy", "/privacy/")],
   foot="BiswaPath is free for every student, always. Founded by Dr Sumit Konar.",
   soon="In preparation"),
 "bn": dict(lang="bn", other="en", other_label="English", skip="মূল লেখায় যান",
   nav=[("স্কুল", "/bn/#school"), ("বিশ্ববিদ্যালয়", "/bn/universities/"), ("শিক্ষাব্যবস্থার তুলনা", "/bn/education-systems/"), ("প্রশ্নোত্তর", "/bn/faq/"), ("পরিসংখ্যান", "/bn/statistics/"), ("বিদেশে পড়াশোনা", "/bn/#abroad"), ("গবেষণা ও PhD", "/bn/#research"), ("আমাদের কথা", "/bn/about/"), ("যুক্ত হোন", "/bn/contribute/")],
   foot_nav=[("শিক্ষাব্যবস্থার তুলনা", "/bn/education-systems/"), ("প্রশ্নোত্তর", "/bn/faq/"), ("পরিসংখ্যান", "/bn/statistics/"), ("আমাদের কথা", "/bn/about/"), ("যুক্ত হোন", "/bn/contribute/"), ("সম্পাদকীয় নীতি", "/bn/editorial-policy/"), ("গোপনীয়তা", "/bn/privacy/")],
   foot="বিশ্বপাঠ সব ছাত্রছাত্রীর জন্য সবসময় বিনামূল্যে। প্রতিষ্ঠাতা ড. সুমিত কোনার।",
   soon="প্রস্তুত হচ্ছে"),
}

def other_path(lang, path):
    if lang == "en": return "/bn" + path
    return path[3:] or "/"

def page(lang, path, title, desc, body, current=None):
    t = T[lang]
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if current == h else ""}>{l}</a>' for l, h in t["nav"])
    fnav = "".join(f'<a href="{h}">{l}</a>' for l, h in t["foot_nav"])
    alt = other_path(lang, path)
    home = "/" if lang == "en" else "/bn/"
    full_title = f"{title} | BiswaPath · বিশ্বপাঠ" if title else "BiswaPath · বিশ্বপাঠ"
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="alternate" hreflang="en" href="https://biswapath.pages.dev{path if lang=='en' else alt}">
<link rel="alternate" hreflang="bn" href="https://biswapath.pages.dev{path if lang=='bn' else alt}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BiswaPath · বিশ্বপাঠ">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="https://biswapath.pages.dev{path}">
<meta property="og:image" content="https://biswapath.pages.dev/assets/biswapath-share.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/tiro-bangla-bengali-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<script src="/assets/rule.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
<div class="page">
<header class="wrap top">
  <a class="brand" href="{home}"><span class="bn" lang="bn">বিশ্বপাঠ</span><span class="en" lang="en">BiswaPath</span></a>
  <nav class="nav" aria-label="Main">{nav}<a class="lang" href="{alt}" lang="{t['other']}" hreflang="{t['other']}">{t['other_label']}</a></nav>
</header>
<main id="main">
{body}
</main>
<footer class="wrap foot">
  <nav aria-label="Footer">{fnav}</nav>
  <p><a href="https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote('https://biswapath.pages.dev' + path, safe='')}" target="_blank" rel="noopener">{'Share this page on LinkedIn' if lang=='en' else 'এই পেজটি LinkedIn-এ শেয়ার করুন'}</a></p>
  <p>{t['foot']} © {YEAR}</p>
</footer>
</div>
</body>
</html>
"""

def res_list(items, soon):
    return '<ul class="res">' + "".join(f'<li><span>{i}</span><span class="when">{soon}</span></li>' for i in items) + "</ul>"

# ---------- HOME ----------
HOME = {
 "en": dict(
   meaning='<em lang="bn">পাঠ</em> means a lesson. <em lang="bn">পথ</em> means a path. In English letters both are written “path”, and BiswaPath means both: learning from the world, and a path into it.',
   lede="Free learning and honest guidance for Bengali-speaking students in West Bengal, Bangladesh and around the world, from school chemistry to a funded PhD.",
   path_h="Your path", path_intro="Three stages, one journey. Every resource is free and checked by a person before it is published.",
   stops=[
     ("school", "School", "স্কুল", "Clear explanations and practice questions, starting with chemistry.",
      ["Moles without fear: a step-by-step guide", "Reading the periodic table: what the patterns tell you"]),
     ("abroad", "Study abroad", "বিদেশে পড়াশোনা", "Practical guides to studying overseas, starting with the UK. Visa and fee information always links to the official source.",
      ["Studying in the UK: a first guide for Bengali students", "Scholarships for UK study: where to look"]),
     ("research", "Research & PhD", "গবেষণা ও PhD", "How research careers really work, from finding a funded PhD to your first paper.",
      ["How to find a funded PhD", "Writing to a potential supervisor"]),
   ],
   help_h="Help build BiswaPath", help_p="Teachers, researchers and students: if you can explain one topic well, you can help thousands of students. Contributions are voluntary and every article carries its author's name.",
   help_btn="Become a contributor",
   founder_h="Why this exists",
   founder_p=["I am Dr Sumit Konar, a chemist living in the UK. I grew up learning in Bengali, and I know how much a clear explanation or one honest piece of advice can change a student's path.",
              "BiswaPath will stay free for students, always. No paywalls, no paid courses, and no selling of anyone's data."],
   founder_more="More about BiswaPath",
   title="", desc="Free bilingual learning and guidance for Bengali-speaking students: school chemistry, studying abroad, and research and PhD careers."),
 "bn": dict(
   meaning='<em>পাঠ</em> মানে শেখা। <em>পথ</em> মানে রাস্তা। ইংরেজি অক্ষরে দুটোই লেখা হয় “path”, আর বিশ্বপাঠ মানে দুটোই: বিশ্ব থেকে শেখা, আর বিশ্বের দিকে এগিয়ে যাওয়ার পথ।',
   lede="পশ্চিমবঙ্গ, বাংলাদেশ আর সারা পৃথিবীর বাংলাভাষী ছাত্রছাত্রীদের জন্য বিনামূল্যে পড়াশোনা আর সৎ পরামর্শ: স্কুলের কেমিস্ট্রি থেকে স্কলারশিপসহ PhD পর্যন্ত।",
   path_h="আপনার পথ", path_intro="তিনটি ধাপ, একটাই যাত্রা। প্রতিটি লেখা বিনামূল্যে, আর প্রকাশের আগে একজন মানুষ নিজে যাচাই করেন।",
   stops=[
     ("school", "স্কুল", "School", "সহজ ব্যাখ্যা আর অনুশীলনের প্রশ্ন, শুরু কেমিস্ট্রি দিয়ে।",
      ["মোল ধারণা: ভয় ছাড়াই, ধাপে ধাপে", "পর্যায় সারণি পড়তে শেখা: প্যাটার্নগুলো কী বলে"]),
     ("abroad", "বিদেশে পড়াশোনা", "Study abroad", "বিদেশে পড়তে যাওয়ার কাজের গাইড, শুরু UK দিয়ে। ভিসা আর ফি-র তথ্যে সবসময় অফিসিয়াল সূত্রের লিংক থাকবে।",
      ["UK-তে পড়াশোনা: বাঙালি ছাত্রছাত্রীদের প্রথম গাইড", "UK-তে পড়ার স্কলারশিপ: কোথায় খুঁজবেন"]),
     ("research", "গবেষণা ও PhD", "Research & PhD", "গবেষণার কেরিয়ার আসলে কীভাবে চলে: স্কলারশিপসহ PhD খোঁজা থেকে প্রথম পেপার পর্যন্ত।",
      ["স্কলারশিপসহ PhD কীভাবে খুঁজবেন", "সম্ভাব্য সুপারভাইজারকে কীভাবে ইমেল লিখবেন"]),
   ],
   help_h="বিশ্বপাঠ গড়ে তুলতে সাহায্য করুন", help_p="শিক্ষক, গবেষক বা ছাত্রছাত্রী: একটা বিষয় ভালো করে বোঝাতে পারলে আপনি হাজারো ছাত্রছাত্রীকে সাহায্য করতে পারেন। যুক্ত হওয়া স্বেচ্ছায়, আর প্রতিটি লেখায় লেখকের নাম থাকবে।",
   help_btn="লেখক হিসেবে যুক্ত হোন",
   founder_h="কেন এই উদ্যোগ",
   founder_p=["আমি ড. সুমিত কোনার, UK-তে থাকা একজন রসায়নবিদ। আমি বাংলায় পড়াশোনা করে বড় হয়েছি, আর জানি একটা পরিষ্কার ব্যাখ্যা বা একটা সৎ পরামর্শ একজন ছাত্রের পথ কতটা বদলে দিতে পারে।",
              "বিশ্বপাঠ ছাত্রছাত্রীদের জন্য সবসময় বিনামূল্যে থাকবে। কোনো পেওয়াল নেই, পেইড কোর্স নেই, কারও তথ্য বিক্রি নেই।"],
   founder_more="বিশ্বপাঠ সম্পর্কে আরও",
   title="", desc="বাংলাভাষী ছাত্রছাত্রীদের জন্য বিনামূল্যে দ্বিভাষিক পড়াশোনা ও পরামর্শ: স্কুলের কেমিস্ট্রি, বিদেশে পড়াশোনা, গবেষণা ও PhD।"),
}

def home(lang):
    c = HOME[lang]; t = T[lang]; pre = "" if lang == "en" else "/bn"
    stops = ""
    for sid, h, other, p, items in c["stops"]:
        other_lang = "bn" if lang == "en" else "en"
        stops += f'<li class="stop" id="{sid}"><h3>{h}<span class="other" lang="{other_lang}">{other}</span></h3><p>{p}</p>{res_list(items, t["soon"])}</li>'
    body = f"""
<section class="hero" aria-label="BiswaPath"><div class="wrap">
  <h1 class="wordmark"><span lang="bn">বিশ্বপাঠ</span><span class="latin" lang="en">BiswaPath</span></h1>
  <p class="meaning">{c['meaning']}</p>
  <p class="lede">{c['lede']}</p>
</div></section>
<section class="wrap section" aria-labelledby="path-h">
  <h2 id="path-h">{c['path_h']}</h2>
  <p class="intro">{c['path_intro']}</p>
  <ol class="stops">{stops}</ol>
</section>
<section class="wrap section" aria-labelledby="help-h">
  <h2 id="help-h">{c['help_h']}</h2>
  <div class="invite"><p>{c['help_p']}</p><a class="btn" href="{pre}/contribute/">{c['help_btn']}</a></div>
</section>
<section class="wrap section" aria-labelledby="why-h">
  <h2 id="why-h">{c['founder_h']}</h2>
  <div class="founder"><div class="initials" aria-hidden="true">সু</div><div>{''.join(f'<p>{x}</p>' for x in c['founder_p'])}<p><a href="{pre}/about/">{c['founder_more']}</a></p></div></div>
</section>"""
    return page(lang, "/" if lang == "en" else "/bn/", c["title"], c["desc"], body)

# ---------- PROSE PAGES ----------
PAGES = {
 "about": {
  "en": ("About BiswaPath", "What BiswaPath is, who runs it, and the promises it makes to students.", """
<p>BiswaPath (বিশ্বপাঠ) is a free, independent education website for Bengali-speaking students in West Bengal, Bangladesh and around the world. It covers three stages of a student's journey: school, studying abroad, and research and PhD careers.</p>
<h2>Our promises</h2>
<ul>
<li>Free for students, permanently. No subscriptions, paid courses or premium content.</li>
<li>Checked by people. Every article is reviewed by a person before it is published, including anything drafted with AI tools.</li>
<li>Official sources first. Visa, fee and scholarship information always links to the official page.</li>
<li>Your data is not for sale.</li>
</ul>
<h2>Founder</h2>
<p>BiswaPath was founded in 2026 by Dr Sumit Konar, a chemist with a PhD and international research experience, based in the UK. He also runs <a href="https://www.sumitkonar.com/">Global Puja Parikrama</a>, a map of Durga Pujas around the world.</p>
<h2>How it is built</h2>
<p>The website is built with the help of AI tools (Claude and ChatGPT) and reviewed by people. Content is written or checked by named contributors.</p>
<h2>A note on advice</h2>
<p>BiswaPath gives general information, not personal advice. For visa or immigration questions, always use the official government website or a regulated adviser.</p>
"""),
  "bn": ("বিশ্বপাঠ সম্পর্কে", "বিশ্বপাঠ কী, কে চালান, আর ছাত্রছাত্রীদের কাছে আমাদের প্রতিশ্রুতি।", """
<p>বিশ্বপাঠ (BiswaPath) পশ্চিমবঙ্গ, বাংলাদেশ আর সারা পৃথিবীর বাংলাভাষী ছাত্রছাত্রীদের জন্য একটি বিনামূল্যের, স্বাধীন শিক্ষামূলক ওয়েবসাইট। এখানে একজন ছাত্রের যাত্রার তিনটি ধাপ নিয়ে লেখা থাকবে: স্কুল, বিদেশে পড়াশোনা, আর গবেষণা ও PhD কেরিয়ার।</p>
<h2>আমাদের প্রতিশ্রুতি</h2>
<ul>
<li>ছাত্রছাত্রীদের জন্য চিরকাল বিনামূল্যে। কোনো সাবস্ক্রিপশন, পেইড কোর্স বা প্রিমিয়াম কনটেন্ট নেই।</li>
<li>মানুষের যাচাই। প্রতিটি লেখা প্রকাশের আগে একজন মানুষ যাচাই করেন, AI-র সাহায্যে লেখা হলেও।</li>
<li>আগে অফিসিয়াল সূত্র। ভিসা, ফি আর স্কলারশিপের তথ্যে সবসময় অফিসিয়াল পেজের লিংক থাকবে।</li>
<li>আপনার তথ্য বিক্রির জন্য নয়।</li>
</ul>
<h2>প্রতিষ্ঠাতা</h2>
<p>২০২৬ সালে বিশ্বপাঠ শুরু করেন ড. সুমিত কোনার, UK-তে থাকা একজন রসায়নবিদ, যাঁর PhD আর আন্তর্জাতিক গবেষণার অভিজ্ঞতা আছে। তিনি <a href="https://www.sumitkonar.com/">Global Puja Parikrama</a>-ও চালান, সারা পৃথিবীর দুর্গাপুজোর একটি ম্যাপ।</p>
<h2>কীভাবে তৈরি</h2>
<p>ওয়েবসাইটটি AI টুলের (Claude ও ChatGPT) সাহায্যে তৈরি, আর মানুষ যাচাই করেন। প্রতিটি লেখা লেখেন বা যাচাই করেন নাম-সহ লেখকেরা।</p>
<h2>পরামর্শ নিয়ে একটি কথা</h2>
<p>বিশ্বপাঠ সাধারণ তথ্য দেয়, ব্যক্তিগত পরামর্শ নয়। ভিসা বা ইমিগ্রেশনের প্রশ্নে সবসময় সরকারি ওয়েবসাইট বা অনুমোদিত উপদেষ্টার সাহায্য নিন।</p>
""")},
 "contribute": {
  "en": ("Become a contributor", "How teachers, researchers and students can write for BiswaPath.", """
<p>BiswaPath grows through people who explain things well. You do not need to write a lot: one clear article on a topic you know can help thousands of students.</p>
<h2>Who we are looking for</h2>
<ul>
<li>Teachers of chemistry, physics, biology and mathematics</li>
<li>Researchers and PhD students in any subject</li>
<li>Bengali students studying abroad who can share their experience</li>
<li>People who can translate carefully between Bengali and English</li>
</ul>
<h2>How it works</h2>
<ol>
<li>Fill in the short form below with your subject and background.</li>
<li>We agree a topic with you.</li>
<li>You write, we review and check facts, and you approve the final version.</li>
<li>The article is published with your name.</li>
</ol>
<p>Contributing is voluntary and unpaid. You keep the right to be named on everything you write.</p>
<p><a class="btn" href="#form-coming">Contributor form (coming soon)</a></p>
"""),
  "bn": ("লেখক হিসেবে যুক্ত হোন", "শিক্ষক, গবেষক আর ছাত্রছাত্রীরা কীভাবে বিশ্বপাঠে লিখতে পারেন।", """
<p>যাঁরা ভালো করে বোঝাতে পারেন, তাঁদের হাত ধরেই বিশ্বপাঠ বড় হবে। অনেক লিখতে হবে না: আপনার জানা একটা বিষয়ে একটা পরিষ্কার লেখা হাজারো ছাত্রছাত্রীকে সাহায্য করতে পারে।</p>
<h2>আমরা কাদের খুঁজছি</h2>
<ul>
<li>কেমিস্ট্রি, ফিজিক্স, বায়োলজি আর অঙ্কের শিক্ষক</li>
<li>যেকোনো বিষয়ের গবেষক আর PhD ছাত্রছাত্রী</li>
<li>বিদেশে পড়তে যাওয়া বাঙালি ছাত্রছাত্রী, যাঁরা নিজেদের অভিজ্ঞতা জানাতে পারেন</li>
<li>যাঁরা যত্ন নিয়ে বাংলা-ইংরেজি অনুবাদ করতে পারেন</li>
</ul>
<h2>কীভাবে কাজ হবে</h2>
<ol>
<li>নিচের ছোট ফর্মে আপনার বিষয় আর পরিচয় লিখুন।</li>
<li>আমরা একসঙ্গে একটা বিষয় ঠিক করব।</li>
<li>আপনি লিখবেন, আমরা যাচাই আর তথ্য-পরীক্ষা করব, শেষ সংস্করণে আপনি সম্মতি দেবেন।</li>
<li>লেখাটি আপনার নাম-সহ প্রকাশিত হবে।</li>
</ol>
<p>যুক্ত হওয়া স্বেচ্ছায় এবং অবৈতনিক। আপনার প্রতিটি লেখায় আপনার নাম থাকবে।</p>
<p><a class="btn" href="#form-coming">লেখকের ফর্ম (শিগগিরই আসছে)</a></p>
""")},
 "editorial-policy": {
  "en": ("Editorial policy", "How BiswaPath checks what it publishes.", """
<p class="updated">Last updated: 19 October 2026</p>
<ul>
<li><strong>Accuracy first.</strong> Every scientific and educational article is fact-checked before publication.</li>
<li><strong>Human review of AI drafts.</strong> AI tools may help draft or translate, but nothing is published without a person reviewing it.</li>
<li><strong>Official sources.</strong> University, scholarship, fee and visa information links to the official source and shows the date it was checked.</li>
<li><strong>Dates on every article.</strong> Each article shows when it was published and last updated.</li>
<li><strong>Named authors.</strong> Contributors are named, and their stated background is checked.</li>
<li><strong>Copyright.</strong> We do not copy exam papers or other people's teaching materials. We link to them.</li>
<li><strong>Natural Bengali.</strong> Translations are reviewed by a Bengali speaker for accuracy and readability.</li>
<li><strong>Corrections.</strong> If you find a mistake, tell us and we will fix it and note the change.</li>
</ul>
"""),
  "bn": ("সম্পাদকীয় নীতি", "বিশ্বপাঠ কীভাবে প্রকাশিত লেখা যাচাই করে।", """
<p class="updated">শেষ আপডেট: ১৯ অক্টোবর ২০২৬</p>
<ul>
<li><strong>আগে নির্ভুলতা।</strong> প্রকাশের আগে প্রতিটি বৈজ্ঞানিক ও শিক্ষামূলক লেখার তথ্য যাচাই করা হয়।</li>
<li><strong>AI-র খসড়া মানুষ দেখেন।</strong> খসড়া বা অনুবাদে AI টুল সাহায্য করতে পারে, কিন্তু একজন মানুষ না দেখে কিছুই প্রকাশিত হয় না।</li>
<li><strong>অফিসিয়াল সূত্র।</strong> বিশ্ববিদ্যালয়, স্কলারশিপ, ফি আর ভিসার তথ্যে অফিসিয়াল সূত্রের লিংক আর যাচাইয়ের তারিখ থাকে।</li>
<li><strong>প্রতিটি লেখায় তারিখ।</strong> কবে প্রকাশিত আর কবে শেষ আপডেট হয়েছে, তা লেখা থাকে।</li>
<li><strong>লেখকের নাম।</strong> লেখকদের নাম থাকে, আর তাঁদের পরিচয় যাচাই করা হয়।</li>
<li><strong>কপিরাইট।</strong> আমরা পরীক্ষার প্রশ্নপত্র বা অন্যের পড়ানোর উপকরণ কপি করি না, লিংক দিই।</li>
<li><strong>স্বাভাবিক বাংলা।</strong> অনুবাদ একজন বাংলাভাষী যাচাই করেন, যাতে নির্ভুল আর সহজপাঠ্য হয়।</li>
<li><strong>সংশোধন।</strong> ভুল পেলে জানান, আমরা ঠিক করব আর পরিবর্তনটা উল্লেখ করব।</li>
</ul>
""")},
 "privacy": {
  "en": ("Privacy notice", "What information BiswaPath collects and why.", """
<p class="updated">Last updated: 19 October 2026</p>
<h2>The short version</h2>
<p>You can read everything on BiswaPath without an account. We do not use advertising cookies, and we do not sell or share your data.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Visit statistics.</strong> We use Cloudflare Web Analytics, which counts page views without cookies and without identifying you.</li>
<li><strong>Forms.</strong> If you fill in our contributor form (run on Google Forms), we receive the details you choose to give, such as your name, email and subject. We use them only to contact you about contributing, and delete them if you ask.</li>
</ul>
<h2>Young people</h2>
<p>Many of our readers are school students. We do not ask students under 18 for personal information, and the site has no accounts, comments or messaging.</p>
<h2>Your rights</h2>
<p>You can ask to see, correct or delete information you have sent us. Contact details will be published here before launch.</p>
<p>Who is responsible: Dr Sumit Konar, United Kingdom.</p>
"""),
  "bn": ("গোপনীয়তা নীতি", "বিশ্বপাঠ কী তথ্য সংগ্রহ করে আর কেন।", """
<p class="updated">শেষ আপডেট: ১৯ অক্টোবর ২০২৬</p>
<h2>সংক্ষেপে</h2>
<p>কোনো অ্যাকাউন্ট ছাড়াই বিশ্বপাঠের সবকিছু পড়া যায়। আমরা বিজ্ঞাপনের কুকি ব্যবহার করি না, আর আপনার তথ্য বিক্রি বা শেয়ার করি না।</p>
<h2>আমরা কী সংগ্রহ করি</h2>
<ul>
<li><strong>ভিজিটের পরিসংখ্যান।</strong> আমরা Cloudflare Web Analytics ব্যবহার করি, যা কুকি ছাড়া এবং আপনাকে চিহ্নিত না করে পেজ ভিউ গোনে।</li>
<li><strong>ফর্ম।</strong> লেখকের ফর্ম (Google Forms-এ) পূরণ করলে আপনি যা জানাতে চান, যেমন নাম, ইমেল আর বিষয়, তা আমরা পাই। শুধু লেখা নিয়ে যোগাযোগের জন্য ব্যবহার করি, আর আপনি চাইলে মুছে দিই।</li>
</ul>
<h2>অল্পবয়সীরা</h2>
<p>আমাদের অনেক পাঠক স্কুলের ছাত্রছাত্রী। ১৮ বছরের কম বয়সী ছাত্রছাত্রীদের কাছে আমরা কোনো ব্যক্তিগত তথ্য চাই না, আর সাইটে কোনো অ্যাকাউন্ট, কমেন্ট বা মেসেজিং নেই।</p>
<h2>আপনার অধিকার</h2>
<p>আপনার পাঠানো তথ্য দেখতে, সংশোধন করতে বা মুছে দিতে বলতে পারেন। লঞ্চের আগে যোগাযোগের ঠিকানা এখানে দেওয়া হবে।</p>
<p>দায়িত্বপ্রাপ্ত: ড. সুমিত কোনার, যুক্তরাজ্য।</p>
""")},
}

def prose(lang, slug):
    title, desc, inner = PAGES[slug][lang]
    path = f"/{slug}/" if lang == "en" else f"/bn/{slug}/"
    body = f'<article class="wrap prose"><h1>{title}</h1>{inner}</article>'
    return page(lang, path, title, desc, body, current=path)


# ---------- UNIVERSITY FINDER ----------
import json as _json
UDATA = _json.load(open(os.path.join(os.path.dirname(__file__), "data", "universities.json"), encoding="utf-8"))
UT = {
 "en": dict(title="University finder", desc="Application fees, deadlines, scholarships and ways to talk to current students at 35 universities in the UK, Germany, Sweden and the USA.",
   h1="University finder", intro="Fees, deadlines and scholarships for 35 universities, with links to talk to current students. Every figure links to the official page it came from. Always check it there before you apply.",
   search="Search a university or city", all="All countries", fee="Postgraduate application fee", deadline="Postgraduate deadlines", tuition="Example tuition", sch="Scholarships", chat="Talk to current students", soc="Indian / Bengali / Bangladeshi societies", ug="Undergraduate", phd="PhD", src="Source", web="Website", none="No university matches. Try another name or country.",
   amb_h="Student ambassadors", amb="Each university's official chat service lets you message current students, and you can usually choose students from India or Bangladesh. We don't publish students' personal details. Are you a Bengali student abroad? Volunteer as a BiswaPath ambassador on the contribute page.",
   checked="Checked 19 October 2026", lang_note="", chat_link="Open the chat page", src_link="Official page"),
 "bn": dict(title="বিশ্ববিদ্যালয় খুঁজুন", desc="UK, জার্মানি, সুইডেন ও USA-র ৩৫টি বিশ্ববিদ্যালয়ের আবেদন ফি, ডেডলাইন, স্কলারশিপ আর বর্তমান ছাত্রছাত্রীদের সঙ্গে কথা বলার উপায়।",
   h1="বিশ্ববিদ্যালয় খুঁজুন", intro="৩৫টি বিশ্ববিদ্যালয়ের ফি, ডেডলাইন আর স্কলারশিপ, সঙ্গে বর্তমান ছাত্রছাত্রীদের সঙ্গে কথা বলার লিংক। প্রতিটি তথ্যের পাশে অফিসিয়াল সূত্রের লিংক আছে। আবেদনের আগে সেখানে অবশ্যই মিলিয়ে নিন।",
   search="বিশ্ববিদ্যালয় বা শহরের নাম লিখুন", all="সব দেশ", fee="পোস্টগ্র্যাজুয়েট আবেদন ফি", deadline="পোস্টগ্র্যাজুয়েট ডেডলাইন", tuition="টিউশন ফি-র উদাহরণ", sch="স্কলারশিপ", chat="বর্তমান ছাত্রছাত্রীদের সঙ্গে কথা বলুন", soc="ভারতীয় / বাঙালি / বাংলাদেশি সোসাইটি", ug="আন্ডারগ্র্যাজুয়েট", phd="PhD", src="সূত্র", web="ওয়েবসাইট", none="কোনো বিশ্ববিদ্যালয় মেলেনি। অন্য নাম বা দেশ দিয়ে চেষ্টা করুন।",
   amb_h="স্টুডেন্ট অ্যাম্বাসেডর", amb="প্রতিটি বিশ্ববিদ্যালয়ের অফিসিয়াল চ্যাট সার্ভিসে বর্তমান ছাত্রছাত্রীদের মেসেজ করা যায়, আর সাধারণত ভারত বা বাংলাদেশের ছাত্রছাত্রী বেছে নেওয়া যায়। আমরা কারও ব্যক্তিগত তথ্য প্রকাশ করি না। আপনি কি বিদেশে পড়া বাঙালি ছাত্র? যুক্ত হোন পেজে বিশ্বপাঠ অ্যাম্বাসেডর হিসেবে নাম দিন।",
   chat_link="চ্যাট পেজ খুলুন", src_link="অফিসিয়াল পেজ", checked="যাচাই: ১৯ অক্টোবর ২০২৬", lang_note='<p class="updated">বিশ্ববিদ্যালয়ের তথ্যগুলো ইংরেজিতে দেওয়া হয়েছে, যাতে অফিসিয়াল পেজের সঙ্গে সহজে মেলানো যায়।</p>'),
}
PHD = {"UK": "Funded PhDs (studentships) are listed on each university's research pages and on FindAPhD; most funding deadlines fall December–March.",
       "Germany": "PhDs are often paid research posts; search the DAAD PhD database and university job pages.",
       "Sweden": "PhD places are paid jobs, advertised as vacancies on university websites.",
       "USA": "PhD offers usually include tuition and a stipend; most applications close in December."}

def universities(lang):
    t = UT[lang]; pre = "" if lang == "en" else "/bn"
    data = {"unis": list(UDATA["unis"].values()), "country": UDATA["country"], "phd": PHD, "t": t}
    body = f"""<article class="wrap prose uni">
<h1>{t['h1']}</h1>
<p>{t['intro']}</p>{t['lang_note']}<p><a href="{pre}/education-systems/">{'How do school and degree stages compare between countries?' if lang=='en' else 'বিভিন্ন দেশে স্কুল আর ডিগ্রির ধাপ কীভাবে মেলে?'}</a></p>
<p><a href="/downloads/BiswaPath_University_Guide_2027.xlsx" download>{'Download the full list as an Excel file' if lang=='en' else 'পুরো তালিকা Excel ফাইল হিসেবে ডাউনলোড করুন'}</a></p>
<div class="ufilters"><input id="uq" type="search" placeholder="{t['search']}" aria-label="{t['search']}">
<select id="uc" aria-label="{t['all']}"><option value="">{t['all']}</option><option>UK</option><option>Germany</option><option>Sweden</option><option>USA</option></select></div>
<div id="ulist"></div>
<h2>{t['amb_h']}</h2><p>{t['amb']}</p><p><a class="btn" href="{pre}/contribute/">{'Volunteer as an ambassador' if lang=='en' else 'অ্যাম্বাসেডর হিসেবে নাম দিন'}</a></p>
<p class="updated">{t['checked']}</p>
</article>
<script>var U={_json.dumps(data, ensure_ascii=False)};</script>
<script src="/assets/universities.js"></script>"""
    path = "/universities/" if lang == "en" else "/bn/universities/"
    return page(lang, path, t["title"], t["desc"], body, current=path)

import edu_page
for _l in ("en", "bn"):
    PAGES.setdefault("education-systems", {})[_l] = edu_page.content(_l)
import faq_page
for _l in ("en", "bn"):
    PAGES.setdefault("faq", {})[_l] = faq_page.content(_l)
import stats_page
for _l in ("en", "bn"):
    PAGES.setdefault("statistics", {})[_l] = stats_page.content(_l)

def write(rel, text):
    p = os.path.join(SITE, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text)

for lang in ("en", "bn"):
    pre = "" if lang == "en" else "bn/"
    write(pre + "index.html", home(lang))
    for slug in PAGES:
        write(f"{pre}{slug}/index.html", prose(lang, slug))
    write(f"{pre}universities/index.html", universities(lang))
write("404.html", page("en", "/404/", "Page not found", "Page not found",
  '<article class="wrap prose"><h1>This page does not exist</h1><p>The link may be old or mistyped. <a href="/">Go to the BiswaPath home page</a>, or <a href="/bn/">বাংলা হোম পেজে যান</a>.</p></article>'))
write("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#fafbf7"/><rect x="14" y="0" width="3" height="64" fill="#c42b2b"/><text x="38" y="46" font-family="serif" font-size="38" text-anchor="middle" fill="#1b3a8c">বি</text></svg>')
write("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://biswapath.pages.dev/sitemap.xml\n")
urls = ["/", "/bn/", "/universities/", "/bn/universities/"] + [f"/{s}/" for s in PAGES] + [f"/bn/{s}/" for s in PAGES]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' +
      "".join(f"<url><loc>https://biswapath.pages.dev{u}</loc></url>" for u in urls) + "</urlset>\n")
print("built", len(urls), "pages")
