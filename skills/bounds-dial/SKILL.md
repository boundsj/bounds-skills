---
name: bounds-dial
description: "Build a small dev-only tool the user operates to tune a value judged by eye, ear, or hand, such as motion, timing, framing, gameplay feel, color, mix, or density, then apply the version they save. Use when direct attempts keep missing after repeated feedback, not for values an objective measure settles or for finding a first direction."
license: MIT
---

# Bounds dial

When direct attempts at a value judged by perception keep missing after repeated feedback, stop guessing. Build the smallest dev-only tool the user operates, then ship the version they save.

## Before building

- **Measure first.** If the criterion is objective, such as a contrast ratio, frame budget, or target size, measure it instead of tuning. When a subjective value has a hard floor, the tool enforces or displays it.
- **Direction, not value?** With no numbers or reference yet, use `bounds-options`. If it is absent, build a few distinct variants behind one switch, let the user pick, then return here to fine-tune.
- **Propose.** Briefly say what the tool adjusts, its ranges and floors, where it runs, how it stays out of production, the project path for saves and how a save reaches it from the running surface, and any shipping-code change needed so tool and product read one source. Wait for a go.

Use the project's existing stack: one route, panel, scene, or script, never a framework. A new dependency is a separate ask. The tool is the rerunnable artifact a reviewer can check.

## Build

Read [tool contract](references/tool-contract.md) while building. Every tool:

- shows current values and a version label;
- saves a new file at the agreed path, never overwriting an earlier save;
- opens on a first version that reproduces the shipped value;
- gives the same output after save and reload.

Add a random seed only when output involves randomness, comparison of saved versions only when the user wants A/B, and a format version only when the config outlives the session.

Fit its form to what the user is judging; the tool contract covers the common forms.

## Hand off

Check the first-version and save-reload rules yourself, then explain launching, adjusting, and saving. Say what this surface cannot prove: a simulator or desktop preview is not the device, a muted preview does not verify audio, and fixtures prove presentation only.

Then stop iterating. Fix the tool when it blocks the user, such as a too-narrow range; offer no more guesses.

## Harvest

Harvest often happens in a later session: read [harvest and cleanup](references/harvest.md) now, even if you skipped the sections above.

Apply values from the saved file the user names, never from screenshots or memory. Record which version shipped and the evidence it was judged on: surface, revision, measured size, theme, and data. State what that approval did not cover.

## Remove or gate

The user decides whether to remove the tool or keep it gated out of production. Removal ends replay of saved versions; say so first.
