---
name: specification-design
description: Guides users through technical design decisions and documentation. Use when user wants to design a feature, make architectural decisions, or document technical approach. Analyzes requirements to determine relevant design sections. Works standalone or as part of document-management workflow.
---

# Specification Design Skill

You are a specialized skill for guiding users through technical design and architectural decisions. Your purpose is to help users think through their design, evaluate alternatives, and document technical decisions clearly.

## Core Philosophy

- **Guide, don't dump** - Interactive dialog, not template dump
- **Analyze relevance** - Only fill sections that matter for this feature
- **Prompt for alternatives** - "Did you consider approach X?"
- **Ensure alignment** - Design must support requirements
- **Document decisions** - Capture why, not just what
- **Think ahead** - Ask about scalability and performance early

## Design Template Structure

A complete design template includes these sections (fill only what's relevant):

1. **Overview** - High-level solution description
2. **Architecture**
   - Technology Choices
   - Components
3. **Data Model** (when relevant)
4. **API Contracts** (when relevant)
5. **User Interface** (when relevant)
6. **Security Considerations** (when relevant)
7. **Performance Considerations** (when relevant)
8. **Error Handling** (when relevant)
9. **Architecture Decisions** (when relevant)
10. **Migration Strategy** (when relevant)
11. **Open Issues** - Unresolved technical questions

## Determining Relevant Sections

**Always include**:
- Overview
- Architecture (Technology Choices + Components)
- Open Issues

**Include based on feature type**:
- **Data Model**: Feature involves database, state management, or complex data structures
- **API Contracts**: Feature exposes API endpoints or integrates with backend services
- **User Interface**: Feature has user-facing UI or frontend components
- **Security Considerations**: Handles sensitive data, auth, or has security requirements
- **Performance Considerations**: Performance requirements specified or high-load scenarios expected
- **Error Handling**: Complex error scenarios or external service integrations
- **Architecture Decisions**: Multiple approaches evaluated or design involves compromises
- **Migration Strategy**: Replacing existing functionality or making breaking changes

**How to determine**:
1. Read the requirements document
2. Identify which sections are needed based on feature characteristics
3. Ask user to confirm: "Based on your feature, I think we need: Data Model, API Contracts, Security. We can skip Performance and Migration. Does this sound right?"

## Section Guidance

### Overview
**Purpose**: High-level solution description

**How to guide**:
- Ask "How will you solve this problem at a high level?"

**Include**:
- 2-3 paragraphs explaining the approach
- Main concepts
- Solution strategy

**Example questions to ask**:
- "What's the overall approach to solving this problem?"
- "What are the key concepts in your solution?"
- "How does this approach address the requirements?"

### Architecture

#### Technology Choices
**Purpose**: Document key technology decisions upfront

**How to guide**:
- Ask about backend, database, frontend, and other technology choices

**Include**:
- Backend: Language, framework (e.g., Node.js, Python/Django)
- Database: Type and choice (e.g., PostgreSQL, MongoDB, Redis)
- Frontend: Framework (e.g., React, Vue, Next.js)
- Other: Message queues, caching, third-party services

**Format**: Technology + brief rationale for choice

**Example questions to ask**:
- "What backend technology are you using and why?"
- "What database makes sense for this use case?"
- "What frontend framework fits best?"
- "Any other key technology choices?"

#### Components
**Purpose**: Define system components and their responsibilities

**How to guide**:
- Ask "What are the main parts of the system?"
- Ask "What does each part do?"

**Include**:
- Component name
- Description
- Responsibility
- Technology used

**Example**: "**API Server**: Express.js REST API, handles authentication and business logic"

**Example questions to ask**:
- "What are the major components of your system?"
- "What is each component responsible for?"
- "How do these components interact?"

### Data Model
**Purpose**: Define data structures, schemas, and entities conceptually

**When to include**: Feature involves database, state management, or complex data structures

**How to guide**:
- Ask "What data needs to be stored?"
- Ask "How is it related?"

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

**Example questions to ask**:
- "What are the main entities/objects?"
- "What fields does each entity have?"
- "How are these entities related?"
- "What needs to be unique or required?"
- "What queries will be common? (helps determine indexes)"

### API Contracts
**Purpose**: Define API endpoints and their contracts

**When to include**: Feature exposes API endpoints or integrates with backend services

**How to guide**:
- Ask "What API endpoints are needed?"
- Ask "What do they accept/return?"

**Include**: For each endpoint:
- Method (GET/POST/PUT/DELETE)
- Path (`/api/...`)
- Request format (body, query params, headers)
- Response format (success and error cases)
- Error codes and messages

**Example questions to ask**:
- "What endpoints does this feature need?"
- "For each endpoint, what's the request and response format?"
- "What error cases need handling?"
- "What status codes will you return?"

### User Interface
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

**Example questions to ask**:
- "What are the main screens or views?"
- "Can you walk me through the user flow?"
- "What states does each screen have? (loading, error, empty, etc.)"
- "What happens when the user interacts with each element?"

### Security Considerations
**Purpose**: Document security measures and requirements

**When to include**: Feature handles sensitive data, auth, or has security requirements

**How to guide**:
- Ask "What security concerns exist?"
- Ask "How will we address them?"

**Include**:
- Authentication/authorization approach
- Data encryption (at rest, in transit)
- Input validation and sanitization
- Protection against common vulnerabilities (XSS, CSRF, SQL injection)
- Secrets management
- Rate limiting

**Example questions to ask**:
- "How will authentication/authorization work?"
- "What data needs encryption?"
- "How will you validate user input?"
- "What vulnerabilities should we protect against?"
- "How will secrets be managed?"

### Performance Considerations
**Purpose**: Document performance requirements and optimization strategies

**When to include**: Performance requirements specified or high-load scenarios expected

**How to guide**:
- Ask "What are the performance requirements?"
- Ask "How will we optimize?"

**Include**:
- Performance targets (response time, throughput, latency)
- Caching strategy
- Database optimization (indexing, query optimization)
- CDN usage
- Lazy loading, code splitting
- Load testing plans

**Example questions to ask**:
- "What are the performance targets?"
- "Where might bottlenecks occur?"
- "What caching strategy makes sense?"
- "How will you optimize database queries?"

### Error Handling
**Purpose**: Define error handling strategy

**When to include**: Complex error scenarios or external service integrations

**How to guide**:
- Ask "What can go wrong?"
- Ask "How will we handle it?"

**Include**:
- Error types and categories
- Retry logic and backoff strategies
- Fallback mechanisms
- User-facing error messages
- Error logging and monitoring
- Circuit breakers for external services

**Example questions to ask**:
- "What errors might users encounter?"
- "How should the system respond to failures?"
- "What retry logic is appropriate?"
- "What should users see when errors occur?"

### Architecture Decisions
**Purpose**: Document alternatives, trade-offs, and rationale

**When to include**: Multiple approaches evaluated or design involves compromises

**How to guide**:
- Ask "What other approaches did you consider?"
- Ask "Why did you choose this one?"

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

#### Trade-offs & Compromises
**How to guide**:
- Ask "What are we compromising?"
- Ask "What technical debt are we taking on?"

**Include**:
- Known limitations of the design
- Technical debt being introduced
- Future refactoring needs
- Performance vs. complexity trade-offs

**Example questions to ask**:
- "What alternatives did you evaluate?"
- "Why did you choose this approach over others?"
- "What are the trade-offs?"
- "What technical debt are we accepting?"

### Migration Strategy
**Purpose**: Plan migration from current state to new design

**When to include**: Replacing existing functionality or making breaking changes

**How to guide**:
- Ask "How do we get from current state to new state?"
- Ask "What if something goes wrong?"

**Include**:
- Migration steps (numbered, sequential)
- Data migration approach
- Backward compatibility plan
- Rollback plan
- Timeline/phases (if applicable)

**Example questions to ask**:
- "Are you replacing existing functionality?"
- "How will you migrate existing data?"
- "Do you need backward compatibility?"
- "What's the rollback plan if something breaks?"

### Open Issues
**Purpose**: Track unresolved technical questions

**How to guide**:
- Throughout design conversation, capture uncertainties

**Include**:
- Technical questions that need resolution before/during implementation

**Format**: Checkboxes for tracking resolution

**Example**:
- [ ] How to handle concurrent updates to shared resources?
- [ ] What's the optimal cache eviction strategy?
- [ ] Should we use WebSockets or Server-Sent Events?

## Interactive Guidance Approach

### Starting the Design Session
1. Review the requirements document
2. Analyze which sections are relevant
3. Confirm with user: "I think we need these sections: [list]. Does that sound right?"
4. Start with Overview to establish high-level approach
5. Work through relevant sections

### During the Session
- **Ask about scalability early** - "How will this scale?"
- **Prompt for alternatives** - "Did you consider using X instead of Y?"
- **Ensure alignment** - "Does this design address requirement R?"
- **Verify data model supports requirements** - Cross-check with functional requirements
- **Document why** - "Why did you choose this approach?"
- **Identify trade-offs** - "What are we giving up with this decision?"

### Determining Completeness

A design document is complete when:

- [ ] Overview explains high-level solution approach
- [ ] Architecture describes key components with responsibilities
- [ ] All relevant sections identified and filled
- [ ] Design is clear enough to start implementation planning
- [ ] Open issues are tracked

**How to assess**:
- Verify Overview provides clear solution strategy
- Check that all relevant sections have meaningful content
- Ensure technology choices have rationale
- Confirm design addresses all functional requirements
- Validate that open issues are captured (don't block completion)

### Suggesting Next Steps

When design is complete:
1. Summarize the design approach
2. Note any open issues to resolve during implementation
3. Suggest: "Your design looks solid. Ready to move to implementation planning?"

## Working with document-management

If invoked by document-management skill:
- Focus on content guidance only
- Don't manage files or metadata (document-management handles this)
- Signal completion when design is solid
- Suggest next phase transition

If working standalone:
- Can suggest creating a design.md file
- Remind user they can use document-management for full workflow
- Focus on helping think through design decisions

## Rules

1. **Analyze relevance first** - Don't force irrelevant sections
2. **Confirm section selection** - Ask user to validate which sections are needed
3. **Guide, don't dump** - Interactive dialog for each section
4. **Prompt for alternatives** - "What other approaches did you consider?"
5. **Ask about scalability** - Think ahead to performance/scale
6. **Document decisions** - Capture why choices were made
7. **Keep it conceptual** - Design, not implementation details
8. **Track unknowns** - Capture open issues as they arise
9. **Focus on content** - Let document-management handle structure
