# Worst-case data

Use this in stress-test mode, or when the worst-case content lens applies. The aim is realistic data that real users, imports, or API clients will eventually send, shown side by side with the data the screen was built against.

## 1. Inventory what the screen renders

List every value the screen shows: its source, type, limit, and whether it can be missing. Include the easily forgotten ones: counts in headings and badges, relative times, status labels, button text that comes from data, accessibility labels built from data, image URLs, and the length of each list.

Find limits in validation schemas, database columns, API contracts, and input length caps. Record "unbounded" when none exists; that is a finding on its own. When the input cap is shorter than the storage limit, test the storage limit, because imports and API clients bypass the input.

## 2. Rules for the data

- **Realistic or at the documented limit.** Each value is something a person, import, or API could produce. Random filler such as a long run of one letter proves nothing and invites dismissal.
- **Same entry point as the normal data:** the fixture, mock response, preview provider, or seeded store. Never edit markup, styles, or layout to provoke a failure; that tests the edit.
- **Spread failures across the first visible rows,** as real data does, instead of stacking every extreme into one row.
- **Separate datasets for what one list cannot show:** empty, exactly one, page size and page size plus one, and the realistic maximum, which means thousands of rows when the list is unpaginated.
- **Invented people and reserved domains only** (`example.com`, `example.org`, `.test`). Never copy real customer data into a fixture.

## 3. The toggle

- Place the switch where the reviewer can flip it while looking at the screen. Use whatever the project already has for debug-only tools: a debug menu, a launch argument, a URL parameter read in development builds, a preview variant, or a prototype route.
- States: normal, worst case, and the separate datasets above (for example empty, one, many).
- Gate it out of release builds. Building or inspecting the release configuration proves the gate; reading the condition only suggests it.
- Keep it plain and outside the layout under test, so it is never mistaken for the design and cannot shift what is being measured.
- Prefer a selection that survives reload or relaunch, so captures can be reproduced.
- Keep a running list of every file the harness adds and every existing file it edits, with what changed.

### Handoff

When the stress test and any authorized fixes are done:

1. List every file the harness added and every existing file it edited. Do this whether or not it is removed.
2. Ask whether to keep the harness, with removal as the default. A kept fixture can serve as regression data for later changes.
3. If the user keeps it, it stays gated to debug builds, and later reviews check it under the leftovers lens.
4. Otherwise, delete the added files and revert only the harness's own edits, leaving authorized fixes in place, then check that the normal data path is unchanged. If you have to finish before the user answers, remove it and report what was removed.

## 4. Values that break things

Pick the rows that match the inventory. Mix them across rows.

### Names and people

| Value | Tends to break |
| --- | --- |
| `Anne-Sophie Lefèvre-Desrosiers` | Long, hyphenated, accented; wraps at the hyphen or overflows a one-line row |
| `Robert James Whitfield Jr.` | Suffix; first-and-last-word initials give "RJ" |
| `Bo` | Very short; the column looks empty, one-letter initials |
| `Nguyễn Thị Hồng Nhung` | Stacked diacritics clipped by tight line height with hidden overflow |
| `山田花子` | No spaces; word-based initials find one word, and lines may break between any characters |
| `سارة الهاشمي` | Right-to-left; icons, punctuation, and padding land on the wrong side |
| `🌻 Sunny` | Emoji first; taking the first code unit yields a broken character |
| `👩🏾‍🔬 Dr. Ade` | Multi-part emoji; length counts surprise, truncation can split it |
| `  Lee   Park ` | Stray spaces; empty words, uneven gaps |
| Missing name, email only | The fallback for display name and avatar |

### Identifiers and links

| Value | Tends to break |
| --- | --- |
| `maximilian.vandenberghe@regional-operations-group.example.com` | No break points; pushes trailing actions out of the row |
| `sam+receipts-2026@example.org` | Plus sign; strict validation, end truncation hides the tag |
| `https://docs.example.com/teams/platform/projects/annual-review/drafts/7c1e9a?view=comments&sort=oldest` | Long URL that differs only near the end |
| `3f2c8a91-6b4d-4e7f-9a12-c5d0e8b7f416` | Identifier; width, and end truncation makes several look the same |
| `Budget FY26 – FINAL (v7) [approved].xlsx` | End truncation hides the version and extension |

### Labels and copy from data

| Value | Tends to break |
| --- | --- |
| `Regional Customer Success Operations Lead, EMEA` | Long title in a secondary slot wraps to several lines |
| `Zugriffsberechtigungen` | German compound with no break point; label overflow |
| Translated button and tab labels | Short strings can double or triple in translation, while longer text grows about 30%; fixed-width buttons and tabs overflow first |
| Fifteen tags on one item, or one 40-character tag | Tag rows that wrap into a wall; one chip wider than its container |
| Empty string, whitespace only, `Untitled` | Collapsed headings, zero-height rows |
| `<b>bold</b>`, `&amp;`, `**text**`, `{name}` | Must show literally; reveals double escaping, interpreted markup, or template leaks |
| A newline inside a one-line field | Doubled row height or silently joined words |
| A pasted description thousands of characters long | Clamping, "show more", growing text areas |

