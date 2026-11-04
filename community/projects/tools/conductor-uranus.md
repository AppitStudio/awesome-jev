# Conductor (Claude Code plugin that splits a goal into tasks and runs them in parallel across Claude, Codex, OpenCode, Cursor and Antigravity, with Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin where Claude writes a plan (tasks, acceptance criteria, files touched, dependencies) and a conductor runs the tasks in parallel, each worker in its own git worktree without your `.env` files. Jev picks the worker, the model tier and the workflow for each task; plain rules decide when Jev is not configured, and risky paths such as `auth/`, `billing/`, migrations and tax code always get the strictest workflow. A `shadow` mode logs Jev's answers while rules decide.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uranus-workspace/conductor) |
| Maintainer | [uranus-workspace](https://github.com/uranus-workspace). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code, git and at least one signed-in worker CLI (`claude`, `codex`, `opencode`, `cursor-agent` or `agy`); OpenRouter for model calls including Jev. |
| License | [MIT](https://github.com/uranus-workspace/conductor/blob/eea71847cd219e19cbe118cc037097e4b1e09ead/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/adapters/decision/jev.ts`](https://github.com/uranus-workspace/conductor/blob/eea71847cd219e19cbe118cc037097e4b1e09ead/src/adapters/decision/jev.ts) at the pinned commit. |

## When to use

- Run several coding agents on separate tasks in parallel and let a decision model route each one.
- Mismatch: Jira, Linear and Figma integrations are tested only against simulated servers, and spending is capped by your own budget settings.

## How it works

`src/adapters/decision/jev.ts` builds typed noul, choice and score questions for OpenRouter's System One API, redacts the state, and validates every answer (unreadable ones are left out, never guessed); `decision.mode` is `rules`, `shadow` or `enforce`. Integration evidence: [`src/adapters/decision/jev.ts`](https://github.com/uranus-workspace/conductor/blob/eea71847cd219e19cbe118cc037097e4b1e09ead/src/adapters/decision/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add uranus-workspace/conductor
/plugin install conductor@uranus
/conduct plan
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the workflow, configuration and security notes: [github.com/uranus-workspace/conductor#readme](https://github.com/uranus-workspace/conductor#readme)

## Limits and data handling

Task text goes to OpenRouter on your key, with API keys and Brazilian CPF/CNPJ numbers masked first; workers can spend your provider credits up to the per-task, per-run and per-day budgets you set. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit eea71847cd21](https://github.com/uranus-workspace/conductor/tree/eea71847cd219e19cbe118cc037097e4b1e09ead). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
