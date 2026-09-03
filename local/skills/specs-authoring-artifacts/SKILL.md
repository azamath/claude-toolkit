---
name: specs-authoring-artifacts
description: Authoring specification artifacts — its purpose, content, structure, and principles to follow. Use when creating, drafting, or revising.
---

## Specification artifact types

- Functional Requirements Specs
- Data Specs

## Principles

No artifact holds technical implementation.

## Functional Requirements Specs

Describes the system's behaviour. It is the source used to validate the system.

**Contains:** requirements — each a named behaviour with a description, and optionally the invariants that hold and the scenarios that exercise it.

**Structure:**

````
# <feature> - Functional Requirements

## `FR` <requirement name>
<detailed description of what system should do>

**Rules**
- <invariant that always holds>

### `Scenario` <scenario name>
<concrete trigger and its outcome>

## References
- <link to another spec artifact>
````

A requirement is a name, a description, and optionally rules and scenarios. Both are optional and may appear together — a requirement the description covers on its own needs neither.

**The name** is a noun phrase naming the behavior, kept short enough to scan — *Order confirmation email*, *Session expiry*, *Bulk export*, *Duplicate detection*. It names the requirement; the description states it.

**Rules** are invariants: they hold at all times, with no trigger. Each is one line, so they are a list, not headings — *an order total is never negative*, *an archived record is never returned by search*, *a session token is valid for exactly one device*.

**Scenarios** are a trigger and its outcome, in free prose under a named heading — *Payment declined*, *Import interrupted mid-file*, *Two editors save the same record*. The heading names the situation; the prose says what happens.

**Document-level sections** come after all requirements, at the end of the document. They carry no label — the label is what marks a heading as a requirement. **References** links to other spec artifacts.

## Data Specs

The fixed sets of terms, values, and states the system works with, each spelled out in its own document.

**Contains:** one such set per document —

- **taxonomies and controlled vocabularies** — a closed set of named things the system recognizes, and the meaning of each
- **derivation tables** — a defined quantity and where its value comes from
- **state transition tables** — the states a thing can be in, which transitions are permitted, and what triggers each
- **field and attribute definitions** — the properties something carries, what each means, and which values are valid
- **decision tables and rule matrices** — an outcome that depends on a combination of conditions
- **formats and identifier schemes** — the shape a value must take, when that shape is externally fixed
- **message and copy catalogs** — externally-decided text the system presents, where the exact wording is specified
- **thresholds and limits** — externally-set numeric boundaries, and what happens at each

The list grows as new cases are encountered. An entry belongs here when it is binding specification decided outside the code *and* its natural form is a set, mapping, or table rather than a statement about behaviour. Content that only meets the second half is implementation.

**Structure:**

````
# <feature> - <noun>

<what the document holds, and who decides it>

<the content, in the form its nature takes>

## References
- <link to another spec artifact>
````

A document holds exactly one thing, and its title names that thing. The title and the opening line are fixed; the body takes whatever form the content's nature takes. References is optional. Data specs carry no inline labels: a document holds one thing, so there is nothing to distinguish its headings from.

## Choosing between them

The two types sit at the same level: a feature may hold both, or data specs alone. Content reaches a data spec by the nature of the information, not by its size. Where a requirement depends on a data spec, it links that document explicitly.

## Formatting

**Titles.** Every document is titled `# <feature> - <noun>`, where the noun names what the document holds.

**Prefer lists.** A list is the default form. Reach for a table only when the content is genuinely a grid — when each item carries the same several attributes and they need to be read across as well as down. Content that fits a list should never be forced into one.

**Labels.** Where a document holds headings of more than one kind, each carries an inline-code label naming its kind.
