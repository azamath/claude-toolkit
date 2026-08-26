---
allowed-tools: Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*)
description: Create a git commit using conventions
argument-hint: [--staged | <paths...>]
---

Your task is to help the user to generate a commit message and commit the changes using git.

## Guidelines

- Stage changes according to the staging behavior below.
- **Load the `git-committing` skill** and follow it to author the commit message.

## Staging behavior

Arguments: `$ARGUMENTS`

- **`--staged`** → do not run `git add`. Commit only what is already in the index.
- **Path arguments** (e.g. `src/foo.ts src/bar.ts`) → run `git add -- <paths>` for those paths only, then commit.
- **No arguments (default)** → stage changes automatically, but with judgment:
  1. Run `git status` and `git diff` to see all changed/untracked files.
  2. Decide whether the changes form a single coherent unit of work (same feature, same module, related fix).
  3. **Stage silently and commit** when:
     - Changes are clearly related, OR
     - Only one or two files changed.
  4. **Ask the user first** (via AskUserQuestion) when:
     - Changes span unrelated areas (e.g. an auth fix + an unrelated README typo + a dependency bump).
     - Something suspicious appears (`.env*`, credentials, large binaries, stray debug logs in unrelated files).
     - Untracked files don't obviously belong (scratch scripts, experimental files).
  5. Stage what was confirmed (or what was clearly coherent):
     - If **all** changes belong to the same unit of work, `git add -A` is fine.
     - Otherwise, stage explicitly by path with `git add -- <paths>` and leave unrelated changes untouched.
     - Never use `git add -A` / `git add .` when there are unrelated or suspicious changes in the worktree.
