# hunch (Rust CLI for asking Jev yes/no, multiple-choice and scoring questions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small Rust CLI that sends a state plus one typed question (yes/no, choice or score) to Jev and prints the answer with probabilities, through TypeSafe's API or OpenRouter. The author describes it as a personal learning project with no maintenance promise.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bastiankoetsier/hunch) |
| Maintainer | [bastiankoetsier](https://github.com/bastiankoetsier). Independently curated. |
| Format | Rust CLI (`cargo install` or release installer) |
| Requirements | Rust toolchain or the release installer; `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY`). |
| License | [MIT](https://github.com/bastiankoetsier/hunch/blob/5fb13b6b6ca2d7e83d5bdb0e0477fb3971a21713/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/driver/typesafe.rs`](https://github.com/bastiankoetsier/hunch/blob/5fb13b6b6ca2d7e83d5bdb0e0477fb3971a21713/src/driver/typesafe.rs) at the pinned commit. |

## When to use

- Ask Jev a quick typed question from the shell or a script.
- Mismatch: learning project; no stability promise.

## How it works

`src/driver/typesafe.rs` builds the System One request (default model `jev-latest`) and parses the typed answer; `src/driver/openrouter.rs` offers the same question shapes through OpenRouter. Integration evidence: [`src/driver/typesafe.rs`](https://github.com/bastiankoetsier/hunch/blob/5fb13b6b6ca2d7e83d5bdb0e0477fb3971a21713/src/driver/typesafe.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install --git https://github.com/bastiankoetsier/hunch
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Learning notes: [github.com/bastiankoetsier/hunch/blob/main/docs/learning.md](https://github.com/bastiankoetsier/hunch/blob/main/docs/learning.md)

## Limits and data handling

Your input is sent to TypeSafe or OpenRouter and billed to your key. Unofficial client. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 5fb13b6b6ca2](https://github.com/bastiankoetsier/hunch/tree/5fb13b6b6ca2d7e83d5bdb0e0477fb3971a21713). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
