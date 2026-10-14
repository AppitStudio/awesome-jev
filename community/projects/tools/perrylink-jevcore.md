# jevcore (PerryLink)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeSafe Jev for DeepSeek Harness, MCP hosts and plain Node: typed noul/choice/score tools that are offline by default with disclosed egress.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/PerryLink/jevcore) |
| Maintainer | [PerryLink](https://github.com/PerryLink). Independently curated. |
| Format | Node packages: core, MCP server, DSH plugin, CLI (TypeScript) |
| Requirements | Node.js; TypeSafe API key for live calls. |
| License | [Apache-2.0](https://github.com/PerryLink/jevcore/blob/da5bd49a60c93a86f8b7c261f88ac5f9b736c66a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/core/src/service.ts`](https://github.com/PerryLink/jevcore/blob/da5bd49a60c93a86f8b7c261f88ac5f9b736c66a/packages/core/src/service.ts) at the pinned commit. |

## When to use

- Give an MCP or DeepSeek Harness agent exactly Jev's typed surface.
- Mismatch: distinct from the listed carter1111/jevcore (JevCore Agent).

## How it works

Packages expose typed primitives; nothing calls TypeSafe unless enabled, and egress is redacted and disclosed. Integration evidence: [`packages/core/src/service.ts`](https://github.com/PerryLink/jevcore/blob/da5bd49a60c93a86f8b7c261f88ac5f9b736c66a/packages/core/src/service.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# see README for npm package names per host (core / mcp / dsh / cli)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Packages: `packages/core`, `packages/mcp`, `packages/dsh`, `packages/cli`.
- Security notes: `SECURITY.md`.

## Limits and data handling

When enabled, questions and state go to TypeSafe.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit da5bd49a60c9](https://github.com/PerryLink/jevcore/tree/da5bd49a60c93a86f8b7c261f88ac5f9b736c66a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
