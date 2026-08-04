---
description: Applying a completed change spec into the durable specs and archive the change.
user-invocable: true
---

# Applying a change spec

A change spec describes *how the system got somewhere*. A spec describes *what the system is*. Applying is the translation between those two registers — and the translation is most of the work.

## What carries over, what doesn't

**Carry:**
- Functional, non-functional requirements;
- Requirements related unresolved open questions;
- Additional docs that describe details of that requirement;
- Architectural decisions;

**Don't carry (goes to archive):**
- Out of scope items;
- Design, models, api and components implementation notes;

## How to apply specifications
- For changes that introduce a new feature - create new feature spec;
- If applying change spec complements, fixes or updates existing feature - merge into existing feature spec;

## How to apply ADRs
- Move each ADR from the change's `adrs/` folder to `/docs/adrs/`, keeping its filename;
- Carry the content across as written - an ADR records what was decided at the time, so don't rewrite it to match how things turned out;
- A filename that already exists in `/docs/adrs/` means the decision was reversed: the incoming ADR supersedes it and overwrites the file. Before overwriting, check it absorbs the decision it replaces (see `specs-architectural-decisions`) - if it doesn't, the reasoning is about to be lost, so stop and confirm with the user;

## How to archive change specs
- Make sure change spec has already been implemented (status reqs front-matter `status`), confirm otherwise;
- Use `mv` commands to move files to dedicated archive directory - avoid Create, and delete operations;
- Don't touch or modify change spec docs content;

## Related skills
- `specs-organization` - load in order to learn how to organize spec directories
