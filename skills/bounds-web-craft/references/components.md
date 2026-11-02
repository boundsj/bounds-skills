# Components

Use native elements first, then the project's accessible primitives, and hand-build only what neither provides. The WAI-ARIA Authoring Practices Guide (APG) defines expected keyboard behavior for each widget below.

## Every state

Design and check each interactive component in all of these, with the worst realistic content:

| State | Requirement |
| --- | --- |
| Default | Identifiable as interactive without hover |
| Hover | Pointer devices only; see the interaction reference |
| Focus-visible | Clear ring with 3:1 contrast, never removed without a replacement |
| Active (pressed) | Immediate feedback on press, not on release |
| Disabled | Explained nearby when the reason is not obvious |
| Loading | Keeps its size; blocks duplicate actions; announces completion |
| Empty | Says what belongs here and how to add it |
| Error | Says what went wrong and what to do next, without losing user input |
| Selected or current | Not conveyed by color alone |

Worst-case content: long unbroken names and emails, one-letter names, missing optional fields, 0, 1, and 1,000+ items, translations that double or triple short labels and add about 30% to longer text, right-to-left text, failed images, and every status value at once. Change the data at the fixture or API boundary, not the markup.

## Buttons

- `<button type="button">` for actions, `<a href>` for navigation. Inside forms, set `type` explicitly; the default is `submit`.
- Loading: keep the width fixed (overlay a spinner or keep the label), ignore repeat activation, and announce completion or failure through a live region.
- Prefer leaving a button enabled and explaining what is missing on activation. A disabled button cannot be focused, so its reason is invisible to keyboard and screen reader users. If it must be inert, `aria-disabled="true"` keeps it focusable.
- A button that shows only an icon still needs a name screen readers can announce: `aria-label`, or text hidden visually but kept in the accessibility tree.

## Menus and popovers

- An action menu uses the APG menu button pattern: Enter or Space opens it, arrow keys move between items, and Escape closes it and returns focus to the trigger. Opening with Down Arrow and type-ahead are optional in the pattern; add them for long menus. Site navigation is a list of links, not `role="menu"`.
- Popovers anchor to their trigger, flip or shift at viewport edges, and close on Escape and outside click. The `popover` attribute provides top-layer rendering and light dismiss natively.
- A handful of options often works better as visible radio buttons; long option lists need search.

## Dialogs

- Use `<dialog>` with `showModal()`: it renders in the top layer, makes the rest of the page inert so focus stays inside, and closes on Escape.
- On open, focus the first useful control, or the dialog itself if the content must be read first. On close, return focus to the trigger.
- Label it with its heading (`aria-labelledby`). Lock background scroll, and ensure the dialog itself scrolls at small heights.
- Confirmation dialogs name the action on the button ("Delete project"), not "OK". Reserve them for destructive or irreversible actions; prefer undo elsewhere.

## Toasts

- Announce through a live region (`role="status"` for routine, `role="alert"` only for urgent). Create the region before inserting messages.
- Never put the only path to an action or critical information in a toast. Pause dismissal timers on hover, on focus, and while the tab is hidden; an action that vanishes before people can reach it can fail WCAG 2.2 SC 2.2.1.
- Stack and cap them.

## Tooltips

- Supplemental labels only, never essential or interactive content. Show on hover and on keyboard focus, keep visible while hovered, and dismiss with Escape (SC 1.4.13).
- Delay the first tooltip briefly; once one is open, neighbors can open instantly.
- They do not work on touch. Anything a touch user needs must be visible or in the accessible name.

## Tables

- Use `<table>` with `<th scope>` and a `<caption>` or labelled heading. Right-align numbers with tabular numerals.
- Wide tables scroll in their own container (`overflow-x: auto`) with a focusable, labelled region so keyboard users can scroll it. Keep a sticky header for long tables; inside a scroll container it sticks to the container, not the page.
- Row actions revealed only on hover are unreachable on touch and invisible to keyboard users; show them on focus-within and on coarse pointers.
- Design the empty, loading, error, and no-results states.

## Tabs

- APG tabs: `role="tablist"`, `tab`, and `tabpanel`; arrow keys move between tabs; only the active tab is in the tab order. Activate on focus when panels are cheap; require Enter or Space when switching is expensive.
- Tabs switch views within a page. If each tab changes the URL and loads a page, it is navigation and should be links with `aria-current="page"`.
