# -*- coding: utf-8 -*-
"""Shared HTML partials for THE Baggage Exchange multipage site.
Visual source of truth: tbe-approved-revert/index.html (approved luxe homepage).
Copy reinstated from task brief and tbe_sitemap_blueprint.md.
"""

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400;1,500&family=Mulish:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'
)


def head(title, desc, asset_prefix):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="{asset_prefix}assets/styles.css">
</head>
<body>"""


# Navigation model. (label, href, dropdown items or None)
NAV = [
    ("Home", "/", None),
    ("About", "/about/", None),
    ("The Method", None, [
        ("The H.O.P.E. Journey", "/hope-journey/"),
        ("The H.O.P.E. Curriculum", "/hope-curriculum/"),
        ("The Four H.O.P.E. Beats", "/hope-beats/"),
    ]),
    ("Experiences", None, [
        ("Experiences Hub", "/experiences/"),
        ("Empowerment Brunch", "/empowerment-brunch/"),
        ("Carry On Workshop", "/carry-on-workshops/"),
        ("HER Retreats", "/her-retreats/"),
        ("The Podcast", "/podcast/"),
        ("The H.O.P.E. Shop", "/hope-shop/"),
        ("The Exchange House", "/exchange-house/"),
    ]),
    ("Bring Us In", None, [
        ("Corporate Experiences", "/corporate-experiences/"),
        ("Community Engagement", "/community-engagement/"),
        ("Certification or Licensing", "/certification-licensing/"),
    ]),
    ("Contact", "/contact/", None),
]


def _is_current(href, current):
    return href == current


def header(current, ap):
    # Desktop nav
    items = []
    for label, href, kids in NAV:
        if kids is None:
            cur = ' aria-current="page"' if _is_current(href, current) else ''
            items.append(f'<a href="{href}"{cur}>{label}</a>')
        else:
            child_current = any(_is_current(k[1], current) for k in kids)
            curattr = ' aria-current="true"' if child_current else ''
            links = ''.join(
                f'<a href="{kh}"{" aria-current=\"page\"" if _is_current(kh, current) else ""}>{kl}</a>'
                for kl, kh in kids
            )
            items.append(
                f'<div class="has-menu" data-open="false">'
                f'<button type="button" aria-haspopup="true" aria-expanded="false"{curattr}>{label} <span class="caret">\u25BE</span></button>'
                f'<div class="menu">{links}</div></div>'
            )
    desktop = ''.join(items)

    # Mobile nav
    m = []
    for label, href, kids in NAV:
        if kids is None:
            m.append(f'<a href="{href}">{label}</a>')
        else:
            sub = ''.join(f'<a href="{kh}">{kl}</a>' for kl, kh in kids)
            m.append(f'<div class="m-group"><span>{label}</span>{sub}</div>')
    mobile = ''.join(m)

    return f"""<header class="head"><div class="wrap">
<a class="brand" href="/" aria-label="THE Baggage Exchange home"><img src="{ap}assets/logo-reversed.svg" alt="THE Baggage Exchange"></a>
<nav class="nav" aria-label="Primary">{desktop}<a class="btn btn-gold" href="/contact/">Begin Your Exchange</a></nav>
<button class="menu-btn" aria-label="Open menu" aria-expanded="false">\u2630</button>
</div></header>
<div class="mobile-nav" aria-label="Mobile navigation">{mobile}<a class="btn btn-gold" href="/contact/">Begin Your Exchange</a></div>"""


def marquee():
    spans = [
        "You are allowed to set it down",
        "Lighter is still strong",
        "Your story is the breakthrough",
        "You do not carry it alone",
        "Trade the weight for the work",
        "Healing is a journey, not a deadline",
    ]
    one = ''.join(f'<span>{s}</span>' for s in spans)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{one}{one}</div></div>'


FOOTER_BLURB = ("Where women trade what weighs them down for what lifts them up. A warm community "
                "walking the H.O.P.E. journey together, through Healing, Opportunity, Purpose, and "
                "Empowerment. Rooted in the Carolinas and in BIPOC women, it welcomes women everywhere "
                "to set something heavy down and carry something lighter forward.")

TM_LINE = ("THE Baggage Exchange and the H.O.P.E. system are trademarks of The Baggage Exchange LLC.")

IP_NOTE = ("A trademark application has been submitted for THE BAGGAGE EXCHANGE. THE Baggage Exchange, "
           "the H.O.P.E. Curriculum, the H.O.P.E. Journey, the Four H.O.P.E. Beats, the H.O.P.E. Bag, "
           "HER Retreats, related tools, training materials, content, and brand methods are original "
           "works of The Baggage Exchange LLC. Use, reproduction, teaching, certification, licensing, "
           "or facilitator training by another person or entity requires written permission and a "
           "written license from The Baggage Exchange LLC. Registration status is handled separately "
           "through counsel.")


def footer(ap):
    return f"""<footer class="foot"><div class="wrap">
