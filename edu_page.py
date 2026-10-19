# Content for the "Education systems compared" page (imported by build.py)
# Revised 19 Oct 2026 using the BiswaPath Education Systems Review workbook (correction register C01–C14).
CHECKED = {"en": "19 October 2026", "bn": "১৯ অক্টোবর ২০২৬"}

SRC = {
 "wbchse": ("WBCHSE Notification L/PR/176/2024 (18 April 2024): semester system for Higher Secondary — copy published by WBXPRESS", "https://wbxpress.com/semester-system-higher-secondary-level-wbchse/"),
 "cbse": ("CBSE Circular Acad-14/2026: curriculum for 2026–27", "https://cbseacademic.nic.in/web_material/Circulars/2026/14_Circular_2026.pdf"),
 "ugc_ug": ("UGC undergraduate framework as adopted in West Bengal: Bankura University CCFUP regulations (from 2023–24)", "https://www.bankurauniv.ac.in/uploads/tempimagepdflink/1768551312.pdf"),
 "ugc_pg": ("UGC Curriculum and Credit Framework for Postgraduate Programmes (June 2024) — copy hosted by a university", "https://mits.ac.in/assets/pdf/iqac/Curriculum-and-Credit-Framework-for-Postgraduate-Programmes.pdf"),
 "ugc_phd": ("UGC (Minimum Standards and Procedures for Award of Ph.D. Degree) Regulations, 2022", "https://thc.nic.in/Central%20Governmental%20Regulations/University%20Grants%20Commission%20(Minimum%20Standrads%20and%20Procedures%20for%20Award%20of%20Ph.D%20Degree)%20Regulations,%202022.pdf"),
 "du_phd": ("University of Dhaka: PhD admission requirements (notice for foreign students)", "https://du.ac.bd/du_post_details/Education-Qualification-and-other-Relevant-Requirements-for-Admission-in-Ph.D.-Programme-for--foreign-students/13964"),
 "bd": ("Bangladesh education system (Government of Alberta international education guide)", "https://www.alberta.ca/international-education-guide-bangladesh"),
 "ucas": ("UCAS: the UK degree system", "https://www.ucas.com/international/international-advisers/supporting-international-students/the-uk-degree-system"),
 "qs": ("SQA: Becoming Qualifications Scotland (began 1 February 2026)", "https://www.sqa.org.uk/sqa/116467.html"),
 "nq": ("SQA: National Qualifications (National 5, Higher, Advanced Higher)", "https://www.sqa.org.uk/sqa/96425.html"),
 "scot_ma": ("Times Higher Education: the Scottish undergraduate MA", "https://www.timeshighereducation.com/node/25107"),
 "eurydice": ("Eurydice (European Commission): Bachelor's degrees in Germany", "https://eurydice.eacea.ec.europa.eu/eurypedia/germany/bachelor"),
 "daad": ("DAAD: ways to your PhD in Germany", "https://www.daad.de/en/studying-in-germany/phd-studies-research/ways-to-your-phd/"),
 "nces": ("NCES: state high school graduation requirements", "https://nces.ed.gov/programs/statereform/3_hsc.asp"),
 "sed": ("NSF Survey of Earned Doctorates 2023, Table 8-1 (time to doctorate)", "https://ncses.nsf.gov/pubs/nsf24336/assets/data-tables/tables/nsf24336-tab008-001.pdf"),
 "enic": ("UK ENIC: recognition of international qualifications", "https://www.enic.org.uk/"),
}
ORDER = ["wbchse", "cbse", "ugc_ug", "ugc_pg", "ugc_phd", "bd", "du_phd", "ucas", "qs", "nq", "scot_ma", "eurydice", "daad", "nces", "sed", "enic"]
def s(k): return list(ORDER).index(k) + 1   # citation number

