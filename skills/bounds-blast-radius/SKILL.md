---
name: bounds-blast-radius
description: "Trace what an exact code or configuration change could break beyond its diff, such as callers, shared state, client contracts, caches, serialization, and migrations, and test the safety assumption it rests on. Use before shipping a change you do not fully trust."
license: MIT
---

# Bounds blast radius

Find what a specific change breaks elsewhere, and prove or disprove the fact its safety rests on. Search hits are not the deliverable; neither is a convincing writeup without proof.

Pin the change to exact revisions, or to a fixed snapshot of uncommitted edits. If it cannot be identified, ask. Read what the diff implies without spelling out: changed defaults, ordering, timing, error paths, removed fallbacks.

Most risky-looking changes are safe or unsafe because of one or two facts, such as "this evicts only entries no reader still holds" or "every deployed client already sends the new field". Name them early and spend the effort there.

## Look where symbol search stops

- Callers, dynamic dispatch, generated code, and other languages reading the same bytes.
- Shared state: other writers, and mutable caches treated as authority.
- Client contracts: payloads, path formats, schemas, versions already deployed, and fields a client silently drops.
- Caches, freshness, and pagination across restart or retry.
- Cancellation, late completion after teardown, concurrent writers, interrupted jobs, and retries that run twice.
- Serialization, persisted formats, and migrations meeting old data or mixed versions.
- Flags, configuration, and pinned or patched dependencies; read library source when behavior matters.
- Leakage between training, validation, and evaluation data.

Cite real `file:line` or library source. Never invent a caller or API; an empty search is a result.

## Prove it

Take each load-bearing fact as far as is cheap: stated, cited, failure path shown unreachable, executed against real code, reproduced in the running app or device. When execution is authorized and safe, write the smallest check that calls the real interface through existing runners and fails loudly if you are wrong, then report its output. Keep throwaway checks outside the change unless asked. Never mutate shared or production systems to prove a point.

## Report

- **What changed,** including the non-obvious part, at which revisions.
- **Safety fact:** level reached and proof, or "unproven".
- **Risks:** mechanism, location, likelihood and cost, how to check.
- **Cleared:** what you checked and why it is fine.
- **Before merge:** the cheapest check that catches the real bug.
- **Not executed:** named checks not run, and why.
