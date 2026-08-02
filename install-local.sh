#!/bin/bash

# Claude Toolkit Local Installation Script
# Symlinks components from local/ individually into global Claude configuration

set -e

TOOLKIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_DIR="${TOOLKIT_DIR}/local"
CLAUDE_CONFIG_DIR="${HOME}/.claude"

echo "Claude Toolkit Local Installer"
echo "=============================="
echo ""
echo "Local components: ${LOCAL_DIR}"
echo "Claude config directory: ${CLAUDE_CONFIG_DIR}"
echo ""

# Create Claude config directory if it doesn't exist
if [ ! -d "${CLAUDE_CONFIG_DIR}" ]; then
    echo "Creating Claude config directory..."
    mkdir -p "${CLAUDE_CONFIG_DIR}"
fi

# Link a single item, creating parent directories as needed
# $1 = path relative to LOCAL_DIR, $2 = path relative to CLAUDE_CONFIG_DIR
link_item() {
    local rel="$1"
    local target_rel="$2"
    local source="${LOCAL_DIR}/${rel}"
    local target="${CLAUDE_CONFIG_DIR}/${target_rel}"

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
    [ -d "${LOCAL_DIR}/commands" ] || return 0
    echo "Commands:"
    local found=0
    while IFS= read -r file; do
        found=1
        link_item "commands/${file#./}" "commands/${file#./}"
    done < <(cd "${LOCAL_DIR}/commands" && find . -type f -name '*.md' | sed 's|^\./||' | sort)
    [ "${found}" -eq 0 ] && echo "- none found"
    echo ""
}

# Link every agent (leaf .md files)
install_agents() {
    [ -d "${LOCAL_DIR}/agents" ] || return 0
    echo "Agents:"
    local found=0
    while IFS= read -r file; do
        found=1
        link_item "agents/${file#./}" "agents/${file#./}"
    done < <(cd "${LOCAL_DIR}/agents" && find . -type f -name '*.md' | sed 's|^\./||' | sort)
    [ "${found}" -eq 0 ] && echo "- none found"
    echo ""
}

# Link every skill as a whole directory (skills bundle SKILL.md plus resources)
install_skills() {
    [ -d "${LOCAL_DIR}/skills" ] || return 0
    echo "Skills:"
    local found=0
    while IFS= read -r dir; do
        found=1
        link_item "skills/${dir}" "skills/${dir}"
    done < <(cd "${LOCAL_DIR}/skills" && find . -mindepth 1 -maxdepth 1 -type d | sed 's|^\./||' | sort)
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