T = {
"en": dict(
 title="Education systems compared",
 desc="West Bengal and India compared with Bangladesh, England, Scotland, Germany and the USA: school qualifications, degree lengths and PhD rules, with official sources.",
 intro="How school and university stages are organised in West Bengal and India, Bangladesh, England, Scotland, Germany and the USA. This is a guide to <em>structure</em>, not a qualification-equivalence table: two qualifications taken at a similar age are not automatically equal, and syllabuses can differ a lot.",
 warn_h="Who decides what counts",
 warn="Only the university you apply to (and, where relevant, the national recognition body, such as <a href=\"https://www.enic.org.uk/\" target=\"_blank\" rel=\"noopener\">UK ENIC</a>) decides whether your qualification meets its entry requirements. Always check the entry requirements on the course page. Wales and Northern Ireland are not covered yet.",
 school_h="1. School qualifications",
 degree_h="2. Bachelor's and master's degrees",
 phd_h="3. PhD",
 cols_school=["System", "Typical school stages", "Main qualifications", "Who sets the rules", "Take care"],
 cols_degree=["System", "Bachelor's", "Master's", "Take care"],
 cols_phd=["System", "Usual entry", "Coursework", "Assessment", "Typical length", "Take care"],
 changes_h="Recent changes",
 changes=[
  f"<b>West Bengal Higher Secondary is semester-based.</b> WBCHSE Notification L/PR/176/2024 (18 April 2024) split Class XI–XII into four semesters: Class XI from 2024–25, Class XII from 2025–26. Semesters I and III use multiple-choice questions; II and IV use short and descriptive answers. The Council conducts Semesters III and IV. [{'{'}wbchse{'}'}]",
  "<b>CBSE has a new curriculum for 2026–27.</b> Released 1–2 April 2026; it brings the NCF-2023 scheme of studies into Class IX. [{cbse}]",
  "<b>Indian bachelor's degrees can now be 3 or 4 years.</b> Under the UGC undergraduate framework, a student can leave with a certificate after 1 year, a diploma after 2, a degree after 3, or an Honours (or Honours with Research) after 4. Each university adopts it separately: Bankura University, for example, from 2023–24. [{ugc_ug}]",
  "<b>Indian master's: 1 or 2 years.</b> The UGC postgraduate framework (June 2024) allows a 1-year master's after a 4-year Honours degree (160 credits) and a 2-year master's after a 3-year degree (120 credits). Universities implement it in their own regulations. [{ugc_pg}]",
  "<b>Scotland has a new qualifications body.</b> Qualifications Scotland replaced the SQA on 1 February 2026. National 5, Higher and Advanced Higher courses continue. [{qs}]",
 ],
 src_h="Sources", checked="Last checked", note_src="Numbers in square brackets refer to these sources. Where an official site could not be reached directly, we cite a faithful published copy and say so.",
 next_h="Coming next", next="A topic-by-topic Chemistry comparison: Madhyamik and Higher Secondary alongside GCSE and A-level.",
),
"bn": dict(
 title="শিক্ষাব্যবস্থার তুলনা",
 desc="পশ্চিমবঙ্গ ও ভারতের সঙ্গে বাংলাদেশ, ইংল্যান্ড, স্কটল্যান্ড, জার্মানি ও USA-র তুলনা: স্কুলের যোগ্যতা, ডিগ্রির মেয়াদ আর PhD-র নিয়ম, অফিসিয়াল সূত্র-সহ।",
 intro="পশ্চিমবঙ্গ ও ভারত, বাংলাদেশ, ইংল্যান্ড, স্কটল্যান্ড, জার্মানি আর USA-তে স্কুল আর বিশ্ববিদ্যালয়ের ধাপগুলো কীভাবে সাজানো। এটা <em>কাঠামো</em>-র গাইড, যোগ্যতার সমতুল্যতার তালিকা নয়: প্রায় একই বয়সে নেওয়া দুটো যোগ্যতা আপনা থেকে সমান হয় না, আর সিলেবাসেও অনেক তফাত থাকতে পারে।",
 warn_h="কোনটা গণ্য হবে, তা কে ঠিক করে",
 warn="আপনার যোগ্যতা এন্ট্রি রিকোয়ারমেন্ট পূরণ করে কি না, তা ঠিক করে শুধু যে বিশ্ববিদ্যালয়ে আবেদন করছেন তারা (আর দরকার হলে জাতীয় স্বীকৃতি সংস্থা, যেমন <a href=\"https://www.enic.org.uk/\" target=\"_blank\" rel=\"noopener\">UK ENIC</a>)। কোর্স পেজে এন্ট্রি রিকোয়ারমেন্ট অবশ্যই দেখুন। ওয়েলস আর নর্দার্ন আয়ারল্যান্ড এখনও যোগ করা হয়নি।",
 school_h="১. স্কুলের যোগ্যতা",
 degree_h="২. স্নাতক (ব্যাচেলর) আর স্নাতকোত্তর (মাস্টার্স)",
 phd_h="৩. PhD",
 cols_school=["ব্যবস্থা", "স্কুলের সাধারণ ধাপ", "প্রধান যোগ্যতা", "নিয়ম কে ঠিক করে", "সাবধান"],
 cols_degree=["ব্যবস্থা", "ব্যাচেলর", "মাস্টার্স", "সাবধান"],
 cols_phd=["ব্যবস্থা", "সাধারণ যোগ্যতা", "কোর্সওয়ার্ক", "মূল্যায়ন", "সাধারণ মেয়াদ", "সাবধান"],
 changes_h="সাম্প্রতিক পরিবর্তন",
 changes=[
  "<b>পশ্চিমবঙ্গের উচ্চ মাধ্যমিক এখন সেমেস্টারে।</b> WBCHSE বিজ্ঞপ্তি L/PR/176/2024 (১৮ এপ্রিল ২০২৪) একাদশ-দ্বাদশকে চারটি সেমেস্টারে ভাগ করেছে: একাদশ ২০২৪–২৫ থেকে, দ্বাদশ ২০২৫–২৬ থেকে। সেমেস্টার I আর III-এ MCQ; II আর IV-এ ছোট ও বর্ণনামূলক প্রশ্ন। সেমেস্টার III আর IV-এর পরীক্ষা নেয় কাউন্সিল। [{wbchse}]",
  "<b>CBSE-র ২০২৬–২৭-এর নতুন কারিকুলাম।</b> ১–২ এপ্রিল ২০২৬-এ প্রকাশিত; নবম শ্রেণিতে NCF-2023 পাঠক্রম চালু। [{cbse}]",
  "<b>ভারতে স্নাতক এখন ৩ বা ৪ বছরের।</b> UGC-র কাঠামোয় ১ বছর পর সার্টিফিকেট, ২ বছর পর ডিপ্লোমা, ৩ বছর পর ডিগ্রি, বা ৪ বছর পর অনার্স (বা রিসার্চ-সহ অনার্স) নিয়ে বেরোনো যায়। প্রতিটি বিশ্ববিদ্যালয় আলাদা করে চালু করে: যেমন বাঁকুড়া বিশ্ববিদ্যালয় ২০২৩–২৪ থেকে। [{ugc_ug}]",
  "<b>ভারতে মাস্টার্স ১ বা ২ বছরের।</b> UGC-র পোস্টগ্র্যাজুয়েট কাঠামো (জুন ২০২৪) অনুযায়ী ৪ বছরের অনার্সের (১৬০ ক্রেডিট) পর ১ বছরের, আর ৩ বছরের ডিগ্রির (১২০ ক্রেডিট) পর ২ বছরের মাস্টার্স। বিশ্ববিদ্যালয়গুলো নিজেদের নিয়মে তা চালু করে। [{ugc_pg}]",
  "<b>স্কটল্যান্ডে নতুন সংস্থা।</b> ১ ফেব্রুয়ারি ২০২৬ থেকে SQA-র জায়গায় Qualifications Scotland। National 5, Higher আর Advanced Higher কোর্স চলছে। [{qs}]",
 ],
 src_h="সূত্র", checked="শেষ যাচাই", note_src="বন্ধনীর সংখ্যাগুলো এই সূত্রগুলোকে বোঝায়। কোনো অফিসিয়াল সাইট সরাসরি খোলা না গেলে আমরা তার নির্ভরযোগ্য প্রকাশিত কপি দিয়েছি আর সেটা উল্লেখ করেছি।",
 next_h="এরপর আসছে", next="বিষয়ভিত্তিক কেমিস্ট্রির তুলনা: মাধ্যমিক আর উচ্চ মাধ্যমিকের পাশে GCSE আর A-level।",
)}

