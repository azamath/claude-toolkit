---
description: Patterns for localizing SwiftUI views using String(localized:) and String Catalog. Apply when writing or editing SwiftUI views that contain hardcoded user-facing strings. Covers key naming, translator comments, and what to skip.
---

Use `String(localized:defaultValue:)` to give each user-facing string an explicit key. This feeds Xcode's String Catalog for translation while keeping the English default inline as a readable fallback.

## Pattern

```swift
// BEFORE
Text("Keep track of all your important events")

// AFTER (self-explanatory — no comment needed)
Text(String(localized: "events.list.subtitle",
           defaultValue: "Keep track of all your important events"))

// AFTER (ambiguous — comment adds value for translators)
Text(String(localized: "events.share.action",
           defaultValue: "Save",
           comment: "Means 'bookmark this event', not persist changes"))

// String interpolation — wrap when static text surrounds a variable
Text(String(localized: "events.detail.sharedWith",
           defaultValue: "Shared with \(count) people"))
```

## Key Naming Convention

Use dot-separated hierarchy: `{feature}.{screen}.{element}`

Name `{element}` by **semantic meaning** — what the string says or represents. Use a role (`title`, `subtitle`, `placeholder`) only to disambiguate multiple strings on the same screen.

- `events.details.noReminders` — describes content
- `import.contacts.subtitle` — role distinguishes it from `import.contacts.title`
- `paywall.restore.restorePurchases` — what the button says, not `button`

## When to Add `comment`

Only add `comment` when it provides information a translator can't infer from the key + defaultValue:

- **Ambiguous short words** — `"Save"`, `"Set"`, `"Post"` where meaning depends on context
- **Placeholders** — `"Shared with %lld people"` → explain what the variable represents
- **Length constraints** — e.g., "Shown in widget, keep under 20 chars"
- **Identical defaultValues** — two different `"Done"` buttons where context differs

If the key and defaultValue already make the meaning obvious, omit `comment`.

## Opting Out of Localization

Xcode extracts all string literals in SwiftUI views into the String Catalog — including strings inside `#if DEBUG` and `#Preview` blocks. To prevent non-user-facing strings from polluting the catalog, explicitly opt them out. Use `verbatim:` for `Text`; wrap in `String(...)` for components that don't support `verbatim:` (`Button`, `Label`, `Menu`, etc.).

**Skeleton / non-visible views** — redacted views, hidden layout placeholders, or other views where the text is never displayed.

```swift
Text(verbatim: "Placeholder name")
    .redacted(reason: .placeholder)

Button(String("Skeleton action")) { ... }
    .hidden()
```

**Debug and preview strings** — anything inside `#if DEBUG`, `#Preview` blocks, or debug-only files.

```swift
#if DEBUG
Text(verbatim: "Debug: \(viewModel.state)")
#endif

#Preview {
    Text(verbatim: "Preview placeholder")
}
```

## What to Skip

**Standard short labels** — SwiftUI auto-localizes these via `LocalizedStringKey`. Xcode extracts them to the String Catalog once, naturally deduplicated across all screens. If a label is ambiguous in context, wrap it — see "When to Add `comment`" above.

```swift
// CORRECT — leave as plain string
Button("Cancel") { ... }
Button("Done") { ... }
// Common labels: "Cancel", "Save", "Delete", "Done", "OK", "Retry", "Edit", "Close", "Back", "Next"
```

**Dynamic values** — strings that are purely computed with no translatable static text. If static text surrounds a variable (e.g., `"Shared with \(count) people"`), that's translatable — wrap it using the interpolation pattern above.

```swift
// Skip — no translatable content
Text(user.name)
Text(event.formattedDate)
Text("\(score)")
```

**Asset identifiers** — SF Symbol names, image/asset catalog names, and other non-displayed identifiers.

```swift
// Skip — not displayed as text to the user
Image(systemName: "calendar.badge.plus")
Image("onboarding-hero")
```
