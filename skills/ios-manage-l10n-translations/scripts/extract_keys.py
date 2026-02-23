#!/usr/bin/env python3
"""
Extract string keys with context from Localizable.xcstrings.

Usage:
    python3 extract_keys.py <xcstrings_path>                  # Print keys with context as JSON
    python3 extract_keys.py <xcstrings_path> --template <lang> # Output a translation template for a language
"""

import copy
import json
import re
import sys

# CLDR plural categories by language code
PLURAL_CATEGORIES = {
    "ar": ["zero", "one", "two", "few", "many", "other"],
    "cs": ["one", "few", "many", "other"],
    "da": ["one", "other"],
    "de": ["one", "other"],
    "el": ["one", "other"],
    "en": ["one", "other"],
    "es": ["one", "many", "other"],
    "fi": ["one", "other"],
    "fr": ["one", "many", "other"],
    "he": ["one", "two", "other"],
    "hi": ["one", "other"],
    "id": ["other"],
    "it": ["one", "many", "other"],
    "ja": ["other"],
    "ko": ["other"],
    "nb": ["one", "other"],
    "nl": ["one", "other"],
    "pl": ["one", "few", "many", "other"],
    "pt-BR": ["one", "many", "other"],
    "ru": ["one", "few", "many", "other"],
    "sv": ["one", "other"],
    "th": ["other"],
    "tr": ["one", "other"],
    "uk": ["one", "few", "many", "other"],
    "vi": ["other"],
    "zh-Hans": ["other"],
    "zh-Hant": ["other"],
}

# Parse args
template_lang = None

args = sys.argv[1:]
if "--template" in args:
    idx = args.index("--template")
    template_lang = args[idx + 1]
    args = args[:idx] + args[idx + 2:]

if not args:
    print("Usage: python3 extract_keys.py <xcstrings_path> [--template <lang>]")
    sys.exit(1)

xcstrings_path = args[0]

with open(xcstrings_path, "r", encoding="utf-8") as f:
    data = json.load(f)


def _needs_plural(en_value):
    """Check if a string contains integer format specifiers that indicate plural needs."""
    return bool(re.search(r'%(\d+\$)?l?l?d', en_value))


def _get_en_value(entry, key):
    """Get the English value for a string entry."""
    en_loc = entry.get("localizations", {}).get("en", {})
    en_unit = en_loc.get("stringUnit", {})
    return en_unit.get("value", key)


def _blank_values(obj):
    """Recursively blank out 'value' fields and set 'state' to 'translated'."""
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if k == "value" and isinstance(v, str):
                result[k] = ""
            elif k == "state":
                result[k] = "translated"
            else:
                result[k] = _blank_values(v)
        return result
    if isinstance(obj, list):
        return [_blank_values(item) for item in obj]
    return obj


def _adjust_plural_categories(obj, categories):
    """Replace plural category keys with target language's CLDR categories.

    Walks the structure looking for any 'plural' dict (top-level variations
    or inside substitutions) and replaces its keys.
    """
    if not isinstance(obj, dict):
        return
    for key, val in list(obj.items()):
        if key == "plural" and isinstance(val, dict):
            # Use 'other' (or any existing) as the shape template
            shape = val.get("other", next(iter(val.values())))
            obj[key] = {cat: copy.deepcopy(shape) for cat in categories}
        elif isinstance(val, dict):
            _adjust_plural_categories(val, categories)


def _make_template_entry(en_loc, categories):
    """Create a blank localization entry from English, adjusted for target language."""
    tmpl = _blank_values(copy.deepcopy(en_loc))
    _adjust_plural_categories(tmpl, categories)
    return tmpl


if template_lang:
    # Output a translation template in native xcstrings localization format.
    # Each value is what goes under strings.<key>.localizations.<lang>.
    # Only includes keys that don't already have this language.
    categories = PLURAL_CATEGORIES.get(template_lang, ["one", "other"])
    template = {}
    for key in sorted(data["strings"].keys()):
        entry = data["strings"][key]
        if template_lang in entry.get("localizations", {}):
            continue

        en_loc = entry.get("localizations", {}).get("en")
        if en_loc:
            # Copy English structure, blank values, adjust plural categories
            template[key] = _make_template_entry(en_loc, categories)
        else:
            # No English localization — generate from heuristics
            en_value = _get_en_value(entry, key)
            if _needs_plural(en_value):
                template[key] = {
                    "variations": {
                        "plural": {
                            cat: {"stringUnit": {"state": "translated", "value": ""}}
                            for cat in categories
                        }
                    }
                }
            else:
                template[key] = {"stringUnit": {"state": "translated", "value": ""}}
    print(json.dumps(template, ensure_ascii=False, indent=2))
else:
    # Output context JSON: key -> {en, comment, needs_plural}
    context = {}
    for key in sorted(data["strings"].keys()):
        entry = data["strings"][key]
        info = {}

        # English value: from explicit en localization, or the key itself
        en_value = _get_en_value(entry, key)
        info["en"] = en_value

        # Comment
        comment = entry.get("comment")
        if comment:
            info["comment"] = comment

        # Flag strings that need plural forms
        if _needs_plural(en_value):
            info["needs_plural"] = True

        context[key] = info

    print(json.dumps(context, ensure_ascii=False, indent=2))