<div class="grid">
<div><div class="flogo"><img src="{ap}assets/logo-reversed.svg" alt="THE Baggage Exchange"></div>
<p class="blurb">{FOOTER_BLURB}</p></div>
<div><h4>Explore</h4><ul>
<li><a href="/about/">About</a></li>
<li><a href="/hope-journey/">The H.O.P.E. Journey</a></li>
<li><a href="/hope-curriculum/">The H.O.P.E. Curriculum</a></li>
<li><a href="/hope-beats/">The Four H.O.P.E. Beats</a></li>
<li><a href="/experiences/">Experiences</a></li>
<li><a href="/podcast/">The Podcast</a></li>
<li><a href="/hope-shop/">The H.O.P.E. Shop</a></li>
</ul></div>
<div><h4>Connect</h4><ul>
<li><a href="tel:+17043122777">704.312.2777</a></li>
<li><a href="tel:+18445053848">1.844.505.3848</a></li>
<li><a href="mailto:hello@thebaggageexchange.org">hello@thebaggageexchange.org for general inquiries</a></li>
<li><a href="mailto:podcast@thebaggageexchange.org">podcast@thebaggageexchange.org for media and podcast inquiries</a></li>
<li><a href="https://thebaggageexchange.org">thebaggageexchange.org</a></li>
</ul></div>
</div>
<div class="legal-block">
<p class="tm-line">THE BAGGAGE EXCHANGE \u2122 &mdash; {TM_LINE}</p>
<p>{IP_NOTE}</p>
<p>&copy; 2025 The Baggage Exchange LLC. Trade what weighs you down for what lifts you up.</p>
</div>
</div></footer>
<script src="{ap}assets/site.js"></script>
</body></html>"""


# ---- Reusable SVG components (from approved source) ----

HERO_PASSPORT_SVG = """<svg class="passport" viewBox="0 0 560 800" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="THE Baggage Exchange Passport"><defs><linearGradient id="pgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0D27A"/><stop offset=".5" stop-color="#D4A53C"/><stop offset="1" stop-color="#A9781F"/></linearGradient><linearGradient id="pplum" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A2240"/><stop offset=".55" stop-color="#4D1A33"/><stop offset="1" stop-color="#3A1224"/></linearGradient><linearGradient id="psheen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".14"/><stop offset=".4" stop-color="#fff" stop-opacity="0"/></linearGradient></defs><rect width="560" height="800" rx="20" fill="url(#pplum)"/><rect width="560" height="800" rx="20" fill="url(#psheen)"/><rect x="26" y="26" width="508" height="748" rx="12" fill="none" stroke="#D9A93C" stroke-width="2" stroke-opacity=".85"/><rect x="34" y="34" width="492" height="732" rx="9" fill="none" stroke="#D9A93C" stroke-width="1" stroke-opacity=".45"/><text x="280" y="120" text-anchor="middle" font-family="'Playfair Display',serif" font-size="17" font-weight="700" letter-spacing="5" fill="#D9A93C">THE BAGGAGE EXCHANGE</text><g transform="translate(185,190)"><path d="M0 42 q0 -22 20 -22 q20 0 20 22" fill="none" stroke="#FBF5EC" stroke-width="7" stroke-linecap="round" transform="translate(40,0)"/><rect x="0" y="40" width="120" height="92" rx="13" fill="url(#pgold)"/><line x1="5" y1="80" x2="115" y2="80" stroke="#FBF5EC" stroke-width="6"/><rect x="50" y="74" width="20" height="14" rx="2" fill="#FBF5EC"/><rect x="120" y="100" width="78" height="60" rx="9" fill="#FBF5EC"/><line x1="124" y1="126" x2="194" y2="126" stroke="#D4A53C" stroke-width="4"/></g><text x="280" y="400" text-anchor="middle" font-family="'Playfair Display',serif" font-size="72" font-weight="700" letter-spacing="8" fill="#D9A93C">PASSPORT</text><line x1="160" y1="430" x2="400" y2="430" stroke="#D9A93C" stroke-width="1.4" stroke-opacity=".7"/><text x="280" y="470" text-anchor="middle" font-family="'Playfair Display',serif" font-size="20" font-style="italic" fill="#FBF5EC">Check your baggage. Claim your H.O.P.E.</text><g transform="translate(280,650)"><circle r="56" fill="none" stroke="#D9A93C" stroke-width="2"/><circle r="48" fill="none" stroke="#D9A93C" stroke-width="1" stroke-opacity=".5"/><text y="-6" text-anchor="middle" font-family="'Playfair Display',serif" font-size="15" font-weight="700" letter-spacing="2" fill="#D9A93C">H.O.P.E.</text><text y="16" text-anchor="middle" font-family="'Space Mono',monospace" font-size="9" letter-spacing="3" fill="#FBF5EC">THE JOURNEY</text></g></svg>"""

