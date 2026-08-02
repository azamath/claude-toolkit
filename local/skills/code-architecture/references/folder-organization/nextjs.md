# Folder Organization — Next.js (App Router)

> Concrete layout applying `principles.md` to a Next.js App Router project. Read
> `principles.md` first; this file only covers what's Next-specific. The headline is
> **Rule 7**: `app/` is framework-owned — keep it thin and delegate into your
> domain-organized code.

## The split

Next.js's `app/` directory **is** the router: the folder structure maps to URLs and
certain filenames are reserved by the framework. That makes `app/` framework-owned — it
can't be reorganized by domain, because its shape is dictated by routes.

So separate two trees, side by side at the project root:

- **`app/` — framework-owned, thin.** Routing-shaped files only. A `page.tsx` imports a
  feature component and renders it; it does not hold business logic, data shaping, or
  reusable UI.
- **Feature folders (+ `shared/`) — yours, domain-organized.** All the principles apply
  here. The actual feature lives here; `app/` just points at it.

Keep `app/` pure routing — feature code never lives inside it. Each feature is one folder
at the root, and the route delegates into it.

## What lives in `app/`

`app/` holds the framework's reserved files — `page`, `layout`, `route`, `loading`,
`error`, and so on — plus its routing constructs (`(groups)`, `[dynamic]`, `@slots`). For
what each one is and how routing maps folders to URLs, see the Next.js docs:
<https://nextjs.org/docs/app/getting-started/layouts-and-pages.md>.

What matters here is the rule, not the catalog: **everything in `app/` stays thin and
delegates inward.** These files are entry points, not homes — they import from a feature
folder and render or respond. Routing folders are URL constructs, not domain folders;
don't make them mirror your feature names beyond what the URL needs.

## Layout

Feature folders sit flat at the root, alongside the framework-owned `app/` and the
`shared/` layer. No `src/` wrapper.

```
.
├── app/                          # framework-owned: routing only, kept THIN
│   ├── layout.tsx                # root shell
│   ├── page.tsx                  # home — imports + renders a feature component
│   ├── billing/
│   │   ├── page.tsx              # `import { BillingPage } from '@/billing'` → render
│   │   └── invoices/
│   │       └── page.tsx
│   └── api/
│       └── billing/
│           └── route.ts          # thin: parse → call billing logic → respond
│
├── billing/                      # a feature — minimal shape (see "Inside a feature")
│   ├── BillingPage.tsx           # presentation layer — the UI component + its hooks
│   └── actions.ts                # data layer — fetching + actions + logic
├── search/                       # another feature
│   └── ...
│
└── shared/                       # cross-cutting, no single feature owner (Rule 4)
    ├── ui/                       # design-system primitives
    ├── lib/                      # framework/vendor wrappers
    └── types/
```

## Inside a feature

A feature folder has two tiers. Start at **Flat**; graduate to **Structured** only when a
feature genuinely outgrows it. Don't start structured — pre-built folders for a five-file
feature are the over-engineering this guide exists to prevent.

### Tier 1 — Flat

A flat folder, no subfolders. The minimal feature is **two files, split presentation
from data**:

```
billing/
├── BillingPage.tsx       # presentation layer — the UI component(s) + any custom hooks
└── actions.ts            # data layer — fetching + 'use server' actions + logic, together
```

Custom hooks (`useState`/`useEffect` view state, form handling, a data-fetching hook) are
**presentation** — they live with the component, in the same file at this size. Don't let
them disappear into the component unnamed; they're a real part of the UI layer.

The split line is **presentation vs. data**, *not* server vs. client. Server-vs-client is
a rendering detail (mark a component `'use client'` where needed); it is not how the
feature is organized. The presentation file(s) hold UI; `actions.ts` holds everything
behind it — fetching, mutations, and any business logic — grouped as one data layer.

> Why two and not one: a `'use client'` component and server-side data/actions don't
> belong in the same file, so two is the real floor. `actions.ts` keeps the data side
> bundled until it's big enough to split (Tier 2).

