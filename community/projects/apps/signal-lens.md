# SignalLens

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Privacy-conscious local-first chat signal analyzer: redacts sensitive spans on-device, then TypeSafe Jev judges emotion, intent, and engagement signals for a closeness index.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xinian5216/chat-signal-analyzer) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/xinian5216/chat-signal-analyzer#readme) — Windows portable exe and Streamlit source; no separate SaaS. |
| Pricing and access | MIT source and Windows portable release; no app purchase fee, checked **2026-09-23**. Needs a TypeSafe API key (stored under portable `data/settings.env` or env for source runs). TypeSafe usage billed separately. |
| Jev evidence | Inspected [`analyzer.py`](https://github.com/xinian5216/chat-signal-analyzer/blob/4c1bac58a652036317bd0982fec23c5f1cbfc60a/analyzer.py): `typesafe_sdk` Choice/Noul/Score fan-out (nine questions per TA message) via `TypeSafeClient`. Local redaction in `privacy.py`. Windows GUI/live Jev not run on the Linux review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; portable exe, Streamlit UI, and live TypeSafe were **not** executed here. Distinct from [Crush Monitor](crush-monitor.md) / [tg-crush](tg-crush.md) (different chat surfaces and product shape). |
| Maintainer | [xinian5216](https://github.com/xinian5216). |
| Format | Python Streamlit app (**SignalLens**); Windows x64 portable zip via GitHub Releases (`SignalLens-v0.2.0-…`). |
| Platform and availability | Windows portable for end users; source build elsewhere with Python deps in `requirements.txt`. Listens on loopback (`127.0.0.1`, port 8765+). |
| Jev's role | Per-message structured judgments (emotion/intent Choices, Scores, Nouls); local code aggregates an interaction closeness signal. Jev does not rewrite chat text. |
| Requirements | TypeSafe API key. Source: `streamlit`, `typesafe-sdk`, etc. |
| License | [MIT](https://github.com/xinian5216/chat-signal-analyzer/blob/4c1bac58a652036317bd0982fec23c5f1cbfc60a/LICENSE). |

## When to use

Use it for **local analysis of chat exports** when you want typed emotion/intent signals after on-device redaction. Prefer [Crush Monitor](crush-monitor.md) for a WeChat-paste TypeScript stack, or ordinary notes when you do not want any chat text to leave the device.

## How it works

Parsing, redaction, cache, and reporting stay local. [`analyzer.py`](https://github.com/xinian5216/chat-signal-analyzer/blob/4c1bac58a652036317bd0982fec23c5f1cbfc60a/analyzer.py) sends redacted context to TypeSafe Jev with a schema-versioned question set; scores feed local formulas. Portable builds bind only to localhost.

## Get started

```sh
# Windows users: download SignalLens-v0.2.0 Windows portable zip from Releases, unzip to a writable folder, run SignalLens.exe
# Source sketch:
git clone https://github.com/xinian5216/chat-signal-analyzer.git
cd chat-signal-analyzer
git checkout 4c1bac58a652036317bd0982fec23c5f1cbfc60a
# python -m venv .venv && pip install -r requirements.txt
# set TYPESAFE_API_KEY; streamlit run app.py   # per upstream
```

## Examples and demos

- Evaluation fixtures under `evaluation/`.
- Privacy notes in `PRIVACY.md` / `SECURITY.md`.

## Limits and data handling

Redacted snippets still leave the host on live Jev calls. API key and SQLite cache stay in the app `data/` folder for portable builds. Treat closeness scores as optional reference, not relationship advice. Live analysis not run here.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 4c1bac5](https://github.com/xinian5216/chat-signal-analyzer/tree/4c1bac58a652036317bd0982fec23c5f1cbfc60a) (MIT; portable **v0.2.0** documented upstream). AI-assisted review of README, LICENSE, `analyzer.py`. No Windows/live TypeSafe run.

Related: [Crush Monitor](crush-monitor.md), [tg-crush](tg-crush.md), [Jev Chat Windows](jev-chat-windows.md).