SCHOOL = {
"en": [
 ["West Bengal state boards", "Classes 9–10, then 11–12", "Madhyamik (WBBSE); Higher Secondary (WBCHSE), now in four semesters", "Two state boards: WBBSE and WBCHSE", "Check syllabuses by year: the HS semester system changed what is examined [{wbchse}]"],
 ["CBSE (national board)", "Classes 9–10, then 11–12", "CBSE Class 10; CBSE Class 12", "CBSE publishes a curriculum each year", "CBSE schools in West Bengal follow CBSE, not the state board [{cbse}]"],
 ["CISCE (national board)", "Classes 9–10, then 11–12", "ICSE (Class 10); ISC (Class 12)", "CISCE sets separate ICSE and ISC syllabuses", "ICSE and ISC are different qualifications"],
 ["Bangladesh", "Secondary, then higher secondary (12 years of school)", "SSC (after Grade 10); HSC (after Grade 12)", "Education boards; general, madrasah and technical streams", "Not automatically the same as Indian Class 10 or 12 [{bd}]"],
 ["England", "Key Stage 4, then sixth form or college", "GCSE; then A-levels or other post-16 routes", "Exam boards, regulated by Ofqual", "A-levels are not the only route after 16"],
 ["Scotland", "Broad general education, then the senior phase (S4–S6)", "National 5; Higher; Advanced Higher", "Qualifications Scotland (replaced the SQA on 1 February 2026)", "National 5 is not a GCSE by default; schools choose subject levels [{qs}] [{nq}]"],
 ["Germany", "School types and tracks vary by federal state", "Abitur (general university entrance qualification), usually after 12 or 13 years — one of several routes", "Each federal state (Land)", "Not every student takes the Gymnasium/Abitur route"],
 ["United States", "High school, usually Grades 9–12", "High school diploma; optional AP or IB courses", "States and school districts set graduation rules", "No single national exam like GCSE or A-level [{nces}]"],
],
"bn": [
 ["পশ্চিমবঙ্গের রাজ্য বোর্ড", "ক্লাস ৯–১০, তারপর ১১–১২", "মাধ্যমিক (WBBSE); উচ্চ মাধ্যমিক (WBCHSE), এখন চার সেমেস্টারে", "দুটি রাজ্য বোর্ড: WBBSE আর WBCHSE", "সাল দেখে সিলেবাস মেলান: সেমেস্টার চালু হওয়ায় পরীক্ষার বিষয়বস্তু বদলেছে [{wbchse}]"],
 ["CBSE (জাতীয় বোর্ড)", "ক্লাস ৯–১০, তারপর ১১–১২", "CBSE Class 10; CBSE Class 12", "CBSE প্রতি বছর কারিকুলাম প্রকাশ করে", "পশ্চিমবঙ্গের CBSE স্কুল রাজ্য বোর্ড নয়, CBSE মেনে চলে [{cbse}]"],
 ["CISCE (জাতীয় বোর্ড)", "ক্লাস ৯–১০, তারপর ১১–১২", "ICSE (ক্লাস ১০); ISC (ক্লাস ১২)", "CISCE আলাদা ICSE আর ISC সিলেবাস দেয়", "ICSE আর ISC দুটো আলাদা যোগ্যতা"],
 ["বাংলাদেশ", "মাধ্যমিক, তারপর উচ্চ মাধ্যমিক (১২ বছর স্কুল)", "SSC (দশম শ্রেণির পর); HSC (দ্বাদশ শ্রেণির পর)", "শিক্ষা বোর্ড; সাধারণ, মাদ্রাসা আর কারিগরি ধারা", "ভারতের ক্লাস ১০ বা ১২-এর সঙ্গে আপনা থেকে সমান নয় [{bd}]"],
 ["ইংল্যান্ড", "Key Stage 4, তারপর সিক্সথ ফর্ম বা কলেজ", "GCSE; তারপর A-level বা ১৬-র পরের অন্য পথ", "পরীক্ষা বোর্ড, নিয়ন্ত্রক Ofqual", "১৬-র পর A-level-ই একমাত্র পথ নয়"],
 ["স্কটল্যান্ড", "ব্রড জেনারেল এডুকেশন, তারপর সিনিয়র ফেজ (S4–S6)", "National 5; Higher; Advanced Higher", "Qualifications Scotland (১ ফেব্রুয়ারি ২০২৬ থেকে SQA-র জায়গায়)", "National 5 আপনা থেকে GCSE নয়; বিষয়ের স্তর স্কুল ঠিক করে [{qs}] [{nq}]"],
 ["জার্মানি", "রাজ্য অনুযায়ী স্কুলের ধরন আর ধারা আলাদা", "Abitur (বিশ্ববিদ্যালয়ে ঢোকার সাধারণ যোগ্যতা), সাধারণত ১২ বা ১৩ বছর পর — কয়েকটি পথের একটি", "প্রতিটি রাজ্য (Land)", "সব ছাত্রছাত্রী Gymnasium/Abitur পথে যায় না"],
 ["USA", "হাই স্কুল, সাধারণত গ্রেড ৯–১২", "হাই স্কুল ডিপ্লোমা; ঐচ্ছিক AP বা IB কোর্স", "রাজ্য আর স্কুল ডিস্ট্রিক্ট পাশের নিয়ম ঠিক করে", "GCSE বা A-level-এর মতো একটা জাতীয় পরীক্ষা নেই [{nces}]"],
]}

