# jev-tier-router (Hermes Agent plugin routing each turn to Haiku or Opus with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that asks Jev through OpenRouter's Decisions API once per turn whether a fast model can handle it, then sends the turn to Claude Haiku or Opus; fails open.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vhsgreed/jev-tier-router) |
| Maintainer | [vhsgreed](https://github.com/vhsgreed). Independently curated. |
| Format | Hermes plugin (Python, MIT; experimental) |
| Requirements | Hermes Agent ≥ 0.21.5 on the Claude subscription provider and an `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/vhsgreed/jev-tier-router/blob/0cd86e555b9db2b466d9308868b2d464a93184ae/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`__init__.py`](https://github.com/vhsgreed/jev-tier-router/blob/0cd86e555b9db2b466d9308868b2d464a93184ae/__init__.py) at the pinned commit. |

## When to use

- Save subscription usage on simple turns.
- Log routing decisions for review.
- Mismatch: experimental snapshot; the author disabled it after brief use.

## How it works

`__init__.py` posts to `https://openrouter.ai/api/alpha/decisions` with `~typesafe/jev-latest` and logs each decision to `jev-tier-router-decisions.jsonl`; errors fall back to the default model. Integration evidence: [`__init__.py`](https://github.com/vhsgreed/jev-tier-router/blob/0cd86e555b9db2b466d9308868b2d464a93184ae/__init__.py).

## Get started

Install with `hermes plugins install vhsgreed/jev-tier-router` and enable it.

```sh
hermes plugins install vhsgreed/jev-tier-router
hermes plugins enable jev-tier-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/vhsgreed/jev-tier-router/blob/0cd86e555b9db2b466d9308868b2d464a93184ae/README.md](https://github.com/vhsgreed/jev-tier-router/blob/0cd86e555b9db2b466d9308868b2d464a93184ae/README.md)

## Limits and data handling

Each user turn is sent to OpenRouter/TypeSafe for classification.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 0cd86e555b9d](https://github.com/vhsgreed/jev-tier-router/tree/0cd86e555b9db2b466d9308868b2d464a93184ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
