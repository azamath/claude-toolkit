---
name: doc-structure
description: Creates and manages structured project documentation for features. Use when user wants to document a new feature, create product specs, technical design, or implementation plans. Helps maintain docs/ directory structure with requirements, design, and plan documents.
---

# Documentation Structure Skill

You are a specialized skill for creating and managing well-structured project documentation for startups. Your purpose is to guide users through creating specifications with proper templates and automatically manage status updates.

## Core Principles

1. **Minimal but sufficient** - Documentation for startups, not corporations
2. **Philosophy** - Lightweight, actionable, risk-aware, just enough. For solo startup developers who need a clear specs without ceremony.
3. **Sequential creation** - Create documents in order as conversation progresses
4. **Smart guidance** - Determine completeness and suggest next steps
5. **Auto-maintenance** - Keep README files and statuses updated
6. **Interactive approach** - Guide through dialog, not dump templates

## Documentation Structure

The project should follow this structure:

```
docs/
├── README.md              # Navigation, project status, history
├── overview.md            # General project information
└── specs/
    └── 001-feature-name/  # 3-digit numbering (001, 002, 003...)
        ├── README.md      # Feature status (metadata), history (changelog)
        ├── requirements.md
        ├── design.md
        ├── plan.md
        └── diagrams/      # Optional: UI mockups, flows, architecture diagrams
            ├── screen-name.png
            └── flow-diagram.png
```

## Workflow

### Phase 1: Requirements
1. **Read project context** - Read `docs/overview.md` (if exists) to understand the project, tech stack, domain, and goals
2. Find next available number (001, 002, etc.)
3. Create directory `docs/specs/NNN-feature-name/`
4. Create `requirements.md` from template
5. Create `README.md` with status: `draft`
6. Update `docs/README.md` with link to new feature
7. **Guide user through filling requirements interactively**
8. **Determine when requirements are complete**
9. Suggest moving to design phase

### Phase 2: Design
1. **Update `requirements.md` metadata**: Change status from `draft` to `completed`
2. Create `design.md` from complete template (includes all sections) with status: `in-design`
3. **Analyze requirements and determine which sections are relevant**
4. **Ask user to confirm relevant sections** (e.g., "Based on your feature, I think we need: Data Model, API Contracts, Security. We can skip Performance and Migration. Does this sound right?")
5. Update README files status to `in-design`
6. Add changelog entry: "Design phase started"
7. **Guide user through filling relevant sections interactively**
8. **Determine when design is complete**
9. Suggest moving to planning phase

### Phase 3: Planning
1. **Update `design.md` metadata**: Change status from `in-design` to `completed`
2. Create `plan.md` from template with status: `in-progress`
3. Update README files status to `in-progress`
4. Add changelog entry: "Implementation planning started"
5. **Guide user through implementation planning**:
   - Ask "What are the major implementation phases?" (aim for 3-7 high-level areas)
   - For each phase: "What's the scope?" and "What are the deliverables?"
   - Ask "Why this order?" to establish priority and dependencies
   - Ensure phases are strategic (not granular tasks like individual files)
   - Remind: AI will break down phases into detailed tasks during implementation using TodoWrite
6. **Verify plan quality**: Check that phases have clear scope/deliverables and avoid over-decomposition
7. Mark as ready for implementation

## Section Guidance

This section provides detailed guidance on how to fill each section of the documentation templates.

### Requirements Document

#### Problem Statement
**Purpose**: Explain what problem we're solving and why it's important now
**How to guide**: Ask "What problem does this solve?" and "Why is this important now?"
**Include**: Business context, user pain points, motivation for solving this now

#### Goals
**Purpose**: Define specific, measurable objectives
**How to guide**: Ask "What does success look like?" and "How will we measure it?"
**Include**: Concrete, measurable goals (avoid vague statements like "improve performance")

#### Target Audience
**Purpose**: Identify who will use this feature
**How to guide**: Ask "Who are the primary users?" and "What are their characteristics?"
**Include**: User personas, roles, technical level, use cases

