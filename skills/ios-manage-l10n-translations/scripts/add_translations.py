#!/usr/bin/env python3
"""
Add translations for a language to Localizable.xcstrings.

Usage:
    python3 add_translations.py [--overwrite] <lang_code> <translations_json> <xcstrings_path>

    --overwrite:        Replace existing translations instead of skipping them
    lang_code:          ISO 639-1 language code (e.g., "ja", "ru", "zh-Hans")
    translations_json:  Path to a JSON file mapping string keys to translated values

The translations JSON file should look like:
{
    "Cancel": "Отмена",
    "Save": "Сохранить",
    "Add\nPhoto": "Добавить\nФото",
    "event.status.inDays": {
        "plural": {
            "one": "Через %lld день",
            "few": "Через %lld дня",
            "many": "Через %lld дней",
            "other": "Через %lld дней"
        }
    }
}

Values can be:
- A string for simple translations (stringUnit)
- A dict with "plural" key for plural variations
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

    if isinstance(value, str):
        # Simple string translation
        data["strings"][key]["localizations"][lang_code] = {
            "stringUnit": {"state": "translated", "value": value}
        }
    elif isinstance(value, dict) and "plural" in value:
        # Plural variations
        plural_forms = value["plural"]
        plural_units = {}
        for category, text in plural_forms.items():
            plural_units[category] = {
                "stringUnit": {"state": "translated", "value": text}
            }
        data["strings"][key]["localizations"][lang_code] = {
            "variations": {"plural": plural_units}
        }
    else:
        print(f"  WARN: unrecognized value format for key: {repr(key)}")
        continue

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
