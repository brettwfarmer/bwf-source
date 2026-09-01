# Phase B Handoff — Series Card Copy Brief

**Prepared:** 2026-08-30, from live ground truth (brettwfarmer.ghost.io, 74 published posts, 14 tags).
**Lane:** This brief is produced by the theme lane. The copy itself is drafted in the
content project under voice governance (voice skill + write-like-a-human + em-dash
discipline), per the division of labor locked in `BWF_Website_Update_Plan.md`.
**Returns to:** the theme lane as final text, applied in Phase C.

---

## 1. Scope — four descriptions ship, not six

**Both arc tags now exist and both arcs ship.** Architecture That Persuades was
tagged on 2026-08-30 (4 posts) and Who Pays for Clarity on 2026-08-31 (3 posts);
both clear the >= 3 gate, both cards render, and both routes are active. **Scope is
six card descriptions plus `header_text`.**

Note on Who Pays for Clarity: its three posts were grouped by inference from theme,
not from anything the author declared — no post names the arc. The card copy should
be checked against the three posts rather than assumed. See `TAGGING_PROPOSAL.md`
Tier 3.

## 2. Constraints the copy must satisfy

- One sentence per card. Current lines run 45-59 characters; treat ~60 as the ceiling.
- Renders at 1.45rem in `--color-text-secondary` (#B0ADA6), beneath a 1.9rem
  accent-colored series name.
- Audience: a first-time reader, frequently a recruiter arriving from LinkedIn. Each
  card must be recognizable cold, by someone who has read none of the posts.
- US English.
- Retired language must appear nowhere: "Real Talk. Real Strategy. Real Results."
  and "Down to the Hardware".
- Locked tagline, for register: "Grounded certainty for digital transformation leaders."
- Final text lands in the `card-desc` spans of
  `partials/components/series-nav.hbs`. That partial is the single handoff point
  between the content lane and the theme lane.

## 3. Evidence base — what each series actually contains

### Operational Learning — 10 posts, Mar-May 2026, amber `#D4943A`
Signals vs. Noise · Reopen Triggers · Exception Design · What Your Standards Are
Quietly Teaching You · When Everything You Know Lives in One Person's Head ·
What's Running Underneath · Cadence as Control · Ownership as Architecture ·
The Missing Path · Hands Stilled

> Current: "Building systems that keep lessons learned under pressure." (58)
> Assessment: holds up against the posts. The weakest candidate for change.

### Across the Divide — 10 posts, Oct-Dec 2025, bronze `#A86A28`
Why Technology Must Be Strategy, Not Just Support · Technology as Strategy in the
Public Sector · Execution in the Public Sector · From Service Delivery to
Transformation Leadership · Beginning New to Manufacturing · Weather the Storm ·
Standards in Motion · The Quiet Work of Making Things Better · Scaling Better
Without Breaking Trust · When Better Becomes Muscle

> Current: "When IT becomes strategy instead of plumbing." (45)
> Assessment: accurate but narrow. The series carries a substantial public-sector
> and manufacturing thread the current line does not signal at all.

### Data Done Right — 7 posts, Aug-Nov 2025, steel `#7EB3CC`
Dirty Data = Expensive Decisions · Scaling with Purpose · Building the Foundation
for Trust · From Discipline to Confidence · From Confidence to Capability ·
From Capability to Possibility · The Journey to Possibility

> Current: "Rebuilding trust in the numbers your organization runs on." (58)
> Assessment: the series is an explicit progression - discipline > confidence >
> capability > possibility. The line captures trust but not the movement.

### Architecture That Persuades — 4 posts, May-Jun 2026, accent unratified (arc)
The Diagram That Stayed · Maps That Decide is NOT in this series · Still Running ·
The Date That Held · Drawn Clean

> Current: "When the structure makes the case the argument can&rsquo;t." (59)
> Assessment: written when the arc was invisible, so it was never checked against
> the posts. The four pieces are about diagrams, roadmap dates, and retirement
> decisions doing persuasive work inside organizations. Brand system §5.4 locked the
> arc's visual language on 2026-05-25: "weathered structural detail separating two
> materially distinct organizational layers."

### Who Pays for Clarity — 3 posts, Jul-Aug 2026, accent unratified (arc)
The Double Bill · The Unmeasured Advantage · The Standing Charge

> Current: "The real cost of clarity, and who ends up carrying it." (54)
> Assessment: written before the arc had any tagged content, and in fact this line
> is what the three posts were grouped by. All three run an explicit cost metaphor:
> a bill paid twice, a team that pays for every team that isn't measurable, a
> standing charge for telling the truth. The line holds up unusually well — but
> confirm the grouping is right before trusting that.

### Real Talk to Real Results — 5 posts, Sep-Oct 2025, accent UNRATIFIED (see 4)
Accountability Starts at the Top · Governance Without Bureaucracy · From Features
to Outcomes · Execution that Sticks · How Transformation Becomes a Habit

> Current: "Accountability, governance, and execution that sticks." (54)
> Assessment: reads as a list of its own post titles rather than a claim about
> the series. The strongest candidate for a rewrite.

## 4. Open decisions that belong to this phase

1. ~~Real Talk to Real Results accent~~ **RESOLVED 2026-08-30: amber `#D4943A`.**
   Four cards over three accents means one accent necessarily repeats; amber puts
   the repeat at positions 1 and 4 rather than adjacent, and leaves steel as the
   interactive/link token. Applied in the partial; brand skill table updated.
2. **Arc card accents are unratified** (both steel, both currently hidden).
3. ~~rgba(255,255,255,0.15) border fallback~~ **RESOLVED 2026-08-30.** Changed to
   `var(--color-border, #4A4D52)` per the runbook. The brand hex/rgb grep now
   returns clean, so the runbook's "known open finding" note is stale and should be
   dropped at the next edit of the deploy skill.

## 5. Also in Phase B, but not in this repo

The About page rewrite and the homepage framing check (site title/description, CTA
line) are Phase B items. They apply directly in Ghost Admin and never touch the
theme, so they are out of scope for this brief and for Phase C.
