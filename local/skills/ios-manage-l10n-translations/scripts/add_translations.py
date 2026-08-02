#!/usr/bin/env python3
"""
Add translations for a language to Localizable.xcstrings.

Usage:
    python3 add_translations.py [--overwrite] <lang_code> <translations_json> <xcstrings_path>

    --overwrite:        Replace existing translations instead of skipping them
    lang_code:          ISO 639-1 language code (e.g., "ja", "ru", "zh-Hans")
    translations_json:  Path to a JSON file mapping string keys to translated values

The translations JSON maps each key to its xcstrings localization value — the
exact JSON that goes under strings.<key>.localizations.<lang>.  Any structure
Xcode supports (stringUnit, variations, substitutions, etc.) works as-is.

As a convenience, a plain string is auto-wrapped in a stringUnit:

{
    "Cancel": "Отмена",
    "Save": "Сохранить",
    "event.status.inDays": {
        "variations": {
            "plural": {
                "one":   { "stringUnit": { "state": "translated", "value": "Через %lld день" } },
                "few":   { "stringUnit": { "state": "translated", "value": "Через %lld дня" } },
                "many":  { "stringUnit": { "state": "translated", "value": "Через %lld дней" } },
                "other": { "stringUnit": { "state": "translated", "value": "Через %lld дней" } }
            }
        }
    }
}
"""

import json
import os
import shutil
import sys

# Parse --overwrite flag
args = sys.argv[1:]
overwrite = False
if "--overwrite" in args:
    overwrite = True
    args.remove("--overwrite")

if len(args) < 3:
    print("Usage: python3 add_translations.py [--overwrite] <lang_code> <translations_json> <xcstrings_path>")
    sys.exit(1)

lang_code = args[0]
translations_path = args[1]
xcstrings_path = args[2]
backup_path = os.path.join("temp", "Localizable.xcstrings.backup")

# Load translations
with open(translations_path, "r", encoding="utf-8") as f:
    translations = json.load(f)

# Load existing xcstrings
with open(xcstrings_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Backup before modification
os.makedirs(os.path.dirname(backup_path), exist_ok=True)
shutil.copy2(xcstrings_path, backup_path)
print(f"Backup saved to {backup_path}")

# Add translations
added = 0
overwritten = 0
skipped_missing = 0
skipped_exists = 0

for key, value in translations.items():
    if key not in data["strings"]:
        skipped_missing += 1
        print(f"  WARN: key not in xcstrings, skipped: {repr(key)}")
        continue

    if "localizations" not in data["strings"][key]:
        data["strings"][key]["localizations"] = {}

    is_overwrite = lang_code in data["strings"][key]["localizations"]
    if is_overwrite and not overwrite:
        skipped_exists += 1
        continue

    # Plain string shorthand: auto-wrap in stringUnit
    if isinstance(value, str):
        value = {"stringUnit": {"state": "translated", "value": value}}

    # Pass-through: value is the raw xcstrings localization blob
    data["strings"][key]["localizations"][lang_code] = value

    if is_overwrite:
        overwritten += 1
    else:
        added += 1

# Save with restore on failure
try:
    with open(xcstrings_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ' : '))
except Exception as e:
    print(f"ERROR: Failed to write — restoring from backup: {e}")
    shutil.copy2(backup_path, xcstrings_path)
    sys.exit(1)

print(f"Added {added} translations for '{lang_code}'")
if overwritten:
    print(f"Overwritten {overwritten} (replaced existing)")
if skipped_exists:
    print(f"Skipped {skipped_exists} (already translated)")
if skipped_missing:
    print(f"Skipped {skipped_missing} (key not found in xcstrings)")
print(f"To revert: cp {backup_path} {xcstrings_path}")
