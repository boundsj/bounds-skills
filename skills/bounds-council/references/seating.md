# Seating

## Discover

- **T3 Code:** call `orchestrator_capabilities`. It lists providers (with `providerInstanceId`), their models, each model's options (such as an effort select with its listed values and default), runtime modes, and whether a provider can run a child task or a cross-provider child task. The list is short; pass `search` to find other models. Use a linked environment's `environmentId` only when the user's instructions name it; T3, not this skill, runs that route.
- **Claude Code, Codex, and other hosts:** use the host's own subagent tool. It usually runs only that host's provider, which seats one provider; report that council cannot seat a second unless the user's instructions name another route.
- **Other routes,** such as an installed CLI or second-opinion tool, only when the user's instructions name them. Do not install tooling, sign in, or launch another host to manufacture a seat.

## Choose

- Count providers by vendor: two model lines from one vendor are one provider, whatever host or brand name serves them.
- Seat one model per available provider, at most three unless the user asks for more. At least one seat must come from a provider other than the implementer's; a seat from the implementer's provider still starts fresh.
- Per provider, pick the newest generation's flagship general model the catalog lists. Skip small, fast, and legacy variants unless named; use a preview only when it is the provider's newest flagship, and say so. When two candidates are close, prefer the host's default for that provider and say which you chose.
- Reasoning: high, or the provider's equivalent, by default. Use the highest listed level for security, data-loss, or concurrency changes and for a disputed final round. Never seat a fast or low-effort mode. Pass only option ids and values the catalog lists.

## Launch in T3

Start every seat with `delegate_task` in the same turn:

- `task`: the complete brief. A child gets no parent history, so include everything it needs, and no secrets.
- `target`: `providerInstanceId`, `model`, and `options` (such as the effort option and value) from the catalog.
- `role`: `review`; `title`: council, seat provider, and round.
- `isolation`: `worktree` for a committed head; the child gets a prepared checkout from the parent's current commit, so check out the reviewed head before launching. Uncommitted edits stay out. For uncommitted work, commit to the task branch when authorized, or give each seat a snapshot path.
- `mode`: `async`. Keep each `taskId`.

Do not poll a running seat; T3 wakes the parent when a child finishes. Then read it once with `task_status`. Accept a result only when `status` is `completed` and `summary` is not empty; a failed, cancelled, or interrupted task can also show `result_available`, and its partial summary is not a review. Compare the executed model T3 reports with the requested one and report a mismatch as a substitution; when it reports none, record the requested model and "executed model not reported". For a stuck or failed seat, `task_cancel` it, confirm it stopped, then relaunch once or report it. Never run two seats for the same provider and round.

## Brief additions

Append to the `bounds-review` brief:

```text
Council seat <n> of <total>, round <r>. Before reviewing, confirm the
checkout is at <head SHA> (or the snapshot is <identity>); if not, stop and report.
Return APPROVE or CHANGES and a score out of 10 for this revision,
where 10 means ready to merge as is.
Prior rounds: <ledger with IDs, responses, and status>, or none.
```

For a plan or design, replace the diff scope with the pinned document revision and its acceptance criteria.
