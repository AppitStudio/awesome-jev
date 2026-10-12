# jevey

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small Python wrapper around TypeSafe's Jev API so you can accumulate typed questions (Noul, Choice, …) on a client and await calibrated answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CarloLepelaars/jevey) |
| Maintainer | [CarloLepelaars](https://github.com/CarloLepelaars). Independently curated. |
| Format | Python library (pip `jevey`) |
| Requirements | Python 3; a TypeSafe API key for live calls. |
| License | [Apache-2.0](https://github.com/CarloLepelaars/jevey/blob/af8365549d0c1d0dcb71c56eec70e51fba38d54c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Prototyping Jev integrations in notebooks or scripts without hand-rolling request JSON.
- Mismatch: Thin wrapper—policy and fallbacks stay in your code.

## How it works

You add typed question objects to a `Client`, then call it with state text; it posts to TypeSafe and returns probabilities. Core client: [`jevey/core.py`](https://github.com/CarloLepelaars/jevey/blob/af8365549d0c1d0dcb71c56eec70e51fba38d54c/jevey/core.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jevey
# then: from jevey import Client, Noul
```

## Limits and data handling

State text is sent to TypeSafe when you call live; billed by usage. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit af8365549d0c](https://github.com/CarloLepelaars/jevey/tree/af8365549d0c1d0dcb71c56eec70e51fba38d54c). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
