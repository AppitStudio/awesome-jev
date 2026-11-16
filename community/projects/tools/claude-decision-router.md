# Decision Router by frankievalentine (Claude Code plugin that picks Haiku, Sonnet, Opus or Fable for each message from a decision model's rating and your usage limits)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that chooses the Claude model for each message so a subscription goes further: a small decision model rates each prompt (how hard, how much code, whether it touches security) and a policy that knows your 5-hour and weekly limits turns that into Haiku, Sonnet, Opus or Fable, shown in a band under the prompt. `/router setup` picks and tests the decision model; optional subagent routing is off by default. Decision model choices: a local llama.cpp server (for example Clef Flash), Unsloth or SGLang, Cloudflare Workers AI Clef, or TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/frankievalentine/claude-decision-router) |
| Maintainer | [frankievalentine](https://github.com/frankievalentine). Independently curated. |
| Format | Claude Code plugin (TypeScript hooks) |
| Requirements | Claude Code 2.1.299+ and one decision model: a TypeSafe API key for Jev, or a local llama.cpp/Unsloth server or Cloudflare Workers AI token. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin/src/classifier.ts`](https://github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/plugin/src/classifier.ts) at the pinned commit. |

## When to use

- Stretch a Claude subscription by sending easy turns to smaller models automatically.
- Mismatch: API users who pick models per request themselves.

## How it works

`plugin/src/classifier.ts` sends the rating questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` when TypeSafe is the chosen decision model; the other backends share the same question set. Integration evidence: [`plugin/src/classifier.ts`](https://github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/plugin/src/classifier.ts).

## Get started

Install from the marketplace, then run setup and choose TypeSafe Jev as the decision model.

```sh
/plugin install decision-router --marketplace frankievalentine/claude-decision-router
/router setup    # choose TypeSafe Jev and paste your key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/README.md](https://github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/README.md)
- Privacy notice: [github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/PRIVACY.md](https://github.com/frankievalentine/claude-decision-router/blob/e61d6f9739850717d70845977cc693ff91b4bdec/PRIVACY.md)

## Limits and data handling

Jev is one of four decision backends; local llama.cpp is an alternative that keeps text on your machine. With Jev, the first 6,000 characters of your message and short snippets of the last two messages go to TypeSafe on your key, per the plugin's privacy notice. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit e61d6f973985](https://github.com/frankievalentine/claude-decision-router/tree/e61d6f9739850717d70845977cc693ff91b4bdec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
