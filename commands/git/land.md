---
allowed-tools: Bash(git merge:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git log:*), Bash(git switch:*), Bash(git rebase:*), Bash(git pull:*), Bash(git push:*), Bash(git branch:*), Bash(git rev-parse:*), Bash(git stash:*), Bash(git symbolic-ref:*)
description: Land current branch onto the default branch
---

Land the current branch onto the default branch. This means: commit any pending changes, rebase onto the latest default branch, merge, push, and clean up the feature branch.

Throughout this document, `<default>` refers to the repository's default branch (e.g., `main`, `master`, `develop`).

## Pre-flight Checks

1. Detect the default branch: `git symbolic-ref --short refs/remotes/origin/HEAD` (returns e.g. `origin/main`; strip the `origin/` prefix). If that fails, fall back to checking for `main` or `master` locally.
2. Identify the current branch. If already on `<default>`, abort with a message.
2. Detect if inside a git worktree: compare `git rev-parse --git-dir` and `git rev-parse --git-common-dir`. If they differ, you are in a worktree.
3. Run `git status` to check for uncommitted changes.
   - If there are staged or unstaged changes, you MUST use the `/git:commit` skill to commit them. Never run `git commit` directly — the skill applies project commit conventions.
   - If the commit is skipped or fails, abort the merge.

## Merge Procedure

### Step 1: Rebase onto default branch

```
git pull --rebase origin <default>
```

If rebase conflicts occur:
- Assess the scope: check `git diff --name-only --diff-filter=U` for conflicting files and the size of conflicts.
- If conflicts are minor (few files, small changes), attempt to resolve them.
- If conflicts are large or risky (many files, complex changes), run `git rebase --abort` and inform the user.

### Step 2: Merge and push

**If in a worktree:** push the branch directly to the default branch on the remote (guaranteed fast-forward after rebase):
```
git push origin <branch-name>:<default>
```

**If in a regular checkout:**
```
git switch <default>
git pull
git merge <branch-name>
git push origin <default>
```

### Step 3: Clean up the feature branch

- If the branch had a remote tracking branch, delete it: `git push origin --delete <branch-name>`
- If in a worktree, skip local branch deletion (worktree cleanup is a separate workflow).
- Otherwise, delete the local branch: `git branch -d <branch-name>`

## Rules

- Never force-push or use `--force`.
- Never use interactive rebase (`-i`).
- If merge conflicts occur, stop immediately and report the issue to the user.
- For rebase conflicts, assess risk before deciding to resolve or abort (see procedure above).
