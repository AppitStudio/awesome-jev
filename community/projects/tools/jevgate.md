# jevgate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust CLI that gates a shell pipeline on a yes/no Jev judgment: text passes through (or a command runs) only when P(yes) clears a threshold — a smarter cron/grep.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gordonbrander/jevgate) |
| Maintainer | [gordonbrander](https://github.com/gordonbrander). Independently curated. |
| Format | Rust CLI |
| Requirements | Rust 1.85+; TypeSafe API key (`JEV_API_KEY`). |
| License | [MIT](https://github.com/gordonbrander/jevgate/blob/6d9eb915a606393bbc29aaed0194b7ce74ff7eec/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/provider.rs`](https://github.com/gordonbrander/jevgate/blob/6d9eb915a606393bbc29aaed0194b7ce74ff7eec/src/provider.rs) at the pinned commit. |

## When to use

- Run a notification or script only when cron output is really an outage.
- Filter streams of text with a natural-language yes/no question.
- Mismatch: one question per invocation; not a workflow engine.

## How it works

jevgate reads stdin, sends it with your question as a Noul request to `api.typesafe.ai/v1/systemone`, and passes the text through or runs the command after `--` when the score clears the threshold. Integration evidence: [`src/provider.rs`](https://github.com/gordonbrander/jevgate/blob/6d9eb915a606393bbc29aaed0194b7ce74ff7eec/src/provider.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install --path .
echo "Production API is returning 500s" | jevgate -v "Does this report an outage?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage examples in the upstream README.

## Limits and data handling

Piped text is sent to TypeSafe and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 6d9eb915a606](https://github.com/gordonbrander/jevgate/tree/6d9eb915a606393bbc29aaed0194b7ce74ff7eec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
