# "Students abroad: the numbers" (imported by build.py). Revised 19 Oct 2026 after a source-by-source check.
# Rule: every figure carries its measure type, reference period and a direct source link.
import re

CHECKED = {"en": "19 October 2026", "bn": "১৯ অক্টোবর ২০২৬"}

# key: (title, url, kind) — kind: "primary" = the body that produced the figure; "secondary" = report of it
SRC = {
 "mea": ("Ministry of External Affairs (India): Data on Indian students abroad, as on 1 January 2025 (Annexure I)", "https://www.mea.gov.in/Images/CPV/557-en-01-04-12-2025.pdf", "primary"),
 "od_in": ("IIE Open Doors 2025: India fact sheet (academic year 2024/25)", "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_India_Fact-Sheet-2025.pdf", "primary"),
 "od_bd": ("IIE Open Doors 2025: Bangladesh fact sheet (academic year 2024/25)", "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_Bangladesh_Fact-Sheet-2025.pdf", "primary"),
 "od_pr": ("IIE Open Doors 2025 press release (November 2025)", "https://opendoorsdata.org/wp-content/uploads/2025/11/OD25_Open-Doors-2025-Press-Release.pdf", "primary"),
 "od_1819": ("Open Doors 2018/19 data on Indian students by field, as charted by Datawrapper", "https://datawrapper.dwcdn.net/MlZW9/1", "secondary"),
 "sevis": ("US ICE: 2024 SEVIS by the Numbers (calendar year 2024)", "https://www.ice.gov/doclib/sevis/btn/25_0605_2024-sevis-btn.pdf", "primary"),
 "ho": ("UK Home Office: Why do people come to the UK? Study (year ending June 2026)", "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/why-do-people-come-to-the-uk-study", "primary"),
 "hesa": ("HESA: Higher Education Student Statistics, UK 2024/25 — where students come from (27 January 2026)", "https://www.hesa.ac.uk/news/27-01-2026/sb273-higher-education-student-statistics/location", "primary"),
 "hesa_wiki": ("Wikipedia: International students in the United Kingdom (cites HESA 'Where do HE students come from?')", "https://en.wikipedia.org/wiki/International_students_in_the_United_Kingdom", "secondary"),
 "wiwe": ("DAAD/DZHW: Wissenschaft weltoffen 2026 press release (14 October 2026), as published by bildungsklick", "https://bildungsklick.de/hochschule-und-forschung/detail/deutschland-weltweit-standort-studium-promotion", "primary"),
 "daad_in": ("DAAD India: Indian students in Germany at an all-time high (22 September 2025)", "https://www.daad.in/en/2025/09/22/indian-students-in-germany-at-an-all-time-high/", "primary"),
 "destatis": ("Destatis via DZHW data portal, Table 2.5.33: foreign students by citizenship, winter semesters to 2023/24", "https://ice.dzhw.eu/portal/de/Tabelle-2.5.33.pdf", "primary"),
 "bs": ("Business Standard: 69,816 Indian students in Germany, attributed to DAAD (13 August 2026)", "https://www.business-standard.com/amp/immigration/nearly-70-000-indians-now-studying-in-germany-numbers-jump-17-5-in-a-year-126081301682_1.html", "secondary"),
 "vde": ("VDE: role of international students in electrical engineering (2026), citing CHE/HSI-Monitor on Destatis data", "https://www.vde.com/resource/blob/2490198/c014b82d79ca673b951816c18b12f7ec/teil-3-rolle-internationaler-studierender-data.pdf", "secondary"),
 "the": ("Times Higher Education (31 July 2025): ApplyBoard analysis of UK enrolment data, 2023/24", "https://www.timeshighereducation.com/node/738245", "secondary"),
 "unesco": ("The Daily Star (August 2023): UNESCO data on Bangladeshi students abroad, 2022", "https://www.thedailystar.net/news/bangladesh/news/number-students-going-abroad-triples-15-years-despite-university-boom-3397431", "secondary"),
 "icef": ("ICEF Monitor (November 2025): OECD data on Bangladeshi students abroad, 2022", "https://monitor.icef.com/2025/11/the-economic-indicators-driving-outbound-student-mobility-from-bangladesh-indonesia-nepal-and-vietnam/", "secondary"),
 "tbs": ("TBS News (4 December 2025): UK visa refusals and recruitment pauses for Bangladesh", "https://www.tbsnews.net/explainer/why-are-uk-universities-restricting-recruitment-bangladeshi-pakistani-students-1302001", "secondary"),
 "khda": ("Gulf News: Dubai's international students in 2024/25 (KHDA figures)", "https://gulfnews.com/uae/indian-students-top-dubais-global-intake-at-43-pakistanis-at-6-1.500190286", "secondary"),
 "bt": ("Business Today (26 July 2025): MEA data on new departures, 2023 vs 2024", "https://www.businesstoday.in/amp/nri/study/story/india-sees-sharp-fall-in-students-heading-to-us-uk-canada-russia-and-bangladesh-gain-486434-2025-07-26", "secondary"),
 "cn": ("The Tribune (10 September 2022): Indian embassy advisory on studying medicine in China", "https://www.tribuneindia.com/news/nation/india-issues-advisory-outlining-risks-for-students-planning-to-study-medicine-in-china-430391/amp", "secondary"),
 "ls": ("Lok Sabha Starred Question 84 (29 July 2024): national totals only, no state-wise data", "https://sabrangindia.in/wp-content/uploads/2024/08/loksabhaquestions_Students-Migration.pdf", "secondary"),
 "qs_subj": ("QS World University Rankings by Subject 2026 (official tables)", "https://www.topuniversities.com/subject-rankings/2026", "primary"),
 "xx": ("XuanXiao: QS 2026 subject positions by country (used to read the QS tables; check against QS)", "https://xuanxiao.org/en/subjects/engineering", "secondary"),
 "saar": ("Example of a university publishing its own nationality data: Saarland University, winter 2025/26", "https://www.uni-saarland.de/fileadmin/upload/universitaet/statistik/2025-ws/herkunft.pdf", "primary"),
}
ORDER = list(SRC)

