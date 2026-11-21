---
name: bounds-ship
description: "Carry an authorized change to proof, cross-provider review, green required CI, and a PR handoff. Use when asked to ship or finish through PR readiness; merge requires the user’s explicit instruction."
license: MIT
---

# Bounds ship

Take an authorized change to its agreed finish line. Use `bounds-review` for review mechanics and `bounds-ketchup` for a requested briefing; report missing skills. This skill grants no extra permissions.

## Agree the finish

Recover the goal, acceptance checks, exclusions, and authorized external actions from the request. Resolve material gaps while continuing independent work. Ask whether deployment is intended only when it makes sense here and the request is silent; a deploy needs authorization and its own acceptance evidence.

Inspect the branch, local edits, and existing PR first. Preserve unrelated work. Use a task branch. Check auto-merge and queue state before each push, after filing, and at handoff. If it could merge automatically, disable auto-merge/remove it from the queue when authorized; otherwise stop before pushing and report the blocker.

## Finish and prove

Complete the smallest coherent change and run the required checks. Observe direct evidence for the intended behavior: reproduce a fix, exercise a workflow, or inspect the running UI where applicable. Record commands/results and gaps against the exact commit; green mocks alone do not prove a user workflow.

Get one independent cross-provider review of the final commit under `bounds-review`. Discover capabilities; never silently substitute providers or models. If unavailable, provide its review packet and report blocked review. Fix real findings within the bounded protocol. Recheck and review any changed head before claiming readiness; rebases follow `bounds-review`'s approval rule.

## File and follow through

Reuse the branch’s PR or open one against the intended base; write its body per [PR body](references/pr-body.md). Check public text for private details. Use `bounds-leaving-pr-comments` for authorized replies; filing a PR does not authorize unsolicited comments.

Handle CI and review findings. The owning thread uses the host’s PR watcher; unwatch before handoff. Report missing monitoring. Before starting a release, deploy, or CI rerun, check for one already running for the same revision and follow it. Update branches by rebasing onto their base by default; no merge commits from base unless the user asks. Force-push when appropriate, preferably `--force-with-lease` pinned to the observed remote head; never force-push shared/default branches without the user’s say-so. Reassess a failed lease.

## Handoff gate

Re-fetch the live head and base. Readiness requires proof and cross-provider review on that head, green required CI, an up-to-date mergeable branch, and no unresolved actionable findings or review requests. Separate missing human approval from technical blockers.

Report PR URL, final SHA, evidence, review outcome, risks, and exactly what the user must accept. Leave it open and unmerged. Merge only on the user’s explicit word pinned to the reviewed SHA; revalidate the gate immediately beforehand, without protection bypasses. Never enable automatic merging without that authorization.
