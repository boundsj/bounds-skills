# Marketing pages

A marketing page has one job: help a visitor understand what this is, believe it, and take the next step. Positioning, claims, and voice belong to the human. Draft and recommend, but do not invent customer names, numbers, quotes, or awards.

## Page structure

A sequence that works for most product pages, to be adapted rather than followed:

1. **Hero:** what it is, who it is for, the primary action.
2. **Proof:** evidence that it works for people like the visitor.
3. **How it works:** the few capabilities that matter, each tied to an outcome.
4. **Objections:** pricing clarity, security, migration, FAQ.
5. **Closing action:** the same primary action, restated.

Every section should answer a question a visitor has at that point. Cut sections that only exist because other sites have them.

## Hero

- A headline that states the outcome in plain words, with a supporting line that says what the product is. Clever with no meaning loses to plain and specific.
- Show the real product: a screenshot, a short loop, or an interactive demo. Abstract illustration explains nothing.
- One primary action and at most one secondary. The primary should be visible without scrolling at common phone and laptop sizes; check at measured viewports.
- If the hero fills the screen, size it with `100svh` rather than `100vh` or `100dvh`, so it never hides behind the mobile toolbar or resizes while scrolling.

## Proof

- Specific beats general: a named outcome with a number and a source beats "loved by teams everywhere."
- Testimonials need a real name, role, and context, with permission. Logos need permission too.
- Put proof near the claim it supports, not in a single block far down the page.

## Calls to action

- Labels say what happens next: "Start free trial," "Book a demo," "Read the docs." Avoid vague labels like "Submit" or "Learn more" when a specific one fits.
- One visual style for the primary action across the page; secondary actions are visibly quieter.
- Mention friction removers next to the button (no card required, cancel anytime) only when they are true.
- Links and buttons follow the same rules as product UI: real `<a>` and `<button>` elements, focus styles, and targets of at least 24×24 CSS px.

## Readable copy blocks

- Keep line length around 45 to 75 characters, with body text at 16px or larger and line height about 1.5. Headings that a scanner can read alone carry the page.
- Short paragraphs, one idea each. Lists for parallel items, tables for comparisons.
- Use one `h1`, then headings in order, so screen reader users and search engines get the same outline.
- Check contrast over images and gradients at their weakest point.

## Media and performance

- The hero image or video poster is usually the LCP element: do not lazy-load it, give it `fetchpriority="high"`, explicit dimensions, and modern formats.
- Background video: `muted`, `playsinline`, a poster, a pause control if it runs longer than 5 seconds (WCAG 2.2 SC 2.2.2), and a static fallback under reduced motion or data saving.
- Defer third-party scripts (chat, analytics, embeds) until after load or interaction; they usually cost more than the page itself.
- Pre-render static pages at build time where the stack allows.
- Set a page title, meta description, canonical URL, and social preview image.

## Motion

Marketing pages have more room for motion than product UI, but scroll reveals on every section hold content back from fast scrollers and repeat on every visit. Prefer one considered moment, such as a hero entrance or a demo that explains a feature, and keep everything readable with reduced motion on.

## Verify

Load the page on a real phone over a throttled connection and check where the primary action sits, how the hero looks before fonts and images finish, and whether anything shifts. Run Lighthouse or field data for LCP and CLS, and say which. Test both themes if the site supports them. Report claims and numbers that still need the human's confirmation.
