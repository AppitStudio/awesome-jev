# Finney (finance agent for hackathon directors, with Jev reviewing agent traces)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Event finance workspace for hackathon directors that keeps source evidence, budget commitments, decisions and reports together in Supabase with a Next.js front end; OpenCode and Hermes do scoped agent work, Jev asks four yes/no questions about each finished trace (unsupported completions, missing payer evidence, needless clarifications, stale links), and payments run only on Base Sepolia test funds with exact-action approvals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pauravhp/finney) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://finney-beta.vercel.app) |
| Pricing and access | Open source (MIT); free source build. Jev calls are billed to your Vercel AI Gateway key; Supabase and hosting are yours. Access terms for the hosted beta were not verified. Checked 2026-10-26. |
| Jev evidence | [`app/models/providers.py`](https://github.com/pauravhp/finney/blob/3a01835a837cc3cf43b34b6a47a97f770f606554/app/models/providers.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [pauravhp](https://github.com/pauravhp). Independently curated. |
| Format | Next.js web app with a Python service |
| Platform and availability | Web; hosted beta at finney-beta.vercel.app (sign-in required) or self-host. |
| Jev's role | Trace reviewer: completed agent traces get four Noul questions, and flagged ones queue a bounded diagnosis. |
| Requirements | Supabase, Node.js and Python; OpenCode or Hermes for agent work; a Vercel AI Gateway key for Jev; Coinbase Wallet MCP on Base Sepolia for test payments. |
| License | [MIT](https://github.com/pauravhp/finney/blob/3a01835a837cc3cf43b34b6a47a97f770f606554/LICENSE) |

## When to use

- Run an event budget with an agent while keeping every decision tied to evidence.
- Catch agent claims that a payment happened without proof.
- Mismatch: payments are testnet only (no mainnet execution); a hackathon-scale project.

## How it works

`app/models/providers.py` defines `JevClient`, which posts the trace with four Noul questions to `https://ai-gateway.vercel.sh/typesafe/v1/systemone` using `typesafe-ai/jev-1.14.0`; Jev's key is kept separate from the agent's. Integration evidence: [`app/models/providers.py`](https://github.com/pauravhp/finney/blob/3a01835a837cc3cf43b34b6a47a97f770f606554/app/models/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/pauravhp/finney && cd finney
# follow the README setup; put AI_GATEWAY_API_KEY in the environment to enable Jev reviews
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guided practice event: [finney-beta.vercel.app/desk?demo=guided](https://finney-beta.vercel.app/desk?demo=guided)
- README: [github.com/pauravhp/finney#readme](https://github.com/pauravhp/finney#readme)

## Limits and data handling

Agent traces go to Vercel AI Gateway and on to TypeSafe; Jev is reached through the gateway. Payments use Base Sepolia test funds only. It can read a connected Gmail mailbox through Hermes. The README calls Jev scores triage, not proof of correct finances.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 3a01835a837c](https://github.com/pauravhp/finney/tree/3a01835a837cc3cf43b34b6a47a97f770f606554). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
