# Known Issues & Gaps

Limitations of the current add-language approach.

Priority: `P0` = fix before next use, `P1` = fix soon, `P2` = nice to have

## ~~P0: Data Safety~~ FIXED

- ~~**No backup before modification**~~ — `add_translations.py` now backs up to `temp/Localizable.xcstrings.backup` before modifying. Auto-restores on write failure.

## ~~P0: Translation Context~~ FIXED

- ~~**Existing comments not surfaced**~~ — `extract_keys.py` now outputs English values and comments as context JSON. The LLM reads this before translating.
- `extract_keys.py --template <lang>` generates a template with only untranslated keys.

## ~~P1: Project File Automation~~ FIXED

- ~~**`knownRegions` edit is manual**~~ — `add_known_region.py` automates this. Auto-quotes hyphenated codes, skips duplicates.

## P2: Incremental Updates

- **No workflow for translating new strings only** — If 20 new strings are added next week, there's no way to translate just the delta. The temp JSON is already deleted. (Partially mitigated: `extract_keys.py --template <lang>` already outputs only untranslated keys.)
- ~~**No overwrite/update mode**~~ — `add_translations.py --overwrite` now replaces existing translations instead of skipping them.

## ~~P1: Pluralization & Variations~~ FIXED

- ~~**Only handles simple `stringUnit`**~~ — Scripts are now schema-agnostic. `add_translations.py` passes through any xcstrings localization structure as-is (plain strings auto-wrapped in `stringUnit`). `extract_keys.py --template` copies the English localization structure, blanks values, and adjusts plural categories for the target language.
- ~~**Complex plural forms ignored**~~ — `extract_keys.py` auto-detects `%lld`/`%d` strings and generates correct CLDR plural categories per language. `verify_coverage.py` recursively detects `stringUnit` at any nesting depth.

## P2: Translation Quality

- **Quality degrades at scale** — Translating hundreds of strings in one pass, especially for languages the LLM is weaker in (Thai, Hindi, Arabic), leads to lower quality.
- **No native speaker review step** — There's no built-in workflow for human review of generated translations.

## ~~P2: String Substitutions~~ FIXED

- ~~**No positional format specifier reordering**~~ — Scripts are now schema-agnostic pass-throughs. Substitutions, positional specifiers, and any xcstrings structure are preserved as-is from the template and written directly. The template copies the English localization structure (including `substitutions` keys) and blanks values for the translator to fill in.

## P2: Verification Gaps

- **Build-only validation** — A build confirms valid JSON and compilation, but doesn't verify translations display correctly — truncated labels, overlapping text, or broken layouts with longer translations are not caught.
- **Stale keys possible** — Keys are extracted from `.xcstrings`, but if strings were just added in code and the project hasn't been built in Xcode, they won't appear in the catalog yet.

## P2: RTL Languages

- **No layout verification for RTL** — Arabic and Hebrew are in the language table, but there's no step to verify the UI mirrors correctly. Adding translations is only half the work.

## P2: Xcode Conflicts

- **No Xcode-open safety check** — If Xcode is open while the script modifies `.xcstrings`, Xcode may overwrite changes or conflict on next save.
