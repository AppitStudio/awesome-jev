# template-next-agent (open-source Next.js starter for durable AI agents, with a Jev transaction decision lab)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Next.js starter with two examples: an always-on assistant (EVE agent, cloud browser in Vercel Sandbox, durable Workflow SDK runs, calendar watch) and a decision lab that classifies synthetic transactions or your own CSV with Jev through Vercel AI Gateway, letting you step through each decision and compare models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trancethehuman/template-next-agent) |
| Maintainer | [trancethehuman](https://github.com/trancethehuman). Independently curated. |
| Format | Next.js starter (TypeScript with Bun, AGPL-3.0) |
| Requirements | Node.js 24, Bun, and a Vercel AI Gateway key (`AI_GATEWAY_API_KEY`); Google and Vercel credentials only for the assistant features. |
| License | [AGPL-3.0](https://github.com/trancethehuman/template-next-agent/blob/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/classification/jev.ts`](https://github.com/trancethehuman/template-next-agent/blob/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda/lib/classification/jev.ts) at the pinned commit. |

## When to use

- Start a Next.js agent project with a worked example of Jev classification.
- Mismatch: closed-source products that cannot meet AGPL-3.0 terms.

## How it works

`lib/classification/jev.ts` calls the AI SDK's `experimental_evaluate` with model `typesafe-ai/jev` through Vercel AI Gateway, asking choice questions for category and movement type with probabilities shown per step. The assistant side uses other models (GPT-6.1 Terra by default). Integration evidence: [`lib/classification/jev.ts`](https://github.com/trancethehuman/template-next-agent/blob/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda/lib/classification/jev.ts).

## Get started

Clone, install with Bun, copy the env file and start the dev server; open `/transactions` for the decision lab.

```sh
git clone https://github.com/trancethehuman/template-next-agent.git && cd template-next-agent
bun install
cp .env.local.example .env.local
bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/trancethehuman/template-next-agent/blob/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda/README.md](https://github.com/trancethehuman/template-next-agent/blob/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda/README.md)

## Limits and data handling

Transaction rows (synthetic or your CSV) go to Vercel AI Gateway and TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit ab6a6bc0ea6e](https://github.com/trancethehuman/template-next-agent/tree/ab6a6bc0ea6ed4a1d67d13ec3b4856faa2804fda). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