PASSPORT_OPEN_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="100%" style="display:block" role="img" aria-label="THE Baggage Exchange Passport open spread with six lane stamps"><defs><linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0D27A"/><stop offset="0.5" stop-color="#D4A53C"/><stop offset="1" stop-color="#A9781F"/></linearGradient><linearGradient id="cream" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFDF8"/><stop offset="0.5" stop-color="#FBF5EC"/><stop offset="1" stop-color="#F2E8D7"/></linearGradient></defs><rect width="100%" height="680" rx="10" fill="#E9DEC9"/><rect x="24" y="24" width="464" height="632" rx="6" fill="url(#cream)"/><rect x="512" y="24" width="464" height="632" rx="6" fill="url(#cream)"/><rect x="497" y="24" width="6" height="632" fill="#000" opacity=".06"/><text x="256" y="74" text-anchor="middle" font-family="Playfair Display" font-size="13" font-weight="700" letter-spacing="4" fill="#D9A93C">THE BAGGAGE EXCHANGE</text><text x="256" y="106" text-anchor="middle" font-family="Playfair Display" font-size="26" font-weight="700" fill="#4D1A33">Traveler</text><text x="58" y="260" font-family="Arial" font-size="12" font-weight="700" letter-spacing="2" fill="#D9A93C">NAME</text><line x1="58" y1="274" x2="454" y2="274" stroke="#E3C6A0" stroke-width="1.4"/><text x="58" y="312" font-family="Arial" font-size="12" font-weight="700" letter-spacing="2" fill="#D9A93C">MEMBER SINCE</text><line x1="58" y1="326" x2="454" y2="326" stroke="#E3C6A0" stroke-width="1.4"/><text x="256" y="630" text-anchor="middle" font-family="Playfair Display" font-size="12" font-style="italic" fill="#4D1A33">Trade what weighs you down for what lifts you up.</text><text x="744" y="74" text-anchor="middle" font-family="Playfair Display" font-size="13" font-weight="700" letter-spacing="5" fill="#D9A93C">STAMPS</text><text x="744" y="102" text-anchor="middle" font-family="Playfair Display" font-size="15" font-style="italic" fill="#4D1A33">One for every exchange.</text><g font-family="Playfair Display" font-size="11" font-weight="700" letter-spacing="1" fill="none"><circle cx="589" cy="295" r="44" stroke="#C5746E" stroke-width="2.4"/><text x="589" y="294" text-anchor="middle" fill="#C5746E">BRUNCH</text><circle cx="744" cy="295" r="44" stroke="#6F9072" stroke-width="2.4"/><text x="744" y="294" text-anchor="middle" fill="#6F9072">WORKSHOPS</text><circle cx="899" cy="295" r="44" stroke="#4D1A33" stroke-width="2.4"/><text x="899" y="294" text-anchor="middle" fill="#4D1A33">HER</text><circle cx="589" cy="536" r="44" stroke="#B8881F" stroke-width="2.4"/><text x="589" y="535" text-anchor="middle" fill="#B8881F">PODCAST</text><circle cx="744" cy="536" r="44" stroke="#21160F" stroke-width="2.4" opacity=".4"/><text x="744" y="535" text-anchor="middle" fill="#21160F" opacity=".4">SHOP</text><circle cx="899" cy="536" r="44" stroke="#A8623A" stroke-width="2.4" opacity=".4"/><text x="899" y="535" text-anchor="middle" fill="#A8623A" opacity=".4">HOUSE</text></g></svg>"""

