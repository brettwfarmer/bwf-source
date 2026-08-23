# bwf-source

The production Ghost theme for **[brettwfarmer.com](https://brettwfarmer.com)**.

This is a **light fork of [Ghost Source](https://github.com/TryGhost/Source)**, forked at Source **v1.7.0**. The point of the fork is that its diff from upstream stays tiny, so upstream Source releases merge cheaply. Exactly three files differ from stock:

| File | Change |
| --- | --- |
| `partials/components/series-nav.hbs` | **New.** Server-rendered "Explore the Series" card row, replacing a legacy Code Injection JS row. |
| `home.hbs` | One added include: `{{> "components/series-nav"}}`, between the CTA and the post list. |
| `package.json` | Theme identity — name, version, description. |

If a change would touch a fourth file, stop and justify it. The default answer is no.

## Read this before changing anything

**[`CLAUDE.md`](CLAUDE.md)** carries the hard constraints. The ones that bite hardest:

- Series pages are **routes.yaml channel routes, never Ghost collections** — collections re-home posts and break existing flat permalinks.
- **Brand tokens and fonts live in Ghost Code Injection, not the theme**, so brand changes never require a theme release.
- `npx gscan .` must pass clean for Ghost 6.x before any release zip is built.

## Layout

- `ghost-admin/` — reference copies of what is applied **by hand** in Ghost Admin: `code-injection-head.html` (Site header) and `routes.yaml` (Settings → Labs). These are not theme files and are not shipped in the release zip.
- `.claude/skills/` — `bwf-brand-system` (brand tokens, typography, series accent mapping) and `ghost-deploy-qa` (upstream sync, build, staging, QA, cutover runbook). Read the relevant one before any visual or release work.
- `MAINTENANCE.md` — the original fork-maintenance procedure, superseded by the deploy skill and kept for history. **Not currently present in this repo.**

## Versioning

Release tags are namespaced **`bwf-v*`** (e.g. `bwf-v1.0.0`). Upstream Source's own `v*` tags are present in this repo via the `upstream` remote; using the bare `v*` namespace for fork releases collides with them.

```sh
git remote add upstream https://github.com/TryGhost/Source.git   # if absent
git fetch upstream --tags
```

## Upstream

Built on [Ghost Source](https://github.com/TryGhost/Source), MIT licensed — see [`LICENSE`](LICENSE). Upstream documentation for the underlying theme lives in the [Ghost theme docs](https://ghost.org/docs/themes/).
