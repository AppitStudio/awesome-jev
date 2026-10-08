# Jev Model Router (Codex skill)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex skill (Chinese and English docs) where the parent session condenses a non-trivial task and asks TypeSafe Jev to recommend the model tier and reasoning effort for an execution subagent; a standard-library Python script validates the answer against local policy and outputs one JSON decision, keeping the current model on timeout or invalid responses.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrhsiung2015/jev-model-router) |
| Maintainer | [mrhsiung2015](https://github.com/mrhsiung2015). Independently curated. |
| Format | Codex skill folder (`SKILL.md` + `scripts/route.py`) |
| Requirements | Codex with skills and subagents; `TYPESAFE_API_KEY` (or `JEV_API_KEY`). |
| License | [MIT](https://github.com/mrhsiung2015/jev-model-router/blob/1c75436d29dde55139a66f3f2e76d18df5a9b197/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Avoid hand-picking a model for every delegated Codex task.
- Mismatch: cannot switch the running parent session's model.

## How it works

[`scripts/route.py`](https://github.com/mrhsiung2015/jev-model-router/blob/1c75436d29dde55139a66f3f2e76d18df5a9b197/scripts/route.py) sends the task summary to Jev and applies policy; [`SKILL.md`](https://github.com/mrhsiung2015/jev-model-router/blob/1c75436d29dde55139a66f3f2e76d18df5a9b197/SKILL.md) tells Codex how to delegate. English README: [`README.en.md`](https://github.com/mrhsiung2015/jev-model-router/blob/1c75436d29dde55139a66f3f2e76d18df5a9b197/README.en.md).

## Get started

Clone into your Codex skills folder (README *Install*):

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/mrhsiung2015/jev-model-router.git "${CODEX_HOME:-$HOME/.codex}/skills/jev-model-router"
```

One Jev request per routed task on your key.

## Examples and demos

- Tests: [`tests/test_route.py`](https://github.com/mrhsiung2015/jev-model-router/blob/1c75436d29dde55139a66f3f2e76d18df5a9b197/tests/test_route.py).

## Limits and data handling

The task summary goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 1c75436d29dd](https://github.com/mrhsiung2015/jev-model-router/tree/1c75436d29dde55139a66f3f2e76d18df5a9b197). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
