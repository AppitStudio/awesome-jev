# Navigator (qf-studio)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-engineering plugin for Claude Code (loop mode, research, memories, live `/nav` pane) whose keyword prompt gates can get an optional typed TypeSafe Jev judge — one request per prompt, decisive answers override, the rest fall back to keywords.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qf-studio/navigator) |
| Product homepage | [quantflow.studio](https://quantflow.studio) |
| Maintainer | [qf-studio](https://github.com/qf-studio). Independently curated. |
| Format | Claude Code plugin with hooks, skills and a terminal pane |
| Requirements | Claude Code 2.1.287+; for the judge, `TYPESAFE_API_KEY` (or `~/.config/typesafe/api_key`, mode 600). |
| License | [MIT](https://github.com/qf-studio/navigator/blob/0da404a959036976e53ec408f04d0c14ba9789fe/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route long Claude Code sessions into the right workflow (loop mode, research, plain reply) with fewer missed triggers than keyword matching alone.
- Keep the gate cheap: one typed Jev call per prompt instead of an extra LLM turn.
- Mismatch: the judge sends each prompt's text to TypeSafe, which is why upstream leaves it off by default.

## How it works

Navigator's loop-trigger, complexity and ambiguity detectors are keyword matchers. With the judge enabled (v7.7.0), each prompt goes to Jev as one typed request; decisive answers override the keyword result and uncertain ones fall back to it. The maintainer reports tier accuracy rising from 38 to 53 of 60 labelled prompts. Setup and tuning are in `.agent/sops/integrations/typesafe-judge-setup.md`; `python3 hooks/nav_hook_lib/judge.py --check` verifies the configuration ([README](https://github.com/qf-studio/navigator/blob/0da404a959036976e53ec408f04d0c14ba9789fe/README.md#optional-typed-prompt-judge)).

## Get started

Install the plugin, then enable the judge (live TypeSafe call per prompt):

```sh
/plugin marketplace add qf-studio/navigator
/plugin install navigator
export TYPESAFE_API_KEY=...
# in Claude Code: "enable judge"
python3 hooks/nav_hook_lib/judge.py --check   # from the plugin root
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README *Optional: Typed Prompt Judge* and `hooks/nav_hook_lib/fixtures/judge_eval.json` / `judge_eval_recorded.json` (labelled prompts and recorded judge results).
- `hooks/mod/lib/judge.ts` and its tests in `hooks/mod/tests/judge.test.ts`.

## Limits and data handling

Prompt text leaves the machine when the judge is on. The 38 → 53 figure is a maintainer measurement on 60 prompts and was not reproduced. Navigator's other features do not use Jev.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 0da404a95903](https://github.com/qf-studio/navigator/tree/0da404a959036976e53ec408f04d0c14ba9789fe). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
