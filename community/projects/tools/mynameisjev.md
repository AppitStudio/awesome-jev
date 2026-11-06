# mynameisjev (Claude Code plugin that routes each message with TypeSafe Jev via OpenRouter)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that sizes every user message and asks TypeSafe Jev (served as `typesafe/jev-1.14` on OpenRouter) whether a cheaper Claude model, a stronger one, or Codex should handle it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bradsec/mynameisjev) |
| Maintainer | [bradsec](https://github.com/bradsec). Independently curated. |
| Format | Claude Code plugin (JavaScript, MIT) |
| Requirements | Claude Code with the plugin installed and an OpenRouter API key that can call `typesafe/jev-1.14`. |
| License | [MIT](https://github.com/bradsec/mynameisjev/blob/9bfeacf98d81e7fa10653eeff591439e4b4e6896/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin/scripts/jev-api.js`](https://github.com/bradsec/mynameisjev/blob/9bfeacf98d81e7fa10653eeff591439e4b4e6896/plugin/scripts/jev-api.js) at the pinned commit. |

## When to use

- Route Claude Code traffic by message difficulty.
- Prefer OpenRouter's TypeSafe Jev decision endpoint.
- Mismatch: OpenRouter-only client in the reviewed tip; not a direct api.typesafe.ai SDK.

## How it works

`plugin/scripts/jev-api.js` POSTs structured decision requests to `https://openrouter.ai/api/alpha/decisions` with model `typesafe/jev-1.14` and returns the parsed answers used by the router hook. Integration evidence: [`plugin/scripts/jev-api.js`](https://github.com/bradsec/mynameisjev/blob/9bfeacf98d81e7fa10653eeff591439e4b4e6896/plugin/scripts/jev-api.js).

## Get started

Install the Claude Code plugin per README and configure an OpenRouter key that can call TypeSafe Jev.

```sh
git clone https://github.com/bradsec/mynameisjev.git && cd mynameisjev
# follow README Claude Code plugin install
export OPENROUTER_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bradsec/mynameisjev/blob/9bfeacf98d81e7fa10653eeff591439e4b4e6896/README.md](https://github.com/bradsec/mynameisjev/blob/9bfeacf98d81e7fa10653eeff591439e4b4e6896/README.md)

## Limits and data handling

Redacted message state and routing questions are sent to OpenRouter on your key. Review the plugin's redaction helpers before enabling on sensitive repos.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 9bfeacf98d81](https://github.com/bradsec/mynameisjev/tree/9bfeacf98d81e7fa10653eeff591439e4b4e6896). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
