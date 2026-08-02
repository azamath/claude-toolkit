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
