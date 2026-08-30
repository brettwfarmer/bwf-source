# Claude Code Kickoff — bwf-source Session 1 (Audit + Enablement + Sync)

Setup before running:
1. Clone your fork locally: `git clone git@github.com:brettwfarmer/bwf-source.git && cd bwf-source`
2. Copy the `repo-files/` contents from this package into the repo root (CLAUDE.md, `.claude/`, `ghost-admin/`).
3. Start Claude Code from inside the repo and paste the fenced block.

---

```
You are in my local clone of github.com/brettwfarmer/bwf-source, a Ghost publication
theme that is a LIGHT FORK of Ghost Source (forked at Source v1.7.0). Read CLAUDE.md
in this repo root first; it carries the hard constraints. Two skills exist in
.claude/skills/ (bwf-brand-system, ghost-deploy-qa); use them.

STATE: This repo was built on 2026-06-01 and has not been touched since. A prior
production-readiness prompt was never run, so expect the June 1 state exactly:
the three-file diff from stock Source 1.7.0 (series-nav partial, one home.hbs
include line, package.json identity), tagged/released as v1.0.0. The files I just
copied in (CLAUDE.md, .claude/, ghost-admin/) are new and uncommitted.

Work in this order. STOP at each checkpoint for my review. Do not push, do not open
PRs, do not touch the live Ghost site at any point in this session.

1. VERIFY BASELINE. Confirm the three-file diff discipline holds:
   - git remote check: origin = my fork; add upstream https://github.com/TryGhost/Source.git if absent.
   - git fetch upstream, then diff against the Source v1.7.0 tag (the fork base):
     only the three intended files should differ (ignore the files I just copied in).
   - Run npx gscan . and confirm it passes for Ghost 6.x.
   - Inventory every placeholder in partials/components/series-nav.hbs (card
     descriptions, accent assignments, anything marked TBD). Report them; do NOT
     write copy for them. Final card copy comes from a separate drafting session.
   CHECKPOINT 1: report findings (diff state, gscan result, placeholder inventory,
   anything unexpected).

2. COMMIT ENABLEMENT FILES. Commit CLAUDE.md, .claude/skills/, and ghost-admin/ as
   a single commit. Add/extend .gitignore (node_modules, *.zip, .DS_Store). If no
   README.md exists beyond stock Source's, add a short one identifying the fork,
   pointing at CLAUDE.md and MAINTENANCE.md.
   CHECKPOINT 2: show the commit and any README diff.

3. UPSTREAM SYNC. Check how far upstream Source has moved past v1.7.0 (git log
   upstream/main since the fork base; check package.json version at upstream HEAD).
   Report what changed at a glance (files touched, anything overlapping home.hbs or
   the partials tree).
   - If the overlap is low risk: merge per the ghost-deploy-qa runbook on a branch
     (update-source-<version>), resolve the expected conflicts only, re-run gscan,
     and run the brand greps from the skill.
   - If upstream restructured home.hbs or partials/components/: STOP and report
     before merging anything.
   CHECKPOINT 3: report the sync result, gscan, and grep output. Do not merge the
   branch to main until I confirm.

4. ROUTES GROUND TRUTH. The ghost-admin/routes.yaml file has every tag slug marked
   VERIFY. Query the live Content API if a key is available to you, or give me the
   exact list of slugs to read out of Ghost Admin > Tags. Correct the file against
   ground truth. Do not invent slugs.
   CHECKPOINT 4: show the corrected routes.yaml and how each slug was verified.

5. RELEASE PREP (dry). Bump package.json to the next version on the sync branch,
   build the release zip per the runbook, and verify its contents (no node_modules,
   .git, .claude, ghost-admin, or zips inside). Leave it in the repo root untracked.
   CHECKPOINT 5 (end of session): summarize repo state, the zip, and exactly what
   still blocks cutover (expected: final card copy from the drafting session, plus
   the Ghost Admin staging steps which I perform by hand).
```

---

## What this session deliberately does not do

- No card copy, no About page, no prose. That is drafted under voice governance in
  the content project and handed over as final text.
- No Ghost Admin actions. Upload, injection, routes, and activation are performed
  by Brett per the ghost-deploy-qa runbook, after the copy lands.
