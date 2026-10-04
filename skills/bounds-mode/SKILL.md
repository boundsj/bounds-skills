---
name: bounds-mode
description: "Coordinate a task with Bounds workflows when the user explicitly asks for bounds-mode. Select only the skills needed for the current work."
license: MIT
disable-model-invocation: true
---

# Bounds mode

Use this entrypoint only when explicitly requested. Optimize for accepted work per minute of human attention: preserve the task, resolve routine details from evidence, and keep small requests small. This skill adds no permissions or external actions.

## Route the task

Read the relevant project instructions and available skill descriptions. Load a supporting skill's body only when its phase is needed, using the host's skill mechanism or its discovered file path. References are conditional too.

| Need | Skill |
| --- | --- |
| Material scope, behavior, or dependency decisions | `bounds-plan` |
| An observed failure or regression | `bounds-debug` |
| A requested review or consequential implementation to check | `bounds-review` |
| Repeated corrections or avoidable work to examine | `bounds-retro` |
| Agent documentation to create or repair | `bounds-agent-docs` |
| A reusable project verification recipe to establish | `bounds-create-verification` |
| An existing recipe or feature map to refresh | `bounds-maintain-verification` |

A typo needs a direct edit and a quick inspection. A feature may need a short plan, implementation, a behavior check, then review. A bug starts with reproduction. A request for a plan or review ends with that deliverable; it does not authorize implementation. Preserve relevant specialist skills and native tools.

Carry authorized implementation through the agreed acceptance checks. Use the project's existing verification recipe when useful; creating one is a separate need, not a compulsory phase. Report the outcome, actual evidence, and consequential gaps. A short command/result is enough for a small change. Use independent review when warranted, available, and permitted by existing user and host instructions, under `bounds-review`'s bounded protocol. Reuse authorization already granted.

If a selected skill is absent, say which one. Continue with the available tools when feasible, without pretending it loaded or installing dependencies unasked.

## Continuity

Honor opt-out immediately. Follow the user's continuing task while context retains it; there is no portable sticky-mode switch. Do not persist a mode setting or modify standing instructions. For invocation, fresh-session discovery, or host limitations, read [host behavior](references/hosts.md).
