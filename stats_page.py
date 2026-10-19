# Content for the "Students abroad: the numbers" page (imported by build.py). Checked 19 Oct 2026.
import re

CHECKED = {"en": "19 October 2026", "bn": "১৯ অক্টোবর ২০২৬"}

SRC = {
 "mea": ("Orissa Post: Ministry of External Affairs written reply in the Rajya Sabha (December 2025)", "https://www.orissapost.com/over-18-lakh-indians-study-abroad-govt-flags-visa-violations-behind-many-deportations/amp/"),
 "od_in": ("Open Doors 2025: India fact sheet (IIE)", "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_India_Fact-Sheet-2025.pdf"),
 "od_bd": ("Open Doors 2025: Bangladesh fact sheet (IIE)", "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_Bangladesh_Fact-Sheet-2025.pdf"),
 "od_pr": ("Open Doors 2025 press release (IIE)", "https://opendoorsdata.org/wp-content/uploads/2025/11/OD25_Open-Doors-2025-Press-Release.pdf"),
 "od_1819": ("Open Doors 2018/19, Indian students by field (chart)", "https://datawrapper.dwcdn.net/MlZW9/1"),
 "ho": ("Home Office: Why do people come to the UK? Study (year ending June 2026)", "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/why-do-people-come-to-the-uk-study"),
 "daad": ("DAAD India: Indian students in Germany at an all-time high (September 2025)", "https://www.daad.in/en/2025/09/22/indian-students-in-germany-at-an-all-time-high/"),
 "pie": ("The PIE News: Indian students in Germany, winter semester 2025/26", "https://thepienews.com/number-of-indian-students-in-germany-rises-to-record-70k-high/"),
 "unesco": ("The Daily Star: Bangladeshi students abroad, UNESCO data (August 2023)", "https://www.thedailystar.net/news/bangladesh/news/number-students-going-abroad-triples-15-years-despite-university-boom-3397431"),
 "icef": ("ICEF Monitor: outbound students from Bangladesh, OECD data (November 2025)", "https://monitor.icef.com/2025/11/the-economic-indicators-driving-outbound-student-mobility-from-bangladesh-indonesia-nepal-and-vietnam/"),
 "tbs": ("TBS News: why UK universities are restricting Bangladeshi and Pakistani recruitment (December 2025)", "https://www.tbsnews.net/explainer/why-are-uk-universities-restricting-recruitment-bangladeshi-pakistani-students-1302001"),
 "the": ("Times Higher Education: Asian international students shift to tech and health courses (July 2025)", "https://www.timeshighereducation.com/node/738245"),
 "mea_annex": ("Ministry of External Affairs: Data on Indian students abroad, as on 1 January 2025 (Annexure I)", "https://www.mea.gov.in/Images/CPV/557-en-01-04-12-2025.pdf"),
 "bt": ("Business Today: fewer Indian students to the US, UK and Canada; Russia and Bangladesh gain (July 2025)", "https://www.businesstoday.in/amp/nri/study/story/india-sees-sharp-fall-in-students-heading-to-us-uk-canada-russia-and-bangladesh-gain-486434-2025-07-26"),
 "cn": ("The Tribune: Indian embassy advisory on studying medicine in China (September 2022)", "https://www.tribuneindia.com/news/nation/india-issues-advisory-outlining-risks-for-students-planning-to-study-medicine-in-china-430391/amp"),
 "jp": ("The Week: language barrier discourages student exchange between India and Japan (December 2025)", "https://www.theweek.in/news/india/2025/12/13/language-barrier-discourages-student-exchange-between-india-and-japan.amp.html"),
 "sg": ("Ministry of Education Singapore: parliamentary reply on the Tuition Grant for international students (April 2024)", "https://www.moe.gov.sg/news/parliamentary-replies/20240402-public-benefit-of-the-tuition-grant-scheme-for-is"),
 "khda": ("Gulf News: Indian students are 43% of Dubai's international intake (KHDA, 2024–25)", "https://gulfnews.com/uae/indian-students-top-dubais-global-intake-at-43-pakistanis-at-6-1.500190286"),
 "qs27": ("QS Top Universities: the world's top 100 universities (QS 2027)", "https://www.topuniversities.com/student-info/choosing-university/worlds-top-100-universities"),
 "au": ("Ardent Overseas: Australia student visa rules 2026 (confirm on immi.homeaffairs.gov.au)", "https://ardentoverseas.com/study-in-australia/student-visa/"),
 "ls": ("Lok Sabha Starred Question 84, 29 July 2024: students going abroad (national totals only)", "https://sabrangindia.in/wp-content/uploads/2024/08/loksabhaquestions_Students-Migration.pdf"),
}
ORDER = list(SRC)

