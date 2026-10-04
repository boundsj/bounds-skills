# bounds-skills

Eight portable engineering workflows for Codex and Claude Code. Use them individually or enter Bounds mode for a task. The aim is more accepted work per minute of human attention: fewer repeated corrections, selective context, and evidence you can trust.

- **bounds-mode** selects the relevant workflow and carries authorized work through proportionate checks.
- **bounds-plan** defines scope, retained behavior, acceptance checks, and dependencies.
- **bounds-debug** reproduces a symptom, isolates its cause, and verifies the fix.
- **bounds-review** reviews a pinned change for correctness, requirements, and maintainability.
- **bounds-retro** finds recurring waste in accessible work and proposes structural improvements.
- **bounds-agent-docs** keeps agent documentation short, accurate, and easy to navigate.
- **bounds-create-verification** builds and executes a project-local Launch, Doctor, Drive, Evidence, Cleanup recipe.
- **bounds-maintain-verification** refreshes that recipe and feature map, separating drift, tooling gaps, and product defects.

A typo stays a small edit. A skill grants no extra permissions, installs no dependencies on invocation, and creates no cross-host delegation. Generated verification recipes belong in their own projects.

## Try a task

In Codex, use `$bounds-mode`; in Claude Code, use `/bounds-mode`. Start a fresh session after installation. T3 uses the provider on its execution host; shorthand handling and continuity depend on that provider. See [tested compatibility](docs/compatibility.md).

```text
Use bounds-mode to fix this failing import and verify the original error is gone.
Use bounds-plan to plan CSV export, preserving the current JSON interface.
Use bounds-debug to reproduce why the second page repeats the first page's rows.
Use bounds-review to review this branch against main and SPEC.md.
Use bounds-retro to examine the repeated corrections in this task.
Use bounds-agent-docs to shorten this project's AGENTS.md and check its commands.
Use bounds-create-verification to build and execute a local recipe for this CLI.
Use bounds-maintain-verification to check the recipe after the search route changed.
```

Use the provider's explicit prefix for any individual skill too. Bounds mode is an explicit entrypoint, not a persistent provider setting. Say “stop using bounds-mode” to opt out; reinvoke it in a new session.

## Install and maintain

Use `npx skills` on each execution host, targeting `codex` and/or `claude-code`. [Installation](docs/install.md) covers a pinned source, selective installs, updates, status, and removal. No bespoke installer or plugin framework is required.

Version **0.1.0** is a release candidate. Representative Codex and Claude CLI invocations are tested in isolated temporary homes; no real user-home rollout or other-host installation has been performed. [Validation](docs/validation.md) records the provider-specific coverage and remaining gaps.

## Develop

Read [SPEC.md](SPEC.md) for the durable contract. Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests`. For isolated installer and provider checks, follow [validation](docs/validation.md). Test artifacts stay outside the repository.

MIT licensed. Adapted from selected pinned Matt Pocock and Lauren Tan/pstack workflows; see [sources, notices, and adaptations](THIRD_PARTY.md).
