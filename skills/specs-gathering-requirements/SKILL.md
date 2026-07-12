---
description: The process of gathering requirements for a change-spec — sourcing them, interviewing the user, and producing the requirements doc.
user-invocable: true
---

# Gathering requirements

The requirements step answers *what must be true* for a change, before anyone decides *how* to build it. This skill covers the *process* — how to source, interview for, and write up requirements. For the authoring craft itself — what counts as a requirement, what doesn't, and the grammar for writing one — **load the `specs-writing-requirements` skill**; keep it in view throughout, since every statement you draft here follows its rules.

## Before you interview

Two things settle *where requirements come from* before you ask a single question — get them right and the interview stays requirement-first on its own.

**Ground in the existing requirements, not the code.** Read what is *already required* so you don't re-derive settled ground from the user or mistake an existing need for a new one: the durable feature specs, and the requirements of any in-progress changes. These are the requirement register — *what the system already does and what was already resolved* — so they sharpen requirement-first thinking rather than biasing it. (See `specs-organization` for where these live; read only the requirement documents, not design/architecture notes.)

**Take the need from the change, not from the implementation.** The requirements come from *what must be true after this change* — the desired behavior and the user's goal — never from how the system is built today. Do not read the code to source questions: it is the starting point you are moving *away from*, and letting it drive you anchors the change to the status quo, biases it toward small diffs, and dresses design details up as requirements ("the code caches X — should it still?"). Reconciling requirements against the existing implementation is a separate concern, not part of gathering them.

Apply to a candidate *question* the same test `specs-writing-requirements` applies to a *statement*: "would this still matter if the system were rebuilt a completely different way?" If no, it's design — keep it out of the interview.

## How to interview

Work **one topic at a time**. Ask a focused round of questions, write down what you learned, then move to the next topic. Do not dump every question at once — requirements surface in layers, and each answer reshapes the next question.

Use the **AskUserQuestion tool** for each round. Provide concrete options when you can infer plausible ones; leave questions open when you genuinely don't know the space. After each round, reflect the answers back into the draft so the user sees the spec take shape.

Suggested progression of topics (adapt to the change):

1. **Problem & goal** — what's broken or missing, and what does success look like? Who is affected?
2. **Functional behavior** — what must the system *do*? Walk the main flows and the important edge cases.
3. **Non-functional needs** — performance, security, accessibility, scale, compatibility constraints. Ask only about categories that plausibly apply.
4. **Boundaries** — what is explicitly *out of scope*? What's deferred to a later change?
5. **Acceptance** — how will we know each requirement is met?

Stop when the picture is coherent and the open questions are written down, not when every detail is resolved. Unknowns are allowed — record them as open questions rather than guessing.

## Filling the template

When you create the requirements document, start from the `templates/reqs.md` template in the `specs-organization` skill and follow its structure. The template carries the section layout and the front-matter `status` field that tracks lifecycle (new requirements start as `draft`; the apply/archive workflow keys off this).

Its `<!-- ... -->` comments are guidance, not content — delete them in the final doc. Replace every `<angle-bracket>` placeholder with real content, and drop any section or category that doesn't apply.

Write every requirement in the grammar from `specs-writing-requirements` — including its **Keeping the set lean** rules. Express acceptance criteria as a checklist of done-criteria.

## Lifecycle note

When this change is later applied to the durable feature specs, the registers split (see `specs-applying-change`): functional and non-functional requirements and any unresolved requirement-related open questions **carry over** into the feature spec, while acceptance criteria and out-of-scope items stay with the archived change. Write the requirements so that separation is clean — keep durable needs distinct from this-change-only bookkeeping.

## Related skills
- `specs-writing-requirements` — the authoring craft: what a requirement is, what it isn't, and the grammar for writing one
- `specs-organization` — where change folders and feature specs live, and the naming convention
- `specs-applying-change` — what happens to these requirements when the change lands
