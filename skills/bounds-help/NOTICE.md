# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `poteto-help`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/poteto-help/SKILL.md, with `references/prompting.md` and
  `references/recipes.md`

Retains answering help questions without starting the work, one clarifying
multiple-choice question when needed, close-call distinctions, and prompt advice
(goal, done check, proof, known context, constraints). Adds live catalog discovery,
recommendations limited to installed skills, and host-scope honesty. Removes the
static pstack catalog, Cursor setup and model-rule checks, Custom Mode and plugin
instructions, playbook routing, public file links, automatic routing of work
requests into a mode, and explicit-only metadata.

Update from pstack `sharpen` at `792440e8a560a4a3f63748cdee70491ecd412982` (https://github.com/cursor/plugins/tree/792440e8a560a4a3f63748cdee70491ecd412982/pstack/skills/sharpen/SKILL.md): when asked, make a prompt deeper, not bigger, by naming the expert approach, raw material, methods, and an outside check, then rewriting the prompt, with experiments for choices they can settle and preference choices left to the user.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
