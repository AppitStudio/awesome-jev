# jev-gpt (single-model GPT-6.1 Terra proxy for Codex: Jev picks reasoning effort and resumes tasks that stop early)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy between Codex (or any Chat Completions client) and one GPT model, GPT-6.1 Terra by default: before each generation Jev reads the turn so far and sets reasoning effort from low to xhigh, and when the model stops before the task is done Jev detects it and the proxy resumes. A sibling of the listed jev-sol-terra by the same author. Chinese-language docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stevenke1981/jev-gpt) |
| Maintainer | [stevenke1981](https://github.com/stevenke1981). Independently curated. |
| Format | Node.js proxy |
| Requirements | Node.js, Codex or another Chat Completions client, and an OpenRouter key. |
| License | [MIT](https://github.com/stevenke1981/jev-gpt/blob/871082fd675dd96d37f294370dcea9356b510e6a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions.js`](https://github.com/stevenke1981/jev-gpt/blob/871082fd675dd96d37f294370dcea9356b510e6a/src/decisions.js) at the pinned commit. |

## When to use

- Spend high reasoning effort only where a long Codex task needs it.
- Mismatch: Chinese docs; tied to one upstream model.

## How it works

`src/decisions.js` calls TypeSafe Jev (`typesafe/jev-1.14`) through OpenRouter's Decisions API for an effort score and an unfinished-task check on each generation. Integration evidence: [`src/decisions.js`](https://github.com/stevenke1981/jev-gpt/blob/871082fd675dd96d37f294370dcea9356b510e6a/src/decisions.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/stevenke1981/jev-gpt && cd jev-gpt
# see the README (Chinese) for the Codex profile and port 8789 setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/stevenke1981/jev-gpt#readme](https://github.com/stevenke1981/jev-gpt#readme)

## Limits and data handling

Turn summaries go to OpenRouter for the Jev decision; prompts go to the upstream GPT model.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 871082fd675d](https://github.com/stevenke1981/jev-gpt/tree/871082fd675dd96d37f294370dcea9356b510e6a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
