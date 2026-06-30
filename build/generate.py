# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import partials as P

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def write_page(route, html):
    """route '' for home, otherwise 'about' -> /about/index.html"""
    if route == "":
        path = os.path.join(ROOT, "index.html")
    else:
        d = os.path.join(ROOT, route)
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


# Asset prefix is always "/" relative for clean folder routes; we use absolute paths.
AP = "/"


def page(route, title, desc, body, current):
    return (P.head(title, desc, AP) + P.header(current, AP) + body + P.footer(AP))


def begin_cta(label="Begin Your Exchange", href="/contact/"):
    return f'<a class="btn btn-gold" href="{href}">{label}</a>'


# ============ HOME ============
def build_home():
    hero = (f'<section class="hero" id="top"><div class="wrap"><div class="hero-copy">'
            f'<p class="eyebrow">For women ready to set something down</p>'
            f'<h1>Trade what weighs you down for <em>what lifts you up.</em></h1>'
            f'<p class="lead">THE Baggage Exchange is a transformational lifestyle and community brand that '
            f'helps women trade what weighs them down for what lifts them up through brunches, workshops, '
            f'retreats, media, products, merchandise, corporate experiences, and community engagement.</p>'
            f'<div class="journey-arrows"><b>HEALING</b> \u2192 <b>OPPORTUNITY</b> \u2192 <b>PURPOSE</b> \u2192 <b>EMPOWERMENT</b></div>'
            f'<div class="cta"><a class="btn btn-gold" href="/experiences/">Choose your exchange</a>'
            f'<a class="btn btn-ghost" href="/hope-journey/">Explore the H.O.P.E. Journey</a></div>'
            f'<p class="fineprint">A warm transformation community founded by a survivor and doctorally '
            f'prepared nurse practitioner. Trauma informed at its foundation, culturally responsive '
            f'throughout. At launch, HER Retreats center Black women, with wider lanes open to all.</p></div>'
            f'<div class="hero-art">{P.HERO_PASSPORT_SVG}<span class="tagline-chip">CHECK YOUR BAGGAGE</span></div>'
            f'</div></section>')

    overview = (f'<section class="section overview"><div class="wrap">'
                f'<div class="sec-head reveal"><p class="eyebrow">Website overview</p>'
                f'<h2>A lifestyle and community brand built around H.O.P.E.</h2></div>'
                f'<div class="copy-grid">'
                f'<article class="copy-card reveal"><h3>Website overview</h3><p>THE Baggage Exchange is a '
                f'transformational lifestyle and community brand that helps women trade what weighs them down '
                f'for what lifts them up through brunches, workshops, retreats, media, products, merchandise, '
                f'corporate experiences, and community engagement.</p></article>'
                f'<article class="copy-card reveal"><h3>The H.O.P.E. Curriculum</h3><p>The H.O.P.E. Curriculum '
                f'is the structured method behind every experience. It guides participants through Healing, '
                f'Opportunity, Purpose, and Empowerment in a way that can be adapted for brunches, workshops, '
                f'retreats, podcast conversations, corporate partners, community engagement, products, and '
                f'future facilitator training.</p></article>'
                f'<article class="copy-card reveal"><h3>The Four H.O.P.E. Beats</h3><p>The Four H.O.P.E. Beats '
                f'translate the H.O.P.E. Journey into a repeatable rhythm for conversations, events, workshops, '
                f'retreats, podcast episodes, social content, and digital experiences.</p></article>'
                f'</div></div></section>')

    journey = (f'<section class="section journey"><div class="wrap">'
               f'<div class="sec-head reveal"><p class="eyebrow">The method</p>'
               f'<h2>H.O.P.E. is a journey, not a slogan.</h2>'
               f'<p>The H.O.P.E. Curriculum is the structured method behind every experience. It guides '
               f'participants through Healing, Opportunity, Purpose, and Empowerment in a way that can be '
               f'adapted for brunches, workshops, retreats, podcast conversations, corporate partners, '
               f'community engagement, products, and future facilitator training.</p></div>'
               f'<div class="stages">'
               f'<div class="stage reveal"><div class="lt">H</div><h3>Healing</h3><p class="one">Set it down.</p>'
               f'<p>Make space to name it, feel safe, and set something down. Everything else grows from here.</p></div>'
               f'<div class="stage reveal"><div class="lt">O</div><h3>Opportunity</h3><p class="one">See what was there.</p>'
               f'<p>Reframe what happened and notice what is now possible, the openings that were there all along.</p></div>'
               f'<div class="stage reveal"><div class="lt">P</div><h3>Purpose</h3><p class="one">Turn pain to calling.</p>'
               f'<p>Turn lived experience, lessons, and values into meaningful direction and real momentum.</p></div>'
               f'<div class="stage reveal"><div class="lt">E</div><h3>Empowerment</h3><p class="one">Step forward.</p>'
               f'<p>Step forward with voice, clarity, confidence, and action. You leave with tools and a plan.</p></div>'
               f'</div></div></section><hr class="rule-perf">')

    podcast = (f'<section class="section pod"><div class="wrap"><div class="pod-cover reveal">{P.PODCAST_COVER_SVG}</div>'
               f'<div class="reveal"><p class="eyebrow">The podcast</p>'
               f'<h2>Real stories, <em>lighter bags.</em></h2>'
               f'<p>THE Baggage Exchange Podcast is the storytelling arm of the brand, on Spotify. Each week a '
               f'guest tells one real chapter of their life, then reads it a new way, guided by the Four '
               f'H.O.P.E. Beats. It brings the work into ongoing conversation and points listeners toward the '
               f'brunches, workshops, and retreats. Real stories, lighter bags.</p>'
               f'<p class="when">LAUNCHING ON SPOTIFY JULY 1</p>'
               f'<a class="btn btn-gold" href="/podcast/">Explore the podcast</a></div></div></section>')

    founder = (f'<section class="section founder"><div class="wrap reveal"><p class="eyebrow">Meet the founder</p>'
               f'<h2>Her story is the brand.</h2>'
               f'<p>\u201cDr. Shukairo Baker, DNP, built THE Baggage Exchange from what she lived. She traded what '
               f'weighed her down for what lifted her up, again and again, until the trading itself became the '
               f'way through.\u201d</p>'
               f'<a class="btn btn-plum" href="/about/">Read her story</a></div></section>')

    final = (f'<section class="section final"><div class="wrap reveal"><p class="eyebrow">Begin Your Exchange</p>'
             f'<h2>Ready to set something down?</h2>'
             f'<p>Reach out about a retreat, bring a brunch or workshop to your group, or just connect. We respond '
             f'personally, with no pressure and no obligation.</p>'
             f'<div class="cta"><a class="btn btn-gold" href="/contact/">Begin Your Exchange</a>'
             f'<a class="btn btn-plum" href="/experiences/">Browse all experiences</a></div></div></section>')

    body = (hero + P.marquee() + overview + journey + P.lanes_section() + P.bag_section()
            + P.passport_section() + podcast + founder + final)
    write_page("", page("", "THE Baggage Exchange | Trade what weighs you down for what lifts you up",
                         "THE Baggage Exchange is a transformational lifestyle and community brand that helps women trade what weighs them down for what lifts them up.",
                         body, "/"))


