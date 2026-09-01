# Untagged Post Backlog — Proposed Series Mapping

**Date:** 2026-08-30 | **Status:** Tiers 1-3 APPLIED 2026-08-31. Tier 4 still open.
**Scope:** the 19 posts carrying no public tag, of 74 published.

Apply with `ghost-admin/tools/tag_posts.py` (dry-run by default).

---

## Tier 1 — Conclusive (6 posts). **APPLIED 2026-08-31.**

Evidence is the post's own title, or an exact gap in an unbroken weekly cadence.

### -> `real-talk-roundup` (existing tag, 6 posts)

| Published | Title |
| --- | --- |
| 2025-10-15 | Real Talk Roundup - October 15, 2025 |
| 2025-11-05 | Real Talk Round Up - November 5, 2025 |
| 2025-12-16 | Real Talk Roundup - December 16, 2025 |
| 2026-03-31 | Real Talk Roundup - March 31, 2026 |

The title *is* the series name. Note "Round Up" is spelled as two words on the
2025-11-05 post; that is a title inconsistency worth fixing separately, but it does
not affect tagging.

### -> `operational-learning` (existing tag, 10 posts)

| Published | Title |
| --- | --- |
| 2026-04-26 | Operational Learning: The Politics of Friction |
| 2026-05-10 | Operational Learning: The Polite Lie |

Explicit title prefix, and they fill the only two gaps in the series' weekly run.
Tagged OL posts land on Mar 1, 8, 15, 22, 29, Apr 5, 12, 19, May 3, 17 — missing
exactly Apr 26 and May 10, which is where these two sit. Conclusive.

## Tier 2 — Strong (1 post). **APPLIED 2026-08-31.**

### -> `decision-system` (existing tag, 9 posts)

| Published | Title |
| --- | --- |
| 2026-01-04 | Data that Decides |

The decision series runs weekly from 2025-12-07 to 2026-02-08 with exactly one gap:
2026-01-04. This post fills it, and its excerpt — "Trusted numbers to repeatable
calls: the operating system behind real outcomes" — matches the series' subject.
Short of conclusive only because it lacks the "Decision X:" title prefix every
other member carries.

## Tier 3 — Hypothesis (3 posts). **APPLIED 2026-08-31.** This was my reading, not the author's — see the caveat below; it stands as a thing to sanity-check against the posts.

### -> `who-pays-for-clarity` — WOULD CREATE THE TAG AND LIGHT UP ARC 2

| Published | Title | Excerpt |
| --- | --- | --- |
| 2026-07-26 | The Double Bill | "The person who had been catching everything quietly got the bill, twice." |
| 2026-08-09 | The Unmeasured Advantage | "The first team to become measurable pays for every team that doesn't." |
| 2026-08-16 | The Standing Charge | "The person who keeps saying the true thing ends up holding a bill no one else can see." |

All three run an explicit cost-and-payment metaphor over clarity, measurement, or
truth-telling. The arc's own card copy reads "The real cost of clarity, and who ends
up carrying it," which describes these three precisely.

**Confidence caveat, stated plainly.** Arc 1 was safe to tag because its posts
carried the series name in their titles. These do not. I searched the full text of
all eight July-August posts and **none contains the string "Who Pays for Clarity"**,
so nothing here is author-declared. This grouping is inference from theme and
publication window.

**If approved, this is consequential.** Three posts clears the >= 3 gate, so the
second arc card renders and `/who-pays-for-clarity/` can be enabled — which takes
Phase B from five card descriptions to **six**, and means both arcs ship at cutover.

Borderline, not included: **A Wrong Name Beats an Empty Box** (2026-08-03) sits in
the same weekly run and concerns naming and ownership, but its cost is implicit
rather than the explicit bill/charge/pays metaphor the other three share.

## Tier 4 — Needs your call (9 posts). **STILL OPEN — no proposal made or applied.**

These have no defensible mapping from the outside.

### Pre-series foundations (3)

| Published | Title |
| --- | --- |
| 2025-08-11 | Digital Transformation Starts at the Core - Here's Why |
| 2025-08-24 | You Don't Need a New Tool, You Need a New Mindset |
| 2025-09-14 | Getting Real About Digital Transformation: What We've Learned |

All three predate the series structure — the earliest tagged series post is Data
Done Right on 2025-08-31. They read as foundational entry points. Options: leave
untagged, or create a "Foundations" / "Start Here" tag that is deliberately not a
series card.

### Cross-series and standalone (6)

| Published | Title | Why it resists mapping |
| --- | --- | --- |
| 2025-12-31 | Closing 2025: When Agreement Stops Being the Hard Part | Year-ender on data trust. Sits 3 days after Decision Cadence, off the weekly cadence |
| 2026-06-07 | Maps That Decide | Excluded from Arc 1 by decision on 2026-08-30. Capability-map subject sits between Architecture That Persuades and the decision series |
| 2026-07-05 | The Iteration Is The Work | No series signal in title, excerpt or body |
| 2026-07-12 | Start Here If You Inherited a Function You Didn't Build | A hub essay — "these seven, in this order." Mentions Operational Learning. Probably wants "Start Here" treatment, not series membership |
| 2026-07-19 | The Words for It | Names **both** Architecture That Persuades and Operational Learning. "The names are not a glossary. They are one operating architecture, seen from above." Reads as cross-series synthesis; forcing it into one series would misrepresent it |
| 2026-08-03 | A Wrong Name Beats an Empty Box | See Tier 3 borderline note |

---

## If Tiers 1-3 are approved

- 10 of 19 posts tagged; untagged drops from 19 to 9 (26% of the archive to 12%).
- No new tags except `who-pays-for-clarity`.
- Arc 2 renders; both arc routes go live; Phase B grows to six card descriptions.
- Every slug must match `routes.yaml` and `series-nav.hbs` exactly. A mismatch does
  not 404 — it renders an empty channel and silently hides the gated card.


---

## Applied 2026-08-31

Tiers 1-3, ten posts, via `ghost-admin/tools/tag_posts.py` after a dry run.
Verified through the Content API afterwards.

| Tag | Was | Now |
| --- | --- | --- |
| operational-learning | 10 | 12 |
| decision-system | 9 | 10 |
| real-talk-roundup | 6 | 10 |
| **who-pays-for-clarity** | did not exist | **3 (new)** |

Untagged fell from 19 to **9** (26% -> 12%). All six series routes are now active
and every route's tag was re-verified live against the theme's hrefs and gates.

**Watch item.** Who Pays for Clarity sits at exactly 3 posts against a gate of 3.
There is no margin: unpublishing or retagging any one of those posts drops the count
to 2 and the arc card silently stops rendering, while `/who-pays-for-clarity/`
keeps resolving to a thin channel. The same is not true of Arc 1, which has 4.
