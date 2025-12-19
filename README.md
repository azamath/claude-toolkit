# Claude Toolkit

## What is it?

A local collection of reusable Claude Code components (commands, agents, skills) that symlink into your global `~/.claude/` configuration.

## Why does it exist?

Instead of duplicating commands, agents, and skills across projects, maintain them in one place. Changes here are instantly available everywhere.

## How to use

1. **Install** - Symlink toolkit to global config:
   ```bash
   ./install.sh
   ```

2. **Backup** - If you have existing directories, back them up first:
   ```bash
   ./backup.sh
   ./install.sh
   ```

3. **Uninstall** - Remove symlinks when done:
   ```bash
   ./uninstall.sh
   ```
