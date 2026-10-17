# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `ketchup`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/ketchup/SKILL.md

Retains a read-only catch-up anchored at the user's last message, current-state
rechecks, user-owned action items with a recommendation, and plain status lines.
Adds an explicit boundary with cross-session recall, child-work and liveness checks,
and separate implemented, reviewed-at-revision, merged, deployed, and accepted
states. Removes the required sibling voice skill, mandatory visuals and visualization
tools, rigid word and box limits, slash-command-only invocation, and explicit-only
metadata.

Workflow design was informed by a private, generalized summary of one user's
engineering practices. No transcripts, private links, host addresses, or personal
project details are distributed. Integrations remain optional.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