# ============ ABOUT ============
def build_about():
    crumb = '<a href="/">Home</a> / About'
    hero = P.subhero(crumb, "Meet the founder", "Her story is the brand.",
                     "THE Baggage Exchange was built from lived experience, then shaped into a method women can walk together.",
                     begin_cta("Read on"))
    # NOTE: Exact longer Founder story copy ("a Black woman", "a trauma survivor") was not located
    # in approved sources. Using the exact short About starter + required structure + respectful,
    # approved-source-only language. Replace when exact founder story is provided.
    about_long_comment = "<!-- ABOUT_LONG_COPY_NEEDED_FROM_USER: The exact longer Founder and Origin story (with identity language such as 'a Black woman' and 'a trauma survivor') was not found in approved workspace sources or memory. The structure and short approved starter are in place. Replace the body of these three sections with the exact founder story when the user provides it. Do not fabricate sensitive personal details. -->"
    body = (hero + about_long_comment +
            '<section class="section cream-sec"><div class="wrap prose reveal">'
            '<p class="eyebrow">Founder and Origin</p>'
            '<h2 style="font-size:clamp(26px,3.4vw,40px);margin:12px 0 18px">Why THE Baggage Exchange exists</h2>'
            '<p class="lead-p">This brand was created for people who are ready to name what they have carried, '
            'set down what no longer serves them, and walk forward with H.O.P.E.</p>'
            '<p>THE Baggage Exchange is a transformational lifestyle and community brand that helps women trade '
            'what weighs them down for what lifts them up through brunches, workshops, retreats, media, products, '
            'merchandise, corporate experiences, and community engagement. It was founded by a survivor and '
            'doctorally prepared nurse practitioner, trauma informed at its foundation and culturally responsive '
            'throughout.</p></div></section>'
            '<section class="section warm"><div class="wrap prose reveal">'
            '<p class="eyebrow">The roots</p>'
            '<h2 style="font-size:clamp(24px,3vw,34px);margin:12px 0 16px">Where the work comes from</h2>'
            '<p>The work is rooted in the Carolinas and in Black women, and it welcomes women everywhere to set '
            'something heavy down and carry something lighter forward. At launch, HER Retreats center Black women, '
            'with wider lanes open to all. The H.O.P.E. Curriculum, the structured method behind every experience, '
            'grew out of that lived foundation and now guides participants through Healing, Opportunity, Purpose, '
            'and Empowerment.</p></div></section>'
            '<section class="section cream-surface-sec"><div class="wrap prose reveal">'
            '<p class="eyebrow">The invitation</p>'
            '<h2 style="font-size:clamp(24px,3vw,34px);margin:12px 0 16px">An invitation to travel lighter</h2>'
            '<p>Wherever you start, the invitation is the same. Set something down and carry something better '
            'forward. Begin with a warm Empowerment Brunch, practice the work in a Carry On Workshop, or go all '
            'the way in on a HER Retreat. Every in person lane sends you home with a H.O.P.E. Bag, and every '
            'exchange adds a stamp to your passport.</p>'
            '<p style="font-family:var(--display);font-style:italic;color:var(--plum);font-size:18px;margin-top:8px">'
            'Dr. Shukairo Baker, DNP<br>Founder, THE Baggage Exchange</p>'
            '<div class="related"><a href="/hope-journey/">The H.O.P.E. Journey</a>'
            '<a href="/hope-curriculum/">The H.O.P.E. Curriculum</a>'
            '<a href="/experiences/">Explore the Experiences</a></div></div></section>'
            + final_cta())
    write_page("about", page("about", "About | THE Baggage Exchange",
                             "Meet the founder of THE Baggage Exchange and the origin of the H.O.P.E. method.",
                             body, "/about/"))


def final_cta(title="Ready to set something down?", body_txt="Reach out about a retreat, bring a brunch or workshop to your group, or just connect. We respond personally, with no pressure and no obligation.", extra=""):
    extra_btn = extra or '<a class="btn btn-plum" href="/experiences/">Browse all experiences</a>'
    return (f'<section class="section final"><div class="wrap reveal"><p class="eyebrow">Begin Your Exchange</p>'
            f'<h2>{title}</h2><p>{body_txt}</p>'
            f'<div class="cta"><a class="btn btn-gold" href="/contact/">Begin Your Exchange</a>{extra_btn}</div></div></section>')