def cite(text):
    return re.sub(r"\[(\w+)\]", lambda m: f'<sup><a href="#src-{m.group(1)}">[{ORDER.index(m.group(1)) + 1}]</a></sup>' if m.group(1) in SRC else m.group(0), text)

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

def lakh(v, lang): return f"{v/1e5:.2f} {'lakh' if lang=='en' else 'লাখ'}"

# Indian students at universities/tertiary institutions, MEA, 1 Jan 2025
MEA_TERTIARY = [("Canada", "কানাডা", 427085), ("USA", "USA", 255247), ("UK", "UK", 173190), ("Australia", "অস্ট্রেলিয়া", 138579), ("Germany*", "জার্মানি*", 49483), ("Russia", "রাশিয়া", 27000)]

# Subject categories. verified text = published figures about Indian students; QS lists = illustrative subject strength (QS 2026), NOT enrolment.
SUBJECTS = [
 ("engineering", "Engineering", "ইঞ্জিনিয়ারিং",
  {"en": "Germany: 60% of Indian students in “Engineering incl. biology-related fields” (DAAD India, 2025) [daad_in]. Engineering and computer science together: about 26,000 Indian students in Germany in 2024 (CHE/HSI-Monitor on Destatis data, reported by VDE) [vde].",
   "bn": "জার্মানি: ভারতীয় ছাত্রদের ৬০% “Engineering incl. biology-related fields”-এ (DAAD India, ২০২৫) [daad_in]। ইঞ্জিনিয়ারিং আর কম্পিউটার সায়েন্স মিলিয়ে ২০২৪-এ জার্মানিতে প্রায় ২৬,০০০ ভারতীয় ছাত্র (Destatis-এর তথ্যে CHE/HSI-Monitor, VDE-র রিপোর্টে) [vde]।"},
  "QS Engineering &amp; Technology 2026", [("Oxford", 4), ("Cambridge", 5), ("Imperial", 7)], [("TUM", 16), ("KIT", "=42"), ("TU Berlin", "=42")], [("MIT", 1), ("Stanford", 2), ("UC Berkeley", 6)]),
 ("cs", "Computer science", "কম্পিউটার সায়েন্স",
  {"en": "UK 2023/24: computing and IT plus health and medicine together drew nearly one in four Indian students (ApplyBoard analysis of UK data) [the]. USA: no current Indian split; in 2018/19 nearly 70% studied maths, computer science or engineering [od_1819].",
   "bn": "UK ২০২৩/২৪: কম্পিউটিং ও IT আর স্বাস্থ্য ও মেডিসিন মিলিয়ে প্রায় প্রতি চারজন ভারতীয় ছাত্রের একজন (UK-র তথ্যে ApplyBoard-এর বিশ্লেষণ) [the]। USA: এখনকার ভারতীয় হিসেব নেই; ২০১৮/১৯-এ প্রায় ৭০% অঙ্ক, কম্পিউটার সায়েন্স বা ইঞ্জিনিয়ারিং পড়ত [od_1819]।"},
  "QS Computer Science &amp; Information Systems 2026", [("Oxford", "=4"), ("Cambridge", 8), ("Imperial", 12)], [("TUM", 26), ("TU Berlin", "=76"), ("LMU Munich", "=91")], [("MIT", 1), ("Stanford", 2), ("Carnegie Mellon", 3)]),
 ("business", "Business and management", "বিজনেস ও ম্যানেজমেন্ট",
  {"en": "Germany: 21% in “Social Sciences/Economics/Management” combined (DAAD India, 2025) [daad_in]. No published Indian-only figure for the UK or USA.",
   "bn": "জার্মানি: “Social Sciences/Economics/Management” মিলিয়ে ২১% (DAAD India, ২০২৫) [daad_in]। UK বা USA-র জন্য শুধু ভারতীয়দের প্রকাশিত হিসেব নেই।"},
  "QS Business &amp; Management Studies 2026", [("Oxford", 5), ("Cambridge", 6), ("London Business School", 9)], [("TUM", "=91")], [("Harvard", 1), ("Stanford", 2), ("MIT", 3)]),
 ("chemistry", "Chemistry", "কেমিস্ট্রি",
  {"en": "No published Indian-only figure. Germany's “Mathematics/Natural Sciences” group (18%) includes chemistry [daad_in].",
   "bn": "শুধু ভারতীয়দের প্রকাশিত হিসেব নেই। জার্মানির “Mathematics/Natural Sciences” গ্রুপে (১৮%) কেমিস্ট্রি ধরা আছে [daad_in]।"},
  "QS Chemistry 2026", [("Cambridge", "=2"), ("Oxford", 5), ("Imperial", 10)], [("TUM", "=25"), ("KIT", "=50"), ("LMU Munich", "=55")], [("MIT", 1), ("Harvard", "=2"), ("Stanford", 4)]),
 ("physics", "Physics", "ফিজিক্স",
  {"en": "No published Indian-only figure. Included in Germany's “Mathematics/Natural Sciences” group [daad_in].",
   "bn": "শুধু ভারতীয়দের প্রকাশিত হিসেব নেই। জার্মানির “Mathematics/Natural Sciences” গ্রুপে ধরা [daad_in]।"},
  "QS Physics &amp; Astronomy 2026", [("Oxford", 3), ("Cambridge", 5), ("Imperial", 12)], [("TUM", 27), ("LMU Munich", "=39"), ("Heidelberg", "=43")], [("MIT", 1), ("Harvard", 2), ("Stanford", 4)]),
 ("biology", "Biology and life sciences", "বায়োলজি ও লাইফ সায়েন্স",
  {"en": "No clean figure: DAAD India counts “biology-related fields” inside engineering, which may explain why its shares add up to 105% [daad_in].",
   "bn": "পরিষ্কার হিসেব নেই: DAAD India “biology-related fields” ইঞ্জিনিয়ারিং-এর মধ্যে গোনে, তাই হয়তো তাদের ভাগ যোগ করলে ১০৫% হয় [daad_in]।"},
  "QS Biological Sciences 2026", [("Oxford", 3), ("Cambridge", 5), ("Imperial", "=7")], [("Heidelberg", 28), ("LMU Munich", "=29")], [("Harvard", 1), ("MIT", 2), ("Stanford", 4)]),
 ("medicine", "Medicine", "মেডিসিন",
  {"en": "No subject-level count: MEA does not record subjects. Russia, Kyrgyzstan and Georgia, reported as mainly medical destinations, together host about 59,500 Indian university students [mea] [bt]. A foreign MBBS must meet National Medical Commission rules to practise in India.",
   "bn": "বিষয়ভিত্তিক গণনা নেই: MEA বিষয় লেখে না। রাশিয়া, কিরগিজস্তান আর জর্জিয়া — যেগুলো মূলত মেডিসিনের গন্তব্য বলে রিপোর্টে বলা হয় — মিলিয়ে প্রায় ৫৯,৫০০ ভারতীয় বিশ্ববিদ্যালয়-ছাত্র [mea] [bt]। বিদেশের MBBS দিয়ে ভারতে প্র্যাকটিস করতে National Medical Commission-এর নিয়ম মানতে হয়।"},
  "QS Medicine 2026", [("Oxford", 2), ("Cambridge", 5), ("UCL", 6)], [("Heidelberg", 34)], [("Harvard", 1), ("Stanford", 3), ("Johns Hopkins", 4)]),
 ("maths", "Mathematics and statistics", "অঙ্ক ও পরিসংখ্যান",
  {"en": "Germany: part of the 18% “Mathematics/Natural Sciences” group [daad_in]. USA 2018/19: counted together with computer science and engineering [od_1819].",
   "bn": "জার্মানি: ১৮% “Mathematics/Natural Sciences” গ্রুপের অংশ [daad_in]। USA ২০১৮/১৯: কম্পিউটার সায়েন্স আর ইঞ্জিনিয়ারিং-এর সঙ্গে একসঙ্গে গোনা [od_1819]।"},
  "QS Mathematics 2026", [("Oxford", 2), ("Cambridge", 3), ("Imperial", "=8")], [("Bonn", 39), ("TUM", 50), ("TU Berlin", 53)], [("MIT", 1), ("Harvard", 4), ("Princeton", 5)]),
 ("economics", "Economics", "অর্থনীতি",
  {"en": "Germany: inside the 21% “Social Sciences/Economics/Management” group [daad_in]. No separate Indian figure for the UK or USA.",
   "bn": "জার্মানি: ২১% “Social Sciences/Economics/Management” গ্রুপের মধ্যে [daad_in]। UK বা USA-র আলাদা ভারতীয় হিসেব নেই।"},
  "QS Economics &amp; Econometrics 2026", [("LSE", 6), ("Oxford", 8), ("Cambridge", 10)], [("LMU Munich", 47), ("Bonn", 50), ("Mannheim", "=56")], [("Harvard", 1), ("MIT", 2), ("Stanford", 3)]),
 ("humanities", "Humanities", "হিউম্যানিটিজ",
  {"en": "Germany: part of the 6% “Other (Sports/Arts/German Studies, etc.)” [daad_in]. No Indian-only figure elsewhere.",
   "bn": "জার্মানি: ৬% “Other (Sports/Arts/German Studies, etc.)”-এর অংশ [daad_in]। অন্য কোথাও শুধু ভারতীয়দের হিসেব নেই।"},
  "QS Arts &amp; Humanities 2026", [("Oxford", 1), ("Cambridge", 3), ("UCL", 8)], [("Humboldt Berlin", "=24"), ("FU Berlin", 30), ("LMU Munich", "=35")], [("Harvard", 2), ("Stanford", 4), ("Yale", 5)]),
 ("social", "Social sciences", "সমাজবিজ্ঞান",
  {"en": "Germany: inside the 21% “Social Sciences/Economics/Management” group [daad_in].",
   "bn": "জার্মানি: ২১% “Social Sciences/Economics/Management” গ্রুপের মধ্যে [daad_in]।"},
  "QS Social Sciences &amp; Management 2026 (broad area)", [("Oxford", 2), ("Cambridge", 4), ("LSE", 5)], [], [("Harvard", 1), ("Stanford", 3)]),
]

