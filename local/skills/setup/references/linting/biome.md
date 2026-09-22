# Formatting and linting — Biome

> This guide commits to one default with firm rules. When in doubt, follow the rules.
>
> Scope: any TypeScript/JavaScript project. The layout below is written for a monorepo;
> see "Single-package projects" at the end for the collapsed form.

## The decision

**Use [Biome](https://biomejs.dev) as the single formatter, linter, and import organizer.** Not ESLint, not Prettier, not both. One binary, one config format, one pass over the file — no plugin resolution, no formatter/linter rule conflicts to arbitrate.

## Install

**Install Biome once, at the repo root.**

```bash
pnpm add -Dw @biomejs/biome
```

Not per package. Every package extends the same base config and runs the same two commands, so a
per-package copy buys nothing and risks the packages drifting onto different Biome versions.

## Config layout

Three files, each with a distinct job. Only the first carries opinions:

- **The shared base** holds every opinion — rules, formatter, VCS integration. One file, one owner.
- **The root config** anchors the tree. Biome requires one; it holds no opinions of its own.
- **A package config** exists only to declare a deviation from the base.

**1. The shared base**, in an internal config package:

```jsonc
// packages/configs/package.json
{
  "name": "@repo/configs",
  "private": true,
  "exports": { "./biome": "./biome.json" }
}
```

```jsonc
// packages/configs/biome.json
{
  "$schema": "../../node_modules/@biomejs/biome/configuration_schema.json",
  "root": false,
  "files": { "ignoreUnknown": true },
  "vcs": { "enabled": true, "clientKind": "git", "useIgnoreFile": true },
  "assist": { "actions": { "source": { "organizeImports": "on" } } },
  "linter": {
    "enabled": true,
    "rules": { "preset": "recommended" }
  },
  "formatter": { "enabled": true, "indentStyle": "space", "indentWidth": 2 },
  "javascript": {
    "formatter": { "quoteStyle": "double", "semicolons": "asNeeded" }
  }
}
```

`"root": false` keeps it out of the one-root-per-tree count (rule 2) — it is a fragment to extend, never a config Biome runs from.

**2. The root config**, which anchors the tree and nothing else:

```jsonc
// biome.json
{
  "$schema": "./node_modules/@biomejs/biome/configuration_schema.json",
  "extends": ["@repo/configs/biome"]
}
```

This is not a third layer of opinion. Biome 2 requires exactly one config per tree without `"root": false`, and this is it — a mechanical requirement, not a design decision. It also happens to cover loose files at the repo root (`turbo.json`, `docker-compose.yml`, root scripts), which need no rules of their own.

Resist putting exclusions here. Biome skips `node_modules` unconditionally — with no `.gitignore` and `vcs` disabled outright, it still won't walk it — and `vcs.useIgnoreFile` covers everything in `.gitignore`, build output included. A `files.includes` at the root is almost always a no-op restating one of those two.

**3. A package config only where a package genuinely differs**, extending the base with `"root": false`:

```jsonc
// packages/db/biome.json — exists for one exclusion
{
  "$schema": "../../node_modules/@biomejs/biome/configuration_schema.json",
  "extends": ["@repo/configs/biome"],
  "root": false,
  "files": { "includes": ["**", "!supabase/migrations"] }
}
```

```jsonc
// apps/web/biome.json — exists for one rule
{
  "$schema": "../../node_modules/@biomejs/biome/configuration_schema.json",
  "extends": ["@repo/configs/biome"],
  "root": false,
  "linter": { "rules": { "a11y": { "useValidAriaRole": "off" } } }
}
```

Packages with no deviation get **no file at all** — a config holding only `extends` and a redundant exclusion is noise that reads like configuration.

Whether you're removing a config or adding an exclusion, confirm it matters the same way: delete it, re-run, compare the file count and the diagnostics. Most exclusions turn out to be no-ops.

## Rules

1. **A package config exists only to hold a deviation.** If deleting it changes nothing, delete it. A config that only re-states the base is a fork waiting to drift.
2. **Every config outside the repo root is `"root": false`.** Biome allows exactly one root config per tree; a second one fails the run with `Found a nested root configuration`.
3. **`$schema` is relative to the config file, not to the package.** With a root-only install, a config two levels down needs `../../node_modules/...`. A wrong path costs nothing at runtime — Biome ignores it — but your editor silently loses completion and validation.
4. **Start from the `recommended` preset and turn individual rules off.** Don't hand-pick a rule list. The preset moves with the tool; an explicit list rots into whatever was current the day it was written.
5. **A disabled rule is a deviation, not a default.** Turn it off in the package that needs it. Promote it to the base only once a second package needs the same exception.
6. **Let `vcs.useIgnoreFile` do the excluding.** Set it once in the base. Build output, caches, and local artifacts are already in `.gitignore`; restating them in `files.includes` is duplication that goes stale on its own schedule.
7. **`files.includes` is for what `.gitignore` can't express** — committed source you don't want linted. Generated migrations, scaffolded component libraries (shadcn's `components/ui`), codegen output. You didn't author it, so its style isn't yours to enforce, and reformatting it fights the generator on every regeneration.
8. **Write exclusions by negation:** `["**", "!supabase/migrations"]`. New source directories are covered the day they appear; an allowlist silently skips them.
9. **`"ignoreUnknown": true` belongs in the base, once.** Biome should pass over file types it has no parser for rather than failing. It's a repo-wide stance, not a per-package one.

## Scripts and the task runner

**A whole-tree tool that already understands the monorepo gets invoked once, directly. Don't route it through the task runner.**

A task runner earns its place on per-package work that produces artifacts it can hash, cache, and parallelize across the dependency graph. A repo-wide format pass is none of those things: Biome resolves each file's config itself in a single walk, so fanning it out into one invocation per package buys you N process startups and interleaved output to split work a single process already does in one pass.

Formatting is also a *write*, which a cache must never skip. A cached write task with no declared outputs stores an empty entry, and on an input-hash repeat — a revert, a branch switch, a bad merge — reports success without running, leaving files unformatted.

So, at the repo root:

```jsonc
{
  "scripts": {
    "format": "biome check --write .",
    "lint": "turbo lint"
  }
}
```

`format` calls Biome directly. There is no `format` task in the task runner config at all — nothing to configure, nothing to cache wrongly.

`lint` stays behind the runner: `biome check .` is read-only, and a per-package pass/fail verdict over unchanged inputs is a real thing to cache and skip. Give it no `dependsOn` — linting a package doesn't consume its dependencies' lint results, so `["^lint"]` only serializes work that could run in parallel:

```jsonc
// turbo.json
{ "tasks": { "lint": {} } }
```

Packages keep only `"lint": "biome check ."`. Drop their `format` scripts — nothing calls them once the root stops fanning out, and `biome check --write .` from inside any package does the same job.

**Why `check --write` and not `format --write`.** `biome format` touches formatting only. `organizeImports` is an *assist* action, applied by `biome check --write`. Using `check --write` as the one write command means import order is always handled — after a path-alias change, a moved module, a merged barrel file — instead of being a separate step you have to remember.

## Running it on part of the repo

Biome resolves config per file, not per invocation. For each file it walks up to the nearest
`biome.json` and follows its `extends` chain — so a path argument given from the repo root still
gets that package's rules and exclusions:

```bash
pnpm biome check apps/web/features/billing
```

You don't need the package manager's workspace filter to scope a run, and one call may span
packages with different configs — each file is still judged by its own.

The one to remember:

```bash
pnpm biome check --changed --since=main
```

Lints only what changed against a ref, using the `vcs` config. Usually what you actually want
instead of naming directories by hand, and it crosses package boundaries the way a changeset does.

When fixing a subset with `--write`, scope the path to the change rather than to the package you
happen to be working in — an import-path rewrite leaves importers elsewhere needing the same pass.

## Single-package projects

There is nothing to share, so there is nothing to split: one `biome.json` at the repo root holding the rules, formatter settings, and `vcs`. No `@repo/configs` package, no `"root": false` anywhere, and no task runner in the picture — `format` and `lint` both call Biome directly:

```jsonc
{
  "scripts": {
    "format": "biome check --write .",
    "lint": "biome check ."
  }
}
```
