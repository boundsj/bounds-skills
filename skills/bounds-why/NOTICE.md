# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `why`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/why/SKILL.md, with `references/epistemics.md`,
  `references/investigator-prompt.md`, `references/synthesizer-prompt.md`, and
  `references/sources/code-archaeology.md`

Retains the code anchor, repository-history techniques, confidence tiers, tested
embedded hypotheses, explicit gaps and contradictions, a sources-consulted record, and
Preserve/Change/Avoid/Risk constraints. Condenses the epistemics guidance into one
reference. Adds prompt-injection caution for external records and private-citation
handling. Removes compulsory connector discovery, one-investigator-per-category
fan-out, the separate synthesizer, per-service playbooks, model slugs and role
files, read-only mode workarounds, and explicit-only metadata. Optional sources are
consulted only where their evidence fits the question.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
