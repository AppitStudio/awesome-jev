# jev-grep by m407 (Rust CLI for semantic search over log and code fragments with Jev, plus an agent skill)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Rust CLI that lets you describe what you want in natural language instead of writing a regex: it groups log records or ast-grep code matches into fragments, asks Jev whether each fragment matches, and returns matching text with source, line range and byte offsets; an agent skill teaches coding agents to build these pipelines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m407/jev-grep) |
| Maintainer | [m407](https://github.com/m407). Independently curated. |
| Format | Rust CLI and agent skill (no license file; README in English and Russian) |
| Requirements | Rust with edition 2024 to build, and a provider endpoint that speaks the System One protocol (TypeSafe or OpenRouter) with a key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/api.rs`](https://github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/src/api.rs) at the pinned commit. |

## When to use

- Search logs or code by meaning ("requests that failed on auth") in shell pipelines.
- Mismatch: exact-pattern search, where grep or ripgrep is free and faster.

## How it works

`src/api.rs` sends `{model, state, questions}` System One requests to the configured `JEV_GREP_API_URL`; the default model is `jev-1.13` (`src/main.rs`), and an OpenAI-compatible chat endpoint alone is not enough. Inference runs at the provider; the CLI runs locally with no index. Integration evidence: [`src/api.rs`](https://github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/src/api.rs).

## Get started

Install from the repository root, then set the endpoint, model and key variables.

```sh
cargo install --path . --locked
export JEV_GREP_API_URL=... JEV_GREP_MODEL=jev-1.13 JEV_GREP_API_KEY=...
jev-grep --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/README.md](https://github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/README.md)
- Agent skill: [github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/docs/skill/jev-grep/SKILL.md](https://github.com/m407/jev-grep/blob/3816804b175c3b112de4ef6a39ca7dc77ba44e94/docs/skill/jev-grep/SKILL.md)

## Limits and data handling

Each log or code fragment you evaluate goes to the configured provider on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 3816804b175c](https://github.com/m407/jev-grep/tree/3816804b175c3b112de4ef6a39ca7dc77ba44e94). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
