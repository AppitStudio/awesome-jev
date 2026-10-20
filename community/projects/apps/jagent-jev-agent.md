# Jagent (jev-agent.com)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Independent hosted web app and Jev gateway: a no-key playground with a compare mode, browser tools such as an essay grader, resume checker and agent-router playground, games where Jev picks each move from the legal options (chess, a Wikipedia race, Connect 4), and a Jev API on its own key with System One, ruleset, Decisions-format and MCP endpoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://jev-agent.com) |
| Tags | `Closed source` · `Freemium` · `Commercial` |
| Product homepage | [jev-agent.com](https://jev-agent.com) · [getting started](https://jev-agent.com/getting-started) · [API docs](https://jev-agent.com/docs) · [llms.txt](https://jev-agent.com/llms.txt) |
| Pricing and access | Playground runs without an account on a shared anonymous trial of three runs. API keys (`jv_live_…`) need a Google or email-code sign-in and no card; each account gets 5 free credits a month (1 credit = 1,000 input tokens; output is not billed; failed requests are free, per the submitter), with paid one-time credit packs on the [pricing page](https://jev-agent.com/pricing). Optional `X-TypeSafe-Key` header runs a call on your own TypeSafe account at 0 credits. Keys work only on this host. Checked **2026-10-20**. |
| Jev evidence | Public [API docs](https://jev-agent.com/docs) document `POST /api/v1/systemone` in TypeSafe's request and answer shape, `POST /api/v1/classify` with eight published rulesets, `POST /api/v1/decisions` in OpenAI's Decisions format, and a hosted MCP server at `https://jev-agent.com/api/mcp`. Benchmarks page links a public reproduction repo, [WallerChen/jev-measured](https://github.com/WallerChen/jev-measured). Implementation not inspected; no live calls made on the review host. |
| Disclosure | Self-submitted by the operator ([issue #1855](https://github.com/AppitStudio/awesome-jev/issues/1855)), who states the site is independent and not affiliated with TypeSafe AI and that the submission was drafted with AI assistance. Commercial: paid credit packs alongside free monthly credits. Closed source; behaviour described here comes from public pages. AI-assisted catalog review; no affiliation with the operator. Listing is not an endorsement. |
| Maintainer | Operator of jev-agent.com (GitHub [WallerChen](https://github.com/WallerChen)). |
| Format | Hosted web app, REST API and hosted MCP server |
| Platform and availability | Web browser; live since September 2026 per the submitter. Pages listed here returned HTTP 200 on 2026-10-20. |
| Jev's role | Requests pass through jev-agent.com to TypeSafe's hosted Jev API: Jev answers the playground's Choice, Score and Noul questions, picks moves in the games, and serves the API endpoints. |
| Requirements | A modern browser; for the API, a jev-agent.com key (or your own TypeSafe key via `X-TypeSafe-Key`). |
| License | Proprietary hosted service; no source license. |

## When to use

- Try Jev questions on your own text in a browser before writing integration code, or compare Jev with another decision model on the same question.
- Watch Jev choose moves step by step with probabilities shown.
- Call Jev from code or an MCP client without a TypeSafe account, within a small free allowance.
- Mismatch: for production on TypeSafe's own terms and SLA, use a TypeSafe account directly; this is not a local model or a self-hosted gateway.

## How it works

The site forwards requests to TypeSafe's hosted Jev API. `/api/v1/systemone` accepts your own questions in TypeSafe's shape; `/api/v1/classify` takes text plus one of eight named rulesets whose exact Jev call is published; `/api/v1/decisions` accepts OpenAI's Decisions API request. All share one key and credit balance. These details come from the public docs; the implementation is closed.

## Get started

1. Open the [playground](https://jev-agent.com) and run a question without an account (three shared trial runs).
2. To use the API, sign in, create a key at the API access page, then call the System One endpoint:

```sh
curl -X POST https://jev-agent.com/api/v1/systemone \
  -H "Authorization: Bearer jv_live_..." \
  -H "Content-Type: application/json" \
  -d @request.json   # TypeSafe System One request body
```

Calls spend jev-agent.com credits (or your TypeSafe account with `X-TypeSafe-Key`). These commands were not run on the review host.

## Examples and demos

- Chess with Jev: [jev-agent.com/chess](https://jev-agent.com/chess)
- Wikipedia race: [jev-agent.com/wikirace](https://jev-agent.com/wikirace)
- Measured benchmarks: [jev-agent.com/benchmarks](https://jev-agent.com/benchmarks) and [WallerChen/jev-measured](https://github.com/WallerChen/jev-measured)

## Limits and data handling

Text you submit passes through jev-agent.com to TypeSafe; logging and retention on jev-agent.com were not inspected. Jev input is text only on this site. The free allowance is small, and keys are not interchangeable with TypeSafe keys.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) from the public homepage, chess and wikirace demos, pricing, docs, getting-started, benchmarks and llms.txt pages (HTTP 200) and the submission in [issue #1855](https://github.com/AppitStudio/awesome-jev/issues/1855). No account was created and no paid or live calls were made. Catalog checks (`npm run check`) ran locally; they verify navigation, not product claims. AI-assisted review.
