---
description: Convention for organizing project specification documents.
---

## Specifications Organization

- **Live Specs** - live specifications are durable documents that describe current state and functionality of the system; used as an author source to validate the implementation.
- **ADRs** - architectural decisions records. A flat register, not organized by feature: an architectural decision is about the system, and tells why it is shaped that way, and often cuts across several features or belongs to none.
- **Change Specs** - specifications for a change describe the intended change to the system and "delta"s of the live specifications that should be implemented and applied.  
  Consists of:
  - **Proposal** - brief description about the intent, why this change is made and its scope; used to keep necessary background information which can't be found in specifications.
  - **Delta Specs** - set of artifacts that represent proposed modifications in format as live specs but with marks what is added, modified or removed; eventually merged into live specs after implementation. 
  - Other kind of docs depending on the workflow and project specifics (e.g. ADRs)
- **Archived Change Specs** - applied change specs go to archive to preserve historical lineage; The archive preserves history without cluttering the active changes list.

## Specifications Storage

Specifications can be kept different way depending on the project or team.

### Storage: Filesystem

Mapping:

- Live specs: `/docs/specs/<feature-name>-<kind>.md`;
- ADRs (applied): `/docs/adrs/<decision>.md` - one document per decision;
- Change specs: `/docs/changes/<NNN>-<description-slug>/`.  
  Each change is a folder, numbered incrementally with three digits (`001-add-auth`, `002-rework-billing`). The folder holds whatever documents the change needs:
  - Proposal: `proposal.md`
  - Delta Specs: `specs/<feature-name>-<kind>.md` — specification artifacts that will be merged into durable specs (by feature);
  - ADRs: `adrs/<decision>.md` — architecture decisions, one document per decision (`event-driven-billing.md`); Named by slug, not numbered — a number assigned inside a change would collide with a concurrent change's on the way in. The slug is fixed when the ADR is written, so it survives the move and any reference to it keeps working. Git holds the chronology;
- Archived Change Specs: `/docs/changes/.archive/<NNN>-<description-slug>/`

Applying:
- change spec fragments merge into `/docs/specs/<feature-name>-<kind>.md`;
- change ADRs move to `/docs/adrs/`;
- the change folder itself moves to `/docs/changes/.archive/<NNN>-<description-slug>/`;

### Storage: Notion (https://notion.com)

<!-- TODO -->
