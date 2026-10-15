# ghwatch

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Ruby orchestrator that runs coding, review and finalizer agents off GitHub issues and pull requests, with optional TypeSafe Jev issue screening before work starts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/koshian/ghwatch) |
| Maintainer | [koshian](https://github.com/koshian). Independently curated. |
| Format | Ruby gem and CLI (alpha) |
| Requirements | Ruby 3.2+, Git, authenticated `gh`, the agent CLIs you configure; `TYPESAFE_API_KEY` only when `[triage.screening]` is enabled. |
| License | [MIT](https://github.com/koshian/ghwatch/blob/e9774cb216ca91c7825bd5f491063da22c5f3970/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/koshian/status/2110620654416634017)). |
| Jev evidence | [`lib/ghwatch/issue_screening.rb`](https://github.com/koshian/ghwatch/blob/e9774cb216ca91c7825bd5f491063da22c5f3970/lib/ghwatch/issue_screening.rb) at the pinned commit. |

## When to use

- Run issue-to-PR agent loops with GitHub as the shared conversation surface for human replies and review.
- Screen incoming issues with a cheap typed decision before an agent spends tokens on them.
- Mismatch: alpha software; Jev is an optional triage step, not the core of the orchestrator.

## How it works

With `[triage.screening]` enabled (off by default), Jev (`POST /v1/systemone`) judges each changed issue from its comments, open PRs and mentioned issues; only confident (`min_confidence`, default 0.8) deferred/followup/skip answers are settled there, and everything else goes on to the LLM triage role. If the key is missing or the call fails, triage continues without screening. The Jev client lives in `lib/ghwatch/jev.rb`. Integration evidence: [`lib/ghwatch/issue_screening.rb`](https://github.com/koshian/ghwatch/blob/e9774cb216ca91c7825bd5f491063da22c5f3970/lib/ghwatch/issue_screening.rb).

## Get started

From the upstream README (not run on the review host):

```sh
gem build ghwatch.gemspec
gem install --user-install ./ghwatch-*.gem
ghwatch --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration reference: `lib/ghwatch/default_config.toml` in the repository.

## Limits and data handling

Issue text goes to TypeSafe only when screening is enabled, billed to your key; agent CLIs you configure receive repository content under their own terms.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit e9774cb216ca](https://github.com/koshian/ghwatch/tree/e9774cb216ca91c7825bd5f491063da22c5f3970). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
