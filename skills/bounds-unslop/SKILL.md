---
name: bounds-unslop
description: "Edit prose the user asks to tighten so it reads direct and concrete, preserving meaning, commitments, numbers, uncertainty, citations, quotes, and code. Use for requested rewrites of drafts, docs, PR text, or messages, not for unrequested style passes."
license: MIT
---

# Bounds unslop

Edit the text the user supplies or names so its reader gets the point faster. The meaning stays; only the wording changes. Touch only the requested text, not surrounding documents or the rest of the conversation.

## Set the audience

Infer the reader and destination from the request: a commit message, PR description, user docs, a status update, a chat reply. Match that register and any house style or template already present. When the author's conventions conflict with a pattern below, keep theirs.

## Preserve exactly

- Facts, claims, commitments, and scope, including what is deliberately not promised.
- Numbers, units, dates, versions, names, and identifiers.
- Uncertainty and its strength. "May" stays "may"; a calibrated hedge is content, not filler.
- Citations, links, quotations, and attributions.
- Code, commands, paths, configuration, and log output, including inline code.
- Structure that something depends on: required headings, front matter, legal or compliance wording, and formats a tool parses.

When a sentence is vague because its content is missing, do not invent the fact. Leave a short question for the author.

## Then cut

Read [patterns](references/patterns.md) for the common problems: filler, inflated vocabulary, vague attributions, stacked hedges, metaphor standing in for mechanism, forced groups of three, inline-header lists, chatbot phrases, and over-compression. Prefer active voice with a named actor, the plain word, a number over an adverb, and one idea per sentence. Shorter is a result, not the goal; keep what the reader needs.

## Return

Return the edited text ready to paste. Add a brief note only for what the user must act on: spots that need information you lack, edits near the meaning line, or conventions you deliberately kept. Do not list every change. When the user asked you to edit a file, change only that text and show the diff.
