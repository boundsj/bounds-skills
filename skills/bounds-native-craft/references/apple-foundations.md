# Apple foundations

Values come from Apple's Human Interface Guidelines (HIG) and change between releases. Check the current HIG before overriding system behavior on a newer OS.

## Hierarchy

- Put the most important content at the top and leading edge; people scan in reading order.
- Make one action per region visibly primary. Demote competitors to secondary styles, menus, or a deeper level.
- Express relationships with spacing, alignment, and containers before separators or color.
- Keep the same functions at every size. Rearrange across size classes; do not drop features.

## Layout and safe areas

- Keep content and controls inside the safe area. Extend only backgrounds under bars and corners, with `ignoresSafeArea` on the background.
- Add custom bars with `safeAreaInset(edge:)` so scrolling content insets beneath them.
- Use system margins and readable-width guides (`readableContentGuide`, default `padding()`, `contentMargins`) instead of hand-picked numbers.
- Leave room for localization: translated short strings can double or triple in length. Lay out with leading and trailing, not left and right, so system layouts mirror for right-to-left languages.
- macOS: keep critical controls away from a window's bottom edge, which people often drag offscreen. iPadOS windowed mode puts window controls at the toolbar's leading edge; keep leading toolbar items clear of them.

## Size classes and adaptive layout

- Decide layout from size class and measured space, never device model or orientation. An iPad window can be compact width; a large iPhone in landscape can be regular width.
- Read `horizontalSizeClass` and `verticalSizeClass` from the environment. Measure real sizes with `onGeometryChange` or `GeometryReader`, not the screen.
- Switch arrangements with `ViewThatFits`, or `AnyLayout` when views must keep state across the switch. Let `NavigationSplitView` collapse in compact width.
- Reduce columns as text size grows.

## Typography

Use text styles, not fixed sizes, so text follows Dynamic Type.

| Platform | Default text | Minimum text |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| visionOS | 17 pt | 12 pt |

On iOS at the default size, Body is 17 pt on 22 pt leading and Large Title 34 on 41. At the largest accessibility size, Body reaches 53 pt.

- Prefer Regular through Bold weights; avoid Ultralight, Thin, and Light, especially small.
- The system font tracks itself per size. Never apply one fixed tracking value to SF.
- Avoid tight leading for three or more lines.
- Scale custom fonts with `Font.custom(_:size:relativeTo:)` or `UIFontMetrics`, and confirm they honor Bold Text.
- Scale spacing and icons beside text with `@ScaledMetric`. Use `monospacedDigit()` for numbers that change in place.

## Color, dark mode, and contrast

- Use semantic colors by purpose: label colors for text, system or grouped backgrounds for surfaces, `separator` for dividers. Do not repurpose them.
- Define custom colors in the asset catalog with light, dark, and increased-contrast variants. Do not hard-code system color values.
- Never let color alone carry status or interactivity; add a shape, symbol, or text.
- iOS Dark Mode uses dimmer base and brighter elevated backgrounds so sheets advance. System backgrounds do this; custom ones lose it.
- Aim for at least 4.5:1 text contrast, and 7:1 for small custom-colored text. Check both appearances with Increase Contrast and Reduce Transparency, separately and together.
- The HIG advises against an app-specific appearance setting. That is a product call; raise it rather than deciding.

## SF Symbols

- Prefer SF Symbols for interface icons. Size them with `.font` so they track Dynamic Type and match adjacent text weight; adjust emphasis with `imageScale`.
- Pair icons with text through `Label`. Pick the rendering mode by legibility at the actual size.
- Build custom symbols from an exported template and give them accessibility labels. Symbols may not appear in app icons or logos.

## Materials and depth

- Where Liquid Glass exists, it belongs to the controls-and-navigation layer above content, never the content layer. System bars and controls adopt it; apply `glassEffect` to custom controls sparingly.
- Default to regular glass. Reserve clear glass for controls over rich media, adding a dark dimming layer over bright media (the HIG suggests 35% opacity).
- In the content layer, use standard materials, ultra-thin through thick; thicker gives text more contrast. Use vibrant label colors on materials, and avoid quaternary labels on thin ones.
- Custom blur or translucency must read `accessibilityReduceTransparency` and become solid when it is on.