PODCAST_COVER_SVG = """<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="THE Baggage Exchange Podcast cover"><defs><linearGradient id="cgold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F0D27A"/><stop offset=".5" stop-color="#D4A53C"/><stop offset="1" stop-color="#A9781F"/></linearGradient><linearGradient id="cplum" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A2240"/><stop offset=".6" stop-color="#4D1A33"/><stop offset="1" stop-color="#3A1224"/></linearGradient></defs><rect width="300" height="300" rx="18" fill="url(#cplum)"/><text x="150" y="52" text-anchor="middle" font-family="Space Mono" font-size="11" letter-spacing="3" fill="#D9A93C">THE BAGGAGE EXCHANGE</text><text x="150" y="218" text-anchor="middle" font-family="Playfair Display" font-size="42" font-weight="700" letter-spacing="3" fill="#D9A93C">PODCAST</text><text x="150" y="250" text-anchor="middle" font-family="Playfair Display" font-size="15" font-style="italic" fill="#FBF5EC">Real stories, lighter bags.</text></svg>"""


# Luggage tag lane data: (cls, lane_eyebrow, name, sub, desc, code, href, soon)
LANES = [
    ("brunch", "Experience Lane", "Empowerment Brunch", "A seat at the table.",
     "THE Baggage Exchange Empowerment Brunch is the social front door to the brand. A warm, light gathering where good food, honest conversation, and one small exchange help guests set something down and leave a little lighter. No heavy lifting, just permission to put one thing down for a while.",
     "BRN 01", "/empowerment-brunch/", False),
    ("workshops", "Experience Lane", "Carry On Workshop", "Practice the work.",
     "The Carry On Workshop by THE Baggage Exchange is a guided experience that helps participants name what they carry, set down what no longer serves them, and leave with practical tools for moving forward with lighter bags.",
     "WRK 02", "/carry-on-workshops/", False),
    ("her", "Experience Lane", "HER Retreats", "A deep dive.",
     "HER Retreats by THE Baggage Exchange are the deep-dive experience for women ready for immersive restoration. You travel for three to four immersive days within the United States or five to seven abroad, walking the full H.O.P.E. journey across a held, trauma-informed space. Guests set the heaviest things down, reframe the whole story, connect their lived experience to a calling, and leave with tools, a plan, and the confidence to step forward. This is where you dive deep into the H.O.P.E. curriculum and move through Healing, Empowerment, and Restoration. You leave with the fullest H.O.P.E. Bag of any experience. At the inaugural launch planned for November 2026, HER Retreats center BIPOC women, with broader retreats to follow.",
     "HER 03", "/her-retreats/", False),
    ("podcast", "Experience Lane", "The Podcast", "Unpack it in half an hour.",
     "THE Baggage Exchange Podcast is the storytelling arm of the brand, on Spotify. Each week a guest tells one real chapter of their life, then reads it a new way, guided by the Four H.O.P.E. Beats. It brings the work into ongoing conversation and points listeners toward the brunches, workshops, and retreats. Real stories, lighter bags.",
     "POD 04", "/podcast/", False),
    ("shop", "Experience Lane", "The H.O.P.E. Shop", "Shop the tools.",
     "The Shop is where the work becomes something you can hold. Branded merchandise, Carry On Tags, journals, workbooks, affirmation cards, and practical tools tied to the H.O.P.E. Curriculum, and the signature H.O.P.E. Bag stays exclusive to those who join an in person exchange, so it is not sold here forward.",
     "SHP 05", "/hope-shop/", False),
    ("house", "Experience Lane", "The Exchange House", "Coming soon.",
     "The Exchange House by THE Baggage Exchange is the future physical home for the brand. One warm, welcoming space for brunches, workshops, community gatherings, podcast tapings, and restorative experiences. Working toward Summer 2027.",
     "HSE 06", "/exchange-house/", True),
]


def tag_card(lane, link=True):
    cls, eyebrow, name, sub, desc, code, href, soon = lane
    soon_badge = '<span class="soon">COMING SOON</span>' if soon else ''
    link_cls = ' linktag' if link else ''
    inner = (f'<span class="grommet"></span><span class="cord"></span>{soon_badge}'
             f'<p class="lane-eyebrow">{eyebrow}</p><h3>{name}</h3>'
             f'<p class="sub">{sub}</p><p class="desc">{desc}</p>'
             f'<div class="tagfoot"><div class="barcode"></div><span class="code">{code}</span></div>')
    if link:
        return f'<a class="tag {cls}{link_cls} reveal" href="{href}" aria-label="{name}">{inner}</a>'
    return f'<article class="tag {cls} reveal">{inner}</article>'