# ============ THE METHOD: H.O.P.E. JOURNEY ============
def build_hope_journey():
    crumb = '<a href="/">Home</a> / <a href="/hope-journey/">The Method</a> / The H.O.P.E. Journey'
    hero = P.subhero(crumb, "The method", "H.O.P.E. is a <em>journey</em>, not a slogan.",
                     "The H.O.P.E. Journey is the inner pathway behind every experience. It moves through Healing, Opportunity, Purpose, and Empowerment.",
                     begin_cta())
    stages = (f'<section class="section journey"><div class="wrap">'
              f'<div class="sec-head reveal"><p class="eyebrow">The four stages</p>'
              f'<h2>Healing, Opportunity, Purpose, Empowerment.</h2>'
              f'<p>Each stage carries its own purpose and its own outcome for the participant. Together they form '
              f'one held pathway from setting something down to stepping forward.</p></div>'
              f'<div class="stages">'
              f'<div class="stage reveal"><div class="lt">H</div><h3>Healing</h3><p class="one">Set it down.</p>'
              f'<p>Purpose: make space to name it, feel safe, and set something down. Outcome: you leave a little '
              f'lighter, with permission to put one thing down for a while.</p></div>'
              f'<div class="stage reveal"><div class="lt">O</div><h3>Opportunity</h3><p class="one">See what was there.</p>'
              f'<p>Purpose: reframe what happened and notice what is now possible. Outcome: you see openings that '
              f'were there all along and a new way to read your own story.</p></div>'
              f'<div class="stage reveal"><div class="lt">P</div><h3>Purpose</h3><p class="one">Turn pain to calling.</p>'
              f'<p>Purpose: turn lived experience, lessons, and values into direction. Outcome: you connect your '
              f'story to a calling and real momentum.</p></div>'
              f'<div class="stage reveal"><div class="lt">E</div><h3>Empowerment</h3><p class="one">Step forward.</p>'
              f'<p>Purpose: step forward with voice, clarity, confidence, and action. Outcome: you leave with tools, '
              f'a plan, and the confidence to keep going.</p></div>'
              f'</div></div></section>')
    connect = ('<section class="section warm"><div class="wrap prose reveal">'
               '<p class="eyebrow">How it travels</p>'
               '<h2 style="font-size:clamp(24px,3vw,34px);margin:12px 0 16px">From method to experience to keepsake</h2>'
               '<p>The H.O.P.E. Journey is delivered through the H.O.P.E. Curriculum, the structured method behind '
               'every experience. You walk it at different depths across the lanes, and every in person lane sends '
               'you home with a H.O.P.E. Bag that holds the journey in your hands.</p>'
               '<div class="related"><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a>'
               '<a href="/hope-beats/">The Four H.O.P.E. Beats</a>'
               '<a href="/experiences/">Explore the Experiences</a></div></div></section>')
    body = hero + stages + connect + final_cta()
    write_page("hope-journey", page("hope-journey", "The H.O.P.E. Journey | THE Baggage Exchange",
                                    "The H.O.P.E. Journey is the inner pathway through Healing, Opportunity, Purpose, and Empowerment.",
                                    body, "/hope-journey/"))


# ============ THE METHOD: CURRICULUM ============
def build_hope_curriculum():
    crumb = '<a href="/">Home</a> / <a href="/hope-curriculum/">The Method</a> / The H.O.P.E. Curriculum'
    hero = P.subhero(crumb, "The method", "The H.O.P.E. Curriculum.",
                     "The H.O.P.E. Curriculum is the structured method behind every experience. It guides participants through Healing, Opportunity, Purpose, and Empowerment in a way that can be adapted for brunches, workshops, retreats, podcast conversations, corporate partners, community engagement, products, and future facilitator training.",
                     begin_cta())
    body = (hero +
            '<section class="section cream-sec"><div class="wrap prose reveal">'
            '<p class="eyebrow">What it is</p>'
            '<h2 style="font-size:clamp(24px,3vw,34px);margin:12px 0 16px">The structured method behind every experience</h2>'
            '<p class="lead-p">The H.O.P.E. Curriculum is the structured method behind every experience. It guides '
            'participants through Healing, Opportunity, Purpose, and Empowerment in a way that can be adapted for '
            'brunches, workshops, retreats, podcast conversations, corporate partners, community engagement, '
            'products, and future facilitator training.</p></div></section>'
            '<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">Where it adapts</p>'
            '<h2>One method, many rooms.</h2></div>'
            '<div class="chips">'
            '<span class="chip">Brunches</span><span class="chip">Workshops</span><span class="chip">Retreats</span>'
            '<span class="chip">Podcast conversations</span><span class="chip">Corporate partners</span>'
            '<span class="chip">Community engagement</span><span class="chip">Products</span>'
            '<span class="chip">Future facilitator training</span></div></div></section>'
            '<section class="section cream-surface-sec"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">Depths</p>'
            '<h2>Light, working, and immersive.</h2>'
            '<p>The same curriculum appears at different depths, so you can start small or go all in.</p></div>'
            '<div class="cards-3">'
            '<div class="feature t-gold reveal"><h3>Light</h3><p>A warm taste of the work at an Empowerment Brunch, '
            'where one small exchange helps you set something down.</p></div>'
            '<div class="feature t-sage reveal"><h3>Working</h3><p>Hands on practice in a Carry On Workshop, where you '
            'name what you carry and leave with practical tools.</p></div>'
            '<div class="feature t-plum reveal"><h3>Immersive</h3><p>The full journey on a HER Retreat, where you move '
            'through Healing, Empowerment, and Restoration in a held space.</p></div></div></div></section>'
            '<section class="section cream-sec"><div class="wrap prose reveal">'
            '<p class="eyebrow">Connected work</p>'
            '<h2 style="font-size:clamp(22px,2.6vw,30px);margin:12px 0 14px">Keep exploring</h2>'
            '<div class="related"><a href="/hope-journey/">The H.O.P.E. Journey</a>'
            '<a href="/hope-beats/">The Four H.O.P.E. Beats</a><a href="/experiences/">Experiences</a>'
            '<a href="/corporate-experiences/">Corporate Experiences</a>'
            '<a href="/community-engagement/">Community Engagement</a></div></div></section>'
            + final_cta())
    write_page("hope-curriculum", page("hope-curriculum", "The H.O.P.E. Curriculum | THE Baggage Exchange",
                                       "The H.O.P.E. Curriculum is the structured method behind every experience.",
                                       body, "/hope-curriculum/"))


