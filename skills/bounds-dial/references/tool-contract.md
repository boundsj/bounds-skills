# Tool contract

## The proposal

For example:

> **Dial for** the panel's open spring: stiffness, damping, and mass, each with range and unit. **Floor:** reduced-motion path shown alongside. **Runs:** a dev-only route via the usual dev command. **Saves:** a new file per save in the agreed folder. Go?

Ranges bracket the shipped value and every direction the feedback pointed. Widening a range the user has hit is a tool fix, not a new guess.

## Always

- **Visible values.** Every adjustable value with its unit, updated live.
- **Version label.** Which version is loaded and whether it has unsaved changes. The label is the saved file's name, so "ship v3" means one file.
- **Save without overwriting.** Each save writes a new file under the agreed path with the next free label. A browser tool needs a dev-only endpoint or a download the user moves; an app on a device saves to its own container, so plan an export the user can send or a copy step from the device. Never fall back to retyping values. Store values exactly as the tool uses them, not rounded for display, plus label and timestamp, in a format the project already reads, such as JSON.
- **First version is the shipped value.** Read initial values from the source the product reads, not a retyped copy, and save them as the first version. For an unshipped feature, use what the code does now. Compare the tool's output with the product's at the same state.
- **Save and reload match.** Any saved file loads back, and a reload gives the output it had at save time. Script the comparison when output can be captured: a frame at a fixed time, a computed curve, a rendered file.
- **Dev-only.** Gate it with the project's existing mechanism, such as a dev route, debug build, or flag. A production build must not reach it.

## Only when needed

- **Seed.** When output involves randomness, such as particles, procedural placement, spawn tables, or AI behavior, show, save, and allow pinning the seed. Otherwise reloads differ and A/B means nothing.
- **A/B of saved versions.** When the user wants to compare, one control switches between two saved files at the same state, with no transition. For audio, match loudness first; the louder version tends to win regardless of the setting.
- **Format version.** When the config outlives the session because it is committed, read by the product, or harvested later, add a version field. Read or clearly reject older versions.

## Shape it around the judgment

Judge in realistic context at full size, never in thumbnails.

- **Curves, springs, timing:** replay on every change, a slow-motion toggle, the reduced-motion path alongside.
- **Camera framing:** live position, angle, and field of view, a composition or safe-area overlay, the reference frame at adjustable opacity, a jump straight to the shot.
- **Gameplay tuning:** live parameters in a running build, a jump to the state under test, a reset that restores it, a pinned seed.
- **Color grade:** the same content side by side or under a split wipe against the reference, with a live contrast readout as the floor. Note the display used.
- **Mix level:** per-source faders in decibels, solo and mute, level-matched A/B, a peak meter as the floor.
- **Layout density:** spacing and size controls over realistic content, including longest and empty cases, measured surface sizes, minimum target size displayed.

## Keep it small

One file or a handful, in the project's language and framework. No plugin system, generic control-panel layer, or persistence beyond save files. A control-panel library the project lacks is a separate ask.

Before handoff, run it: the first version matches the product, a save lands as a new file, and a reload matches. Then write the harvest note from [harvest and cleanup](harvest.md).
