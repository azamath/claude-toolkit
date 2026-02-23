#!/usr/bin/env python3
"""
Verify translation coverage in Localizable.xcstrings.

Usage:
    python3 verify_coverage.py <xcstrings_path>              # Show all languages
    python3 verify_coverage.py <xcstrings_path> <lang_code>  # Show specific language + missing keys
"""

import json
import sys

if len(sys.argv) < 2:
    print("Usage: python3 verify_coverage.py <xcstrings_path> [<lang_code>]")
    sys.exit(1)

xcstrings_path = sys.argv[1]
target_lang = sys.argv[2] if len(sys.argv) > 2 else None

with open(xcstrings_path, "r") as f:
    data = json.load(f)

total = len(data["strings"])


def _is_translated(obj):
    """Recursively check if a localization entry contains a stringUnit anywhere.

    Works for any xcstrings structure: simple stringUnit, variations.plural,
    substitutions with nested plurals, device variations, etc.
    """
    if not isinstance(obj, dict):
        return False
    if "stringUnit" in obj:
        return True
    return any(_is_translated(v) for v in obj.values())


# Collect per-language counts
langs = {}
for val in data["strings"].values():
    for lang, loc in val.get("localizations", {}).items():
        if _is_translated(loc):
            langs[lang] = langs.get(lang, 0) + 1

# Print summary
for lang, count in sorted(langs.items()):
    pct = count * 100 // total if total else 0
    status = "OK" if pct >= 99 else "WARN"
    print(f"{status} {lang}: {count}/{total} ({pct}%)")

# If a specific language was requested, show missing keys
if target_lang:
    missing = []
    for k, v in data["strings"].items():
        loc = v.get("localizations", {}).get(target_lang)
        if loc is None or not _is_translated(loc):
            missing.append(k)
    if missing:
        print(f"\nMissing {len(missing)} translations for '{target_lang}':")
        for k in sorted(missing):
            print(f"  {repr(k)}")
    else:
        print(f"\nAll strings translated for '{target_lang}'")
