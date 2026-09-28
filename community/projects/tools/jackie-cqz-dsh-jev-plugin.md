# dsh-jev-plugin (jackie-cqz)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin for TypeSafe Jev: typed decisions, configurable guardrails, and Web UI result cards.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jackie-cqz/dsh-jev-plugin) |
| Maintainer | [jackie-cqz](https://github.com/jackie-cqz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | DeepSeek Harness (DSH) Cordis plugin package. |
| Requirements | Node.js ≥22; DeepSeek Harness ≥0.1.6-alpha.2 <0.2.0; `TYPESAFE_API_KEY` for live judgments. |
| License | [MIT](https://github.com/jackie-cqz/dsh-jev-plugin/blob/57c0276b4b2c9bfae92c2a4f30b6415f29834463/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [dsh-jev](dsh-jev.md), [dsh-jev-decide](dsh-jev-decide.md), and related DSH plugins. |

## When to use

Use when a DeepSeek Harness agent should call TypeSafe Jev for typed decisions with guardrails and UI cards. Prefer narrower dsh-jev* plugins if you already standardize on one tool name.

## How it works

Registers Jev noul/choice/score tools for DSH agents with configurable guardrails and Web UI result cards. Installed via `dsh.bundle` / plugin add without forking DSH. Distinct from dsh-jev, dsh-jev-decide, dsh-jev-verify, and related plugins. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/jackie-cqz/dsh-jev-plugin.git
cd dsh-jev-plugin
git checkout 57c0276b4b2c9bfae92c2a4f30b6415f29834463
npm ci --legacy-peer-deps
# dsh plugin --profile jev-dev add /path/to/dsh-jev-plugin — follow upstream README
```

Pin revision `57c0276b4b2c9bfae92c2a4f30b6415f29834463` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live DSH/TypeSafe and browser result-card paths not run on the review host. Target DSH 0.1.7-rc.2 per upstream. Distinct from other dsh-jev* listings.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 57c0276](https://github.com/jackie-cqz/dsh-jev-plugin/tree/57c0276b4b2c9bfae92c2a4f30b6415f29834463). AI-assisted README and LICENSE inspection; install/live paths not executed.
