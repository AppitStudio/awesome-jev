# jet (fast coding agent built on TypeSafe Jev judgments and recursive context decomposition)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Coding agent where a small TypeSafe Jev judgment model decides in milliseconds and the large model only sees key context built by Recursive LLM Context Decomposition (RLCD); CLI plus local web UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arczhi/jet) |
| Maintainer | [arczhi](https://github.com/arczhi). Independently curated. |
| Format | Python coding agent (CC BY-NC 4.0, not OSI open source) |
| Requirements | Python 3, an LLM key, and a TypeSafe API key. |
| License | [CC-BY-NC-4.0](https://github.com/arczhi/jet/blob/8e95d71d50ac832e723d0f606637036c91f3bba8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jet/providers/typesafe_judge.py`](https://github.com/arczhi/jet/blob/8e95d71d50ac832e723d0f606637036c91f3bba8/src/jet/providers/typesafe_judge.py) at the pinned commit. |

## When to use

- Try a coding agent that keeps the big model's context small.
- Study Jev-based step and context judgments.
- Mismatch: Creative Commons NonCommercial license; not for commercial use and not OSI open source.

## How it works

`src/jet/providers/typesafe_judge.py` sends typed judgment questions to TypeSafe (`src/jet/config.py` defaults to `https://api.typesafe.ai` and `jev-latest`). Integration evidence: [`src/jet/providers/typesafe_judge.py`](https://github.com/arczhi/jet/blob/8e95d71d50ac832e723d0f606637036c91f3bba8/src/jet/providers/typesafe_judge.py).

## Get started

Clone, install, configure the LLM and TypeSafe keys in the setup screen, and run a task.

```sh
git clone https://github.com/arczhi/jet.git && cd jet
export TYPESAFE_API_KEY=...
pip install -e . && python scripts/smoke.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/arczhi/jet/blob/8e95d71d50ac832e723d0f606637036c91f3bba8/README.md](https://github.com/arczhi/jet/blob/8e95d71d50ac832e723d0f606637036c91f3bba8/README.md)

## Limits and data handling

Code context for judgments goes to TypeSafe and selected context to your LLM provider, on your keys.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 8e95d71d50ac](https://github.com/arczhi/jet/tree/8e95d71d50ac832e723d0f606637036c91f3bba8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
