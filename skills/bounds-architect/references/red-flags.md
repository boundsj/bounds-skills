# Design red flags

Screen each candidate before choosing. A red flag is a reason to revise or reject a shape, not an automatic veto; some domains are complex. Assume the next contributor sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Prefer the design where a change that looks right from one file is right for the whole system.

## Shallow module

A large interface hides little. Callers coordinate several methods for one operation, public options expose internal stages, or learning the interface does not spare the caller from learning the implementation. A deep module concentrates capability behind a small interface; a deep call chain scatters it across layers and is not the same thing.

## Information leakage

Several modules depend on the same internal decision, so changing a representation, policy, or protocol detail needs coordinated edits. Re-exported transport or storage types are the usual case. Parse into domain types behind the interface.

## Organized by execution order

Separate load, validate, transform, and save modules often repeat one representation and its invariants at every boundary. Group code by the knowledge it owns instead.

## Pass-through layer

A method forwards the same arguments to another method of the same shape. Remove it, or keep the boundary only when it adds policy, adaptation, or a distinct abstraction.

## Split ownership

More than one module writes the same state or keeps its own copy. Their rules drift because an editor of one cannot see the others. Give each piece of state one owner; others read it or ask the owner to change it.

## Derived copy treated as authority

A cache, mirror, or snapshot answers questions only the source of truth can answer. Restarts, pagination, and concurrent writes then return stale or partial results. Name the authority, and make the copy's freshness rule explicit.

## Two ways to do one task

Every path keeps gaining callers because contributors copy whichever they find first. Keep one, move callers off the others, and delete them in the same change where feasible.

## Reachable internals

Callers can import a module's internals, so the internals become interface. Make them unreachable from outside where the language allows.

## Hand-synced lists

Adding an item means editing several lists. Derive the others from one list, or make the build fail when they disagree.
