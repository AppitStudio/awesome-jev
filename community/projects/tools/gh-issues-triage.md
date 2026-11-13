# GitHub Issues Triage (Rust TUI and CLI that ranks a repository's latest 100 issues by importance with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust terminal tool that fetches the latest 100 issues of a GitHub repository and has Jev score and classify them, so the next issue to work on is at the top; it also has a JSON `next` mode for calling from an AI agent skill.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tkumata/gh-issues-triage) |
| Maintainer | [tkumata](https://github.com/tkumata). Independently curated. |
| Format | Rust TUI/CLI built with Cargo (no license file) |
| Requirements | Rust (edition 2024), a GitHub App client ID (`GITHUB_CLIENT_ID`) for Device Flow sign-in, and `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/tkumata/gh-issues-triage/blob/274b19ed1d6729c11f8bf788152962bc6b7a7fd4/src/jev.rs) at the pinned commit. |

## When to use

- Pick the next issue to work on in a busy repository.
- Feed a ranked issue list to a coding agent with `next --format json`.
- Mismatch: writing labels back to GitHub; it only reads issues. README is in Japanese.

## How it works

`src/jev.rs` builds one request with `jev-latest` that asks a `score` question for importance and `choice` questions for category and readiness over the issues, sent to `https://api.typesafe.ai/v1/systemone`; GitHub data comes from the REST API, and tokens are kept in the macOS Keychain or Linux Secret Service. Integration evidence: [`src/jev.rs`](https://github.com/tkumata/gh-issues-triage/blob/274b19ed1d6729c11f8bf788152962bc6b7a7fd4/src/jev.rs).

## Get started

Set the two environment variables and run it against a repository.

```sh
export GITHUB_CLIENT_ID='<GitHub App client ID>'
export TYPESAFE_API_KEY='<TypeSafe API key>'
cargo run -- owner/repo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshot and architecture diagram: [github.com/tkumata/gh-issues-triage/blob/274b19ed1d6729c11f8bf788152962bc6b7a7fd4/README.md](https://github.com/tkumata/gh-issues-triage/blob/274b19ed1d6729c11f8bf788152962bc6b7a7fd4/README.md)

## Limits and data handling

Issue titles and bodies go to TypeSafe on your key; private repositories need a GitHub App with Issues read access.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 274b19ed1d67](https://github.com/tkumata/gh-issues-triage/tree/274b19ed1d6729c11f8bf788152962bc6b7a7fd4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
