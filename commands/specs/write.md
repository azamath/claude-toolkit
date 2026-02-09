---
description: "Specify and write a requirement, design or implementation plan"
argument-hint: "Describe your feature or requirement to specify"
---

**Task:** Describe a requirement, solution design or plan and write to specification documents depending on user prompt  

**User prompt:** $ARGUMENTS

**Workflow:**
- Call skill `specification-management` for specs orchestration
- Find and read `docs/product.md` to understand product context
- Depending on user request call corresponding skill
