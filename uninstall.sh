#!/bin/bash

# Claude Toolkit Uninstallation Script
# Removes symlinks from global Claude configuration

set -e

CLAUDE_CONFIG_DIR="${HOME}/.claude"

echo "Claude Toolkit Uninstaller"
echo "=========================="
echo ""

# Function to remove symlink
remove_symlink() {
    local target_dir="${CLAUDE_CONFIG_DIR}/$1"

    if [ -L "${target_dir}" ]; then
        echo "Removing symlink: $1"
        rm "${target_dir}"
        echo "✓ Removed: ${target_dir}"
    elif [ -e "${target_dir}" ]; then
        echo "⚠ Warning: $1 exists but is not a symlink"
        echo "  Skipping: ${target_dir}"
    else
        echo "- Not installed: $1"
    fi
}

# Remove symlinks for each component
echo "Uninstalling components..."
echo ""

remove_symlink "commands"
remove_symlink "agents"
remove_symlink "skills"

echo ""
echo "Uninstallation complete!"
