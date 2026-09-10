---
name: specs-authoring-artifacts
description: Authoring specification artifacts — artifact types, their content, structure, and writing principles to follow. Use when creating, drafting, or revising.
---

## Specification artifact types

- Functional Requirements Specs
- Data Specs

## Authoring Principles

- No artifact holds details of the implementation. The specification serves as source of what is required, and a contract to validate the implementation.
- Content reaches a data spec by the nature of the information, not by its size.
- A spec references another only where it directly relates to or depends on it. References are optional; a spec that stands alone carries none.

## Artifacts Writing and Formatting

These rules applied to every artifact described here and defines how content is laid out on the page, so a reader can find what they need without reading it all.

- **Titles.** Every artifact is titled `<feature> - <artifact type>`, where the noun names what it holds.

- **Every sentence carries content.** Cut restatement, hedging, and preamble.

- **Break content into named parts.** Content is not run together as prose.

- **Prefer lists to tables.** A list is the default form. Reach for a table only when the content is genuinely a grid — when each item carries the same several attributes and they need to be read across as well as down. Content that fits a list should never be forced into one.

## Artifact Type: Functional Requirements Specs

Describes the system's behaviour. It is the source used to validate the system.

### High-level layout

```
# [feature] - Functional Requirements

<!-- requirement block: -->
## Requirement: [requirement name 1]
[detailed description of the requirement 1]

<!-- optional scenarios: -->
### Scenario: [scenario name]
[concrete trigger and its outcome]
<!-- end scenarios: -->
<!-- end requirement block -->

<!-- requirement block: -->
## Requirement: [requirement name 2]
[detailed description of the requirement 2]
<!-- end requirement block -->

## References <!-- optional -->
- [linked title] - [description of what it contains]
```

**Notes:**

- **The requirement name** is a noun phrase naming the behavior, kept short enough to scan — *Order confirmation email*, *Session expiry*, *Bulk export*, *Duplicate detection*. It names the requirement; the description states it. The `Requirement:` prefix marks the heading as opening a requirement block.
- **The requirement description** the actual body of the requirement that states what the system should do - verifiable against the implementation.
- **Scenarios** are optional. They are a trigger and its outcome, in free prose under a named heading — *Payment declined*, *Import interrupted mid-file*, *Two editors save the same record*. The heading names the situation; the prose says what happens. The `Scenario:` prefix marks the heading as opening a scenario block.

## Artifact Type: Data Specs

The fixed sets of terms, values, and states the system works with.

Example kinds:

- **taxonomies and controlled vocabularies** — a closed set of named things the system recognizes, and the meaning of each
- **derivation tables** — a defined quantity and where its value comes from
- **state transition tables** — the states a thing can be in, which transitions are permitted, and what triggers each
- **field and attribute definitions** — the properties something carries, what each means, and which values are valid
- **decision tables and rule matrices** — an outcome that depends on a combination of conditions
- **formats and identifier schemes** — the shape a value must take, when that shape is externally fixed
- **message and copy catalogs** — externally-decided text the system presents, where the exact wording is specified
- **thresholds and limits** — externally-set numeric boundaries, and what happens at each
- other kinds that is specific to a problem domain or area

### High-level layout

```
# [topic] - [artifact type]

[what the document holds]

## [section title] <!-- optional title: if artifact contains more than one kind of information -->
[the content in shape of lists or tables, in the form its nature takes]

## References <!-- optional -->
- [linked title] - [description of what it contains]
```
