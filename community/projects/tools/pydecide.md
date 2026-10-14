# pydecide

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

One Python client for typed decisions (Choice, Score, Noul) over Jev, OpenRouter, OpenAI Decisions, Laya, MLX and cross-encoders, with a confidence-gated fallback chain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gopaljigaur/decide) |
| Maintainer | [gopaljigaur](https://github.com/gopaljigaur). Independently curated. |
| Format | Python library and CLI (PyPI `pydecide`) |
| Requirements | Python; TypeSafe or other provider keys for hosted tiers. |
| License | [MIT](https://github.com/gopaljigaur/decide/blob/393d323f662b74ec601db7af1b3e9eb6d4967c99/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decide/client.py`](https://github.com/gopaljigaur/decide/blob/393d323f662b74ec601db7af1b3e9eb6d4967c99/decide/client.py) at the pinned commit. |

## When to use

- Use one API for Jev and open alternatives, escalating only low-confidence questions to the better model.
- Run decisions from the command line with the `decide` CLI.
- Mismatch: tier quality depends on the backends you configure.

## How it works

Questions go through a chain of backends; a confidence gate forwards uncertain answers to the next tier. The TypeSafe backend posts to `api.typesafe.ai/v1/systemone` with `jev-latest` by default. Integration evidence: [`decide/client.py`](https://github.com/gopaljigaur/decide/blob/393d323f662b74ec601db7af1b3e9eb6d4967c99/decide/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install pydecide
uv add pydecide
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Fallback-chain diagram and examples in the upstream README.

## Limits and data handling

State sent to hosted tiers (TypeSafe, OpenRouter, OpenAI) is billed to your keys; local tiers stay on your machine.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 393d323f662b](https://github.com/gopaljigaur/decide/tree/393d323f662b74ec601db7af1b3e9eb6d4967c99). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
