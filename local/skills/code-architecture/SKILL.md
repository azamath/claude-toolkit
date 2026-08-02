---
description: Opinionated guidance on code architecture — where logic lives, how modules are bounded, how dependencies flow, and how state and data move through the system. Use when deciding where new code should go or critiquing/refactoring existing structure.
user-invocable: true
---

# Code Architecture

A library of opinionated, self-contained guides on code architecture — where logic lives,
how modules are bounded, how dependencies flow, and how state and data move through the
system. Each covers one topic under `references/`. This file maps situations to the right
guide.

Match the situation to a guide below, read that file, and apply it — load only the ones
the current task needs.

## Available guides

- **`references/folder-organization/principles.md`** — where files and folders go: top-level project layout, how to group code (by feature vs. by layer), shared code, naming, and where new code should live. Read when setting up a new project's structure, adding a feature and unsure where it belongs, or critiquing/refactoring an existing layout. Start here for any folder question, then read the matching stack file below.
  - **`references/folder-organization/nextjs.md`** — concrete Next.js App Router layout: how the framework-owned `app/` directory and reserved route filenames coexist with your domain-organized `features/`. Read when working in a Next.js project.

<!--
Add a bullet per topic. Keep each to: the file path + a one-line trigger describing
WHEN to read it (the situation), not what it says. The detailed guidance stays in the
reference file.
-->
