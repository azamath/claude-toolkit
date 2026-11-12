---
description: Perform code review using my tools
argument-hint: what to review
---

Review target: $ARGUMENTS. If empty, review the recent changes.

Use the engineering:code-reviewer agent to review the target.

In parallel, run a default agent in the background that reviews the target using the ponytail:ponytail-review skill.
