# jev-strict

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial, standard-library Python client for Jev that pins one model, meters usage in a crash-safe JSONL file, refuses calls past a hard monthly cap, and asks every choice and score in both option orders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jubii100/jev-strict) |
| Maintainer | [Jubii100](https://github.com/Jubii100). Independently curated. |
| Format | Python library (stdlib only, Python 3.9+) |
| Requirements | Python 3.9+, a TypeSafe API key, the endpoint from TypeSafe's API reference. |
| License | [MIT](https://github.com/Jubii100/jev-strict/blob/d5dc3d825ff5b4c16414f885eb80a2b3782a8c0b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_strict/client.py`](https://github.com/Jubii100/jev-strict/blob/d5dc3d825ff5b4c16414f885eb80a2b3782a8c0b/jev_strict/client.py) at the pinned commit. |

## When to use

- Share one Jev key across many jobs without overrunning a monthly budget.
- Treat order-inconsistent answers as "no answer" instead of trusting them.
- Mismatch: you must supply your own price per token; with a price of 0 no cap holds.

## How it works

`Client` refuses the moving `jev-latest` alias, errors if a response names another model, and checks the shared meter before any request leaves. `Judge` sends each choice or score in forward and reversed order in one request and returns nothing when they disagree; a missing key or budget raises `Unavailable`. Integration evidence: [`jev_strict/client.py`](https://github.com/Jubii100/jev-strict/blob/d5dc3d825ff5b4c16414f885eb80a2b3782a8c0b/jev_strict/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install git+https://github.com/Jubii100/jev-strict
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quick start with `Client` and `Judge` in the README.

## Limits and data handling

Questions go to TypeSafe on your key. The usage meter is a local file shared by every process that spends against the same cap.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit d5dc3d825ff5](https://github.com/Jubii100/jev-strict/tree/d5dc3d825ff5b4c16414f885eb80a2b3782a8c0b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
