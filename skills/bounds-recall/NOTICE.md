# Attribution

This is a Bounds adaptation, not an upstream installation.

Selected source: Lauren Tan's MIT-licensed pstack `recall`, revision
`182f2ce414e83224915c190d2f63239c1608d0a5`:
https://github.com/cursor/plugins/blob/182f2ce414e83224915c190d2f63239c1608d0a5/pstack/skills/recall/SKILL.md

Retains bounded history retrieval, shared-record reconciliation, live-state checks,
and a concise current-state brief. Adds Codex/Claude/T3 source discovery, explicit
host identity and coverage, permission chronology, duplicate-source handling, and
separate review/merge/deployment/acceptance evidence. Removes Cursor-only paths,
mandatory fan-out, fixed model choices, rigid status tags, explicit-only metadata,
and dependencies on `why`, `poteto-mode`, `session-pickup`, and `unslop`.

Workflow design was informed by a private, bounded sample of agent history and a
development journal. No transcripts, private links, host addresses, or personal
project details are distributed. Integrations remain optional.

Full Bounds and upstream notices are in [LICENSE.txt](LICENSE.txt). The bundle
also retains Matt Pocock's MIT notice for consistency with its existing packages.
