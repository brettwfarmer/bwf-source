# BWF OG Card Template

Generates the 1200x627 social card used as a post's **feature image**, so every
post carries the publication's signature in a LinkedIn feed instead of an
unrelated AI image.

## Use

```bash
./render.sh "Post title" "Series name" out.png
```

`Series name` must be one of the four ratified series; anything else falls back
to steel:

| Series | Accent |
| --- | --- |
| Operational Learning | amber `#D4943A` |
| Data Done Right | steel `#7EB3CC` |
| Across the Divide | bronze `#A86A28` |
| Real Talk to Real Results | amber `#D4943A` |

Upload the PNG as the post's feature image in Ghost. Ghost derives `og:image`
and `twitter:image` from it automatically.

## Design notes

- 1200x627 is the `summary_large_image` ratio. The site's current homepage card
  is 1024x1024 square, which LinkedIn crops or downgrades - that is the defect
  this template exists to stop repeating.
- The left accent stripe is the strongest series signal at feed scale, where the
  title is often unreadable. Series recognition survives the thumbnail; wording
  does not.
- Titles step down from 82px in 2px increments until they fit three lines. Long
  headlines are the norm here, so silent clipping was not acceptable.

## Why the fonts are vendored

`fonts/` holds the latin subsets of Newsreader 600 and DM Sans 500. Chrome's
`--screenshot` fires on the load event; pulling webfonts from Google at render
time is a race that silently yields a card set in the fallback serif. That is
the same class of failure that kept Newsreader off the live site for months.

Do not add `--virtual-time-budget` to the Chrome invocation. It hangs
indefinitely in combination with `--screenshot` on Chrome 151.
