#!/usr/bin/env python3
"""
Add a language code to knownRegions in project.pbxproj.

Usage:
    python3 add_known_region.py <lang_code> <pbxproj_path>

Hyphenated codes (e.g., pt-BR, zh-Hans) are automatically quoted.
"""

import re
import sys

if len(sys.argv) < 3:
    print("Usage: python3 add_known_region.py <lang_code> <pbxproj_path>")
    sys.exit(1)

lang_code = sys.argv[1]
pbxproj_path = sys.argv[2]

with open(pbxproj_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find knownRegions block
pattern = r"(knownRegions\s*=\s*\()([^)]*?)(\);)"
match = re.search(pattern, content, re.DOTALL)

if not match:
    print("ERROR: knownRegions not found in project.pbxproj")
    sys.exit(1)

regions_block = match.group(2)

# Check if already present (with or without quotes)
existing = re.findall(r'["\']?([^"\',\s]+)["\']?', regions_block)
if lang_code in existing:
    print(f"'{lang_code}' already in knownRegions, nothing to do")
    sys.exit(0)

# Quote if contains hyphen
entry = f'"{lang_code}"' if "-" in lang_code else lang_code

# Detect indentation from existing entries
indent_match = re.search(r"\n(\s+)\w", regions_block)
indent = indent_match.group(1) if indent_match else "\t\t\t\t"

# Insert before closing paren
new_regions = regions_block.rstrip() + f"\n{indent}{entry},\n\t\t\t"
new_content = content[:match.start(2)] + new_regions + content[match.end(2):]

with open(pbxproj_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Added '{entry}' to knownRegions")
