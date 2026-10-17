# Skill shape

A working-style skill is read by an agent at the start of work. Every line should change a decision that agent would otherwise make differently.

## Frontmatter

- `name`: short and stable, chosen by the user or following the existing skill's name.
- `description`: trigger on the user asking agents to work in their style, or on the skill's name. Do not trigger on generic task words such as "write code" or "review a PR"; that would load it into unrelated work.
- Invocation policy: a style skill can steer every task it loads into. Preserve an existing invocation policy. For a new skill, keep normal discovery unless the user requests explicit-only invocation. Write only metadata verified for the target hosts.

## Sections

Use only the ones where the user has a specific rule. Common ones:

- **Updates:** length, format, reading device, what to lead with, what to leave out.
- **Autonomy:** what the agent may finish without asking, and which actions still need confirmation.
- **Understand first:** what to read or reproduce before changing code.
- **Done and evidence:** what proof counts. For example: real UI, device, or hosted proof versus unit checks; results tied to the current head, not an older reviewed revision; merged, deployed, and accepted reported separately.
- **Review and delivery:** independent review expectations, PR and merge conventions.
- **Hosts and delegation:** which providers or delegated agents to use and how far their results can be trusted.

Skip a section the user has no rule for. "Communicate clearly" is not a rule. "Lead with the outcome in one line; tables only to compare options" is.

## Wording

- Imperatives addressed to the agent, referring to "the user", not a personal name.
- Decision criteria, not anecdotes. "Treat a mutable cache as a hint, not the source of truth" generalizes an incident; "the cache bug last week" does not.
- One rule in one place. Point to other skills or project docs by name rather than restating them.
- Short. A style skill is not a manual. If it grows past a few hundred words, move conditional detail into a reference.

## Privacy check

Before writing, remove or generalize:

- transcript excerpts and quotations from private conversations;
- session, thread, page, or ticket identifiers and private links;
- private project or customer names, personal names other than the user's chosen skill name, and account details;
- hostnames, IP addresses, usernames, and local paths;
- credentials, tokens, and real financial or personal figures.

Use synthetic examples where an example helps.

## Check the result

Read it back with the user. Then try two or three representative prompts mentally: one it should load for and one it should not, such as a generic coding request. Check that its rules would change the agent's choices in the first and stay out of the second.
