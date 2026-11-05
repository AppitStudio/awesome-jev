# local-orchestra (local-first coding pipeline where three expert models propose, Jev picks the winner and a coder applies and verifies, failing closed)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first LLM orchestrator for code tasks: a council of three independent senior-engineer models proposes, Jev (typesafe/jev-1.14 via OpenRouter) chooses the winning proposal with a typed Choice question, a coder applies the change in the workspace with backups, and Jev or an LLM reviews the diff. If Jev cannot give a valid answer the run stops (fail-closed) and every step is logged as JSONL.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ketenci7enes/local-orchestra) |
| Maintainer | [ketenci7enes](https://github.com/ketenci7enes). Independently curated. |
| Format | Python command-line orchestrator |
| Requirements | Python 3.11+ and an OpenRouter key; the README documents a free fallback model list. |
| License | [MIT](https://github.com/ketenci7enes/local-orchestra/blob/962d6e71f76ea36a59ecff2129716469a39c6ebc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`judge.py`](https://github.com/ketenci7enes/local-orchestra/blob/962d6e71f76ea36a59ecff2129716469a39c6ebc/judge.py) at the pinned commit. |

## When to use

- Study a council-then-judge pattern where a decision model picks between proposals.
- Run code changes with logged, replayable steps and backups.
- Mismatch: README is in Turkish; the LLM fallback decider can take over if Jev fails.

## How it works

`judge.py` sends `{goal, proposals}` to the OpenRouter decisions endpoint (with `/v1/systemone` as a fallback), asks for the best option, flags close calls by confidence gap and raises `JevUnavailable` when no valid option is returned. Integration evidence: [`judge.py`](https://github.com/ketenci7enes/local-orchestra/blob/962d6e71f76ea36a59ecff2129716469a39c6ebc/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py --workspace . [--auto] [--git] [--no-jev]
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Turkish) with the Jev decision mechanism: [github.com/ketenci7enes/local-orchestra/blob/962d6e71f76ea36a59ecff2129716469a39c6ebc/README.md](https://github.com/ketenci7enes/local-orchestra/blob/962d6e71f76ea36a59ecff2129716469a39c6ebc/README.md)

## Limits and data handling

Task text and proposals go to OpenRouter and the models you configure; the tool edits files in the workspace you point it at, so use version control. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 962d6e71f76e](https://github.com/ketenci7enes/local-orchestra/tree/962d6e71f76ea36a59ecff2129716469a39c6ebc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