def lanes_section(link=True):
    cards = ''.join(tag_card(l, link=link) for l in LANES)
    return (f'<section class="section lanes"><div class="wrap">'
            f'<div class="sec-head reveal"><p class="eyebrow">SIX EXPERIENCE LANES</p>'
            f'<h2>Choose where you begin.</h2>'
            f'<p>Each lane is a different way to exchange what weighs you down for what lifts you up. '
            f'Start small or go all in. Whether you want a warm gathering, a hands on workshop, or a few '
            f'immersive days away, there is a lane that meets you where you are, and every in person lane '
            f'sends you home with a H.O.P.E. Bag. Ready? Let\u2019s Travel!</p></div>'
            f'<div class="tags">{cards}</div></div></section>')


def bag_section():
    return ("""<section class="section bag"><div class="wrap">
<div class="reveal"><p class="eyebrow">The signature takeaway</p>
<h2>Every in person exchange sends you home with a H.O.P.E. Bag\u2122.</h2>
<p>The H.O.P.E. Bag\u2122 is the signature takeaway you earn by attending an in person exchange. You do not buy it. You earn it by showing up and doing the work in the room. It holds tools, prompts, and keepsakes matched to your experience, so the work leaves the room in your hands and keeps going at home. The H.O.P.E. Shop sells tools anyone can buy, while the H.O.P.E. Bag\u2122 stays exclusive to people who come in person.</p>
<div class="holds">
<div class="hold"><b>CARRY ON TAG</b><span>The luggage tag that marks your lane.</span></div>
<div class="hold"><b>AFFIRMATION CARDS</b><span>A set grouped by room.</span></div>
<div class="hold"><b>JOURNAL PAGE</b><span>To capture what you set down.</span></div>
<div class="hold"><b>A KEEPSAKE</b><span>One signature piece to remember it.</span></div>
</div></div>
<div class="levels reveal">
<div class="lvl"><b>Empowerment Brunch</b><p>The lightest bag. A warm welcome, a tag, a short card set, and a small keepsake.</p></div>
<div class="lvl"><b>Carry On Workshop</b><p>A working bag. Everything in the brunch bag, plus a session workbook and a tool tied to the skill you practiced.</p></div>
<div class="lvl"><b>HER Retreats</b><p>The fullest bag. A complete journal, the H.O.P.E. Journey workbook, ritual cards, a keepsake, and resources to carry forward.</p></div>
</div></div></section>""")


def passport_section():
    return (f'<section class="section passport-sec"><div class="wrap">'
            f'<div class="reveal"><p class="eyebrow">Stamp the journey</p>'
            f'<h2>Collect your H.O.P.E. Passport.</h2>'
            f'<p>Every exchange you attend earns a stamp in its own ink. A full passport shows the H.O.P.E. '
            f'Journey at a glance. Watch the pages fill as you move through the lanes, until a single passport '
            f'tells the whole story of where you have been. It is a light, gamified keepsake, not an account.</p>'
            f'<div class="ink-row"><span class="ink" style="background:#C5746E">Brunch</span>'
            f'<span class="ink" style="background:#6F9072">Workshop</span>'
            f'<span class="ink" style="background:#4D1A33">HER</span>'
            f'<span class="ink" style="background:#B8881F">Podcast</span>'
            f'<span class="ink" style="background:#21160F">Shop</span>'
            f'<span class="ink" style="background:#A8623A">House</span></div></div>'
            f'<div class="reveal"><div class="passport-open">{PASSPORT_OPEN_SVG}</div></div></div></section>')


def subhero(crumb_html, eyebrow, title_html, lead, cta_html=""):
    cta = f'<div class="cta">{cta_html}</div>' if cta_html else ''
    return (f'<section class="subhero"><div class="wrap">'
            f'<p class="crumbs">{crumb_html}</p>'
            f'<p class="eyebrow" style="margin-top:14px">{eyebrow}</p>'
            f'<h1>{title_html}</h1>'
            f'<p class="lead">{lead}</p>{cta}</div></section>')
