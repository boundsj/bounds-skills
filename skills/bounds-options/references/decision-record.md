# Comparison, mixing, and decision record

The examples below use one illustrative question; replace every value with what was actually built and observed.

## Comparison

Present only after exercising every variant. Lead with the question and how to open and switch the harness. Keep the table neutral; put any recommendation after it, with its reason. Give evidence per row when it differs between variants.

```md
Question: Should order history lead with status or with date?
Open: http://localhost:5173/orders?variant=1 (keys 1-3 or left/right arrows)

| # | Variant | Bets on | Wins when | Cost or risk |
| --- | --- | --- | --- | --- |
| 1 | Baseline (current) | date order | most visits check a recent purchase | delayed orders are easy to miss |
| 2 | Status groups | hierarchy: action needed first | people come to fix a problem | groups reshuffle as statuses change |
| 3 | Timeline | tone: each order as a story | orders have many steps | half as many orders per screen |

Evidence, all variants: commit 4f9c2e1 plus uncommitted harness; Chromium desktop; viewport measured at 1280x800 and 320x640 CSS px, DPR 2; light and dark; text at 100% and 200%; fixture orders-worst (42 orders, longest names, empty and error states); mouse and keyboard.
Not seen: touch, screen reader, real account data.
Recommendation: 2, because most support contacts are about delayed orders.
```

## Mixing

Accept short replies:

- `2`: choose variant 2.
- `2, with 3's header`: variant 2 is the base; port the named part from 3.
- `2, with 3's header and 1's empty state`: port several parts.
- `more like 2`: a new round of variants around 2's direction, replacing the others.
- `none`: no direction works; revisit the question before building more.

To build a combination:

1. Write it down first as a list of parts: what each part is, which variant supplies it, and what it replaces. When a word like "header" could point to more than one element, confirm with the human before building.
2. The base, the variant named first, sets the frame. Its layout, type scale, and spacing govern; incoming parts are rebuilt to fit them, and each such adjustment is noted.
3. If two requested parts cannot coexist, such as both claiming the same space or one depending on navigation the other removes, show the conflict and let the human choose. Never blend them into a compromise nobody asked for.
4. Give the combination its own variant file, the next free number, and a name for its direction, so every variant it draws on stays intact to compare against. Its sources leave the switcher only when the human retires them.
5. Run it through the same content and state pass as the others, looking hardest at the seams: alignment and spacing where parts meet, focus and reading order across them, and states in which one part grows, shrinks, or disappears.
6. Add it to the comparison as a new row, list its sources and adjustments, and stop again for the human.

Each round should leave fewer parts in dispute. If a second round leaves as many open as the first, or the same part keeps going in and coming out, stop building and question the question. Ask the human:

- Is the answer outside this set? Start a fresh round from the parts they keep choosing.
- Does it depend on the situation, such as first use against daily use? It may be two designs.
- Is an unstated goal or limit rejecting each candidate? Name it, then rebuild against it.
- Is the call someone else's, or does it need evidence from real use rather than another look?

## Decision record

Draft the record and return it in the response. Post it to an issue, a PR description, or a comment only when the user has authorized that write. Add it to the repository, in the decision log the project already keeps, only as part of work authorized to change the repository. Do not start a new documentation system for it.

```md
## Decision: Should order history lead with status or with date?
- Chosen: 4 Status groups with steps, base 2 plus 3's step count per order
- Superseded: 2 Status groups, the base of 4
- Rejected: 1 Baseline, delayed orders fell below the fold with 42 orders
- Rejected: 3 Timeline, "too much scrolling for a list I check daily"
- Not ported from 3: per-step timestamps, crowded the row at 320 px
- Settled values: group header spacing 24 px
- Approved: layout and hierarchy, viewed at 6a0d5b2 in Chromium desktop at 1280x800 and 320x640 CSS px, light and dark, 100% and 200% text, fixture orders-worst, mouse and keyboard
- Not covered: touch on a phone, screen reader order, real account data, load time at production volume
- Follow-ups: decide whether groups collapse (separate question); review status label copy
- Exploration: branch explore/order-history at 7b1d0a3; harness removed in 9e2c4f8
```

Capture which variant won and the reason for each loser, quoting the human when they gave one; reopening the question then needs new evidence. Approval covers only what was seen. If integration changes the winner, show the changed part again before treating it as approved.
