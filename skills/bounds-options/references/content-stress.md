# Content and state stress

On kind data, every variant looks fine. Give all variants the same hard dataset and states, and check them in the same environments. Cover what the question touches and name what you skipped.

## Rules

- Change data where it enters: fixture, mock, API stub, or props. Editing markup or styles to force a case tests the edit, not the design.
- Use values a real user could produce, or the actual limit from the validation schema, database column, API contract, or input length limit. A field with no limit anywhere is a finding; test something long but believable.
- Spread different hard cases across the visible rows instead of stacking them all in the first.
- Use invented names and `example.com`, `example.org`, or `.test` addresses, never real people or inboxes.

## Content

| Kind | Try |
| --- | --- |
| Text | the longest realistic name and title; a one- or two-letter name; a missing optional field; a line break in a one-line field; user text containing markup or entities, which must render literally |
| Unbreakable strings | long emails and URLs, file names that differ only at the end, identifiers and hashes |
| Localization | expansion (German compounds, longer French phrasing), CJK without spaces, stacked diacritics (Vietnamese, Thai) under tight line height, right-to-left text; platform pseudo-localization where available, such as Xcode's double-length and right-to-left pseudolanguages or Android's `en-XA` and `ar-XB` pseudolocales |
| Numbers | 0, 1, thousands, very large, negative, missing; locale separators; a value that updates live |
| Collections | empty, one item, exactly one page and one more, the realistic maximum |
| Media | missing and failing images, extreme aspect ratios, slow loads |
| Time | just now, a future date, the far past, a timestamp that falls on a different day in another time zone |

Format plurals, numbers, and dates through the platform's locale APIs (on the web, `Intl.PluralRules`, `Intl.NumberFormat`, `Intl.DateTimeFormat`) so lengths are realistic.

## States

Empty (first use and no results), loading (first load and refresh), error (network, validation, permission), partial data, offline where the product works offline, disabled or read-only, and success. A variant with no answer for a state is incomplete, not simpler.

## Environment

- **Theme:** light and dark; increased contrast or forced colors where the product supports them.
- **Text size:** the largest users can set. On the web, text resized to 200% (WCAG 2.2 SC 1.4.4) and the text-spacing overrides in SC 1.4.12; on iOS, iPadOS, and visionOS, the largest accessibility Dynamic Type size, and on macOS whatever text sizing the app offers; on Android, the largest font scale.
- **Size:** the real container width, the narrowest supported (320 CSS px for reflow, SC 1.4.10), and the widest; landscape, split-screen, and resizable windows where supported; safe areas on devices.
- **Input:** each method the product supports. Pointer with hover, touch without hover, keyboard with visible focus, screen reader names and reading order, and where relevant pen, game controller, or remote focus. Check touch targets against WCAG 2.2 SC 2.5.8 (24 by 24 CSS px minimum) and platform guidance (the Apple HIG's default and minimum sizes for the target platform, such as 44 and 28 pt on iOS; Material 48 by 48 dp).
- **Motion:** the reduced-motion setting, when variants move.
- **Direction:** right-to-left layout, when the product ships right-to-left locales.

## Visual assets

Judge look-dev on the hardest frames, not the prettiest: the darkest and brightest shots, fast motion, extreme close and wide framing, and the smallest size the asset ships at, such as a thumbnail or phone screen. Check every delivered aspect-ratio crop, SDR and HDR when both ship, and the final compression; banding and noise often appear only at delivery bitrate.

## Minimum pass

When the full set is out of proportion to the question, view each variant with at least the worst realistic content, one empty and one error state, light and dark, the narrowest and widest size, the largest text size, and the primary input method. Name what was skipped.

## Record what was seen

For each view, note the revision and any uncommitted changes; the environment (browser and version, simulator or emulator model and OS, or physical device); geometry measured at runtime (viewport in CSS px and device pixel ratio, or the window and safe-area size the app reports), not a size assumed from a design; theme; text size; data fixture; and input method. A fixture proves presentation, not real data. A simulator is not a device. A screenshot is not an interaction.
