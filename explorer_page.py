# World Explorer | বিশ্বপাঠ বিশ্বমানচিত্র — embeds the BiswaPath Google My Maps map (imported by build.py).
MID = "1iAQeb6f1nSrqDbnwVxNS8QmyDqzPnHk"
EMBED = f"https://www.google.com/maps/d/embed?mid={MID}"
VIEW = f"https://www.google.com/maps/d/viewer?mid={MID}"

T = {
 "en": dict(
  title="World Explorer | বিশ্বপাঠ বিশ্বমানচিত্র",
  desc="One free map of universities and Bengali communities around the world, for students planning to study abroad.",
  intro="One map for two questions every student asks before going abroad: <em>where could I study?</em> and <em>who will be near me when I get there?</em>",
  open="Open the map in Google Maps", open_note="Opens in a new tab; on a phone it can open in the Google Maps app.",
  layers_h="The two layers",
  layers=[("Universities", "Universities listed in our <a href=\"/universities/\">University finder</a>. Fees, deadlines and scholarships are on the finder, with links to official pages."),
          ("Bengali Communities", "Bengali associations and Durga Puja organisers, from the Global Puja Parikrama directory. They are a starting point for finding people near you, all year round.")],
  how_h="How to use it",
  how=["Click the list icon at the top left of the map to show or hide each layer.",
       "Click a marker to see its name and details.",
       "Zoom in on the city you are considering to see both layers together."],
  care_h="Please note",
  care=["Community markers may show an approximate city location, not the exact venue.",
        "Puja entries are historical records from past years. They are not confirmed current events — check dates and venues with the organisers before you travel.",
        "Always confirm university information on the university's own website."],
  free="World Explorer is free to use, like everything on BiswaPath. The map is hosted by Google My Maps.",
  fix="Spotted a mistake or know a Bengali association that is missing? <a href=\"/contribute/\">Tell us</a>.",
  frame="Map of universities and Bengali communities"),
 "bn": dict(
  title="বিশ্বপাঠ বিশ্বমানচিত্র | World Explorer",
  desc="বিদেশে পড়তে যেতে চাওয়া ছাত্রছাত্রীদের জন্য বিশ্ববিদ্যালয় আর বাঙালি কমিউনিটির একটা বিনামূল্যের মানচিত্র।",
  intro="বিদেশে যাওয়ার আগে প্রত্যেক ছাত্র দুটো প্রশ্ন করে: <em>কোথায় পড়তে পারি?</em> আর <em>সেখানে গেলে কাছাকাছি কারা থাকবে?</em> — দুটোর উত্তর একটা মানচিত্রে।",
  open="Google Maps-এ মানচিত্রটা খুলুন", open_note="নতুন ট্যাবে খুলবে; ফোনে Google Maps অ্যাপেও খুলতে পারে।",
  layers_h="দুটো লেয়ার",
  layers=[("Universities (বিশ্ববিদ্যালয়)", "আমাদের <a href=\"/bn/universities/\">বিশ্ববিদ্যালয় খোঁজার পাতায়</a> থাকা বিশ্ববিদ্যালয়গুলো। ফি, ডেডলাইন আর স্কলারশিপের তথ্য অফিসিয়াল লিংক-সহ সেই পাতায় আছে।"),
          ("Bengali Communities (বাঙালি কমিউনিটি)", "Global Puja Parikrama-র তালিকা থেকে বাঙালি সংগঠন আর দুর্গাপুজোর আয়োজকেরা। সারা বছর কাছাকাছি মানুষ খুঁজে পাওয়ার একটা শুরু।")],
  how_h="কীভাবে ব্যবহার করবেন",
  how=["মানচিত্রের ওপরে বাঁদিকের তালিকা-আইকনে ক্লিক করে প্রতিটা লেয়ার দেখান বা লুকান।",
       "কোনো মার্কারে ক্লিক করলে নাম আর বিস্তারিত দেখা যাবে।",
       "যে শহরের কথা ভাবছেন, সেখানে জুম করলে দুটো লেয়ার একসঙ্গে দেখবেন।"],
  care_h="মনে রাখবেন",
  care=["কমিউনিটির মার্কার অনেক সময় শহরের আনুমানিক জায়গা দেখায়, ঠিক ঠিকানা নয়।",
        "পুজোর তথ্যগুলো আগের বছরের রেকর্ড। এগুলো এ বছরের নিশ্চিত অনুষ্ঠান নয় — যাওয়ার আগে আয়োজকদের সঙ্গে তারিখ আর জায়গা মিলিয়ে নিন।",
        "বিশ্ববিদ্যালয়ের তথ্য সবসময় বিশ্ববিদ্যালয়ের নিজের ওয়েবসাইটে মিলিয়ে নিন।"],
  free="বিশ্বপাঠের সবকিছুর মতো বিশ্বমানচিত্রও বিনামূল্যে। মানচিত্রটা Google My Maps-এ রাখা।",
  fix="কোনো ভুল চোখে পড়েছে, বা কোনো বাঙালি সংগঠন বাদ পড়েছে? <a href=\"/bn/contribute/\">আমাদের জানান</a>।",
  frame="বিশ্ববিদ্যালয় আর বাঙালি কমিউনিটির মানচিত্র"),
}

def content(lang):
    t = T[lang]
    layers = "".join(f"<li><b>{n}</b> — {d}</li>" for n, d in t["layers"])
    how = "".join(f"<li>{x}</li>" for x in t["how"])
    care = "".join(f"<li>{x}</li>" for x in t["care"])
    inner = f"""<p>{t['intro']}</p>
<p><a class="btn" href="{VIEW}" target="_blank" rel="noopener">{t['open']}</a> <span class="updated">{t['open_note']}</span></p>
</article>
<div class="mapwrap"><iframe src="{EMBED}" title="{t['frame']}" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<article class="wrap prose explorer">
<h2>{t['layers_h']}</h2><ul>{layers}</ul>
<h2>{t['how_h']}</h2><ol>{how}</ol>
<div class="invite"><p><b>{t['care_h']}</b></p><ul>{care}</ul></div>
<p>{t['free']}</p>
<p>{t['fix']}</p>"""
    return t["title"], t["desc"], inner
