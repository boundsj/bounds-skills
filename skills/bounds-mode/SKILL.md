---
name: bounds-mode
description: "Coordinate a task with Bounds workflows when the user explicitly asks for bounds-mode. Select only the skills needed for the current work."
license: MIT
disable-model-invocation: true
---

# Bounds mode

Use only when explicitly requested. Optimize for accepted work per minute of human attention: preserve the task, resolve routine details from evidence, and keep small requests small. This skill adds no permissions or external actions.

## Route the task

Read relevant project instructions and skill descriptions. Load a supporting skill's body only when its phase is needed, and references conditionally.

| Need | Skill |
| --- | --- |
| Scope, behavior, or dependencies to decide | `bounds-plan` |
| An observed failure or regression | `bounds-debug` |
| A review, or consequential work to check | `bounds-review`; council on request: `bounds-council`; UI experience: `bounds-ui-review` |
| Authorized work to finish through PR readiness | `bounds-ship` |
| A stale or inherited PR | `bounds-modernize` |
| Authorized GitHub comments | `bounds-leaving-pr-comments` |
| Prior decisions or unfinished work | `bounds-recall` |
| Repeated corrections or wasted work | `bounds-retro` |
| Agent documentation | `bounds-agent-docs` |
| A new project verification recipe | `bounds-create-verification` |
| An existing recipe or feature map | `bounds-maintain-verification` |
| Progress since the user's last message | `bounds-ketchup` |
| Work to pause or pass to another agent | `bounds-handoff` |
| An external fact a decision waits on | `bounds-research` |
| Rationale behind existing code | `bounds-why` |
| Downstream effects of a change | `bounds-blast-radius` |
| A measured number to vet before reporting | `bounds-measure` |
| A code walkthrough | `bounds-how` |
| Interfaces and state ownership | `bounds-architect` |
| Requested prose to tighten | `bounds-unslop` |
| A reusable working-style skill | `bounds-automate-me` |
| An idea or plan to stress-test | `bounds-grill` |
| An open design direction | `bounds-options` |
| A felt value that keeps missing | `bounds-dial` |

Keep phases proportional: inspect a typo directly; reproduce a bug first. A plan or review request ends with that deliverable, not implementation. Preserve specialist skills, such as installed craft skills, and native tools.

Carry authorized implementation through the agreed acceptance checks, using the project's verification recipe when useful; creating one is a separate need. Report the outcome, evidence, and consequential gaps. Use independent review when warranted, available, and permitted by existing instructions, under `bounds-review`'s bounded protocol, reusing authorization already granted.

If a selected skill is absent, say which one and continue with available tools when feasible; never pretend it loaded or install anything unasked.

## Continuity

Honor opt-out immediately. Follow the continuing task while context retains it; there is no portable sticky mode. Do not persist a mode setting or edit standing instructions. For invocation, discovery, or host limits, read [host behavior](references/hosts.md).