DEGREE = {
"en": [
 ["India (UGC framework)", "BA/BSc: 3-year degree or 4-year Honours / Honours with Research; exit points after each year [{ugc_ug}]", "MA/MSc: 1 year after a 4-year Honours (160 credits); 2 years after a 3-year degree (120 credits) [{ugc_pg}]", "Each university adopts the framework in its own regulations; colleges are not all identical"],
 ["Bangladesh", "Pass degree 3 years; Honours 4 years [{bd}]", "Usually 1 year after Honours; 2 years after a Pass degree [{bd}]", "Each university sets its own degree regulations"],
 ["England", "Usually 3 years full-time [{ucas}]", "Taught master's usually 1 year full-time [{ucas}]", "Integrated master's (e.g. MChem) and longer professional degrees exist"],
 ["Scotland", "Honours degree usually 4 years [{ucas}]", "Taught master's usually 1 year full-time", "At the ancient universities, an MA in arts subjects can be a 4-year undergraduate degree [{scot_ma}]"],
 ["Germany", "Standard period 6–8 semesters (3–4 years); at least 180 ECTS credits [{eurydice}]", "Consecutive bachelor's + master's: 5 years in total at universities (master's often 2–4 semesters) [{eurydice}]", "Programmes and regulated professions differ"],
 ["United States", "Usually 4 years, with general education plus a major", "Varies, often 1–2 years", "Credit requirements vary by institution"],
],
"bn": [
 ["ভারত (UGC কাঠামো)", "BA/BSc: ৩ বছরের ডিগ্রি বা ৪ বছরের অনার্স / রিসার্চ-সহ অনার্স; প্রতি বছর বেরোনোর সুযোগ [{ugc_ug}]", "MA/MSc: ৪ বছরের অনার্সের (১৬০ ক্রেডিট) পর ১ বছর; ৩ বছরের ডিগ্রির (১২০ ক্রেডিট) পর ২ বছর [{ugc_pg}]", "প্রতিটি বিশ্ববিদ্যালয় নিজের নিয়মে কাঠামো চালু করে; সব কলেজ এক রকম নয়"],
 ["বাংলাদেশ", "পাস ডিগ্রি ৩ বছর; অনার্স ৪ বছর [{bd}]", "সাধারণত অনার্সের পর ১ বছর; পাস ডিগ্রির পর ২ বছর [{bd}]", "প্রতিটি বিশ্ববিদ্যালয় নিজের ডিগ্রির নিয়ম ঠিক করে"],
 ["ইংল্যান্ড", "পূর্ণ সময়ে সাধারণত ৩ বছর [{ucas}]", "টট মাস্টার্স পূর্ণ সময়ে সাধারণত ১ বছর [{ucas}]", "ইন্টিগ্রেটেড মাস্টার্স (যেমন MChem) আর দীর্ঘতর পেশাদার ডিগ্রিও আছে"],
 ["স্কটল্যান্ড", "অনার্স ডিগ্রি সাধারণত ৪ বছর [{ucas}]", "টট মাস্টার্স পূর্ণ সময়ে সাধারণত ১ বছর", "পুরোনো বিশ্ববিদ্যালয়গুলোতে কলা বিভাগের MA হতে পারে ৪ বছরের স্নাতক ডিগ্রি [{scot_ma}]"],
 ["জার্মানি", "নির্ধারিত মেয়াদ ৬–৮ সেমেস্টার (৩–৪ বছর); অন্তত ১৮০ ECTS ক্রেডিট [{eurydice}]", "পরপর ব্যাচেলর + মাস্টার্স: বিশ্ববিদ্যালয়ে মোট ৫ বছর (মাস্টার্স প্রায়ই ২–৪ সেমেস্টার) [{eurydice}]", "প্রোগ্রাম আর নিয়ন্ত্রিত পেশা অনুযায়ী তফাত"],
 ["USA", "সাধারণত ৪ বছর, জেনারেল এডুকেশন আর একটি মেজর", "আলাদা আলাদা, প্রায়ই ১–২ বছর", "ক্রেডিটের নিয়ম প্রতিষ্ঠান অনুযায়ী আলাদা"],
]}

