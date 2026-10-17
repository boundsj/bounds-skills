# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack, revision
`101b274dd991f694e1f7024be2157e5f3adf07de`:
- `blast-radius`: https://github.com/cursor/plugins/blob/101b274dd991f694e1f7024be2157e5f3adf07de/pstack/skills/blast-radius/SKILL.md

Retains the focus on breakage beyond the diff, the single load-bearing safety fact,
the proof ladder from assertion to reproduction, cited risks, a cleared list, and the
cheapest pre-merge check. Adds revision pinning, an explicit checklist of shared state,
client contracts, caches and pagination, cancellation and late completion,
serialization and migrations, and data leakage, plus authorization and honest
reporting of unexecuted checks. Removes the multi-model arena step, required sibling
skills, framework-specific examples, and explicit-only metadata.

Workflow design was informed by a private, generalized summary of one user's
engineering practices. No transcripts, private links, host addresses, or personal
project details are distributed. Integrations remain optional.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
