# BWF Website Update Plan — Source Cutover + Content Legibility
**Date:** 2026-08-23 | **Status:** Locked, amended 2026-08-30 (phase C2 added; cutover re-sequenced)

## Decisions carried in (locked, prior sessions)
- Light fork build path: server-rendered series-nav in forked `home.hbs` + one partial; tokens/fonts in Code Injection; series URLs via channel routes, never collections. (2026-06-01)
- Card set of six: Operational Learning, Data Done Right, Across the Divide, Real Talk to Real Results, plus gated arc cards Architecture That Persuades and Who Pays for Clarity. Better Me: Better World held out. (2026-06-01)
- Repo state: fork at June 1 build (three-file diff, v1.0.0); the June production-readiness prompt never ran. (Confirmed 2026-08-23)
- Scope: theme cutover + content legibility pass in one push. (2026-08-23)

## Decisions made this session
- **Division of labor:** Claude Code owns theme, repo, sync, and release mechanics. The content project (here) owns all audience-facing prose under voice governance: six card descriptions, About page, homepage framing. The card descriptions are the single handoff point (they live in the theme partial).
- **Enablement artifacts ship into the repo,** version-controlled with the theme: `CLAUDE.md`, `.claude/skills/bwf-brand-system/`, `.claude/skills/ghost-deploy-qa/`, and `ghost-admin/` reference copies (Code Injection head block, routes.yaml template with VERIFY-marked slugs).
- **Cutover timing rule:** never within a day of a scheduled LinkedIn post that links to the site.

## Phases

**A. Claude Code Session 1 — audit, enablement, sync (Brett runs; ~1 sitting)**
Fresh clone; copy in repo-files; run the kickoff prompt. Outputs: baseline verified, enablement committed, upstream sync branch validated (gscan + brand greps), routes slugs corrected against ground truth, dry release zip, and a placeholder inventory for the card copy.

**B. Content legibility session (here; separate sitting)**
Drafted under voice skill + write-like-a-human + em-dash discipline, with the career-legibility lens from the pause-window plan (the site is the conversion surface a recruiter lands on from LinkedIn):
1. Six series/arc card descriptions (short; recognizable to a first-time reader).
2. About page rewrite (the main legibility surface; likely wants a light extraction round).
3. Homepage framing check (site title/description, CTA line) against the locked tagline.

**C. Claude Code Session 2 — apply copy, final release (short)**
Final card copy into the partial; version bump; gscan + greps; release zip.

**C2. Brand v1.2 — design + defect clearing (added 2026-08-30)**
Decided in `BWF_BRAND_v1_2_DECISIONS.md` after an audit found Brand System v1.1 was
never fully shipped: tokens absent, Newsreader never loading, the server-rendered
series-nav not deployed, and three hard rules violated live (retired teal, retired
tagline in the footer, pure white). Scope: clear the six P0 defects, then design the
OG card template and the typographic scale. Runs in parallel with B. Decided to ship
in full **before** cutover, so D now waits on this.

**D. Staging + cutover (Brett in Ghost Admin, runbook-guided)**
Upload-without-activate; preview QA per the checklist; apply routes.yaml and Code Injection; activate in a quiet window; re-run QA live; retire Solo-era injection blocks (the legacy JS series-nav above all — this also kills the retired-tagline footer leak if it lives in injection; if the tagline lives in site settings instead, fix it there at the same time). About page applies independently via Ghost Admin, any time after B.

**E. Post-cutover backlog (unchanged)**
Brand mark finalization; feature-image replacement on old posts; GitHub deploy workflow after 30 days of stability; vault inferred-entry spot checks.

## Open items and risks
- ~~The Standing Charge page live status~~ **RESOLVED 2026-08-30: live.** `/the-standing-charge/` returns HTTP 200 with correct OG title and description. No longer gates the first-comment link or the QA row.
- **June 1 output files** (full Code Injection package with the deeper rule groups; original routes.yaml; Phase 2 README): if Brett still has them, they merge into `ghost-admin/`; the regenerated head block covers fonts + tokens only and says so in its provenance note.
- **Upstream drift** (unverified): Source has likely moved past 1.7.0 and Ghost past 6.42 since June. Session 1 measures it; a restructured upstream homepage is the one thing that could re-open build decisions.
- **Content pass scope creep:** the About rewrite is the piece most likely to grow. If it wants to become a positioning essay, it gets cut back; it is a conversion surface, not an article.

## Sequence sketch (indicative, not committed)
Week of 8/24: Session 1 (A) any evening; content session (B) midweek; Session 2 (C) after copy locks. Cutover (D): weekend window 8/29–30, clear of the Tuesday and Thursday posts.
