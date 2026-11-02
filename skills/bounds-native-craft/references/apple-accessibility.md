# Apple accessibility

Accessibility is part of the change, not a later pass. Start from system controls; they arrive with labels, traits, focus, and text scaling that custom views must rebuild by hand.

## VoiceOver labels, traits, and values

- Every control needs a short label that names its action or object. Do not include the control type; traits say "button".
- `Button` and `Label` derive labels from their text. Icon-only controls need `accessibilityLabel`.
- Put changing state in `accessibilityValue` ("3 of 10", "On"). Add `accessibilityHint` only when the result is not obvious.
- Hide decorative images with `Image(decorative:)` or `accessibilityHidden(true)`.
- Custom controls add traits such as `.isButton`, `.isHeader`, or `.isSelected` with `accessibilityAddTraits`. Mark section titles as headers so the rotor can jump between them.
- When a custom control behaves like a standard one, `accessibilityRepresentation` lends it the standard control's accessibility.

## Grouping and order

- One logical item should be one stop. Combine a row's parts with `accessibilityElement(children: .combine)`, or use `.ignore` and write one label.
- Use `.contain` for containers whose children stay separate.
- If reading order differs from the visual order people expect, fix the layout first; use `accessibilitySortPriority` only when layout cannot change.

## Actions

- Swipe actions, context menus, drag-only interactions, and hover reveals need equivalents: `accessibilityAction(named:)` for custom actions, `accessibilityAdjustableAction` for increment and decrement.
- Long content can offer `accessibilityRotor` entries.
- Announce changes that happen away from focus, such as a completed upload, with an accessibility announcement notification.

## Dynamic Type to accessibility sizes

- The HIG recommends letting people enlarge text by at least 200 percent where possible. At the largest accessibility size, iOS body text is 53 pt against 17 pt by default.
- Layouts must reflow, not truncate. When `dynamicTypeSize.isAccessibilitySize` is true, stack horizontal rows vertically, let text wrap, and reduce columns. `ViewThatFits` or `AnyLayout` can make the switch.
- Keep essential text untruncated, and make every screen scroll if its content can outgrow it.
- Bars that cannot grow can support the Large Content Viewer with `accessibilityShowsLargeContentViewer`.
- Cap a component with `dynamicTypeSize(...)` only for a stated reason. Never cap the whole app.

## Display settings

Read these when custom drawing or motion is involved; system components adapt themselves.

| Setting | SwiftUI environment value |
| --- | --- |
| Reduce Motion | `accessibilityReduceMotion` |
| Reduce Transparency | `accessibilityReduceTransparency` |
| Increase Contrast | `colorSchemeContrast == .increased` |
| Differentiate Without Color | `accessibilityDifferentiateWithoutColor` |
| Bold Text | `legibilityWeight == .bold` |

## Contrast

Accessibility Inspector uses WCAG AA values: 4.5:1 for text up to 17 pt, 3:1 for 18 pt and larger or bold text. For small custom-colored text, strive for 7:1. Check both appearances. If defaults fall short, Increase Contrast must at least supply a higher-contrast scheme, through asset-catalog high-contrast variants.

## Alternative input

- **Voice Control** speaks visible names. Labels must match visible text; add spoken alternatives with `accessibilityInputLabels`.
- **Switch Control** steps through elements, so grouping and custom actions decide how many steps a task takes.
- **Full Keyboard Access** must reach every function. Avoid overriding system-defined keyboard shortcuts.
- Avoid time limits on content people need to act on.

## Tools and evidence

- **Previews** with `.environment(\.dynamicTypeSize, .accessibility5)` and a dark color scheme show presentation for one fixture.
- **Xcode Environment Overrides** change text size, appearance, and accessibility settings while the app runs.
- **Accessibility Inspector** (Xcode, Open Developer Tool) inspects elements and runs audits.
- **UI tests** can call `performAccessibilityAudit()` to catch regressions in CI.
- **A device** is required for VoiceOver on iOS; an iOS simulator cannot run it. Swipe through every changed screen, activate each control, confirm labels, values, and order, and trigger each custom action. Try Voice Control with names shown, and Switch Control where interactions are custom.
- **Report** which settings and assistive technologies were exercised, on which device and OS, and which were not.
