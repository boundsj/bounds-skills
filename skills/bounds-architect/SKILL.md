---
name: bounds-architect
description: "Design state ownership, types, interfaces, and module shape before implementing a nontrivial change, comparing a few meaningful alternatives with compatibility, risk, and verification. Use when the wrong shape would be costly to undo, not for scoping or task breakdown."
license: MIT
---

# Bounds architect

Settle the shape of a change before code locks it in. Scoping work into slices is a separate planning job.

Ground the design in the code it touches: entrypoints, shared types and state, and callers it must not break. When the existing shape looks odd, check its history before treating it as an accident. Carry forward accepted decisions. Skip grounding only for greenfield work.

## Design from usage

1. **Usage.** Write realistic call sites first. Derive types from them; when they disagree, change the types.
2. **State.** One owner per piece of state. Ask what happens when two actors write, an operation runs twice, or it stops halfway. Parse external data into domain types at the boundary.
3. **Interfaces.** The smallest public surface hiding the most complexity. Keep transport, storage, and framework details private. Encode invariants in types before runtime checks before comments.
4. **Alternatives.** When real contenders exist, sketch two or three whole-shape options, not variants of one. If constraints force one answer, say why. Screen candidates against [design red flags](references/red-flags.md).
5. **Compatibility.** Persisted data, wire formats, mixed versions, existing clients. Expand, migrate, then contract when a break cannot land at once.
6. **Verification.** Observable checks through existing real interfaces for new and retained behavior.

## Deliver

One page sized to the change: problem and constraints, usage, shape, tradeoffs accepted ("we accept X for Y"), alternatives and why they lost, open questions, risks, verification, and the first implementation step. A sketch of signatures with unimplemented bodies stays in the response unless implementation is authorized.

A design request ends with the design. When implementation is already authorized, build against it and surface deviations. Repeated deviations of one kind mean the design is wrong: escape-hatch types, special cases, locks on supposedly unshared state, callers needing internal rules. Stop patching and redesign smaller.
