# @omadia/decision-jev (omadia plugin that lets Jev decide each chat message's route, data source, memory and evidence checks before any language-model call)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Plugin that makes Jev the decision model of the omadia agent platform: in one request it decides whether a message needs a language model, which read-only tool or data source can answer it, whether a learned query fits, and whether a plan is needed. It also rates recalled notes, whether a turn is worth remembering and whether evidence supports a claim; when Jev fails or is unsure, the language model takes over.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/byte5ai/omadia-jev-plugin) |
| Maintainer | [byte5ai](https://github.com/byte5ai). Independently curated. |
| Format | omadia plugin (TypeScript, packaged as a zip) |
| Requirements | omadia with `@omadia/plugin-api` 1.53.0+ and `@omadia/fast-path` 0.3.0+; a TypeSafe key (or an OpenRouter, LiteLLM or Zuplo gateway). |
| License | [MIT](https://github.com/byte5ai/omadia-jev-plugin/blob/1bfc0e5172d17ddafab54b41b05cd49cc56cbf79/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevClient.ts`](https://github.com/byte5ai/omadia-jev-plugin/blob/1bfc0e5172d17ddafab54b41b05cd49cc56cbf79/src/jevClient.ts) at the pinned commit. |

## When to use

- Skip the language-model call for messages that a tool or learned query can answer, with a fallback when Jev is unsure.
- Mismatch: only works inside omadia, and the fast path's thresholds are tuned per Jev version.

## How it works

`src/jevClient.ts` builds batched typed questions for `POST {base}/v1/systemone` (pinned `jev-1.14.0`, 1.5 s timeout) with a circuit breaker that pauses after three failures or on 429/401/403, and validates every answer against the requested options. Integration evidence: [`src/jevClient.ts`](https://github.com/byte5ai/omadia-jev-plugin/blob/1bfc0e5172d17ddafab54b41b05cd49cc56cbf79/src/jevClient.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/byte5ai/omadia-jev-plugin.git
cd omadia-jev-plugin
npm install
npm run typecheck && npm test
npm run build && npm run package   # out/omadia-decision-jev-<version>.zip
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the decision tasks, settings and guardrails: [github.com/byte5ai/omadia-jev-plugin#readme](https://github.com/byte5ai/omadia-jev-plugin#readme)

## Limits and data handling

Jev receives the chat message after omadia's Privacy Shield has masked it (when one runs) plus fixed option texts, and never tool results or rows; logs hold the task, choice, confidence, time and cost, not the message. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 1bfc0e5172d1](https://github.com/byte5ai/omadia-jev-plugin/tree/1bfc0e5172d17ddafab54b41b05cd49cc56cbf79). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
