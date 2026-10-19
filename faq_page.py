# Content for the FAQ page for students and parents (imported by build.py)
# Every figure is in the local currency with an approximate INR estimate. Checked 19 Oct 2026.
import re

CHECKED = {"en": "19 October 2026", "bn": "১৯ অক্টোবর ২০২৬"}

# Rates derived from ECB euro reference rates of 16 Oct 2026 (1 EUR = 106.8640 INR = 1.1253 USD = 0.84385 GBP = 11.1450 SEK)
RATE = {"£": 126.6, "$": 95.0, "€": 106.9, "SEK": 9.59, "CAD": 67.45, "AUD": 66.32, "AED": 25.87}

def inr(v, lang):
    lakh = "lakh" if lang == "en" else "লাখ"
    if v >= 1e7:
        return f"₹{v/1e7:.2f} crore" if lang == "en" else f"₹{v/1e7:.2f} কোটি"
    if v >= 1e6:
        return f"₹{v/1e5:.1f} {lakh}"
    if v >= 1e5:
        return f"₹{v/1e5:.2f} {lakh}"
    return f"₹{round(v, -2):,.0f}"

def M(lang):
    """returns a function m(amount, cur, suffix='') -> '£1,529 (≈ ₹1.94 lakh)'"""
    def m(a, cur, suffix=""):
        n = f"{a:,.2f}" if a != int(a) else f"{int(a):,}"
        loc = f"{cur} {n}" if cur in ("SEK", "CAD", "AUD", "AED") else f"{cur}{n}"
        return f'{loc}{suffix} <span class="inr">(≈ {inr(a * RATE[cur], lang)})</span>'
    return m

