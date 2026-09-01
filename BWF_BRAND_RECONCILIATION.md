# Brand System Reconciliation — repo vs. authority document

**Date:** 2026-08-30
**Reconciles:** `.claude/skills/bwf-brand-system/`, `CLAUDE.md`, the v1.2 decision
record, and the shipped injection against the authority document.

---

## 0. The authority is v1.1.1, not v1.1

Everything in this repo cites `BWF_Brand_System_v1_1.docx`. There are two files
with that name and they are not the same document:

| Path | Real format | Version | Date |
| --- | --- | --- | --- |
| `~/Desktop/Consulting/BWF_Brand_System_v1_1.docx` | Word (valid .docx) | **v1.1** | April 2026 (mtime May 9) |
| `~/Desktop/Consulting/Folders/BWF_Brand_System_v1_1.docx` | **Markdown text**, misnamed `.docx` | **v1.1.1** | **July 2026** (mtime Jul 5) |

The newer document is v1.1.1 and carries an amendment the repo has never seen:

> *v1.1.1 amendment (proposed 2026-07-05): Section 4.3 gains a concrete-subject
> composition exception when brand treatment is held constant.*

It also adds a **sixth** entry to Section 5.4 Series Visual Language, for
Architecture That Persuades, marked *"Locked 2026-05-25 with The Diagram That
Stayed; inherits across all five Arc 1 pieces."*

**Action:** rename the July file to `BWF_Brand_System_v1_1_1.md` so its format and
version are honest, and repoint the skill and `CLAUDE.md` at it. Until then, any
agent reading "the docx" reads a five-month-old revision.

---

## 1. The skill misread the authority — Real Talk to Real Results

The skill states:

> **Open gap:** *Real Talk to Real Results* is an always-on series card with no
> accent lead defined in this table.

**That is wrong.** Section 2.2 has a row for it in both v1.1 and v1.1.1:

| Series | Lead accent | Rationale |
| --- | --- | --- |
| Real Talk to Real Results | **Balanced steel + amber** | Equal weight. The broadest series, using the full warm/cool tension without favoring either. |

The gap was in the distillation, not the source: the skill's table shape holds one
hex per series and could not represent "balanced," so the row was dropped and
recorded as missing.

**Consequence.** On 2026-08-30 this session ratified Real Talk to Real Results as
amber `#D4943A` on the reasoning that the accent was undefined. It was not. The
authority says balanced steel + amber.

In fairness to the decision: a single `--bwf-accent` on a nav card cannot express
"balanced," and Section 2.2 predates that surface existing. Amber is a defensible
*implementation* of a spec that never contemplated a one-hex card accent. But it
was decided on a false premise and must not stand as "ratified" without a ruling.

**Needs a decision — see Section 5, item 1.**

---

## 2. Implementation deviations from the authority

Found by checking the shipped injection and OG template against v1.1.1 directly.

| # | Authority says | We shipped | Severity |
| --- | --- | --- | --- |
| 2.1 | §3.3 Body text 17-18px, line-height 1.65 | 19px, line-height 1.65 | Leading matches exactly; size is 1px over the stated range |
| 2.2 | §3.3 Article subheads (H2/H3) Newsreader Regular 22-26px | h2 30px, h3 24px | h2 is 4px over range |
| 2.3 | §3.3 Article headlines Newsreader Medium 30-36px | Source's clamp, 34-46px, not overridden | Top of range exceeded by 10px |
| 2.4 | §4.4 Pull quotes: Newsreader Regular 24px, *italic*, `--color-text-primary`, **4px** left border in accent-primary, 24px indent | 3px border, `--color-text-secondary`, `font-style: normal`, no size set | Four deviations in one rule |
| 2.5 | §4.2 Social post title in Newsreader **Medium (500)** | OG card uses Newsreader **SemiBold (600)** | Wrong weight; only 600 was vendored |
| 2.6 | §3.5 Type variables rebound in **Site Footer** injection | All in Site Header injection | Header is correct practice (avoids FOUC); the document is behind |
| 2.7 | §4.5 Focus state: 2px outline in accent-primary, 2px offset | Exactly that | **Matches.** Worth noting Source shipped no focus state at all, so this was a spec violation before we fixed it |

Deviations 2.1-2.3 are all in the same direction: the shipped scale runs larger
than the document specifies. That may be right — the document's sizes were written
before anyone read Newsreader on this ground at these measures — but it is a
deliberate divergence, not a match, and the document should say so either way.

---

## 3. Problems inside the authority document itself

### 3.1 Bronze fails the document's own accessibility floor

§4.5 sets *"Inline accents (links, emphasis): minimum 4.5:1"* with no large-text
exemption. Measured against `--color-bg` `#040A1C`:

| Token | Ratio | §4.5 requires | Result |
| --- | --- | --- | --- |
| `--color-text-primary` #E8E6E0 | 15.79:1 | 7.0 (AAA body) | PASS |
| `--color-text-secondary` #B0ADA6 | 8.80:1 | 4.5 | PASS |
| `--color-text-muted` #8A8880 | 5.55:1 | 4.5 | PASS |
| steel #7EB3CC | 8.64:1 | 4.5 | PASS |
| amber #D4943A | 7.60:1 | 4.5 | PASS |
| **bronze #A86A28** | **4.47:1** | 4.5 | **FAIL by 0.03** |

