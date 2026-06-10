---
status: draft
---

<!-- TEMPLATE — copy this structure into the requirements doc.
     <!- - ... - -> comments are guidance: delete them.
     Replace every <angle-bracket> placeholder with real content. -->


# Requirements: <change name>

## Context
<!-- One short paragraph: the problem and the goal. Why this change exists. -->
<the problem and goal>

## Functional requirements
<!-- The heading is the contract ("the system must…") — no binding line.
     Start each bullet at the verb, imperative mood. One line per requirement —
     one actor, one behavior, one testable claim. Sub-bullets only for genuine
     conditions/exceptions.
     DEFAULT: a flat list with no sub-headings — this is the common case.
     Split into ### sub-headings ONLY when the change spans 2+ major features,
     where a feature maps to its own /docs/specs/<feature-name>/ entry
     (e.g. ### Authentication, ### Checkout). Flows/validation/error-handling are
     NOT features — never invent headings for them. -->
- <verb-first behavior, e.g. "Let a user reset their password without contacting support.">

## Non-functional requirements
<!-- Qualities, not actions. Shape: "<aspect>: <measurable bound>".
     Keep only the categories that apply; delete the rest — no "N/A" lines. -->
- <aspect>: <measurable bound, e.g. "Performance: search returns within 500 ms (p95).">

## Acceptance criteria
<!-- A checklist of done-criteria. Each item is something you could verify
     as true or false. Group by feature, mirroring the functional sub-headings. -->
- [ ] <observable, testable condition>

## Out of scope
<!-- Explicit list of what this change does NOT cover, and what is deferred. -->
- <thing this change does not address>

## Open questions
<!-- Unresolved items to track. Remove each as it gets answered. Delete the section if none. -->
- <unresolved question>
