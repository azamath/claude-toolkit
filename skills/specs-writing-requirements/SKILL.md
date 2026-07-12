---
description: The craft of writing a good requirement — what counts as a requirement versus a design detail, and the grammar for functional and non-functional requirements. Use when authoring, reviewing, or critiquing requirement statements.
user-invocable: true
---

# Writing requirements

A requirement answers *what must be true* for a change, before anyone decides *how* to build it. This skill is the authoring craft: what counts as a requirement, what doesn't, and the grammar for writing one. It is independent of any particular process for gathering or storing requirements.

## What is a requirement

A requirement states a need or a constraint in terms the user cares about — observable behavior, an outcome, a quality the system must hold to. It is true or false independent of how the code is written. Two kinds:

- **Functional** — something the system must *do*: a capability, a behavior, a rule it enforces, a response to an input or event.
- **Non-functional** — a quality or constraint the system must *hold to*: performance, security, accessibility, scale, compatibility, regulatory limits.

A good requirement is **declarative** (states what, not how), **verifiable** (you can point at the system and say yes/no), **atomic** (one need per statement), and **solution-free** (survives a change of implementation).

## What is *not* a requirement

Keep this register strict. The following describe *how*, or belong to other steps — route them elsewhere rather than into the requirements doc:

- **Implementation & design** — mechanisms, libraries, frameworks, data models, schemas, API shapes, algorithms. *("Store sessions in Redis", "use JWT", "add a `users` table.")* → design.
- **Architecture decisions** — the choice between options and its rationale. → ADRs.
- **Tasks & plans** — steps, sequencing, who does what, estimates. → task tracking.
- **Solutions disguised as needs** — "Add a dropdown" is a UI solution; the requirement is "the user must be able to pick one of N options." Ask *why* until you reach the need.
- **Vague aspirations** — "fast", "secure", "user-friendly" with nothing measurable. Push these to a verifiable form or drop them.

When a statement describes a mechanism, ask "would this still be true if we built it a completely different way?" If no, it's design, not a requirement.

## How to write a requirement

One grammar, applied consistently — this is what keeps the doc scannable and quick to review.

**Functional requirements** are verb-first bullets under the `Functional requirements` heading — that heading *is* the contract ("the system must…"), so no binding line precedes the bullets:

```
## Functional requirements
- Let a user reset their password without contacting support.
- Reject a delete request from anyone but the account owner.
- Keep the cart intact when a payment is declined.
```

Read each as *heading + bullet* ("Functional requirements… let a user reset their password"). The obligation lives in the heading, not on every line — so the eye lands on what differs.

Rules:
- **Start at the verb, imperative mood** — *Let, Reject, Return, Allow, Prevent, Lock*. No "the system must / shall / should / be able to" anywhere — not on the bullet, not as a preamble line; the heading owns it.
- **One requirement, one line** — one actor, one behavior, one testable claim. If an "and" joins two independent behaviors, split them.
- **Sub-bullets only for genuine conditions or exceptions**, never to continue a thought:
  ```
  - Lock the account after 5 failed login attempts.
    - Unlock automatically after 15 minutes, or immediately via email reset.
  ```
- **Default to a flat list; group only across real features.** A change that touches one feature gets a flat bullet list with **no** sub-headings — this is the common case, expected and correct. Add `###` sub-headings *only* when the change genuinely spans two or more distinct major features.
  - A **major feature** is a capability that maps to its own `/docs/specs/<feature-name>/` entry — something that is, or would become, its own feature spec (e.g. `### Authentication`, `### Checkout`).
  - **Flows, phases, and categories are not features.** Do not invent headings like "Validation", "Error handling", "Notifications", or "Edge cases" — those are bullets (or sub-bullets), never feature groups.
  - When you do split, bullets stay verb-first directly under each sub-heading — no binding line. Group by meaning, never by line count, and never split a single feature just because it has many bullets.

**Non-functional requirements** are qualities, not actions, so the imperative heading doesn't fit. Give each its own terse shape — `<aspect>: <measurable bound>`:

```
- Performance: search returns within 500 ms (p95).
- Security: only the account owner can delete an account.
- Accessibility: every flow is operable by keyboard alone.
```

**When the imperative would distort the meaning** — a constraint that isn't a system action, or a rule about an external actor — fall back to a plain declarative line. Prefer the imperative; don't mangle meaning to obey it.

## Keeping the set lean

A requirements list is for fast review, not exhaustive prose:
- **Default to one line per requirement.** Reach for a sub-bullet only when a real condition or exception needs it.
- **Drop non-functional categories that don't apply** — leave them out entirely rather than writing "N/A". An empty section is noise.
- **Merge near-duplicates and cut filler.** Delete any line that restates the context, hedges ("ideally", "if possible"), or describes *how*.

## Related skills
- `specs-organization` — the requirements-doc template (`templates/reqs.md`): its sections and layout
- `specs-gathering-requirements` — the process that produces a requirements doc: sourcing and interviewing
