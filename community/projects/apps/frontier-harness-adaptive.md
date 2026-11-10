# Frontier (desktop coding-agent harness that routes each turn with a Jev classifier)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Desktop workspace where one conversation about a project folder can be answered by Claude Code, Codex, Gemini or OpenCode; Adaptive mode uses TypeSafe as the classifier that picks the cheapest capable agent per message.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SecondStageTurbine/FrontierHarness) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/SecondStageTurbine/FrontierHarness#readme) (source-built; no separate product site verified). |
| Pricing and access | Free download/source; no license file on the reviewed commit. Agent subscriptions and TypeSafe usage are separate. Checked 2026-11-10. |
| Jev evidence | [`backend/adaptive.py`](https://github.com/SecondStageTurbine/FrontierHarness/blob/cba28627363a6a012dd2e51c0d0d5c7b6d5dbd8d/backend/adaptive.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [SecondStageTurbine](https://github.com/SecondStageTurbine). Independently curated. |
| Format | Tauri desktop app with Python backend (source plus GitHub release builds) |
| Platform and availability | Windows and Linux (GitHub release builds: setup.exe, AppImage, .deb; v0.27.78 at review) or source build |
| Jev's role | Jev classifies each message's needs so Adaptive mode can route it to the cheapest capable agent. |
| Requirements | Windows or Linux (x64 builds), the coding-agent CLIs you want to use, and a TypeSafe API key for the TypeSafe classifier (or a local Ollama model instead). |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Let a router pick which coding agent handles each message by need and cost.
- See Jev used as a classifier that never answers itself.
- Mismatch: no license file (source-available only); no macOS build in the reviewed release.

## How it works

`backend/adaptive.py` asks TypeSafe (`jev-latest`) fixed typed questions about the message (request kind, many files, concrete target, auth/data/money risk, effort) and matches them against per-agent capability profiles, escalating up to two rungs on failure. TypeSafe never takes a turn. Integration evidence: [`backend/adaptive.py`](https://github.com/SecondStageTurbine/FrontierHarness/blob/cba28627363a6a012dd2e51c0d0d5c7b6d5dbd8d/backend/adaptive.py).

## Get started

Download the latest Windows or Linux build from the repo's GitHub releases or run from source, connect agents, add the "TypeSafe (classifier)" provider and pick Adaptive.

```sh
git clone https://github.com/SecondStageTurbine/FrontierHarness.git
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Verification notes: [github.com/SecondStageTurbine/FrontierHarness/blob/cba28627363a6a012dd2e51c0d0d5c7b6d5dbd8d/docs/verification.md](https://github.com/SecondStageTurbine/FrontierHarness/blob/cba28627363a6a012dd2e51c0d0d5c7b6d5dbd8d/docs/verification.md)

## Limits and data handling

Message text and repo context go to TypeSafe on your key when Adaptive uses the TypeSafe classifier.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit cba28627363a](https://github.com/SecondStageTurbine/FrontierHarness/tree/cba28627363a6a012dd2e51c0d0d5c7b6d5dbd8d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
