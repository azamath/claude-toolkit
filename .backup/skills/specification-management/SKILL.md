---
name: specification-management
description: Manages specification workflow infrastructure - creates spec directories, tracks document statuses in README.md, and guides progression through requirements/design/planning phases. Coordinates with specialized skills for content. Use for starting specs, checking status, or workflow guidance.
---

# Specification Management

This guide is for managing project specification documents structure and lifecycle. The purpose is to create and maintain the documentation structure, manage statuses, and orchestrate the workflow across requirements, design, and planning phases.

## When to Activate

- User wants to create new specification directory
- User wants to check specification documents statuses
- User wants full end-to-end specification workflow
- User wants to organize feature specifications

## Main Principles

### Directory Structure

The specification management follows this structure:

```
docs/
├── product.md             # General project information
└── specs/
    └── [number]-[name]/   # 3-digit numbering (001, 002, 003...)
        ├── README.md      # Specfication status and history
        ├── requirements.md
        ├── design.md
        ├── plan.md
        └── diagrams/      # Optional: UI mockups, flows, architecture
```

### Documents Tracked

- **requirements.md** - What to build and why
- **design.md** - How to build it technically
- **plan.md** - Implementation strategy

### Document Statuses

**Tracking** - All statuses are tracked in README.md.

**Document Status Values**: `pending` | `in_progress` | `completed` | `skipped`

**Document Status Flow**:
```
pending → in_progress → completed
                      → skipped (from any state)
```

## Specification Workflow Guidance

**Purpose**: Detect current specification status and suggest logical continuation points.

**Common Workflow**: requirements → design → plan (optional) → implement

### Understanding Current State

1. Check if `docs/specs/[Number]-[Name]/` directory exists
2. Read `README.md` to understand:
   - Which documents exist
   - Current status of each document
   - Current phase
   - Last updated date
3. Identify what's been completed vs. what's pending

### Suggesting Continuation

Based on README Documents section status:

- **All pending** → Suggest starting with requirements
- **Requirements in_progress** → Suggest continuing requirements work
- **Requirements completed, Design pending** → Suggest starting design
- **Design completed, Plan pending** → Assess whether planning is needed (see Planning Assessment)
- **Design completed, Plan skipped** → Suggest moving to implementation
- **All completed** → Suggest moving to implementation or reviewing specification

### Planning Assessment

The planning stage is **optional**. After design is completed, assess whether a plan is needed based on the feature's complexity.

**Plan IS needed** when the feature:
- Requires multiple distinct implementation phases that depend on each other
- Involves changes across several subsystems or layers (e.g., database + API + UI)
- Has ordering constraints where some parts must be built and validated before others
- Carries significant risk that benefits from incremental delivery

**Plan is NOT needed** (skip it) when the feature:
- Can be implemented in a single pass (write code → test → done)
- Touches a small, well-defined area of the codebase
- Has a straightforward implementation path clear from the design
- Doesn't require phased rollout or incremental validation

When planning is not needed, set Plan status to `skipped` in README.md and suggest moving directly to implementation.

## README Management

Every spec directory should have a `README.md` tracking decisions and progress.

### README Template (docs/specs/NNN-name/README.md)

```markdown
# Specification [Number]: [Specification Name]

[Brief description of the feature]

## Status

- **Created**: YYYY-MM-DD HH:mm
- **Current Phase**: Requirements
- **Last Updated**: YYYY-MM-DD HH:mm

## Documents

- **Requirements**: pending
- **Design**: pending
- **Plan**: pending

## History

- YYYY-MM-DD HH:mm: Started initial requirements
```

### History Rules

- Only add entries for major milestones (phase transitions, completion)
- No intermediate updates ("updated requirements", "added section")
- Format: `YYYY-MM-DD HH:mm: Brief description of milestone`
- Chronological order (oldest first, append new at bottom)

### Update Triggers

Update `README.md` when:
- Creating new phase document
- Transitioning status (pending → in_progress → completed)
- Major milestones occur

## Coordination with Specialized Skills

- **specification-requirements**: Handles requirements content guidance
- **specification-design**: Handles design content guidance
- **specification-planning**: Handles planning content guidance

**This guide role**: Create structure, manage statuses in README, orchestrate workflow.
**Their guide role**: Guide content creation, determine completeness.

## Rules

1. Always update README.md Documents section when status changes
2. Always add history entries for phase transitions
3. Delegate content guidance to specialized skills
4. Focus on structure and status management
