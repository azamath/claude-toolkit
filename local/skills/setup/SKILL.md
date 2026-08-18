---
description: Opinionated guidance on setting up and configuring project tooling — which tool to pick for a job, how it's configured, and how it wires into the runtime. Use when setting up a tool in a project or reviewing an existing setup.
user-invocable: true
---

# Setup

A library of opinionated, self-contained guides on project tooling — which tool to pick for a job, how it's configured, and how it wires into the runtime. Each covers one topic under `references/`. This file maps situations to the right guide.

Match the situation to a guide below, read that file, and apply it — load only the ones the current task needs.

## Available guides

- **`references/logging/node-gcp.md`** — application logging for a Node service running on Google Cloud: picking the logger, emitting structured entries Cloud Logging understands, and wiring errors through to Error Reporting. Read when adding logging to a Node service deployed on GCP, or reviewing one that logs unstructured text.
