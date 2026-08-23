---
name: bwf-brand-system
description: The Brett W. Farmer brand system (v1.1) for brettwfarmer.com — color tokens, typography, series accent mapping, retired elements, and visual rules. Use this skill for ANY work that touches visual presentation on the site or theme: CSS, Code Injection, the series-nav partial, card styling, fonts, OG/social meta, images, favicons, or accessibility checks. Also use it when validating that a change contains no retired brand elements. If a hex value, font name, or accent choice is about to be written, consult this skill first rather than guessing.
---

# BWF Brand System v1.1 (locked)

Authoritative distillation of `BWF_Brand_System_v1_1.docx`. If this file and that document ever disagree, the document wins and this skill needs updating.

## Identity

- Brand: **Brett W. Farmer**
- Tagline: **"Grounded certainty for digital transformation leaders."** (locked; tagline exploration is concluded)
- Retired and must appear nowhere: "Real Talk. Real Strategy. Real Results." / "Down to the Hardware" / the synthwave-retrowave aesthetic / teal `#4A8A7A`.

## Core token system (nine tokens)

| Token | Hex | Use |
| --- | --- | --- |
| `--color-bg` | `#040A1C` | Primary background. The canvas across every touchpoint. |
| `--color-surface` | `#0D1220` | Elevated surfaces: cards, content containers, overlays. |
| `--color-text-primary` | `#E8E6E0` | Headlines and body text on dark backgrounds. |
| `--color-text-secondary` | `#B0ADA6` | Subheadings, secondary labels, structural metadata. |
| `--color-text-muted` | `#8A8880` | Captions, timestamps, tertiary information. |
| `--color-accent-primary` | `#7EB3CC` | Steel. Links, primary accents, Data Done Right series lead. |
| `--color-accent-secondary` | `#D4943A` | Amber. Emphasis, warmth, Operational Learning series lead. |
| `--color-accent-tertiary` | `#A86A28` | Bronze. Across the Divide series lead. Weathered metal register. |
| `--color-border` | `#4A4D52` | Dividers, borders, structural separators. |

## Extended palette (supporting values only, never primary accents)

- Steel deep `#5A8FA8` (supporting strokes, secondary borders, hover on amber)
- Steel light `#A3CFDE` (highlights, tinted areas)
- Steel highlight `#D1E8F0` (background tints, very light emphasis)
- Amber deep `#8B6420` (dark amber details on dark backgrounds)
- Amber light `#E8B86A` (secondary highlights, lighter warmth)
- Amber highlight `#F4D9A8` (background tints, very light warm emphasis)
- Surface elevated `#141A2E` (hover states, secondary panels above `--color-surface`)
- Structure `#2A2E36` (subtle background differentiation on dark surfaces)

## Series accent leads

| Series | Lead accent |
| --- | --- |
| Operational Learning | Amber `#D4943A` |
| Data Done Right | Steel `#7EB3CC` |
| Across the Divide | Bronze `#A86A28` |

Arc cards (Architecture That Persuades; Who Pays for Clarity): accent assignments are decided in the series-nav partial work; verify against the partial or ask Brett rather than inventing. Both currently render steel `#7EB3CC` in `partials/components/series-nav.hbs`. The three accents never compete at equal weight in one composition.

**Open gap:** *Real Talk to Real Results* is an always-on series card with no accent lead defined in this table. The partial currently assigns it steel `#7EB3CC` as the default interactive token. Deferred to the card-copy/visual drafting session — do not treat steel as ratified.

## Typography

- **Headlines:** Newsreader (serif). In Source, inject via `--gh-font-heading`.
- **Body:** DM Sans. In Source, inject via `--gh-font-body`.
- Source's native typography settings cannot supply these fonts; 100% of font implementation lives in Code Injection. Load via Google Fonts (or self-host) in the head injection.

## Hard visual rules

- Never pure white `#FFFFFF` text; use `--color-text-primary` `#E8E6E0`.
- Never pure black `#000000`; darkest value is `--color-bg` `#040A1C`.
- Teal `#4A8A7A` is retired; it appears nowhere, including comments and examples.
- WCAG 2.1 AA contrast is the accessibility floor for all text and interactive elements.
- Steel is the token for interactive and emphasis elements by default.

## Verification habit

Before finishing any visual change, grep the diff for `#4A8A7A`, `#FFFFFF`, `#000000`, "Real Talk. Real Strategy", and "Down to the Hardware". All five must return nothing.
