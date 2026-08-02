#!/bin/bash

# Claude Toolkit Local Uninstallation Script
# Removes individual symlinks pointing back into this toolkit

set -e

TOOLKIT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_DIR="${TOOLKIT_DIR}/local"
CLAUDE_CONFIG_DIR="${HOME}/.claude"

echo "Claude Toolkit Local Uninstaller"
echo "================================"
echo ""

# Remove a symlink only if it points into this toolkit
# $1 = path relative to CLAUDE_CONFIG_DIR
unlink_item() {
    local rel="$1"
    local target="${CLAUDE_CONFIG_DIR}/${rel}"

    if [ -L "${target}" ]; then
        local dest
        dest="$(readlink "${target}")"
        case "${dest}" in
            "${TOOLKIT_DIR}"/*)
                rm "${target}"
                echo "✓ Removed: ${rel}"
                ;;
            *)
                echo "- Skipping (not ours): ${rel} -> ${dest}"
                ;;
        esac
    elif [ -e "${target}" ]; then
        echo "⚠ Exists but is not a symlink, skipping: ${rel}"
    else
        echo "- Not installed: ${rel}"
    fi
}

# Remove links for a component, mirroring what install-local.sh created
# $1 = component dir, $2 = find expression type ("files" or "dirs")
uninstall_component() {
    local component="$1"
    local kind="$2"

    [ -d "${LOCAL_DIR}/${component}" ] || return 0
    echo "${component}:"

    local found=0
    if [ "${kind}" = "files" ]; then
        while IFS= read -r file; do
            found=1
            unlink_item "${component}/${file}"
        done < <(cd "${LOCAL_DIR}/${component}" && find . -type f -name '*.md' | sed 's|^\./||' | sort)
    else
        while IFS= read -r dir; do
            found=1
            unlink_item "${component}/${dir}"
        done < <(cd "${LOCAL_DIR}/${component}" && find . -mindepth 1 -maxdepth 1 -type d | sed 's|^\./||' | sort)
    fi
    [ "${found}" -eq 0 ] && echo "- none found"

    # Prune directories we may have created, deepest first, only if empty
    if [ -d "${CLAUDE_CONFIG_DIR}/${component}" ] && [ ! -L "${CLAUDE_CONFIG_DIR}/${component}" ]; then
        find "${CLAUDE_CONFIG_DIR}/${component}" -depth -type d -empty -delete 2>/dev/null || true
    fi
    echo ""
}

echo "Uninstalling components..."
echo ""

uninstall_component "commands" files
uninstall_component "agents" files
uninstall_component "skills" dirs

echo "Uninstallation complete!"
