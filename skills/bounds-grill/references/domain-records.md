# Domain records

Read only when the user requests documentation during grilling. This reference
adds no permissions. Use the requested project; infer it from instructions and
context, asking only if ambiguous. Follow existing documentation conventions.
Never write to other projects or global configuration, commit, or publish unasked.
If file writes are excluded, keep drafts in the conversation.

## During rounds

Read the relevant glossary and decisions. Challenge conflicting or overloaded
terms, propose precise names, and test boundaries with concrete scenarios.
Check claims against accessible code; distinguish observed behavior, intended
behavior, and unresolved contradictions. Scenarios are probes, not evidence.
Keep the skill's question limits and recommendations.

Capture each term or decision once the user confirms it, within the requested
scope. Do not wait for the closing summary when incremental writes are already
authorized. Unresolved proposals stay in conversation. Report records changed
or drafted at close; summary confirmation grants no implementation authority.

## Glossary

Use existing locations. Otherwise use a root `GLOSSARY.md` for one context.
Read an existing root `GLOSSARY-MAP.md` to locate multiple contexts; ask when
ownership is unclear. Create a map only when multiple contexts are established:
list each context, its glossary location, and its relationships to the others.
Keep each term in its owning context rather than merging distinct meanings.

Create files only when the first confirmed entry needs them. Use:

```markdown
# Ordering

Receives and tracks customer orders.

## Language

**Order**:
A customer's confirmed request for goods.
_Avoid_: Purchase, transaction
```

Define project-domain concepts in one or two sentences; choose canonical terms
and list rejected synonyms. Group terms only when useful. Exclude general
programming concepts, implementation details, plans, and scratch notes.
Mark proposed vocabulary as intended when it differs from current code; do not
silently rename code or declare a migration complete.

## Decision records

Offer an ADR only when all three hold: meaningful reversal cost, surprising
without context, and a real tradeoff among alternatives. Confirm the decision
and reason; use existing write authorization without another permission ritual.

Follow existing conventions. Otherwise use `docs/adr/` at the project root for
system decisions or inside the owning context for local decisions. Create the
directory lazily. Scan that directory and increment its highest number, using
`0001-slug.md`; recheck before writing and never overwrite a collision.

Use a title and one to three sentences covering context, decision, and why.
Add status, rejected alternatives, or consequences only when useful. Keep
unconfirmed decisions as proposed drafts. Preserve history when revisiting an
accepted decision: mark the old record superseded and link its replacement.
