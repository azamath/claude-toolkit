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

## Code comments

Comments explain *why*, not *what*. The code already says what it does; a comment earns its place only by adding information the code cannot.

- **Comment the non-obvious.** Explain intent, trade-offs, constraints, and the reason behind a surprising choice — a workaround, an edge case, a business rule, a link to an issue or spec.
- **Delete comments that restate the code.** `// increment i` above `i++` is noise. If a comment only paraphrases the line below it, remove it and let the code speak.
- **Prefer clearer code over an explanatory comment.** If a comment is needed to understand *what* the code does, first try renaming, extracting a function, or simplifying. Reach for a comment only when the clarity can't live in the code itself.
- **Keep comments truthful and current.** A wrong comment is worse than none. When changing code, update or delete the comments around it — never leave a stale one behind.
- **No commented-out code.** Delete it; version control remembers. Dead code left in comments rots and confuses.
- **Use the language's doc convention for public API.** Document exported functions, types, and modules with the idiomatic doc-comment format (JSDoc, docstrings, `///`, etc.) — describe purpose, parameters, and gotchas, not the implementation.
