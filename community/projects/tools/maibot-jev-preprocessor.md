# MaiBot Jev Preprocessor (MaiBot plugin where Jev drops irrelevant memories and flags factual questions before the Planner runs; Chinese)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MaiBot SDK2 plugin that runs just before the Planner request: Jev judges each injected heuristic memory and removes it only when two separate signals agree it is irrelevant, and adds a fixed-wording marker when the chat depends on external facts. It never writes replies or sends messages. Separate from maibot-jev-gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CharTyr/MaiBot-JevPreprocessor) |
| Maintainer | [CharTyr](https://github.com/CharTyr). Independently curated. |
| Format | MaiBot plugin (Python) |
| Requirements | MaiBot with SDK2 plugins; a Jev API key (`api.typesafe.ai` by default). |
| License | [GPL-3.0](https://github.com/CharTyr/MaiBot-JevPreprocessor/blob/13ca088e6625a3e4f5fb51c835d3f60885258b41/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`client.py`](https://github.com/CharTyr/MaiBot-JevPreprocessor/blob/13ca088e6625a3e4f5fb51c835d3f60885258b41/client.py) at the pinned commit. |

## When to use

- Keep a MaiBot group-chat bot's Planner from acting on loosely matched memories.
- Mismatch: docs are in Chinese; it is off by default and does nothing outside MaiBot.

## How it works

`client.py` posts the Planner's assembled window to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) with per-memory noul and choice questions; fixed thresholds in code decide drops, with request merging, a SHA-256 cache and a circuit breaker so failures leave the request unchanged. Integration evidence: [`client.py`](https://github.com/CharTyr/MaiBot-JevPreprocessor/blob/13ca088e6625a3e4f5fb51c835d3f60885258b41/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
cd plugins/
git clone https://github.com/CharTyr/MaiBot-JevPreprocessor.git CharTyr_JevPreprocessor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese) with config and stats format: [github.com/CharTyr/MaiBot-JevPreprocessor#readme](https://github.com/CharTyr/MaiBot-JevPreprocessor#readme)

## Limits and data handling

Chat windows and memory text are sent to TypeSafe or the configured compatible service; the client never logs request bodies or keys. GPL-3.0. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 13ca088e6625](https://github.com/CharTyr/MaiBot-JevPreprocessor/tree/13ca088e6625a3e4f5fb51c835d3f60885258b41). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
