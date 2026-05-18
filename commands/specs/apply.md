---
description: "Workflow for applying change-spec"
argument-hint: "a change-spec number or description"
---

**Task:** Apply a change-spec to final feature specs and archive it.

**User prompt:** $ARGUMENTS

**Required skills:**
- `specs-organization`
- `specs-applying-change`

**Workflow:**
1. Identify which change-spec to apply:
   - if user didn't specify which change-spec to apply - find current implemented change-specs and list candidates to confirm with user;
   - if specified change spec is not marked as implemented - ask user using AskUserQuestion options to check the implementation in code or mark as completed right away;
2. Make a plan using TaskCreate, and start applying and archiving process.
3. Report user with a summary list: what was applied, which existing features were updated and which were created.
4. Suggest commiting the work.