Bronze is Across the Divide's lead accent. On the series card the name renders at
19px/700, which qualifies as WCAG large text and needs only 3:1 — so the live
rendering is compliant under WCAG. It is the *document's own stricter rule*, stated
without a large-text carve-out, that bronze misses. Either the rule gains that
carve-out or bronze needs lightening.

### 3.2 Feature image and social card specs contradict each other

- §4.3: feature images are **3:2**, abstract architectural form, **"No text
  overlaid... The title comes from Source's post layout."** They serve as *"both
  the Source post card and the social sharing preview."*
- §4.2: LinkedIn post images are **1200 x 627**, **with** title text in Newsreader.

Ghost allows one feature image per post and derives `og:image` from it. So a post
cannot simultaneously have a 3:2 untitled feature image serving as the social
preview and a 1200x627 titled social card. 3:2 is 1.5:1; the `summary_large_image`
card wants 1.91:1, so a compliant §4.3 feature image is letterboxed or cropped in
the LinkedIn feed — the same defect class as the current square homepage card.

**This directly affects the OG template built on 2026-08-30.** That template
produces a titled 1200x627 card and its README instructs uploading it as the post's
feature image. That satisfies §4.2 and violates §4.3. The template is not wrong; the
document has two incompatible rules and the template picked one without knowing.

**Needs a decision — see Section 5, item 2.**

### 3.3 Section 4.4 is specified but unimplemented

The document specifies six long-form structural devices in detail - soft anchors,
pull quotes, principle callouts, comparison tables, code blocks, footnotes and a
Sources section - and §6 Phase 2 lists them as required Code Injection work. **None
are implemented.** The shipped injection covers tokens, fonts, the type scale and
conversion surfaces only.

The 2026-06-01 injection package that reportedly carried them was searched for on
2026-08-30 across Downloads, Desktop and Documents and does not exist on this
machine. It is lost, not misplaced. Everything in §4.4 is specified precisely enough
to rebuild from the document, so nothing is blocked - but it is unbuilt work, and it
is the largest remaining gap between the document and the site.

### 3.4 v1.2 was anticipated and has arrived

§2.1: *"Note on warning and success colors: not yet tokenized. They will be added
in v1.2 if member portals or interactive forms enter scope."*

Interactive forms entered scope on 2026-08-30 with the conversion-surface work.
The form carries a `data-members-error` element that currently has no token.
v1.2 should tokenize warning and success.

---

## 4. Content finding: Arc 1 is written but untagged

§5.4 of v1.1.1 says Architecture That Persuades *"inherits across all five Arc 1
pieces."* The Content API shows five matching posts, all published, **all carrying
zero tags**:

| Published | Title |
| --- | --- |
| 2026-05-31 | Architecture that Persuades: The Diagram That Stayed |
| 2026-06-07 | Maps That Decide |
| 2026-06-14 | Architecture That Persuades: Still Running |
| 2026-06-21 | Architecture That Persuades: The Date That Held |
| 2026-06-28 | Architecture That Persuades: Drawn Clean |

This explained the 2026-08-30 routes finding: the tag did not exist, so the
`{{#get}}` gate hid the card and the route was commented out — but the *content* had
existed since May and the brand system locked its visual language on 2026-05-25. The
arc was not unready. It was untagged.

**RESOLVED 2026-08-30.** The tag `architecture-that-persuades` was created and
applied via the Admin API to the **four prefixed posts**. Maps That Decide was
excluded by decision — it carries no title prefix, so it is treated as a standalone
rather than Arc 1's fifth piece. Verified through the Content API afterwards: tag
exists, public, 4 published posts, clearing the >= 3 gate. The card renders and
`/architecture-that-persuades/` is re-enabled in `routes.yaml`.

**Note for the document:** §5.4 says the arc's visual language "inherits across all
five Arc 1 pieces." Only four are tagged. Either the fifth is Maps That Decide and
the count needs the prefix decision revisited, or §5.4's count is wrong.

Broader: **9 of 74 posts (12%) still carry no public tag**, down from 23. Ten more
were tagged on 2026-08-31 per `TAGGING_PROPOSAL.md`, which also created the Who Pays
for Clarity arc. The nine that remain are Tier 4 there: three pre-series foundational
posts and six that resist single-series mapping.

---

## 5. Decisions needed

1. **Real Talk to Real Results accent.** The authority says "balanced steel +
   amber"; the card shipped amber. Either (a) confirm amber for the card surface
   and amend §2.2 to say so, or (b) revert the card and define what "balanced"
   means for a one-hex accent. Recommend (a) - the constraint is real and the
   document did not anticipate this surface.
2. **Feature image vs social card.** §4.3 and §4.2 cannot both hold. Either
   (a) feature images become titled 1200x627 cards, amending §4.3, or (b) feature
   images stay 3:2 untitled art and the OG template's output becomes a separate
   asset posted directly to LinkedIn rather than uploaded to Ghost.
3. **Bronze contrast.** Add a large-text carve-out to §4.5, or lighten bronze.
4. **Type scale divergence.** Ratify the larger shipped scale in §3.3, or bring the
   injection back to the documented sizes.
5. **The Mark.** §4.6 requires the mark deployed *with* cutover in Phase 4. The
   plan of record lists mark finalization as post-cutover backlog. These conflict.
6. ~~Arc 1 tagging~~ **DONE 2026-08-30** — four posts tagged, card and route live.
   Residual: §5.4 claims five Arc 1 pieces; four are tagged. See section 4.
