# jev-sol-terra (Jev picks GPT-6.1 Sol or Terra and the reasoning effort for each step)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy between Codex, opencode or aider and the upstream API that decides, before every generation, whether GPT-6.1 Sol (hard code, deep questions) or Terra (clear instructions, computer use) should answer and how much reasoning effort to use, escalating when steps fail and stepping down after recovery; TypeSafe Jev makes the routing decisions through OpenRouter. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stevenke1981/jev-sol-terra) |
| Maintainer | [stevenke1981](https://github.com/stevenke1981). Independently curated. |
| Format | Node.js proxy |
| Requirements | Node.js; an OpenAI-compatible upstream key and an OpenRouter key for the Jev decisions. |
| License | [MIT](https://github.com/stevenke1981/jev-sol-terra/blob/615dac741afda21ec9e9b9be589a99f34eee4399/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions.js`](https://github.com/stevenke1981/jev-sol-terra/blob/615dac741afda21ec9e9b9be589a99f34eee4399/src/decisions.js) at the pinned commit. |

## When to use

- Cut cost on routine agent steps while escalating hard ones automatically.
- Mismatch: Jev is reached through OpenRouter; derived from the author's jev effort router.

## How it works

`src/decisions.js` sends the step context to `typesafe/jev-1.14` via the OpenRouter Decisions API; the proxy rewrites only the model and effort fields so the prompt cache stays warm. Integration evidence: [`src/decisions.js`](https://github.com/stevenke1981/jev-sol-terra/blob/615dac741afda21ec9e9b9be589a99f34eee4399/src/decisions.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/stevenke1981/jev-sol-terra.git && cd jev-sol-terra
npm link   # then see the README for client setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/stevenke1981/jev-sol-terra#readme](https://github.com/stevenke1981/jev-sol-terra#readme)

## Limits and data handling

Bounded step context goes to OpenRouter and on to TypeSafe for each decision; prompts go to your upstream as usual.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 615dac741afd](https://github.com/stevenke1981/jev-sol-terra/tree/615dac741afda21ec9e9b9be589a99f34eee4399). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
