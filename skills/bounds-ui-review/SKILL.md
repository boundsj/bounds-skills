---
name: bounds-ui-review
description: "Review an interface change, such as screens, flows, or visual output, for experience quality: interaction across inputs, accessibility, states, worst-case content, layout, motion, and leftovers, tied to the build and evidence actually observed. Use when asked to review, critique, or stress-test UI before it ships. Not for code correctness against requirements, which is bounds-review."
license: MIT
---

# Bounds UI review

Judge what a person meets when using the change; `bounds-review` checks code against requirements. Report by default. Edit only for authorized fixes, or to build and later remove a requested stress test's debug-only harness.

## Pin the evidence

Record the revision or build and how it was observed: device, simulator or emulator, browser and engine, or source only. Measure geometry in the running build, not the design: viewport or window, container widths, scale factor, safe areas, orientation. Note theme, text size, input, and data state. Exercise flows with test accounts and sandbox modes; never trigger real charges, messages, or deletions.

Label each finding's evidence: device, simulator or browser, fixture or preview, or source. Fixtures and demo data prove presentation only. A simulator is not a device. Compiled is not seen, played, or used. Unheard audio and unfelt haptics are unverified.

## Choose lenses

Read [lenses](references/lenses.md) and apply only those the change calls for. Name each skipped lens and why.

Judge consistency against the project's design rules, components, and tokens; find them first. For platform standards, use `bounds-web-craft` or `bounds-native-craft` when installed; otherwise WCAG 2.2 and MDN, Apple's Human Interface Guidelines, Material 3, and Android accessibility guidance. Install nothing.

## Judge

Each finding names what breaks, for whom, and when. Taste, direction, product calls, and removing intentional content belong to the user: recommend, never decide.

- **Blocking:** an intended task fails or gives a wrong result for a user, input, or setting the product supports, or the change causes a critical safety or privacy failure.
- **Should fix:** a concrete defect within the change that real use will reach.
- **Nit:** an improvement the user may skip.

Working defaults and advice beyond a cited criterion never make a finding blocking alone.

## Stress test

For a requested stress test, read [worst-case data](references/worst-case-data.md). Feed realistic worst-case data through the normal data's entry point, behind a debug-only toggle; never edit the component to provoke a break. Report each break with its fix; fix only on request. At handoff, list every file the harness added or edited and ask whether to keep it; default to removing it.

## Report

Use the [output format](references/output-format.md):

1. Verdict: ship, ship after fixes, or rethink.
2. Fixable in source: location, fix, severity.
3. Check on real hardware or services: the exact check and what passes.
4. Your call: the decision and its options.
5. What held up.
6. Approval scope: what was covered, on which evidence, and what was not.

Apply only the named, authorized fixes, with existing components and tokens; recheck affected screens on the same evidence pin. Earlier observations belong to the earlier revision; say what was not rechecked.
