# Jev Mail Classifier

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Classify IMAP inbox messages with Jev yes/no category judgments, then tag, move, flag, or notify from a Textual TUI and CLI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/parth-kp/jev-mail-classifier) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/parth-kp/jev-mail-classifier#readme) — local CLI/TUI; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Requires a Jev provider key (`TYPESAFE_API_KEY`, `OPENROUTER_API_KEY`, or Vercel AI Gateway) plus IMAP credentials (often an app password). Provider and mailbox host usage can incur charges. |
| Jev evidence | Inspected [jev_mail/classify.py](https://github.com/parth-kp/jev-mail-classifier/blob/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/jev_mail/classify.py) and [jev_mail/providers/typesafe_direct.py](https://github.com/parth-kp/jev-mail-classifier/blob/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/jev_mail/providers/typesafe_direct.py): one System One request with a Noul question per configured category. Offline pytest suite mocks providers. Live mailbox classification was not run. |
| Disclosure | Free source access does not include inference or IMAP hosting. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [parth-kp](https://github.com/parth-kp). |
| Format | Python package (`jev-mail-classifier` 0.1.0) with Textual setup TUI, IMAP client, and cron-friendly CLI. |
| Platform and availability | Source build on Python 3.10+. Linux/macOS-oriented; Windows not verified here. Experimental local tool—mailbox credentials and processed-state files stay on the machine that runs it. |
| Jev's role | Answers one Noul probability per configured category against a compact email state string; application code thresholds those scores and performs IMAP actions (tag/move/flag) or webhooks. |
| Requirements | Python 3.10+, IMAP host access, and one of the supported Jev keys. Optional webhook destinations for notify actions. |
| License | [MIT](https://github.com/parth-kp/jev-mail-classifier/blob/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/LICENSE). |

## When to use

Use it to keep a personal or small-team inbox sorted with plain-language categories (for example “receipts”, “security alerts”) without writing chat-completion prompts per message. Prefer a simpler IMAP filter or vendor rules when you do not need calibrated Jev probabilities or a local TUI.

## How it works

`install.sh` creates a local venv and opens the Textual wizard for credentials and categories. Classification builds a state string from mailbox metadata/body excerpts, then [classify](https://github.com/parth-kp/jev-mail-classifier/blob/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/jev_mail/classify.py) asks the selected provider for one Noul per category. The TypeSafe direct client posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Matched categories drive configured actions. `run --dry-run` reports intended actions without mutating the mailbox; `watch` uses IMAP IDLE.

## Get started

```sh
git clone https://github.com/parth-kp/jev-mail-classifier.git
cd jev-mail-classifier
git checkout 942bbba6ecfe97ee9d1ae96aedfddc1467b40990
./install.sh
./jev-mail run --dry-run
```

Live `run` / `watch` send email-derived state to the chosen Jev provider and can modify the mailbox. Provider charges apply. Use app passwords where the IMAP host requires them; do not commit `.env` or `config.yaml`.

Offline tests (no keys or mailbox required):

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
pytest -q
```

## Examples and demos

- Upstream [demo GIF/MP4](https://github.com/parth-kp/jev-mail-classifier/tree/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/media) and TUI screenshots illustrate setup; they are upstream recordings, not this catalog's execution.
- [tests/](https://github.com/parth-kp/jev-mail-classifier/tree/942bbba6ecfe97ee9d1ae96aedfddc1467b40990/tests): config, classify, mailbox, actions, providers, CLI, and TUI coverage with mocks.

## Limits and data handling

Email-derived state (subject/body excerpts as constructed by the client) goes to TypeSafe, OpenRouter, or Vercel AI Gateway depending on which key is configured. IMAP credentials stay local. Thresholds are operational policy, not measured classification accuracy. Destructive mailbox moves should be dry-run first. Direct TypeSafe path is marked upstream as less live-verified than OpenRouter in README notes—treat provider choice carefully.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 942bbba](https://github.com/parth-kp/jev-mail-classifier/tree/942bbba6ecfe97ee9d1ae96aedfddc1467b40990): package **0.1.0**, MIT. AI-assisted source review of classify/providers/TUI paths, license, and README. On Python 3.13.5 with a local venv, **`pytest`: 61 passed**. No live IMAP, TypeSafe, OpenRouter, or webhook calls were performed.

Related: [Testimonial miner](../tools/testimonial-miner.md) also judges email text with Jev, focused on extracting praise rather than inbox routing.
