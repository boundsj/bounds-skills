# Interaction and accessibility

Semantic HTML gives most of this for free. Add ARIA only where no native element expresses the behavior; a wrong role is worse than none.

## Targets

- WCAG 2.2 SC 2.5.8 (AA): pointer targets at least 24×24 CSS px. A smaller target still passes when a circle 24 CSS px across, centered on it, intersects neither another target nor another small target's circle. Other exceptions: links inside running text, a function also offered by a compliant control on the same page, browser-default controls the author has not resized, and presentations that are essential or legally required.
- Recommended for touch: 44×44 (SC 2.5.5 AAA and Apple's Human Interface Guidelines); Material uses 48×48 dp.
- Extend a small visual control's hit area with padding or a positioned pseudo-element instead of enlarging the visual. Make sure extended areas do not overlap.

## Hover versus touch

- Gate hover styles with `@media (hover: hover) and (pointer: fine)`. On touch, a tap applies `:hover` and it sticks until the next tap elsewhere. Tailwind v4's `hover:` variant already wraps styles in `@media (hover: hover)`, though not `(pointer: fine)`.
- Anything revealed only on hover (row actions, overflow menus, previews) is unreachable on touch. Show it always on coarse pointers and on `:focus-within`.
- Devices mix inputs, such as touchscreen laptops. Branch on capability queries, never on user agent or screen width.

## Focus

- Never remove the focus outline without an equal replacement. Style `:focus-visible` rather than `:focus`: browsers apply it for keyboard focus and skip most mouse clicks, but text inputs match it on click too, since they take typing either way. Aim for a ring at least 2px thick with 3:1 contrast against adjacent colors (SC 1.4.11). SC 2.4.13 Focus Appearance (AAA) measures the indicator by comparing the same pixels focused and unfocused.
- Focused elements must not be completely hidden behind sticky headers, cookie banners, or chat widgets (SC 2.4.11). `scroll-padding` on the scroller helps.
- Dialogs: move focus in on open and back to the trigger on close. Background content is inert (`inert` attribute, or `<dialog>` with `showModal()`).
- In single-page apps, after a route change move focus to the new page's heading or main region and update `document.title`; otherwise screen reader users get no signal that anything changed.
- When content a user acted on disappears (a deleted row, a closed panel), put focus somewhere sensible, not back at the top of the document.

## Keyboard

- Everything operable by pointer is operable by keyboard (SC 2.1.1), with no traps (SC 2.1.2) and a focus order that preserves meaning and operability (SC 2.4.3), which usually means following the reading order.
- Never use a positive `tabindex`. Use `tabindex="0"` only on custom controls, and `-1` for elements that receive focus programmatically.
- Composite widgets (toolbars, tabs, listboxes, grids, menus) take one tab stop and use arrow keys inside, via roving `tabindex` or `aria-activedescendant`. Follow the APG pattern for the widget.
- Give people a way past repeated blocks (SC 2.4.1): a skip link to the main content, or landmarks and headings that assistive technology can jump between. A skip link also serves sighted keyboard users, who rarely have landmark navigation.
- Keyboard shortcuts: show the right modifier for the platform (⌘ on Apple, Ctrl elsewhere), and avoid single-character shortcuts unless they can be turned off or remapped (SC 2.1.4).

## Screen readers and ARIA

- Every control has an accessible name: visible label, `aria-label`, or `aria-labelledby`. Icon-only buttons are the common miss.
- Expose state: `aria-expanded` on disclosure triggers, `aria-pressed` on toggles, `aria-current` for the current page or step, `aria-selected` in tabs and listboxes.
- Announce asynchronous results (saved, failed, 12 results) through a live region that exists before the update (SC 4.1.3).
- Hide decorative images and icons with `alt=""` or `aria-hidden="true"`. Never put `aria-hidden` on something focusable.
- Test with at least one real screen reader (VoiceOver with Safari, or NVDA with Firefox or Chrome). The accessibility tree in DevTools is a quick check, not a substitute.

## Pointer events

- Give visual feedback on press (`:active`, `pointerdown`), but run the action on release, so a user can slide off to cancel (SC 2.5.2).
- During drags, call `setPointerCapture` so tracking continues outside the element, handle `pointercancel`, and ignore extra pointers once a drag starts.
- Every drag interaction needs a single-pointer alternative, such as buttons or a menu to reorder (SC 2.5.7).
- Set `touch-action` on custom gesture surfaces so the browser keeps the axes you do not handle.

## Reduced motion and other preferences

- Honor `prefers-reduced-motion: reduce` by replacing movement with short opacity changes, not by removing all feedback. See the motion reference.
- Moving, blinking, or scrolling content that starts automatically, lasts more than 5 seconds, and appears alongside other content needs a way to pause, stop, or hide it (SC 2.2.2); so does auto-updating content that starts automatically. Nothing flashes more than three times in any one second unless the flashes stay below the general and red flash thresholds (SC 2.3.1).

Record which assistive technology, browser, and input method each check used. Automated scanners catch only part of the problems; a clean scan is not an accessibility approval.
