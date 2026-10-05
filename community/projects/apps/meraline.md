# Meraline

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Mac ⌥Space assistant for any app with a Decision mode: ask yes/no, choice or level questions about selected text and get Jev (direct or via OpenRouter) or local decision-model answers with how sure they are.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Meldiron/meraline) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [GitHub releases](https://github.com/Meldiron/meraline/releases/latest) (signed, notarized DMG; Homebrew cask `meldiron/tap/meraline`). |
| Pricing and access | Free MIT app download; bring your own provider keys (TypeSafe or OpenRouter for Jev) or local Ollama models; provider usage billed separately. Checked 2026-10-06. |
| Jev evidence | [README](https://github.com/Meldiron/meraline/blob/ad255492fe91fa411b4ae37ec03436a9668c23f3/README.md) Decision mode and provider table, plus `Meraline/Providers/DecisionClient.swift` and `Meraline/Chat/Decision.swift` with tests; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [Meldiron](https://github.com/Meldiron). Independently curated. |
| Format | Native macOS app (Swift) |
| Platform and availability | macOS; distributed as a signed/notarized DMG and Homebrew cask. |
| Jev's role | Decision mode only: Jev (or another System One model) answers typed questions about the provided text; chat, rewrites and agents use other providers. |
| Requirements | A Mac; for Jev a TypeSafe or OpenRouter key stored in Keychain (or Ollama with Nimble/Tev1 locally). |
| License | [MIT](https://github.com/Meldiron/meraline/blob/ad255492fe91fa411b4ae37ec03436a9668c23f3/LICENSE). |

## When to use

- Triage text from any Mac app in a keystroke: "Is this urgent?", "Which team should handle this?", "How high a priority is this?".
- Ask the same question about each line of a list and see Yes / No / Not sure groups with confidence.
- Mismatch: for long-form answers use Meraline's chat providers; Decision mode returns probabilities, not text.

## How it works

In Decision mode (⌘3) Meraline sends your question and the optional selected or copied text to the chosen decision provider — TypeSafe's Jev directly or through OpenRouter, other OpenRouter System One models, or Nimble/Tev1 via Ollama — and shows the answer with its probability; custom answers and ordered levels map to choice and score questions. API keys live in Keychain and conversations stay in memory.

## Get started

Install the app, add a TypeSafe or OpenRouter key in Settings, and press ⌥Space → ⌘3 (live calls per question):

```sh
brew install --cask meldiron/tap/meraline
# Settings → providers → TypeSafe (or OpenRouter) key
# ⌥ Space, ⌘ 3, ask: "Is this urgent?"
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README screenshots of Decision mode (yes/no with confidence, named answers, ordered levels, per-line decisions).
- `MeralineTests/DecisionTests.swift` and `LiveDecisionTests.swift`.

## Limits and data handling

Selected text goes to the chosen provider. Usage figures shown in the app use OpenRouter's public prices and are estimates. macOS only; not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit ad255492fe91](https://github.com/Meldiron/meraline/tree/ad255492fe91fa411b4ae37ec03436a9668c23f3). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
