# Installation and updates

Requires Git, Node.js/npm, and the provider installed on the execution host. The tested installer is `skills@1.7.0`; `npx --yes` accepts downloading that CLI, while the final `--yes` accepts the selected skill installation.

No repository registration or npm publication is needed. `npx` runs the skills CLI, which reads the skill directories directly from GitHub. The shorthand `boundsj/bounds-skills` follows the repository's default branch; use a pinned URL to try an unmerged candidate or keep installations repeatable.

For repeatable installation, choose a reviewed full commit SHA (or a published release tag). Set `bounds_ref` to it, then use the same value on each host. Version 0.1.0 is a candidate; no release tag has been published. The exact tested revision is in [validation](validation.md).

```sh
bounds_ref='<reviewed full commit SHA or published tag>'
bounds_source="https://github.com/boundsj/bounds-skills/tree/$bounds_ref"

# Inspect the package before installation.
npx --yes skills@1.7.0 add "$bounds_source" --list

# Install all eight globally with explicit provider targets.
npx --yes skills@1.7.0 add "$bounds_source" --global --agent codex claude-code --skill '*' --yes

# Or select only the workflows you want.
npx --yes skills@1.7.0 add "$bounds_source" --global --agent codex claude-code --skill bounds-mode bounds-plan --yes
```

Installing a selection does not remove previously installed skills. Mode can use whichever supporting skills are present and reports missing ones. Each skill's references and license notices travel with it. In the tested CLI, Codex reads the canonical `~/.agents/skills` copy; Claude receives links in its configured skill home. Other providers that read the universal directory can also discover those files. Agent selection controls installer targets, not universal-directory visibility. Avoid `--all`, which selects every supported agent.

```sh
npx --yes skills@1.7.0 list --global --agent codex
npx --yes skills@1.7.0 list --global --agent claude-code
npx --yes skills@1.7.0 check
```

`check` is an informational installer status check and may include other tracked skills. Inspect its skipped/error messages. It does not prove provider discovery or invocation. Start a fresh Codex or Claude Code session and confirm the installed names are available. Invoke a small task explicitly before relying on the bundle across projects.

For a reproducible upgrade or rollback, change `bounds_ref` to the chosen revision and rerun `add` with your same explicit skill/agent selection. Keep the previous ref if you need to roll back. Re-adding overwrites selected skill names, so preserve any intentional local edits first.

Use explicit re-add for updates. In `skills@1.7.0`, `update --global <skill names> --yes` can install an updated skill into other detected providers because it does not preserve the original agent selection. This was reproduced in an isolated fixture. Naming only Bounds skills does not prevent that expansion. An immutable pinned source stays at that source; a successful no-change `update` is not proof of safe provider targeting, nor does it select a newer Bounds release. Local-path installations may also be skipped by update tracking. No custom installer is needed: re-add the chosen ref with the same explicit `--agent` and `--skill` arguments.

```sh
# Remove one skill from one provider.
npx --yes skills@1.7.0 remove bounds-plan --global --agent claude-code --yes

# Remove the Bounds bundle from both providers, preserving unrelated skills.
npx --yes skills@1.7.0 remove bounds-mode bounds-plan bounds-debug bounds-review bounds-retro bounds-agent-docs bounds-create-verification bounds-maintain-verification --global --agent codex claude-code --yes
```

Removing a Claude link can leave Codex's canonical copy intact. Removing from Codex alone cannot hide that shared copy while another provider still uses it; remove from both when removing the shared bundle. Installation is per execution host. T3 does not synchronize these files to another machine. The first release was tested in temporary homes; real user-home rollout is a separate step.
