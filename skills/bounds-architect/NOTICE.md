# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `architect`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/architect/SKILL.md, with
  `references/design-red-flags.md`, `references/rationale-template.md`, and
  `references/runner-prompt.md`

Retains grounding, usage-first design, data structures and single state ownership,
interface depth, real whole-shape alternatives, the design red flags, the one-page
rationale, and the scrap-and-redesign signals. Adds compatibility and migration
checks, verification through existing interfaces, and a derived-copy-as-authority red
flag. Separates design from scoping. Removes the multi-model arena, fixed minimum
candidate counts, model slugs, mandatory todo phases, automatic implementation after
design, required principle skills, and explicit-only metadata.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
