# Host behavior

Use capabilities actually exposed in the current session. Shared files do not create tools, provider access, background workers, or cross-host delegation.

- **Codex:** `agents/openai.yaml` sets `allow_implicit_invocation: false` for this entrypoint. Use the skill picker or an explicit `$bounds-mode` invocation. Other Bounds skills retain normal selection behavior.
- **Claude Code:** `disable-model-invocation: true` makes this entrypoint user-invoked. Use `/bounds-mode`. Supporting skills can be selected normally or invoked individually.
- **T3 Code:** discovery and tool availability come from the provider on the execution host. If the composer does not forward a provider's shorthand, explicitly name the skill and use its discovered path. Confirm it actually loaded. A T3 orchestration tool, when present, is a separate capability.

After installing or updating, start a fresh provider session and confirm discovery before relying on it. A natural-language mention is a request, not proof that metadata was honored. Do not infer one provider's behavior from another's successful install.

Conversation continuity, compaction, slash-command parsing, and automatic selection vary by host. Reinvoke explicitly in a new session. If discovery, a tool, or delegation is unavailable, report the limitation and use a proportionate local fallback. Never describe self-review as independent review.
