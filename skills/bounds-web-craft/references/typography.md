# Typography

Type carries most of an interface. Settle the scale, rhythm, and loading before tuning anything else, and use the project's existing type tokens when they exist.

## Scale

- Pick a small set of sizes and use only those. A modular ratio (1.125 to 1.25 for dense product UI, up to about 1.333 for editorial pages) or a hand-tuned list such as 12, 14, 16, 18, 20, 24, 30, 36, 48 both work; ad hoc sizes do not.
- Body text for reading starts at 16px (`1rem` at the browser default). Dense secondary UI text can go to 14px; treat 12px as a floor for labels and captions, not for sentences.
- Size in `rem` so text follows the user's browser setting. WCAG 2.2 SC 1.4.4 requires text to resize to 200% without loss of content or function.
- For headings that should grow with the viewport, use `clamp()` with a `rem` component, such as `clamp(2rem, 1.5rem + 2vw, 3rem)`. Pure `vw` sizes do not grow when the user zooms.

## Line height and measure

- Body copy: unitless `line-height` around 1.5. Headings: 1.1 to 1.25, tighter as size grows. Single-line UI labels: 1.2 to 1.4.
- Keep reading text at roughly 45 to 75 characters per line. `max-width: 65ch` is a reasonable start, but `ch` is the width of the zero glyph, so check with real copy.
- SC 1.4.12 Text Spacing: layouts must survive users forcing line height to 1.5×, paragraph spacing to 2×, letter spacing to 0.12em, and word spacing to 0.16em. Fixed heights on text containers fail this.
- `text-wrap: balance` evens short headings; `text-wrap: pretty` reduces orphans in paragraphs. Both are progressive and harmless where unsupported.

## Tracking

Letter spacing depends on size. Display text above about 32px usually wants slight negative tracking (`-0.01em` to `-0.03em`); body text stays at `0`; small uppercase labels want positive tracking (`0.04em` to `0.08em`). Use `em` so it scales with the font. Never apply one tracking value to every size. Fonts with an optical size axis adjust some of this themselves; leave `font-optical-sizing: auto` on.

## Numerals and characters

- `font-variant-numeric: tabular-nums` for anything that updates, aligns in columns, or counts: timers, prices, tables, progress.
- Typewriter stand-ins for punctuation look unfinished in a polished interface. Let the copy or localization layer supply proper glyphs, since quotation marks and spacing rules differ by language, and join each number to its unit with a non-breaking space so a line break cannot split them.
- Format with `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.RelativeTimeFormat`, and `Intl.PluralRules` instead of string building. "1 members" and hardcoded separators are bugs.
- Prefer high-level properties (`font-variant-numeric`, `font-variant-caps`) over raw `font-feature-settings`, which overrides the cascade wholesale.

## Overflow

- User-supplied strings (emails, URLs, IDs, compound words) need `overflow-wrap: anywhere` or a deliberate truncation.
- Flex and grid children that truncate need `min-width: 0`.
- Single-line truncation needs `overflow: hidden`, `white-space: nowrap`, and `text-overflow: ellipsis`. The unprefixed `line-clamp` is not Baseline yet, so clamp to N lines with the prefixed set that works across engines: `display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: N; overflow: hidden`.
- Truncation hides content; make the full value reachable another way. A `title` attribute is not reachable on touch.
- Set `lang` on the document so hyphenation and screen reader pronunciation work, and `dir="auto"` on user-generated text.

## Font loading

- Every family, weight, and style is a download. Prefer a variable font or two weights; default to `system-ui` stacks when the design does not need a custom face.
- Self-host WOFF2, subset to the characters you ship, and preload only the one or two files used above the fold (`<link rel="preload" as="font" type="font/woff2" crossorigin>`).
- `font-display: swap` shows text immediately and risks a visible reflow; `optional` avoids a late swap at the cost of sometimes using the fallback. Reduce swap shift with `size-adjust`, `ascent-override`, and `descent-override` on a fallback `@font-face`.
- Set `font-synthesis: none` when the real bold or italic is loaded, so the browser never fakes one.

## Hierarchy

Build levels from size, weight, color, and spacing together, and use no more than about three per view. Use heading elements for document structure (one `h1`, no skipped levels) and style them independently of their level. Never change font weight on hover or selection; the text reflows. Choosing a typeface or a scale ratio is a taste call: propose one with a reason and let the human decide.
