# hfanshu/dsh-jev (DeepSeek Harness plugin exposing native jev_* tools over System One HTTP)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness adapter plugin that adds jev_* native tools and a small HTTP client for TypeSafe System One classification, triage, routing, scoring and gate judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hfanshu/dsh-jev) |
| Maintainer | [hfanshu](https://github.com/hfanshu). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript, MIT) |
| Requirements | DeepSeek Harness host and a TypeSafe (or compatible System One) base URL and API key. |
| License | [MIT](https://github.com/hfanshu/dsh-jev/blob/4b5dae4fbd1c647e14121203c7f0e24856e1a227/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-client.ts`](https://github.com/hfanshu/dsh-jev/blob/4b5dae4fbd1c647e14121203c7f0e24856e1a227/jev-client.ts) at the pinned commit. |

## When to use

- Add calibrated Jev tools inside DeepSeek Harness.
- Call POST /v1/systemone from a small HTTP client.
- Mismatch: Harness-specific plugin; not a standalone CLI. Distinct from the already-listed noetion/dsh-jev package.

## How it works

`jev-client.ts` POSTs to `{baseUrl}/v1/systemone` for typed System One answers used by the plugin tools. Integration evidence: [`jev-client.ts`](https://github.com/hfanshu/dsh-jev/blob/4b5dae4fbd1c647e14121203c7f0e24856e1a227/jev-client.ts).

## Get started

Install into DeepSeek Harness per README and configure base URL plus API key.

```sh
git clone https://github.com/hfanshu/dsh-jev.git && cd dsh-jev
export TYPESAFE_API_KEY=...
# follow README Harness install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/hfanshu/dsh-jev/blob/4b5dae4fbd1c647e14121203c7f0e24856e1a227/README.md](https://github.com/hfanshu/dsh-jev/blob/4b5dae4fbd1c647e14121203c7f0e24856e1a227/README.md)

## Limits and data handling

Tool state and questions are sent to the configured System One endpoint on your key.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 4b5dae4fbd1c](https://github.com/hfanshu/dsh-jev/tree/4b5dae4fbd1c647e14121203c7f0e24856e1a227). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