SRC = {
 "ecb": ("European Central Bank: euro foreign exchange reference rates (16 October 2026)", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"),
 "uk_money": ("GOV.UK: Student visa — money you need", "https://www.gov.uk/student-visa/money"),
 "uk_visa": ("GOV.UK: Student visa — overview, fee and when to apply", "https://www.gov.uk/student-visa"),
 "uk_ihs": ("GOV.UK: Immigration health surcharge — how much you pay", "https://www.gov.uk/healthcare-immigration-application/how-much-pay"),
 "uk_work": ("Uni2Study summary: UK student work hours and Graduate Route changes from 2027 (check GOV.UK Graduate visa page)", "https://www.uni2study.com/articles/uk-student-visa-work-hours-20-graduate-route"),
 "uk_stats": ("Home Office: Why do people come to the UK? Study (year ending June 2026)", "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2026/why-do-people-come-to-the-uk-study"),
 "uk_rent": ("HEPI: 2024 Accommodation Costs Survey (Unipol/HEPI), London figures", "https://www.hepi.ac.uk/?p=29520"),
 "de_block": ("study.eu: German blocked account amount for 2026 (confirm with your German mission)", "https://www.study.eu/article/germany-blocked-bank-accounts-for-students-guide"),
 "de_work": ("Make it in Germany (Federal Government): working while studying and after graduation", "https://make-it-in-germany.com/en/looking-for-foreign-professionals/entering/admission-labour-market/students"),
 "de_rent": ("MLP Studentenwohnreport 2025 (press release, 1 October 2025)", "https://mlp-se.de/redaktion/mlp-se-de/presse/pressemitteilungen/2025/mlp-se-pm-d-01102025.pdf"),
 "de_ins": ("GradGermany: student visa, blocked account and health insurance guide", "https://www.gradgermany.com/blog/germany-student-visa-guide-blocked-account-insurance"),
 "de_stats": ("DAAD/DZHW: Wissenschaft weltoffen 2026 press release (14 October 2026)", "https://bildungsklick.de/hochschule-und-forschung/detail/deutschland-weltweit-standort-studium-promotion"),
 "se_money": ("Migrationsverket: residence permit for higher education — money and work rules", "https://www.migrationsverket.se/en/you-want-to-extend/study/higher-education.html"),
 "se_job": ("Migrationsverket: permit to look for work after your studies", "https://www.migrationsverket.se/en/you-want-to-extend/study/look-for-work-after-completing-your-studies-in-sweden.html"),
 "se_budget": ("Uppsala University: financial matters (monthly student budget)", "https://www.uu.se/en/study/masters-studies/living-in-sweden/financing"),
 "us_fees": ("Boston University ISSO: visa integrity fee, visa fee and SEVIS fee (May 2026)", "https://www.bu.edu/isso/2026/05/19/visa-integrity-fee/"),
 "us_work": ("NACE: guide to work options for international students (F-1, OPT, STEM OPT)", "https://naceweb.org/public-policy-and-legal/legislation-and-regulations/a-guide-to-work-options-for-foreign-students"),
 "us_cost": ("University of Illinois Urbana-Champaign: 2026–27 MSPE programme costs", "https://economics.illinois.edu/academics/master-science-policy-economics/admission/program-costs/2026-2027-mspe-program-costs"),
 "us_stats": ("Open Doors 2025: India fact sheet (IIE)", "https://opendoorsdata.org/wp-content/uploads/2026/01/OD_India_Fact-Sheet-2025.pdf"),
 "mea": ("Ministry of External Affairs (India): Data on Indian students abroad, as on 1 January 2025", "https://www.mea.gov.in/Images/CPV/557-en-01-04-12-2025.pdf"),
 "chevening": ("Business Today: Chevening 2027/28 opens — deadline and what it covers", "https://www.businesstoday.in/nri/story/chevening-scholarship-opens-for-2027-28-who-can-apply-what-it-covers-key-deadline-for-indians-555345-2026-09-14"),
 "csc": ("Commonwealth Scholarship Commission: Commonwealth Master's Scholarships", "https://cscuk.fcdo.gov.uk/masters"),
 "great_in": ("Careers360: GREAT Scholarships 2027 for Indian students (British Council)", "https://news.careers360.com/4-uk-universities-offer-indian-students-10000-pounds-great-scholarships-2027-postgraduate-courses-british-council"),
 "great_bd": ("British Council Study UK: GREAT Scholarships — Bangladesh", "https://study-uk.britishcouncil.org/scholarships-funding/great-scholarships/bangladesh"),
 "daad": ("GradRight: DAAD scholarship amounts for Indian students (check daad.in)", "https://gradright.com/daad-scholarship-for-indian-students-eligibility-benefits-and-how-to-apply/"),
 "si": ("IndiaScholarships: Swedish Institute Scholarships for Global Professionals (check si.se)", "https://www.indiascholarships.in/scholarships/swedish-institute-scholarships-for-global-professionals"),
 "fulbright": ("IndiaScholarships: Fulbright-Nehru Master's Fellowships (official site: usief.org.in)", "https://www.indiascholarships.in/scholarships/fulbright-nehru-masters-fellowships"),
 "madad": ("Consulate General of India, Chicago: student registration on the MADAD portal", "https://cgichicago.gov.in/page/student-registration-at-madad-portal"),
 "qs": ("QS Top Universities: the world's top 100 universities (QS World University Rankings 2027)", "https://www.topuniversities.com/student-info/choosing-university/worlds-top-100-universities"),
 "ca_funds": ("CIC News: Canada raises study permit proof of funds from 1 September 2026", "https://www.cicnews.com/2026/08/canada-hikes-funds-needed-by-study-permit-applicants-0879805.html/amp"),
 "ca_rules": ("IDP: Canada visa rules for international students in 2026 (confirm on canada.ca)", "https://www.idp.com/india/blog/visa-rules-for-international-students-canada/"),
 "au_visa": ("Ardent Overseas: Australia student visa rules 2026 (confirm on immi.homeaffairs.gov.au)", "https://ardentoverseas.com/study-in-australia/student-visa/"),
 "au_485": ("AHC Lawyers: Temporary Graduate visa (subclass 485) streams (January 2026)", "https://www.ahclawyers.com/news-articles/26/01/30/which-temporary-graduate-visa-subclass-485-stream-is-for-you"),
 "uae_visa": ("Gulf News: UAE student visa rules for new applicants and renewals", "https://gulfnews.com/uae/government/uae-student-visa-rules-for-new-applicants-renewals-outlined-1.102495102"),
 "uae_qs": ("Gulf News: UAE universities in the QS World University Rankings 2027", "https://gulfnews.com/amp/story/uae%2Feducation%2Fuae-universities-hit-record-qs-rankings-2027-eight-institutions-achieve-all-time-highs-1.500578559"),
 "ecb19": ("European Central Bank: euro reference rates, 19 October 2026 (CAD, AUD)", "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"),
 "su": ("Stockholm University: ranked 167 in the QS ranking (22 June 2026)", "https://www.su.se/english/news/articles/2026-06-22-stockholm-university-ranks-167-in-the-qs-ranking"),
}
ORDER = list(SRC)

def cite(text):
    return re.sub(r"\[(\w+)\]", lambda m: f'<sup><a href="#src-{m.group(1)}">[{ORDER.index(m.group(1)) + 1}]</a></sup>' if m.group(1) in SRC else m.group(0), text)

# QS World University Rankings 2027 ("=" means a tie). None = outside the top 100 (not on the QS top-100 list).
QS = [
 ("MIT", "USA", "1"), ("Imperial College London", "UK", "=2"), ("Stanford University", "USA", "=2"),
 ("University of Oxford", "UK", "4"), ("University of Cambridge", "UK", "6"), ("UCL", "UK", "=8"),
 ("Technical University of Munich (TUM)", "Germany", "25"), ("University of Edinburgh", "UK", "35"),
 ("King's College London", "UK", "37"), ("University of Manchester", "UK", "=40"), ("Carnegie Mellon University", "USA", "55"),
 ("University of Bristol", "UK", "57"), ("LMU Munich", "Germany", "61"), ("LSE", "UK", "62"),
 ("University of Warwick", "UK", "=68"), ("University of Birmingham", "UK", "=68"), ("Lund University", "Sweden", "71"),
 ("University of Illinois Urbana-Champaign", "USA", "74"), ("University of Leeds", "UK", "=77"), ("University of Glasgow", "UK", "80"),
 ("University of Sheffield", "UK", "=82"), ("KTH Royal Institute of Technology", "Sweden", "=82"), ("Durham University", "UK", "85"),
 ("Heidelberg University", "Germany", "86"), ("Uppsala University", "Sweden", "=87"), ("University of Nottingham", "UK", "=97"),
 ("Purdue University", "USA", "=100"), ("Stockholm University", "Sweden", "167 [su]"),
 ("UNSW Sydney", "Australia", "19"), ("University of Melbourne", "Australia", "=22"), ("University of Sydney", "Australia", "28"),
 ("Australian National University", "Australia", "29"), ("McGill University", "Canada", "30"), ("Monash University", "Australia", "31"),
 ("University of Toronto", "Canada", "32"), ("University of British Columbia", "Canada", "=45"), ("University of Alberta", "Canada", "96"),
 ("Khalifa University", "UAE", "147 [uae_qs]"), ("United Arab Emirates University", "UAE", "217 [uae_qs]"), ("American University of Sharjah", "UAE", "258 [uae_qs]"),
]
QS_OUT = "University of Southampton, Queen Mary University of London, Newcastle University, Coventry University, RWTH Aachen, TU Berlin, Chalmers, University of Waterloo"

def sections(lang):
    m = M(lang); E = lang == "en"
    S = []
    # ---------------- 1. Application ----------------
    S.append(("apply", "Applying: fees and visas" if E else "আবেদন: ফি আর ভিসা", [
     ("How much does it cost to apply to a university?" if E else "বিশ্ববিদ্যালয়ে আবেদন করতে কত খরচ?",
      (f"It depends on the country and often on the course. Examples for 2027 entry (master's unless stated): "
       f"<ul><li><b>UK:</b> Oxford {m(75,'£')} for taught courses; UCL {m(90,'£')}; LSE {m(95,'£')}; Warwick {m(75,'£')}; Imperial {m(90,'£')} ({m(125,'£')} for Business School MSc). "
       f"Several universities charge nothing, e.g. Birmingham (taught), Leeds, Newcastle, Coventry. Undergraduate applications go through UCAS: {m(34.5,'£')}.</li>"
       f"<li><b>Germany:</b> most public universities charge nothing; applications through uni-assist cost {m(75,'€')} for the first and {m(30,'€')} for each extra one.</li>"
       f"<li><b>Sweden:</b> {m(900,'SEK')} once per round on universityadmissions.se (up to several programmes).</li>"
       f"<li><b>USA:</b> set per programme, e.g. UIUC {m(90,'$')}, Purdue {m(75,'$')}, Stanford Graduate School of Education {m(125,'$')}. Waivers for international applicants are rare.</li></ul>"
       f"Every figure, with its official link, is in the <a href=\"/universities/\">University finder</a>.")
      if E else
      (f"দেশ আর অনেক সময় কোর্সের ওপর নির্ভর করে। ২০২৭ ভর্তির কিছু উদাহরণ (আলাদা করে না বললে মাস্টার্স): "
       f"<ul><li><b>UK:</b> Oxford-এ taught কোর্সে {m(75,'£')}; UCL {m(90,'£')}; LSE {m(95,'£')}; Warwick {m(75,'£')}; Imperial {m(90,'£')} (Business School MSc-তে {m(125,'£')})। "
       f"অনেক বিশ্ববিদ্যালয় কোনো ফি নেয় না, যেমন Birmingham (taught), Leeds, Newcastle, Coventry। আন্ডারগ্র্যাজুয়েট আবেদন হয় UCAS দিয়ে: {m(34.5,'£')}।</li>"
       f"<li><b>জার্মানি:</b> বেশিরভাগ সরকারি বিশ্ববিদ্যালয় ফি নেয় না; uni-assist দিয়ে আবেদন করলে প্রথমটায় {m(75,'€')}, পরের প্রতিটায় {m(30,'€')}।</li>"
       f"<li><b>সুইডেন:</b> universityadmissions.se-তে প্রতি রাউন্ডে একবার {m(900,'SEK')} (কয়েকটা প্রোগ্রাম একসঙ্গে)।</li>"
       f"<li><b>USA:</b> প্রতিটা প্রোগ্রাম আলাদা ঠিক করে, যেমন UIUC {m(90,'$')}, Purdue {m(75,'$')}, Stanford Graduate School of Education {m(125,'$')}। বিদেশি আবেদনকারীদের ফি মকুব খুব কম হয়।</li></ul>"
       f"প্রতিটা অঙ্ক অফিসিয়াল লিংক-সহ পাবেন <a href=\"/bn/universities/\">বিশ্ববিদ্যালয় খোঁজার পাতায়</a>।")),
     ("How much does the student visa cost?" if E else "স্টুডেন্ট ভিসার খরচ কত?",
      (f"<ul><li><b>UK:</b> {m(558,'£')} from outside the UK [uk_visa], plus the Immigration Health Surcharge of {m(776,'£')} per year of visa (half for any part-year under 6 months) [uk_ihs]. A one-year master's visa usually runs about 16 months, so expect roughly {m(1164,'£')} surcharge. You can apply up to 6 months before the course starts [uk_visa].</li>"
       f"<li><b>USA:</b> visa (MRV) fee {m(185,'$')} + SEVIS I-901 fee {m(350,'$')}; some consulates have started charging a {m(250,'$')} visa integrity fee on issue [us_fees].</li>"
       f"<li><b>Canada:</b> study permit {m(235,'CAD')} including biometrics [ca_rules].</li>"
       f"<li><b>Australia:</b> {m(2500,'AUD')} for the main applicant from 1 July 2026 [au_visa].</li>"
       f"<li><b>UAE:</b> student residence permit about {m(2500,'AED')} plus {m(500,'AED')}, arranged through the university [uae_visa].</li>"
       f"<li><b>Germany:</b> national visa about {m(75,'€')} [de_ins].</li>"
       f"<li><b>Sweden:</b> pay the fee shown by Migrationsverket when you apply online.</li></ul>")
      if E else
      (f"<ul><li><b>UK:</b> UK-র বাইরে থেকে {m(558,'£')} [uk_visa], সঙ্গে Immigration Health Surcharge, ভিসার প্রতি বছরের জন্য {m(776,'£')} (৬ মাসের কম অংশের জন্য অর্ধেক) [uk_ihs]। এক বছরের মাস্টার্সের ভিসা সাধারণত প্রায় ১৬ মাসের হয়, তাই surcharge মোটামুটি {m(1164,'£')}। কোর্স শুরুর ৬ মাস আগে থেকে আবেদন করা যায় [uk_visa]।</li>"
       f"<li><b>USA:</b> ভিসা (MRV) ফি {m(185,'$')} + SEVIS I-901 ফি {m(350,'$')}; কিছু কনস্যুলেট ভিসা দেওয়ার সময় {m(250,'$')} visa integrity fee নিতে শুরু করেছে [us_fees]।</li>"
       f"<li><b>কানাডা:</b> study permit {m(235,'CAD')}, বায়োমেট্রিক-সহ [ca_rules]।</li>"
       f"<li><b>অস্ট্রেলিয়া:</b> ১ জুলাই ২০২৬ থেকে মূল আবেদনকারীর {m(2500,'AUD')} [au_visa]।</li>"
       f"<li><b>UAE:</b> student residence permit মোটামুটি {m(2500,'AED')} আর {m(500,'AED')}, বিশ্ববিদ্যালয়ের মাধ্যমে [uae_visa]।</li>"
       f"<li><b>জার্মানি:</b> ন্যাশনাল ভিসা মোটামুটি {m(75,'€')} [de_ins]।</li>"
       f"<li><b>সুইডেন:</b> অনলাইনে আবেদনের সময় Migrationsverket যে ফি দেখায়, সেটাই দিতে হয়।</li></ul>")),
     ("How much money must we show for the visa?" if E else "ভিসার জন্য ব্যাংকে কত টাকা দেখাতে হয়?",
      (f"<ul><li><b>UK:</b> the first year's tuition still owed, plus living costs of {m(1529,'£','/month')} in London or {m(1171,'£','/month')} elsewhere, for up to 9 months (maximum {m(13761,'£')} London / {m(10539,'£')} elsewhere). The money must sit in the account for 28 days in a row, ending no more than 31 days before you apply [uk_money].</li>"
       f"<li><b>Germany:</b> usually a blocked account of {m(11904,'€','/year')}, i.e. {m(992,'€','/month')} for 2026 [de_block].</li>"
       f"<li><b>Sweden:</b> at least {m(10656,'SEK','/month')} for the whole permit (2026 applications) [se_money].</li>"
       f"<li><b>USA:</b> the full first-year cost on your I-20, set by the university (see the UIUC example below).</li>"
       f"<li><b>Canada:</b> first-year tuition and travel, plus {m(23448,'CAD','/year')} living costs for a single student outside Quebec (applications from 1 September 2026) [ca_funds].</li>"
       f"<li><b>Australia:</b> {m(29710,'AUD','/year')} living costs, plus travel and first-year tuition [au_visa].</li></ul>")
      if E else
      (f"<ul><li><b>UK:</b> প্রথম বছরের বাকি টিউশন ফি, সঙ্গে থাকার খরচ: লন্ডনে {m(1529,'£','/মাস')}, অন্যত্র {m(1171,'£','/মাস')}, সর্বোচ্চ ৯ মাস (লন্ডনে সর্বোচ্চ {m(13761,'£')}, অন্যত্র {m(10539,'£')})। টাকাটা টানা ২৮ দিন অ্যাকাউন্টে থাকতে হবে, আর সেই সময় আবেদনের ৩১ দিনের মধ্যে শেষ হতে হবে [uk_money]।</li>"
       f"<li><b>জার্মানি:</b> সাধারণত blocked account-এ {m(11904,'€','/বছর')}, মানে ২০২৬-এ {m(992,'€','/মাস')} [de_block]।</li>"
       f"<li><b>সুইডেন:</b> পুরো পারমিটের মেয়াদের জন্য অন্তত {m(10656,'SEK','/মাস')} (২০২৬-এর আবেদন) [se_money]।</li>"
       f"<li><b>USA:</b> I-20-তে বিশ্ববিদ্যালয় প্রথম বছরের যে পুরো খরচ লেখে, সেটা (নিচে UIUC-র উদাহরণ দেখুন)।</li>"
       f"<li><b>কানাডা:</b> প্রথম বছরের টিউশন আর যাতায়াত, সঙ্গে কুইবেকের বাইরে একা ছাত্রের থাকার খরচ {m(23448,'CAD','/বছর')} (১ সেপ্টেম্বর ২০২৬ থেকে আবেদনে) [ca_funds]।</li>"
       f"<li><b>অস্ট্রেলিয়া:</b> থাকার খরচ {m(29710,'AUD','/বছর')}, সঙ্গে যাতায়াত আর প্রথম বছরের টিউশন [au_visa]।</li></ul>")),
    ]))
    # ---------------- 2. Costs ----------------
    S.append(("costs", "Costs: tuition, rent and monthly expenses" if E else "খরচ: টিউশন, ভাড়া আর মাসিক খরচ", [
     ("How much does it cost per month to live there?" if E else "সেখানে থাকতে মাসে কত খরচ?",
      (f"The visa figures above are the official minimums, and a good guide to a modest student budget:"
       f"<ul><li><b>UK:</b> {m(1529,'£')} London / {m(1171,'£')} elsewhere [uk_money].</li>"
       f"<li><b>Germany:</b> {m(992,'€')} [de_block]. Public health insurance for students under 30 is roughly {m(140,'€')}–{m(160,'€')} of that [de_ins].</li>"
       f"<li><b>Sweden:</b> Uppsala University's sample budget is {m(9500,'SEK')}–{m(11600,'SEK')}: housing {m(4000,'SEK')}–{m(6500,'SEK')}, food {m(3400,'SEK')}, transport {m(500,'SEK')}, phone {m(300,'SEK')} [se_budget].</li>"
       f"<li><b>USA:</b> UIUC estimates room and board at {m(19253,'$')} for 12 months (about {m(1604,'$','/month')}) [us_cost]. Big coastal cities cost more.</li>"
       f"<li><b>Canada:</b> the visa minimum works out at about {m(1954,'CAD','/month')} [ca_funds].</li>"
       f"<li><b>Australia:</b> the visa minimum works out at about {m(2476,'AUD','/month')} [au_visa].</li></ul>")
      if E else
      (f"ওপরের ভিসার অঙ্কগুলো সরকারি ন্যূনতম, আর সাধারণ ছাত্রের মাসিক বাজেটের ভালো আন্দাজ দেয়:"
       f"<ul><li><b>UK:</b> লন্ডনে {m(1529,'£')}, অন্যত্র {m(1171,'£')} [uk_money]।</li>"
       f"<li><b>জার্মানি:</b> {m(992,'€')} [de_block]। ৩০ বছরের কম বয়সী ছাত্রদের সরকারি হেলথ ইনশিওরেন্স এর মধ্যে মোটামুটি {m(140,'€')}–{m(160,'€')} [de_ins]।</li>"
       f"<li><b>সুইডেন:</b> Uppsala University-র নমুনা বাজেট {m(9500,'SEK')}–{m(11600,'SEK')}: থাকা {m(4000,'SEK')}–{m(6500,'SEK')}, খাওয়া {m(3400,'SEK')}, যাতায়াত {m(500,'SEK')}, ফোন {m(300,'SEK')} [se_budget]।</li>"
       f"<li><b>USA:</b> UIUC-র হিসেবে ১২ মাসের থাকা-খাওয়া {m(19253,'$')} (মাসে প্রায় {m(1604,'$')}) [us_cost]। সমুদ্র-তীরের বড় শহরে খরচ বেশি।</li>"
       f"<li><b>কানাডা:</b> ভিসার ন্যূনতম হিসেবে মাসে প্রায় {m(1954,'CAD')} [ca_funds]।</li>"
       f"<li><b>অস্ট্রেলিয়া:</b> ভিসার ন্যূনতম হিসেবে মাসে প্রায় {m(2476,'AUD')} [au_visa]।</li></ul>")),
     ("How much is rent?" if E else "বাড়িভাড়া কত?",
      (f"<ul><li><b>London:</b> a university-owned en-suite room averaged {m(226,'£','/week')} on a 41-week contract; comparable private halls {m(341,'£','/week')} on 50 weeks (2024 survey) [uk_rent]. Outside London rents are usually much lower — check each university's accommodation page.</li>"
       f"<li><b>Germany</b> (shared-flat room, 2025): average {m(505,'€','/month')}; Munich {m(790,'€')}, Heidelberg {m(633,'€')}, Berlin {m(624,'€')}, Aachen {m(483,'€')} [de_rent].</li>"
       f"<li><b>Sweden:</b> {m(4000,'SEK')}–{m(6500,'SEK','/month')} in Uppsala's sample budget [se_budget]. Housing queues in Stockholm and Uppsala are long — apply as soon as you get an offer.</li></ul>"
       f"Tip: ask a current student on the university's official chat page which areas are safe and affordable.")
      if E else
      (f"<ul><li><b>লন্ডন:</b> বিশ্ববিদ্যালয়ের নিজস্ব en-suite ঘরের গড় ভাড়া {m(226,'£','/সপ্তাহ')}, ৪১ সপ্তাহের চুক্তি; বেসরকারি একই রকম ঘর {m(341,'£','/সপ্তাহ')}, ৫০ সপ্তাহ (২০২৪ সমীক্ষা) [uk_rent]। লন্ডনের বাইরে ভাড়া সাধারণত অনেক কম — প্রতিটা বিশ্ববিদ্যালয়ের accommodation পেজ দেখুন।</li>"
       f"<li><b>জার্মানি</b> (শেয়ার্ড ফ্ল্যাটের একটা ঘর, ২০২৫): গড় {m(505,'€','/মাস')}; মিউনিখ {m(790,'€')}, হাইডেলবার্গ {m(633,'€')}, বার্লিন {m(624,'€')}, আখেন {m(483,'€')} [de_rent]।</li>"
       f"<li><b>সুইডেন:</b> Uppsala-র নমুনা বাজেটে মাসে {m(4000,'SEK')}–{m(6500,'SEK')} [se_budget]। স্টকহোম আর উপসালায় হাউজিং-এর লাইন লম্বা — অফার পেলেই আবেদন করুন।</li></ul>"
       f"পরামর্শ: বিশ্ববিদ্যালয়ের অফিসিয়াল chat পেজে কোনো বর্তমান ছাত্রকে জিজ্ঞেস করুন কোন এলাকা নিরাপদ আর সস্তা।")),
     ("What does a full year cost? A worked example" if E else "পুরো এক বছরে কত খরচ? একটা উদাহরণ",
      (f"<b>UK, one-year master's in London</b> (King's College London Physics MSc): tuition {m(38100,'£')} + living {m(13761,'£')} (9 × £1,529) + visa {m(558,'£')} + health surcharge about {m(1164,'£')} = about {m(53583,'£')}, before flights and deposits. "
       f"<br><b>USA, UIUC MS Policy Economics 2026–27:</b> tuition and fees {m(52554,'$')} + living, books and supplies {m(25268,'$')} = {m(77822,'$')}, with a recommended {m(3000,'$')} contingency [us_cost]. "
       f"<br><b>Germany:</b> most public universities charge no tuition, but TUM charges non-EU students {m(4000,'€')}–{m(6000,'€','/semester')} and Heidelberg (Baden-Württemberg) {m(1500,'€','/semester')} plus a semester fee — see the <a href=\"/universities/\">University finder</a>.")
      if E else
      (f"<b>UK, লন্ডনে এক বছরের মাস্টার্স</b> (King's College London Physics MSc): টিউশন {m(38100,'£')} + থাকা-খাওয়া {m(13761,'£')} (৯ × £1,529) + ভিসা {m(558,'£')} + হেলথ সারচার্জ প্রায় {m(1164,'£')} = প্রায় {m(53583,'£')}, বিমানভাড়া আর ডিপোজিট বাদে। "
       f"<br><b>USA, UIUC MS Policy Economics ২০২৬–২৭:</b> টিউশন ও ফি {m(52554,'$')} + থাকা, বই ও অন্যান্য {m(25268,'$')} = {m(77822,'$')}, সঙ্গে {m(3000,'$')} জরুরি তহবিল রাখার পরামর্শ [us_cost]। "
       f"<br><b>জার্মানি:</b> বেশিরভাগ সরকারি বিশ্ববিদ্যালয়ে টিউশন নেই, কিন্তু TUM non-EU ছাত্রদের থেকে {m(4000,'€')}–{m(6000,'€','/সেমেস্টার')} আর Heidelberg (Baden-Württemberg) {m(1500,'€','/সেমেস্টার')} ও সেমেস্টার ফি নেয় — <a href=\"/bn/universities/\">বিশ্ববিদ্যালয় খোঁজার পাতা</a> দেখুন।")),
    ]))
    # ---------------- 3. Scholarships ----------------
    S.append(("scholarships", "Scholarships" if E else "স্কলারশিপ", [
     ("Which big scholarships can students from India and Bangladesh apply for?" if E else "ভারত আর বাংলাদেশের ছাত্ররা কোন বড় স্কলারশিপে আবেদন করতে পারে?",
      (f"<ul><li><b>Commonwealth Master's (UK)</b> — India and Bangladesh are eligible. Covers tuition, flights and a stipend of {m(1712,'£','/month')} ({m(2000,'£')} in London). You apply through a nominating agency in your country; the 2027 deadline is <b>20 October 2026, 16:00 BST</b> [csc].</li>"
       f"<li><b>Chevening (UK)</b> — tuition, monthly allowance, flights and visa fee for a one-year master's. Needs 2,800 hours (about two years) of work experience. The 2027/28 round closed on 6 October 2026; the next opens around August 2027 [chevening].</li>"
       f"<li><b>GREAT Scholarships (UK)</b> — at least {m(10000,'£')} off tuition for a one-year taught master's at named universities (for India 2027–28: Manchester, Manchester Met, Salford, RNCM) [great_in]; Bangladesh has its own list [great_bd].</li>"
       f"<li><b>DAAD (Germany)</b> — about {m(992,'€','/month')} for master's students and {m(1300,'€')}–{m(1400,'€','/month')} for PhD, plus insurance and travel [daad].</li>"
       f"<li><b>Swedish Institute (SISGP)</b> — full tuition, {m(12000,'SEK','/month')}, a {m(15000,'SEK')} travel grant and insurance; India is eligible (check si.se for Bangladesh). Applications usually open in February [si].</li>"
       f"<li><b>Fulbright-Nehru Master's (USA)</b> — for Indians with at least 3 years' work experience in listed fields; mostly fully funded. See usief.org.in [fulbright].</li></ul>"
       f"Many universities also offer their own awards, e.g. Newcastle {m(10000,'£')} and Sheffield {m(7000,'£')} for Indian students, QMUL {m(8000,'£')} — see the University finder.")
      if E else
      (f"<ul><li><b>Commonwealth Master's (UK)</b> — ভারত আর বাংলাদেশ দুটোই যোগ্য। টিউশন, বিমানভাড়া আর মাসে {m(1712,'£')} (লন্ডনে {m(2000,'£')}) ভাতা। নিজের দেশের nominating agency-র মাধ্যমে আবেদন; ২০২৭-এর শেষ তারিখ <b>২০ অক্টোবর ২০২৬, বিকেল ৪টে (BST)</b> [csc]।</li>"
       f"<li><b>Chevening (UK)</b> — এক বছরের মাস্টার্সের টিউশন, মাসিক ভাতা, বিমানভাড়া আর ভিসা ফি। ২,৮০০ ঘণ্টা (প্রায় দু-বছর) কাজের অভিজ্ঞতা লাগে। ২০২৭/২৮ রাউন্ড ৬ অক্টোবর ২০২৬-এ বন্ধ হয়েছে; পরেরটা খুলবে মোটামুটি আগস্ট ২০২৭-এ [chevening]।</li>"
       f"<li><b>GREAT Scholarships (UK)</b> — নির্দিষ্ট বিশ্ববিদ্যালয়ে এক বছরের taught মাস্টার্সে অন্তত {m(10000,'£')} টিউশন ছাড় (ভারতের জন্য ২০২৭–২৮: Manchester, Manchester Met, Salford, RNCM) [great_in]; বাংলাদেশের আলাদা তালিকা আছে [great_bd]।</li>"
       f"<li><b>DAAD (জার্মানি)</b> — মাস্টার্সে মাসে প্রায় {m(992,'€')}, PhD-তে {m(1300,'€')}–{m(1400,'€')}, সঙ্গে ইনশিওরেন্স আর যাতায়াত [daad]।</li>"
       f"<li><b>Swedish Institute (SISGP)</b> — পুরো টিউশন, মাসে {m(12000,'SEK')}, {m(15000,'SEK')} ট্রাভেল গ্রান্ট আর ইনশিওরেন্স; ভারত যোগ্য (বাংলাদেশের জন্য si.se দেখুন)। সাধারণত ফেব্রুয়ারিতে আবেদন খোলে [si]।</li>"
       f"<li><b>Fulbright-Nehru Master's (USA)</b> — নির্দিষ্ট বিষয়ে অন্তত ৩ বছর কাজের অভিজ্ঞতা থাকা ভারতীয়দের জন্য; প্রায় পুরো খরচ দেয়। usief.org.in দেখুন [fulbright]।</li></ul>"
       f"অনেক বিশ্ববিদ্যালয় নিজেরাও স্কলারশিপ দেয়, যেমন ভারতীয় ছাত্রদের জন্য Newcastle {m(10000,'£')} আর Sheffield {m(7000,'£')}, QMUL {m(8000,'£')} — বিশ্ববিদ্যালয় খোঁজার পাতা দেখুন।")),
     ("Should we pay an agent to get a scholarship?" if E else "স্কলারশিপের জন্য কি এজেন্টকে টাকা দেওয়া উচিত?",
      ("No. All the scholarships above are applied for directly, for free, on their official websites. Be careful of anyone who promises a guaranteed scholarship or visa for a fee."
       if E else
       "না। ওপরের সব স্কলারশিপে সরাসরি, বিনা পয়সায়, অফিসিয়াল ওয়েবসাইটে আবেদন করা যায়। টাকার বদলে নিশ্চিত স্কলারশিপ বা ভিসার প্রতিশ্রুতি যে দেয়, তার থেকে সাবধান।")),
    ]))
    # ---------------- 4. Jobs ----------------
    S.append(("jobs", "Working during and after your studies" if E else "পড়ার সময় আর পরে কাজ", [
     ("Can I work part-time while studying?" if E else "পড়ার সময় কি পার্ট-টাইম কাজ করা যায়?",
      (f"<ul><li><b>UK:</b> up to 20 hours a week in term time on a degree-level course; full time in official vacations [uk_work].</li>"
       f"<li><b>Germany:</b> 140 full days or 280 half days a year, or up to 20 hours a week in the lecture period; student-assistant jobs at the university are not limited [de_work].</li>"
       f"<li><b>Sweden:</b> new rule — for bachelor's and master's permits granted from 11 June 2026, up to 15 hours a week during semesters; no limit in June, July and August [se_money].</li>"
       f"<li><b>USA (F-1):</b> on-campus jobs only, up to 20 hours a week in term and full time in vacations [us_work].</li>"
       f"<li><b>Canada:</b> up to 24 hours a week off campus during term [ca_rules].</li>"
       f"<li><b>Australia:</b> 48 hours a fortnight during term, unlimited in scheduled breaks; no limit for research master's and PhD [au_visa].</li>"
       f"<li><b>UAE:</b> on- or off-campus work needs the university's permission and a work permit [uae_visa].</li></ul>"
       f"Do not plan to pay tuition from part-time work: the visa needs the money in the bank before you go.")
      if E else
      (f"<ul><li><b>UK:</b> ডিগ্রি-স্তরের কোর্সে টার্মের সময় সপ্তাহে সর্বোচ্চ ২০ ঘণ্টা; অফিসিয়াল ছুটিতে ফুল-টাইম [uk_work]।</li>"
       f"<li><b>জার্মানি:</b> বছরে ১৪০ পুরো দিন বা ২৮০ অর্ধেক দিন, অথবা ক্লাস চলার সময় সপ্তাহে সর্বোচ্চ ২০ ঘণ্টা; বিশ্ববিদ্যালয়ের student-assistant কাজে সীমা নেই [de_work]।</li>"
       f"<li><b>সুইডেন:</b> নতুন নিয়ম — ১১ জুন ২০২৬ থেকে দেওয়া ব্যাচেলর/মাস্টার্স পারমিটে সেমেস্টারে সপ্তাহে সর্বোচ্চ ১৫ ঘণ্টা; জুন, জুলাই, আগস্টে সীমা নেই [se_money]।</li>"
       f"<li><b>USA (F-1):</b> শুধু ক্যাম্পাসের ভেতরের কাজ, টার্মে সপ্তাহে সর্বোচ্চ ২০ ঘণ্টা, ছুটিতে ফুল-টাইম [us_work]।</li>"
       f"<li><b>কানাডা:</b> টার্মে ক্যাম্পাসের বাইরে সপ্তাহে সর্বোচ্চ ২৪ ঘণ্টা [ca_rules]।</li>"
       f"<li><b>অস্ট্রেলিয়া:</b> টার্মে দু-সপ্তাহে ৪৮ ঘণ্টা, ছুটিতে সীমা নেই; রিসার্চ মাস্টার্স আর PhD-তে সীমা নেই [au_visa]।</li>"
       f"<li><b>UAE:</b> ক্যাম্পাসে বা বাইরে কাজের জন্য বিশ্ববিদ্যালয়ের অনুমতি আর ওয়ার্ক পারমিট লাগে [uae_visa]।</li></ul>"
       f"পার্ট-টাইম কাজ করে টিউশন দেওয়ার পরিকল্পনা করবেন না: ভিসার জন্য যাওয়ার আগেই টাকা ব্যাংকে থাকতে হয়।")),
     ("Can I stay and work after I graduate?" if E else "পাস করার পর কি থেকে কাজ করা যায়?",
      (f"<ul><li><b>UK Graduate visa:</b> 2 years if you apply by 31 December 2026; <b>18 months</b> for bachelor's and master's graduates applying from 1 January 2027; 3 years for PhD graduates [uk_work]. In the year to June 2026, 157,356 Graduate-route extensions were granted [uk_stats].</li>"
       f"<li><b>Germany:</b> up to 18 months to look for a job after graduating [de_work].</li>"
       f"<li><b>Sweden:</b> up to 1 year to look for work (12–18 months after a PhD), if you can support yourself on {m(10656,'SEK','/month')} [se_job].</li>"
       f"<li><b>USA:</b> 12 months of OPT, plus 24 more months (STEM OPT) for STEM degrees with an E-Verify employer [us_work].</li>"
       f"<li><b>Canada:</b> Post-Graduation Work Permit of up to 3 years; master's graduates get 3 years if the programme lasted at least 8 months [ca_rules].</li>"
       f"<li><b>Australia:</b> Temporary Graduate visa (485) — 2 years after a bachelor's or coursework master's, 3 years after a research master's or PhD [au_485].</li>"
       f"<li><b>UAE:</b> no general post-study visa, but top graduates (GPA 3.5+ from an A-rated university, within two years of graduating) can get a 10-year residence visa [uae_visa].</li></ul>")
      if E else
      (f"<ul><li><b>UK Graduate visa:</b> ৩১ ডিসেম্বর ২০২৬-এর মধ্যে আবেদন করলে ২ বছর; ১ জানুয়ারি ২০২৭ থেকে ব্যাচেলর আর মাস্টার্সের জন্য <b>১৮ মাস</b>; PhD-র জন্য ৩ বছর [uk_work]। জুন ২০২৬ পর্যন্ত এক বছরে ১,৫৭,৩৫৬টি Graduate-route এক্সটেনশন দেওয়া হয়েছে [uk_stats]।</li>"
       f"<li><b>জার্মানি:</b> পাস করার পর চাকরি খোঁজার জন্য সর্বোচ্চ ১৮ মাস [de_work]।</li>"
       f"<li><b>সুইডেন:</b> কাজ খোঁজার জন্য সর্বোচ্চ ১ বছর (PhD-র পর ১২–১৮ মাস), যদি মাসে {m(10656,'SEK')} দিয়ে নিজের খরচ চালাতে পারেন [se_job]।</li>"
       f"<li><b>USA:</b> ১২ মাস OPT, আর STEM ডিগ্রি হলে E-Verify নিয়োগকর্তার সঙ্গে আরও ২৪ মাস (STEM OPT) [us_work]।</li>"
       f"<li><b>কানাডা:</b> সর্বোচ্চ ৩ বছরের Post-Graduation Work Permit; প্রোগ্রাম অন্তত ৮ মাসের হলে মাস্টার্সে ৩ বছর [ca_rules]।</li>"
       f"<li><b>অস্ট্রেলিয়া:</b> Temporary Graduate visa (485) — ব্যাচেলর বা কোর্সওয়ার্ক মাস্টার্সের পর ২ বছর, রিসার্চ মাস্টার্স বা PhD-র পর ৩ বছর [au_485]।</li>"
       f"<li><b>UAE:</b> সাধারণ পোস্ট-স্টাডি ভিসা নেই, তবে সেরা গ্র্যাজুয়েটরা (A-rated বিশ্ববিদ্যালয় থেকে GPA 3.5+, পাসের দু-বছরের মধ্যে) ১০ বছরের রেসিডেন্স ভিসা পেতে পারেন [uae_visa]।</li></ul>")),
    ]))
    # ---------------- 5. Rankings & statistics ----------------
    S.append(("rankings", "QS World Rankings and student statistics" if E else "QS ওয়ার্ল্ড র‍্যাংকিং আর ছাত্রদের পরিসংখ্যান", [
     ("Where do the universities on BiswaPath rank in the QS World University Rankings 2027?" if E else "BiswaPath-এর বিশ্ববিদ্যালয়গুলো QS World University Rankings 2027-এ কোথায়?",
      "QSTABLE"),
     ("How much should rankings matter?" if E else "র‍্যাংকিং কতটা গুরুত্ব দেওয়া উচিত?",
      ("Rankings measure the whole university, mostly research reputation. For your choice, the course content, the department's strength in your subject, total cost, location and job outcomes matter more. A university ranked 150 can be better for your subject than one ranked 30."
       if E else
       "র‍্যাংকিং পুরো বিশ্ববিদ্যালয়কে মাপে, বেশিটাই গবেষণার সুনাম। আপনার সিদ্ধান্তে কোর্সের বিষয়বস্তু, আপনার বিষয়ে বিভাগটা কত ভালো, মোট খরচ, জায়গা আর চাকরির সুযোগ বেশি জরুরি। ১৫০ নম্বরে থাকা বিশ্ববিদ্যালয় আপনার বিষয়ে ৩০ নম্বরের চেয়ে ভালো হতেই পারে।")),
     ("How many Indian students study abroad, and where?" if E else "কতজন ভারতীয় ছাত্র বিদেশে পড়ে, আর কোথায়?",
      ("<ul><li><b>12.54 lakh</b> Indian students were at universities or other tertiary institutions abroad on 1 January 2025, according to India's Ministry of External Affairs. Its headline total of 18.82 lakh also counts 6.28 lakh school pupils. Largest university-level destinations: Canada 4.27 lakh, USA 2.55 lakh, UK 1.73 lakh, Australia 1.39 lakh [mea].</li>"
       "<li><b>USA (2024/25):</b> Open Doors counts 363,019 Indian students — 219,279 enrolled plus 143,740 graduates on OPT work permits [us_stats].</li>"
       "<li><b>UK:</b> 82,523 study <i>visas</i> went to Indian main applicants in the year to June 2026 — a count of visas granted, not of students in the UK [uk_stats].</li>"
       "<li><b>Germany:</b> about 69,000 international students from India in winter semester 2025/26, the largest group [de_stats].</li></ul>"
       "These measures differ, so do not add them up. Details, Bangladesh and subjects: <a href=\"/statistics/\">Students abroad: the numbers</a>.")
      if E else
      ("<ul><li>ভারতের বিদেশ মন্ত্রকের হিসেবে ১ জানুয়ারি ২০২৫-এ <b>১২.৫৪ লাখ</b> ভারতীয় ছাত্রছাত্রী বিদেশের বিশ্ববিদ্যালয় বা অন্য উচ্চশিক্ষা প্রতিষ্ঠানে ছিল। তাদের মোট ১৮.৮২ লাখের মধ্যে ৬.২৮ লাখ স্কুলের ছাত্রছাত্রী। বিশ্ববিদ্যালয়-স্তরে বড় গন্তব্য: কানাডা ৪.২৭ লাখ, USA ২.৫৫ লাখ, UK ১.৭৩ লাখ, অস্ট্রেলিয়া ১.৩৯ লাখ [mea]।</li>"
       "<li><b>USA (২০২৪/২৫):</b> Open Doors-এর হিসেবে ৩,৬৩,০১৯ জন ভারতীয় — ভর্তি ২,১৯,২৭৯, আর OPT ওয়ার্ক পারমিটে ১,৪৩,৭৪০ জন গ্র্যাজুয়েট [us_stats]।</li>"
       "<li><b>UK:</b> জুন ২০২৬ পর্যন্ত এক বছরে ভারতীয় মূল আবেদনকারীরা ৮২,৫২৩টি স্টাডি <i>ভিসা</i> পেয়েছেন — এটা দেওয়া ভিসার সংখ্যা, UK-তে থাকা ছাত্রের নয় [uk_stats]।</li>"
       "<li><b>জার্মানি:</b> শীতকালীন সেমেস্টার ২০২৫/২৬-এ ভারত থেকে প্রায় ৬৯,০০০ আন্তর্জাতিক ছাত্র, সবচেয়ে বড় দল [de_stats]।</li></ul>"
       "মাপগুলো আলাদা, তাই যোগ করবেন না। বিস্তারিত, বাংলাদেশ আর বিষয়ভিত্তিক তথ্য: <a href=\"/bn/statistics/\">বিদেশে ছাত্রছাত্রী: সংখ্যার হিসেব</a>।")),
     ("What about Singapore, Japan, China and Russia?" if E else "সিঙ্গাপুর, জাপান, চীন আর রাশিয়া?",
      ("At university level, few Indians go to these countries, for different reasons (MEA, 1 January 2025): Russia about 27,000, mostly for MBBS; China about 5,300, down after Covid visa bans; Singapore about 3,250, because places at NUS and NTU are few and competitive; Japan about 1,500, where language is the main barrier. Singapore and the UAE also have many Indian <i>school</i> pupils, which inflates their totals [mea]. Details and sources: <a href=\"/statistics/#other\">Students abroad: the numbers</a>."
       if E else
       "বিশ্ববিদ্যালয়-স্তরে এই দেশগুলোতে ভারতীয় কম যায়, আলাদা আলাদা কারণে (MEA, ১ জানুয়ারি ২০২৫): রাশিয়ায় প্রায় ২৭,০০০, বেশিরভাগ MBBS; চীনে প্রায় ৫,৩০০, কোভিডের ভিসা নিষেধাজ্ঞার পর কমেছে; সিঙ্গাপুরে প্রায় ৩,২৫০, কারণ NUS আর NTU-তে আসন কম আর ভর্তি কঠিন; জাপানে প্রায় ১,৫০০, মূল বাধা ভাষা। সিঙ্গাপুর আর UAE-তে অনেক ভারতীয় <i>স্কুল</i>-ছাত্রও আছে, তাই তাদের মোট সংখ্যা বড় দেখায় [mea]। বিস্তারিত আর সূত্র: <a href=\"/bn/statistics/#other\">বিদেশে ছাত্রছাত্রী: সংখ্যার হিসেব</a>।")),
]))
    # ---------------- 6. Safety ----------------
    S.append(("safety", "Safety" if E else "নিরাপত্তা", [
     ("What should my child do in an emergency?" if E else "জরুরি অবস্থায় আমার ছেলে/মেয়ে কী করবে?",
      ("<ul><li>Emergency numbers: <b>UK 999</b> (or 112; NHS non-emergency 111), <b>Germany 112</b> (police 110), <b>Sweden 112</b>, <b>USA and Canada 911</b>, <b>Australia 000</b>, <b>UAE 999</b> (police; ambulance 998).</li>"
       "<li>Save the university's 24-hour security number and the international student office's email on the first day.</li>"
       "<li>Indian students: register on the government's <a href=\"https://www.madad.gov.in/madad/StudentRegistration\" target=\"_blank\" rel=\"noopener\">MADAD portal</a> so the nearest Indian embassy or consulate can reach you [madad]. Bangladeshi students: note the contact details of your Bangladesh High Commission or Embassy.</li></ul>")
      if E else
      ("<ul><li>জরুরি নম্বর: <b>UK 999</b> (বা 112; NHS-এর জরুরি নয় এমন দরকারে 111), <b>জার্মানি 112</b> (পুলিশ 110), <b>সুইডেন 112</b>, <b>USA আর কানাডা 911</b>, <b>অস্ট্রেলিয়া 000</b>, <b>UAE 999</b> (পুলিশ; অ্যাম্বুলেন্স 998)।</li>"
       "<li>প্রথম দিনেই বিশ্ববিদ্যালয়ের ২৪ ঘণ্টার security নম্বর আর international student office-এর ইমেল ফোনে সেভ করে রাখুন।</li>"
       "<li>ভারতীয় ছাত্ররা সরকারের <a href=\"https://www.madad.gov.in/madad/StudentRegistration\" target=\"_blank\" rel=\"noopener\">MADAD পোর্টালে</a> নাম নথিভুক্ত করুন, যাতে নিকটতম ভারতীয় দূতাবাস বা কনস্যুলেট যোগাযোগ করতে পারে [madad]। বাংলাদেশি ছাত্ররা নিজেদের হাই কমিশন বা দূতাবাসের যোগাযোগের তথ্য রেখে দিন।</li></ul>")),
     ("How do we avoid scams?" if E else "প্রতারণা থেকে কীভাবে বাঁচব?",
      ("<ul><li>Pay visa fees only on the official government site (GOV.UK, the US State Department, German missions, Migrationsverket).</li>"
       "<li>Police and immigration officials do not ask for money over the phone. Hang up and call the official number yourself.</li>"
       "<li>Never pay a rent deposit for a flat you or a trusted person has not seen; prefer university halls in the first year.</li>"
       "<li>Never let anyone use your bank account to move money.</li></ul>")
      if E else
      ("<ul><li>ভিসা ফি শুধু সরকারের অফিসিয়াল সাইটে দিন (GOV.UK, US State Department, জার্মান মিশন, Migrationsverket)।</li>"
       "<li>পুলিশ বা ইমিগ্রেশন অফিসার ফোনে টাকা চায় না। ফোন রেখে নিজে অফিসিয়াল নম্বরে ফোন করুন।</li>"
       "<li>নিজে বা বিশ্বস্ত কেউ না দেখে কোনো ফ্ল্যাটের ভাড়ার ডিপোজিট দেবেন না; প্রথম বছরে বিশ্ববিদ্যালয়ের হল ভালো।</li>"
       "<li>নিজের ব্যাংক অ্যাকাউন্ট দিয়ে কাউকে টাকা পাঠাতে দেবেন না।</li></ul>")),
    ]))
    # ---------------- 7. Community ----------------
    S.append(("community", "Bengali community and support" if E else "বাঙালি কমিউনিটি আর সাহায্য", [
     ("Will there be other Bengalis nearby?" if E else "কাছাকাছি কি অন্য বাঙালিরা থাকবেন?",
      ("Almost certainly. Durga Pujas are held in hundreds of cities worldwide; the <a href=\"https://www.sumitkonar.com\" target=\"_blank\" rel=\"noopener\">Global Puja Parikrama map</a> shows the nearest ones with distances. Most large universities also have Indian, Bangladeshi or Bengali student societies through the students' union, and you can talk to current students through each university's official chat page in our <a href=\"/universities/\">University finder</a>."
       if E else
       "প্রায় নিশ্চিতভাবেই। বিশ্বের শত শত শহরে দুর্গাপুজো হয়; <a href=\"https://www.sumitkonar.com\" target=\"_blank\" rel=\"noopener\">Global Puja Parikrama ম্যাপে</a> দূরত্ব-সহ সবচেয়ে কাছের পুজোগুলো দেখা যায়। বেশিরভাগ বড় বিশ্ববিদ্যালয়ে students' union-এর মাধ্যমে ভারতীয়, বাংলাদেশি বা বাঙালি ছাত্র সংগঠনও থাকে, আর আমাদের <a href=\"/bn/universities/\">বিশ্ববিদ্যালয় খোঁজার পাতায়</a> প্রতিটা বিশ্ববিদ্যালয়ের অফিসিয়াল chat পেজে বর্তমান ছাত্রদের সঙ্গে কথা বলা যায়।")),
     ("Where can we get free, reliable advice?" if E else "বিনা পয়সায় নির্ভরযোগ্য পরামর্শ কোথায় পাব?",
      ("From the university's international admissions team (email them directly), the British Council, DAAD, the Swedish Institute and USIEF/EducationUSA — all free. If you are studying abroad already and would like to help others, <a href=\"/contribute/\">join BiswaPath as a volunteer</a>."
       if E else
       "বিশ্ববিদ্যালয়ের international admissions টিম (সরাসরি ইমেল করুন), British Council, DAAD, Swedish Institute আর USIEF/EducationUSA — সবই বিনা পয়সায়। আপনি যদি এখন বিদেশে পড়েন আর অন্যদের সাহায্য করতে চান, <a href=\"/bn/contribute/\">স্বেচ্ছাসেবক হিসেবে BiswaPath-এ যুক্ত হোন</a>।")),
    ]))
    return S

T = {
 "en": dict(title="Questions students and parents ask",
   desc="Costs, monthly expenses, rent, application and visa fees, scholarships, part-time and graduate jobs, QS rankings, statistics and safety for studying in the UK, Germany, Sweden and the USA — with INR estimates and official sources.",
   intro="Straight answers on money, safety and jobs for studying in the UK, Germany, Sweden, the USA, Canada, Australia and the UAE. Every amount is shown in the local currency with an approximate Indian rupee figure. Click a question to open it.",
   rates="INR estimates use the European Central Bank reference rates of 16 October 2026: £1 ≈ ₹126.6, $1 ≈ ₹95.0, €1 ≈ ₹106.9, 1 SEK ≈ ₹9.59 [ecb]; CAD 1 ≈ ₹67.45 and AUD 1 ≈ ₹66.32 use the rates of 19 October 2026 [ecb19]; AED 1 ≈ ₹25.87 (the dirham is fixed to the US dollar). Your bank's rate will differ, and fees change — always check the official page before paying.",
   jump="Jump to", qs_cols=["University", "Country", "QS 2027 rank"],
   qs_note="“=” means a tie. Not in the QS top 100: " + QS_OUT + ". Source: [qs]",
   src_h="Sources", checked="Last checked",
   note_src="Numbers in square brackets refer to these sources. Where we quote a secondary summary, we say so — check the official page before relying on it."),
 "bn": dict(title="ছাত্র আর অভিভাবকদের প্রশ্ন",
   desc="UK, জার্মানি, সুইডেন আর USA-তে পড়ার খরচ, মাসিক খরচ, বাড়িভাড়া, আবেদন ও ভিসা ফি, স্কলারশিপ, পার্ট-টাইম আর পাস করার পরের চাকরি, QS র‍্যাংকিং, পরিসংখ্যান আর নিরাপত্তা — টাকার আনুমানিক হিসেব আর অফিসিয়াল সূত্র-সহ।",
   intro="UK, জার্মানি, সুইডেন, USA, কানাডা, অস্ট্রেলিয়া আর UAE-তে পড়তে যাওয়ার টাকা, নিরাপত্তা আর চাকরি নিয়ে সোজা উত্তর। প্রতিটা অঙ্ক সেই দেশের মুদ্রায়, সঙ্গে ভারতীয় টাকায় আনুমানিক হিসেব। প্রশ্নে ক্লিক করলে উত্তর খুলবে।",
   rates="টাকার হিসেব European Central Bank-এর ১৬ অক্টোবর ২০২৬-এর রেট ধরে: £1 ≈ ₹126.6, $1 ≈ ₹95.0, €1 ≈ ₹106.9, 1 SEK ≈ ₹9.59 [ecb]; CAD 1 ≈ ₹67.45 আর AUD 1 ≈ ₹66.32 ১৯ অক্টোবর ২০২৬-এর রেট ধরে [ecb19]; AED 1 ≈ ₹25.87 (দিরহাম US ডলারের সঙ্গে বাঁধা)। আপনার ব্যাংকের রেট আলাদা হবে, আর ফি বদলায় — টাকা দেওয়ার আগে অফিসিয়াল পেজ অবশ্যই দেখুন।",
   jump="সরাসরি যান", qs_cols=["বিশ্ববিদ্যালয়", "দেশ", "QS 2027 র‍্যাংক"],
   qs_note="“=” মানে সমান স্থান। QS-এর প্রথম ১০০-য় নেই: " + QS_OUT + "। সূত্র: [qs]",
   src_h="সূত্র", checked="শেষ যাচাই",
   note_src="বন্ধনীর সংখ্যাগুলো এই সূত্রগুলো বোঝায়। কোথাও অন্যের সারাংশ উদ্ধৃত করলে সেটা বলে দিয়েছি — ভরসা করার আগে অফিসিয়াল পেজ দেখুন।"),
}
CTRY_BN = {"UK": "UK", "USA": "USA", "Germany": "জার্মানি", "Sweden": "সুইডেন", "Canada": "কানাডা", "Australia": "অস্ট্রেলিয়া", "UAE": "UAE"}

def qs_table(lang):
    t = T[lang]; c = t["qs_cols"]
    rows = "".join(f'<tr><th scope="row">{n}</th><td data-label="{c[1]}">{k if lang=="en" else CTRY_BN[k]}</td><td data-label="{c[2]}">{cite(r)}</td></tr>' for n, k, r in sorted(QS, key=lambda x: int(re.match(r"=?(\d+)", x[2]).group(1))))
    head = "".join(f'<th scope="col">{x}</th>' for x in c)
    return (f'<div class="tablewrap stack"><table class="cmp"><caption>QS World University Rankings 2027</caption>'
            f'<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div><p class="updated">{cite(t["qs_note"])}</p>')

def content(lang):
    t = T[lang]; ck = CHECKED[lang]
    secs = sections(lang)
    jump = " · ".join(f'<a href="#{sid}">{h}</a>' for sid, h, _ in secs)
    out = f'<p>{t["intro"]}</p><div class="invite"><p>{cite(t["rates"])}</p></div><p class="jump"><b>{t["jump"]}:</b> {jump}</p>'
    for sid, h, qa in secs:
        out += f'<h2 id="{sid}">{h}</h2><div class="faq">'
        for q, a in qa:
            body = qs_table(lang) if a == "QSTABLE" else cite(a)
            if "<ul" not in body and "<div" not in body: body = f"<p>{body}</p>"
            out += f'<details><summary>{q}</summary><div class="ans">{body}</div></details>'
        out += "</div>"
    src = "".join(f'<li id="src-{k}"><a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a></li>' for k in ORDER)
    out += f'<h2>{t["src_h"]}</h2><p class="updated">{t["note_src"]}</p><ol class="srcs">{src}</ol><p class="updated">{t["checked"]}: {ck}</p>'
    return t["title"], t["desc"], out
