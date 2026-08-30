# CLAUDE.md — bwf-source

This repository is the production theme for **brettwfarmer.com**, a Ghost Pro publication. It is a **light fork of Ghost Source** (forked at Source v1.7.0). The entire value of this fork is that its diff from upstream stays tiny, so upstream Source updates merge cheaply. Protect that property in every change.

## What this fork is

Only three files are intended to differ from stock Source:

1. `partials/components/series-nav.hbs` — NEW. A server-rendered "Explore the Series" card row. It deliberately replaces a legacy Code Injection JS row that could break silently.
2. `home.hbs` — ONE added line including the partial, between the CTA and the main post list: `{{> "components/series-nav"}}`
3. `package.json` — name `bwf-source`, version, description.

If you find yourself changing a fourth file, stop and justify it. The default answer is no.

This three-file rule governs **theme files** — everything that ships in the release zip. Repo-level metadata that Ghost never sees (`CLAUDE.md`, `README.md`, `.gitignore`, `.claude/`, `ghost-admin/`) sits outside it. Verify the theme diff with:

```bash
git diff upstream/main --stat -- . ':!CLAUDE.md' ':!README.md' ':!.gitignore' ':!.claude' ':!ghost-admin'
```

## Hard constraints (never violate)

- **Series page URLs use routes.yaml CHANNEL routes, never Ghost collections.** Collections re-home every post and break existing permalinks. Existing article URLs are flat (`brettwfarmer.com/{slug}/`) and must stay working. Never convert to collections.
- **Brand tokens and fonts live in Ghost Code Injection, not the theme.** Do not move colors, fonts, or brand CSS into theme files. This is deliberate: brand changes must never require a theme release. Reference copies live in `ghost-admin/` in this repo, but they are applied by hand in Ghost Admin.
- **routes.yaml is not a theme file.** A reference copy lives in `ghost-admin/`; it is uploaded in Ghost Admin > Settings > Labs.
- **Retired teal `#4A8A7A` appears nowhere.** Not in code, not in comments, not in examples.
- **The retired taglines appear nowhere:** "Real Talk. Real Strategy. Real Results." and "Down to the Hardware" are both retired brand language.
- **The two arc cards are gated.** "Architecture That Persuades" and "Who Pays for Clarity" render only when their tag holds at least 3 published posts (via `{{#get}}` count in the partial). Keep the gate even though both arcs currently satisfy it; it is the correct behavior for future arcs.
- **Never pure white (#FFFFFF) or pure black (#000000)** anywhere in any styling you do touch. Text on dark uses `#E8E6E0`; darkest value is `#040A1C`.
- `npx gscan .` must pass clean for Ghost 6.x before any release zip is built.

## Where the knowledge lives

- `.claude/skills/bwf-brand-system/` — the full brand token system, typography, series accent mapping, and visual rules. Read it before touching anything visual. The authority it distills is **v1.1.1 (July 2026)**, which is Markdown despite its `.docx` name; the valid `.docx` on the Desktop is the older v1.1.
- `BWF_BRAND_RECONCILIATION.md` — where this repo and the authority document disagree, and the six open decisions that follow. Read it before citing the brand system as settled.
- `.claude/skills/ghost-deploy-qa/` — the upstream-sync, build, staging, QA, and cutover runbook. Read it before any release work.
- `MAINTENANCE.md` — the original fork-maintenance procedure (superset absorbed into the deploy skill; kept for history).
- `ghost-admin/` — reference copies of Code Injection and routes.yaml as applied (or to be applied) in Ghost Admin.

## Working conventions

- US English spelling everywhere.
- Do not push, open PRs, or touch the live Ghost site without an explicit go-ahead from Brett. Stop at review checkpoints.
- When syncing upstream, conflicts should only ever appear in `home.hbs`, `package.json`, and `README.md`. Keep the series-nav include line; keep the `bwf-source` name; bump version; resolve `README.md` as ours (this fork's README replaces Source's, so upstream README edits conflict by design and are always discarded).
- Anything you cannot verify from this repo, the live site, or Brett directly gets flagged as unverified, not assumed.
