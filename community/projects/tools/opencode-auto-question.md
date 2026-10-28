# opencode-auto-question (opencode plugin that answers an autonomous agent's questions with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

opencode plugin for autonomous runs: when an agent on your list asks the `question` tool, a fast Jev Choice or Noul pass answers from the question and options, and a second pass can gather context with tools before answering; agents not on the list still ask the human.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jflowers/opencode-auto-question) |
| Maintainer | [jflowers](https://github.com/jflowers). Independently curated. |
| Format | opencode plugin (TypeScript) |
| Requirements | opencode; an OpenCode Zen or OpenRouter key (or an LLM for the JSON-contract engine). |
| License | [Apache-2.0](https://github.com/jflowers/opencode-auto-question/blob/5fe6edce6732c699ddadbe098af2036e060883e2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engines/jev.ts`](https://github.com/jflowers/opencode-auto-question/blob/5fe6edce6732c699ddadbe098af2036e060883e2/src/engines/jev.ts) at the pinned commit. |

## When to use

- Keep unattended opencode agents moving when they stop to ask questions.
- Mismatch: answers are guesses on your behalf; limit it to agents you trust to run alone.

## How it works

`src/engines/jev.ts` calls OpenCode Zen's `/zen/v1/systemone` (`jev-1.13`) or OpenRouter Decisions (`typesafe/jev-1.14`) with the question and options as Choice or Noul. Integration evidence: [`src/engines/jev.ts`](https://github.com/jflowers/opencode-auto-question/blob/5fe6edce6732c699ddadbe098af2036e060883e2/src/engines/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jflowers/opencode-auto-question && cd opencode-auto-question
cp config/auto-question.jsonc ~/.config/opencode/auto-question.jsonc
# add the repo path to the "plugin" array in ~/.config/opencode/opencode.jsonc
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jflowers/opencode-auto-question#readme](https://github.com/jflowers/opencode-auto-question#readme)

## Limits and data handling

Questions, options and gathered context go to OpenCode Zen or OpenRouter.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 5fe6edce6732](https://github.com/jflowers/opencode-auto-question/tree/5fe6edce6732c699ddadbe098af2036e060883e2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