def subject_table(lang):
    E = lang == "en"
    cols = (["Subject", "What is published about Indian students", "Illustrative only: highly ranked for the subject (QS 2026 rank)"] if E
            else ["বিষয়", "ভারতীয় ছাত্রদের নিয়ে যা প্রকাশিত", "শুধু উদাহরণ: বিষয়ে উঁচু র‍্যাংক (QS 2026)"])
    rows = []
    for sid, en, bn, ver, qsname, uk, de, us in SUBJECTS:
        def fmt(lst):
            return ", ".join(f"{n} ({r})" for n, r in lst) if lst else ("not in the visible top list" if E else "দৃশ্যমান তালিকায় নেই")
        ill = f'<span class="ucity">{qsname}</span><br><b>UK:</b> {fmt(uk)}<br><b>{"Germany" if E else "জার্মানি"}:</b> {fmt(de)}<br><b>USA:</b> {fmt(us)} [xx]'
        rows.append([f'<span id="subj-{sid}">{en if E else bn}</span>', ver[lang], ill])
    return table(cols, rows, "Where do Indian students study, by subject?" if E else "কোন বিষয়ে ভারতীয় ছাত্ররা কোথায় পড়ে?")

def content(lang):
    E = lang == "en"; ck = CHECKED[lang]
    L = lambda v: lakh(v, lang)
    title = "Students abroad: the numbers" if E else "বিদেশে ছাত্রছাত্রী: সংখ্যার হিসেব"
    desc = ("How many Indian and Bangladeshi students study abroad, where and in which subjects — each figure with its measure, year and original source."
            if E else "কতজন ভারতীয় আর বাংলাদেশি ছাত্রছাত্রী বিদেশে পড়ে, কোথায়, কোন বিষয়ে — প্রতিটা সংখ্যা তার মাপ, বছর আর মূল সূত্র-সহ।")
    if E:
        h = f"""<p>How many students from India and Bangladesh study abroad, where, and in which subjects. Every figure below names what it measures, the period it covers and its original source.</p>
<div class="invite"><p><b>Four different measures — never add them together.</b><br>
<b>Enrolments</b>: students registered at a university at a point in time (HESA, Destatis, Open Doors).<br>
<b>OPT participants</b>: in the USA, graduates on Optional Practical Training work permits. Open Doors counts them in its totals although they are no longer attending classes.<br>
<b>Visa grants</b>: visas issued in a year (UK Home Office). Not the number of students in the country.<br>
<b>Government estimates</b>: India's Ministry of External Affairs (MEA) compiles counts from its missions, including school pupils.</p></div>

<h2 id="india">India: how many, and where</h2>
<p>MEA, as on 1 January 2025: <b>18,82,318</b> Indian students abroad in 153 countries. This total includes <b>6,28,305 school pupils</b>; the figure for <b>universities and other tertiary institutions is 12,54,013 (12.54 lakh)</b>. The MEA table gives no notes on how missions collected the numbers [mea].</p>
<p>Indian students at universities, by country (MEA, 1 January 2025) [mea]:</p>
{bars(MEA_TERTIARY, lang, L, 427085)}
<p class="updated">* MEA's Germany figure (49,483) equals Germany's official count for winter semester 2023/24 [destatis], so it is about a year older than the date of the table.</p>

<h2 id="usa">USA</h2>
{table(["Measure", "Figure", "Period", "Source"], [
 ["Open Doors total (enrolled + OPT)", "<b>3,63,019</b> Indian students; India is the largest source country", "2024/25", "IIE Open Doors [od_in] [od_pr]"],
 ["of which enrolled", "<b>2,19,279</b>: 1,77,892 graduate, 40,135 undergraduate, 1,252 non-degree", "2024/25", "[od_in]"],
 ["of which OPT participants", "<b>1,43,740</b> graduates on work permits, not attending classes", "2024/25", "[od_in]"],
 ["SEVIS active records", "<b>4,22,335</b> F-1/M-1 records with Indian citizenship. Counts records, not people; one student can have more than one", "Calendar year 2024", "US ICE [sevis]"],
 ["New international enrolment, all countries", "Down 17% in autumn 2025 (Fall Snapshot of 825+ institutions)", "Autumn 2025", "[od_pr]"],
], "Indian students in the USA — three different measures")}

<h2 id="uk">UK</h2>
{table(["Measure", "Figure", "Period", "Source"], [
 ["Study visas granted to Indian main applicants", "<b>82,523</b> — 23% of all 3,65,868; down 16%", "Year ending June 2026", "Home Office [ho]"],
 ["Graduate-visa extensions granted to Indians", "<b>64,495</b>", "Year ending June 2026", "Home Office [ho]"],
 ["Enrolments of students from India", "<b>1,46,480</b> (21.4% of international students) — <i>not yet checked at source</i>: HESA's site could not be opened by our checker; figure as cited from HESA by Wikipedia", "2024/25", "HESA [hesa]; cited in [hesa_wiki]"],
], "Indian students in the UK — visas and enrolments")}

<h2 id="germany">Germany</h2>
{table(["Measure", "Figure", "Period", "Source"], [
 ["International students from India", "<b>About 69,000</b>; India is the largest country of origin", "Winter semester 2025/26", "DAAD/DZHW, Wissenschaft weltoffen 2026 [wiwe]"],
 ["Exact figure reported in the media", "69,816 (+17.5%), attributed to DAAD — <i>not found in a DAAD publication</i>", "Winter semester 2025/26", "[bs]"],
 ["Indian students (Bachelor's, Master's, PhD)", "<b>59,419</b> (semester not stated by DAAD India; published September 2025)", "2025 report", "DAAD India [daad_in]"],
 ["Foreign students with Indian citizenship (official)", "<b>49,483</b>", "Winter semester 2023/24", "Destatis [destatis]"],
], "Indian students in Germany — official and DAAD figures")}

<h2 id="other">Other destinations, and why some are small</h2>
<p>MEA, as on 1 January 2025. Universities and schools are counted separately [mea]:</p>
{table(["Country", "University/tertiary", "School", "Why students go — or don't"], [
 ["Australia", "1,38,579", "57,529", "English-taught degrees and post-study work rights."],
 ["Russia", "27,000", "222", "Mostly medicine (MBBS). New departures rose from 25,503 in 2023 to 31,444 in 2024 [bt]."],
 ["Kyrgyzstan / Georgia", "16,500 / 16,000", "50 / 20", "Mainly medicine."],
 ["Ireland", "10,000", "10,000", "English-taught, EU member."],
 ["UAE", "6,507", "2,47,325", "Mostly children of Indian families living there. Dubai's universities had 42,026 international students in 2024/25, 43% from India [khda]."],
 ["China", "5,330", "9", "Once a major MBBS destination; Covid visa bans stranded thousands, clinical training is in Chinese, and only 16% of graduates from China's 45 approved medical schools passed India's licensing exam in 2015–21 [cn]."],
 ["Singapore", "3,250", "30,000", "Few university places; NUS and NTU are highly selective."],
 ["Japan", "1,532", "1,909", "Few English-taught degrees; language is the main barrier."],
], "Indian students in other countries, 1 January 2025")}

<h2 id="bangladesh">Bangladesh</h2>
{table(["Measure", "Figure", "Period", "Source"], [
 ["Bangladeshi students in the USA (Open Doors total)", "<b>20,156</b>, 9th largest source country; enrolled 17,166 (13,016 graduate, 4,041 undergraduate, 109 non-degree) + 2,990 on OPT", "2024/25", "IIE Open Doors [od_bd]"],
 ["Bangladeshi students abroad, all countries", "At least <b>49,151</b> (UNESCO) — a historical estimate, not a current total; largest hosts UAE 11,157, USA 8,665, Malaysia 6,180", "2022", "UNESCO, as reported by The Daily Star [unesco]"],
 ["Same, OECD estimate", "About <b>52,800</b>", "2022", "OECD, as reported by ICEF Monitor [icef]"],
 ["UK student-visa refusal rate", "22% of Bangladeshi applications refused; several UK universities paused or limited recruitment", "Year to September 2025", "Reported by TBS News [tbs]"],
], "Bangladeshi students abroad")}

<h2 id="subjects">Where do Indian students study, by subject?</h2>
<p>Two different kinds of information sit side by side below, and they must not be confused:</p>
<ul>
<li><b>What is published about Indian students.</b> Only a few broad figures exist. DAAD India's German shares — engineering incl. biology-related fields 60%, social sciences/economics/management 21%, mathematics/natural sciences 18%, other 6% — add up to <b>105%</b>, so they cannot be read as separate slices of one whole until DAAD explains the overlap [daad_in].</li>
<li><b>Illustrative examples, not enrolment.</b> Universities that QS ranks highly for the subject in 2026 [qs_subj]. This says nothing about how many Indian students attend them. Rankings favour large research universities; many excellent, more affordable options rank lower.</li>
</ul>
{subject_table(lang)}
<p class="updated">We do not publish any “most popular universities for Indian students” list, because no source supports one yet.</p>

<h2 id="datasets">What data exists at university and subject level</h2>
<ul>
<li><b>UK (HESA):</b> publishes students by university and by country of permanent address, and separately by university and subject. It does not publish the three together, so a ranking such as “universities with the most Indian chemistry students” is not available in open data; it would need a custom HESA data request [hesa].</li>
<li><b>Germany (Destatis, DAAD/DZHW):</b> national counts of foreign students by citizenship [destatis] and international students by broad subject group [wiwe]. Some universities publish their own tables of students by nationality, e.g. Saarland University [saar], but there is no national university × subject × nationality table.</li>
<li><b>USA (Open Doors, SEVIS):</b> totals by country of origin and by academic level [od_in]; fields of study and leading institutions for all international students together, not by nationality [sevis]. Some universities publish their own international student reports.</li>
<li><b>Bengali students:</b> no country counts students by mother tongue, and India's government reports national totals only — a parliamentary question asking for state-wise figures received none [ls].</li>
</ul>
<div class="invite"><p><b>Help us count.</b> If you are a Bengali student abroad, tell us your subject and university (and, if you like, your home district) through the <a href="/contribute/">Contribute</a> page. With enough answers, BiswaPath will publish the first map of where Bengali students study, by subject — counts only, never names.</p></div>"""
    else:
        h = f"""<p>ভারত আর বাংলাদেশ থেকে কতজন বিদেশে পড়ে, কোথায়, কোন বিষয়ে। নিচের প্রতিটা সংখ্যার সঙ্গে লেখা আছে সেটা কী মাপে, কোন সময়ের, আর মূল সূত্র কী।</p>
<div class="invite"><p><b>চার রকম মাপ — কখনও যোগ করবেন না।</b><br>
<b>ভর্তি (enrolment)</b>: কোনো এক সময়ে বিশ্ববিদ্যালয়ে নথিভুক্ত ছাত্র (HESA, Destatis, Open Doors)।<br>
<b>OPT</b>: USA-তে Optional Practical Training ওয়ার্ক পারমিটে থাকা গ্র্যাজুয়েট। ক্লাস না করলেও Open Doors এঁদের মোট সংখ্যায় ধরে।<br>
<b>ভিসা দেওয়া (visa grants)</b>: এক বছরে দেওয়া ভিসা (UK Home Office)। দেশে মোট কতজন ছাত্র আছে, তা নয়।<br>
<b>সরকারি আনুমানিক হিসেব</b>: ভারতের বিদেশ মন্ত্রক (MEA) দূতাবাসগুলোর থেকে সংখ্যা জোগাড় করে, স্কুলের ছাত্রছাত্রী-সহ।</p></div>

<h2 id="india">ভারত: কতজন, কোথায়</h2>
<p>MEA, ১ জানুয়ারি ২০২৫: ১৫৩টি দেশে <b>18,82,318</b> জন ভারতীয় ছাত্রছাত্রী। এর মধ্যে <b>6,28,305 জন স্কুলের</b>; <b>বিশ্ববিদ্যালয় ও অন্যান্য উচ্চশিক্ষা প্রতিষ্ঠানে 12,54,013 জন (১২.৫৪ লাখ)</b>। দূতাবাসগুলো কীভাবে সংখ্যা জোগাড় করেছে, MEA-র টেবিলে তার কোনো ব্যাখ্যা নেই [mea]।</p>
<p>দেশভিত্তিক বিশ্ববিদ্যালয়-স্তরের ভারতীয় ছাত্রছাত্রী (MEA, ১ জানুয়ারি ২০২৫) [mea]:</p>
{bars(MEA_TERTIARY, lang, L, 427085)}
<p class="updated">* MEA-র জার্মানির সংখ্যা (49,483) জার্মানির সরকারি হিসেবে শীতকালীন সেমেস্টার ২০২৩/২৪-এর সংখ্যার সমান [destatis], অর্থাৎ টেবিলের তারিখের চেয়ে প্রায় এক বছর পুরোনো।</p>

<h2 id="usa">USA</h2>
{table(["মাপ", "সংখ্যা", "সময়", "সূত্র"], [
 ["Open Doors-এর মোট (ভর্তি + OPT)", "<b>3,63,019</b> জন ভারতীয়; সবচেয়ে বড় উৎস ভারত", "২০২৪/২৫", "IIE Open Doors [od_in] [od_pr]"],
 ["এর মধ্যে ভর্তি", "<b>2,19,279</b>: স্নাতকোত্তর 1,77,892, স্নাতক 40,135, নন-ডিগ্রি 1,252", "২০২৪/২৫", "[od_in]"],
 ["এর মধ্যে OPT", "<b>1,43,740</b> জন গ্র্যাজুয়েট ওয়ার্ক পারমিটে, ক্লাস করেন না", "২০২৪/২৫", "[od_in]"],
 ["SEVIS-এর সক্রিয় রেকর্ড", "ভারতীয় নাগরিকত্বের <b>4,22,335</b>টি F-1/M-1 রেকর্ড। মানুষ নয়, রেকর্ড গোনা; একজনের একাধিক রেকর্ড থাকতে পারে", "ক্যালেন্ডার বছর ২০২৪", "US ICE [sevis]"],
 ["নতুন বিদেশি ভর্তি, সব দেশ মিলিয়ে", "২০২৫-এর শরতে ১৭% কম (৮২৫+ প্রতিষ্ঠানের Fall Snapshot)", "শরৎ ২০২৫", "[od_pr]"],
], "USA-তে ভারতীয় ছাত্রছাত্রী — তিন রকম মাপ")}

<h2 id="uk">UK</h2>
{table(["মাপ", "সংখ্যা", "সময়", "সূত্র"], [
 ["ভারতীয় মূল আবেদনকারীদের দেওয়া স্টাডি ভিসা", "<b>82,523</b> — মোট 3,65,868-এর ২৩%; ১৬% কম", "জুন ২০২৬ পর্যন্ত এক বছর", "Home Office [ho]"],
 ["ভারতীয়দের দেওয়া Graduate-ভিসা এক্সটেনশন", "<b>64,495</b>", "জুন ২০২৬ পর্যন্ত এক বছর", "Home Office [ho]"],
 ["ভারত থেকে আসা ছাত্রের ভর্তি", "<b>1,46,480</b> (বিদেশি ছাত্রদের ২১.৪%) — <i>মূল সূত্রে এখনও যাচাই হয়নি</i>: আমাদের যাচাই-ব্যবস্থা HESA-র সাইট খুলতে পারেনি; Wikipedia HESA-কে উদ্ধৃত করে এই সংখ্যা দিয়েছে", "২০২৪/২৫", "HESA [hesa]; উদ্ধৃত [hesa_wiki]"],
], "UK-তে ভারতীয় ছাত্রছাত্রী — ভিসা আর ভর্তি")}

<h2 id="germany">জার্মানি</h2>
{table(["মাপ", "সংখ্যা", "সময়", "সূত্র"], [
 ["ভারত থেকে আসা আন্তর্জাতিক ছাত্র", "<b>প্রায় 69,000</b>; উৎস দেশ হিসেবে ভারত প্রথম", "শীতকালীন সেমেস্টার ২০২৫/২৬", "DAAD/DZHW, Wissenschaft weltoffen 2026 [wiwe]"],
 ["সংবাদমাধ্যমে দেওয়া সঠিক সংখ্যা", "69,816 (+১৭.৫%), DAAD-এর বলে উল্লেখ — <i>DAAD-এর কোনো প্রকাশনায় পাওয়া যায়নি</i>", "শীতকালীন সেমেস্টার ২০২৫/২৬", "[bs]"],
 ["ভারতীয় ছাত্র (ব্যাচেলর, মাস্টার্স, PhD)", "<b>59,419</b> (DAAD India সেমেস্টার উল্লেখ করেনি; সেপ্টেম্বর ২০২৫-এ প্রকাশিত)", "২০২৫-এর রিপোর্ট", "DAAD India [daad_in]"],
 ["ভারতীয় নাগরিকত্বের বিদেশি ছাত্র (সরকারি)", "<b>49,483</b>", "শীতকালীন সেমেস্টার ২০২৩/২৪", "Destatis [destatis]"],
], "জার্মানিতে ভারতীয় ছাত্রছাত্রী — সরকারি আর DAAD-এর হিসেব")}

<h2 id="other">অন্য দেশ, আর কেন কয়েকটায় কম যায়</h2>
<p>MEA, ১ জানুয়ারি ২০২৫। বিশ্ববিদ্যালয় আর স্কুল আলাদা গোনা [mea]:</p>
{table(["দেশ", "বিশ্ববিদ্যালয়/উচ্চশিক্ষা", "স্কুল", "কেন যায় — বা যায় না"], [
 ["অস্ট্রেলিয়া", "1,38,579", "57,529", "ইংরেজিতে ডিগ্রি আর পাসের পর কাজের সুযোগ।"],
 ["রাশিয়া", "27,000", "222", "বেশিরভাগ মেডিসিন (MBBS)। নতুন যাওয়া ২০২৩-এ 25,503 থেকে ২০২৪-এ 31,444 [bt]।"],
 ["কিরগিজস্তান / জর্জিয়া", "16,500 / 16,000", "50 / 20", "মূলত মেডিসিন।"],
 ["আয়ারল্যান্ড", "10,000", "10,000", "ইংরেজিতে পড়ানো, EU-র সদস্য।"],
 ["UAE", "6,507", "2,47,325", "বেশিরভাগই সেখানে থাকা ভারতীয় পরিবারের সন্তান। ২০২৪/২৫-এ দুবাইয়ের বিশ্ববিদ্যালয়ে 42,026 জন বিদেশি ছাত্রের ৪৩% ভারতীয় [khda]।"],
 ["চীন", "5,330", "9", "একসময় MBBS-এর বড় গন্তব্য; কোভিডের ভিসা নিষেধাজ্ঞায় হাজার হাজার ছাত্র আটকে ছিল, ক্লিনিক্যাল পড়াশোনা চীনা ভাষায়, আর ২০১৫–২১-এ চীনের ৪৫টি অনুমোদিত মেডিক্যাল স্কুলের মাত্র ১৬% গ্র্যাজুয়েট ভারতের লাইসেন্স পরীক্ষায় পাস করেছেন [cn]।"],
 ["সিঙ্গাপুর", "3,250", "30,000", "বিশ্ববিদ্যালয়ে আসন কম; NUS আর NTU-তে ভর্তি খুব কঠিন।"],
 ["জাপান", "1,532", "1,909", "ইংরেজিতে ডিগ্রি কম; মূল বাধা ভাষা।"],
], "অন্য দেশে ভারতীয় ছাত্রছাত্রী, ১ জানুয়ারি ২০২৫")}

<h2 id="bangladesh">বাংলাদেশ</h2>
{table(["মাপ", "সংখ্যা", "সময়", "সূত্র"], [
 ["USA-তে বাংলাদেশি ছাত্র (Open Doors-এর মোট)", "<b>20,156</b>, উৎস দেশ হিসেবে ৯ নম্বর; ভর্তি 17,166 (স্নাতকোত্তর 13,016, স্নাতক 4,041, নন-ডিগ্রি 109) + OPT 2,990", "২০২৪/২৫", "IIE Open Doors [od_bd]"],
 ["বিদেশে বাংলাদেশি ছাত্র, সব দেশ", "অন্তত <b>49,151</b> (UNESCO) — পুরোনো হিসেব, এখনকার মোট নয়; বড় গন্তব্য UAE 11,157, USA 8,665, মালয়েশিয়া 6,180", "২০২২", "UNESCO, The Daily Star-এর রিপোর্টে [unesco]"],
 ["একই, OECD-র হিসেব", "প্রায় <b>52,800</b>", "২০২২", "OECD, ICEF Monitor-এর রিপোর্টে [icef]"],
 ["UK স্টুডেন্ট-ভিসা বাতিলের হার", "বাংলাদেশি আবেদনের ২২% বাতিল; কয়েকটা UK বিশ্ববিদ্যালয় ভর্তি বন্ধ বা সীমিত করেছে", "সেপ্টেম্বর ২০২৫ পর্যন্ত এক বছর", "TBS News-এর রিপোর্টে [tbs]"],
], "বিদেশে বাংলাদেশি ছাত্রছাত্রী")}

<h2 id="subjects">কোন বিষয়ে ভারতীয় ছাত্ররা কোথায় পড়ে?</h2>
<p>নিচে দু-রকম তথ্য পাশাপাশি আছে, দুটো গুলিয়ে ফেলবেন না:</p>
<ul>
<li><b>ভারতীয় ছাত্রদের নিয়ে যা প্রকাশিত।</b> খুব অল্প কয়েকটা মোটা দাগের সংখ্যা আছে। DAAD India-র জার্মানির ভাগগুলো — ইঞ্জিনিয়ারিং (বায়োলজি-সংক্রান্ত বিষয়-সহ) ৬০%, সমাজবিজ্ঞান/অর্থনীতি/ম্যানেজমেন্ট ২১%, অঙ্ক/প্রাকৃতিক বিজ্ঞান ১৮%, অন্যান্য ৬% — যোগ করলে <b>১০৫%</b> হয়, তাই DAAD ব্যাখ্যা না দেওয়া পর্যন্ত এগুলোকে একটা গোটার আলাদা আলাদা ভাগ ধরা যায় না [daad_in]।</li>
<li><b>শুধু উদাহরণ, ভর্তির হিসেব নয়।</b> ২০২৬-এ QS যে বিশ্ববিদ্যালয়গুলোকে বিষয়ে উঁচু র‍্যাংক দিয়েছে [qs_subj]। সেখানে কতজন ভারতীয় পড়ে, তা এতে বোঝা যায় না। র‍্যাংকিং বড় গবেষণা-বিশ্ববিদ্যালয়ের দিকে ঝোঁকে; নিচের দিকেও অনেক ভালো, কম খরচের বিকল্প আছে।</li>
</ul>
{subject_table(lang)}
<p class="updated">“ভারতীয় ছাত্রদের সবচেয়ে পছন্দের বিশ্ববিদ্যালয়” জাতীয় কোনো তালিকা আমরা প্রকাশ করি না, কারণ এখনও কোনো সূত্র তা সমর্থন করে না।</p>

<h2 id="datasets">বিশ্ববিদ্যালয় আর বিষয় স্তরে কী তথ্য আছে</h2>
<ul>
<li><b>UK (HESA):</b> বিশ্ববিদ্যালয় আর ছাত্রের স্থায়ী ঠিকানার দেশ ধরে সংখ্যা দেয়, আর আলাদা ভাবে বিশ্ববিদ্যালয় আর বিষয় ধরে। তিনটে একসঙ্গে দেয় না, তাই “সবচেয়ে বেশি ভারতীয় কেমিস্ট্রি ছাত্র কোন বিশ্ববিদ্যালয়ে” — এমন তালিকা খোলা তথ্যে নেই; তার জন্য HESA-র কাছে আলাদা ডেটা অনুরোধ করতে হয় [hesa]।</li>
<li><b>জার্মানি (Destatis, DAAD/DZHW):</b> নাগরিকত্ব ধরে বিদেশি ছাত্রের জাতীয় সংখ্যা [destatis] আর মোটা দাগের বিষয়-গ্রুপ ধরে আন্তর্জাতিক ছাত্র [wiwe]। কিছু বিশ্ববিদ্যালয় নিজেরাই নাগরিকত্ব ধরে ছাত্রের টেবিল প্রকাশ করে, যেমন Saarland University [saar], কিন্তু বিশ্ববিদ্যালয় × বিষয় × নাগরিকত্ব — এমন জাতীয় টেবিল নেই।</li>
<li><b>USA (Open Doors, SEVIS):</b> উৎস দেশ আর পড়ার স্তর ধরে মোট সংখ্যা [od_in]; বিষয় আর প্রধান প্রতিষ্ঠানের হিসেব সব বিদেশি ছাত্র মিলিয়ে, দেশ ধরে নয় [sevis]। কিছু বিশ্ববিদ্যালয় নিজেদের আন্তর্জাতিক ছাত্রের রিপোর্ট প্রকাশ করে।</li>
<li><b>বাঙালি ছাত্রছাত্রী:</b> কোনো দেশ মাতৃভাষা ধরে ছাত্র গোনে না, আর ভারত সরকার শুধু সারা দেশের মোট সংখ্যা দেয় — সংসদে রাজ্যভিত্তিক হিসেব চাওয়া হলেও দেওয়া হয়নি [ls]।</li>
</ul>
<div class="invite"><p><b>গুনতে সাহায্য করুন।</b> আপনি যদি বিদেশে পড়া বাঙালি ছাত্র বা ছাত্রী হন, <a href="/bn/contribute/">যুক্ত হোন</a> পাতা দিয়ে আপনার বিষয় আর বিশ্ববিদ্যালয় (চাইলে নিজের জেলাও) জানান। যথেষ্ট উত্তর পেলে BiswaPath প্রকাশ করবে বাঙালি ছাত্রছাত্রীরা কোথায়, কোন বিষয়ে পড়ে তার প্রথম মানচিত্র — শুধু সংখ্যা, কারও নাম নয়।</p></div>"""
    kind = {"primary": ("original source", "মূল সূত্র"), "secondary": ("report of the figure", "সংখ্যার রিপোর্ট")}
    src = "".join(f'<li id="src-{k}"><a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a> <span class="ucity">— {kind[SRC[k][2]][0 if E else 1]}</span></li>' for k in ORDER)
    h = cite(h) + (f'<h2>{"Sources" if E else "সূত্র"}</h2><p class="updated">{"Each source is marked as the original source or a report of the figure. Where only a report was available, we say so." if E else "প্রতিটা সূত্রের পাশে লেখা আছে সেটা মূল সূত্র, নাকি সংখ্যার রিপোর্ট। যেখানে শুধু রিপোর্ট পাওয়া গেছে, সেটা বলে দিয়েছি।"}</p><ol class="srcs">{src}</ol>'
                   f'<p class="updated">{"Last checked" if E else "শেষ যাচাই"}: {ck}</p>')
    return title, desc, h
