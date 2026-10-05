# rippy

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust shell-command safety hook for AI coding tools; a separate opt-in `rippy-jev` build can ask Jev to approve only commands rippy is unsure about, never ones that require human approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mpecan/rippy) |
| Maintainer | [mpecan](https://github.com/mpecan). Independently curated. |
| Format | Coding-agent hook binary; Jev review only in the `rippy-jev` distribution |
| Requirements | Rust/Cargo or Homebrew. For Jev: install `rippy-jev` (or `cargo install rippy-cli --features jev`), enable `[jev]` in config, and provide the key via the env variable named in `api-key-env` (OpenRouter or TypeSafe `/v1/systemone`). |
| License | [MIT](https://github.com/mpecan/rippy/blob/fb88990359fa41f69cb3a91ee4ccd13006c755d5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Reduce prompt fatigue for read-only commands rippy cannot classify, without auto-approving anything that needs you.
- Restrict Jev to effect classes you choose (`read_only`, optionally `remote_read`, `local_change`) with a high confidence floor.
- Mismatch: the default distribution has no network code at all; stay on it if commands must never leave the machine.

## How it works

rippy asks for two reasons: a human must approve, or rippy cannot tell. Only the second kind can go to Jev, which may approve or leave it as an ask; it never blocks and never touches allow/deny/approval asks. Commands whose behavior is defined elsewhere (scripts, task runners, interpreters with arguments) are never sent ([README: Jev review of uncertain asks](https://github.com/mpecan/rippy/blob/fb88990359fa41f69cb3a91ee4ccd13006c755d5/README.md#jev-review-of-uncertain-asks-rippy-jev-only)).

## Get started

Install the Jev build and enable it in config (live Jev calls only for uncertain asks):

```sh
cargo install rippy-cli --features jev   # or: brew install mpecan/tools/rippy-jev
# config:
# [jev]
# enabled = true
# endpoint = "https://api.typesafe.ai/v1/systemone"
# model = "jev-latest"
# api-key-env = "TYPESAFE_API_KEY"
# allow-effects = ["read_only"]
# min-confidence = 0.9
```

Only uncertain asks are sent to the configured provider (OpenRouter or TypeSafe) and billed there.

## Examples and demos

- README config example and `docs/jev.md` (per-risk gates) upstream.

## Limits and data handling

Upstream states plainly that this trades some safety for fewer prompts: Jev judges a command by its text. Command text goes to the provider. `rippy --version` ends in `+jev` on the Jev build.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit fb88990359fa](https://github.com/mpecan/rippy/tree/fb88990359fa41f69cb3a91ee4ccd13006c755d5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