def cite(text):
    return re.sub(r"\[(\w+)\]", lambda m: f'<sup><a href="#src-{m.group(1)}">[{ORDER.index(m.group(1)) + 1}]</a></sup>' if m.group(1) in SRC else m.group(0), text)

IN_DEST = [("Canada", "কানাডা", 4.27), ("USA", "USA", 2.55), ("UAE", "UAE", 2.53), ("Australia", "অস্ট্রেলিয়া", 1.96), ("UK", "UK", 1.73)]
BD_DEST = [("UAE", "UAE", 11157), ("USA", "USA", 8665), ("Malaysia", "মালয়েশিয়া", 6180)]

def bars(rows, lang, fmt, maxv):
    out = '<div class="bars">'
    for en, bn, v in rows:
        out += (f'<div class="bar"><span class="lbl">{en if lang=="en" else bn}</span>'
                f'<span class="track"><span class="fill" style="width:{v/maxv*100:.1f}%"></span></span>'
                f'<span class="val">{fmt(v)}</span></div>')
    return out + "</div>"

def table(cols, rows, cap):
    head = "".join(f'<th scope="col">{c}</th>' for c in cols)
    body = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f'<td data-label="{cols[i+1]}">{cite(x)}</td>' for i, x in enumerate(r[1:])) + "</tr>" for r in rows)
    return f'<div class="tablewrap stack"><table class="cmp"><caption>{cap}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