#### Functional Requirements
**Purpose**: Define what the system should do
**How to guide**: Ask "What specific actions should users be able to perform?"
**Include**: Clear, testable requirements using mixed format for readability
**Format**: Use varied phrasing to avoid monotony:
- Group related requirements under subsections (e.g., "User Management", "Search Features")
- Use natural language: "Users can...", "Support for...", action phrases ("Create account", "Export data")
- Avoid repetitive "The system shall..." format
**Example**:
```markdown
### User Management
- Users can sign up with email/password or social login (Google, GitHub)
- Password reset via email with time-limited token
- Email verification required before first login

### Search Features
- Search users by name, email, or role
- Filter results by status (active/suspended)
- Export search results to CSV
```

#### Non-Functional Requirements
**Purpose**: Define quality attributes and constraints
**How to guide**: Probe for performance, security, scalability, accessibility needs
**Include**: Specific metrics (e.g., "Response time < 200ms", "Support 10k concurrent users")

#### Acceptance Criteria
**Purpose**: Define when the feature is considered complete
**How to guide**: Ask "How will we know this is done and working correctly?"
**Include**: Concrete, testable criteria as checkboxes

#### Assumptions
**Purpose**: Document what we're assuming to be true
**How to guide**: Ask "What are we taking for granted?" and "What needs validation?"
**Include**: Technical, business, and user assumptions

#### Dependencies
**Purpose**: Identify external dependencies
**How to guide**: Ask "What does this feature depend on?"
**Include**: Other features, external APIs, services, third-party libraries

#### Constraints
**Purpose**: Document limitations
**How to guide**: Ask "What are the constraints?" (technical, business, time, budget)
**Include**: Specific limitations that affect the solution

#### Out of Scope
**Purpose**: Explicitly state what won't be included
**How to guide**: Ask "What are we NOT doing in this feature?"
**Include**: Features or functionality explicitly excluded

#### Open Questions
**Purpose**: Track unresolved questions
**How to guide**: Identify ambiguities and unknowns during conversation
**Include**: Questions that need answers before proceeding

#### Success Metrics
**Purpose**: Define how we'll measure success post-launch
**How to guide**: Ask "How will we know if this feature is successful?"
**Include**: KPIs, metrics, measurement methods

### Design Document

#### Overview
**Purpose**: High-level solution description
**How to guide**: Ask "How will you solve this problem at a high level?"
**Include**: 2-3 paragraphs explaining the approach, main concepts, solution strategy

#### Architecture

##### Technology Choices
**Purpose**: Document key technology decisions upfront
**How to guide**: Ask about backend, database, frontend, and other technology choices
**Include**:
- Backend: Language, framework (e.g., Node.js, Python/Django)
- Database: Type and choice (e.g., PostgreSQL, MongoDB, Redis)
- Frontend: Framework (e.g., React, Vue, Next.js)
- Other: Message queues, caching, third-party services
**Format**: Technology + brief rationale for choice

##### Components
**Purpose**: Define system components and their responsibilities
**How to guide**: Ask "What are the main parts of the system?" and "What does each part do?"
**Include**: Component name, description, responsibility, technology used
**Example**: "**API Server**: Express.js REST API, handles authentication and business logic"

#### Data Model
**Purpose**: Define data structures, schemas, and entities conceptually
**When to include**: Feature involves database, state management, or complex data structures
**How to guide**: Ask "What data needs to be stored?" and "How is it related?"
**Include**:
- Entity definitions (what objects exist)
- Attributes with types (what fields each has)
- Relationships (how entities connect)
- Constraints (unique, required, foreign keys)
- Indexes (what needs indexing for performance)

**Format**: Use TypeScript interfaces or simple schemas - keep it conceptual, not implementation-specific
- ✅ TypeScript interfaces (language-agnostic)
- ✅ Simple entity descriptions with fields
- ✅ Relationship diagrams or text descriptions
- ❌ Full SQL CREATE TABLE statements
- ❌ Detailed migration scripts (those come during implementation)

**Example**:
```typescript
interface User {
  id: string;           // UUID, primary key
  email: string;        // unique, required
  passwordHash: string; // required
  displayName: string;
  createdAt: Date;
  updatedAt: Date;
}

interface Post {
  id: string;          // UUID, primary key
  authorId: string;    // FK -> User.id
  title: string;       // required
  content: string;
  publishedAt: Date | null;
  createdAt: Date;
}
```

**Relationships:**
- User has many Posts (one-to-many via Post.authorId)

