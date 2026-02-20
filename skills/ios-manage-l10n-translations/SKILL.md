---
name: ios-manage-l10n-translations
description: Manage translations in an iOS app using Xcode String Catalogs (.xcstrings). Add a new language, translate missing strings, or update existing translations.
user-invocable: true
allowed-tools: Bash, Read, Edit, Write, Grep, Glob
argument-hint: <language name, e.g. "Japanese", "Russian">
---

# Manage Translations

Manage translations in an iOS app that uses Xcode String Catalogs (`.xcstrings`). Takes language name as argument (e.g., "Japanese", "Chinese", "Italian").

**Scripts:** All `scripts/` paths in this document are relative to this skill's directory (the directory containing this SKILL.md).

## Workflows

This skill handles three scenarios — the agent determines which one applies automatically:

| Scenario | When | What happens |
|----------|------|--------------|
| **Add new language** | Language has no translations yet | Full flow: translate all strings, register language in Xcode project |
| **Translate missing strings** | Language exists but has gaps | Translate only untranslated keys |
| **Update existing translations** | User explicitly asks to fix/redo translations | Re-translate with `--overwrite` |

## Usage

```
/ios-manage-l10n-translations Japanese
/ios-manage-l10n-translations Chinese (Simplified)
/ios-manage-l10n-translations Russian
```

## Steps

### 0. Discover Project Paths

Use the Glob tool to find the two required files:
- `**/Localizable.xcstrings` — the String Catalog
- `**/*.xcodeproj/project.pbxproj` — the Xcode project file

If either glob returns zero or multiple matches, ask the user which path to use. Store the results as `$XCSTRINGS_PATH` and `$PBXPROJ_PATH` for all subsequent steps.

### 1. Determine Workflow

Run the template command to check current state:

```bash
python3 scripts/extract_keys.py $XCSTRINGS_PATH --template <LANG_CODE>
```

This outputs only untranslated keys. Based on the result:

- **Empty output `{}`** — language is fully translated. If the user wants to update/fix translations, proceed with the **update** workflow (use `--overwrite` in Step 3).
- **Output has keys** — proceed to translate them. If this is a new language (no existing translations at all), also run Step 5 (register in Xcode).

### 2. Extract Context

Extract string keys with context (English values and comments) to understand what each string means:

```bash
python3 scripts/extract_keys.py $XCSTRINGS_PATH
```

This outputs a JSON like:
```json
{
  "Cancel": { "en": "Cancel", "comment": "Button to dismiss" },
  "items_count_%lld": { "en": "%lld items", "comment": "Number of items in a list", "needs_plural": true }
}
```

Read this output carefully — use the `en` value and `comment` to understand what each string means before translating.

### 3. Create Translations JSON and Apply

Fill in the template from Step 1 with translations and save as `temp/translations_<language_code>.json`:

```json
{
    "Cancel": "<translated>",
    "Done": "<translated>",
    "Delete\nAll": "<translated>\n<translated>"
}
```

Then apply translations:

```bash
python3 scripts/add_translations.py <LANG_CODE> temp/translations_<language_code>.json $XCSTRINGS_PATH
```

For the **update** workflow (re-translating existing strings), add `--overwrite`:

```bash
python3 scripts/add_translations.py --overwrite <LANG_CODE> temp/translations_<language_code>.json $XCSTRINGS_PATH
```

A backup is saved to `temp/Localizable.xcstrings.backup` before modification.

**Notes on the JSON file:**
- Must include EVERY key from the template
- Strings with newlines use literal `\n` (JSON escape)
- Preserve format specifiers exactly: `%@`, `%lld`, `%d`, `%.2f`
- Preserve interpolation patterns: `\(variableName)`

### 4. Verify Translation Coverage

Check coverage for the language (shows missing keys if any):

```bash
python3 scripts/verify_coverage.py $XCSTRINGS_PATH <LANG_CODE>
```

