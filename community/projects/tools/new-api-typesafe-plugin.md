# TypeSafe plugin for New API (official new-api task plugin that serves Jev System One through your gateway)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Official task plugin for the new-api AI gateway that exposes TypeSafe System One and the Jev models (`jev-1.14.0`, `jev-1.13.0`, `jev-latest`, `jev-preview`) at `/v1/systemone`, with per-token billing and quota reservation, so gateway users can call Jev with the official SDKs pointed at the gateway.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/QuantumNous/new-api-plugins) |
| Maintainer | [QuantumNous](https://github.com/QuantumNous). Independently curated. |
| Format | new-api JavaScript task plugin (Apache-2.0) |
| Requirements | A self-hosted new-api gateway with the task-plugin runtime, and a TypeSafe API key for the channel. |
| License | [Apache-2.0](https://github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/tasks/typesafe/1.2.0/plugin.js`](https://github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/plugins/tasks/typesafe/1.2.0/plugin.js) at the pinned commit. |

## When to use

- Offer Jev to your team through an existing new-api gateway with per-user tokens and quotas.
- Mismatch: if you do not run new-api; call TypeSafe directly instead.

## How it works

`plugins/tasks/typesafe/1.2.0/plugin.js` forwards `POST /v1/systemone` (and `/typesafe/v1/systemone`) to `https://api.typesafe.ai` by default, adds TypeSafe's image header for asset uploads, passes TypeSafe errors through, and settles charges on the input tokens TypeSafe reports. Published version directories are immutable and hashed in `index.json`. Integration evidence: [`plugins/tasks/typesafe/1.2.0/plugin.js`](https://github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/plugins/tasks/typesafe/1.2.0/plugin.js).

## Get started

In new-api, create a Task Plugin (61) channel, bind the TypeSafe plugin and enter your TypeSafe key; leave the API address empty for the default.

```sh
curl https://your-gateway.example.com/v1/systemone \
  -H "Authorization: Bearer sk-..." -H "Content-Type: application/json" -d @request.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plugin README: [github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/plugins/tasks/typesafe/README.md](https://github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/plugins/tasks/typesafe/README.md)
- Plugin index: [github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/index.json](https://github.com/QuantumNous/new-api-plugins/blob/278e92ee46c26801e4e9007409e31869bd33debc/index.json)

## Limits and data handling

Requests pass through your own gateway to TypeSafe on the channel's key; the gateway reserves quota per request (65,792 input tokens, more with long context) before settling.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 278e92ee46c2](https://github.com/QuantumNous/new-api-plugins/tree/278e92ee46c26801e4e9007409e31869bd33debc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
