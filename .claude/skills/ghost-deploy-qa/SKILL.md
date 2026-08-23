---
name: ghost-deploy-qa
description: The release runbook for the bwf-source Ghost theme — upstream sync, gscan validation, release zip build, upload-without-activate staging, the pre-cutover QA checklist, activation, and rollback. Use this skill for ANY release-adjacent work: syncing the fork against a new Ghost Source version, building or verifying a theme zip, preparing for or executing a theme cutover on brettwfarmer.com, running QA against a Ghost preview, or rolling back a bad activation. If the task mentions "release", "upload", "cutover", "sync fork", "gscan", or "go live", read this skill before acting.
---

# bwf-source Deploy and QA Runbook

The site is on **Ghost Pro** (managed hosting; no server access, no separate staging site). Staging is done with Ghost's **upload-without-activate + preview** flow. The live theme stays active until explicit activation, and the previously active theme remains installed as the instant rollback.

## 1. Sync against upstream Source

```bash
git fetch upstream                      # upstream = https://github.com/TryGhost/Source.git
git checkout -b update-source-<version>
git merge upstream/main                 # confirm upstream default branch name first
```

Conflicts should ONLY appear in `home.hbs` and `package.json`:
- `home.hbs`: keep the `{{> "components/series-nav"}}` include line.
- `package.json`: keep name `bwf-source`; bump the version.

If any other file conflicts, the fork has drifted; stop and report before resolving.

After merge, diff-check the three-file discipline:

```bash
git diff upstream/main --stat           # should show only the three intended files
```

## 2. Validate

```bash
npx gscan .                             # must pass clean, Ghost 6.x compatible
```

Then the brand greps (all must return nothing):

```bash
grep -rn "4A8A7A\|FFFFFF\|000000" --include="*.hbs" --include="*.css" . | grep -v node_modules
grep -rn "Real Talk. Real Strategy\|Down to the Hardware" . | grep -v node_modules
```

(Stock Source CSS may legitimately contain #fff/#000 values; the grep gate applies to files this fork touches. Anything in the three-file diff or new files must be clean.)

## 3. Build the release zip

```bash
VERSION=$(node -p "require('./package.json').version")
zip -r "bwf-source-${VERSION}.zip" . -x "node_modules/*" ".git/*" ".claude/*" "ghost-admin/*" "*.zip"
```

The zip must NOT contain: node_modules, .git, .claude, ghost-admin, routes.yaml, or any Code Injection file. Verify by listing the zip before handing it over.

## 4. Stage (Brett performs in Ghost Admin; guide, do not do)

1. Ghost Admin > Settings > Design & branding > Change theme > Upload theme. Upload the zip. **Do not activate.**
2. Use the preview link on the uploaded theme to review before activation.
3. Code Injection (Settings > Code injection): apply/verify the head block from `ghost-admin/code-injection-head.html`. This can be applied before cutover; it is token- and font-scoped and safe under the old theme only if reviewed for selector collisions first. Default: apply at cutover.
4. routes.yaml (Settings > Labs > Upload routes file): apply `ghost-admin/routes.yaml` at cutover. Channel routes only; never collections.

## 5. Pre-cutover QA checklist (run against preview)

- [ ] Homepage renders: header, CTA, series-nav row, post feed, footer.
- [ ] Series-nav row shows the six-card set with correct series accents; the two arc cards render (their tags now hold 3+ posts) and the gate logic is still present in the partial.
- [ ] No placeholder copy anywhere in the row.
- [ ] Newsreader on headings, DM Sans on body (inspect computed styles).
- [ ] Token colors applied: bg #040A1C, surface #0D1220, text #E8E6E0; links steel.
- [ ] No teal #4A8A7A anywhere (inspect series cards especially, the Solo-era Across the Divide card was teal).
- [ ] Footer contains no retired tagline ("Real Talk. Real Strategy. Real Results.").
- [ ] Spot-check 5 existing article URLs (flat `/{slug}/`): all resolve, no redirects, correct styling.
- [ ] Series channel URLs from routes.yaml resolve and list the right posts.
- [ ] Responsive at Source's real breakpoints: 767 / 991 / 1199 px (4-up grid drops to 3 at <=1199, stacks at <=767).
- [ ] Post page: images, pull quotes, sources sections render acceptably.
- [ ] OG meta present on homepage and a sample article.
- [ ] No console errors.

## 6. Cutover

- Pick a quiet window: never within a day of a scheduled LinkedIn post that links to the site.
- Activate the theme, apply routes.yaml and Code Injection if not already applied, then re-run the QA checklist against the live site.
- Retire the Solo-era Code Injection blocks that the theme now carries natively (the legacy JS series-nav row above all); confirm against `ghost-admin/` reference copies what stays.

## 7. Rollback

The previous theme (Solo) remains installed. Rollback = re-activate Solo in Design settings and restore the prior Code Injection contents (keep a saved copy of the pre-cutover injection before changing anything). Practice rule: never edit the live injection without first copying its current full contents into a dated file in `ghost-admin/`.

## 8. After 30 days of stability

Revisit the deferred GitHub deploy workflow (GitHub as theme source with manual deploy). Not before.
