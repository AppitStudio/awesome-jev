# jev-py-sdk

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Python SDK and CLI for typed Jev judgments (`noul`, `choice`, `score`) that masks state, instructions, and criteria before they leave your machine, with a local decision log. Python port of the maintainer's TypeScript `jev-sdk`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ogarciarevett/jev-py-sdk) |
| Maintainer | [ogarciarevett](https://github.com/ogarciarevett). Independently curated. |
| Format | Python library + `jev` CLI (wheel on GitHub Releases) |
| Requirements | Python 3.10+; `httpx`; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/ogarciarevett/jev-py-sdk/blob/dde0d4f8f9c68054b24cf8547e6466a5dc3251ab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Ask Jev several typed questions about one state from Python with masking built in.
- Mismatch: not on PyPI yet; install from the release wheel.

## How it works

`judge(state, questions)` masks inputs, calls Jev, and returns typed verdicts; the CLI can log and report decisions. (Summarized from the upstream [README](https://github.com/ogarciarevett/jev-py-sdk/blob/dde0d4f8f9c68054b24cf8547e6466a5dc3251ab/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install the release wheel with `pip`, then call `jev_sdk.judge(...)` or run `jev judge --state - --questions ...`.

## Limits and data handling

Masked state is sent to TypeSafe; README states verdicts inform but never authorize actions. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit dde0d4f8f9c6](https://github.com/ogarciarevett/jev-py-sdk/tree/dde0d4f8f9c68054b24cf8547e6466a5dc3251ab). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
