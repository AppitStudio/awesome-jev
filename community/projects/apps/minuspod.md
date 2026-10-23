# MinusPod (self-hosted podcast ad remover with native System One support)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted server that transcribes podcast episodes, detects and cuts ad segments, and learns sponsor patterns from your corrections; it has a native System One adapter so Jev can run ad detection and verification.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ttlequals0/MinusPod) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/ttlequals0/MinusPod#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free to self-host. Inference uses your own provider keys. Checked 2026-10-24. |
| Jev evidence | [`src/llm_client.py`](https://github.com/ttlequals0/MinusPod/blob/875334139d929b2dda40c1e0d3adaf9169a750bf/src/llm_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ttlequals0](https://github.com/ttlequals0). Independently curated. |
| Format | Self-hosted server with web UI (Docker) |
| Platform and availability | Self-hosted via Docker (CPU multi-arch or NVIDIA GPU image). |
| Jev's role | Optional: with TypeSafe selected as the System One provider, Jev handles ad detection, verification and ad categories. |
| Requirements | Docker; GPU optional; a TypeSafe key for the Jev route (or another LLM provider). |
| License | [MIT](https://github.com/ttlequals0/MinusPod/blob/875334139d929b2dda40c1e0d3adaf9169a750bf/LICENSE) |

## When to use

- Remove ads from podcasts before playback in your own podcast app.
- Use a cheap decision model for ad detection.
- Mismatch: chapter generation and pattern cleanup are unsupported on System One routes.

## How it works

`src/llm_client.py` routes System One stages to TypeSafe's endpoint (`https://api.typesafe.ai/v1`), and the `src/systemone/` adapter turns transcript windows into typed questions. See `docs/system-one.md`. Integration evidence: [`src/llm_client.py`](https://github.com/ttlequals0/MinusPod/blob/875334139d929b2dda40c1e0d3adaf9169a750bf/src/llm_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
docker compose -f docker-compose.cpu.yml up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- System One docs: [github.com/ttlequals0/MinusPod/blob/main/docs/system-one.md](https://github.com/ttlequals0/MinusPod/blob/main/docs/system-one.md)

## Limits and data handling

Transcript windows are sent to the configured provider. The ad reviewer on System One is marked experimental.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 875334139d92](https://github.com/ttlequals0/MinusPod/tree/875334139d929b2dda40c1e0d3adaf9169a750bf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
