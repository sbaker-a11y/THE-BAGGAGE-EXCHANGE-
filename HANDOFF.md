# THE Baggage Exchange — Multipage Static Site (Handoff)

**Project path:** `/home/user/workspace/tbe-multipage-approved/`
**Build type:** Clean static multi-page site — plain HTML/CSS/JS, shared `/assets/styles.css` + `/assets/site.js`, folder routes (`/about/index.html`, etc.). No framework.
**Visual source of truth matched:** `/home/user/workspace/tbe-approved-revert/index.html` (approved luxe design).
**Status:** Complete. All 16 pages built, QA passed, git committed. NOT deployed/published/pushed (per instructions).

---

## How to run / regenerate

- **Local preview:** from the project root, `python3 -m http.server 8099` then open `http://localhost:8099/`.
- **Regenerate pages after editing partials/generator:** `python3 build/generate.py` (run from project root). HTML pages are produced by `build/partials.py` (shared head/header/footer/nav/SVGs/sections) + `build/generate.py`.
- **Logos:** copied from the official uploaded asset set; `assets/logo-reversed.svg` is used in the header and footer (dark surfaces); horizontal/icon/stacked variants are also present.

---

## 16 routes (each a folder with `index.html`)

1. `/` — Home
2. `/about/` — About / founder
3. `/hope-journey/` — The H.O.P.E. Journey (The Method)
4. `/hope-curriculum/` — The H.O.P.E. Curriculum (The Method)
5. `/hope-beats/` — The Four H.O.P.E. Beats (The Method)
6. `/experiences/` — Experiences hub
7. `/empowerment-brunch/` — Empowerment Brunch
8. `/carry-on-workshops/` — Carry On Workshop
9. `/her-retreats/` — HER Retreats
10. `/podcast/` — The Podcast
11. `/hope-shop/` — The H.O.P.E. Shop  (path is `/hope-shop` exactly)
12. `/exchange-house/` — The Exchange House
13. `/corporate-experiences/` — Corporate Experiences (Bring Us In)
14. `/community-engagement/` — Community Engagement (Bring Us In)
15. `/certification-licensing/` — Certification or Licensing (Bring Us In)
16. `/contact/` — Contact

**Navigation model:** Home · About · The Method ▾ (Journey / Curriculum / Four Beats) · Experiences ▾ (Hub / Empowerment Brunch / Carry On Workshop / HER Retreats / Podcast / H.O.P.E. Shop / Exchange House) · Bring Us In ▾ (Corporate / Community / Certification or Licensing) · Contact · gold **Begin Your Exchange** button. Dropdowns open on hover and click; mobile uses a drawer toggled by the menu button.

---

## Constraint compliance (verified)

- **Button text** is exactly `Begin Your Exchange` (present on all 16 pages).
- **H.O.P.E. Shop path** is `/hope-shop` exactly.
- **H.O.P.E. Bag** is NOT a nav item, shop product, or standalone page. No `/hope-bag/` directory exists (it correctly 404s). The Bag appears only as the recurring takeaway moment ("every in-person lane sends you home with a H.O.P.E. Bag™").
- **Passport** is a recurring moment (a content section), not a standalone page or account system.
- **About structure:** Founder and Origin / The roots / The invitation, with sign-off "Dr. Shukairo Baker, DNP / Founder, THE Baggage Exchange".
- **No fabricated identity language** ("a Black woman" / "a trauma survivor") appears anywhere in body copy. (Those phrases appear only inside the gap-note HTML comment describing what was NOT found — see Copy Gap below.)
- **Footer** on every page: brand blurb, contact details, and the trademark/IP line `THE BAGGAGE EXCHANGE ™ — THE Baggage Exchange and the H.O.P.E. system are trademarks of The Baggage Exchange LLC.` plus the full IP note.
- **Contact details present:** 704.312.2777, 1.844.505.3848, hello@thebaggageexchange.org (general), podcast@thebaggageexchange.org (media/podcast).
- **Voice:** active, warm, direct. No emojis, no hashtags. Exact approved copy was not rewritten.
- **Forms:** static front end with accessible labels. On submit, the handler shows a friendly note that the form is NOT connected to a server and to email hello@thebaggageexchange.org. No backend submission is claimed.

