# jev-lint (ckorhonen)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fuzzy linter for coding agents—flags team best-practice violations while the agent is still writing, not at review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ckorhonen/jev-lint) |
| Maintainer | [ckorhonen](https://github.com/ckorhonen). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Agent hook + rule packs; site at jevlint.dev. |
| Requirements | Bun/Node; Claude Code or Codex hooks; TypeSafe/judge key per upstream; optional local models. |
| License | [MIT](https://github.com/ckorhonen/jev-lint/blob/05ecfa8576047ad044b9ecca9984dea4e8ac6b7b/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [jev-lint (mizchi)](jev-lint.md) and [JevLint (huntedman)](jevlint.md). Site: [jevlint.dev](https://jevlint.dev). |

## When to use

Use when coding agents should get fast fuzzy lint feedback mid-edit. Prefer mizchi/jev-lint or Ice-Hazymoon/jevlint for CLI-centric semantic lint.

## How it works

Post-edit hooks score agent-written files against opinionated language packs using fuzzy/Jev-style judgments; fail-open so edits are never blocked. Distinct from mizchi/jev-lint (ast-grep CLI) and huntedman/JevLint. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ckorhonen/jev-lint.git
cd jev-lint
git checkout 05ecfa8576047ad044b9ecca9984dea4e8ac6b7b
# follow upstream README / jevlint.dev for hook install and rule packs
```

Pin revision `05ecfa8576047ad044b9ecca9984dea4e8ac6b7b` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Violation-reduction stats are upstream-reported. Live agent/hook/provider paths not run on the review host. Distinct from mizchi/jev-lint and huntedman/JevLint.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 05ecfa8](https://github.com/ckorhonen/jev-lint/tree/05ecfa8576047ad044b9ecca9984dea4e8ac6b7b). AI-assisted README and LICENSE inspection; install/live paths not executed.
