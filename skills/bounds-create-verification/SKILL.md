---
name: bounds-create-verification
description: "Create and execute a project-local verification recipe and small feature map using the project's existing tools to launch, health-check, drive, capture evidence, and clean up."
license: MIT
---

# Bounds create verification

Inspect the project before asking the user: its real user surface, run/build commands, dependencies, authentication needs, fixtures, and existing test or driving tools. Preserve useful specialists and native host tools. Identify how to isolate ports, processes, data, and profiles from active work.

Find an existing verification recipe first. Extend it if appropriate. Otherwise use the project's documentation convention, falling back to `docs/verification/README.md` with `features.md` alongside it. A discoverable local skill is optional when the project already uses one; keep its files inside that project. Never write a project recipe into this shared bundle or a global skill home.

Read [recipe shape](references/recipe.md) when authoring. Fill it with observed commands and checks, not guessed placeholders:

- **Launch:** setup, isolated runtime, readiness signal, and owned resources. A short-lived CLI needs no background server.
- **Doctor:** a read-only check of the intended instance, version, prerequisites, and health before driving.
- **Drive:** user-facing actions through existing tools and stable handles, with explicit expected results.
- **Evidence:** commands, results, host/tool versions, revision including dirty state, coverage, and durable artifact paths. Capture the action and its effect.
- **Cleanup:** release only resources this run owns, on failure too. Evidence lives outside disposable runtime state and survives teardown.

Add a small feature map, usually three to five important behaviors or fewer for a small project. For each, name the user entrypoint, prerequisites, action, expected observation, and verification status. Mark unexercised paths explicitly.

Execute the recipe end to end for at least one mapped behavior. Run Doctor after surprises; repair recipe errors and retry a failed step once before reporting a blocker. Verify evidence still exists after cleanup. A recipe not executed is a draft; a build or source read alone does not prove user behavior.

Report coverage and remaining prerequisites. A startup or product defect outside scope is a finding, not permission for a broad repair. Point to `bounds-maintain-verification` for later upkeep without scheduling it.
