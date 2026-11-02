# Design rules

Read this when a project has a visual system, such as tokens or theme values, shared components with variants, and styles, and agents build screens with it. New screens should use what exists, not invent values, variants, or components.

## Ground every entry

Start from the sources of truth: token or theme definitions, shared components, style helpers, and a screen that uses them well. Document only what the code defines and screens use. Planned components, design-file-only tokens, and unbuilt variants stay out; an aspirational entry sends agents to code that does not exist.

When no shared system exists, say so in one line and name the most consistent screen to follow. When two token sets or component versions coexist, name the one new work uses and mark the other legacy. Building or consolidating a system is the user's call: recommend, then ask.

## Write what the code cannot say

Point to names, values, and props in code rather than copying them; copies drift. Spend words on what lookup cannot reveal:

- **Token roles.** Which semantic token serves which purpose; screens use semantic tokens, not the primitives they alias. In the W3C Design Tokens Community Group format, intent lives in `$description` and `$deprecated`; point there.
- **Component choice.** When to use it, which sibling to pick instead, what each variant means, and which states exist per platform.
- **The gap rule.** When nothing fits, compose existing pieces. Adding a token, variant, or component is a design decision: stop and ask.

## Load little, link the rest

The always-loaded file gets a few lines: where tokens and components live, the gap rule, and a pointer that names its trigger, such as "Before building or changing a screen, read `docs/ui.md`." Token roles and one entry per shared component go behind that pointer. Split by platform or area only when tasks would otherwise load detail they never use.

## Example entry

Names are illustrative.

```markdown
### ListRow (`ui/list-row`)
One item in a vertical list. For a standalone summary with media, use `Card`.
Reference usage: `screens/settings`.
- `trailing`: `chevron` navigates, `switch` toggles in place,
  `value` shows read-only text, `none` (default).
- Tokens: `space.inset.md` padding, `color.border.subtle` divider,
  `color.text.muted` secondary text.
- States: pressed, selected, disabled. While loading, render `ListRowSkeleton` rows.
- Web: keyboard focus uses `focus.ring`. Native: keep the platform press feedback.
- No swipe actions; ask before adding them.
```

## Check it with an agent

Give a fresh agent, with only the always-loaded file in context, a realistic screen task in a disposable worktree, branch, or copy. Keep its misses, discard its code, and say so in the report. If you cannot start one, read the entrypoint as one and label the check a read-through. Review the result for:

- raw values or primitives where a semantic token exists;
- new variants, props, or local copies of shared components;
- whether the agent opened the linked doc.

Trace each miss to the docs, fix the cause, and rerun the same task:

- **Skipped the doc:** sharpen the pointer's trigger; inline the rule only if that fails.
- **Read it and still guessed:** add or correct the entry. For a judgment call, move the rule up and show the wrong choice beside the right one.
- **Repeated mechanical miss:** propose a check in the project's existing tooling, such as a lint rule against raw values outside token files or a variant type that rejects unknown names. Once structure enforces a rule, cut its prose to a pointer at the check.

Correcting only the agent's diff teaches the next agent nothing. The trial proves component choice, not appearance; render on each target platform before claiming a visual result.

Update or delete an entry in the change that alters its token or component. Report the trial task, the platforms covered, and what was not checked.
