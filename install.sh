#!/bin/bash

# Claude Toolkit Installation Script
# Symlinks toolkit components individually into global Claude configuration

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

# Link a single item, creating parent directories as needed
# $1 = path relative to TOOLKIT_DIR
link_item() {
    local rel="$1"
    local source="${TOOLKIT_DIR}/${rel}"
    local target="${CLAUDE_CONFIG_DIR}/${rel}"

    mkdir -p "$(dirname "${target}")"

    if [ -L "${target}" ]; then
        if [ "$(readlink "${target}")" = "${source}" ]; then
            echo "✓ Already linked: ${rel}"
        else
            echo "⚠ Symlink exists but points elsewhere: ${rel}"
            echo "  Points to: $(readlink "${target}")"
        fi
    elif [ -e "${target}" ]; then
        echo "⚠ Warning: ${rel} already exists and is not a symlink"
        echo "  Please backup and remove: ${target}"
    else
        ln -s "${source}" "${target}"
        echo "✓ Linked: ${rel}"
    fi
}

# Link every command (leaf .md files, namespace directories recreated as real dirs)
install_commands() {
    [ -d "${TOOLKIT_DIR}/commands" ] || return 0
    echo "Commands:"
    local found=0
    while IFS= read -r file; do
        found=1
        link_item "commands/${file#./}"
    done < <(cd "${TOOLKIT_DIR}/commands" && find . -type f -name '*.md' | sed 's|^\./||' | sort)
    [ "${found}" -eq 0 ] && echo "- none found"
    echo ""
}

# Link every agent (leaf .md files)
install_agents() {
    [ -d "${TOOLKIT_DIR}/agents" ] || return 0
    echo "Agents:"
    local found=0
    while IFS= read -r file; do
        found=1
        link_item "agents/${file#./}"
    done < <(cd "${TOOLKIT_DIR}/agents" && find . -type f -name '*.md' | sed 's|^\./||' | sort)
    [ "${found}" -eq 0 ] && echo "- none found"
    echo ""
}

# Link every skill as a whole directory (skills bundle SKILL.md plus resources)
install_skills() {
    [ -d "${TOOLKIT_DIR}/skills" ] || return 0
    echo "Skills:"
    local found=0
    while IFS= read -r dir; do
        found=1
        link_item "skills/${dir}"
    done < <(cd "${TOOLKIT_DIR}/skills" && find . -mindepth 1 -maxdepth 1 -type d | sed 's|^\./||' | sort)
    [ "${found}" -eq 0 ] && echo "- none found"
    echo ""
}

echo "Installing components..."
echo ""

install_commands
install_agents
install_skills

echo "Installation complete!"
echo ""
echo "Your toolkit components are now available globally."