**Within Tier 1, a feature grows by extracting — only when a concern earns it** (it's
grown long, it's reused, or mixing it in hurts readability):

- Presentation splits into more **`*.tsx`** components (PascalCase, named for what they
  render), and **hook files** (`useInvoices.ts`, `useBillingForm.ts`) once a hook is reused
  or big enough to stand alone.
- The data side can start pulling pieces out of `actions.ts` — e.g. a `data.ts` for
  fetching once it's more than a call or two. It stays flat; it just becomes a few files.

Most features never leave Tier 1.

### Tier 2 — Structured (a mature feature)

At scale the two-file split isn't enough: the presentation side has many components, and
the data layer bundled in `actions.ts` is doing too many *different* jobs to stay in one
file. So the feature fans out. The presentation `*.tsx` files become **`ui/`**, and the
data layer separates into its distinct concerns — **`data/`** (fetching/queries),
**`actions/`** (`'use server'` mutations), and **`logic/`** (pure rules):

```
billing/
├── ui/                   # presentation — components AND their hooks
│   ├── BillingPage.tsx
│   ├── InvoiceList.tsx
│   ├── InvoiceRow.tsx
│   ├── useInvoices.ts    # hooks live here too — they're presentation
│   └── useBillingForm.ts
├── data/                 # data layer: fetching, queries
├── actions/              # data layer: 'use server' mutations
└── logic/                # data layer: pure business rules
```

The thread from Tier 1: what you kept bundled in `actions.ts` is exactly what splits apart
here. The presentation-vs-data line still holds — `ui/` on one side, `data/` + `actions/` +
`logic/` on the other — it's just that the data side is now big enough to warrant internal
structure.

Fan out **one part at a time**, not all at once: if only the components have multiplied,
make `ui/` and leave the data side as flat files. A feature can be half-and-half. And a
data-only concern you don't have (no real business rules → no `logic/`) simply doesn't
appear.

### When to graduate

- **Start at two files** (presentation + `actions.ts`) and stay flat while the feature
  reads comfortably — a handful of files, no single one dominating.
- **Extract within Tier 1** when one concern outgrows its file: pull `data.ts` out of
  `actions.ts`, split a component out of the page. Still flat, just more files.
- **Fan out to Tier 2** when the flat folder itself is hard to scan — a wall of `*.tsx`,
  or a data side that's become several files doing distinct jobs. Fan out the part that
  hurts; leave the rest flat.
- Judge on the **pain of finding things**, not file *count* — small files are fine.

### The boundary is a convention, not a wall

There's no `index.ts` barrel. Outside code imports a feature's top-level files directly
(`@/billing/data`), and the rule "don't import another feature's internals" is enforced by
discipline, not by the module system. This avoids barrel-file bundling and circular-import
headaches, at the cost of a boundary nothing mechanically guards — keep imports shallow and
deliberate.

### Types

Types aren't one bucket — put each where it belongs by what it is. There's no default
`types.ts`.

- **Derived / owner-local types** live **with their owner**, in the same file you derive
  them from — a component's prop/view-model types beside the component, a fetch-result type
  beside the fetch. Most types are this; don't move them.
- **A contract** — a type that's a shared agreement consumed **across layers** (presentation
  *and* data) — earns its own file at the **feature root**, since it belongs to no single
  layer and both sides import it.
- **A model** — a domain entity, internal or external (a DB row, an external API's shape) —
  earns its own file in the **data layer** (`data/`), where it enters the system; the
  presentation imports it from there.

## Rules of thumb (Next-specific)

- **`page.tsx`/`route.ts` are entry points, not homes.** If one grows past wiring +
  render/respond, the excess belongs in the feature folder.
- **Co-locate route-only pieces sparingly.** A bit of route-segment-specific UI can sit
  beside its `page.tsx`, but anything reusable or logic-bearing moves to the feature folder.
- **`app/` mirrors URLs; feature folders mirror the domain.** They won't be a 1:1 mapping,
  and that's fine — multiple routes can delegate into one feature, and one route can
  compose several.