# ============ THE METHOD: FOUR BEATS ============
def build_hope_beats():
    crumb = '<a href="/">Home</a> / <a href="/hope-beats/">The Method</a> / The Four H.O.P.E. Beats'
    hero = P.subhero(crumb, "The method", "The Four H.O.P.E. Beats.",
                     "The Four H.O.P.E. Beats translate the H.O.P.E. Journey into a repeatable rhythm for conversations, events, workshops, retreats, podcast episodes, social content, and digital experiences.",
                     begin_cta())
    beats = ('<section class="section journey"><div class="wrap">'
             '<div class="sec-head reveal"><p class="eyebrow">The rhythm</p>'
             '<h2>A repeatable rhythm for the work.</h2>'
             '<p>The Four H.O.P.E. Beats translate the H.O.P.E. Journey into a repeatable rhythm. Each beat ties to '
             'one stage of the journey.</p></div>'
             '<div class="beats">'
             '<div class="beat reveal"><p class="num">BEAT ONE</p><h3>Bag Check</h3><p class="tie">Tied to Healing.</p>'
             '<p>Name what you carry and make space to set something down.</p></div>'
             '<div class="beat reveal"><p class="num">BEAT TWO</p><h3>Plot Twist</h3><p class="tie">Tied to Opportunity.</p>'
             '<p>Reframe the story and notice the openings that were there all along.</p></div>'
             '<div class="beat reveal"><p class="num">BEAT THREE</p><h3>The Spark</h3><p class="tie">Tied to Purpose.</p>'
             '<p>Turn lived experience into direction and a sense of calling.</p></div>'
             '<div class="beat reveal"><p class="num">BEAT FOUR</p><h3>One Bold Move</h3><p class="tie">Tied to Empowerment.</p>'
             '<p>Step forward with one clear, confident action.</p></div></div></div></section>')
    uses = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">Where the beats play</p>'
            '<h2>One rhythm, many formats.</h2></div>'
            '<div class="chips">'
            '<span class="chip">Conversations</span><span class="chip">Events</span><span class="chip">Workshops</span>'
            '<span class="chip">Retreats</span><span class="chip">Podcast episodes</span>'
            '<span class="chip">Social content</span><span class="chip">Digital experiences</span></div>'
            '<div class="related" style="margin-top:24px"><a href="/hope-journey/">The H.O.P.E. Journey</a>'
            '<a href="/hope-curriculum/">The H.O.P.E. Curriculum</a><a href="/podcast/">The Podcast</a></div>'
            '</div></section>')
    body = hero + beats + uses + final_cta()
    write_page("hope-beats", page("hope-beats", "The Four H.O.P.E. Beats | THE Baggage Exchange",
                                  "The Four H.O.P.E. Beats translate the H.O.P.E. Journey into a repeatable rhythm.",
                                  body, "/hope-beats/"))


# ============ EXPERIENCES HUB ============
def build_experiences():
    crumb = '<a href="/">Home</a> / Experiences'
    hero = P.subhero(crumb, "Six experience lanes", "Choose where you begin.",
                     "Each lane is a different way to exchange what weighs you down for what lifts you up. Start small or go all in.",
                     begin_cta())
    distinction = ('<section class="section bag"><div class="wrap">'
                   '<div class="reveal"><p class="eyebrow">Shop tools or earn the bag</p>'
                   '<h2>The H.O.P.E. Shop and the H.O.P.E. Bag\u2122 are not the same.</h2>'
                   '<p>The H.O.P.E. Shop sells tools anyone can buy. The H.O.P.E. Bag\u2122 is the signature takeaway '
                   'you earn by attending an in person exchange. You do not buy the bag. You earn it by showing up '
                   'and doing the work in the room, and it stays exclusive to people who come in person.</p>'
                   '<div class="related"><a href="/hope-shop/" style="color:#FBF5EC;border-color:rgba(217,169,60,.5)">Visit the H.O.P.E. Shop</a></div></div>'
                   '<div class="levels reveal">'
                   '<div class="lvl"><b>Empowerment Brunch</b><p>The lightest bag.</p></div>'
                   '<div class="lvl"><b>Carry On Workshop</b><p>A working bag.</p></div>'
                   '<div class="lvl"><b>HER Retreats</b><p>The fullest bag.</p></div></div></div></section>')
    body = hero + P.lanes_section() + P.passport_section() + distinction + final_cta()
    write_page("experiences", page("experiences", "Experiences | THE Baggage Exchange",
                                   "Six experience lanes to exchange what weighs you down for what lifts you up.",
                                   body, "/experiences/"))


# ============ EXPERIENCE DETAIL PAGES ============
def detail_page(route, current, eyebrow, title_html, lead, approved_copy, sections_html,
                bag_level, cta_label, meta_title, meta_desc, crumb_label, hero_class="subhero"):
    crumb = f'<a href="/">Home</a> / <a href="/experiences/">Experiences</a> / {crumb_label}'
    hero = P.subhero(crumb, eyebrow, title_html, lead, begin_cta(cta_label))
    intro = (f'<section class="section cream-sec"><div class="wrap prose reveal">'
             f'<p class="lead-p">{approved_copy}</p></div></section>')
    bag = ('<section class="section warm"><div class="wrap prose reveal">'
           '<p class="eyebrow">Your H.O.P.E. Bag\u2122</p>'
           f'<h2 style="font-size:clamp(22px,2.8vw,32px);margin:12px 0 14px">What you carry home</h2>'
           f'<p>{bag_level}</p>'
           '<p class="form-note">The H.O.P.E. Bag\u2122 is earned in person, never sold. The H.O.P.E. Shop sells '
           'tools anyone can buy.</p></div></section>') if bag_level else ''
    body = hero + intro + sections_html + bag + final_cta(extra='<a class="btn btn-plum" href="/experiences/">Browse all experiences</a>')
    write_page(route, page(route, meta_title, meta_desc, body, current))


def build_brunch():
    sections = ('<section class="section cream-surface-sec"><div class="wrap reveal">'
                '<div class="sec-head reveal"><p class="eyebrow">What happens</p>'
                '<h2>Good food, honest conversation, one small exchange.</h2></div>'
                '<div class="cards-3">'
                '<div class="feature t-gold reveal"><h3>The social front door</h3><p>The warm, lightest way into the '
                'brand. No heavy lifting, just permission to put one thing down for a while.</p></div>'
                '<div class="feature t-sage reveal"><h3>One small exchange</h3><p>A short, guided moment where you set '
                'something down and leave a little lighter.</p></div>'
                '<div class="feature t-rose reveal"><h3>Carry forward</h3><p>You leave with a warm welcome, a tag, a '
                'short card set, and a small keepsake.</p></div></div></div></section>')
    detail_page("empowerment-brunch", "/empowerment-brunch/", "Experiences",
                "Empowerment Brunch.", "A seat at the table.",
                "THE Baggage Exchange Empowerment Brunch is the social front door to the brand. A warm, light gathering where good food, honest conversation, and one small exchange help guests set something down and leave a little lighter. No heavy lifting, just permission to put one thing down for a while.",
                sections,
                "Empowerment Brunch attendees take home the lightest H.O.P.E. Bag\u2122: a warm welcome, a tag, a short card set, and a small keepsake.",
                "Join or inquire", "Empowerment Brunch | THE Baggage Exchange",
                "The Empowerment Brunch is the warm social front door to THE Baggage Exchange.",
                "Empowerment Brunch")


