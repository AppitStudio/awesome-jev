# Model Picker by Tatendaz (Jev model and effort suggestions for Codex and Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for Codex and Claude Code that, as a task grows harder, asks Jev which of the host's models and effort levels fit the work and shows the recommendation in chat; it never changes a setting, keeps its state local and uses only the Python standard library.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Tatendaz/model-picker) |
| Maintainer | [Tatendaz](https://github.com/Tatendaz). Independently curated. |
| Format | Codex and Claude Code plugin (Python, standard library) |
| Requirements | macOS or Linux, Python 3.9+; a TypeSafe API key in `TYPESAFE_API_KEY` or the macOS Keychain, billed separately from your Codex or Claude plan. |
| License | [MIT](https://github.com/Tatendaz/model-picker/blob/5f04c938049f536d67aaaaa31b843e2b2284d724/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/codex-model-advisor/scripts/advisor.py`](https://github.com/Tatendaz/model-picker/blob/5f04c938049f536d67aaaaa31b843e2b2284d724/plugins/codex-model-advisor/scripts/advisor.py) at the pinned commit. |

## When to use

- Get a nudge to switch to a lighter or heavier model as a session changes scope.
- Keep model choice manual while still getting a second opinion per task.
- Mismatch: suggestions only; you switch models yourself. Distinct from the separately listed AI Model Picker app.

## How it works

`plugins/codex-model-advisor/scripts/advisor.py` sends a summary of the task with the host's available models and effort levels as typed questions to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) and renders the chosen pair as a chat note. Integration evidence: [`plugins/codex-model-advisor/scripts/advisor.py`](https://github.com/Tatendaz/model-picker/blob/5f04c938049f536d67aaaaa31b843e2b2284d724/plugins/codex-model-advisor/scripts/advisor.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
# Codex
codex plugin marketplace add Tatendaz/model-picker
codex plugin add codex-model-advisor@model-picker
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Tatendaz/model-picker#readme](https://github.com/Tatendaz/model-picker#readme)

## Limits and data handling

Task summaries and the list of host models go to TypeSafe on each check. Plugin state stays on your machine.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 5f04c938049f](https://github.com/Tatendaz/model-picker/tree/5f04c938049f536d67aaaaa31b843e2b2284d724). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
