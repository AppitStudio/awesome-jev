# AIWG

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Multi-agent workflow framework for existing AI tools whose opt-in decision runtime can bind the same validated decision definitions to Jev or to an LLM subagent, with pins, projection, bounded retries, fallback and receipts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jmagly/aiwg) |
| Maintainer | [jmagly](https://github.com/jmagly). Independently curated. |
| Format | Node.js framework + CLI (npm `aiwg`) |
| Requirements | Node.js; an AI coding tool; a TypeSafe key and explicit enablement for Jev decisions. |
| License | [MIT](https://github.com/jmagly/aiwg/blob/c564f11f025fb888cb432e272d0dd613c8f281c5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision/adapters/jev.ts`](https://github.com/jmagly/aiwg/blob/c564f11f025fb888cb432e272d0dd613c8f281c5/src/decision/adapters/jev.ts) at the pinned commit. |

## When to use

- Offload narrow workflow decisions to Jev with `aiwg decision ask` while keeping the same definitions runnable on an LLM.
- Study a hardened adapter: explicit origin allow-list, validated distributions, gated live smoke test.
- Mismatch: a broad framework; Jev is one opt-in decision binding, off unless enabled.

## How it works

Decision definitions (`decision.aiwg.io/v1alpha1/2`) are validated and projected, then run through either the Jev adapter (POST to `https://api.typesafe.ai/v1/systemone` with validated value and distribution checks) or an LLM-subagent binding; the dispatcher needs `AIWG_DECISION_ENABLED=1`. Integration evidence: [`src/decision/adapters/jev.ts`](https://github.com/jmagly/aiwg/blob/c564f11f025fb888cb432e272d0dd613c8f281c5/src/decision/adapters/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g aiwg
aiwg decision setup jev   # then follow docs/decision/jev-quickstart.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision runtime docs: `docs/decision/README.md`, `docs/decision/jev-quickstart.md`.
- Project site: [aiwg.io](https://aiwg.io)

## Limits and data handling

Projected decision state goes to TypeSafe only when a Jev binding is enabled and a credential mapped; tests use fixtures.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit c564f11f025f](https://github.com/jmagly/aiwg/tree/c564f11f025fb888cb432e272d0dd613c8f281c5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
