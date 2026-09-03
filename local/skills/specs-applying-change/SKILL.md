---
description: Applying a completed change spec into the durable specs and archive the change.
user-invocable: true
---

# Applying a change spec

A change spec describes *how the system got somewhere*. A spec describes *what the system is*. The change already carries its behavior as spec fragments under `specs/`, written in the durable register - so applying is a merge, not a translation.

## What carries over, what doesn't

**Carry:**
- The spec fragments under `specs/`;
- Unresolved open questions about behavior;
- Additional docs that describe details of that behavior;
- Architectural decisions;

**Don't carry (goes to archive):**
- The proposal itself - rationale, what changed, out of scope items;
- Design, models, api and components implementation notes;

## How to apply spec fragments
- Each fragment under `specs/<feature-name>/<artifact>.md` targets `/docs/specs/<feature-name>/<artifact>.md`;
- No such artifact exists - the fragment becomes it;
- It already exists - merge the fragment in, section by section. The fragment is the newer description of the same system: where the two disagree, the fragment wins;
- Merging is not appending. A fragment that restates an existing behavior replaces it; one that adds behavior slots in beside it. The result reads as one description of the feature, with no trace of which change contributed what;

## How to apply ADRs
- Move each ADR from the change's `adrs/` folder to `/docs/adrs/`, keeping its filename;
- Carry the content across as written - an ADR records what was decided at the time, so don't rewrite it to match how things turned out;
- A filename that already exists in `/docs/adrs/` means the decision was reversed: the incoming ADR supersedes it and overwrites the file. Before overwriting, check it absorbs the decision it replaces (see `specs-architectural-decisions`) - if it doesn't, the reasoning is about to be lost, so stop and confirm with the user;

## How to archive change specs
- Make sure change spec has already been implemented (the `status` front-matter field in `proposal.md`), confirm otherwise;
- Use `mv` commands to move files to dedicated archive directory - avoid Create, and delete operations;
- Don't touch or modify change spec docs content;

## Related skills
- `specs-organization` - load in order to learn how to organize spec directories
