---
name: bounds-agent-docs
description: "Create or maintain concise agent-facing project documentation with verified commands, clear entrypoints, and references loaded only when their task applies."
license: MIT
---

# Bounds agent docs

Start from the requests future agents need to complete and the documentation already in scope. Read applicable instructions and inspect the relevant commands and entrypoints. Preserve project conventions and user-authored constraints; make a focused patch rather than replacing unrelated guidance.

Keep always-loaded files small: the project purpose, essential constraints, navigation, and commands that earn their space. Put a specialized procedure behind a link that says when to read it. Keep each fact in one maintained location. Prefer an accurate pointer to configuration over duplicating a discoverable inventory.

Write direct actions with observable completion criteria. Include working directory, prerequisites, and side effects where a command would otherwise be ambiguous. Run safe commands to check accuracy; label commands that could not be executed and why. Do not run deployments or other external mutations just to validate documentation.

For a skill, keep the description narrow enough to select it correctly and the body sufficient for its ordinary path. Supporting resources should live inside that skill's distributable folder; selective installation must not break links to siblings. Only promise provider metadata or invocation syntax that has been checked on that provider.

Check links and paths after moving material. Read the entrypoint as a fresh agent: can it find the right procedure without loading every reference? Remove stale examples, duplicated rules, unsupported guarantees, and scaffolding.

Return the changed entrypoints, what was validated, and remaining gaps. Keep generated docs within the requested project and avoid publishing private session details or local credentials. No global configuration changes are implied.
