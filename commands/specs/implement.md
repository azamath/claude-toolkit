---
description: "Work on implementation based on specification"
argument-hint: "Specification number or description"
---

**Task:** Work on implementation based on specification provided by user.  

**User prompt:** $ARGUMENTS

**Workflow:**
- Call skill `specification-management` to find requested specs docs and status
- Read `requirements.md` and `design.md` to understand spec scope
- If `plan.md` exists and is not skipped, read it for phased implementation strategy
- Load documents and sources mentioned in the spec docs
- If plan exists: suggest further actions according to the specification plan phases
- If plan is skipped: implement directly based on requirements and design as a single-pass task

**Principles:**
- When plan exists: execute one phase at a time, update plan.md checkboxes for done tasks
- When plan is skipped: implement the full feature, then validate
- Switch to Plan mode before start
- In the final plan, include a "Pre-implementation" section at the top that instructs to read the full spec files (with absolute paths to requirements.md, design.md, and plan.md if exists) before starting any implementation work
- Use TodoWrite to break down large tasks
- Validate the implementation before moving to the next phase
- Wait for user confirmation where manual testing is required