def build_workshops():
    sections = ('<section class="section cream-surface-sec"><div class="wrap reveal">'
                '<div class="sec-head reveal"><p class="eyebrow">Practice the work</p>'
                '<h2>Name it, set it down, carry tools forward.</h2></div>'
                '<div class="cards-3">'
                '<div class="feature t-sage reveal"><h3>Name what you carry</h3><p>Guided experiences that help you '
                'see what you have been holding.</p></div>'
                '<div class="feature t-gold reveal"><h3>Set down what no longer serves</h3><p>Practice letting go of '
                'the weight that is not yours to keep.</p></div>'
                '<div class="feature t-plum reveal"><h3>Leave with practical tools</h3><p>Move forward with lighter '
                'bags and skills tied to the H.O.P.E. Curriculum.</p></div></div>'
                '<div class="related" style="margin-top:24px"><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a></div>'
                '</div></section>')
    detail_page("carry-on-workshops", "/carry-on-workshops/", "Experiences",
                "Carry On Workshop.", "Practice the work.",
                "The Carry On Workshop by THE Baggage Exchange is a guided experience that helps participants name what they carry, set down what no longer serves them, and leave with practical tools for moving forward with lighter bags.",
                sections,
                "Workshop attendees take home a working H.O.P.E. Bag\u2122: everything in the brunch bag, plus a session workbook and a tool tied to the skill you practiced.",
                "Book or inquire", "Carry On Workshop | THE Baggage Exchange",
                "Carry On Workshop help you name what you carry and leave with practical tools.",
                "Carry On Workshop")


def build_her():
    sections = ('<section class="section cream-surface-sec"><div class="wrap reveal">'
                '<div class="sec-head reveal"><p class="eyebrow">A deep dive.</p>'
                '<h2>Immersive restoration across the full journey.</h2></div>'
                '<div class="cards-3">'
                '<div class="feature t-plum reveal"><h3>Travel and time</h3><p>Three to four immersive days within the '
                'United States or five to seven abroad.</p></div>'
                '<div class="feature t-sage reveal"><h3>A held space</h3><p>Walk the full H.O.P.E. journey across a '
                'held, trauma-informed space.</p></div>'
                '<div class="feature t-rose reveal"><h3>Healing, Empowerment, Restoration</h3><p>Dive deep into the '
                'H.O.P.E. curriculum and move through each.</p></div></div></div></section>'
                '<section class="section warm"><div class="wrap prose reveal">'
                '<p class="eyebrow">Inaugural launch</p>'
                '<h2 style="font-size:clamp(22px,2.8vw,32px);margin:12px 0 14px">Planned for November 2026</h2>'
                '<p>At the inaugural launch planned for November 2026, HER Retreats center Black women, with broader '
                'retreats to follow.</p></div></section>')
    detail_page("her-retreats", "/her-retreats/", "Experiences",
                "HER Retreats.", "A deep dive.",
                "HER Retreats by THE Baggage Exchange are the deep-dive experience for women ready for immersive restoration. You travel for three to four immersive days within the United States or five to seven abroad, walking the full H.O.P.E. journey across a held, trauma-informed space. Guests set the heaviest things down, reframe the whole story, connect their lived experience to a calling, and leave with tools, a plan, and the confidence to step forward. This is where you dive deep into the H.O.P.E. curriculum and move through Healing, Empowerment, and Restoration. You leave with the fullest H.O.P.E. Bag of any experience. At the inaugural launch planned for November 2026, HER Retreats center Black women, with broader retreats to follow.",
                sections,
                "Retreat guests take home the fullest H.O.P.E. Bag\u2122 of any experience: a complete journal, the H.O.P.E. Journey workbook, ritual cards, a keepsake, and resources to carry forward.",
                "Join the retreat list", "HER Retreats | THE Baggage Exchange",
                "HER Retreats are the deep-dive immersive restoration experience of THE Baggage Exchange.",
                "HER Retreats")


# ============ PODCAST ============
def build_podcast():
    crumb = '<a href="/">Home</a> / <a href="/experiences/">Experiences</a> / The Podcast'
    hero = P.subhero(crumb, "The podcast", "Real stories, <em>lighter bags.</em>",
                     "The storytelling arm of THE Baggage Exchange, launching on Spotify on July 1.",
                     '<a class="btn btn-gold" href="mailto:podcast@thebaggageexchange.org">Media and podcast inquiries</a>')
    main = (f'<section class="section pod"><div class="wrap"><div class="pod-cover reveal">{P.PODCAST_COVER_SVG}</div>'
            f'<div class="reveal"><p class="eyebrow">The podcast</p><h2>Real stories, <em>lighter bags.</em></h2>'
            f'<p>THE Baggage Exchange Podcast is the storytelling arm of the brand, on Spotify. Each week a guest '
            f'tells one real chapter of their life, then reads it a new way, guided by the Four H.O.P.E. Beats. It '
            f'brings the work into ongoing conversation and points listeners toward the brunches, workshops, and '
            f'retreats. Real stories, lighter bags.</p>'
            f'<p class="when">LAUNCHING ON SPOTIFY JULY 1</p>'
            f'<a class="btn btn-gold" href="#">Listen on Spotify</a></div></div></section>')
    how = ('<section class="section cream-sec"><div class="wrap reveal">'
           '<div class="sec-head reveal"><p class="eyebrow">How each episode travels</p>'
           '<h2>One chapter, read a new way.</h2></div>'
           '<div class="cards-3">'
           '<div class="feature t-gold reveal"><h3>Weekly guest story</h3><p>Each week a guest tells one real chapter '
           'of their life.</p></div>'
           '<div class="feature t-sage reveal"><h3>Guided by the beats</h3><p>Bag Check, Plot Twist, The Spark, and '
           'One Bold Move shape the conversation.</p></div>'
           '<div class="feature t-rose reveal"><h3>Points you onward</h3><p>It points listeners toward the brunches, '
           'workshops, and retreats.</p></div></div>'
           '<div class="related" style="margin-top:24px"><a href="/hope-beats/">The Four H.O.P.E. Beats</a></div>'
           '</div></section>')
    inquiry = ('<section class="section warm"><div class="wrap prose reveal">'
               '<p class="eyebrow">Media and booking</p>'
               '<h2 style="font-size:clamp(22px,2.8vw,32px);margin:12px 0 14px">For media and podcast inquiries</h2>'
               '<p>Reach the show for guest, media, and booking inquiries at '
               '<a href="mailto:podcast@thebaggageexchange.org" style="color:#7a5a18;font-weight:700">podcast@thebaggageexchange.org</a>.</p>'
               '</div></section>')
    body = hero + main + how + inquiry + final_cta()
    write_page("podcast", page("podcast", "The Podcast | THE Baggage Exchange",
                               "THE Baggage Exchange Podcast launches on Spotify on July 1. Real stories, lighter bags.",
                               body, "/podcast/"))


