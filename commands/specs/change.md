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

3. Gather requirements. **Load the `specs-gathering-requirements` skill** and follow it: interview the user one topic at a time and write the requirements doc into the change folder.
