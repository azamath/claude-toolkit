---
description: Conventions for authoring git commit messages — type prefixes, title and body format. Use when writing a commit message.
user-invocable: false
---

# Git Committing

Conventions for the commit message itself. Generate the message only for what will actually be in the commit.

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
* DO NOT add any ads such as "Generated with [Claude Code](https://claude.ai/code)"

Avoid

* Vague titles like: "update", "fix stuff"
* Overly long or unfocused titles
* Excessive detail in bullet points

## Core Types

* `feat` — New feature or functionality: capabilities and behaviors that didn't exist before, updates to an existing feature, and new configuration options.
* `fix` — Bug fix: correcting unintentional errors, resolving known issues, malfunctioning styles, and crashes.
* `docs` — Documentation: README files, inline comments and docstrings, API descriptions, setup instructions.
* `refactor` — Code restructure without behavior change: extracting helpers, splitting modules, renaming for clarity. Internal organization, unlike `style`.
* `test` — Adding, modifying, fixing, or improving tests: unit, integration, and end-to-end, including edge-case coverage.
* `perf` — Measurable performance improvements: speed or memory, reduced database/API overhead, caching.
* `chore` — Maintenance and routine tasks that don't touch production code: `.gitignore`, file renames without logic changes, dev dependencies, build warnings.
* `style` — Cosmetic changes only: formatter/linter runs, whitespace, indentation, line breaks. No behavior change.
* `build` — Build process or production dependencies: build scripts, dependency upgrades, bundling, deployment configuration.
* `ci` — Continuous integration: CI/CD configuration files, workflows (GitHub Actions, GitLab CI, Jenkins), new CI steps.
* `revert` — Rolling back a previous commit, referencing the reverted commit.
