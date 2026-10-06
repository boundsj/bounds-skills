# Sources and adaptations

Bounds adapts selected workflows from two MIT-licensed sources. These revisions are the source contract for 0.1.0. One later document informs `bounds-retro`, recorded below; no newer workflow material was substituted.

- [Matt Pocock's skills](https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888), revision `24fe0ef7737efae15c87225755e9f6f5965e4888`. [Original MIT notice](licenses/Matt-Pocock-MIT.txt), copyright 2026 Matt Pocock.
- [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack), revision `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a`. [Original MIT notice](licenses/Lauren-Tan-MIT.txt), copyright 2026 Lauren Tan.

| Bounds skill | Selected source material | Adaptation |
| --- | --- | --- |
| bounds-mode | pstack `poteto-mode`, `principle-guard-the-context-window` | Thin explicit router; task-sized phases and conditional references. Removes broad hooks, automatic publication, sticky-mode metadata, and fixed model choices. |
| bounds-plan | Pocock `to-spec`, `to-tickets`, `tdd` | Retains scope, observable acceptance, verifiable slices and dependency edges. Adds retained behavior; removes required tracker setup, exhaustive stories, ticket publication and seam approval. |
| bounds-debug | Pocock `diagnosing-bugs`, `tdd`; pstack `principle-test-behavior-not-implementation` | Keeps symptom-specific feedback, falsifiable probes and regression evidence. Allows proportionate diagnosis and honest partial progress without mandatory hypothesis counts. |
| bounds-review | Pocock `code-review`; pstack `interrogate` | Checks requirements, maintainability and correctness. Pins revisions, supports local snapshots, defaults to one warranted independent reviewer and bounds re-review. Removes model tables and unconditional fan-out. |
| bounds-retro | Pocock `retro` and its retro documentation (see below); pstack `correct`, `principle-encode-lessons-in-structure` | Bounded accessible evidence, structural improvements before standing instructions. Keeps retro's fix destinations, mechanical-check-first classification, reviewer-owned standards and moment-traceable candidates. Adds human-attention ranking, multi-provider attribution and a conditional reference for user-named session records. Removes automatic global edits, recurring rule tables, compulsory fixes and the required writing-style skill load. |
| bounds-agent-docs | Pocock `writing-for-agents`; pstack `principle-guard-the-context-window` | Short entrypoints, conditional pointers, observable completion and pruning. Uses portable distribution boundaries without universal word/style rituals. |
| bounds-create-verification | pstack `create-verification-skill` | Keeps Launch, Doctor, Drive, Evidence, Cleanup and an executed feature map. Uses project conventions or local docs instead of a fixed Cursor path; supports small maps and scoped startup blockers. |
| bounds-maintain-verification | pstack `maintain-verification-skill` | Keeps live coverage, cleanup invariants and drift/gap/defect triage. Allows affected-feature maintenance, bounded retries and honest partial coverage without mandatory per-feature agents or PRs. |

`bounds-retro` also draws on Pocock's [retro documentation](https://github.com/mattpocock/skills/blob/4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d/docs/engineering/retro.md) at revision `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d`. Its known limits are one-session judgement, unpruned checks and generic advice. The retro `SKILL.md` at that revision is identical to the pinned one.

Source directories in Pocock's tree are `skills/engineering/` for the engineering workflows and `skills/productivity/` for `writing-for-agents`. Pstack workflows are under `pstack/skills/`.

Both upstream notices are reproduced verbatim in `licenses/` and every installed skill's `LICENSE.txt`, alongside the Bounds MIT notice. Each skill also carries `NOTICE.md`, so selective installation preserves attribution. These files are packaging records, not references every invocation must load.

[Vercel's skills CLI](https://github.com/vercel-labs/skills) is an external installer, not vendored code. Validation pins the npm distribution `skills@1.7.0`. Provider metadata follows the local skill-creator guidance, Codex runtime behavior, and [Claude Code's skills documentation](https://code.claude.com/docs/en/skills). Runtime results and limits are recorded separately in [validation](docs/validation.md).