# ============ H.O.P.E. SHOP ============
def build_shop():
    crumb = '<a href="/">Home</a> / <a href="/experiences/">Experiences</a> / The H.O.P.E. Shop'
    hero = P.subhero(crumb, "The shop", "The H.O.P.E. Shop.",
                     "Where the work becomes something you can hold.",
                     begin_cta())
    intro = ('<section class="section cream-sec"><div class="wrap prose reveal">'
             '<p class="lead-p">The Shop is where the work becomes something you can hold. Branded merchandise, Carry '
             'On Tags, journals, workbooks, affirmation cards, and practical tools tied to the H.O.P.E. Curriculum, '
             'and the signature H.O.P.E. Bag stays exclusive to those who join an in person exchange, so it is not '
             'sold here forward.</p></div></section>')
    grid = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">What you can hold</p>'
            '<h2>Tools tied to the H.O.P.E. Curriculum.</h2></div>'
            '<div class="cards-3">'
            '<div class="feature t-gold reveal"><h3>Branded merchandise</h3><p>Wear the reminder to travel lighter.</p></div>'
            '<div class="feature t-sage reveal"><h3>Carry On Tags</h3><p>The luggage tag that marks your lane.</p></div>'
            '<div class="feature t-rose reveal"><h3>Journals</h3><p>To capture what you set down.</p></div>'
            '<div class="feature t-plum reveal"><h3>Workbooks</h3><p>Walk the curriculum at your own pace.</p></div>'
            '<div class="feature t-gold reveal"><h3>Affirmation cards</h3><p>Short sets grouped by room.</p></div>'
            '<div class="feature t-sage reveal"><h3>Practical tools</h3><p>Tied directly to the H.O.P.E. Curriculum.</p></div>'
            '</div></div></section>')
    distinction = ('<section class="section bag"><div class="wrap">'
                   '<div class="reveal"><p class="eyebrow">Shop tools, earn the bag</p>'
                   '<h2>The H.O.P.E. Bag\u2122 stays exclusive to in person exchanges.</h2>'
                   '<p>The H.O.P.E. Shop sells tools anyone can buy. The signature H.O.P.E. Bag\u2122 is not sold here. '
                   'It stays exclusive to people who join an in person exchange, earned by showing up and doing the '
                   'work in the room.</p>'
                   '<div class="related"><a href="/experiences/" style="color:#FBF5EC;border-color:rgba(217,169,60,.5)">See the in person lanes</a></div></div>'
                   '<div class="levels reveal">'
                   '<div class="lvl"><b>In the Shop</b><p>Tools anyone can buy.</p></div>'
                   '<div class="lvl"><b>In the Bag\u2122</b><p>Earned in person, never sold.</p></div>'
                   '<div class="lvl"><b>The Passport</b><p>Every exchange earns a stamp in its own ink.</p></div></div></div></section>')
    body = hero + intro + grid + distinction + final_cta(extra='<a class="btn btn-plum" href="/experiences/">Browse all experiences</a>')
    write_page("hope-shop", page("hope-shop", "The H.O.P.E. Shop | THE Baggage Exchange",
                                 "The H.O.P.E. Shop is where the work becomes something you can hold.",
                                 body, "/hope-shop/"))


# ============ EXCHANGE HOUSE ============
def build_house():
    crumb = '<a href="/">Home</a> / <a href="/experiences/">Experiences</a> / The Exchange House'
    hero = P.subhero(crumb, "Coming soon", "The Exchange House.",
                     "The future physical home for the brand. Working toward Summer 2027.",
                     '<a class="btn btn-gold" href="/contact/">Follow updates</a>')
    intro = ('<section class="section cream-sec"><div class="wrap prose reveal">'
             '<p class="lead-p">The Exchange House by THE Baggage Exchange is the future physical home for the brand. '
             'One warm, welcoming space for brunches, workshops, community gatherings, podcast tapings, and '
             'restorative experiences. Working toward Summer 2027.</p>'
             '<p style="font-family:var(--mono);font-size:12px;letter-spacing:.18em;color:#9A4F49;text-transform:uppercase;'
             'background:rgba(197,116,110,.14);border:1px solid rgba(197,116,110,.4);display:inline-block;'
             'padding:8px 16px;border-radius:30px;opacity:.85">Coming soon &mdash; working toward Summer 2027</p></div></section>')
    grid = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">One warm space</p>'
            '<h2>A home for the work.</h2></div>'
            '<div class="cards-3">'
            '<div class="feature t-gold reveal"><h3>Brunches</h3><p>A seat at the table, hosted in one place.</p></div>'
            '<div class="feature t-sage reveal"><h3>Workshops</h3><p>Hands on practice, all under one roof.</p></div>'
            '<div class="feature t-rose reveal"><h3>Community gatherings</h3><p>Space to come together and belong.</p></div>'
            '<div class="feature t-plum reveal"><h3>Podcast tapings</h3><p>Real stories recorded in the room.</p></div>'
            '<div class="feature t-gold reveal"><h3>Restorative experiences</h3><p>A held space to set things down.</p></div>'
            '<div class="feature t-sage reveal"><h3>Working toward Summer 2027</h3><p>Follow along as the house takes shape.</p></div>'
            '</div></div></section>')
    body = hero + intro + grid + final_cta(title="Want to follow the Exchange House?",
                                           body_txt="Reach out to follow updates or to inquire about the future home for the brand.",
                                           extra='<a class="btn btn-plum" href="/experiences/">Browse all experiences</a>')
    write_page("exchange-house", page("exchange-house", "The Exchange House | THE Baggage Exchange",
                                      "The Exchange House is the future physical home for THE Baggage Exchange. Working toward Summer 2027.",
                                      body, "/exchange-house/"))