**Target: 100% coverage.** If missing, add them to the JSON and re-run Step 3.

To see all languages at once:

```bash
python3 scripts/verify_coverage.py $XCSTRINGS_PATH
```

### 5. Register Language in Xcode (new languages only)

Skip this step if the language already existed in the project.

```bash
python3 scripts/add_known_region.py <LANG_CODE> $PBXPROJ_PATH
```

Hyphenated codes (e.g., `pt-BR`, `zh-Hans`) are automatically quoted. Skips if already present.

### 6. Clean Up

Remove the translations JSON after successful execution:
```bash
rm temp/translations_<language_code>.json
```

## Plural Forms

The xcstrings format supports `variations.plural` for count-dependent strings (e.g., "1 day" vs "5 days"). Languages like Russian (3 plural forms) and Arabic (6 forms) produce incorrect grammar without this.

### How It Works

1. `extract_keys.py` flags strings containing `%lld` or `%d` with `"needs_plural": true` in context output
2. `extract_keys.py --template <lang>` auto-generates the correct plural structure based on CLDR categories for the target language
3. `add_translations.py` accepts both simple strings and plural objects in the same JSON

### CLDR Plural Categories by Language

| Language | Code | Categories |
|----------|------|------------|
| Arabic | ar | zero, one, two, few, many, other |
| Czech | cs | one, few, many, other |
| Danish | da | one, other |
| German | de | one, other |
| English | en | one, other |
| Spanish | es | one, many, other |
| French | fr | one, many, other |
| Hebrew | he | one, two, other |
| Indonesian | id | other |
| Italian | it | one, many, other |
| Japanese | ja | other |
| Korean | ko | other |
| Norwegian | nb | one, other |
| Dutch | nl | one, other |
| Polish | pl | one, few, many, other |
| Portuguese (BR) | pt-BR | one, many, other |
| Russian | ru | one, few, many, other |
| Swedish | sv | one, other |
| Thai | th | other |
| Turkish | tr | one, other |
| Ukrainian | uk | one, few, many, other |
| Vietnamese | vi | other |
| Chinese (Simplified) | zh-Hans | other |
| Chinese (Traditional) | zh-Hant | other |

### Example: Mixed Translations JSON

```json
{
    "Cancel": "Отмена",
    "items_count_%lld": {
        "plural": {
            "one": "%lld элемент",
            "few": "%lld элемента",
            "many": "%lld элементов",
            "other": "%lld элементов"
        }
    }
}
```

Simple strings use a string value; plural strings use a `{"plural": {...}}` object with one entry per CLDR category.

## Translation Guidelines

When translating:
- Keep translations natural and idiomatic, not literal
- Match the tone (formal/informal) of the original
- For button labels, keep them concise
- For error messages, be clear and helpful
- Do not translate app/brand names — keep them as-is
- Preserve format specifiers exactly: `%@`, `%lld`, `%d`, `%.2f`
- Preserve `String(localized:)` interpolation patterns: `\(variableName)`
- Preserve newlines `\n` in the same positions

## Files Modified

1. `$XCSTRINGS_PATH` (Localizable.xcstrings) — translations added/updated
2. `$PBXPROJ_PATH` (project.pbxproj) — language code in knownRegions (new languages only)

## Common Issues

**Localizable.xcstrings doesn't exist yet:**
- The project uses `String(localized:)` but no String Catalog has been created
- Open the project in Xcode, add a new file > String Catalog > name it `Localizable`
- Build once so Xcode populates it with discovered strings

**Missing translations after script runs:**
- Check if keys have special characters (newlines, quotes)
- Keys with `\n` in the JSON must use JSON-escaped newlines
- Verify the key exists in the xcstrings file (typos cause silent skips)
- The script logs warnings for keys not found in xcstrings

**Language not recognized by iOS:**
- Verify language code added to `knownRegions` in project.pbxproj
- Ensure the code matches Apple's expected format (e.g., `pt-BR` not `pt_BR`)
