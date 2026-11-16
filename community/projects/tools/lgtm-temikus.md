# LGTM by Temikus (GitHub workflow that scores pull requests with Jev into approve, deny or needs-human, starting in shadow mode)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go CLI and pair of GitHub workflows that ask a decision model typed questions about each pull request: is the diff aligned with its description, scoped, free of malice and security mistakes, tested? The 0-1 answers combine into one verdict, approve, deny or needs-human, that you can gate a merge on; a malice veto and many caps (prompt injection, unusual lockfile registries, files that auto-run on developer machines, sensitive paths, fork PRs, large diffs) hold approvals for a human. It starts in shadow mode, posting a check and one comment without gating, and never writes reviews, approves or merges. A typical PR costs a fraction of a cent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Temikus/lgtm) |
| Maintainer | [Temikus](https://github.com/Temikus). Independently curated. |
| Format | Go CLI + GitHub Actions workflows (Apache-2.0) |
| Requirements | Go to install the CLI, a GitHub repository, and an OpenRouter key (default) or `TYPESAFE_API_KEY` for TypeSafe direct. |
| License | [Apache-2.0](https://github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/jev/client.go`](https://github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/internal/jev/client.go) at the pinned commit. |

## When to use

- Add a cheap typed mistake detector next to human reviewers on pull requests.
- Mismatch: a security boundary or a replacement for required human review, as the README says.

## How it works

`internal/jev/client.go` posts the questions to `{base}/systemone` on OpenRouter or `https://api.typesafe.ai/v1` (TypeSafe), with `cmd/lgtm/env.go` reading `LGTM_API_KEY` or `TYPESAFE_API_KEY` for the TypeSafe provider; the default model is `typesafe/jev-1.13`. Integration evidence: [`internal/jev/client.go`](https://github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/internal/jev/client.go).

## Get started

Install the CLI, write the workflows and add the key as a repository secret.

```sh
go install github.com/Temikus/lgtm/cmd/lgtm@latest
lgtm init                    # writes two workflows and .github/lgtm.toml
gh secret set OPENROUTER_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/README.md](https://github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/README.md)
- Calibration notes: [github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/docs/calibration.md](https://github.com/Temikus/lgtm/blob/5a973fff907f2d2f7afb2bbe712b458f16228446/docs/calibration.md)

## Limits and data handling

PR titles, descriptions, linked issue titles and diffs go to the model provider; excluded paths are never sent. Early v0 with thresholds calibrated in the repo's own docs.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 5a973fff907f](https://github.com/Temikus/lgtm/tree/5a973fff907f2d2f7afb2bbe712b458f16228446). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
