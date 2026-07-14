---
description: Judge whether a decision warrants an ADR. Use when a choice gets settled during design or implementation — a technology picked, a boundary drawn, an obvious approach deliberately rejected, an alternative turned down — to decide whether it's worth recording or should just be left in the code.
user-invocable: true
---

## When to offer an ADR

All three of these must be true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will look at the code and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If a decision is easy to reverse, skip it — you'll just reverse it. If it's not surprising, nobody will wonder why. If there was no real alternative, there's nothing to record beyond "we did the obvious thing."

### What qualifies

- **Architectural shape.** "We're using a monorepo." "The write model is event-sourced, the read model is projected into Postgres."
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library — just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use AWS because of compliance requirements." "Response times must be under 200ms because of the partner API contract."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it — otherwise someone will suggest GraphQL again in six months.

## How to document an ADR

One document per decision.

```markdown
# <The decision, as a statement>

## Context
<!-- The forces in play: the constraint, the pressure, the thing that made this a real
     question. What a reader needs to know before the decision makes sense. -->
<the forces>

## Decision
<!-- What was chosen, in the active voice. "We store money as integer cents,"
     not "it was decided that..." -->
<what was chosen>

## Consequences
<!-- What this buys and what it costs. The costs are the point — an ADR with only
     upsides is advertising, not a record. -->
<what it buys and what it costs>

## Alternatives
<!-- What else was on the table and why it lost. Only when the rejection is
     non-obvious; drop the section otherwise. -->
<what lost, and why>
```

### Writing it

- **Write for a stranger.** The reader is someone staring at the code years from now, asking "why on earth is it like this?" Nothing outside this entry is loaded in their head: no ticket, no thread, no memory of the discussion. If a sentence only parses for someone who was in the room, rewrite it.
- **Record the why, not the what.** The code already shows what was chosen. The ADR exists for the reasoning, which is the part the code cannot hold.
- **Be concrete about the forces.** "For performance" is not a reason. "The partner API contract caps us at 200ms and the join was costing 400ms" is a reason — and it stays checkable later, when someone wonders whether the constraint still binds.
- **State the cost honestly.** The next engineer needs to know what pain was accepted on purpose, so they can tell a deliberate trade-off from a bug.
- **Keep it short.** A few paragraphs. If it's growing into an essay, the design detail belongs elsewhere and the ADR should link to it.

### Reversing an earlier decision

When the decision overturns one already recorded, it is not a new ADR — it replaces the old one, and reuses its slug. Write it to absorb what it replaces: the Context says what was decided before and what changed to make it wrong, and the Alternatives carry the old decision as an option now rejected.

The register holds one answer per question, so the replaced document does not survive. Anything worth keeping from it must be argued into the new one.
