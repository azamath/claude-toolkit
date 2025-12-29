---
description: "Work on implementation based on specification"
argument-hint: "Specification number or description"
---

**Task:** Work on implementation based on specification provided by user.  

**User prompt:** $ARGUMENTS

**Workflow:**
- Call skill `specification-management` to find requested specs docs and status
- Read all `requirements.md`, `design.md`, `plan.md` to understand spec scope
- Load documents and sources mentioned in the spec docs
- Depending on user request suggest further actions according to the specification plan

**Principles:**
- Execute one phase at a time
- Use TodoWrite to break down task large tasks
- Validate the implementation before moving to the next phase
- Wait for user confirmation where manual testing is required
- Update plan.md checkboxes for done tasks
