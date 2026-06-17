# Folder & Directory Organization — Principles

> This guide explores the trade-offs only enough to justify a pick, then **commits to one
> default with firm rules**. When in doubt, follow the rules — don't re-litigate the
> trade-offs.
>
> These principles are stack-agnostic. Concrete directory trees for a specific stack
> (e.g. `nextjs.md`, `node-service.md`) live as sibling files in this folder; read the
> one matching the project in play.

## The decision

**Organize by feature/domain at the top level; layer *inside* a feature only once it
grows.** Plus a deliberate **shared layer** for genuinely cross-cutting code, established
from the start.

So the top level reads as a list of *what the product does* (`billing/`, `search/`,
`auth/`), not *what things are* (`controllers/`, `models/`, `components/`). Within a
small feature, keep files flat. When a feature gets big enough that the flat list is hard
to scan, sub-divide it by layer (`ui/`, `logic/`, `data/`) — not before.

## Why (briefly)

- **Feature-first keeps related code together.** A change to "billing" touches billing's
  UI, logic, and types — all in one folder, not scattered across four type-named
  directories. You read and modify a feature as a unit.
- **It scales with the product.** New capability → new feature folder. The top level grows
  in a dimension that means something to humans, instead of a fixed set of technical
  buckets that everything gets crammed into.
- **Layer-first scatters change** across `controllers/`, `services/`, `models/`… and the
  top level tells you nothing about what the app actually does. Reserve layering for
  *inside* a feature, where it earns its keep only once the feature is large.
- **A dedicated shared layer prevents the junk-drawer.** Cross-cutting code needs an
  obvious home; without one it accretes into a `utils/` swamp or gets duplicated. Naming
  it up front makes "is this shared?" a deliberate decision, not an accident.

## Rules

1. **Top level is organized by feature/domain**, named after what the product does — nouns
   from the domain, not technical roles.
2. **A feature folder owns everything for that feature** — its UI, logic, types, tests,
   and local helpers live together. It must *not* reach into another feature's internals;
   cross-feature use goes through that feature's public surface or through the shared layer.
3. **Keep a feature flat until it hurts.** Only introduce internal layer folders
   (`ui/`, `logic/`, `data/`, etc.) when the flat file list is genuinely hard to scan.
   Don't pre-create empty layer folders.
4. **Cross-cutting code lives in a dedicated `shared/` layer.** Use `shared/` as the name
   — consistently, one home. This is for code with no single feature owner: design-system
   primitives, framework/vendor wrappers, app-wide types, generic helpers.
5. **The shared layer is for the genuinely shared, not the conveniently dumped.** If a
   thing belongs to one feature, it stays in that feature even if it's "kind of generic."
   Shared is a deliberate home, not a default landing spot. Don't scaffold `shared/` (or
   sub-folders inside it) in advance — let it appear when the first genuinely shared thing
   needs a home.
6. **Name by domain, not by pattern.** Folders say *what the code is about*
   (`checkout/`, `notifications/`), not *what design pattern it uses* (`factories/`,
   `helpers/`).
7. **When a framework imposes a convention directory, keep it thin and delegate inward.**
   Some frameworks own part of your layout — the folder structure *is* the config (Next.js
   `app/` routing, Nuxt `pages/`, Remix `routes/`, Rails `app/`). Don't fight it and don't
   put your feature logic there. The convention directory holds thin entry points that
   import from your domain-organized code and wire it in; the real feature lives in your
   own tree, where rules 1–6 apply. The framework folder obeys the framework; everything
   you own obeys these principles.

## Where new code goes (decision flow)

When adding something and unsure where it belongs:

1. **Does it belong to exactly one feature?** → Put it in that feature's folder. Keep it
   flat unless the feature is already layered.
2. **Is it used by two or more features (or app-wide infrastructure with no single
   owner)?** → Put it in the shared layer.
3. **Is it "kind of generic" but currently used by only one feature?** → Keep it local to
   that feature. Promote to shared *only when a second real consumer appears* — don't
   pre-promote on speculation.
4. **Is it a whole new capability?** → Create a new top-level feature folder for it.
5. **Is it a framework route/convention file** (e.g. a Next.js `page.tsx`)? → Put it in the
   framework's convention directory, kept thin — it should import from the feature's own
   folder and render, not hold logic.

## Anti-patterns

- **Type-named top level** (`controllers/`, `services/`, `components/`, `models/` at the
  root) — scatters every change across buckets and hides what the app does.
- **Premature `utils/` / `helpers/`** — a magnet folder with no clear owner; it grows
  without bound and hides duplication. Use the shared layer deliberately instead.
- **Pre-layering small features** — empty or near-empty `ui/`/`logic/`/`data/` folders
  inside a feature that has three files. Add structure when the size demands it, not before.
- **Cross-feature reaching** — one feature importing another's internal files. Go through a
  public surface or the shared layer; otherwise the feature boundary is fiction.
- **Pattern-named folders** (`factories/`, `decorators/`) — organize by what the code is
  *about*, not the pattern it happens to use.
