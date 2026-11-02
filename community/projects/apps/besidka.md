# Besidka (open-source BYOK AI chat that adds seven optional Jev checks on your own TypeSafe key)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Bring-your-own-key AI chat on Nuxt and Cloudflare Workers that shows the price of every message and puts all your models in one chat, with no subscription. With your own TypeSafe key, Jev adds optional yes/no checks such as prompt-injection screening, memory checks and reranking, each with its own threshold and toggle; the chat works without it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/besidka/besidka) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://besidka.com) |
| Pricing and access | Free hosted app with no subscription or markup; you pay AI providers (and TypeSafe for Jev checks) through your own keys. Free source build under MIT. Checked 2026-11-02. |
| Jev evidence | [`server/utils/jev/client.ts`](https://github.com/besidka/besidka/blob/2c57294afb992a090b936c547aa4f0a21f920b1f/server/utils/jev/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/serhiichernenko/status/2117247044582515090)). |
| Maintainer | [besidka](https://github.com/besidka). Independently curated. |
| Format | Web app (Nuxt + Cloudflare Workers) |
| Platform and availability | Web (hosted at besidka.com); self-host on Cloudflare. |
| Jev's role | Runs optional yes/no checks such as injection screening, memory checks and reranking. |
| Requirements | A browser and your own AI provider key; `TYPESAFE_API_KEY` for the Jev checks; Cloudflare to self-host. |
| License | [MIT](https://github.com/besidka/besidka/blob/2c57294afb992a090b936c547aa4f0a21f920b1f/LICENSE) |

## When to use

- Use one chat for many providers and add cheap safety and memory checks.
- Mismatch: Jev only adds checks on top of the chat; if it is slow or down the chat carries on without them.

## How it works

`server/utils/jev/client.ts` uses `@ai-sdk/typesafe-ai` and the AI SDK's `experimental_decide` with the user's stored, encrypted TypeSafe key; modules such as `injection-screening.ts`, `rerank.ts` and `memory/jev-check.ts` each ask one question and act above a threshold. Integration evidence: [`server/utils/jev/client.ts`](https://github.com/besidka/besidka/blob/2c57294afb992a090b936c547aa4f0a21f920b1f/server/utils/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone git@github.com:besidka/besidka.git
cd besidka
pnpm install
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted app: [besidka.com](https://besidka.com)
- Creator's post on the seven Jev checks: [x.com/serhiichernenko/status/2117247044582515090](https://x.com/serhiichernenko/status/2117247044582515090)

## Limits and data handling

With the Jev checks on, the relevant message or memory text is sent to TypeSafe on your key; chat content goes to the providers you choose. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 2c57294afb99](https://github.com/besidka/besidka/tree/2c57294afb992a090b936c547aa4f0a21f920b1f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
