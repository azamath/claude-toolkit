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

**Don't carry (goes to archive):**
- Out of scope items;
- Acceptance/done criteria;
- Design, models, api and components implementation notes;
- Architectural decisions;

## How to apply specifications
- For changes that introduce a new feature - create new feature spec;
- If applying change spec complements, fixes or updates existing feature - merge into existing feature spec;

## How to archive change specs
- Make sure change spec has already been implemented (status reqs front-matter `status`), confirm otherwise;
- Use `mv` commands to move files to dedicated archive directory - avoid Create, and delete operations;
- Don't touch or modify change spec docs content;

## Related skills
- `specs-organization` - load in order to learn how to organize spec directories