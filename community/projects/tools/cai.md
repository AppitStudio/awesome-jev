# cai

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust CLI for AI tasks across many providers that adds TypeSafe Jev subcommands (`cai noul`, `choice`, `score`, `jev`) for typed questions about text piped on stdin.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ad-si/cai) |
| Maintainer | [ad-si](https://github.com/ad-si). Independently curated. |
| Format | Command-line tool |
| Requirements | Rust/Cargo. The Jev subcommands were added on the default branch in October 2026 and are not in the latest crates.io/Homebrew release checked (0.13.0, January 2026), so install from Git. Jev commands need a TypeSafe key (`cai` setup prompt, `CAI_TYPESAFE_API_KEY`, or `TYPESAFE_API_KEY`); other commands use their own provider keys. |
| License | [ISC](https://github.com/ad-si/cai/blob/6971ac23e7ccc62819bd35fc44be2c420bd44c03/license.txt). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Script quick triage in shell pipelines: is this message urgent, which label fits, how severe is it.
- Compare a typed Jev answer with a chat model's answer from the same tool.
- Mismatch: for programmatic use inside an application, an SDK is a better fit than shelling out.

## How it works

The Jev subcommands build a `/v1/systemone` request with stdin text as state and your question(s), default model `jev-latest`, and print the answer with probabilities and the model that answered. Base URL is configurable (`typesafe_base_url`, default `https://api.typesafe.ai/v1`) ([`src/typesafe.rs`](https://github.com/ad-si/cai/blob/6971ac23e7ccc62819bd35fc44be2c420bd44c03/src/typesafe.rs)).

## Get started

Install from the default branch and ask a typed question about piped text (live Jev call):

```sh
cargo install --git https://github.com/ad-si/cai   # crates.io 0.13.0 predates the Jev commands
export TYPESAFE_API_KEY=...
echo "Server is down for all EU customers" | cai noul is this urgent
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README feature list and `cai --help` output for `noul`, `choice`, `score` and `jev`.

## Limits and data handling

Jev support is unreleased at the reviewed commit (default branch only). Piped text is sent to TypeSafe and billed. The default `jev-latest` alias can change behind the scenes; pin a version for repeatable thresholds. Output is for humans; parse with care in scripts.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 6971ac23e7cc](https://github.com/ad-si/cai/tree/6971ac23e7ccc62819bd35fc44be2c420bd44c03). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
