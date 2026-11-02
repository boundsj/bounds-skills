# Surfaces

Surfaces tell people what sits on what. Keep a short, named set of levels and make every container use one of them.

## Elevation levels

Define a few levels and tie each to a background, a shadow, and a z-index token:

| Level | Typical use |
| --- | --- |
| Base | Page background |
| Raised | Cards, panels, list containers |
| Overlay | Menus, popovers, select lists, tooltips |
| Modal | Dialogs and sheets, with a scrim |
| Notification | Toasts and banners, above the other layers |

- Use a z-index scale (for example 0, 10, 20, 30, 40 mapped to those names) instead of arbitrary values. `isolation: isolate` on a component stops its internal z-index from leaking.
- The native `<dialog>` with `showModal()` and the `popover` attribute render in the top layer, which avoids most stacking fights.
- Higher surfaces get stronger separation, not just a different color.

## Borders or shadows

- A border separates things on the same plane: table cells, inputs, list rows, sidebars. A shadow says something floats above: menus, popovers, dialogs, dragged items.
- An edge color with some transparency blends with whatever lies under it, so one token can serve every surface level; an opaque gray only matches the background it was picked against. A 1px spread `box-shadow` draws the same edge without taking layout space.
- Build depth from more than one shadow: a small, close one where the surface meets the page and a broad, faint one for distance. One big soft shadow reads as a halo rather than height.
- When a border is what identifies an input, it needs 3:1 against the background (WCAG 2.2 SC 1.4.11). Do not swap it for a faint shadow.
- In dark themes shadows nearly disappear. Show elevation with a lighter surface and a faint light edge instead.
- Shadows are dropped in forced-colors mode, so overlays still need a real border there.

## Radius

- Use a small radius scale, for example 4, 8, 12, 16, plus full for pills, and apply it by component size: small controls get smaller radii than the cards that hold them.
- Make nested corners concentric: subtract the padding between the two boxes from the container's radius to get the child's (16px outside with 6px of padding gives 10px inside). Equal radii on both leave the corner gap visibly thinner than the straight sides. When the padding is at least the outer radius, the child can have square corners.
- Mixing sharp and rounded containers in one view reads as unfinished. Whether the product is sharp or soft is a taste call for the human.
- Avoid `overflow: hidden` on a rounded container that holds focusable children; it clips their focus rings. Use an inset ring or padding instead.

## Translucency and blur

- `backdrop-filter: blur()` on a semi-opaque background works for sticky headers, toolbars, and sheets where content scrolls underneath. Older Safari needs the `-webkit-` prefix.
- Check legibility over the worst content that can scroll beneath: photos, dense text, bright colors. Raise opacity until text passes contrast against all of it.
- Provide an opaque fallback with `@supports not (backdrop-filter: blur(1px))`, and honor `prefers-reduced-transparency` where browsers support it.
- Do not stack translucent layers; legibility collapses and blur cost multiplies. Large animated blurs are expensive, especially on phones.

## Dividers

- Try space and grouping first, then a subtle background change, then a line. Many dividers suggest the grouping is wrong.
- In lists with leading icons or avatars, inset the divider to where the text starts, unless the rows are separate objects.
- Keep line weight and color consistent across the product; one divider token, used everywhere.
- A scrolling region under a sticky header can show its edge only once content passes beneath, rather than drawing a permanent line.

## Images and media

- A faint inner outline keeps light images from bleeding into light backgrounds; use a translucent color so it works in both themes.
- Reserve space with `width`/`height` attributes or `aspect-ratio`, and crop with `object-fit: cover`.

Verify surfaces in both themes, at forced colors if the product supports Windows users, and over real content, not empty fixtures.
