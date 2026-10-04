# Validation

This file records release-candidate evidence and its limits. Installer validation creates fresh temporary homes for child processes, with isolated provider/config/cache directories. It never installs into the invoking user's skill homes. Logs and generated recipes remain in the temporary test projects.

## Reproduce

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
python3 scripts/validate_install.py
```

The installer script prints its temporary run directory. It invokes the real `npx --yes skills@1.7.0` CLI and checks file hashes, selective discovery, all eight packages, provider lists, tag upgrades, SHA rollback, removal, and preservation of an unrelated installed sentinel. Its disposable HTTP Git remote tests refs without publishing test tags.

Once a candidate commit is pushed, also test the GitHub path:

```sh
python3 scripts/validate_install.py --remote "https://github.com/boundsj/bounds-skills/tree/$bounds_ref"
python3 scripts/validate_codex_discovery.py /path/printed/by/validate_install
```

The optional remote pass compares all installed skill files with the checkout and runs installer check/update against the pinned source. The discovery script starts a new Codex app-server and uses its `skills/list` API; it needs no model credentials. Retained evidence is under the run directory's `evidence/` folder. Remove that specific temporary run directory when finished with its evidence.

Behavioral validation must also exercise representative tasks in disposable projects: a small mode edit, plan-only scope, reproduced debugging, review with unavailable delegation, a bounded retrospective, agent-doc maintenance, and recipe creation/maintenance with evidence surviving cleanup. Evaluate observable results and tool traces, not just an assistant's claim to have followed a skill.

## Recorded results

Release-candidate execution results are added after the isolated checks complete. No support claim rests on this checklist alone.
