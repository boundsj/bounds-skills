---
name: bounds-web-craft
description: "Apply interface craft when building, styling, or reviewing web UIs in HTML, CSS, and JavaScript frameworks, including web UIs inside desktop or mobile shells: typography, color, surfaces, layout, components, forms, accessibility, motion, performance, mobile web, and marketing pages, verified in a real browser. Use when a task changes or judges how a web interface looks, reads, or responds. Not for fully native or React Native interfaces (use bounds-native-craft) and not for backend or API work."
license: MIT
---

# Bounds web craft

Build web interfaces that read clearly, respond at once, and survive real content and settings. Keep small requests small: a contrast fix needs one reference, not an audit.

## Workflow

1. **Identify the surface:** product UI, form, marketing page, or phone app; the framework, styling, and design tokens. Extend existing tokens; never add a parallel set.
2. **Read only the references** the task touches.
3. **Apply them.** Prefer native elements and the project's accessible primitives to hand-built widgets. Design for the worst realistic content.
4. **Reviews report findings; edit only when asked.** This skill loads automatically; a review request is not permission to change files.
5. **Stop for the human** on taste and product calls: brand color, typeface, density, motion personality, copy claims, truncate or wrap. Recommend one option with a reason; they choose.
6. **Verify in a real browser, in proportion to the change.** At minimum, the changed element in its states and affected themes, at one width. Add phone-to-wide widths and 200% zoom for layout or text, keyboard and a screen reader for interaction, touch hardware for touch, and reduced motion for animation; everything for new pages or shared tokens. Capture screenshots or recordings.
7. **Report what was checked and what was not:** revision, browser and version, device or emulation, measured viewport, theme, zoom, and data state.

## Evidence

- Fixtures, previews, and static renders prove presentation only.
- Desktop emulation is not a phone; touch, input zoom, safe areas, and keyboards need hardware.
- Compiled is not seen; a screenshot is not used; motion watched once at full speed is not reviewed.
- When approving, state what was approved, on what evidence, and what was not covered.

**Routing:** for a web UI in Electron, Tauri, Capacitor, or a WebView, use this skill for the UI and `bounds-native-craft` for platform conventions (menus, windows, system shortcuts, haptics, accessibility settings). React Native, Expo, and native apps use `bounds-native-craft` plus the framework's docs. If it is absent, say so and follow the platform's guidelines.

## Topic map

- [Typography](references/typography.md): sizes, line height, measure, tracking, fonts, numerals, overflow
- [Color](references/color.md): palettes, tokens, contrast, dark mode, state colors, gradients
- [Surfaces](references/surfaces.md): borders, shadows, radii, elevation, translucency, dividers
- [Layout](references/layout.md): spacing, alignment, grouping, density, responsive behavior
- [Components](references/components.md): buttons, menus, dialogs, toasts, tooltips, tables, tabs, states
- [Forms](references/forms.md): labels, input types, autofill, validation, errors, submission
- [Interaction and accessibility](references/interaction-and-a11y.md): targets, hover, focus, keyboard, screen readers
- [Motion](references/motion.md): adding, tuning, reviewing, removing animation
- [Performance](references/performance.md): jank, layout shift, input latency, media, fonts, long lists
- [Mobile web](references/mobile-web.md): phones and installed web apps
- [Marketing pages](references/marketing-pages.md): landing pages, heroes, proof, calls to action, copy
