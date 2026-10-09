# JevTools

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Toolkit and reference implementation for Jev via OpenRouter decisions or the TypeSafe API: zero-dependency Python localhost server and web dashboard for review analysis, topic classification and custom decisions, local SQLite request history, and Markdown docs on control-inversion design.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RileyCarney/JevTools) |
| Maintainer | [RileyCarney](https://github.com/RileyCarney). Independently curated. |
| Format | Python localhost server + HTML dashboard |
| Requirements | Python 3.8+, `requests`; `OPENROUTER_API_KEY` or `TYPESAFE_API_KEY`. |
| License | [GPL-3.0](https://github.com/RileyCarney/JevTools/blob/29f29439ee78202f6791f9fe316985a0f79e116b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Local Jev experimentation with logged history.
- Mismatch: alpha endpoints; dashboard is a personal tool.

## How it works

See the upstream [README](https://github.com/RileyCarney/JevTools/blob/29f29439ee78202f6791f9fe316985a0f79e116b/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/RileyCarney/JevTools.git && cd JevTools
python server.py
```

## Limits and data handling

Requests go to OpenRouter or TypeSafe; history stays in a gitignored local SQLite file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 29f29439ee78](https://github.com/RileyCarney/JevTools/tree/29f29439ee78202f6791f9fe316985a0f79e116b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