def content(lang):
    E = lang == "en"; ck = CHECKED[lang]
    lakh = (lambda v: f"{v:.2f} lakh") if E else (lambda v: f"{v:.2f} লাখ")
    num = lambda v: f"{v:,}"
    title = "Students abroad: the numbers" if E else "বিদেশে ছাত্রছাত্রী: সংখ্যার হিসেব"
    desc = ("How many Indian and Bangladeshi students study abroad, in which countries and in which subjects — official figures with sources."
            if E else "কতজন ভারতীয় আর বাংলাদেশি ছাত্রছাত্রী বিদেশে পড়ে, কোন দেশে, কোন বিষয়ে — সূত্র-সহ সরকারি হিসেব।")
    if E:
        h = f"""<p>How many students from India and Bangladesh study abroad, where they go, and what they study. Countries count students in different ways — visas issued, students enrolled, or people who say “study” at the airport — so numbers from different sources are not directly comparable.</p>
<h2 id="india">India</h2>
<p><b>About 18.82 lakh</b> Indian students were studying abroad in 2025, in 153 countries. The five largest destinations: [mea]</p>
{bars(IN_DEST, lang, lakh, 4.27)}
{table(["Country", "Latest figure", "What it counts"], [
 ["USA", "<b>3,63,019</b> in 2024/25, up 10%; India is the largest source country [od_in] [od_pr]", "Students enrolled plus 1,43,740 graduates on OPT work permits. New international enrolments fell 17% in autumn 2025 [od_pr]."],
 ["UK", "<b>82,523</b> study visas in the year to June 2026 — 23% of all, down 16% [ho]", "Visas granted to main applicants. Indians also received 64,495 Graduate-visa extensions [ho]."],
 ["Germany", "<b>69,816</b> in winter semester 2025/26, a record, up 17.5% [pie]", "Students enrolled at universities; India is Germany's largest group of foreign students."],
], "Indian students in three BiswaPath countries")}
<h2 id="other">Other destinations, and why some are small</h2>
<p>Indian students by country on 1 January 2025, from the Ministry of External Affairs [mea_annex]:</p>
{table(["Country", "Indian students", "Why students go — or don't"], [
 ["Canada", "4,27,085", "Largest destination, but new arrivals fell about 41% in 2024 as Canada capped study permits and relations with India worsened [bt]."],
 ["UAE", "2,53,832", "Close to home, with branch campuses of UK, Australian and Indian universities. This figure is far above the roughly 18,000 Indians among Dubai's 42,026 university students in 2024–25, so it probably also counts many students from Indian families already living in the UAE [khda]."],
 ["Australia", "1,96,108", "Post-study work rights and English-taught courses; the visa fee is now AUD 2,500 (from 1 July 2026) and you must show AUD 29,710 a year for living costs [au]."],
 ["Singapore", "33,250", "Two of Asia's best universities (NUS 10th and NTU 12th in QS 2027) but few places and high fees [qs27]. A Tuition Grant lowers fees but requires three years' work in Singapore after graduating [sg]."],
 ["Russia", "27,222", "Mostly medicine (MBBS) at lower cost than private medical colleges in India; new arrivals rose from 25,503 in 2023 to 31,444 in 2024 [bt]."],
 ["Kyrgyzstan / Georgia", "16,550 / 16,020", "Also mainly medicine."],
 ["China", "5,339", "Once a major MBBS destination; over 23,000 Indians were enrolled in 2022, mostly medics, but Covid visa bans left many stuck at home. India's embassy warned that clinical training is in Chinese and that only 16% of graduates from China's 45 approved medical schools passed India's licensing exam (2015–21) [cn]."],
 ["Japan", "3,441", "Excellent, low-fee universities (University of Tokyo 39th in QS 2027), but few English-taught degrees — language is the main barrier [jp] [qs27]."],
], "Indian students in other countries, 1 January 2025")}
<p>For medicine abroad, check the National Medical Commission's rules before you choose: they decide whether a foreign MBBS lets you practise in India.</p>
<h2 id="bangladesh">Bangladesh</h2>
<p>At least <b>49,151</b> Bangladeshi students were abroad in 2022 (UNESCO), three times the 2008 figure; OECD data gives about <b>52,800</b> [unesco] [icef]. The three largest destinations in 2022: [unesco]</p>
{bars(BD_DEST, lang, num, 11157)}
{table(["Country", "Latest figure", "Note"], [
 ["USA", "<b>20,156</b> in 2024/25, up 18%; 9th largest source country [od_bd]", "Two-thirds (13,016) are postgraduates."],
 ["UK", "No published total", "In the year to September 2025, 22% of Bangladeshi student-visa applications were refused, and several UK universities paused or limited recruitment from Bangladesh, including Coventry, Sunderland, London Met and Hertfordshire [tbs]."],
], "Bangladeshi students: the US and the UK")}
<h2 id="subjects">Which subjects?</h2>
<ul>
<li><b>Germany</b> (Indian students): engineering 60%, social sciences, economics and management 21%, maths and natural sciences 18% [daad].</li>
<li><b>USA:</b> 57% of all international students study STEM subjects [od_pr]. The last published split for Indian students (2018/19) showed nearly 70% in maths, computer science or engineering [od_1819].</li>
<li><b>UK</b> (2023/24): nearly one in four Indian students chose computing and IT or health and medicine; 12% of Bangladeshi students chose computing and IT, up from 9% in 2019/20. Business and management is still the largest subject overall [the].</li>
</ul>
<h2 id="gaps">What nobody counts</h2>
<p><b>Bengali students.</b> India's government reports only national totals — a reply to Parliament asked for state-wise figures and gave none [ls] — and no country records students by mother tongue. Bangladesh's figures are, in practice, almost all Bengali students; for West Bengal there is no published number.</p>
<p><b>Subject by university.</b> No official source shows which universities, say, Indian chemistry students choose compared with economics students. For that, use subject rankings and the course pages in our <a href="/universities/">University finder</a>.</p>
<div class="invite"><p><b>Help us count.</b> If you are a Bengali student abroad, tell us your subject and university (and, if you like, your home district) through the <a href="/contribute/">Contribute</a> page. With enough answers, BiswaPath will publish the first map of where Bengali students study, by subject — counts only, never names.</p></div>"""
    else:
        h = f"""<p>ভারত আর বাংলাদেশ থেকে কতজন বিদেশে পড়তে যায়, কোথায় যায়, কী পড়ে। বিভিন্ন দেশ আলাদা ভাবে গোনে — দেওয়া ভিসা, ভর্তি হওয়া ছাত্র, বা বিমানবন্দরে যারা “পড়াশোনা” বলে — তাই আলাদা সূত্রের সংখ্যা সরাসরি তুলনা করা যায় না।</p>
<h2 id="india">ভারত</h2>
<p>২০২৫-এ <b>প্রায় ১৮.৮২ লাখ</b> ভারতীয় ছাত্রছাত্রী ১৫৩টি দেশে পড়ছিল। সবচেয়ে বড় পাঁচটা গন্তব্য: [mea]</p>
{bars(IN_DEST, lang, lakh, 4.27)}
{table(["দেশ", "সর্বশেষ সংখ্যা", "কী গোনা হয়েছে"], [
 ["USA", "২০২৪/২৫-এ <b>3,63,019</b>, ১০% বেশি; সবচেয়ে বড় উৎস ভারত [od_in] [od_pr]", "ভর্তি হওয়া ছাত্র, সঙ্গে OPT ওয়ার্ক পারমিটে থাকা 1,43,740 জন গ্র্যাজুয়েট। ২০২৫-এর শরতে নতুন বিদেশি ভর্তি ১৭% কমেছে [od_pr]।"],
 ["UK", "জুন ২০২৬ পর্যন্ত এক বছরে <b>82,523</b>টি স্টাডি ভিসা — মোটের ২৩%, ১৬% কম [ho]", "মূল আবেদনকারীদের দেওয়া ভিসা। ভারতীয়রা 64,495টি Graduate-ভিসা এক্সটেনশনও পেয়েছেন [ho]।"],
 ["জার্মানি", "শীতকালীন সেমেস্টার ২০২৫/২৬-এ রেকর্ড <b>69,816</b>, ১৭.৫% বেশি [pie]", "বিশ্ববিদ্যালয়ে ভর্তি ছাত্র; জার্মানিতে বিদেশি ছাত্রদের মধ্যে ভারতীয়রাই সবচেয়ে বেশি।"],
], "BiswaPath-এর তিনটে দেশে ভারতীয় ছাত্রছাত্রী")}
<h2 id="other">অন্য দেশ, আর কেন কয়েকটায় কম যায়</h2>
<p>১ জানুয়ারি ২০২৫-এ দেশভিত্তিক ভারতীয় ছাত্রছাত্রী, বিদেশ মন্ত্রকের হিসেবে [mea_annex]:</p>
{table(["দেশ", "ভারতীয় ছাত্রছাত্রী", "কেন যায় — বা যায় না"], [
 ["কানাডা", "4,27,085", "সবচেয়ে বড় গন্তব্য, কিন্তু ২০২৪-এ নতুন যাওয়া প্রায় ৪১% কমেছে — কানাডা স্টাডি পারমিটে সীমা টেনেছে আর ভারতের সঙ্গে সম্পর্ক খারাপ হয়েছে [bt]।"],
 ["UAE", "2,53,832", "কাছে, আর UK, অস্ট্রেলিয়া ও ভারতের বিশ্ববিদ্যালয়ের শাখা ক্যাম্পাস আছে। ২০২৪–২৫-এ দুবাইয়ের 42,026 জন বিশ্ববিদ্যালয়-ছাত্রের মধ্যে ভারতীয় প্রায় ১৮,০০০; তাই এই সংখ্যায় সম্ভবত UAE-তে আগে থেকেই থাকা ভারতীয় পরিবারের অনেক ছাত্রছাত্রীও ধরা আছে [khda]।"],
 ["অস্ট্রেলিয়া", "1,96,108", "পাসের পর কাজের সুযোগ আর ইংরেজিতে কোর্স; ভিসা ফি এখন AUD 2,500 (১ জুলাই ২০২৬ থেকে), আর থাকার খরচ বাবদ বছরে AUD 29,710 দেখাতে হয় [au]।"],
 ["সিঙ্গাপুর", "33,250", "এশিয়ার সেরা দুটো বিশ্ববিদ্যালয় (QS 2027-এ NUS ১০, NTU ১২), কিন্তু আসন কম আর ফি বেশি [qs27]। Tuition Grant নিলে ফি কমে, তবে পাসের পর সিঙ্গাপুরে তিন বছর কাজ করতে হয় [sg]।"],
 ["রাশিয়া", "27,222", "বেশিরভাগ মেডিসিন (MBBS), ভারতের বেসরকারি মেডিক্যাল কলেজের চেয়ে কম খরচে; নতুন যাওয়া ২০২৩-এ 25,503 থেকে ২০২৪-এ 31,444 [bt]।"],
 ["কিরগিজস্তান / জর্জিয়া", "16,550 / 16,020", "এখানেও মূলত মেডিসিন।"],
 ["চীন", "5,339", "একসময় MBBS-এর বড় গন্তব্য ছিল; ২০২২-এ ২৩,০০০-এর বেশি ভারতীয় ভর্তি ছিল, বেশিরভাগ ডাক্তারি, কিন্তু কোভিডের ভিসা নিষেধাজ্ঞায় অনেকে দেশে আটকে ছিল। ভারতীয় দূতাবাস সতর্ক করেছে যে ক্লিনিক্যাল পড়াশোনা চীনা ভাষায়, আর চীনের ৪৫টি অনুমোদিত মেডিক্যাল স্কুলের মাত্র ১৬% গ্র্যাজুয়েট ভারতের লাইসেন্স পরীক্ষায় পাস করেছেন (২০১৫–২১) [cn]।"],
 ["জাপান", "3,441", "দারুণ, কম ফি-র বিশ্ববিদ্যালয় (QS 2027-এ University of Tokyo ৩৯), কিন্তু ইংরেজিতে ডিগ্রি কম — মূল বাধা ভাষা [jp] [qs27]।"],
], "অন্য দেশে ভারতীয় ছাত্রছাত্রী, ১ জানুয়ারি ২০২৫")}
<p>বিদেশে মেডিসিন পড়ার আগে National Medical Commission-এর নিয়ম দেখে নিন: বিদেশের MBBS দিয়ে ভারতে প্র্যাকটিস করা যাবে কি না, তা তারাই ঠিক করে।</p>
<h2 id="bangladesh">বাংলাদেশ</h2>
<p>২০২২-এ অন্তত <b>49,151</b> জন বাংলাদেশি ছাত্রছাত্রী বিদেশে ছিল (UNESCO), ২০০৮-এর তিন গুণ; OECD-র হিসেবে প্রায় <b>52,800</b> [unesco] [icef]। ২০২২-এর সবচেয়ে বড় তিনটে গন্তব্য: [unesco]</p>
{bars(BD_DEST, lang, num, 11157)}
{table(["দেশ", "সর্বশেষ সংখ্যা", "মন্তব্য"], [
 ["USA", "২০২৪/২৫-এ <b>20,156</b>, ১৮% বেশি; উৎস দেশ হিসেবে ৯ নম্বরে [od_bd]", "দুই-তৃতীয়াংশ (13,016) স্নাতকোত্তর।"],
 ["UK", "মোট সংখ্যা প্রকাশিত হয়নি", "সেপ্টেম্বর ২০২৫ পর্যন্ত এক বছরে বাংলাদেশি স্টুডেন্ট-ভিসা আবেদনের ২২% বাতিল হয়েছে, আর Coventry, Sunderland, London Met, Hertfordshire-সহ কয়েকটা UK বিশ্ববিদ্যালয় বাংলাদেশ থেকে ভর্তি বন্ধ বা সীমিত করেছে [tbs]।"],
], "বাংলাদেশি ছাত্রছাত্রী: USA আর UK")}
<h2 id="subjects">কোন বিষয়?</h2>
<ul>
<li><b>জার্মানি</b> (ভারতীয় ছাত্র): ইঞ্জিনিয়ারিং ৬০%, সমাজবিজ্ঞান, অর্থনীতি ও ম্যানেজমেন্ট ২১%, অঙ্ক ও প্রাকৃতিক বিজ্ঞান ১৮% [daad]।</li>
<li><b>USA:</b> সব বিদেশি ছাত্রের ৫৭% STEM পড়ে [od_pr]। ভারতীয়দের শেষ প্রকাশিত হিসেব (২০১৮/১৯): প্রায় ৭০% অঙ্ক, কম্পিউটার সায়েন্স বা ইঞ্জিনিয়ারিং [od_1819]।</li>
<li><b>UK</b> (২০২৩/২৪): প্রায় প্রতি চারজন ভারতীয় ছাত্রের একজন কম্পিউটিং ও IT বা স্বাস্থ্য ও মেডিসিন বেছেছেন; বাংলাদেশি ছাত্রদের ১২% কম্পিউটিং ও IT, ২০১৯/২০-তে যা ছিল ৯%। সব মিলিয়ে বিজনেস ও ম্যানেজমেন্টই এখনও সবচেয়ে বড় বিষয় [the]।</li>
</ul>
<h2 id="gaps">যা কেউ গোনে না</h2>
<p><b>বাঙালি ছাত্রছাত্রী।</b> ভারত সরকার শুধু সারা দেশের মোট সংখ্যা দেয় — সংসদে রাজ্যভিত্তিক হিসেব চাওয়া হলেও দেওয়া হয়নি [ls] — আর কোনো দেশ মাতৃভাষা ধরে ছাত্র গোনে না। বাংলাদেশের সংখ্যা কার্যত প্রায় সবই বাঙালি ছাত্রছাত্রী; পশ্চিমবঙ্গের কোনো প্রকাশিত সংখ্যা নেই।</p>
<p><b>বিষয় অনুযায়ী বিশ্ববিদ্যালয়।</b> ভারতীয় কেমিস্ট্রির ছাত্ররা কোন বিশ্ববিদ্যালয় বেছে নেয় আর অর্থনীতির ছাত্ররা কোনটা — এমন কোনো সরকারি হিসেব নেই। তার জন্য বিষয়ভিত্তিক র‍্যাংকিং আর আমাদের <a href="/bn/universities/">বিশ্ববিদ্যালয় খোঁজার পাতার</a> কোর্স পেজ দেখুন।</p>
<div class="invite"><p><b>গুনতে সাহায্য করুন।</b> আপনি যদি বিদেশে পড়া বাঙালি ছাত্র বা ছাত্রী হন, <a href="/bn/contribute/">যুক্ত হোন</a> পাতা দিয়ে আপনার বিষয় আর বিশ্ববিদ্যালয় (চাইলে নিজের জেলাও) জানান। যথেষ্ট উত্তর পেলে BiswaPath প্রকাশ করবে বাঙালি ছাত্রছাত্রীরা কোথায়, কোন বিষয়ে পড়ে তার প্রথম মানচিত্র — শুধু সংখ্যা, কারও নাম নয়।</p></div>"""
    src = "".join(f'<li id="src-{k}"><a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a></li>' for k in ORDER)
    h = cite(h) + (f'<h2>{"Sources" if E else "সূত্র"}</h2><ol class="srcs">{src}</ol>'
                   f'<p class="updated">{"Last checked" if E else "শেষ যাচাই"}: {ck}</p>')
    return title, desc, h
