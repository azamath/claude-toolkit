#!/bin/bash

# Claude Toolkit Installation Script
# Symlinks toolkit components into global Claude configuration

set -e

TOOLKIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_CONFIG_DIR="${HOME}/.claude"

echo "Claude Toolkit Installer"
echo "========================"
echo ""
echo "Toolkit directory: ${TOOLKIT_DIR}"
echo "Claude config directory: ${CLAUDE_CONFIG_DIR}"
echo ""

# Create Claude config directory if it doesn't exist
if [ ! -d "${CLAUDE_CONFIG_DIR}" ]; then
    echo "Creating Claude config directory..."
    mkdir -p "${CLAUDE_CONFIG_DIR}"
fi

# Function to create symlink
create_symlink() {
    local source_dir="${TOOLKIT_DIR}/$1"
    local target_dir="${CLAUDE_CONFIG_DIR}/$1"

    if [ -L "${target_dir}" ]; then
        echo "✓ Symlink already exists: $1"
        echo "  Points to: $(readlink "${target_dir}")"
    elif [ -e "${target_dir}" ]; then
        echo "⚠ Warning: $1 already exists and is not a symlink"
        echo "  Please backup and remove: ${target_dir}"
        return 1
    else
        echo "Creating symlink: $1"
        ln -s "${source_dir}" "${target_dir}"
        echo "✓ Created: ${target_dir} -> ${source_dir}"
    fi
}

# Create symlinks for each component
echo "Installing components..."
echo ""

create_symlink "commands"
create_symlink "agents"
create_symlink "skills"

echo ""
echo "Installation complete!"
echo ""
echo "Your toolkit components are now available globally."