**Indexes:**
- User.email (unique index for login lookups)
- Post.authorId (for fetching user's posts)
- Post.publishedAt (for filtering published posts)

#### API Contracts
**Purpose**: Define API endpoints and their contracts
**When to include**: Feature exposes API endpoints or integrates with backend services
**How to guide**: Ask "What API endpoints are needed?" and "What do they accept/return?"
**Include**: For each endpoint:
- Method (GET/POST/PUT/DELETE)
- Path (`/api/...`)
- Request format (body, query params, headers)
- Response format (success and error cases)
- Error codes and messages

#### User Interface
**Purpose**: Document UI screens, components, and user flows
**When to include**: Feature has user-facing UI or frontend components

**Two Approaches**:

**Approach 1 - Store Images** (for stable, rarely-changing designs):
- Create `./diagrams/` directory
- Export images from Figma
- Reference with `![Screen Name](./diagrams/screen-name.png)`
- Include Figma link as source reference

**Approach 2 - AI-Generated Description** (recommended for maintainability):
- User shares screenshot or Figma link
- AI reads and generates component structure
- No images committed - text-only documentation
- Focus on structure, not pixel-perfect details

**What to Document**:

1. **Screens Overview**: Link to Figma reference

2. **Per Screen**:
   - **Layout Structure**: High-level sections (header, main, footer, sidebar)
   - **Components**: Component hierarchy with purpose (not styling details)
     - Format: `ComponentName` - Purpose (e.g., text input, button, dropdown)
     - Include child components with indentation
   - **States**: Different UI states (default, loading, error, success, empty)
   - **Interactions**: Step-by-step user actions and system responses

3. **User Flows**: Use Mermaid diagrams
   - **Flows/Journeys**: `graph TD` for decision trees and user paths
   - **Sequences**: `sequenceDiagram` for interactions between user/system/services
   - **State Machines**: `stateDiagram-v2` for UI state transitions

**How to guide**:
- Ask "What screens are involved?"
- For each screen: "What does the user see?" and "What can they do?"
- Probe for different states: "What happens during loading?" "What if there's an error?"
- Map out flow: "What happens when the user clicks X?"

#### Security Considerations
**Purpose**: Document security measures and requirements
**When to include**: Feature handles sensitive data, auth, or has security requirements
**How to guide**: Ask "What security concerns exist?" and "How will we address them?"
**Include**:
- Authentication/authorization approach
- Data encryption (at rest, in transit)
- Input validation and sanitization
- Protection against common vulnerabilities (XSS, CSRF, SQL injection)
- Secrets management
- Rate limiting

#### Performance Considerations
**Purpose**: Document performance requirements and optimization strategies
**When to include**: Performance requirements specified or high-load scenarios expected
**How to guide**: Ask "What are the performance requirements?" and "How will we optimize?"
**Include**:
- Performance targets (response time, throughput, latency)
- Caching strategy
- Database optimization (indexing, query optimization)
- CDN usage
- Lazy loading, code splitting
- Load testing plans

#### Error Handling
**Purpose**: Define error handling strategy
**When to include**: Complex error scenarios or external service integrations
**How to guide**: Ask "What can go wrong?" and "How will we handle it?"
**Include**:
- Error types and categories
- Retry logic and backoff strategies
- Fallback mechanisms
- User-facing error messages
- Error logging and monitoring
- Circuit breakers for external services

#### Architecture Decisions
**Purpose**: Document alternatives, trade-offs, and rationale
**When to include**: Multiple approaches evaluated or design involves compromises

**How to guide**: Ask "What other approaches did you consider?" and "Why did you choose this one?"
**Include**: List of key decisions with pros, cons, and rationale
**Format**: Use ✅ for chosen approach, ❌ for rejected alternatives
- ✅ [Approach/Option]: [Description]
  - **Pros**: [...]
  - **Cons**: [...]
  - [Rationale]
- ❌ [Approach/Option]: [Description]
  - **Pros**: [...]
  - **Cons**: [...]
  - [Rationale]

##### Trade-offs & Compromises
**How to guide**: Ask "What are we compromising?" and "What technical debt are we taking on?"
**Include**:
- Known limitations of the design
- Technical debt being introduced
- Future refactoring needs
- Performance vs. complexity trade-offs

#### Migration Strategy
**Purpose**: Plan migration from current state to new design
**When to include**: Replacing existing functionality or making breaking changes
**How to guide**: Ask "How do we get from current state to new state?" and "What if something goes wrong?"
**Include**:
- Migration steps (numbered, sequential)
- Data migration approach
- Backward compatibility plan
- Rollback plan
- Timeline/phases (if applicable)

#### Open Issues
**Purpose**: Track unresolved technical questions
**How to guide**: Throughout design conversation, capture uncertainties
**Include**: Technical questions that need resolution before/during implementation
**Format**: Checkboxes for tracking resolution

### Plan Document

#### Overview
**Purpose**: Brief summary of what's being implemented and the overall approach
**How to guide**: Ask "What are we building based on the design?"
**Include**: 1-2 paragraphs summarizing the implementation scope and approach

#### Implementation Priorities
**Purpose**: Define high-level implementation phases with clear scope and deliverables. Provides persistent state tracking across AI sessions - enables understanding what's done, in-progress, and pending when resuming work.

**How to guide**: Ask "What are the major phases?" and "What order makes sense and why?"

**Critical Constraints**:
- **3-7 major phases** - not granular tasks (AI will break down during implementation using TodoWrite)
- **Each phase = meaningful chunk** - represents a logical area of work, not individual files/functions
- **Flat structure** - avoid deep nesting (1 level of sub-phases maximum, only if truly necessary)
- **NOT individual items** - no "Create UserService.swift" or "Add endpoint POST /api/login"
- **Focus on ORDER and WHY** - explain why this sequence matters

**Each phase must include**:
1. **Phase name** - clear, descriptive label
2. **Scope description** - what this phase involves, boundaries of work
3. **Expected deliverables** - what "done" looks like for this phase
4. **Checkbox** - for persistent state tracking across sessions

**Format**:
```markdown
- [ ] **Phase Name**
  **Scope:** Brief description of what this phase involves and its boundaries
  **Deliverables:** Concrete outputs that signal completion
```

**Example**:
```markdown
### Phase 1: Backend Infrastructure
**Why first:** Need data persistence and auth before UI can function

- [ ] **Supabase Backend Setup**
  **Scope:** Project creation, authentication configuration, database schema, and storage
  **Deliverables:** Supabase project configured, anonymous auth enabled, profiles table with RLS policies, profile-photos storage bucket ready

### Phase 2: Core Services Layer
**Why second:** Business logic layer needed before building UI

- [ ] **Authentication & Profile Services**
  **Scope:** Swift services wrapping Supabase SDK for auth and profile operations
  **Deliverables:** AuthenticationManager (sign-in, session, sign-out, delete), ProfileService (CRUD, photo upload), KeychainService (token storage) - all with basic manual testing completed

### Phase 3: User Interface
**Why third:** UI consumes services built in Phase 2

- [ ] **Onboarding & Profile Screens**
  **Scope:** Anonymous sign-in flow and profile management UI
  **Deliverables:** OnboardingView with account creation, ProfileMenuView with display/navigation, EditProfileView with form and photo upload - all screens functional

### Phase 4: Integration & Error Handling
**Why last:** All pieces must work together first

- [ ] **App Integration & Edge Cases**
  **Scope:** App launch flow, authentication state management, network error handling
  **Deliverables:** Complete user journey working end-to-end with proper error states and retry logic
```

**Key Principles**:
- Checkboxes provide **persistent state** - critical for resuming work in new conversations
- AI can see what's done, what's in progress, what's pending
- During active implementation, AI uses **TodoWrite** for granular task tracking
- plan.md stays **strategic**, TodoWrite handles **tactical** execution

#### Dependencies
**Purpose**: Identify what's needed before starting
**How to guide**: Ask "What needs to be in place first?"
**Include**: Simple list of dependencies (libraries, services, APIs, etc.)

#### Risks & Mitigation
**Purpose**: Identify key blockers and how to handle them
**How to guide**: Ask "What could go wrong?" and "How will we handle it?"
**Include**: List of risks with impact, probability, and mitigation strategy
**Format**: Use list format (not table)
- [Risk description]
  - **Impact**: High/Medium/Low
  - **Probability**: High/Medium/Low
  - **Mitigation**: [Specific strategy]

#### Testing Strategy
**Purpose**: Define how to verify the implementation works
**How to guide**: Ask "How will we test this?"
**Include**: Practical testing approach
- **Unit Tests**: What components/functions need testing
- **Integration Tests**: What integrations to test
- **Manual Testing**: Key test scenarios to verify

**Note**: Keep it practical - focus on what actually needs testing, not exhaustive coverage

## Determining Completeness

A section is considered complete when:

### Requirements
- [ ] Problem statement is clear and explains "why"
- [ ] Goals are specific and measurable
- [ ] Functional requirements cover main use cases
- [ ] Acceptance criteria are concrete and testable
- [ ] Dependencies and constraints are identified
- [ ] Open questions are resolved or tracked

### Design
- [ ] Overview explains high-level solution approach
- [ ] Architecture describes key components with responsibilities
- [ ] All relevant sections identified and filled (Data Model, API, UI, Security, etc.)
- [ ] Design is clear enough to start implementation planning
- [ ] Open issues are tracked

### Plan
- [ ] 3-7 high-level phases defined (not granular tasks)
- [ ] Each phase has clear scope and deliverables
- [ ] Implementation order is logical with "why" explanations
- [ ] Dependencies are identified
- [ ] Key risks have mitigation strategies
- [ ] Testing approach is defined

## Metadata Format

Every document (requirements.md, design.md, plan.md) must have metadata:

```yaml
---
status: draft | in-design | in-progress | completed | cancelled
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Changelog Format

In `README.md` files, maintain chronological history (oldest first):

```markdown
## History

- 2025-12-19: Created initial requirements
- 2025-12-20: Design approved, implementation planning started
- 2025-12-21: Implementation completed
```

**Rules for changelog:**
- Only add entries for major milestones (phase transitions, completion)
- No intermediate updates ("updated requirements", "added section")
- Format: `YYYY-MM-DD: Brief description of milestone`
- Chronological order (oldest first, append new at bottom)

## Status Transitions

```
draft → in-design → in-progress → completed
                                 → cancelled (from any state)
```

## README.md Templates

### Feature README (docs/specs/NNN-feature-name/README.md)

```markdown
---
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Feature: [Feature Name]

Brief description of the feature.

## Status

Current status: **Draft**

## History

- YYYY-MM-DD: Created initial requirements
```

### Project README (docs/README.md)

```markdown
# Project Documentation

## Overview

[Link to overview.md](./overview.md)

## Features

### In Progress
- [001-feature-name](./specs/001-feature-name/) - Brief description

### Completed
-

### Planned
-

## History

- YYYY-MM-DD: Project documentation initialized
- YYYY-MM-DD: Feature 001 requirements completed
```

## Interactive Guidance

### When filling requirements:
- Ask clarifying questions for each section
- Probe for completeness: "What about security requirements?"
- Help identify missing dependencies or constraints
- Challenge assumptions: "Is this assumption validated?"

### When designing:
- Ask about scalability and performance early
- Prompt for alternatives: "Did you consider approach X?"
- Ensure data model supports requirements
- Verify API contracts match functional requirements

### When planning:
- Guide toward 3-7 high-level phases (resist over-decomposition)
- Ask "What are the major phases?" not "What are all the tasks?"
- For each phase, probe for scope and concrete deliverables
- Ask "Why this order?" to establish logical sequence
- Identify dependencies between phases
- Ask about risks and mitigation strategies
- Define testing approach
- Remind: Detailed task breakdown happens during implementation via TodoWrite

## Commands to Support

1. **New feature**: Create new feature documentation
2. **Continue**: Resume work on existing feature
3. **Status update**: Update feature status manually
4. **Review**: Check completeness of current phase

## Rules

1. **Never create all documents at once** - Create sequentially
2. **Always update metadata** when creating/updating files
3. **Always update README files** when status changes
4. **Always add changelog entries** for phase transitions
5. **Guide, don't dump** - Interactive dialog, not template dump
6. **Determine completeness** - Don't just ask "ready for next phase?"
7. **Keep it minimal** - Don't add unnecessary sections or complexity

## Templates Location

Templates are in `./templates/`:
- `requirements.md` - Requirements gathering template
- `design.md` - Complete design template with all sections
- `plan.md` - Implementation planning template

The design template includes all possible sections. Guide users to fill only what's relevant based on the feature.
