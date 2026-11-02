---
name: bounds-options
description: "Build two to four genuinely different variants of an undecided UI, visual, or interaction direction behind a switcher with real worst-case content, then stop for the human's pick or mix, record the decision, and remove the harness. Use when a design direction is genuinely open; not for already-decided designs, polish, or reviewing existing UI."
license: MIT
---

# Bounds options

Settle one open design question by letting the human compare real alternatives. If the direction is already decided, just build it. This skill grants no extra permissions.

## Frame

1. State the undecided question in one line before building. If there are several, start with the one that constrains the rest.
2. Choose two to four new variants, plus the current version as baseline, each named for its direction and the axis it bets on: density, hierarchy, interaction model, tone, motion. Tweaks of one idea count as one; never pad the set. Keep the baseline unchanged.

## Build

3. Use the project's real components, tokens, and assets. Give every variant the same realistic data and hardest cases: longest strings and translations, largest text size, empty, loading, and error states, light and dark, narrow and wide sizes, each relevant input method. Read [content stress](references/content-stress.md) when preparing them.
4. Read [harnesses](references/harnesses.md), then build for the medium. Web: a `?variant=` parameter on the existing page, a throwaway route, or a standalone HTML file, with a small floating switcher that is chrome, not design. Native: a debug-only launch argument or debug menu, compiled out of release and failing closed. Film, 3D, or visual assets: look-dev stills or hero frames at delivery resolution, side by side. Switching is instant and preserves state where possible.
5. For an open magnitude, such as a duration, attach a live control; see harnesses.
6. Exercise every variant in each relevant state yourself, recording what you viewed.

## Present and stop

Read [decision record](references/decision-record.md), then present a compact comparison. Per variant: what it bets on, when it wins, its cost or risk, and the evidence viewed (revision; device, simulator, or browser; size measured at runtime; theme; text size; data). Then stop; the choice is the human's. You may recommend, with a reason grounded in the product's use.

The human can also combine parts, like 3's header on 2. Build it as a new variant, stress its seams first, and compare again. If a second round settles nothing, question the question.

## Decide and tear down

Draft a record of the chosen variant, each rejected one and why, follow-ups, and approval scope: what was approved on what evidence, and what was not covered. Fixtures and previews prove presentation only; a simulator is not a device; a still approves neither motion nor feel; unheard audio is unverified.

Before removing anything, ask whether to keep the exploration on a throwaway branch or record its commit. When building the winner is in scope, rewrite it to production standards. Remove the harness and losing variants from shipping code, then confirm a release build cannot reach any switcher.
