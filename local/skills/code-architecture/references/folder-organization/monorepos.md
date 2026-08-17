# Organizing directories in monorepos

> How to lay out the **top level** of a monorepo. The rules inside any one part are the same as everywhere else — read `principles.md` for those, and the matching stack file for concrete trees.
>
> Currently covers single-product monorepos only. Multi-product repos are not settled yet.

## Single product monorepos

When one product ships as several independently deployed or published units (api service, website, admin panel, CLI, client SDKs), organize top level directories by these units:

- (root)
  - `/admin` - Deployed separately (package.json with `name: "admin"`)
  - `/api` - Deployed separately (package.json with `name: "api"`)
  - `/packages` - Internal packages consumed by the deployable units, not shipped on their own
  - `package.json`, `pnpm-workspace.json` - root level package config files

### Why

- **The top level reads as a deployment map.** Each top-level directory maps 1:1 to a deployable unit, so the root listing tells you what gets deployed or published.
- **No wrapper indirection.** `apps/` and `packages/` add a level that carries no domain meaning — `/api` beats `/apps/api`. Fewer path segments, shorter imports.
- **Consistent with the feature-first principle.** Same rule as `principles.md`, applied one level up: name by what it is in the product, not by technical role.
- **`packages/` groups what is deliberately not top level.** Keeping it while rejecting `apps/` is not a half-measure: `apps/` buries deployables behind a segment that means nothing, whereas `packages/` is the single bucket for the things that are *not* deployables. The top level then reads as "every entry ships, plus one directory for what doesn't."

