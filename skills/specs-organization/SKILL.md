---
description: Convention for organizing project specification documents under /docs, splitting in-progress changes from settled feature specs.
disable-model-invocation: true
user-invocable: true
---

Specification documents live under `/docs` in two forms: in-progress changes and settled feature specs.

## Changes — work in progress

Location: `/docs/changes/<NNN>-<slug>/`

Each change is a folder, numbered incrementally with three digits (`001-add-auth`, `002-rework-billing`). The folder holds whatever documents the change needs. Common files:

- `reqs.md` — what is required
- `design.md` — how to build it
- `adrs.md` — architecture decisions

Other files are fine when the change calls for them (`api.md`, `schema.md`, etc.). The naming convention is a default, not a rule.

## Specs — settled state

Location: `/docs/specs/<feature-name>/`

Organized by feature, not by change. This is the durable record of what the system is.

## Lifecycle

A change folder exists while the work is in progress. Once the work lands, its content belongs in `/docs/specs/<feature-name>/` — the change folder itself moves to `/docs/changes/.archive/<NNN>-<slug>/` as historical record.

The archive preserves history without cluttering the active changes list. `/docs/specs/` remains the single source of truth for the system's current state.