# ============ BRING US IN: CORPORATE ============
def build_corporate():
    crumb = '<a href="/">Home</a> / Bring Us In / Corporate Experiences'
    hero = P.subhero(crumb, "Bring us in", "Corporate Experiences.",
                     "Bring the H.O.P.E. Curriculum into your workplace.",
                     begin_cta("Inquire for your team"))
    intro = ('<section class="section cream-sec"><div class="wrap prose reveal">'
             '<p class="lead-p">THE Baggage Exchange Corporate Experiences bring the H.O.P.E. Curriculum into '
             'workplaces through customized conversations and sessions around resilience, leadership, emotional '
             'wellness, burnout prevention, and team culture.</p></div></section>')
    grid = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">What we bring</p>'
            '<h2>Customized for your team.</h2></div>'
            '<div class="cards-3">'
            '<div class="feature t-gold reveal"><h3>Resilience</h3><p>Tools to carry pressure without carrying it home.</p></div>'
            '<div class="feature t-sage reveal"><h3>Leadership</h3><p>Lead from a lighter, clearer place.</p></div>'
            '<div class="feature t-rose reveal"><h3>Emotional wellness</h3><p>Make room to name and tend what is real.</p></div>'
            '<div class="feature t-plum reveal"><h3>Burnout prevention</h3><p>Set the heavy things down before they pile up.</p></div>'
            '<div class="feature t-gold reveal"><h3>Team culture</h3><p>Build a culture that travels lighter together.</p></div>'
            '<div class="feature t-sage reveal"><h3>Customized sessions</h3><p>Conversations and sessions shaped to your group.</p></div>'
            '</div><div class="related" style="margin-top:24px"><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a>'
            '<a href="/community-engagement/">Community Engagement</a></div></div></section>')
    body = hero + intro + grid + final_cta(title="Bring the exchange to work.",
                                           body_txt="Reach out about a customized workplace or organizational booking. We respond personally, with no pressure and no obligation.",
                                           extra='<a class="btn btn-plum" href="/community-engagement/">Community Engagement</a>')
    write_page("corporate-experiences", page("corporate-experiences", "Corporate Experiences | THE Baggage Exchange",
                                             "Bring the H.O.P.E. Curriculum into your workplace with Corporate Experiences.",
                                             body, "/corporate-experiences/"))


# ============ BRING US IN: COMMUNITY ============
def build_community():
    crumb = '<a href="/">Home</a> / Bring Us In / Community Engagement'
    hero = P.subhero(crumb, "Bring us in", "Community Engagement.",
                     "Bring the work into your community.",
                     begin_cta("Inquire for your community"))
    intro = ('<section class="section cream-sec"><div class="wrap prose reveal">'
             '<p class="lead-p">THE Baggage Exchange Community Engagement brings the work into churches, schools, '
             'nonprofits, civic groups, and local communities through healing-centered gatherings, storytelling, '
             'resource connection, and community care.</p></div></section>')
    grid = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">Where we go</p>'
            '<h2>Into the places people gather.</h2></div>'
            '<div class="chips">'
            '<span class="chip">Churches</span><span class="chip">Schools</span><span class="chip">Nonprofits</span>'
            '<span class="chip">Civic groups</span><span class="chip">Local communities</span></div>'
            '<div class="cards-2" style="margin-top:28px">'
            '<div class="feature t-sage reveal"><h3>Healing-centered gatherings</h3><p>Warm spaces to set something '
            'down together.</p></div>'
            '<div class="feature t-gold reveal"><h3>Storytelling</h3><p>Real stories that help people feel less alone.</p></div>'
            '<div class="feature t-rose reveal"><h3>Resource connection</h3><p>Linking people to the support they need.</p></div>'
            '<div class="feature t-plum reveal"><h3>Community care</h3><p>Tending one another with belonging and dignity.</p></div>'
            '</div><div class="related" style="margin-top:24px"><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a>'
            '<a href="/corporate-experiences/">Corporate Experiences</a></div></div></section>')
    body = hero + intro + grid + final_cta(title="Bring the exchange to community.",
                                           body_txt="Reach out about a community partnership. We respond personally, with no pressure and no obligation.",
                                           extra='<a class="btn btn-plum" href="/corporate-experiences/">Corporate Experiences</a>')
    write_page("community-engagement", page("community-engagement", "Community Engagement | THE Baggage Exchange",
                                            "Community Engagement brings the work into churches, schools, nonprofits, civic groups, and communities.",
                                            body, "/community-engagement/"))


