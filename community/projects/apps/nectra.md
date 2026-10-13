# Nectra

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

One chat in front of Claude Code, Codex, Gemini CLI and Ollama: each message is classified and routed to the model that should answer it, then that provider's real terminal opens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MBarc/nectra) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [github.com/MBarc/nectra#readme](https://github.com/MBarc/nectra#readme) |
| Pricing and access | Free MIT source; you use your existing provider subscriptions/keys plus a TypeSafe key. |
| Jev evidence | [`src/jev.rs`](https://github.com/MBarc/nectra/blob/ea8cd029832e85d414c4acad701da6ef325e28d6/src/jev.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [MBarc](https://github.com/MBarc). Independently curated. |
| Format | Rust CLI app |
| Platform and availability | Command line (Rust) |
| Jev's role | Jev classifies each prompt's task type and needed capability; Nectra's scorer picks the model and runtime and explains why. |
| Requirements | Rust toolchain or release binary; at least one agent CLI; TypeSafe key. |
| License | [MIT](https://github.com/MBarc/nectra/blob/ea8cd029832e85d414c4acad701da6ef325e28d6/LICENSE) |

## When to use

- Stop juggling several agent terminals and send each message to an appropriate model.
- Mismatch: Routing quality depends on your enabled models and scoring config.

## How it works

`nectra route` shows the task label, chosen model, score and margin; Nectra hands the conversation to the winning CLI and returns to one prompt. (Summarized from the upstream [README](https://github.com/MBarc/nectra/blob/ea8cd029832e85d414c4acad701da6ef325e28d6/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README, enable your models, then run `nectra`.

## Limits and data handling

Message text goes to TypeSafe for classification and to whichever provider answers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit ea8cd029832e](https://github.com/MBarc/nectra/tree/ea8cd029832e85d414c4acad701da6ef325e28d6). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
