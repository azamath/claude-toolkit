# Claude Toolkit

A collection of reusable Claude Code components, distributed two ways: symlinked into your global Claude configuration, or installed as Claude Code plugins.

## How It Works

This project maintains a centralized collection of Claude Code extensions (commands, agents, skills) in organized directories.
There are two distribution modes, and each component belongs to exactly one of them:

- **Local** — components under `local/` are symlinked into `~/.claude/` by `install-local.sh`, making them available across all your projects.
- **Plugins** — self-contained plugins under `plugins/`, each with its own `.claude-plugin/plugin.json`, published through the marketplace manifest in `.claude-plugin/marketplace.json`.

When adding a component, decide which mode it belongs to first. A plugin bundles its own `commands/`, `agents/`, and `skills/`.

## Directory Structure

- `local/` - Components symlinked into the global config
  - `commands/` - Custom slash commands
  - `agents/` - Custom agent configurations
  - `skills/` - Reusable skills
- `plugins/` - Self-contained Claude Code plugins
- `.claude-plugin/marketplace.json` - Marketplace manifest listing published plugins
- `CLAUDE.md` - This documentation file
- `README.md` - Human-oriented documentation and usage instructions
- `*-local.sh` - Bash scripts for the local install mode

## Writing rules

Rules for what may be written — in skills, commands, templates, and docs like this one.

- **Write only what was settled.** Content is decided in discussion, not during writing. Writing is transcription: it gives settled decisions their final wording and order. It is not the step where the remaining content gets worked out.
- **Never supply a reason that wasn't given.** A rule stated with a rationale its author never offered is worse than a bare rule — it reads as their reasoning, gets trusted, and gets built on. When a decision was made without a stated why, write the decision alone.
- **Compress to the minimum.** Write settled content in the fewest words that carry it. Every sentence must add something the reader doesn't already have — cut restatement, hedging, and preamble. Length is never a proxy for completeness.
- **A gap is a signal, not a slot.** Unaddressed areas are unfinished discussion. Do not close them with plausible content; leave them out and name them as unsettled.