# ============ BRING US IN: CERTIFICATION OR LICENSING ============
def build_certification():
    crumb = '<a href="/">Home</a> / Bring Us In / Certification or Licensing'
    hero = P.subhero(crumb, "Bring us in", "Certification or Licensing.",
                     "Future facilitator training and licensing for the H.O.P.E. Curriculum.",
                     '<a class="btn btn-gold" href="/contact/">Inquire about licensing</a>')
    intro = ('<section class="section cream-sec"><div class="wrap prose reveal">'
             '<p class="lead-p">The H.O.P.E. Curriculum is the structured method behind every experience. Future '
             'facilitator training and licensing will allow approved partners to teach and facilitate the work, with '
             'written permission and a written license from The Baggage Exchange LLC.</p>'
             '<p style="font-family:var(--mono);font-size:12px;letter-spacing:.18em;color:#7a5a18;text-transform:uppercase;'
             'background:rgba(217,169,60,.14);border:1px solid rgba(217,169,60,.4);display:inline-block;'
             'padding:8px 16px;border-radius:30px">Coming soon &mdash; inquire to be notified</p></div></section>')
    grid = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">What it would allow</p>'
            '<h2>Carry the method, with permission.</h2></div>'
            '<div class="cards-3">'
            '<div class="feature t-gold reveal"><h3>Who it is for</h3><p>Facilitators, organizations, and partners who '
            'want to bring the H.O.P.E. Curriculum to their own communities.</p></div>'
            '<div class="feature t-sage reveal"><h3>What it covers</h3><p>Training and licensing to teach and facilitate '
            'the work with fidelity to the method.</p></div>'
            '<div class="feature t-plum reveal"><h3>Status</h3><p>Being formalized. Reach out to express interest and be '
            'notified when it opens.</p></div></div>'
            '<div class="related" style="margin-top:24px"><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a>'
            '<a href="/corporate-experiences/">Corporate Experiences</a><a href="/community-engagement/">Community Engagement</a></div>'
            '</div></section>')
    body = hero + intro + grid + final_cta(title="Interested in facilitating the work?",
                                           body_txt="Reach out about future certification or licensing. We respond personally, with no pressure and no obligation.",
                                           extra='<a class="btn btn-plum" href="/hope-curriculum/">The H.O.P.E. Curriculum</a>')
    write_page("certification-licensing", page("certification-licensing", "Certification or Licensing | THE Baggage Exchange",
                                               "Future facilitator training and licensing for the H.O.P.E. Curriculum.",
                                               body, "/certification-licensing/"))


# ============ CONTACT ============
def build_contact():
    crumb = '<a href="/">Home</a> / Contact'
    hero = P.subhero(crumb, "Begin Your Exchange", "Let\u2019s connect.",
                     "Reach out about a retreat, bring a brunch or workshop to your group, partner with us, or just connect. We respond personally, with no pressure and no obligation.")
    form = ('<section class="section cream-sec"><div class="wrap"><div class="contact-grid">'
            '<div class="reveal"><div class="sec-head reveal" style="margin-bottom:24px"><p class="eyebrow">Send a note</p>'
            '<h2 style="font-size:clamp(24px,3vw,34px)">Tell us what you are carrying.</h2></div>'
            '<form class="form-card" data-static-form data-mailto="hello@thebaggageexchange.org" novalidate>'
            '<div class="field"><label for="name">Your name</label><input id="name" name="name" type="text" autocomplete="name" required></div>'
            '<div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>'
            '<div class="field"><label for="topic">What are you reaching out about?</label>'
            '<select id="topic" name="topic">'
            '<option>General inquiry</option><option>Retreat inquiry</option>'
            '<option>Brunch or workshop inquiry</option><option>Corporate inquiry</option>'
            '<option>Community inquiry</option><option>Media or podcast inquiry</option></select></div>'
            '<div class="field"><label for="message">Your message</label><textarea id="message" name="message" required></textarea></div>'
            '<button class="btn btn-gold" type="submit">Begin Your Exchange</button>'
            '<p class="form-confirm form-note" role="status" tabindex="-1" hidden></p>'
            '<p class="form-note">This form is not connected to a server. You can also email us directly using the details to the right.</p>'
            '</form></div>'
            '<div class="contact-detail reveal">'
            '<div class="blk"><b>General inquiries</b><a href="mailto:hello@thebaggageexchange.org">hello@thebaggageexchange.org</a></div>'
            '<div class="blk"><b>Media and podcast inquiries</b><a href="mailto:podcast@thebaggageexchange.org">podcast@thebaggageexchange.org</a></div>'
            '<div class="blk"><b>Call or text</b><a href="tel:+17043122777">704.312.2777</a><a href="tel:+18445053848">1.844.505.3848</a></div>'
            '<div class="blk"><b>Online</b><a href="https://thebaggageexchange.org">thebaggageexchange.org</a></div>'
            '<div class="blk"><b>How we respond</b><span>We respond personally, with no pressure and no obligation.</span></div>'
            '</div></div></div></section>')
    ways = ('<section class="section warm"><div class="wrap reveal">'
            '<div class="sec-head reveal"><p class="eyebrow">Ways to begin</p>'
            '<h2>Choose your exchange.</h2></div>'
            '<div class="cards-2">'
            '<div class="feature t-gold reveal"><h3>Retreat inquiry</h3><p>Ask about HER Retreats and the inaugural '
            'November 2026 launch. <a href="mailto:hello@thebaggageexchange.org" style="color:#7a5a18;font-weight:700">hello@thebaggageexchange.org</a></p></div>'
            '<div class="feature t-sage reveal"><h3>Brunch or workshop inquiry</h3><p>Bring an Empowerment Brunch or '
            'Carry On Workshop to your group. <a href="mailto:hello@thebaggageexchange.org" style="color:#7a5a18;font-weight:700">hello@thebaggageexchange.org</a></p></div>'
            '<div class="feature t-rose reveal"><h3>Corporate and community inquiry</h3><p>Bring the H.O.P.E. Curriculum '
            'to your workplace or community. <a href="mailto:hello@thebaggageexchange.org" style="color:#7a5a18;font-weight:700">hello@thebaggageexchange.org</a></p></div>'
            '<div class="feature t-plum reveal"><h3>Media and podcast inquiry</h3><p>For media and podcast inquiries, '
            'reach the show at <a href="mailto:podcast@thebaggageexchange.org" style="color:#7a5a18;font-weight:700">podcast@thebaggageexchange.org</a></p></div>'
            '</div></div></section>')
    body = hero + form + ways
    write_page("contact", page("contact", "Contact | THE Baggage Exchange",
                               "Reach THE Baggage Exchange about retreats, brunches, workshops, corporate and community bookings, or media.",
                               body, "/contact/"))


def main():
    build_home()
    build_about()
    build_hope_journey()
    build_hope_curriculum()
    build_hope_beats()
    build_experiences()
    build_brunch()
    build_workshops()
    build_her()
    build_podcast()
    build_shop()
    build_house()
    build_corporate()
    build_community()
    build_certification()
    build_contact()
    print("\nAll pages generated.")


if __name__ == "__main__":
    main()
