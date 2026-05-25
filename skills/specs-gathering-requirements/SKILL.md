---
description: Gathering requirements for a change-spec — how to interview the user and write the requirements doc (functional, non-functional, acceptance criteria, scope).
user-invocable: true
---

# Gathering requirements

The requirements step answers *what must be true* for a change, before anyone decides *how* to build it.

## What is a requirement

A requirement states a need or a constraint in terms the user cares about — observable behavior, an outcome, a quality the system must hold to. It is true or false independent of how the code is written. Two kinds:

- **Functional** — something the system must *do*: a capability, a behavior, a rule it enforces, a response to an input or event.
- **Non-functional** — a quality or constraint the system must *hold to*: performance, security, accessibility, scale, compatibility, regulatory limits.

A good requirement is **declarative** (states what, not how), **verifiable** (you can point at the system and say yes/no), **atomic** (one need per statement), and **solution-free** (survives a change of implementation).

> The system must let a user reset their password without contacting support.
> A search query must return results within 500 ms at the 95th percentile.
> Only the account owner may delete an account.

## What is *not* a requirement

Keep this register strict. The following describe *how*, or belong to other steps — route them elsewhere rather than into the requirements doc:

- **Implementation & design** — mechanisms, libraries, frameworks, data models, schemas, API shapes, algorithms. *("Store sessions in Redis", "use JWT", "add a `users` table.")* → design.
- **Architecture decisions** — the choice between options and its rationale. → ADRs.
- **Tasks & plans** — steps, sequencing, who does what, estimates. → task tracking.
- **Solutions disguised as needs** — "Add a dropdown" is a UI solution; the requirement is "the user must be able to pick one of N options." Ask *why* until you reach the need.
- **Vague aspirations** — "fast", "secure", "user-friendly" with nothing measurable. Push these to a verifiable form or drop them.

When a statement describes a mechanism, ask "would this still be true if we built it a completely different way?" If no, it's design, not a requirement.

## How to interview

Work **one topic at a time**. Ask a focused round of questions, write down what you learned, then move to the next topic. Do not dump every question at once — requirements surface in layers, and each answer reshapes the next question.

Use the **AskUserQuestion tool** for each round. Provide concrete options when you can infer plausible ones; leave questions open when you genuinely don't know the space. After each round, reflect the answers back into the draft so the user sees the spec take shape.

Suggested progression of topics (adapt to the change):

1. **Problem & goal** — what's broken or missing, and what does success look like? Who is affected?
2. **Functional behavior** — what must the system *do*? Walk the main flows and the important edge cases.
3. **Non-functional needs** — performance, security, accessibility, scale, compatibility constraints. Skip categories that plainly don't apply rather than padding the doc.
4. **Boundaries** — what is explicitly *out of scope*? What's deferred to a later change?
5. **Acceptance** — how will we know each requirement is met?

Stop when the picture is coherent and the open questions are written down, not when every detail is resolved. Unknowns are allowed — record them as open questions rather than guessing.

## Writing the requirements doc

When you create the requirements document, load `reqs-template.md` from this skill's directory and follow its structure. The template carries the section layout and the front-matter `status` field that tracks lifecycle (new requirements start as `draft`; the apply/archive workflow keys off this).

In the template, `<!-- ... -->` comments are guidance, not content — delete them in the final doc. Replace every `<angle-bracket>` placeholder with real content, and drop any section or category that doesn't apply.

Use plain headings and bullets — no requirement ID scheme. Express acceptance criteria as a checklist of done-criteria. Keep every statement declarative and verifiable.

## Lifecycle note

When this change is later applied to the durable feature specs, the registers split (see `specs-applying-change`): functional and non-functional requirements and any unresolved requirement-related open questions **carry over** into the feature spec, while acceptance criteria and out-of-scope items stay with the archived change. Write the requirements so that separation is clean — keep durable needs distinct from this-change-only bookkeeping.

## Related skills
- `specs-organization` — where change folders and feature specs live, and the naming convention
- `specs-applying-change` — what happens to these requirements when the change lands
