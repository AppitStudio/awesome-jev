# Juger vite, bloquer juste (talk demo: a mail agent hit by prompt injection, then guarded by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Code from an IndabaX Madagascar 2026 talk: a DeepAgents + Claude mail agent attacked through prompt injection, run in two configs. In A, Jev only watches; in B, Jev quarantines mails that address the AI and blocks drafts that stray from the request or leak a secret. Includes 16 scenarios (10 attacks, 6 benign tasks), a golden set, a Jev-as-judge scorer and two replays that run without keys. French docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lorenzorama/juger-vite-bloquer-juste) |
| Maintainer | [lorenzorama](https://github.com/lorenzorama). Independently curated. |
| Format | Python backend (FastAPI) and Next.js frontend |
| Requirements | uv, Node.js 20+, an Anthropic key and a TypeSafe key (replays need none). |
| License | [MIT](https://github.com/lorenzorama/juger-vite-bloquer-juste/blob/67aae240fd36e5dd87c87ce5f4514495b794d5fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`backend/app/guard.py`](https://github.com/lorenzorama/juger-vite-bloquer-juste/blob/67aae240fd36e5dd87c87ce5f4514495b794d5fb/backend/app/guard.py) at the pinned commit. |

## When to use

- See an input and output guard for an email agent with measurable before/after results.
- Mismatch: demo with invented mailboxes; French docs.

## How it works

`backend/app/guard.py` uses `langchain_typesafe` (`TypeSafeClassifier`, `Noul`) with a pinned `jev-1.14.0` to screen incoming mails and outgoing drafts against thresholds. Integration evidence: [`backend/app/guard.py`](https://github.com/lorenzorama/juger-vite-bloquer-juste/blob/67aae240fd36e5dd87c87ce5f4514495b794d5fb/backend/app/guard.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/lorenzorama/juger-vite-bloquer-juste && cd juger-vite-bloquer-juste
cp .env.example .env   # Anthropic and TypeSafe keys
cd backend && uv sync && uv run uvicorn app.main:app --port 8010
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (French): [github.com/lorenzorama/juger-vite-bloquer-juste#readme](https://github.com/lorenzorama/juger-vite-bloquer-juste#readme)

## Limits and data handling

The agent only writes drafts to a local mailbox; mail text goes to Claude and TypeSafe in live runs.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 67aae240fd36](https://github.com/lorenzorama/juger-vite-bloquer-juste/tree/67aae240fd36e5dd87c87ce5f4514495b794d5fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
