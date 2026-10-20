# leis (working rules as enforced laws for Claude Code)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin (in Portuguese) that turns working rules into short named laws with a yes/no test, hooks that log every break, per-law observe or block modes and a measurement command, with Jev judging the checks that need judgement rather than a text rule.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/leonardocandiani/leis) |
| Maintainer | [leonardocandiani](https://github.com/leonardocandiani). Independently curated. |
| Format | Claude Code plugin (Node.js hooks) |
| Requirements | Claude Code and Node.js 22; a TypeSafe key (`TYPESAFE_API_KEY` or `AI_GATEWAY_API_KEY`) for the Jev-judged checks, which are optional. |
| License | [MIT](https://github.com/leonardocandiani/leis/blob/5d1ff21e9980fd64dea57a09f01eda06a3b04baf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev.mjs`](https://github.com/leonardocandiani/leis/blob/5d1ff21e9980fd64dea57a09f01eda06a3b04baf/scripts/jev.mjs) at the pinned commit. |

## When to use

- Stop repeating the same correction to a session that forgets `CLAUDE.md` rules.
- Measure how often each rule breaks over 24 hours and 7 days.
- Mismatch: README and commands are in Portuguese; hooks fail open.

## How it works

Hooks run at session start, at the end of each reply and before actions. Text checks are rules; checks that need judgement, such as whether a reply ends with a menu of offers, go to Jev through `scripts/jev.mjs` (direct `https://api.typesafe.ai/v1/systemone` or an AI gateway). Breaks are logged locally as JSONL and summarised by `/leis:leis-medir`. Integration evidence: [`scripts/jev.mjs`](https://github.com/leonardocandiani/leis/blob/5d1ff21e9980fd64dea57a09f01eda06a3b04baf/scripts/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add leonardocandiani/leis
claude plugin install leis@leis
# then, in a Claude Code session:
/leis:leis-implantar
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- testes/jev.test.mjs
- README sections on the six model laws and the measurement command

## Limits and data handling

Reply text is sent to TypeSafe for the Jev-judged checks. The log stays on your machine with tokens, emails and phone numbers masked, per the README.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 5d1ff21e9980](https://github.com/leonardocandiani/leis/tree/5d1ff21e9980fd64dea57a09f01eda06a3b04baf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
