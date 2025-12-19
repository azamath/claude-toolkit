#!/bin/bash

# Claude Toolkit Backup Script
# Backs up existing directories in global Claude configuration

set -e

CLAUDE_CONFIG_DIR="${HOME}/.claude"
BACKUP_SUFFIX=".backup"

echo "Claude Toolkit Backup"
echo "====================="
echo ""
echo "Claude config directory: ${CLAUDE_CONFIG_DIR}"
echo ""

# Function to backup directory
backup_directory() {
    local dir_name="$1"
    local target_dir="${CLAUDE_CONFIG_DIR}/${dir_name}"
    local backup_dir="${target_dir}${BACKUP_SUFFIX}"

    if [ -L "${target_dir}" ]; then
        echo "- Skipping ${dir_name} (already a symlink)"
    elif [ -d "${target_dir}" ]; then
        if [ -e "${backup_dir}" ]; then
            echo "⚠ Warning: Backup already exists for ${dir_name}"
            echo "  Existing backup: ${backup_dir}"
            echo "  Skipping backup to avoid overwriting"
        else
            echo "Backing up: ${dir_name}"
            mv "${target_dir}" "${backup_dir}"
            echo "✓ Backed up: ${dir_name} -> ${dir_name}${BACKUP_SUFFIX}"
        fi
    elif [ -e "${target_dir}" ]; then
        echo "⚠ Warning: ${dir_name} exists but is not a directory"
        echo "  Please manually handle: ${target_dir}"
    else
        echo "- No existing ${dir_name} directory to backup"
    fi
}

# Backup each component directory
echo "Checking for existing directories to backup..."
echo ""

backup_directory "commands"
backup_directory "agents"
backup_directory "skills"

echo ""
echo "Backup complete!"
echo ""
echo "You can now run ./install.sh to create the symlinks."
echo "To restore backups later, rename the .backup directories back."
