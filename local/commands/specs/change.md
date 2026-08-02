---
description: "Workflow for working on a change-spec"
argument-hint: "change description"
---

**Task:** Start new or update a change-spec according to user provided prompt.

**User prompt:** $ARGUMENTS

**Note on skills:** Load each skill only at the step that needs it — not in advance.

**Workflow:**
1. If the change scope is not clear enough, ask what they want.

   Use the **AskUserQuestion tool** (open-ended, no preset options) to ask:
   > "What change do you want to work on? Describe what you want to build or fix."

   **IMPORTANT**: Do NOT proceed without understanding what the user wants to build.

2. Decide whether to create a new change-spec or to update an existing one. First **load the `specs-organization` skill** to learn how change folders are laid out, then:
   - user may explicitly indicate if it is a separate change;
   - a change scope may be an addition or fix to a current change, check the list and make a decision.

3. Gather requirements — grounded in the existing specs, **not** the implementation. **Load the `specs-gathering-requirements` skill** and follow it to produce the requirements doc in the change folder.

4. Settle the architectural decisions, before the design. **Load the `specs-architectural-decisions` skill** and write an ADR for each choice that meets its bar. Most changes will have none.

5. Design how to build it, within the decisions from step 4. Produce `design.md` in the change folder.
