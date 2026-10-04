# Provider and host compatibility

The package uses standard `SKILL.md` directories. Only the explicit mode entrypoint has provider adapters:

| Surface | Metadata / invocation | Validation boundary |
| --- | --- | --- |
| Codex CLI 0.160.0 on macOS | `agents/openai.yaml`: `allow_implicit_invocation: false`; explicit `$bounds-mode` | Fresh discovery and representative actual invocations pass. |
| Claude Code 2.1.288 on macOS | `disable-model-invocation: true`; explicit `/bounds-mode` | Fresh discovery, authenticated mode/debug invocations, and exclusion of mode from the automatic skill catalog pass. |
| Other seven skills | Normal skill discovery and automatic selection; individual explicit invocation remains available | Descriptions identify narrow tasks; bodies and references load when relevant. |
| T3 Code | Uses its execution host's provider and exposed tools | This delivery was authored in T3; fresh installed-bundle composer discovery is not tested. Shared skills add no orchestration or cross-host access. |
| Cursor and other hosts | No supplied adapter or support claim | Upstream Cursor mode metadata is intentionally omitted. |

Exact tested versions, results, and gaps are in [validation](validation.md). Installation success alone establishes packaging. Fresh-session discovery establishes that the provider sees the files. An observed skill load and completed task establish invocation for that case. None guarantees identical future model behavior.

The routing table contains names, not unconditional imports. A selectively installed skill contains all its own file references. Mode discovers available supporting skills at runtime and reports missing capabilities. If delegation is absent, review is local and labeled as such.

There is no portable sticky-mode setting. The user's task and opt-out govern use while conversation context retains them. New sessions require a new explicit invocation. Files such as `mode`, `reminder`, Cursor rules, fixed model slugs, and required tracker integrations are not part of this package.
