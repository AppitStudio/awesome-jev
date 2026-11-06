# clai (terminal AI CLI with a native TypeSafe Jev System One vendor)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Command-line artificial intelligence client for context engineering in the terminal, with a first-class TypeSafe Jev vendor that posts to `/v1/systemone` alongside other model backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/baalimago/clai) |
| Maintainer | [baalimago](https://github.com/baalimago). Independently curated. |
| Format | Go CLI (MIT) |
| Requirements | Go build or release binary and `TYPESAFE_API_KEY` when using the Jev vendor. |
| License | [MIT](https://github.com/baalimago/clai/blob/207dfd91c93a8f1e773fa22e282a87adda74e196/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/vendors/jev/jev.go`](https://github.com/baalimago/clai/blob/207dfd91c93a8f1e773fa22e282a87adda74e196/internal/vendors/jev/jev.go) at the pinned commit. |

## When to use

- Drive terminal workflows with mixed generative and decision vendors.
- Call TypeSafe Jev from the same CLI as other providers.
- Mismatch: Jev is one vendor among several; not a Jev-only product.

## How it works

`internal/vendors/jev/jev.go` sets `SystemOneURL` to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Integration evidence: [`internal/vendors/jev/jev.go`](https://github.com/baalimago/clai/blob/207dfd91c93a8f1e773fa22e282a87adda74e196/internal/vendors/jev/jev.go).

## Get started

Install clai per the README and select the Jev vendor with a TypeSafe key.

```sh
git clone https://github.com/baalimago/clai.git && cd clai
# build/install per README
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/baalimago/clai/blob/207dfd91c93a8f1e773fa22e282a87adda74e196/README.md](https://github.com/baalimago/clai/blob/207dfd91c93a8f1e773fa22e282a87adda74e196/README.md)

## Limits and data handling

Prompt/state for Jev calls is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 207dfd91c93a](https://github.com/baalimago/clai/tree/207dfd91c93a8f1e773fa22e282a87adda74e196). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
