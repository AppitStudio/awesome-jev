# pi-jewter by Grigory Bakunov (Pi coding-agent extension where Jev picks the model and thinking level for each step)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Select `jewter/auto` once and, before each agent step, Jev classifies the task and the capability it needs; Jewter then picks a model and thinking level from your `fast`/`medium`/`strong` tiers, with a cache-switch penalty against marginal changes. Optional context compaction and verification hints. Ships no model assignments of its own.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bobuk/pi-jewter) |
| Maintainer | [Grigory Bakunov](https://github.com/bobuk). Independently curated. |
| Format | Pi extension (TypeScript; npm `pi-jewter`, v0.3.6 at review) |
| Requirements | Pi 1.5.0+, Node 22.19.0+, a TypeSafe or OpenRouter key for Jev, and at least one model already usable in Pi. |
| License | [MIT](https://github.com/bobuk/pi-jewter/blob/b994d8e35af6d128fcf83e34b505863f73824d18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/types.ts`](https://github.com/bobuk/pi-jewter/blob/b994d8e35af6d128fcf83e34b505863f73824d18/src/jev/types.ts) at the pinned commit. |

## When to use

- Let Pi switch between cheap and strong models as work moves between kinds of task.
- Mismatch: other coding agents; this is Pi-only.

## How it works

`src/jev/types.ts` defines the TypeSafe (`https://api.typesafe.ai/v1/systemone`) and OpenRouter transports; the router sends conversation context to Jev before each step. Integration evidence: [`src/jev/types.ts`](https://github.com/bobuk/pi-jewter/blob/b994d8e35af6d128fcf83e34b505863f73824d18/src/jev/types.ts).

## Get started

Install from npm or Git, give Jev a key, assign model tiers, then select `jewter/auto`.

```sh
pi install npm:pi-jewter
export TYPESAFE_API_KEY='...'
# in Pi: /jewter -> Models, then /model -> jewter/auto
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Workflows and profiles: [github.com/bobuk/pi-jewter/blob/b994d8e35af6d128fcf83e34b505863f73824d18/docs/workflows.md](https://github.com/bobuk/pi-jewter/blob/b994d8e35af6d128fcf83e34b505863f73824d18/docs/workflows.md)

## Limits and data handling

Conversation context is sent to TypeSafe or OpenRouter for each routing call, billed separately from your answering models. Some features are only in the Git version.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit b994d8e35af6](https://github.com/bobuk/pi-jewter/tree/b994d8e35af6d128fcf83e34b505863f73824d18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
