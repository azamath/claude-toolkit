---
description: Convention for organizing project specification documents under /docs, splitting in-progress changes from settled feature specs.
user-invocable: true
---

Specification documents live under `/docs`: in-progress change-specs, final feature specs, and the architectural decisions behind them.

## Change-specs — work in progress

Location: `/docs/changes/<NNN>-<description-slug>/`

Each change is a folder, numbered incrementally with three digits (`001-add-auth`, `002-rework-billing`). The folder holds whatever documents the change needs. Common files:

- `proposal.md` — why, and what changes. Carries the front-matter `status` field that tracks the change's lifecycle (a new change starts as `draft`; the apply/archive workflow keys off this)
- `specs/<feature-name>/*.md` — specification artifacts that will be converted to durable artifacts (by feature)
- `adrs/<decision>.md` — architecture decisions, one document per decision (`event-driven-billing.md`)

## Feature-specs — applied state

Location: `/docs/specs/<feature-name>/*.md`

Organized by feature, not by change. This is the durable record of what the system is.

## ADRs — applied state

Location: `/docs/adrs/<slug>.md`

One document per decision. A flat register, not organized by feature: an architectural decision is about the system, and often cuts across several features or belongs to none.

Named by slug, not numbered — a number assigned inside a change would collide with a concurrent change's on the way in. The slug is fixed when the ADR is written, so it survives the move and any reference to it keeps working. Git holds the chronology.

## Lifecycle

A change folder exists while the work is in progress. Once the work lands:

- its spec fragments merge into `/docs/specs/<feature-name>/*.md`;
- its ADRs move to `/docs/adrs/`;
- the change folder itself moves to `/docs/changes/.archive/<NNN>-<description-slug>/` as historical record.

The archive preserves history without cluttering the active changes list. `/docs/specs/` and `/docs/adrs/` remain the source of truth for the system's current state — what it does, and why it is shaped that way.
