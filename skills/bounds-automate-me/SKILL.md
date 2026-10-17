---
name: bounds-automate-me
description: "Create or update a scoped skill that captures how the user likes agents to work, from their explicit preferences and bounded evidence of repeated decisions. Use when the user asks to turn their working style into a reusable skill."
license: MIT
---

# Bounds automate me

Turn the user's accepted working conventions into one concise skill agents can follow. The request authorizes drafting or updating that skill in the scope the user chose; it does not authorize global configuration edits, installation, publication, or rollout.

If a working-style skill for this user already exists in scope, update it in place unless they asked to start fresh. Keep uncontradicted sections and prefer evidence newer than its last edit.

## Gather bounded evidence

1. Explicit preferences in this request and conversation come first.
2. Then only sources the user names, such as a development log, particular sessions, or one project's records, within a stated window. Don't search unrelated projects or histories. If an optional integration is unavailable, say what you could not read.
3. Look for repeated decisions: corrections made more than once, restated constraints, what the user accepted as done, how they want updates. A one-task instruction is not a convention. When a preference was reversed, follow the latest accepted decision.

Ask only for intent evidence cannot show, in one short round with concrete options. Don't re-ask for approval already given.

## Draft

Read [skill shape](references/skill-shape.md) for sections, wording, and the privacy check. Write decision criteria, not event logs; include a section only where the user has a specific rule; name other skills instead of copying them. Generalize practices; keep transcripts, private quotations, identifiers, project names, account details, addresses, paths, and credentials out.

## Deliver

Write the skill where the user asked or where the project's skill convention puts it; otherwise return it in the conversation. Report the evidence window and sources read or unreachable, which rules came from explicit statements versus repeated observations, what you dropped as one-off, and open questions. Ask the user whether it reads like how they work. Reuse explicit delivery authorization already given; otherwise propose installation, enabling on other hosts, or publication separately.
