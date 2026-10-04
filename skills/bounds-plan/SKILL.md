---
name: bounds-plan
description: "Turn an engineering idea or change request into a concise, executable plan with scope, retained behavior, acceptance checks, and real dependencies."
license: MIT
---

# Bounds plan

Ground the plan in the user's request, accessible project sources, and current behavior. Read only the code, commands, and decisions needed to resolve the scope. Carry forward accepted corrections and constraints rather than reopening them.

Ask only when a material product choice cannot be inferred or checked. State routine assumptions and proceed with the plan. Separate a blocked decision from work that can already be planned.

Include, at a scale useful for the task:

- **Outcome and scope:** who benefits, what changes, and what is excluded.
- **Retained behavior:** interfaces, data, workflows, or constraints that must survive.
- **Acceptance:** observable examples and the existing commands or user paths that can check them. Label checks not yet run.
- **Work and dependencies:** independently verifiable slices, with only genuine blocking edges. Name relevant entrypoints when they help execution.
- **Open decisions or risks:** the unresolved choice and what evidence would settle it.

Prefer a complete narrow behavior over separate infrastructure, API, and UI phases. For a migration that cannot land in independent slices, use an expand, migrate, remove sequence with explicit compatibility checks. Do not turn a simple edit into a ticket hierarchy or speculative redesign.

Choose existing public interfaces for verification; routine test-boundary choices need no approval ritual. For nontrivial changes, include how to detect a regression in retained behavior, not just the new happy path.

Return the plan in the conversation unless the user requested a durable file or tracker action. Planning alone does not authorize implementation or publication. If implementation is already authorized, use the plan to continue the work.
