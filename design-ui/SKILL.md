---
name: design-ui
description: Design and check any screen a user sees — phone first, languages and right-to-left, light and dark, touch targets and whole-area taps, accessibility — in a browser or a native app. Use when building, changing or reviewing a user interface.
---

# Design UI

## Defaults

The owner's preferences, used unless the project or the request says otherwise:

1. **Mobile first**: design for the phone (390px) first, then widen with min-width breakpoints.
2. **Whole-area taps**: judge each row, card or tile on its own: what would a person expect to tap there? Most that open something open from their whole area (name, empty space, padding), not only through a small badge, chip or text; a chip with its own action sits beside that tap area. Where a whole-area tap would be wrong (a row holding a form control, several equal actions), don't. Put this rule in every brief and review that touches a screen.
3. Touch targets of at least 44px on the phone; the page never scrolls sideways; nothing fixed covers content or another control.
4. Every language the project ships, with right-to-left laid out properly where one is right-to-left; light and dark where the project has both.
5. Accessibility as the platform reports it, not as the markup claims.
6. The project's own design system and components first (in a Lynx app, `@lynx-js/lynx-ui`), before anything new or native; a separate app (an admin or backoffice) keeps its own look.

## Agree once per project

Read the project's rules first (`AGENTS.md`, `CLAUDE.local.md`, its design docs, the request). If they settle the UI, they win. If not, show the defaults as one short list and ask: "Use these, or change any?" No answer, or "go", means the defaults. Write the outcome into the project's rules so it is never asked again. An exception for one screen is noted for that screen only.

## Check before calling it done

Open every changed screen for real and look at the screenshots yourself, using [`references/checks.md`](references/checks.md): a browser for web screens; the iOS Simulator and an Android emulator for a native app (tap through it, do not only render it). Put the same checks in the brief so the builder runs them first. Say which checks you could not run (a real phone, a gesture the tooling cannot make).

## Done

Done when every changed screen passes `references/checks.md` at every size, language and theme the project ships, or the gaps are reported to the owner.
