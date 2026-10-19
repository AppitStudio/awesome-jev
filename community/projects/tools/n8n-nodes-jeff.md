# n8n-nodes-jeff

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial n8n community node for Jev with ready-made decisions (rank a list, triage a message, guard text before an LLM, match two records, verify a claim against a source) plus a plain Ask operation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/n8n-nodes-jeff) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | n8n community node (TypeScript) |
| Requirements | n8n; TypeSafe API key. |
| License | [MIT](https://github.com/saembit/n8n-nodes-jeff/blob/1d61473e1b0bc2d4a93a154f7b3b6c7ed8c68c29/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`credentials/JeffTypeSafeApi.credentials.ts`](https://github.com/saembit/n8n-nodes-jeff/blob/1d61473e1b0bc2d4a93a154f7b3b6c7ed8c68c29/credentials/JeffTypeSafeApi.credentials.ts) at the pinned commit. |

## When to use

- Branch n8n workflows on typed Jev decisions without writing prompts.
- Mismatch: unofficial; questions and thresholds are prewritten.

## How it works

The node sends parameters to TypeSafe with the credential defined in `credentials/JeffTypeSafeApi.credentials.ts` and outputs typed results to branch on. Integration evidence: [`credentials/JeffTypeSafeApi.credentials.ts`](https://github.com/saembit/n8n-nodes-jeff/blob/1d61473e1b0bc2d4a93a154f7b3b6c7ed8c68c29/credentials/JeffTypeSafeApi.credentials.ts).

## Get started

From the upstream README: install the community node in n8n settings and add a TypeSafe (Jeff) API credential.

```sh
# n8n > Settings > Community nodes > install n8n-nodes-jeff
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README Operations section

## Limits and data handling

Everything in node parameters goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1d61473e1b0b](https://github.com/saembit/n8n-nodes-jeff/tree/1d61473e1b0bc2d4a93a154f7b3b6c7ed8c68c29). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
