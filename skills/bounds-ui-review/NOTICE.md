# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Emil Kowalski's MIT-licensed skills, revision
`a81dbca07f2217b7103e510c0f13f8d5b017afc9`:
- `break-ui` (with `CATALOG.md`): https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/break-ui
- `review-animations`: https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/review-animations
- `emil-design-eng` (motion rules): https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/emil-design-eng

Retains the stress-test method: an inventory of rendered values, realistic
worst-case data changed at the data rather than the component, a debug-only
toggle, report first and fix on request, cause and fix tables, and what held
up. Retains motion checks for purpose, frequency, easing, origin,
interruptibility, reduced motion, and composite-only properties, as working
defaults rather than blockers. Adds an evidence pin with runtime geometry,
lenses chosen per change, severity derived from `bounds-review`, a verdict with
separate source, device, and human-decision lists, explicit approval scope,
harness removal by default, platform-guideline fallbacks, and fixes only when
the user authorizes them.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt).
