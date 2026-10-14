# universal-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin and MCP server for coding agents that uses Jev to compress passing terminal logs into receipts and to make fast DOM decisions with a browser-use fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raj8525/universal-jev) |
| Maintainer | [raj8525](https://github.com/raj8525). Independently curated. |
| Format | Agent plugin + MCP server (Node.js) |
| Requirements | Node.js; TypeSafe API key (OpenRouter fallback). |
| License | [MIT](https://github.com/raj8525/universal-jev/blob/aab838596689cbada4279b9e47e7542731ced1d9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.js`](https://github.com/raj8525/universal-jev/blob/aab838596689cbada4279b9e47e7542731ced1d9/src/client.js) at the pinned commit. |

## When to use

- Shrink noisy build/test output for an agent while keeping failures and diffs intact.
- Mismatch: upstream token-savings figures are unverified claims.

## How it works

Jev judges whether log output passed; code always protects diffs, short-circuits on non-zero exit codes, and samples for hidden errors. A browser tier uses Jev for indexed DOM choices before falling back. Integration evidence: [`src/client.js`](https://github.com/raj8525/universal-jev/blob/aab838596689cbada4279b9e47e7542731ced1d9/src/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/raj8525/universal-jev.git ~/.agents/plugins/universal-jev
cd ~/.agents/plugins/universal-jev
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Verification script: `test/verify-all-agents.sh`.
- Receipt logic: `src/receipt.js`.

## Limits and data handling

Terminal output and DOM snapshots go to TypeSafe/OpenRouter.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit aab838596689](https://github.com/raj8525/universal-jev/tree/aab838596689cbada4279b9e47e7542731ced1d9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