PHD = {
"en": [
 ["India", "Master's (usually 55% or equivalent), or a 4-year bachelor's with at least 75% [{ugc_phd}]", "Required: at least 12 credits, including research ethics", "Supervisor, progress reviews, thesis and viva", "Regulatory minimum 3 years (including coursework), maximum 6 years. Extensions are separate: up to 2 more years by re-registration, plus 2 for women and PwD scholars [{ugc_phd}]", "Meeting eligibility does not guarantee a place: universities select by their own tests and interviews"],
 ["Bangladesh", "Varies by university. At the University of Dhaka: an MPhil, or a 4-year Honours + 1-year master's, or (with extra conditions) a 3-year Honours + master's [{du_phd}]", "Varies by institution", "Supervisor, thesis and defence", "No single national length", "An MPhil is one route, not a universal requirement [{du_phd}]"],
 ["England", "Usually a good honours degree or a master's, depending on the programme", "Usually little formal coursework", "Supervision, milestones, thesis and viva", "Often around 3–4 years full-time [{ucas}]", "Funded doctoral training programmes may add taught elements"],
 ["Scotland", "Set by each university and programme", "Usually little formal coursework", "Supervision, thesis and viva", "Often around 3–4 years full-time", "Some doctoral training programmes are structured"],
 ["Germany", "Usually a relevant master's or equivalent", "Individual doctorate: little; structured programme: a course curriculum [{daad}]", "Dissertation and oral examination", "Individual doctorate usually 3–5 years; structured programme 3–4 years [{daad}]", "Funding and employment status vary widely"],
 ["United States", "Often a bachelor's; a master's is not always required", "Usually substantial coursework in the first years", "Adviser and committee, qualifying exams, dissertation and defence", "Median 5.7 years from starting the doctoral programme (2023, science and engineering) [{sed}]", "Strongly depends on the field"],
],
"bn": [
 ["ভারত", "মাস্টার্স (সাধারণত ৫৫% বা সমতুল্য), অথবা অন্তত ৭৫% নম্বর-সহ ৪ বছরের স্নাতক [{ugc_phd}]", "বাধ্যতামূলক: অন্তত ১২ ক্রেডিট, রিসার্চ এথিক্স-সহ", "সুপারভাইজার, অগ্রগতির পর্যালোচনা, থিসিস আর ভাইভা", "নিয়মমাফিক ন্যূনতম ৩ বছর (কোর্সওয়ার্ক-সহ), সর্বোচ্চ ৬ বছর। এক্সটেনশন আলাদা: রি-রেজিস্ট্রেশনে আরও ২ বছর পর্যন্ত, মহিলা ও প্রতিবন্ধী গবেষকদের আরও ২ বছর [{ugc_phd}]", "যোগ্যতা থাকলেই জায়গা নিশ্চিত নয়: বিশ্ববিদ্যালয় নিজের পরীক্ষা আর ইন্টারভিউয়ে বাছাই করে"],
 ["বাংলাদেশ", "বিশ্ববিদ্যালয় অনুযায়ী আলাদা। ঢাকা বিশ্ববিদ্যালয়ে: MPhil, অথবা ৪ বছরের অনার্স + ১ বছরের মাস্টার্স, অথবা (অতিরিক্ত শর্তে) ৩ বছরের অনার্স + মাস্টার্স [{du_phd}]", "প্রতিষ্ঠান অনুযায়ী আলাদা", "সুপারভাইজার, থিসিস আর ডিফেন্স", "একক জাতীয় মেয়াদ নেই", "MPhil একটা পথ, সবার জন্য বাধ্যতামূলক নয় [{du_phd}]"],
 ["ইংল্যান্ড", "প্রোগ্রাম অনুযায়ী সাধারণত ভালো অনার্স ডিগ্রি বা মাস্টার্স", "সাধারণত সামান্য আনুষ্ঠানিক কোর্সওয়ার্ক", "সুপারভিশন, মাইলস্টোন, থিসিস আর ভাইভা", "পূর্ণ সময়ে প্রায়ই ৩–৪ বছর [{ucas}]", "ফান্ডেড ডক্টরাল ট্রেনিং প্রোগ্রামে ক্লাসও থাকতে পারে"],
 ["স্কটল্যান্ড", "প্রতিটি বিশ্ববিদ্যালয় আর প্রোগ্রাম ঠিক করে", "সাধারণত সামান্য আনুষ্ঠানিক কোর্সওয়ার্ক", "সুপারভিশন, থিসিস আর ভাইভা", "পূর্ণ সময়ে প্রায়ই ৩–৪ বছর", "কিছু ডক্টরাল ট্রেনিং প্রোগ্রাম স্ট্রাকচার্ড"],
 ["জার্মানি", "সাধারণত সংশ্লিষ্ট বিষয়ে মাস্টার্স বা সমতুল্য", "ব্যক্তিগত ডক্টরেটে কম; স্ট্রাকচার্ড প্রোগ্রামে কোর্স কারিকুলাম [{daad}]", "ডিসার্টেশন আর মৌখিক পরীক্ষা", "ব্যক্তিগত ডক্টরেট সাধারণত ৩–৫ বছর; স্ট্রাকচার্ড প্রোগ্রাম ৩–৪ বছর [{daad}]", "ফান্ডিং আর চাকরির শর্ত অনেক আলাদা"],
 ["USA", "প্রায়ই ব্যাচেলর; মাস্টার্স সবসময় লাগে না", "প্রথম কয়েক বছর সাধারণত অনেক কোর্সওয়ার্ক", "অ্যাডভাইজার ও কমিটি, কোয়ালিফাইং পরীক্ষা, ডিসার্টেশন আর ডিফেন্স", "ডক্টরাল প্রোগ্রাম শুরু থেকে মিডিয়ান ৫.৭ বছর (২০২৩, বিজ্ঞান ও ইঞ্জিনিয়ারিং) [{sed}]", "বিষয় অনুযায়ী অনেক তফাত"],
]}

