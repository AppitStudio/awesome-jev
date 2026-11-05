# Jeverb (experimental Muse Code and MCP layer that adds typed Jev judgments to agent hooks and graph execution while policy and verifiers keep authority)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental decision, review and graph-execution layer for Muse Code and MCP-compatible hosts. It adds bounded Jev judgments (does an action fit the request, is evidence relevant, which bounded next step) to hooks and MCP tools, runs dependency-ordered graphs through deterministic admission, records receipts, and fails closed when evidence is missing. The README says Jev is advice only and production use is not qualified.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/B-A-M-N/Jeverb) |
| Maintainer | [B-A-M-N](https://github.com/B-A-M-N). Independently curated. |
| Format | TypeScript Muse plugin and MCP server |
| Requirements | Node.js 20+, npm and Muse Code for host install; `TYPESAFE_API_KEY` for live Jev calls. |
| License | [MIT](https://github.com/B-A-M-N/Jeverb/blob/f80a95587a7c37962b005f90ad7b9bd3bac4272a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/B-A-M-N/Jeverb/blob/f80a95587a7c37962b005f90ad7b9bd3bac4272a/src/jev/client.ts) at the pinned commit. |

## When to use

- Explore keeping model judgments advisory while deterministic code decides.
- Reuse the Jev client and calibration code in an agent harness.
- Mismatch: explicitly experimental; the README points to a limitations document.

## How it works

`src/jev/` holds the Jev client, factory, OpenRouter path, calibration and receipt correlation; the plugin wires typed questions into lifecycle hooks and an MCP server. Integration evidence: [`src/jev/client.ts`](https://github.com/B-A-M-N/Jeverb/blob/f80a95587a7c37962b005f90ad7b9bd3bac4272a/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run build
muse plugins install dist/muse-plugins/jeverb --scope user
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with status and limitations: [github.com/B-A-M-N/Jeverb/blob/f80a95587a7c37962b005f90ad7b9bd3bac4272a/README.md](https://github.com/B-A-M-N/Jeverb/blob/f80a95587a7c37962b005f90ad7b9bd3bac4272a/README.md)

## Limits and data handling

Experimental; model reliability and installed-host enforcement are not generally qualified per the README. Prompts and evidence go to the Jev provider you configure. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit f80a95587a7c](https://github.com/B-A-M-N/Jeverb/tree/f80a95587a7c37962b005f90ad7b9bd3bac4272a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
