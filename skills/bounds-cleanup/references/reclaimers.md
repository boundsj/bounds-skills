# Reclaimers

Common measuring and removal commands by owner. Confirm each tool is installed and check its help for the installed version before running it. Commands that remove data run only after the user approves that category. Default locations below are platform defaults; projects and users can move them.

## Measure

- Free space: `df -h` on each affected volume.
- Folder size: `du -sh <path>`. On copy-on-write file systems, clones and shared blocks can make the sum exceed what deletion frees.
- Worktrees: `git worktree list --porcelain`; a `detached` or `locked` line is a gate. Per worktree, `git -C <path> status --porcelain --ignored` (ignored files are deleted with the worktree), `git -C <path> log --oneline HEAD --not --remotes` (commits only this worktree's HEAD holds, including a detached one), and the PR state for its branch. `lsof +D <path>` shows processes holding files there; it is slow on large trees.
- Cache locations: `npm config get cache`, `pnpm store path`, `uv cache dir`, `pip cache dir`, `go env GOCACHE GOMODCACHE`, `brew --cache`; size each with `du -sh`.
- Containers: `docker system df`.
- Homebrew: `brew cleanup -n` lists what cleanup would remove.
- macOS: local snapshots (`tmutil listlocalsnapshots /`) and purgeable space can delay freed space appearing in `df`.

## Git worktrees

`git worktree remove <path>` refuses a tree with modified or untracked files, but it deletes ignored files such as `.env` files and local databases; list them first. `--force` discards uncommitted and untracked files too, so use it only after that loss is approved. For a detached worktree with local commits, create a branch first (`git -C <path> branch <name>`), with the user's OK. If removal leaves files behind, such as read-only files, remove the leftover folder inside the approved path. Then `git worktree prune` (preview with `--dry-run`). Branch refs survive unless deleted separately.

## Apple platforms

- Derived data: `~/Library/Developer/Xcode/DerivedData`; rebuilt on the next build. Quit Xcode first.
- Device support: `~/Library/Developer/Xcode/iOS DeviceSupport` and its other-platform siblings; recreated when a device connects. Keep entries for devices still in use.
- Archives: `~/Library/Developer/Xcode/Archives` hold debug symbols for shipped builds; ask before touching.
- Simulators: `xcrun simctl delete unavailable`; XCTest device clones with `xcrun simctl --set testing delete all`; old runtimes from `xcrun simctl runtime list` then `xcrun simctl runtime delete <id>`.
- Swift packages: per-project `.build` folders; the shared package cache under `~/Library/Caches/org.swift.swiftpm`.

## Android

List with `avdmanager list avd` and `sdkmanager --list_installed`; remove emulators with `avdmanager delete avd -n <name>` and packages with `sdkmanager --uninstall <package>`. Stop Gradle daemons before clearing `~/.gradle/caches`; `./gradlew --stop` stops only daemons of that project's Gradle version.

## Package managers and toolchains

- npm: measure with `du -sh "$(npm config get cache)"`; `npm cache verify` checks and garbage-collects; `npm cache clean --force` clears.
- pnpm: `pnpm store prune`.
- Yarn: `yarn cache clean`.
- Bun: `bun pm cache rm`.
- uv: `uv cache prune`, or `uv cache clean` to clear everything.
- pip: `pip cache purge`.
- Conda: `conda clean --all`.
- Cargo: `cargo clean` per project for `target/`.
- Go: `go clean -cache`; `go clean -modcache` for downloaded modules.
- Homebrew: `brew cleanup` (add `--prune=all` only when approved).
- Dependency folders such as `node_modules` in inactive projects are reinstallable from the lockfile; name the projects.

## Containers

`docker image prune` (add `-a` for all unused images) and `docker builder prune`. Stopped containers keep their writable layer, which can hold data and could be restarted: list them with `docker ps -a -s --filter status=exited` and gate `docker container prune` like volumes. Volumes may hold databases or other user data: `docker volume prune` and `docker system prune --volumes` need explicit approval for that loss. Docker Desktop's disk image may not shrink right away, so measure the host volume after.
