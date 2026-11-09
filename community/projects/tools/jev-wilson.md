# Jev Wilson (prices AI-agent job cover from a seller's record, with an optional Jev grade())

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript/Python/Solidity library that turns the Wilson score bound on an agent seller's delivered/failed record into a coverage premium and fees; an optional `grade()` asks Jev a four-question rubric.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/taifoon-io/jev-wilson) |
| Maintainer | [taifoon-io](https://github.com/taifoon-io). Independently curated. |
| Format | npm + Python + Solidity library (Apache-2.0) |
| Requirements | Node or Python; `@typesafe-ai/sdk` / `typesafe-sdk` and a TypeSafe key only for `grade()`. |
| License | [Apache-2.0](https://github.com/taifoon-io/jev-wilson/blob/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`python/taifoon_jev_wilson/wilson.py`](https://github.com/taifoon-io/jev-wilson/blob/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2/python/taifoon_jev_wilson/wilson.py) at the pinned commit. |

## When to use

- Price cover for agent jobs from a track record.
- Grade deliverables with a fixed Jev rubric.
- Mismatch: Jev is optional; core maths needs no network.

## How it works

`grade()` in `wilson.py` (and `src/wilson.ts`) builds the RUBRIC_v1 questions with the SDK's `choice()` and calls `TypeSafeClient`; the pricing maths itself is offline integer code. Integration evidence: [`python/taifoon_jev_wilson/wilson.py`](https://github.com/taifoon-io/jev-wilson/blob/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2/python/taifoon_jev_wilson/wilson.py).

## Get started

Run `npx @taifoon/jev-wilson premium 90 100 100000000`, or install the `[jev]` extra to use `grade()`.

```sh
npx @taifoon/jev-wilson premium 90 100 100000000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/taifoon-io/jev-wilson/blob/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2/README.md](https://github.com/taifoon-io/jev-wilson/blob/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2/README.md)

## Limits and data handling

Only `grade()` sends task and deliverable text to TypeSafe.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 0d69a0e33f6f](https://github.com/taifoon-io/jev-wilson/tree/0d69a0e33f6fee9ff71f869a2cd73294d1c89be2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
