# Mobile web

A web app feels like a website on a phone because of a handful of platform details: viewport height, tap feedback, zoom, scroll chaining, safe areas, and browser chrome. Most fixes are one declaration. Gate by capability (`hover`, `pointer`, `env()`), never by user agent or screen width.

## Baseline

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
```

```css
html {
  -webkit-tap-highlight-color: transparent;
  -webkit-text-size-adjust: 100%;
}
input, textarea, select { font-size: max(16px, 1rem); }
button, a, [role="button"] { touch-action: manipulation; }
```

Never add `user-scalable=no` or `maximum-scale=1`; blocking zoom fails WCAG 2.2 SC 1.4.4.

## Symptoms and fixes

| Symptom | Fix |
| --- | --- |
| Bottom bar hidden under the browser toolbar | `100dvh` for app shells; `100svh` for a first-screen hero so it does not resize mid-scroll. Plain `vh` equals the largest viewport. |
| Gray or blue flash on tap | Transparent tap highlight, plus your own `:active` state so feedback remains |
| Hover style stuck after tap | Wrap hover rules in `@media (hover: hover) and (pointer: fine)` |
| Page zooms when an input is focused | iOS Safari zooms inputs under 16px; raise the size |
| Taps feel late | With `width=device-width`, modern mobile browsers add no 300ms tap delay, so look for missing feedback or slow handlers: show `:active` or `pointerdown` feedback and keep handlers short. `touch-action: manipulation` on controls still stops rapid repeat taps from zooming |
| Pull-to-refresh or rubber band fights the app | `overscroll-behavior: none` on the root of an app-like page; `contain` on inner scrollers so they keep their own bounce |
| Content hidden by the notch or home indicator | `viewport-fit=cover`, then pad fixed bars with `env(safe-area-inset-top)` and `env(safe-area-inset-bottom, 0px)`; without the meta tag the insets are zero |
| Long-press selects button labels | `user-select: none` (with the `-webkit-` prefix) on controls only, never on content people may copy |
| Horizontal carousel jitters the page vertically | `touch-action: pan-y` on the track, or native `scroll-snap-type: x mandatory` |
| Browser toolbar or status bar color mismatched | See browser chrome color below |

## Software keyboard

- By default, an open keyboard shrinks only the visual viewport. With `interactive-widget=resizes-content`, Chrome on Android shrinks the layout viewport as well, so `dvh` layouts and inputs pinned to the bottom move with it. For a composer that must sit exactly on top of the keyboard, read sizes from the `visualViewport` API.
- On touch devices, let people decide when to type. Focusing a field on load raises the keyboard over much of the page before they have seen it.
- Set `inputmode`, `autocomplete`, and `enterkeyhint` so the right keyboard appears; see the forms reference.

## Browser chrome color

- Browsers disagree here. Some Chromium-based browsers on Android, and installed web apps on some platforms, read `<meta name="theme-color">`; give one per color scheme with a `media` attribute, matching the top of the page, and update it from script if the theme toggles by class. Recent Safari ignores the tag and tints from the page background or from fixed elements at the top edge, and Firefox does not support it.
- So make the page and any fixed header backgrounds correct first, treat `theme-color` as an extra for the contexts that read it, and verify on each target browser.

## Media and gestures

- Inline video that should autoplay needs `muted` and `playsinline`, plus a poster. Respect reduced motion and data-saving preferences.
- Custom gestures use Pointer Events with pointer capture, specify `touch-action` for the axes the browser keeps, and need a non-drag alternative (WCAG 2.2 SC 2.5.7).
- Targets at least 24×24 CSS px (SC 2.5.8); 44×44 is the comfortable size for thumbs.

## Installed web apps

- In a manifest with `display: standalone`, set `theme_color` and `background_color` to match the first screen, and provide maskable icons.
- Standalone mode removes browser back and reload: provide in-app navigation and a way to refresh. Safe areas and status bar overlap change; retest them.
- iOS reads `apple-mobile-web-app-status-bar-style` for the status bar in standalone mode.

## Test on hardware

Desktop device emulation does not reproduce sticky hover, tap highlight, toolbar resizing, input zoom, overscroll, safe areas, or the keyboard. Serve the dev build on the local network, open it on a phone, and inspect with Safari Web Inspector (iOS) or `chrome://inspect` (Android). Include an older mid-range phone, landscape once, the keyboard open, and the installed app if that is a target. Report which checks ran on which device, OS, and browser, and which were verified only from code.
