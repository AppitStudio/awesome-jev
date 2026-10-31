# Elmo (open-source AI visibility tracker where Jev judges brand mentions and sentiment)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Open-source answer-engine-optimization platform: runs your tracked prompts against ChatGPT, Google AI Mode, Gemini, Perplexity, Copilot and model APIs, then reports visibility, share of voice, citations and sentiment. Jev judges whether each passage really mentions your brand or a competitor and how it is framed, keeping the passage each judgment rests on.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elmohq/elmo) |
| Tags | `Open source` · `Freemium` · `Commercial` · `BYOK` |
| Product homepage | [Product homepage](https://www.elmohq.com/) |
| Pricing and access | Self-host free (MIT, bring your own provider and TypeSafe keys); Elmo Cloud from $29/mo Starter, higher tiers on the [pricing page](https://www.elmohq.com/pricing). Checked 2026-10-31. |
| Jev evidence | [`apps/worker/src/mention-judge/jev.ts`](https://github.com/elmohq/elmo/blob/7a8a3a8f63aae7e931d6efa2d76f791b6842aafb/apps/worker/src/mention-judge/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Commercial: Elmo Cloud is a paid hosted service from the maintainers; self-hosting the MIT source is free. |
| Maintainer | [elmohq](https://github.com/elmohq). Independently curated. |
| Format | Web app + worker (self-host) and Elmo Cloud; CLI and MCP server |
| Platform and availability | Self-hosted web app, or Elmo Cloud in the browser. |
| Jev's role | Judges brand and competitor mentions and their sentiment in each answer-engine passage. |
| Requirements | Self-host: PostgreSQL, keys for at least one AI provider or scraper, and a TypeSafe (or OpenRouter) key for Jev. |
| License | [MIT](https://github.com/elmohq/elmo/blob/7a8a3a8f63aae7e931d6efa2d76f791b6842aafb/LICENSE.md) |

## When to use

- Measure how AI answer engines mention your brand with auditable, per-passage judgments.
- Mismatch: Jev only judges mentions and sentiment; scraping and answer collection rely on other providers.

## How it works

`apps/worker/src/mention-judge/jev.ts` sends candidate passages to `api.typesafe.ai/v1/systemone` (pinned `jev-1.13.0`, or `typesafe/jev-1.13` via OpenRouter) as choice questions per brand; the pin is deliberate so a model change means an explicit re-judge. Integration evidence: [`apps/worker/src/mention-judge/jev.ts`](https://github.com/elmohq/elmo/blob/7a8a3a8f63aae7e931d6efa2d76f791b6842aafb/apps/worker/src/mention-judge/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install -g @elmohq/cli
# or self-host from the repo; see the README for env (provider keys + TYPESAFE_API_KEY)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product site: [www.elmohq.com/](https://www.elmohq.com/)

## Limits and data handling

Engine answers and passages are sent to TypeSafe for judging. Elmo Cloud is a paid hosted option. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 7a8a3a8f63aa](https://github.com/elmohq/elmo/tree/7a8a3a8f63aae7e931d6efa2d76f791b6842aafb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
