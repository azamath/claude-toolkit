---
allowed-tools: Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*)
description: Create a git commit using conventions
argument-hint: [--staged | <paths...>]
---

Your task is to help the user to generate a commit message and commit the changes using git.

## Guidelines

- DO NOT add any ads such as "Generated with [Claude Code](https://claude.ai/code)"
- Generate the message only for what will actually be in the commit.
- Follow the rules below for the commit message.

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


## Format

```
<type>:<space><message title>

<bullet points summarizing what was updated>
```

## Example Titles

```
feat(auth): add JWT login flow
fix(ui): handle null pointer in sidebar
refactor(api): split user controller logic
docs(readme): add usage section
```

## Example with Title and Body

```
feat(auth): add JWT login flow

- Implemented JWT token validation logic
- Added documentation for the validation component
```

## Rules

* title is lowercase, no period at the end.
* Title should be a clear summary, max 50 characters.
* Use the body (optional) to explain *why*, not just *what*.
* Bullet points should be concise and high-level.

Avoid

* Vague titles like: "update", "fix stuff"
* Overly long or unfocused titles
* Excessive detail in bullet points

## Allowed Types

| Type     | Description                           |
|----------|---------------------------------------|
| feat     | New feature                           |
| upd      | Update to an existing feature         |
| fix      | Bug fix                               |
| chore    | Maintenance (e.g., tooling, deps)     |
| docs     | Documentation changes                 |
| refactor | Code restructure (no behavior change) |
| test     | Adding or refactoring tests           |
| style    | Code formatting (no logic change)     |
| perf     | Performance improvements              |