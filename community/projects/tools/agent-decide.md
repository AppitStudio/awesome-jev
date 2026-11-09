# agent-decide (adec: typed decisions and model routing over System One models with calibration and abstention)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Decision layer for an agent family: typed decisions over TypeSafe-compatible System One models (hosted Jev or self-hosted), with calibrated abstention, a shadow log and a loopback `/v1/systemone` server.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/STAIxBWLB/agent-decide) |
| Maintainer | [STAIxBWLB](https://github.com/STAIxBWLB). Independently curated. |
| Format | Bun/TypeScript CLI + loopback server (MIT) |
| Requirements | Bun ≥ 1.4.2 and a System One provider (hosted Jev key or a self-hosted compatible server). |
| License | [MIT](https://github.com/STAIxBWLB/agent-decide/blob/91e17500366d40a46287a467a26d8354ade27ce6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/providers/systemone.ts`](https://github.com/STAIxBWLB/agent-decide/blob/91e17500366d40a46287a467a26d8354ade27ce6/src/providers/systemone.ts) at the pinned commit. |

## When to use

- Add calibrated abstention to agent decisions.
- Swap between hosted Jev and self-hosted decision models.
- Mismatch: proposals only; adec never executes actions.

## How it works

`providers/systemone.ts` posts to `{endpoint}/v1/systemone` and validates choice answers; `serve.ts` exposes `/v1/systemone`, `/v1/route` and `/v1/health` on loopback only. Integration evidence: [`src/providers/systemone.ts`](https://github.com/STAIxBWLB/agent-decide/blob/91e17500366d40a46287a467a26d8354ade27ce6/src/providers/systemone.ts).

## Get started

From a checkout run `bun install --frozen-lockfile`, write `~/.adec/config.json` with a provider, then use `bin/adec.js`.

```sh
git clone https://github.com/STAIxBWLB/agent-decide.git && cd agent-decide
bun install --frozen-lockfile
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/STAIxBWLB/agent-decide/blob/91e17500366d40a46287a467a26d8354ade27ce6/README.md](https://github.com/STAIxBWLB/agent-decide/blob/91e17500366d40a46287a467a26d8354ade27ce6/README.md)

## Limits and data handling

Decision state goes to whichever System One provider you configure.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 91e17500366d](https://github.com/STAIxBWLB/agent-decide/tree/91e17500366d40a46287a467a26d8354ade27ce6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
