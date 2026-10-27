# bounds-skills

Portable engineering workflows for Codex and Claude Code. Use them individually or enter Bounds mode for a task. The aim is more accepted work per minute of human attention: fewer repeated corrections, selective context, and evidence you can trust.

- **bounds-mode** selects the relevant workflow and carries authorized work through proportionate checks.
- **bounds-plan** defines scope, retained behavior, acceptance checks, and dependencies.
- **bounds-debug** reproduces a symptom, isolates its cause, and verifies the fix.
- **bounds-review** reviews a pinned change for correctness, requirements, and maintainability.
- **bounds-recall** recovers prior decisions and unfinished work, then checks what still holds now.
- **bounds-retro** finds recurring waste in accessible work and proposes structural improvements.
- **bounds-agent-docs** keeps agent documentation short, accurate, and easy to navigate.
- **bounds-create-verification** builds and executes a project-local Launch, Doctor, Drive, Evidence, Cleanup recipe.
- **bounds-maintain-verification** refreshes that recipe and feature map, separating drift, tooling gaps, and product defects.
- **bounds-ketchup** briefs the user on what changed in the current conversation since their last substantive message, with rechecked state, user-owned decisions, and the next step.
- **bounds-why** investigates why code or a design has its current shape, separating cited evidence from inference, alternatives, and unknowns.
- **bounds-blast-radius** traces what an exact change could break beyond its diff and tests the safety fact it depends on through real interfaces when authorized.
- **bounds-how** explains how existing code or a subsystem works from entrypoint through state and boundaries to outcome, sized to the reader.
- **bounds-architect** designs state ownership, types, interfaces, and module shape before a nontrivial implementation, with real alternatives, compatibility, risk, and verification.
- **bounds-unslop** edits requested prose to be direct and concrete while preserving meaning, commitments, numbers, uncertainty, citations, quotes, and code.
- **bounds-bro** restates the previous answer or supplied text in plain short language, keeping its decision, consequential caveats, and next step.
- **bounds-help** guides the user to the Bounds skills actually available on this host, or a useful prompt for one, without starting the work.
- **bounds-automate-me** creates or updates one scoped working-style skill from the user's explicit preferences and bounded evidence of repeated decisions.
- **bounds-ship** carries an authorized change to proof, cross-provider review, green required CI, and a PR handoff. Use when asked to ship or finish through PR readiness; merge requires Jesse’s explicit instruction.
- **bounds-modernize** reassesses and updates a stale, conflicting, duplicated, or inherited PR. Use for modernizing, rebasing, or taking over existing work while preserving contributor credit.
- **bounds-leaving-pr-comments** writes attributed GitHub comments on Jesse’s behalf when posting is authorized: PR comments, inline reviews, replies, and issue comments. Does not itself authorize posting.

A typo stays a small edit. A skill grants no extra permissions, installs no dependencies on invocation, and creates no cross-host delegation. Generated verification recipes belong in their own projects.

## Try a task

In Codex, use `$bounds-mode`; in Claude Code, use `/bounds-mode`. Start a fresh session after installation. T3 uses the provider on its execution host; shorthand handling and continuity depend on that provider. See [tested compatibility](docs/compatibility.md).

```text
Use bounds-mode to fix this failing import and verify the original error is gone.
Use bounds-plan to plan CSV export, preserving the current JSON interface.
Use bounds-debug to reproduce why the second page repeats the first page's rows.
Use bounds-review to review this branch against main and SPEC.md.
Use bounds-ship to finish this authorized change through a ready PR; do not merge.
Use bounds-modernize to reassess and update PR #42 against its base.
Use bounds-leaving-pr-comments to reply to this reviewer on my behalf.
Use bounds-recall to catch me up on this project across available sessions and the Dev Log.
Use bounds-retro to examine the repeated corrections in this task.
Use bounds-agent-docs to shorten this project's AGENTS.md and check its commands.
Use bounds-create-verification to build and execute a local recipe for this CLI.
Use bounds-maintain-verification to check the recipe after the search route changed.
Use bounds-automate-me to draft a scoped working-style skill from my stated preferences.
Use bounds-help to choose a skill for understanding a design decision.
Use bounds-bro to say that again in plain language.
Use bounds-unslop to tighten this PR description without changing its claims.
Use bounds-architect to design offline draft sync while preserving old clients.
Use bounds-how to explain this request flow and its failure paths.
Use bounds-blast-radius to check the downstream effects of this cache change.
Use bounds-why to investigate why this module uses a retry limit.
Use bounds-ketchup to catch me up on this thread since my last message.
```

Use the provider's explicit prefix for any individual skill too. Bounds mode is an explicit entrypoint, not a persistent provider setting. Say “stop using bounds-mode” to opt out; reinvoke it in a new session.

## Install and maintain

Use `npx skills` on each execution host, targeting `codex` and/or `claude-code`. [Installation](docs/install.md) covers a pinned source, selective installs, updates, status, and removal. No bespoke installer or plugin framework is required.

Version **0.3.0** is a release candidate. The original eight workflows have representative Codex and Claude CLI tests in isolated temporary homes. Evidence for recall and later additions is recorded separately; no real user-home rollout or other-host installation has been performed. [Validation](docs/validation.md) records the provider-specific coverage and remaining gaps.

## Develop

Read [SPEC.md](SPEC.md) for the durable contract. Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests`. For isolated installer and provider checks, follow [validation](docs/validation.md). Test artifacts stay outside the repository.

MIT licensed. Adapted from selected pinned Matt Pocock, Lauren Tan/pstack, and Theo Browne/tstack workflows; see [sources, notices, and adaptations](THIRD_PARTY.md).
