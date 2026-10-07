# Session Board

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local macOS panel for Codex that turns a conversation into cards of open questions, tasks and answers, with opt-in TypeSafe Jev analysis (TypeSafe API or OpenRouter's Jev endpoint) to match messages to cards; listens only on localhost and documents what is stored and sent. Docs are in Russian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kolotovalexander/session-board) |
| Maintainer | [kolotovalexander](https://github.com/kolotovalexander). Independently curated. |
| Format | Python app installed into `~/.local/share/session-board` with Codex hooks; local web panel on `127.0.0.1:60363` |
| Requirements | macOS, Git, Python 3.10+ and Codex with local session files; for analysis, a TypeSafe key (`jev-latest`) or an OpenRouter key (`typesafe/jev-1.13`). |
| License | [MIT](https://github.com/kolotovalexander/session-board/blob/173efb6aad2b6ef0b0acd7d2248ab0e605340e39/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep unanswered questions and tasks from a long Codex conversation visible beside the chat.
- Turn on Jev only for chats you open in the panel.
- Mismatch: macOS + Codex only (Claude/Hermes adapters experimental, Windows/Linux unsupported); README is Russian-only.

## How it works

[`board.py`](https://github.com/kolotovalexander/session-board/blob/173efb6aad2b6ef0b0acd7d2248ab0e605340e39/board.py) serves the local panel and, when analysis is enabled, sends cleaned and size-limited visible message fragments to the configured Jev endpoint (`/v1/systemone`) to match them to cards; [`install.py`](https://github.com/kolotovalexander/session-board/blob/173efb6aad2b6ef0b0acd7d2248ab0e605340e39/install.py) sets up the Codex hooks while preserving existing settings.

## Get started

Clone and run the installer as described in `INSTALL.md` (the README suggests asking Codex to do it), then choose a provider and key in the panel settings:

```sh
git clone https://github.com/kolotovalexander/session-board
cd session-board
python3 install.py   # see INSTALL.md for options
```

With analysis on, syncing a chat sends Jev requests billed by TypeSafe or OpenRouter; without a key the panel works locally.

## Examples and demos

- README *Первый запуск* (first run) and *Что хранится и куда уходит* (what is stored and where it goes).
- Install guide: [`INSTALL.md`](https://github.com/kolotovalexander/session-board/blob/173efb6aad2b6ef0b0acd7d2248ab0e605340e39/INSTALL.md).

## Limits and data handling

Cards and fragments are stored under `~/Library/Application Support/SessionBoard`; with analysis enabled, cleaned visible fragments go to TypeSafe or OpenRouter. Local only. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 173efb6aad2b](https://github.com/kolotovalexander/session-board/tree/173efb6aad2b6ef0b0acd7d2248ab0e605340e39). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
