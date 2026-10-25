# Tidyward (private file housekeeper for macOS where Jev answers what each file is)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Early macOS command-line housekeeper: it identifies files locally first, masks real names before anything leaves the machine, asks Jev only semantic yes/no questions such as "is this an invoice?", and your plain-text rules turn the answers into a keep, archive or Trash plan you confirm; every move can be undone.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chatpoc-ai/tidyward) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/chatpoc-ai/tidyward#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free source build. Jev calls are billed to your TypeSafe or Vercel AI Gateway account. Checked 2026-10-26. |
| Jev evidence | [`crates/tidyward-jev/src/lib.rs`](https://github.com/chatpoc-ai/tidyward/blob/f5cf89736553c77877395e8c25086cb26b34e1e1/crates/tidyward-jev/src/lib.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [chatpoc-ai](https://github.com/chatpoc-ai). Independently curated. |
| Format | Rust command-line app |
| Platform and availability | macOS command line (`cargo install`); no scheduler or GUI yet, Windows planned. |
| Jev's role | Core for semantic matching: Jev returns calibrated yes/no probabilities for each rule's description; exact conditions run locally and the model never chooses an action. |
| Requirements | macOS and Rust 1.85+; optional Magika; a TypeSafe key or a Vercel AI Gateway key. |
| License | [Apache-2.0](https://github.com/chatpoc-ai/tidyward/blob/f5cf89736553c77877395e8c25086cb26b34e1e1/LICENSE) |

## When to use

- Clean up Downloads or Desktop with rules you write in plain language.
- Keep real file names and contents on your Mac while still using a hosted model.
- Mismatch: early; scan, plan, apply and undo work on macOS only.

## How it works

`tidyward-jev` sends masked file names and metadata with Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) or to Vercel's gateway (`typesafe-ai/jev`); files it has already judged are not sent again. Integration evidence: [`crates/tidyward-jev/src/lib.rs`](https://github.com/chatpoc-ai/tidyward/blob/f5cf89736553c77877395e8c25086cb26b34e1e1/crates/tidyward-jev/src/lib.rs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/chatpoc-ai/tidyward && cd tidyward
cargo install --path crates/tidyward-cli
tidyward init
tidyward scan ~/Downloads && tidyward plan
tidyward apply   # confirm each move; tidyward undo reverts
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/chatpoc-ai/tidyward#readme](https://github.com/chatpoc-ai/tidyward#readme)
- Design: [github.com/chatpoc-ai/tidyward/blob/main/docs/design.md](https://github.com/chatpoc-ai/tidyward/blob/main/docs/design.md)

## Limits and data handling

Masked names (meaning kept, identifying parts removed) and file metadata go to the provider you choose; real names, paths and contents stay local. Items go to the macOS Trash, and `undo` puts them back.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit f5cf89736553](https://github.com/chatpoc-ai/tidyward/tree/f5cf89736553c77877395e8c25086cb26b34e1e1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
