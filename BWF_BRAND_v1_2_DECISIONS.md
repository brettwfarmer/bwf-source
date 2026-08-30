# Brand System v1.2 — Decision Record

**Date:** 2026-08-30 | **Status:** Decided, not yet implemented
**Supersedes:** nothing. v1.1 remains the token authority until v1.2 ships.
**Authority note:** `BWF_Brand_System_v1_1.docx` is the stated authority and the
brand skill defers to it on conflict. Every decision below must be reflected there,
or the document and the skill will disagree.

---

## 1. Why this record exists

The trigger was "a new site needs a new brand system." The audit that followed
changed the premise: **Brand System v1.1 was never fully shipped.** The decision is
therefore to *finish and evolve* v1.1 as v1.2, not to replace it.

### What is actually live on brettwfarmer.com (Ghost 6.61, audited 2026-08-30)

| v1.1 element | Live status |
| --- | --- |
| Palette (#040A1C, steel, amber, bronze) | Live, but hard-coded hex in the legacy injection |
| Nine-token `--color-*` system | NOT deployed — zero tokens present |
| Newsreader headings | NOT loading — headings render Noto Sans |
| DM Sans body | Font loads, but `--gh-font-body` resolves to Noto Sans |
| Server-rendered series-nav | NOT deployed — still the legacy JS injection |

### Live violations of v1.1 hard rules

1. Retired teal `#4A8A7A` styles the Across the Divide cards (3 rules: border, hover, title).
2. Retired tagline "Real Talk. Real Strategy. Real Results." renders in the footer `gh-copyright` div.
3. Pure `#FFFFFF` appears in the injected styles.

## 2. Decisions

- **Scope: evolve v1.1 into v1.2.** Keep the bones — dark ground, steel/amber/bronze,
  the locked tagline. Add the expression that was never specified.
- **Goals, all four in scope:** LinkedIn click-through, recruiter conversion,
  time on site / depth, subscriber growth.
- **The three-file fork rule holds.** Series-aware "Read next" would require editing
  `post.hbs`. Rejected for now: enable Source's generic related-articles first and
  measure, then spend the fork-discipline budget only if generic does not move depth.
- **Full v1.2 ships before cutover.** One disruption rather than two. Cutover slips;
  Phase B copy and v1.2 design proceed in parallel.

## 3. P0 — defects, not design

Do these regardless of v1.2 scope. No design work involved.

| # | Item | When | Notes |
| --- | --- | --- | --- |
| 1 | Remove the retired teal (3 rules) | Interim, optional | Lives in the Solo-era injection. Dies at cutover when that block is deleted |
| 2 | Remove retired tagline from footer | Interim, optional | Server-rendered by Solo in `gh-copyright`. bwf-source's footer has no tagline, so cutover resolves it |
| 3 | **Make Newsreader actually load** | Interim or cutover | New injection below does it. The serif/sans pairing IS the identity and it is absent |
| 4 | Homepage OG 1024x1024 -> 1200x627 | **Now** | Site-level, theme-independent, permanent. The only item that is unambiguously do-it-today |
| 5 | Enable `show_related_articles` | **Cutover** | A bwf-source custom setting. Cannot be set until the theme is activated |
| 6 | Set `signup_heading` / `signup_subheading` | **Cutover** | Also bwf-source custom settings. Same constraint |

**Sequencing correction (2026-08-30):** items 5 and 6 were initially listed as
immediate Ghost Admin tasks. They are custom settings defined in this theme's
`package.json`, not Ghost core, so they do not exist in Admin until bwf-source is
uploaded and activated. Items 1-3 are interim hygiene on a theme being retired;
they resolve automatically at cutover. Only item 4 is both immediate and permanent.

Item 3 carries the most weight. Judge v1.1 only after seeing it actually render.

## 4. P1 — what v1.2 adds

### 4.1 OG card template — **BUILT 2026-08-30** (LinkedIn CTR)
Delivered in `ghost-admin/og-template/`: a parameterized HTML card plus a Chrome
render script, producing 1200x627 PNGs uploaded as post feature images. Series
accent stripe, title in Newsreader, auto step-down to fit three lines. Fonts are
vendored locally because fetching them at render time is a race that silently
yields the fallback serif.

### 4.2 Typographic scale — **BUILT 2026-08-30** (depth)
Delivered in the injection. Drives Source's own `--content-font-size` (1.7rem ->
1.9rem) and `--content-width` (720px -> 680px, about 72 characters), plus leading,
tracking, in-content heading steps, excerpt, and an accented blockquote. Verified by
rendering against Source's real screen.css. No theme release required.

### 4.3 Portal and CTA styling — **BUILT 2026-08-30** (subscriber growth)

**Portal itself is not styleable.** It renders into an iframe injected at runtime by
`portal.min.js`; no Code Injection CSS reaches inside. Its only lever is the accent
color (Ghost Admin > Design), already steel `#7EB3CC` and on-brand, plus Portal copy
in Admin. The original plan to "style Ghost Portal to the token system" was not
achievable as written.

What was styled instead - the theme's own conversion surfaces, which is where the
reader is before Portal ever opens. Three defects found and fixed:

1. **Subscribe button failed WCAG AA.** Source sets `color: var(--color-white)` over
   the accent background: pure white on steel measures **2.28:1**, against the 4.5:1
   floor the brand system sets. Now `--color-bg` on steel, **8.64:1**. The fix had to
   invert rather than substitute - the brand's own light text token is worse at 1.83:1.
2. **No keyboard focus indicator.** Source sets `outline: none` on `.gh-form-input`
   and never replaces it anywhere in the stylesheet (WCAG 2.4.7). A `:focus-within`
   ring now sits on the form shell, since the input is positioned to fill it.
3. Form and CTA containers moved onto the token surfaces with explicit borders.

**Resolved 2026-08-30 - not a defect.** An earlier reading of this called the
hidden homepage CTA a subscriber-growth gap and the highest-value open question in
v1.2. That was wrong. `cta.hbs` renders only when `header_style` is not
Landing/Search/Off, and `screen.css` shows `.gh-cta` only for `is-highlight` or
`is-magazine` - but the Landing layout renders its own `email-subscription` form
*and* an `<h1>` carrying `header_text` (falling back to `@site.description`) above
the fold. Source suppresses the mid-page CTA on Landing precisely because it would
duplicate that form. `email-subscription` appears in exactly three places: the
Landing header, the CTA block, and the footer.

Switching to Highlight was considered and rejected on 2026-08-30. Highlight's three
columns are all post cards, so it renders neither the tagline `<h1>` nor a header
signup; it trades an above-the-fold form for a mid-page one and drops the identity
statement a cold recruiter needs. That moves recruiter conversion and subscriber
growth backwards to buy a denser front page. **`header_style` stays Landing**, and
no `package.json` change is needed.

**Handed to Phase B:** `header_text` is the actual above-the-fold lever. It is a
theme custom setting (Ghost Admin > Design > theme settings), currently unset, so
the `<h1>` falls back to `@site.description` - the locked tagline. Whether the
tagline is the right H1 for a cold recruiter, or whether a purpose-written line
should sit there, is a copy decision under voice governance, not a brand one.
