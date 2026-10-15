# jev-xray (decision forensics)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Decision forensics for Jev: ablates parts of the state, re-asks the same question concurrently and reports which segments moved the probability, with a request/cost ledger.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aishwary-dongre/jev-xray) |
| Maintainer | [aishwary-dongre](https://github.com/aishwary-dongre). Independently curated. |
| Format | Python library (PyPI `jev-xray`) with HTML reports |
| Requirements | Python; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/aishwary-dongre/jev-xray/blob/d88bbb5fe741e97cbab212ffa57e2b578aaf2ad7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_xray/transport/http.py`](https://github.com/aishwary-dongre/jev-xray/blob/d88bbb5fe741e97cbab212ffa57e2b578aaf2ad7/src/jev_xray/transport/http.py) at the pinned commit. |

## When to use

- Explain a surprising or wrong Jev answer by measuring which input segments drove it.
- Audit routing or triage questions for sensitivity to irrelevant state.
- Mismatch: distinct from the already-listed viva-lee/jev-xray repo map; attributions are measured deltas, not model explanations.

## How it works

`XRay.explain()` splits the state into segments, sends occlusion variants of the identical question to Jev in parallel, and reports signed per-segment effects, an interaction residual and a ledger of requests, tokens and cost. Integration evidence: [`src/jev_xray/transport/http.py`](https://github.com/aishwary-dongre/jev-xray/blob/d88bbb5fe741e97cbab212ffa57e2b578aaf2ad7/src/jev_xray/transport/http.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jev-xray
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live sample report: [aishwary-dongre.github.io/jev-xray/](https://aishwary-dongre.github.io/jev-xray/)

## Limits and data handling

Each explanation sends several variants of your state to TypeSafe, billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit d88bbb5fe741](https://github.com/aishwary-dongre/jev-xray/tree/d88bbb5fe741e97cbab212ffa57e2b578aaf2ad7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
