---
name: bounds-native-craft
description: "Build, style, and review native app interfaces with platform-correct layout, type, color, interaction, motion, accessibility, and spatial design, verified with device-grade evidence. References cover Apple platforms (SwiftUI first, UIKit and AppKit; iOS, iPadOS, macOS, visionOS); other native platforms follow their own guidelines. Use when building, styling, or reviewing native app UI. Not for web UIs (use bounds-web-craft) or Swift code with no interface."
license: MIT
---

# Bounds native craft

Make a native interface behave the way its platform does, and prove it with evidence that matches the claim. System components, text styles, colors, and behaviors are the default; depart only for a stated reason. Install nothing on invocation.

## Workflow

1. **Scope.** Identify the platforms, deployment targets, framework (SwiftUI, UIKit, AppKit), surface (screen, component, window, volume, immersive space), and topics touched. Reuse the project's components, tokens, and conventions before adding new ones.
2. **Load.** Read only the matching references below. Android and other native platforms have no reference yet: follow their own guidelines (Material 3 on Android) and say so.
3. **Apply.** Taste, brand, and product direction belong to the user: recommend with the tradeoff, then stop for their call.
4. **Verify.**
   - Previews and fixtures prove presentation only, for the data they contain.
   - A simulator is not a device. Feel, haptics, frame pacing, VoiceOver, and visionOS comfort need hardware.
   - Compiled is not seen, and seen is not used.
   - Scale checks to the change. Minimum: the changed view in its states, light and dark, at one size measured at runtime. Add the largest accessibility text size (where Dynamic Type exists) for text or layout, VoiceOver for controls or reading order, and size classes, rotation, and resizing for layout. New screens and shared styles get everything.
5. **Report.** State what changed, then what was checked: revision or build, device or simulator with model and OS, runtime window size, appearance, text size, accessibility settings, and data state. List what was not checked. Approval covers only that evidence.

## References

| Reference | Read when the work touches |
| --- | --- |
| [Foundations](references/apple-foundations.md) | Hierarchy, layout, size classes, localization, typography, color, SF Symbols, materials |
| [Interaction](references/apple-interaction.md) | Targets, gestures, flings and snapping, haptics, pointer, keyboard, focus, macOS input |
| [Motion](references/apple-motion.md) | Animations, springs, transitions, Reduce Motion, dropped frames |
| [Accessibility](references/apple-accessibility.md) | VoiceOver, text sizes, contrast, alternative input, any accessibility review |
| [visionOS](references/apple-visionos.md) | Windows, volumes, immersive spaces, ornaments, hover effects, depth, eye and hand input |
| [Swift](references/apple-swift.md) | State ownership, concurrency errors in UI code, view performance, UI logic tests |

## Routing

- **Web UI**, including inside Electron, Tauri, Capacitor, or other WebView apps: `bounds-web-craft`. This skill covers those apps' platform conventions (menus, windows, system shortcuts, accessibility settings).
- **React Native or Expo:** this skill for platform conventions (targets, haptics, accessibility, navigation patterns); the framework's own docs for implementation.
- **Repeatable device checks:** `bounds-create-verification` builds a project recipe; without it, record the manual steps.

If a named skill is absent, say so and follow the platform's own guidance.
