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

| # | Item | Owner | Notes |
| --- | --- | --- | --- |
| 1 | Remove retired teal `#4A8A7A` (3 rules) | Ghost Admin | Across the Divide takes bronze `#A86A28` |
| 2 | Remove retired tagline from footer | Ghost Admin | Lives in site settings or injection; find and kill |
| 3 | **Make Newsreader actually load** | Injection | The serif/sans pairing IS the identity and it is absent |
| 4 | Homepage OG image 1024x1024 -> 1200x627 | Ghost Admin | Square card against `summary_large_image` costs LinkedIn CTR |
| 5 | Enable `show_related_articles` | Ghost Admin | Theme defaults it true; it is off. Free depth lever |
| 6 | Set `signup_heading` / `signup_subheading` | Ghost Admin | Currently unset; falls back to site title/description |

Item 3 carries the most weight. Judge v1.1 only after seeing it actually render.

## 4. P1 — what v1.2 adds

### 4.1 OG card template — highest-leverage new work (LinkedIn CTR)
1200x627, series accent stripe, title set in Newsreader. Today the feature images are
AI-generated with no shared signature, so nothing in-feed identifies the publication
across posts. A consistent card is what makes a series recognizable while scrolling.

### 4.2 Typographic scale (depth, and everything else)
v1.1 names two fonts and stops. It defines no scale, no measure, no leading. That is
the reading-comfort gap. Pure Code Injection, so it ships without a theme release.

### 4.3 Portal and CTA styling (subscriber growth)
Style Ghost Portal to the token system. CTA copy is a Ghost setting, not theme work.

### 4.4 Recruiter conversion
Homepage above-the-fold framing and the About page. Both are Phase B copy applied in
Ghost Admin — brand supports them, it does not author them.

## 5. What v1.2 does NOT change

- The tagline. "Grounded certainty for digital transformation leaders." stays locked.
- The palette bones. Dark ground, steel / amber / bronze.
- The series accent map, including Real Talk to Real Results = amber `#D4943A`,
  ratified 2026-08-30.
- The theme. Brand tokens live in Code Injection precisely so brand changes never
  require a theme release. The three-file fork and the Phase B brief remain valid.

## 6. Consequences for the plan of record

- A new phase sits between Phase C and cutover: v1.2 design + P0 defect clearing.
- Cutover (Phase D) slips. The 8/29-30 window is gone.
- Phase B copy drafting is unaffected — v1.2 does not reopen the tagline, the
  accent map, or the card copy constraints.

## 7. Open items

- `BWF_Brand_System_v1_1.docx` must be updated to v1.2, or it will contradict the skill.
- Arc card accents remain unratified (both steel, both hidden — harmless for now).
- OG card template needs an actual design pass; nothing in v1.1 specifies one.
- The June 1 fuller Code Injection package (soft anchors, footnote/source cards,
  component styling) is still unmerged into `ghost-admin/` and may already contain
  some of section 4.
