# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `bro`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/bro/SKILL.md

Retains a short plain-language restatement of the previous message. Adds support
for user-supplied text, preservation of decisions, consequential caveats, and the
next step, and a rule against resuming work. Removes explicit-only metadata.

Update from Matt Pocock's MIT-licensed `wait-what` at `abeeaf95660ba9e8b7c753eb38f441ca707a8823` (https://github.com/mattpocock/skills/tree/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/wait-what): an optional ASD-STE100 Simplified Technical English restatement. Bounds keeps only its core sentence rules and applies them on request or by standing preference; it drops the glossary lookup and explicit-only metadata.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
