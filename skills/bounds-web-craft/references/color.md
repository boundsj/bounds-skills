# Color

Separate the palette (raw values) from roles (what a value is for). Components reference roles; themes reassign them.

## Palette and roles

- Build each hue as a tonal ramp of about 10 to 12 steps from near-background to near-text. Define it in `oklch()` where the project allows; its lightness channel is close to perceptual, so equal steps look equal and hue stays stable as lightness changes. HSL ramps drift in perceived brightness across hues.
- Name roles by job, not by value: `--bg`, `--surface`, `--surface-raised`, `--text`, `--text-muted`, `--border`, `--accent`, `--accent-text`, `--focus`, plus `--success`, `--warning`, `--danger`, and `--info`, each with fill, text, and border variants.
- One accent color carries interaction. If everything is colored, nothing is.
- Neutrals tinted slightly toward the accent hue read as more deliberate than pure gray. How much is a taste call.

## Contrast (WCAG 2.2)

| Content | AA minimum |
| --- | --- |
| Body and UI text | 4.5:1 (SC 1.4.3) |
| Large text: at least 24px regular or about 18.7px bold | 3:1 |
| Visual parts needed to identify a control or its state (such as a field's only border), icons, focus indicators, chart marks needed to understand content | 3:1 against adjacent colors (SC 1.4.11) |

- AAA (SC 1.4.6) is 7:1 and 4.5:1. Disabled controls and pure decoration are exempt, but a disabled control should still be legible enough to recognize.
- Check contrast with colors as rendered, not as specified: the text against the surface it actually sits on, in hover and selected states, and after translucent layers composite.
- Placeholder text, muted captions, and borders on inputs are the usual failures.
- APCA is a newer method that models perception better at small sizes and in dark themes. It is not part of WCAG 2.2; it can inform choices, but conformance is judged against the ratios above.

## Dark mode

- Swap role values under one selector or media query; do not scatter per-component overrides.
- Set `color-scheme: light dark` so native controls, scrollbars, and form fields follow the theme. `light-dark()` can pair values inline where supported.
- Use a near-black background rather than pure black for large reading surfaces, and off-white text. Express elevation as lighter surfaces, since shadows barely show on dark backgrounds.
- Lower the chroma of saturated accents; they glow and vibrate on dark backgrounds. Recheck every contrast pair: a hue that passes on white often fails on near-black, and the reverse.
- Offer light, dark, and system. Apply the stored choice before first paint, with a small inline script or a server-rendered attribute, so there is no flash. Suppress transitions for the frame the theme flips, or every element with a color transition animates at once.
- Check logos, illustrations, and screenshots in both themes.

## State colors

- Never rely on color alone (SC 1.4.1). Pair status with an icon, a text label, or a pattern.
- Bright yellow and orange rarely reach 4.5:1 as text on white. Use a darker step for text and the bright step for fills.
- Keep state colors meaningful: red is not decoration, and success green is not a brand accent.

## Color vision deficiency and forced colors

- Color vision deficiency, mostly red-green, affects roughly 1 in 12 men. Do not encode meaning by a red/green difference alone, especially in charts and diffs. Vary lightness as well as hue and add direct labels.
- Use the browser's vision-deficiency emulation, Chromium's Rendering panel for example, as a quick check.
- In `@media (forced-colors: active)`, author colors and `box-shadow` are replaced. Focus rings drawn only with `box-shadow` vanish; draw them with `outline`, or add a transparent outline that forced colors make visible.
- Respect `prefers-contrast: more` with stronger borders and text where the system offers it.

## Gradients

- Interpolate in a perceptual space to avoid a gray middle between distant hues: `linear-gradient(in oklch, ...)` where supported, or add intermediate stops.
- Long, subtle gradients band. More stops or a faint noise texture hides it.
- Text over a gradient or image must pass contrast at its weakest point. Add a scrim or a solid backing instead of hoping.
- `background-clip: text` gradients need a solid `color` fallback and still must meet contrast.

Brand colors, accent choice, and neutral temperature belong to the human. Flag a brand value that cannot meet contrast and offer the nearest step that does.
