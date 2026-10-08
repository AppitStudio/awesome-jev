# Jev + Claude Code case study

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent learning project testing what "Jev + Claude Code" means with two working programs: Triage Desk, a support-ticket app asking Jev six typed questions per ticket in one request with low-confidence cases going to human review, and Jev Guard, a Claude Code PreToolUse hook asking five redacted `noul` questions about ambiguous shell commands that never answers `allow`; both have offline evals and keyword baselines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gsaini/jev-claude-code-case-study) |
| Maintainer | [gsaini](https://github.com/gsaini). Independently curated. |
| Format | Python project (`triage-desk`, `jev-guard` CLIs; Claude Code hook) |
| Requirements | Python 3.11+ (uv optional); offline by default, `TYPESAFE_API_KEY` for live runs. |
| License | [MIT](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Understand where Jev fits around a coding agent before building your own.
- Reuse the guard's fail-safe design (no opinion ≠ allow).
- Mismatch: learning project; eval sets are small (40 tickets, 61 commands).

## How it works

[`src/jev_guard/hook.py`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/src/jev_guard/hook.py) and [`src/jev_guard/questions.py`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/src/jev_guard/questions.py) implement the guard; [`src/triage_desk/questions.py`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/src/triage_desk/questions.py) the triage questions. Research notes: [`docs/research.md`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/docs/research.md).

## Get started

Run offline (README *Quick start*):

```sh
git clone https://github.com/gsaini/jev-claude-code-case-study.git && cd jev-claude-code-case-study
uv sync
uv run triage-desk demo
uv run jev-guard check "git push --force origin main"
```

Offline runs are free; live mode bills your key.

## Examples and demos

- [`docs/jev-guard.md`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/docs/jev-guard.md) · [`docs/triage-desk.md`](https://github.com/gsaini/jev-claude-code-case-study/blob/58738e8cb1134e88738d7330e154eb0e6e676c26/docs/triage-desk.md).

## Limits and data handling

Live mode sends tickets / redacted commands to TypeSafe. Not affiliated with TypeSafe or Anthropic. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 58738e8cb113](https://github.com/gsaini/jev-claude-code-case-study/tree/58738e8cb1134e88738d7330e154eb0e6e676c26). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
