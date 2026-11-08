# Waku Agent (local-first agent harness where TypeSafe Jev decides which memories earn a slot)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first AI agent harness (loop, memory, integrations) with an optional `WAKU_SLOT_GATE=jev` mode where TypeSafe Jev picks which memories enter each answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ShenSeanChen/waku-agent) |
| Maintainer | [ShenSeanChen](https://github.com/ShenSeanChen). Independently curated. |
| Format | Python agent harness (MIT) |
| Requirements | Python, a chat model provider and a TypeSafe API key for the Jev slot gate. |
| License | [MIT](https://github.com/ShenSeanChen/waku-agent/blob/4b69b321324750f231fdfd72a83b38ad7301dcc3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`waku/memory/jev.py`](https://github.com/ShenSeanChen/waku-agent/blob/4b69b321324750f231fdfd72a83b38ad7301dcc3/waku/memory/jev.py) at the pinned commit. |

## When to use

- Filter long-term memory before it reaches the prompt.
- Own your agent harness locally.
- Mismatch: Jev gate is opt-in; default gate does not call TypeSafe.

## How it works

`waku/memory/slot_gate.py` and `waku/memory/jev.py` ask Jev whether each memory candidate belongs in the context (threshold 0.5); `lab/jev-system-one` holds the cases used to tune it. Integration evidence: [`waku/memory/jev.py`](https://github.com/ShenSeanChen/waku-agent/blob/4b69b321324750f231fdfd72a83b38ad7301dcc3/waku/memory/jev.py).

## Get started

Install per README, set `TYPESAFE_API_KEY` and `WAKU_SLOT_GATE=jev` in `.env` (see `docs/integrations.md`).

```sh
git clone https://github.com/ShenSeanChen/waku-agent.git && cd waku-agent
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ShenSeanChen/waku-agent/blob/4b69b321324750f231fdfd72a83b38ad7301dcc3/README.md](https://github.com/ShenSeanChen/waku-agent/blob/4b69b321324750f231fdfd72a83b38ad7301dcc3/README.md)

## Limits and data handling

Memory candidates and the question are sent to TypeSafe when the Jev gate is on.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 4b69b3213247](https://github.com/ShenSeanChen/waku-agent/tree/4b69b321324750f231fdfd72a83b38ad7301dcc3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
