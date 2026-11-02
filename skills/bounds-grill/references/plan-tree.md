# Plan tree

Map the plan's decisions as a tree: each decision opens the ones that depend on it. The frontier is every open decision whose prerequisites are settled. Ask from the frontier, recompute it after each round, and finish when every branch is decided or deliberately deferred.

## Common first branches

Use only those that apply.

- **Outcome:** what changes, for whom, and how it will be observed.
- **Boundaries:** what is in, what is explicitly out, and what must keep working.
- **Constraints:** deadlines, platforms, budget, compatibility, and the people involved.
- **Shape:** where state lives and who owns it, interfaces, and where the code or asset goes.
- **Failure:** errors, partial completion, retries, concurrent use, and loss of connection.
- **Rollout:** reversibility, migration, feature gating, and who sees it first.
- **Evidence:** how each decision will be verified, and on what device, data, or environment.
- **Cost to undo:** which decisions are one-way and which can be revisited cheaply.

## Round format

Ask at most three numbered questions per round. Write a decision's recommendation so "yes" accepts it. For a question of fact or past experience that only the user can answer, describe what a useful answer would contain.

```text
Q1. Offline edits. Should edits made offline sync automatically when the connection returns, or wait for the user to confirm?
Recommended: sync automatically, and prompt only when the server copy changed meanwhile.

Q2. Undo scope. Does undo cover only the last edit, or the whole session?
Recommended: the whole session, because the editor already keeps a history stack.

Q3. Last rollout. How did the previous editor change reach users, and did anything go wrong?
A useful answer: whether everyone got it at once or a group went first, and any problem that surfaced afterward.
```

Hold back a question whose answer depends on another open question in the same round. Put options inside the question when a choice is open-ended. When a fact settles a question, look it up and state it rather than asking.

## Close

- The decisions made, each with its reason.
- Facts you looked up, each with its source.
- What was deliberately left out.
- Assumptions still open, each with the cheapest check.
- Deferred branches and what they wait on.
- Why the session stopped.
