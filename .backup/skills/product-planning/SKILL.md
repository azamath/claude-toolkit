---
name: product-planning
description: Interactive guide for documenting product level information. Use when creating product docs, defining/discussing product requirements, features, tech-stack, planning implementation roadmap or establishing system-wide architecture.
allowed-tools: Read, Write, Edit, Glob, Bash
---

## Files

Location for storing product level information: `<root>docs/product.md`

## `product.md` structure

```markdown
## Overview

**Name:** [PRODUCT NAME]
**Description:** [1-3 SENTENCES THAT DESCRIBE THE PRODUCT]

## Features
- **[FEATURE 1]**: [DESCRIPTION 1]
- **[FEATURE 2]**: [DESCRIPTION 2]

## Technical Stack
[HIGH-LEVEL OVERVIEW OF THE TECHNICAL STACK]

## Roadmap
- [ ] [FIRST FEATURE TO IMPLEMENT]
- [ ] [SECOND FEATURE TO IMPLEMENT]

```

## Rules
- **Focus** - limit your suggestions to the scope of the `product.md` document, never create or suggest addition sections beyond the structure
- **Keep it minimal** - don't write comprehensive descriptions, the purpose is to have general information for using in other specific tasks contexts