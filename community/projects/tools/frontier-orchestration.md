# Frontier Orchestration by bebecap (agent skill and plugin that routes tasks across Claude, Codex and Gemini with a decision engine such as Jev, then has another vendor's model review the result)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Skill and plugin for Claude Code, Codex and Antigravity (or any agent that reads `SKILL.md`). A decision engine picks the model tier for each task, and a model from a different vendor reviews the work. The engine can be TypeSafe Jev, OpenJev or local rules. The README reports routing pick accuracy of 1.00 for Jev against 0.60 for the local-rules baseline on 20 labeled tasks, with 12 of 20 routed below frontier tier and 8 of 9 high-stakes tasks kept on top models (self-measured on 2026-11-16; no dollar savings measured). Standard library Python only.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bebecap/frontier-orchestration) |
| Maintainer | [bebecap](https://github.com/bebecap). Independently curated. |
| Format | Agent skill and plugin (Python standard library, MIT) |
| Requirements | Python 3.9+ on macOS or Linux, and the Claude, Codex or Gemini CLIs you want routed; a TypeSafe key or an OpenJev server for the Jev engine, or local rules with no key. |
| License | [MIT](https://github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/frontier-orchestration/scripts/fo_jev.py`](https://github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/skills/frontier-orchestration/scripts/fo_jev.py) at the pinned commit. |

## When to use

- Route routine tasks to cheaper models and keep high-stakes work on top models, with a cross-vendor review.
- Mismatch: a measured cost saver; the author measured routing accuracy, not dollars.

## How it works

`skills/frontier-orchestration/scripts/fo_jev.py` posts the routing questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`; the default model is `openjev-latest`) with the key read from the environment, a keychain or a file you choose. Integration evidence: [`skills/frontier-orchestration/scripts/fo_jev.py`](https://github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/skills/frontier-orchestration/scripts/fo_jev.py).

## Get started

Install through your agent's plugin or skills command, then run the setup command.

```sh
# Claude Code
/plugin marketplace add bebecap/frontier-orchestration
/plugin install frontier-orchestration@frontier-orchestration
/frontier-orchestration:setup
# any SKILL.md agent
npx skills add bebecap/frontier-orchestration --skill frontier-orchestration
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evaluation: [github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/docs/eval.md](https://github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/docs/eval.md)
- Cost notes: [github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/docs/cost.md](https://github.com/bebecap/frontier-orchestration/blob/03ed65f0743c6f58836df2564baab5fd868609f8/docs/cost.md)

## Limits and data handling

Task descriptions sent to the engine go to TypeSafe (or your OpenJev server) and routed work goes to the vendors you pick, each on your own accounts. The accuracy figures are the author's on a small labeled set and were not reproduced here.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit 03ed65f0743c](https://github.com/bebecap/frontier-orchestration/tree/03ed65f0743c6f58836df2564baab5fd868609f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
