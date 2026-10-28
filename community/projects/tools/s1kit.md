# s1kit (test, calibrate and route System One decision models like Jev on your own data)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python CLI and library for anyone choosing between decision models that speak `/v1/systemone` (Jev, Laya, kev, llama.cpp, Ollama): `s1kit test` runs one labelled suite against every model side by side, `s1kit calibrate` picks a per-question confidence cutoff that reaches your target precision, and `s1kit.Router` asks the cheapest model first and escalates only when it is unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Eliot5566/s1kit) |
| Maintainer | [Eliot5566](https://github.com/Eliot5566). Independently curated. |
| Format | Python package and CLI (PyPI `s1kit`) |
| Requirements | Python; a TypeSafe key or any `/v1/systemone` endpoint (local ones need no key). |
| License | [MIT](https://github.com/Eliot5566/s1kit/blob/9948b2d0665dedbeaa3071c7ea040d0922285c22/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/s1kit/providers.py`](https://github.com/Eliot5566/s1kit/blob/9948b2d0665dedbeaa3071c7ea040d0922285c22/src/s1kit/providers.py) at the pinned commit. |

## When to use

- Decide whether a cheaper or local decision model is good enough for your questions.
- Mismatch: results depend on your labelled suite.

## How it works

`src/s1kit/providers.py` calls each configured `/v1/systemone` endpoint (for example `https://api.typesafe.ai` with `jev-latest`), and `protocol.py` turns each answer into a comparable label and confidence. Integration evidence: [`src/s1kit/providers.py`](https://github.com/Eliot5566/s1kit/blob/9948b2d0665dedbeaa3071c7ea040d0922285c22/src/s1kit/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install s1kit
s1kit init      # writes s1kit.yaml with 10 support tickets and 3 questions
s1kit test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- PyPI: [pypi.org/project/s1kit/](https://pypi.org/project/s1kit/)
- README: [github.com/Eliot5566/s1kit#readme](https://github.com/Eliot5566/s1kit#readme)

## Limits and data handling

Suite items go to every configured endpoint; local endpoints keep them on your machine.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 9948b2d0665d](https://github.com/Eliot5566/s1kit/tree/9948b2d0665dedbeaa3071c7ea040d0922285c22). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
