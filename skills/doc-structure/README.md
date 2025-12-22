# Documentation Structure Skill

A Claude Code skill for creating and managing well-structured project documentation for startups.

## Purpose

This skill helps maintain consistent, minimal, and practical documentation structure throughout the project lifecycle. It guides users through creating specifications with proper templates and automatically manages status updates.

## Documentation Structure

```
docs/
├── README.md              # Navigation, project status, history
├── overview.md            # General project information
└── specs/
    └── 001-feature-name/  # 3-digit numbering
        ├── README.md      # Feature status (metadata), history (changelog)
        ├── requirements.md
        ├── design.md
        ├── plan.md
        └── diagrams/      # Optional: UI mockups, flows, architecture diagrams
            ├── screen-name.png
            └── flow-diagram.png
```

## Features

- **Sequential Document Creation**: Creates documents in order (requirements → design → plan) as the conversation progresses
- **Intelligent Section Guidance**: AI analyzes requirements and determines which design sections are relevant
- **Automatic Status Management**: Updates metadata and status automatically
- **Smart Completion Detection**: Skill determines when sections are complete and suggests next steps
- **Changelog Tracking**: Maintains chronological history in README files
- **Clean Templates**: Structural markup only - all guidance centralized in SKILL.md
- **Flexible UI Documentation**: Support for both image-based and AI-generated component descriptions
- **Mermaid Diagrams**: Built-in support for flows, sequences, and state diagrams

## Document Flow

1. **Requirements Phase**
   - Creates `requirements.md` with template
   - Interactive dialog to fill sections
   - Status: `draft`

2. **Design Phase**
   - Creates `design.md` with complete template (11 sections)
   - AI analyzes requirements and determines relevant sections
   - Asks for confirmation on which sections to fill
   - Updates status to `in-design`
   - Guides through only the relevant sections interactively

3. **Planning Phase**
   - Creates `plan.md` when design is approved
   - Updates status to `in-progress`
   - Helps break down implementation

## Metadata Format

```yaml
---
status: draft | in-design | in-progress | completed | cancelled
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Changelog Format

```markdown
## History

- 2025-12-19: Created initial requirements
- 2025-12-20: Design approved
- 2025-12-21: Implementation started
```

## Usage

```bash
# Start new feature documentation
/doc-structure new-feature "Feature Name"

# Continue existing feature
/doc-structure continue 001-feature-name

# Update status
/doc-structure update-status 001-feature-name completed
```

## Templates

See `templates/` directory for clean, structural templates:
- `requirements.md` - Feature requirements template (12 sections)
- `design.md` - Complete technical design template (11 sections)
- `plan.md` - Lightweight implementation plan template (5 sections)

Templates contain only structural markup. All guidance and instructions are in `SKILL.md` under "Section Guidance".

### Design Sections

The design template includes:
1. Overview
2. Architecture (with Technology Choices and Components)
3. Data Model
4. API Contracts
5. User Interface (supports both image storage and AI-generated descriptions)
6. Security Considerations
7. Performance Considerations
8. Error Handling
9. Architecture Decisions (Alternatives + Trade-offs)
10. Migration Strategy
11. Open Issues

### UI Documentation Approaches

**Approach 1 - Store Images**: Export from Figma to `./diagrams/` directory (for stable designs)

**Approach 2 - AI-Generated** (recommended): Share screenshots with AI to generate text-based component structure (no images committed, maintainable)

User flows use Mermaid diagrams: `graph TD` for flows, `sequenceDiagram` for sequences, `stateDiagram-v2` for state machines.
