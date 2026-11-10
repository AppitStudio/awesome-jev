# E-NEXUS Decision Layer (rules-first decision gateway with a Jev adapter)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Japanese AI- and IDE-agnostic decision gateway (SDK, CLI, HTTP and MCP) that runs deterministic rules first, then a probabilistic adapter such as Jev, and always ends at a human; it never approves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/en540424/e-nexus-decision-layer) |
| Maintainer | [en540424](https://github.com/en540424). Independently curated. |
| Format | Node.js gateway (CLI, HTTP, MCP; zero required dependencies; source only) |
| Requirements | Node.js; `JEV_API_KEY` for TypeSafe Direct (without it the Jev adapter is unavailable and falls back to mock/human). |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapters/jev/jev-direct-provider.mjs`](https://github.com/en540424/e-nexus-decision-layer/blob/6e1470884ba9266636e0e56a8e402489fdcabd81/src/adapters/jev/jev-direct-provider.mjs) at the pinned commit. |

## When to use

- Put a rules-first, human-final decision gate in front of agents and apps.
- Swap Jev in or out behind one adapter contract with usage metering.
- Mismatch: docs in Japanese; no license file (source-available only); built for the author's E-NEXUS projects.

## How it works

`jev-direct-provider.mjs` calls `POST https://api.typesafe.ai/v1/systemone` and records the versioned model that answered; the core engine does not know about Jev, and usage is metered per decision in `data/usage/usage.jsonl`. Integration evidence: [`src/adapters/jev/jev-direct-provider.mjs`](https://github.com/en540424/e-nexus-decision-layer/blob/6e1470884ba9266636e0e56a8e402489fdcabd81/src/adapters/jev/jev-direct-provider.mjs).

## Get started

Run the tests, then send a request to `node src/cli.mjs gateway decide --stdin` or start `gateway serve`.

```sh
git clone https://github.com/en540424/e-nexus-decision-layer.git && cd e-nexus-decision-layer
npm test
node src/cli.mjs gateway health
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/en540424/e-nexus-decision-layer/blob/6e1470884ba9266636e0e56a8e402489fdcabd81/README.md](https://github.com/en540424/e-nexus-decision-layer/blob/6e1470884ba9266636e0e56a8e402489fdcabd81/README.md)

## Limits and data handling

Request inputs go to TypeSafe only when the Jev adapter is configured; HTTP serve binds to loopback unless a token is set.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 6e1470884ba9](https://github.com/en540424/e-nexus-decision-layer/tree/6e1470884ba9266636e0e56a8e402489fdcabd81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
