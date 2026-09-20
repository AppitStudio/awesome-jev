# n8n-nodes-typesafe

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Community [n8n](https://n8n.io) node for TypeSafe System One: ask noul, choice, and score questions about workflow text or JSON and route on typed answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Biztactix/n8n-nodes-typesafe) |
| Maintainer | [Biztactix](https://github.com/Biztactix). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript n8n community node package `@biztactix/n8n-nodes-typesafe` **0.1.0** (not yet on npm at review). |
| Requirements | Self-hosted n8n (reviewed against 2.39.8 upstream notes); Node ≥ 20.15 to build. Live node use needs a TypeSafe API credential in n8n. |
| License | [MIT](https://github.com/Biztactix/n8n-nodes-typesafe/blob/b2f435ff4bed1af3225b68236948c37809798685/LICENSE). |

## When to use

Use it to classify or score emails, tickets, or JSON payloads inside n8n and branch on calibrated answers. Prefer language SDKs or [typesafeai-cli](typesafeai-cli.md) outside n8n workflows.

## How it works

[`nodes/TypeSafe/TypeSafe.node.ts`](https://github.com/Biztactix/n8n-nodes-typesafe/blob/b2f435ff4bed1af3225b68236948c37809798685/nodes/TypeSafe/TypeSafe.node.ts) implements **Ask Questions (System One)** (`POST /v1/systemone`) and **List Models** (`GET /v1/models`). Credentials live in [`credentials/TypeSafeApi.credentials.ts`](https://github.com/Biztactix/n8n-nodes-typesafe/blob/b2f435ff4bed1af3225b68236948c37809798685/credentials/TypeSafeApi.credentials.ts) (Bearer key; default base `https://api.typesafe.ai`). Question rows map to noul/choice/score with named answers under `results.<name>`.

## Get started

Package is early and not published to npm yet. From the reviewed commit:

```sh
git clone https://github.com/Biztactix/n8n-nodes-typesafe.git
cd n8n-nodes-typesafe
git checkout b2f435ff4bed1af3225b68236948c37809798685
npm install
npm test
npm run build
# Then tarball or N8N_CUSTOM_EXTENSIONS install per upstream README
```

Live n8n runs call TypeSafe and are billable. This listing did not start n8n or call the API.

## Examples and demos

- Upstream README install table (community packages, tarball, custom extensions).
- [`docs/DESIGN.md`](https://github.com/Biztactix/n8n-nodes-typesafe/blob/b2f435ff4bed1af3225b68236948c37809798685/docs/DESIGN.md) and package tests under `test/`.
- Upstream notes an end-to-end exercise on local n8n 2.39.8 (2026-09-19)—not re-run here.

## Limits and data handling

Until npm publish, install via tarball or `N8N_CUSTOM_EXTENSIONS` (CUSTOM. namespace). Workflow state you pass is sent to TypeSafe. Credential test hits `/v1/models`. Early **0.1.0** surface may change.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b2f435f](https://github.com/Biztactix/n8n-nodes-typesafe/tree/b2f435ff4bed1af3225b68236948c37809798685): **0.1.0**, MIT. AI-assisted source review of the node, credentials, questions helpers, README, and license. On Node.js 24.8.0, **`npm test`**: **83 passed**. No live n8n or TypeSafe calls were performed.

Related: [typesafeai-cli](typesafeai-cli.md), [Advocaat](advocaat.md), [TypeSafe MCP](typesafe-mcp.md).
