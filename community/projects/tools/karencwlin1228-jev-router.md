# jev-router (KarenCWLin1228)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Python CLI that asks TypeSafe Jev which model tier (fast / standard / deep) a coding task needs and returns a recommendation Claude Code, Codex or Antigravity can act on, plus a `jev-model-router` agent skill wiring it into those hosts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KarenCWLin1228/jev-router) |
| Maintainer | [KarenCWLin1228](https://github.com/KarenCWLin1228). Independently curated. |
| Format | Python CLI (`jev-router`, installed with uv from GitHub) and agent skill in `skills/jev-model-router/` |
| Requirements | Python with uv, a `TYPESAFE_API_KEY` (in `~/.config/jev/.env`) and a `models.json` mapping tiers to your models; `launch`/`collect` need Windows and Orca. |
| License | [MIT](https://github.com/KarenCWLin1228/jev-router/blob/55182807a7a64506b2a07e3605db56e370f11231/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Let Claude Code or Codex ask, per task, whether a cheap fast model is enough or a deep model is needed.
- Use `--route deep` or `--dry-run` to fix the tier without any API call.
- Mismatch: CLI messages and the Antigravity worker prompt are in Traditional Chinese; model names in `models.json` are not checked against your account.

## How it works

[`src/jev_router/client.py`](https://github.com/KarenCWLin1228/jev-router/blob/55182807a7a64506b2a07e3605db56e370f11231/src/jev_router/client.py) sends the question and optional context to `api.typesafe.ai/v1/systemone`; [`routing.py`](https://github.com/KarenCWLin1228/jev-router/blob/55182807a7a64506b2a07e3605db56e370f11231/src/jev_router/routing.py) maps Jev's choice to a tier from `models.json`. The [`jev-model-router` skill](https://github.com/KarenCWLin1228/jev-router/tree/55182807a7a64506b2a07e3605db56e370f11231/skills/jev-model-router) has host notes for Claude Code, Codex and Antigravity.

## Get started

Install the CLI from GitHub (README *Install*):

```sh
uv tool install git+https://github.com/KarenCWLin1228/jev-router
export TYPESAFE_API_KEY=...        # or ~/.config/jev/.env
jev-router recommend --client claude "refactor the auth module"
```

Each `recommend` without `--route`/`--dry-run` is one Jev request billed to your TypeSafe key.

## Examples and demos

- README *Commands* (`recommend` with short follow-ups, long questions from files, fixed tier).
- Skill: [`skills/jev-model-router/SKILL.md`](https://github.com/KarenCWLin1228/jev-router/blob/55182807a7a64506b2a07e3605db56e370f11231/skills/jev-model-router/SKILL.md).

## Limits and data handling

Your question and context go to TypeSafe; upstream states no cache or history is kept and the key is never logged. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 55182807a7a6](https://github.com/KarenCWLin1228/jev-router/tree/55182807a7a64506b2a07e3605db56e370f11231). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