import re
def cite(text):
    return re.sub(r"\[\{(\w+)\}\]", lambda m: f'<sup><a href="#src-{m.group(1)}">[{s(m.group(1))}]</a></sup>', text.replace("{'{'}", "{").replace("{'}'}", "}"))

def table(cols, rows, cap):
    head = "".join(f'<th scope="col">{c}</th>' for c in cols)
    body = ""
    for r in rows:
        body += "<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f'<td data-label="{cols[i+1]}">{cite(x)}</td>' for i, x in enumerate(r[1:])) + "</tr>"
    return f'<div class="tablewrap stack"><table class="cmp"><caption>{cap}</caption><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'

def content(lang):
    t = T[lang]; ck = CHECKED[lang]
    cap = lambda h: f"{h} — {t['checked']}: {ck}"
    src = "".join(f'<li id="src-{k}"><a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a></li>' for k in ORDER)
    inner = f"""<p>{t['intro']}</p>
<div class="invite"><p><b>{t['warn_h']}.</b> {t['warn']}</p></div>
<h2>{t['school_h']}</h2>{table(t['cols_school'], SCHOOL[lang], cap(t['school_h']))}
<h2>{t['degree_h']}</h2>{table(t['cols_degree'], DEGREE[lang], cap(t['degree_h']))}
<h2>{t['phd_h']}</h2>{table(t['cols_phd'], PHD[lang], cap(t['phd_h']))}
<h2>{t['changes_h']}</h2><ul>{''.join(f'<li>{cite(x)}</li>' for x in t['changes'])}</ul>
<h2>{t['next_h']}</h2><p>{t['next']}</p>
<h2>{t['src_h']}</h2><p class="updated">{t['note_src']}</p><ol class="srcs">{src}</ol>
<p class="updated">{t['checked']}: {ck}</p>"""
    return t["title"], t["desc"], inner
