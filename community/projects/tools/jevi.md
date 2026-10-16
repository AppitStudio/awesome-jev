# jevi

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Shell front end for Jev: pipe text in, ask a yes/no, multiple-choice or rubric question, and branch on the answer and probability; supports saved question sets, JSON output and images.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bitomule/jevi) |
| Maintainer | [bitomule](https://github.com/bitomule). Independently curated. |
| Format | Rust CLI (single static binary; `cargo install jevi` or Homebrew) |
| Requirements | A TypeSafe or OpenRouter API key. |
| License | [MIT OR Apache-2.0](https://github.com/bitomule/jevi/blob/aa4caf869ac100fdeb1c2501e2292700e9f1da2f/LICENSE-APACHE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/provider.rs`](https://github.com/bitomule/jevi/blob/aa4caf869ac100fdeb1c2501e2292700e9f1da2f/src/provider.rs) at the pinned commit. |

## When to use

- Put an understanding check in a git hook or shell script (is this commit message describing a bug? how bad is this log?).
- Ask a question about a screenshot (resized automatically to Jev's size limits).
- Mismatch: answers only typed questions; it never writes prose.

## How it works

Each provider maps to its endpoint and model (TypeSafe `https://api.typesafe.ai/v1/systemone` with `jev-latest`, or OpenRouter `typesafe/jev-1.13`); jevi builds the state from stdin, flags or images, sends the question and prints the answer with its probability, or JSON with `--json`. Integration evidence: [`src/provider.rs`](https://github.com/bitomule/jevi/blob/aa4caf869ac100fdeb1c2501e2292700e9f1da2f/src/provider.rs).

## Get started

From the upstream README (not run on the review host):

```sh
cargo install jevi   # or: brew install bitomule/tap/jevi
pbpaste | jevi config set-key openrouter   # or typesafe
jevi doctor --live
echo "the server has been down three hours" | jevi ask "is this urgent"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Question set examples: `questions/examples`.
- Image usage and limits: README section Images.

## Limits and data handling

Text and images go to the chosen provider on your key; the key is stored at `$XDG_CONFIG_HOME/bitomule/jevi/config.json` with mode 0600.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit aa4caf869ac1](https://github.com/bitomule/jevi/tree/aa4caf869ac100fdeb1c2501e2292700e9f1da2f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