### Numbers

| Value | Tends to break |
| --- | --- |
| `0` | Zero states, empty progress, division by zero |
| `1` and `2` | Plural forms; some languages need more than two, and Arabic uses six categories |
| `1000`, `1000000` | Missing separators, badge width, compact notation |
| `-12.50` as currency | Sign placement, meaning carried by color alone |
| `0.1 + 0.2` rendered raw | Floating-point noise on screen |
| `105%`, `-3%` | Progress bars and meters past their bounds |
| `null`, `NaN`, missing | Rendered as literal text |
| `1.234,56` in German, `1,234.56` in US English | Hardcoded separators |
| A live count crossing 99 to 100 | Width jump and jitter without tabular figures |

### Time

| Value | Tends to break |
| --- | --- |
| Now | "0 seconds ago" instead of "just now" |
| A future date | "-3 days ago" |
| `1970-01-01` | A zero timestamp shown as a real date |
| Shortly before midnight in another time zone | The wrong calendar day |
| A daylight-saving transition day | Days of 23 or 25 hours; duration math |
| A duration of 400 hours | Never rolls up into days |

### Collections, media, and states

| Value | Tends to break |
| --- | --- |
| 0, 1, page size, page size plus one | Missing empty state, lonely single card, empty last page, "1 of 1" |
| Thousands of rows, unpaginated | Scroll smoothness, memory, count copy |
| Duplicate names | Lists where the name is the only distinguishing field |
| One item far larger than the rest | Grid rows stretching to the tallest |
| Image URL that fails to load, or no image | Broken-image icons; fallback size and color |
| Very wide or very tall image | Distortion without cropping to the frame |
| Dark logo with transparency on a dark theme | Invisible artwork |
| Slow image | Layout shift without reserved size |
| Every status value in one list | Uneven badge widths, missing styles for rare statuses |
| Some optional fields filled, others not | Misaligned rows |
| No permission for an action | Disabled controls changing the row layout |
| The current user in the list | "You" labels, actions that should not apply to yourself |

## 5. Environment passes

Run the worst case again under each condition the product supports:

- The real container width measured in the running build, then the narrowest and widest supported. On the web, include a 320 CSS pixel viewport, the WCAG reflow width.
- The largest text setting: browser zoom at 200%, Dynamic Type accessibility sizes on iOS and iPadOS, or Android's largest font and display size.
- Dark theme, and increased contrast or forced colors where supported.
- Right-to-left: a right-to-left locale or the platform's pseudolanguage (Xcode offers right-to-left and double-length pseudolanguages; Android offers the `ar-XB` and `en-XA` pseudolocales and a force-RTL developer option). On the web, `dir="rtl"` on a wrapper is a quick proxy.
- Touch, where hover-only controls disappear.

## 6. Common causes

| Symptom | Usual cause | Fix direction |
| --- | --- | --- |
| Avatar or icon squashed | A fixed-size item allowed to shrink | Stop it shrinking (web: `flex-shrink: 0`; native: a fixed frame or higher layout priority) |
| Text spills out of its box | A flex or grid child cannot shrink below its content | Allow shrinking (web: `min-width: 0`, or `minmax(0, 1fr)` in grid), then wrap or truncate |
| Email or URL runs past the edge | No break opportunities | Allow breaks for that element only (web: `overflow-wrap: anywhere`) |
| Trailing action pushed off | Middle content took the space | Middle shrinks; the action keeps its size |
| Accents or tall scripts clipped | Tight line height with clipping | Looser line height; do not clip text boxes |
| Larger text clipped | Fixed heights | Minimum heights; let height follow content |
| Wrong initials | Slicing code units, first-and-last-word logic | Segment by grapheme (web: `Intl.Segmenter`), handle suffixes, fall back to an icon |
| "1 items" | Hardcoded plural | Platform plural rules (`Intl.PluralRules`, Android quantity strings, Apple string catalogs) |
| Raw or wrongly formatted numbers and dates | Hand-built strings | Locale formatters (`Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, or the platform's) |
| Broken-image icon | No load-failure fallback | Fall back to initials or an icon; crop to the frame |
| Ellipsis with no way to read the rest | Truncation alone | Full value reachable on touch and by screen reader, such as a detail view |
| Long list stutters | Every row rendered | Paginate or virtualize, and say which |

## 7. Truncate, wrap, or clamp

Decide per field, not globally:

- **Wrap** values that identify something: names and titles.
- **Truncate the end** of secondary text whose start carries the meaning, and make the full value reachable.
- **Truncate the middle** of values that differ at the end: file names, paths, identifiers, emails sharing a domain.
- **Clamp to a line count** for previews in cards whose heights should match.
- **Never truncate** amounts, dates, quantities, or anything users compare.

When the right choice is not obvious, put it under Your call with a recommendation.

## 8. Reporting breaks

Report each break as a fixable-in-source row: the field, the value that broke it, what happened at which measured width or setting, the evidence, and the fix location. List catalog rows not tried and why: not rendered, not reachable, or not supported. Record what held up, so the user knows the test was real and what not to touch. Close with the harness file list and the keep-or-remove question from the handoff in section 3.
