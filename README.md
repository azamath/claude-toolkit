# Claude Toolkit

## What is it?

A collection of reusable Claude Code components (commands, agents, skills), distributed two ways:

- **Local** — components in `local/` symlink into your global `~/.claude/` configuration.
- **Plugins** — self-contained plugins in `plugins/`, published via the marketplace manifest in `.claude-plugin/marketplace.json`.

## Why does it exist?

Instead of duplicating commands, agents, and skills across projects, maintain them in one place. Changes here are instantly available everywhere.

## Local install

1. **Install** - Symlink `local/` components into the global config:
   ```bash
   ./install-local.sh
   ```

2. **Backup** - If you have existing directories, back them up first:
   ```bash
   ./backup-local.sh
   ./install-local.sh
   ```

3. **Uninstall** - Remove symlinks when done:
   ```bash
   ./uninstall-local.sh
   ```

## Plugins

Published plugins:

- **specs** — specification and product documentation components.

To add one, create `plugins/<name>/` with a `.claude-plugin/plugin.json`
manifest, then add an entry to `.claude-plugin/marketplace.json` with `"source": "./plugins/<name>"`.

Install this repo as a marketplace with:

```bash
/plugin marketplace add /path/to/claude-toolkit
```
