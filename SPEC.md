# Bounds skills specification

Build a small, portable collection of engineering workflows for Codex and Claude Code, usable directly and through T3 Code. Optimize for accepted useful work per minute of human attention: selective context loading, fewer repeated corrections, and trustworthy implementation, review and verification evidence.

## Eight skills

- `bounds-mode`: explicit entrypoint that selects the appropriate workflow, coordinates supporting skills and carries work through proportionate verification and review. Keep routing thin. Do not run every phase on every task. Honor opt-out and explain provider limits on continuity across turns.
- `bounds-plan`: turn an idea into a concise plan with scope, retained behavior, acceptance checks and dependencies. Clarify material ambiguity; infer routine details from available context.
- `bounds-debug`: reproduce an observed problem, isolate its cause, fix it and verify behavior with a meaningful repeatable check.
- `bounds-review`: inspect a pinned change for correctness, requirement compliance and maintainability. Distinguish actionable findings from preferences and actual evidence from assumptions.
- `bounds-retro`: examine a bounded set of accessible work for repeated corrections and wasted effort. Prefer improvements to structure, checks, tooling and navigation over additional standing instructions.
- `bounds-agent-docs`: create and maintain concise agent-facing documentation with accurate commands, clear entrypoints and conditional references.
- `bounds-create-verification`: create a project-local recipe using existing tools: Launch, Doctor, Drive, Evidence, Cleanup. Prove it by execution; evidence must survive cleanup. Include a small feature map.
- `bounds-maintain-verification`: keep that recipe and feature map accurate as the project changes. Separate documentation drift, harness gaps and product defects; report coverage honestly.

## Usage and portability

Users can explicitly enter bounds-mode with a task or invoke any individual skill. The mode loads supporting skills only when their phase is needed. It must not grant permissions, force broad audits for simple requests, hardcode model slugs or assume a particular tracker. Verify invocation metadata and discovery behavior separately for Codex and Claude; do not promise that Cursor sticky-mode behavior is portable.

Keep entrypoints to a few hundred words where practical, with narrow trigger descriptions and conditional references. Preserve existing specialists and native host tools. Provider adapters should be minimal and justified by actual differences. No universal requirement to read every skill or reference at startup.

Shared skills do not provide cross-host delegation. Where review uses delegation, discover native capabilities and use a bounded brief keyed to base/head SHA. Default to one independent reviewer when warranted, another only for consequential or disputed work. Refresh evidence after relevant changes. Bound fix/review loops and return unresolved issues rather than looping indefinitely. Evidence should record commands/results, host, revision and coverage limits without imposing paperwork on trivial work.

## Installation and documentation

Use standard SKILL.md directories in this repository and prefer the existing Vercel skills CLI (`npx skills`) over a custom installer. Target global Codex and Claude installations so skills are available across projects. Install separately on each execution host; T3 uses that host's provider. Keep generated project-specific verification recipes in the relevant project.

Validate exact commands before documenting them. Cover install, selective installation, update, list/status and removal. Test tagged/revision-based installation for repeatable multi-host updates. Use temporary provider homes first and preserve existing skill files. Verify fresh-session discovery before claiming a provider/host is supported. Do not claim an installation on one host synchronizes others.

The README should lead with a bullet summary of each skill and useful example prompts. Keep installation and maintenance docs short. Record tested versions and distinguish packaging tests from real invocation tests. No separate installer or plugin framework unless a demonstrated gap requires it.

## Sources and attribution

Adapt selected workflows; do not install upstream collections wholesale or copy their provider-specific assumptions unchanged.

- Matt Pocock: https://github.com/mattpocock/skills/tree/24fe0ef7737efae15c87225755e9f6f5965e4888 — to-spec, to-tickets, diagnosing-bugs, tdd, code-review, retro and writing-for-agents.
- pstack: https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack — mode routing, interrogate, correct, create-verification-skill, maintain-verification-skill and relevant engineering principles.
- Installer: https://github.com/vercel-labs/skills

Retain both upstream MIT notices (Matt Pocock and Lauren Tan), source revisions and meaningful adaptation notes. If newer upstream material is needed, explicitly record the chosen revision. Avoid mandatory seam-approval rituals, excessive ticket breakdowns, broad rewrites and Cursor-only model/delegation assumptions.

## Boundaries and first release acceptance

This is a standalone workstream. No project-specific tickets, paths, private session histories, required Notion integration, broader fleet automation, Grok Bot, Pi or Durable integrations. Do not publish raw conversation history, private roadmap links or local authentication data.

Deliver eight coherent skills, selective references, concise docs, attribution and reproducible validation. Test discovery/packaging, reference integrity, representative routing examples, installation/update/removal in isolated homes, and truthful missing-capability behavior. Show actual results and remaining gaps. Real installation into user homes is a separate rollout after the bundle is reviewable; do not change other projects or hosts during authoring.
