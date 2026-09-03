---
description: The process of gathering the scope of a change-spec — sourcing it, interviewing the user, and producing the proposal and spec fragments.
user-invocable: true
---

# Gathering scope

The scope step answers *what must be true* for a change, before anyone decides *how* to build it. This skill covers the *process* — how to source, interview for, and write up what the change needs.

## Before you interview

Two things settle *where the scope comes from* before you ask a single question — get them right and the interview stays behavior-first on its own.

**Ground in the existing specs, not the code.** Read what the system is *already specified* to do so you don't re-derive settled ground from the user or mistake an existing behavior for a new one: the durable feature specs, and the spec fragments of any in-progress changes. These are the register of *what the system already does and what was already resolved* — so they sharpen behavior-first thinking rather than biasing it. (See `specs-organization` for where these live; read only the specs, not design/architecture notes.)

**Take the need from the change, not from the implementation.** The scope comes from *what must be true after this change* — the desired behavior and the user's goal — never from how the system is built today. Do not read the code to source questions: it is the starting point you are moving *away from*, and letting it drive you anchors the change to the status quo, biases it toward small diffs, and dresses design details up as needs ("the code caches X — should it still?"). Reconciling the scope against the existing implementation is a separate concern, not part of gathering it.

## How to interview

Work **one topic at a time**. Ask a focused round of questions, write down what you learned, then move to the next topic. Do not dump every question at once — needs surface in layers, and each answer reshapes the next question.

Use the **AskUserQuestion tool** for each round. Provide concrete options when you can infer plausible ones; leave questions open when you genuinely don't know the space. After each round, reflect the answers back into the draft so the user sees the scope take shape.

Suggested progression of topics (adapt to the change):

1. **Problem & goal** — what's broken or missing, and what does success look like? Who is affected?
2. **Functional behavior** — what must the system *do*? Walk the main flows and the important edge cases.
3. **Non-functional needs** — performance, security, accessibility, scale, compatibility constraints. Ask only about categories that plausibly apply.
4. **Boundaries** — what is explicitly *out of scope*? What's deferred to a later change?

Stop when the picture is coherent and the open questions are written down, not when every detail is resolved. Unknowns are allowed — record them as open questions rather than guessing.

## What to produce

The interview lands in two places in the change folder (see `specs-organization`):

- **`proposal.md`** — why the change exists, what changes, what is out of scope, and the open questions.
- **`specs/<feature-name>/*.md`** — the behavior itself, written as it will read in the durable spec: what the system does once the change lands, by feature. A directory per feature the change touches, mirroring the durable layout — each fragment named for the artifact it will merge into.

The split is the point. The fragment describes the system and survives the change; the proposal explains this particular change and is archived with it. Write the fragment so it needs no knowledge of the proposal to make sense.

## Lifecycle note

When this change is applied, the fragments merge into the durable feature specs and the proposal is archived with the change folder (see `specs-applying-change`). Write each fragment as durable system behavior, and keep this-change-only bookkeeping — rationale, out-of-scope items, deferrals — in the proposal.

## Related skills
- `specs-organization` — where change folders and feature specs live, and the naming convention
- `specs-applying-change` — what happens to the proposal and fragments when the change lands
