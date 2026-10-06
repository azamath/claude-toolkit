---
description: Opinionated conventions for writing code — how to comment, and general rules for naming, structure, and formatting. Use when writing new code or reviewing/refactoring for style.
user-invocable: true
---

# Code Style

Conventions for writing code that reads clearly and stays consistent. Apply when writing new code or reviewing existing code for style.

## General rules

- **Name for intent.** Names should reveal purpose and read naturally. Avoid abbreviations, single letters (outside tight loops), and vague names like `data`, `tmp`, `handle`, `manager`.
- **Order top-down.** Place the main exported functions and types first, internal helpers after — the reader meets the public surface before the details.
- **Avoid needless cleverness.** Write the clear version, not the shortest or most impressive one. Optimize only where a real bottleneck justifies the loss in readability.
- **Let tools own formatting.** Defer whitespace, quotes, and line width to the project's formatter and linter. Don't hand-format against them or reformat unrelated lines in a change.

## Code comments rules

- **Explain why, not what.** Write intent, trade-offs, constraints, and the reason behind a surprising choice — a workaround, an edge case, a business rule, a link to an issue or spec. Don't paraphrase the code: `// increment i` above `i++` is noise.
- **Describe only what this code owns.** Document a dependency's behavior in the dependency itself. If this code relies on that behavior, state the reliance, not the behavior.
- **Prefer code over a comment.** If a comment is needed to explain what the code does, rename, extract a function, or simplify instead. If it states a reliance, enforce it with an assertion, type, or test where possible.
- **Keep comments true.** A wrong comment is worse than none. When changing code, update or delete the comments around it. In review, ask of each comment: would it become false if another file changed? If so, move the fact to its owner or rewrite it as a reliance.
- **Delete commented-out code.** Version control remembers; dead code left in comments rots and confuses.
- **Follow the language's doc convention for public API.** Document exported functions, types, constants, and modules with the idiomatic doc-comment format (JSDoc, docstrings, `///`, etc.) — purpose, parameters, and gotchas, not the implementation. Anything exported counts as public, even inside an internal package or monorepo workspace.
- **Doc-comment members of exported shapes.** A comment on a field, property, or enum member of an exported type or object uses the doc-comment format too, so it surfaces on hover. Plain line comments are for function bodies and non-exported code.
