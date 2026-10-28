# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `how`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/how/SKILL.md, with `references/explorer-prompt.md` and
  `references/explainer-prompt.md`
- `teach`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/teach/SKILL.md

Joins runtime explanation with plain teaching in one skill. Retains complexity
sizing, a concrete flow with file anchors, boundaries, gotchas, plain-definition-first
explanation sized to the reader's purpose, and build-up diagrams. Adds an explicit
entrypoint, data and state, ownership, boundary, and failure-path trace, and separates
observed behavior from rationale hypotheses. Removes mandatory explorer and explainer
subagents, model slugs, required `how`/`why`/`unslop` invocations, required
image-generation tools, and explicit-only metadata.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
