# Validation

This file records release-candidate evidence and its limits. Installer validation creates fresh temporary homes for child processes, with isolated provider/config/cache directories. It never installs into the invoking user's skill homes. Logs and generated recipes remain in the temporary test projects.

## Reproduce

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/validate_install.py
```

The installer script prints its temporary run directory. It invokes the real `npx --yes skills@1.7.0` CLI and checks file hashes, selective discovery, all eight packages, provider lists, tag upgrades, SHA rollback, removal, and preservation of an unrelated installed sentinel. Its disposable HTTP Git remote tests refs without publishing test tags.

CI runs only package integrity and validator failure cases. Installer and provider tests are explicit local runs; CI does not install the bundle into provider homes.

Once a candidate commit is pushed, also test the GitHub path:

```sh
python3 scripts/validate_install.py --remote "https://github.com/boundsj/bounds-skills/tree/$bounds_ref"
python3 scripts/validate_codex_discovery.py /path/printed/by/validate_install
```

The optional remote pass compares all installed skill files with the checkout and runs installer check/update against the pinned source. The discovery script starts a new Codex app-server and uses its `skills/list` API; it needs no model credentials. Retained evidence is under the run directory's `evidence/` folder. Remove that specific temporary run directory when finished with its evidence.

Behavioral validation exercises representative tasks in disposable projects. The runner copies only the already-installed Bounds packages into another temporary home, creates a synthetic CLI project, and starts a fresh provider process. Model credentials are needed for actual turns. For Codex, `--codex-auth /path/to/auth.json` temporarily copies only that credential file with mode 0600 and deletes the copy in `finally`; it never prints its contents. Provider-managed system defaults may still start their own tools. The runner isolates writable homes, not the provider binary or system configuration.

```sh
python3 scripts/run_behavior.py /path/to/install-run --case simple --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --case create --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --case maintain --recipe-project /path/to/create-run/project --model YOUR_MODEL --effort YOUR_EFFORT --codex-auth /path/to/auth.json
python3 scripts/run_behavior.py /path/to/install-run --provider claude --case simple
```

Other cases are `plan`, `debug`, `review`, `retro`, `docs`, `missing`, `optout`, `optout_same`, and `catalog`. `optout_same` first invokes mode, then resumes that isolated Codex session with an opt-out; its initial turn is retained in `prime.jsonl`. The runner's exit code is provider process status, **not a behavioral pass**. Inspect the final result, commands, diff, and retained artifacts. `events.jsonl`, `prompt.txt`, and `result.json` remain in the printed temporary run directory; do not publish provider traces or authentication data. No real project or user-home skills are used as test fixtures.

## Recorded results

The immutable package source tested on GitHub is [`38703034edb2c9c163263278ffe3dde05ed32d4b`](https://github.com/boundsj/bounds-skills/tree/38703034edb2c9c163263278ffe3dde05ed32d4b). Later evidence/documentation commits do not change the skill payload unless noted below. No release tag was published; tag upgrade and SHA rollback used a disposable local Git remote.

Completed on the Mac Mini, macOS 26.5 arm64, 2026-10-04. Installer: Node 26.0.0, npm 11.12.1, `skills@1.7.0`. Validation scripts: Python 3.14.2; Git 2.50.1 (Apple Git-155). Providers: Codex CLI 0.160.0 and Claude Code 2.1.288. Codex behavioral cases requested GPT-6 Astra, max reasoning, fast service. Fixture commands used the provider shell's Python 3.9.6.

| Check | Observed result |
| --- | --- |
| Package integrity | Eight frontmatter records, internal reference links, explicit mode policy, reachable conditional references, and both MIT notices in each installable directory pass. Entrypoints are 254–332 words. |
| Validator failure cases | Five unit tests pass, including rejecting missing references, sibling-skill dependencies, missing attribution and accidental implicit mode. |
| Upstream skill-creator check | Seven skills pass directly. Mode's portable fields pass; the validator's older allowlist rejects Claude's `disable-model-invocation` extension. Real Codex/Claude discovery parses that file successfully. The extension is deliberately retained. |
| Isolated installation | Selective/full installation, complete file hashes, provider lists, tag upgrade, SHA rollback, scoped Claude removal, full removal and unrelated sentinels pass. |
| GitHub distribution | Full-SHA tree URL installs all eight with identical hashes. `check` reports current; scoped `update` against that immutable source changes no payload. |
| Moving-ref update limit | Independent review reproduced an upstream CLI issue: after Codex/Claude-only installation, `update --global bounds-plan --yes` for a changed tracked ref also creates a Windsurf link when that provider is detected. The supported upgrade instructions use explicit pinned re-add with agent selection. |
| Fresh Codex discovery | A new app-server's `skills/list` reports all eight enabled without parse errors, for both local and remote installs. |
| Codex explicit-mode policy | A no-tool catalog query lists the seven supporting skills and excludes mode; explicit `$bounds-mode` loads and executes in the other cases. |
| Fresh Claude discovery | New-process init reports all eight in `skills` and `slash_commands`. The attempted `/bounds-mode` turn returns `Not logged in`; no model invocation success is claimed. |
| Simple mode | Only the requested README typo changes; diff check passes. No supporting skill or reference is read. |
| Plan | Produces scope, retained JSON behavior, acceptance examples and dependencies; eight baseline checks pass; no files change. |
| Debug via mode | Reads the debugging workflow, reproduces the wrong page, fixes the offset, and passes 12 concrete CLI cases. Only product correction changes. |
| Review without delegation | Pins base/head, executes both revisions, identifies the pagination regression with file/line and impact, labels the review local, and changes no files. |
| Retro | Uses only the specified synthetic work log, distinguishes a repeated correction from a single incident, recommends wiring the existing check, and labels actual enforcement unverified. |
| Agent docs | Repairs a stale CLI command and duplicated guidance, checks output and links, changes only AGENTS.md. |
| Create verification | Generates a local recipe and four-feature map; 14 real CLI cases pass. Independent inspection confirms cleanup removed runtime state, retained readable evidence with unchanged hashes, and left product code unchanged. |
| Maintain verification | Corrects intentional command-rename drift and a stop-on-first-failure harness gap, then executes all 14 mapped cases: 8 pass, 6 fail for the separate seeded pagination defect. Reports blocked, retains original expectations, changes only verification files, and preserves evidence after cleanup. Product code stays unchanged. |
| Missing supporting skill | With only mode installed, reports `bounds-plan` absent and delivers the requested plan through local inspection; installs nothing and changes no files. |
| Fresh-turn opt-out | “Stop using bounds-mode” performs only the typo edit, with no skill body read. Same-session opt-out is checked separately below. |
| Same-session opt-out | First invokes mode for a read-only summary, then resumes that same Codex session with an opt-out. The second turn makes only the requested typo correction and does not load supporting workflows. |

An independent reviewer inspected base `722ce9ce2e5da00dc9946aa5e2553ec8599ed1b1` through package commit `38703034edb2c9c163263278ffe3dde05ed32d4b`. The moving-ref update recommendation was the sole actionable finding; the installation guide now uses the tested explicit re-add path. No skill-body or attribution findings were reported. Later documentation and harness changes receive local checks; the review is not claimed for an unseen revision.

These are representative synthetic CLI cases, not a model reliability benchmark or proof for browser, mobile, performance, or production workflows. Claude authenticated invocation and implicit-selection behavior remain unverified. Fresh installed-bundle discovery in the T3 composer, other hosts/operating systems, and a real user-home rollout remain untested. No cross-host synchronization or delegation is provided by the bundle.
