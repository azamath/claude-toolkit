# Working notes — product-requirements skill

Temporary. Delete when the skill is finished.

## Frame (settled)

- **Audience:** humans. A PRD aligns a team on what is being built and why. Not an input to a coding agent.
- **Content:** structure only. No process, no interview steps, no file-storage or naming conventions.
- **Stance:** strongly opinionated about what a PRD must not contain.
- **Scale:** scale-adaptive — same structure, sections expand or collapse from small feature to whole product.
- **Clean sheet:** no links to change-specs, ADRs, requirements-gathering, or specs-organization. Never reference them.

## Discussion order

1. Intro — what a PRD is, when it applies, how it scales ← current
2. Requirements
3. Goals vs. Success metrics (merge?)
4. Problem, Non-goals
5. Users & use cases (keep / fold / cut — depends on Requirements)
6. Summary, Constraints, Open questions
7. Bans and writing rules

## Decisions

### Intro

- Status: **settled, written.**
- Definition: problem / who has it / what must be true — enough to agree it's the right
  thing and later tell whether it was done. "Must be true" is load-bearing; it sets up
  the Requirements section's form.
- Core discipline: "describes what must become true for users, not how the system will
  make it true." Every later ban is a corollary, stated once instead of nine times.
  - Rejected: "the change in the world, not the change in the codebase" — same thinking,
    but too cute. Keep the plain phrasing.
- Folded in the sharpest of the what-a-PRD-is-not list: "not a design doc." Dropped the
  rest (not a spec / not a project plan) as redundant with the core discipline.
- Scale rule: **omit, never pad.** A section with nothing real to say is deleted.
  Makes "scale-adaptive" enforceable rather than vague.
- Cut: the "when does a PRD apply / when is it not worth writing" part. Judgment Claude
  exercises anyway; not worth the context budget.

## To fix before finishing

- Frontmatter `description` still says "and the process of writing one" — contradicts the
  structure-only decision. Reword once the sections are final.

### The contents (section list)

- Status: **settled, written.** Eight items as a single "The contents" section, formatted
  as a title–description list.
- Framed as what a PRD *covers*, not headings to reproduce. Authors may merge, rename, or
  drop. Order is a default: context before commitments.
  - Rejected: replacing the list with "questions the PRD answers" and no structure at all
    — too radical a change. The named list stays.
- **Goals & success metrics merged.** Kept apart, goals drift into aspiration and metrics
  drift into whatever is already instrumented, and nobody notices because they sit on
  different pages. Paired, an unmeasurable goal is visibly unmeasurable and an orphan
  metric is visibly orphaned. A goal with no measure yet is written as such.
- **Users & use cases kept**, narrowly scoped to who hits the problem and in what
  situation. The situational half constrains requirements and is lost when folded into
  Problem. Persona theater is handled by a ban later, not by cutting the section.
- Goals-vs-Requirements boundary resolved by the merge: goals are the change in the world,
  requirements are what must be true of the product for it. Restate in Requirements.
- Order changes from the first draft: Users moved up next to Problem (framing pair);
  metrics folded into Goals.

### Writing-rules audit of "The contents"

Checked against the project writing rules. It violated them; fixed.

- Cut three invented rationales (rule: never supply a reason that wasn't given) —
  "for someone who reads nothing else", "so nobody assumes it is included",
  "context before commitments". All were mine from the discussion, never stated by the
  user.
- Cut the "not headings — merge, rename, or drop" framing (rule: write only what was
  settled). Discussed but never confirmed. **Still unsettled** — decide whether the skill
  says anything about authors deviating from the list.
- De-duplicated Constraints: "and what this relies on" just restated "dependencies".
- Intro line reduced to naming what follows: "What a PRD covers."
- Kept: "the evidence that it is real" and the goal–metric pairing — both settled content.

**Standing correction for the rest of the skill:** write the decision, not the argument
for it. Rationale belongs in these notes.

### Outstanding

- The Scale section contains the same defect: "A three-section PRD that is entirely true
  beats a nine-section PRD padded to look complete" is an argument for the rule, not the
  rule. User confirmed the rule, not the justification. Flagged, not yet cut.
- Unsettled: whether the skill says anything about merging/renaming/dropping list items.

### Three-tier reorganization

- Proposed split: **Context** (Summary, Problem, Users & use cases), **Core** (Goals &
  success metrics, Requirements), **Additional** (Non-goals, Constraints & dependencies,
  Open questions).
- **Non-goals moved to Additional — confirmed by user.** It qualifies the core rather than
  being part of it. Noted at the time: this is the section most likely to be skipped once
  filed as additional.
- Status: the tier grouping itself is **not yet written into SKILL.md** — the list there is
  still flat. Decide whether the tiers become headings, or stay as ordering only.

### User stories

- Not a separate list item. Stories are a **format**, not a content kind — they carry
  actor, need, and purpose, which is information only when those vary. When they don't,
  the format produces tautologies.
- Resolution: name user stories among the forms a requirement may take, inside the
  Requirements item. No separate section.
  - Rejected: an optional "User stories" item in the core. More discoverable, but an
    optional slot gets filled, and tautological stories are what fill it.
- **Unsettled:** whether the skill states when the story format fits vs. when it is
  redundant. Deliberately left out of the Requirements description (user asked for content
  and forms only, no rules). Candidate for the bans section.
- **Unsettled:** whether Users & use cases also mentions the story format. Next topic.

### Requirements

- Status: **description settled, written.**
- Content kinds: functional requirements, quality attributes, behavioral rules.
- Forms: user stories, plain statements, acceptance criteria, rules.
- No rules on choosing between them — user asked for content and formats only.
- Parenthetical glosses cut at user's request; minimum info only.
- Left out: data requirements and scale constraints. They blur into Constraints &
  dependencies. If they move here later, Constraints narrows to external dependencies.

## Open cross-section tensions

- Goals vs. Success metrics: merge or keep apart. Decide in step 2.
- Users & use cases: risk of persona theater. Decide after Requirements.

## External resources
- https://carlinyuen.medium.com/writing-prds-and-product-requirements-2effdb9c6def
