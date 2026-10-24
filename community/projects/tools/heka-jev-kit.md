# Jev kit by Mr-heka (record browser or Mac app chores and replay them with Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Skill for Claude Code and Codex: the agent records a browser or Mac app chore into a recipe once, then a runner replays it at machine speed, sending only fuzzy calls (right page, right result, which option fits) to Jev through OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Mr-heka/jev-kit) |
| Maintainer | [Mr-heka](https://github.com/Mr-heka). Independently curated. |
| Format | Agent skill with Python scripts |
| Requirements | Python 3.9+; an OpenRouter account with credit; Playwright for web replay; screen engine on macOS only. |
| License | [MIT](https://github.com/Mr-heka/jev-kit/blob/ea55616578ed92b79e35d0dd5a010be427eceae2/LICENSE.txt) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jevkit/client.py`](https://github.com/Mr-heka/jev-kit/blob/ea55616578ed92b79e35d0dd5a010be427eceae2/scripts/jevkit/client.py) at the pinned commit. |

## When to use

- Repeat the same web or app chore without paying a big model each time.
- Rank items against a rubric with typed answers.
- Mismatch: stops at purchase, send or delete buttons until you approve.

## How it works

`client.py` posts to OpenRouter's Decisions endpoint (`https://openrouter.ai/api/alpha/decisions`) with `typesafe/jev-1.14` by default; every run has call and cost caps. Integration evidence: [`scripts/jevkit/client.py`](https://github.com/Mr-heka/jev-kit/blob/ea55616578ed92b79e35d0dd5a010be427eceae2/scripts/jevkit/client.py).

## Get started

From the upstream README (not run on the review host): paste the prompt in SETUP-PROMPT.md into Claude Code or Codex, which installs the kit. For web replay:

```sh
pip install playwright
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup prompt: [github.com/Mr-heka/jev-kit/blob/main/SETUP-PROMPT.md](https://github.com/Mr-heka/jev-kit/blob/main/SETUP-PROMPT.md)

## Limits and data handling

Only the fields a judgment needs are sent to Jev via OpenRouter. It never types passwords or card numbers.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit ea55616578ed](https://github.com/Mr-heka/jev-kit/tree/ea55616578ed92b79e35d0dd5a010be427eceae2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
