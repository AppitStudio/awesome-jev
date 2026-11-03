# kickroll (orchestrator that plans a task, freezes acceptance tests and retries Claude Code workers up a model ladder, with optional Jev routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Deterministic orchestrator for Claude Code workers: it plans a task, freezes the acceptance tests, hands each sub-task to a `claude -p` worker on the cheapest model likely to do the job, checks the result with real tests, and retries with feedback on a stronger model until the checks pass or a budget runs out. It runs on your Claude subscription with no Anthropic API key. A Jev key is optional and lets Jev decide which model each request gets and screen results as a filter that never accepts on its own.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nicoflbr/kickroll) |
| Maintainer | [nicoflbr](https://github.com/nicoflbr). Independently curated. |
| Format | Python command-line tool (standard library only; optional `kickroll[jev]` extra) |
| Requirements | Python 3.11+, git, Claude Code logged in; optionally `pip install "kickroll[jev]"` and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/nicoflbr/kickroll/blob/bdcf9ee6f022193242452559d9b8ba26face2e0c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`kickroll/jev.py`](https://github.com/nicoflbr/kickroll/blob/bdcf9ee6f022193242452559d9b8ba26face2e0c/kickroll/jev.py) at the pinned commit. |

## When to use

- Run a test-driven loop of Claude Code workers that starts cheap and escalates only when tests fail.
- Mismatch: experimental v0.2, tested on Windows only, and the cheaper-or-better claim is not measured yet.

## How it works

`kickroll/jev.py` calls the TypeSafe SDK's `system_one` with small Choice, Score and Noul questions (`jev-latest`) under an overall deadline; routing falls back to the planner's annotations or a heuristic when Jev is off, and Jev's verification can reject or send work to review but never accepts alone. Integration evidence: [`kickroll/jev.py`](https://github.com/nicoflbr/kickroll/blob/bdcf9ee6f022193242452559d9b8ba26face2e0c/kickroll/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install .
kickroll plan "Add a CLI flag --json to report.py and cover it with tests" --test-cmd "python -m unittest discover -s tests" --dry
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the plan, run and bench commands: [github.com/nicoflbr/kickroll#readme](https://github.com/nicoflbr/kickroll#readme)

## Limits and data handling

Workers and test commands run unsandboxed under your user account, so use trusted repositories or a disposable checkout. With Jev enabled, task text (and diffs for verification) goes to TypeSafe on your key; Jev thresholds are not calibrated. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit bdcf9ee6f022](https://github.com/nicoflbr/kickroll/tree/bdcf9ee6f022193242452559d9b8ba26face2e0c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
