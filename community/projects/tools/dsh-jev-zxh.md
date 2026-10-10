# dsh-jev-zxh

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness (DSH) plugin that exposes TypeSafe Jev as the model-callable `jev_decide` tool for typed `choice`, `noul`, and `score` decisions. README in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TiChuXiXi/dsh-jev-zxh) |
| Maintainer | [TiChuXiXi](https://github.com/TiChuXiXi). Independently curated. |
| Format | DSH plugin (npm `dsh-jev-zxh`, zero-build) |
| Requirements | `@deepseek-ai/dsh` 0.2.0-rc.2 or later; a Jev API key and endpoint configured in DSH plugin settings. |
| License | [MIT](https://github.com/TiChuXiXi/dsh-jev-zxh/blob/267a9dc2dffbbe105fa0804411aaa7d88e935d48/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Let a DSH agent ask Jev typed questions and branch on probabilities.
- Mismatch: DSH only; not related to the separate `dsh-jev` npm package.

## How it works

Registers a `jev_decide` tool that forwards state plus typed questions to Jev and returns typed answers with probabilities. (Summarized from the upstream [README](https://github.com/TiChuXiXi/dsh-jev-zxh/blob/267a9dc2dffbbe105fa0804411aaa7d88e935d48/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `dsh plugin --profile web add dsh-jev-zxh`, then set `apiKey` and `endpoint` under Settings → Plugins.

## Limits and data handling

Tool inputs are sent to the configured Jev endpoint; the package ships no keys. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 267a9dc2dffb](https://github.com/TiChuXiXi/dsh-jev-zxh/tree/267a9dc2dffbbe105fa0804411aaa7d88e935d48). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
