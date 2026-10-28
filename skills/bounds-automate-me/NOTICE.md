# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `automate-me`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/automate-me/SKILL.md

Retains drafting or updating one working-style skill, update-in-place behavior,
repeated-evidence thresholds, minimal operational sections, generic naming, and a
read-back with the user. Adds evidence limited to explicit preferences and named,
bounded sources, separation of accepted conventions from one-off instructions, a
privacy check, and no global configuration, installation, or rollout. Removes
workspace-wide transcript mining, parallel mining subagents, Cursor paths and
built-in skill dependencies, mandatory structured question rounds, required commit
and PR landing, and a default explicit-only flag on the generated skill.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
