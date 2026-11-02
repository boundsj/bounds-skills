# Performance

People judge speed by how soon something responds, whether the page holds still, and whether motion is smooth. Measure before changing code, and name the cause each fix addresses.

## Targets

| Measure | Good | Poor |
| --- | --- | --- |
| Largest Contentful Paint | ≤ 2.5s | > 4s |
| Interaction to Next Paint | ≤ 200ms | > 500ms |
| Cumulative Layout Shift | ≤ 0.1 | > 0.25 |

Core Web Vitals are judged at the 75th percentile of real page loads, so a fast development machine says little. Lab tools (DevTools Performance panel, Lighthouse) find causes; field data confirms the fix.

## Perceived speed

- Acknowledge input within about 100ms: a pressed state, an optimistic update, or a pending indicator. Run the slow work afterward.
- For operations that usually finish in under about 300ms, show nothing; a spinner that flashes reads as a glitch. For longer waits, use a skeleton shaped like the final layout, and show progress past a few seconds.
- Optimistic updates need a visible rollback path when the server disagrees.
- Prefetch the likely next route or data on hover or intent where the framework supports it.

## Layout shift

- Give images, video, iframes, and embeds `width` and `height` attributes or `aspect-ratio`.
- Reserve space for content that arrives late: ads, banners, async panels, error messages. Never insert content above what the user is reading unless they asked for it.
- Font swaps shift text. Match the fallback's metrics with `size-adjust` and the `*-override` descriptors, or use `font-display: optional`.
- Do not change font weight, border width, or padding on hover or selection.

## Animation frame budget

A frame has about 16.7ms at 60Hz and about 8.3ms at 120Hz, shared with everything else the page does. Design against the smaller number.

- Animate `transform` and `opacity`; they skip layout and paint. Animating `width`, `height`, `top`, `left`, `margin`, or `padding` re-lays out the element and often its neighbors every frame. Use `scale()` and `translate()` instead.
- Never write `transition: all`; list the properties.
- Animating `box-shadow` forces a paint on every frame. For a hover lift, put the final shadow on a pseudo-element and transition only its `opacity`.
- JavaScript animation runs on the main thread and stutters while the page loads or hydrates. CSS transitions and the Web Animations API can run on the compositor for `transform` and `opacity`. Libraries that animate individual transform shorthands through CSS variables lose that; animate a full `transform` value when motion must survive a busy page.
- Setting a CSS custom property on a parent recalculates styles for every descendant. Set `transform` on the moving element directly.
- In React, do not drive per-frame motion through state. Write to a ref's `style` or use the animation library's own values.
- Keep animated `blur()` small (under about 20px); large blurs are costly, especially in Safari.
- Add `will-change: transform` only to fix an observed problem, on the element that animates, and remove it when idle. Every promoted layer costs memory.

## Images and fonts

- Serve responsive images with `srcset` and `sizes`, in AVIF or WebP with fallbacks, sized for display.
- Do not lazy-load the hero or other LCP image. Give it `fetchpriority="high"`; use `loading="lazy"` below the fold.
- Subset fonts, ship WOFF2, preload only the one or two used above the fold, and limit weights.

## Long lists and heavy views

- Virtualize lists beyond a few hundred rows, while keeping find-in-page, keyboard navigation, and screen reader counts working (`aria-rowcount`, `aria-setsize`).
- `content-visibility: auto` with `contain-intrinsic-size` skips rendering off-screen sections.
- Pause timers, polling, video, and animations when off-screen or when the tab is hidden.

## Input latency

- Break long tasks (over 50ms) so input can run between them: yield to the event loop, move work to a Web Worker, or defer non-urgent rendering (React's `useTransition` and `useDeferredValue`).
- Keep event handlers small. Register `touchstart`, `touchmove`, and `wheel` listeners with `{ passive: true }` when they never call `preventDefault()`, so scrolling does not wait for them; `scroll` events cannot block scrolling, so the option does nothing there. Debounce expensive derived work, never the visible response.

## Verify

Profile on a mid-range phone over remote debugging, or with CPU throttling as a weaker stand-in, and say which. Report the workload, build mode (production, not development), device, and the before and after numbers from comparable runs. A single fast run is weak evidence.
