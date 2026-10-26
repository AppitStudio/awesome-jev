# jevtester (test decision models, your questions and the decisions your code makes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command-line tool, HTTP API and web UI that run on your own computer to test decision models, the questions you write for them and the decisions your code makes from their answers, comparing targets side by side; it supports TypeSafe's System One, Microsoft-Decision-1 on Azure AI Foundry and Clef models on Cloudflare, Ollama or MLX.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mmacy/jevtester) |
| Maintainer | [mmacy](https://github.com/mmacy). Independently curated. |
| Format | Python CLI, HTTP API and web UI |
| Requirements | Python; keys for the targets you test (TypeSafe for Jev). |
| License | [CC BY-NC-SA 4.0 (source available; non-commercial; not an OSI open-source license)](https://github.com/mmacy/jevtester/blob/00b259d931f569ecdcf3c27052e79cd957556714/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevtester/providers/typesafe.py`](https://github.com/mmacy/jevtester/blob/00b259d931f569ecdcf3c27052e79cd957556714/src/jevtester/providers/typesafe.py) at the pinned commit. |

## When to use

- Check that your Jev questions give the answers you expect before shipping them.
- Compare Jev with other decision models on the same requests.
- Mismatch: CC BY-NC-SA 4.0 licence — non-commercial use only; not open source.

## How it works

`src/jevtester/providers/typesafe.py` calls TypeSafe through `typesafe_sdk`, which posts to `/v1/systemone`, and records each option's probability next to the other targets'. Integration evidence: [`src/jevtester/providers/typesafe.py`](https://github.com/mmacy/jevtester/blob/00b259d931f569ecdcf3c27052e79cd957556714/src/jevtester/providers/typesafe.py).

## Get started

From the upstream README (not run on the review host):

```sh
# see the README quick start for installation and the web UI
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mmacy/jevtester#readme](https://github.com/mmacy/jevtester#readme)

## Limits and data handling

Test requests go to each target you configure. The licence forbids commercial use.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 00b259d931f5](https://github.com/mmacy/jevtester/tree/00b259d931f569ecdcf3c27052e79cd957556714). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
