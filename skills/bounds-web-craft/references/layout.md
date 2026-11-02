# Layout

Layout decides what belongs together and what matters most before anyone reads a word. Get spacing and grouping right first; decoration cannot fix a weak structure.

## Spacing scale

- Use one scale on a 4px base, for example 4, 8, 12, 16, 24, 32, 48, 64, 96, in `rem` so it grows with text. Every margin, padding, and gap comes from it.
- Space inside a group must be clearly smaller than space between groups: roughly 8 between a label and its field, 24 or more between fields that belong to different sections. When everything is spaced equally, nothing is grouped.
- Prefer `gap` on flex and grid parents over margins on children; it removes first- and last-child exceptions.

## Alignment

- Align to a few shared edges. Every new left edge is something the eye must reconcile.
- Align text by baseline where labels and values sit side by side. Right-align numbers in tables so digits line up, with tabular numerals.
- Icons and glyphs often need optical correction: a play triangle looks off-center when mathematically centered, and round shapes look smaller than square ones at the same size. Adjust by eye and check at actual size.
- Icon and text pairs: size icons to the text's cap height or line height, and center them on the line, not on the box.

## Grouping and hierarchy

- Use proximity and headings before boxes. Cards around everything flatten hierarchy and waste space.
- Each view has one primary action. Make it the most prominent through size, weight, color, and position; demote the rest.
- Put controls next to what they affect. A filter far from its list, or a save button far from its form, forces people to search.
- Order content by what people need first, not by data model order.

## Density

- Dense data views (tables, inboxes, admin tools) can use tighter rows, about 32 to 40px, and smaller text, as long as targets still meet 24×24 CSS px (WCAG 2.2 SC 2.5.8) and text stays legible.
- Consumer and onboarding views get more room. If the product needs both, implement density as a token switch, not as separate components.
- Which density the product uses is a product call for the human.

## Responsive behavior

- Start from the narrowest layout and add structure as space allows. Add a breakpoint at the width where the layout stops working, whatever device that happens to be.
- Content must reflow at 320 CSS px wide without horizontal scrolling (SC 1.4.10), except content that is inherently two-dimensional, such as data tables and maps. That width is also what 1280px at 400% zoom looks like.
- Use container queries (`container-type: inline-size` with `@container`) for components that appear in both wide and narrow slots, such as a card in a main column and in a sidebar.
- `grid-template-columns: repeat(auto-fit, minmax(min(16rem, 100%), 1fr))` gives a responsive grid with no breakpoints that still fits containers narrower than 16rem.
- Cap reading width on wide screens. Content stranded across 2560px is as broken as content crushed at 320px.
- Avoid fixed heights on anything containing text; translation, zoom, and user data all make text taller.
- Use logical properties (`margin-inline-start`, `padding-block`) so layouts mirror correctly in right-to-left languages.

## Foundations that prevent shifts

- `scrollbar-gutter: stable` on scroll containers stops content from jumping when a scrollbar appears.
- Give media `aspect-ratio` or explicit dimensions so it never pushes content down on load.
- With sticky headers, set `scroll-padding-top` on the scroll container so anchor jumps and focused elements land below the header.
- Keep breakpoints, spacing, and container widths as tokens beside the type and color tokens.

## Verify

Resize continuously from 320px to the widest supported width and watch for overlaps, orphaned elements, and awkward intermediate states between breakpoints. Repeat at 200% zoom, with long translated strings, and with right-to-left text if the product supports it. Record the measured viewport widths you checked.