---

## Page-specific notes (verified content)

- **Podcast:** "LAUNCHING ON SPOTIFY JULY 1"; podcast@thebaggageexchange.org labeled for media/podcast.
- **Exchange House:** faded dusty-rose lane with a "Coming soon" badge and "Working toward Summer 2027".
- **Experience lane tag colors:** brunch = soft gold, workshops = sage, HER = deep plum, podcast = cream, shop = warm sand, Exchange House = dusty rose.

---

## ⚠️ Copy gap — needs the user (IMPORTANT)

The exact **longer founder/origin story** (the version containing personal identity language such as "a Black woman" and "a trauma survivor") was **NOT found** in the approved workspace sources or in memory. To avoid fabricating sensitive personal details, the About page uses:
- the exact approved short starter ("This brand was created for people who are ready to name what they have carried, set down what no longer serves them, and walk forward with H.O.P.E."),
- the required section structure and sign-off,
- approved-source-only supporting language (survivor + doctorally prepared nurse practitioner; rooted in the Carolinas and Black women).

An HTML comment `ABOUT_LONG_COPY_NEEDED_FROM_USER` is placed in `about/index.html` immediately before the three story sections, explaining exactly what to replace. **Action for user:** supply the exact longer founder story text; drop it into those three sections, replacing the placeholder body copy. Do not invent details.

---

## QA results (PASS)

Performed with the local server + Playwright at desktop 1440 and mobile 390.

- All 16 routes load; `/hope-bag/` correctly 404s.
- No console errors on any tested page.
- Reversed logo renders in header and footer.
- "Begin Your Exchange" gold button present on every page.
- Nav dropdowns expand on hover and click; mobile drawer opens/closes.
- Contact form shows the static-form note (no fake backend claim).
- Exact approved copy verified on the correct pages; footer trademark + IP note present on all pages.

**Bug found and fixed during QA:** scroll-reveal sections could remain at `opacity:0` on full-page renders / fast scroll if the IntersectionObserver never fired for off-screen elements (large blank bands). Fixed by (1) defaulting `.reveal` to visible and only arming the animation via `html.anim` added by JS when motion is allowed and `prefers-reduced-motion` is not set, and (2) adding a JS failsafe that reveals any remaining `.reveal` elements after 2.5s. Re-verified: 0/24 reveal elements remain hidden on desktop and mobile home; full-page screenshot shows every section rendered.

QA screenshots are in `qa_shots/` (e.g. `_final_home_desktop.png`, `_final_home_mobile.png`, plus per-page desktop/mobile shots and header/dropdown/mobile-menu crops).

---

## Git

- Repo initialized in this folder. Commits:
  - `ef2e253` — Build all 16 TBE pages: shared assets, nav model, approved luxe components
  - `dcd7b6b` — QA fix: render reveal content by default + JS failsafe so no section stays hidden; add final QA shots
- user.email = `build@local`, user.name = `TBE Build`.
- NOT pushed to any remote. NOT deployed/published.

---

## Design tokens (in `assets/styles.css`, from approved source)

`--plum:#4D1A33; --plum-deep:#3A1226; --cream:#FBF5EC; --sand:#E3C6A0; --gold:#D9A93C; --espresso:#21160F; --sage:#6F9072; --rose:#C5746E;`
Gold-metal gradient `#F0D27A → #D4A53C → #A9781F`. Fonts: Playfair Display (display), Mulish (body), Space Mono (mono/eyebrows) — loaded via Google Fonts links preserved from the approved source.

---

## Suggested next steps (for the parent agent / user)

1. Provide the exact longer founder story to fill the About `ABOUT_LONG_COPY_NEEDED_FROM_USER` gap.
2. Parent agent may deploy a separate preview of this folder (this subagent did not deploy, per instructions).
3. Optionally wire the contact/lead forms to a real backend or form service before launch (currently static + mailto fallback by design).

## Preview deployment fix

After initial private-preview validation, generated HTML links were converted from root-absolute paths to relative paths so the site loads correctly under path-based private preview URLs. This changed only files inside this separate project folder.

## Direct file preview route fix

Internal route links now point directly to each route folder’s `index.html` file because the private direct-file preview host does not resolve directory indexes for relative route URLs.
