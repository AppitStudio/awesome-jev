# AI Model Picker

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS assistant: describe a task, review rule-ranked app/model/effort choices, and open or prepare the task in the client you already use; optional TypeSafe Jev classification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Gavinluo19/ai-model-picker) |
| Tags | `Open source` · `Free` |
| Product homepage | [github.com/Gavinluo19/ai-model-picker/releases](https://github.com/Gavinluo19/ai-model-picker/releases) |
| Pricing and access | Free MIT download; optional TypeSafe key for Jev classification. |
| Jev evidence | [`Sources/Services.swift`](https://github.com/Gavinluo19/ai-model-picker/blob/86a2a88b86193b21e72838d3fa5b1b2889821ad5/Sources/Services.swift) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [Gavinluo19](https://github.com/Gavinluo19). Independently curated. |
| Format | macOS app (Swift) |
| Platform and availability | macOS (alpha, ad hoc signed, not notarized) |
| Jev's role | Optional Jev classification of the task description feeds the ranking; offline rules work without it. |
| Requirements | macOS; optional TypeSafe key. |
| License | [MIT](https://github.com/Gavinluo19/ai-model-picker/blob/86a2a88b86193b21e72838d3fa5b1b2889821ad5/LICENSE) |

## When to use

- Decide which AI app, model and effort fits a new task before starting it.
- Mismatch: Alpha; live Jev classification still awaiting acceptance per upstream release status.

## How it works

Rules rank four app/model/effort options; when enabled, Jev classifies the task first; you choose and the app opens or copies the prompt into the client. (Summarized from the upstream [README](https://github.com/Gavinluo19/ai-model-picker/blob/86a2a88b86193b21e72838d3fa5b1b2889821ad5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): download the release from GitHub, open it past Gatekeeper, and start with offline recommendations.

## Limits and data handling

Task text goes to TypeSafe only when Jev is enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 86a2a88b8619](https://github.com/Gavinluo19/ai-model-picker/tree/86a2a88b86193b21e72838d3fa5b1b2889821ad5). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
