# toolreview (Jev-reviewed approval rules that classify agent tools as read, write, outbound or destructive)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Go library that asks TypeSafe Jev once per tool—from name, title, description and arguments—which of four classes a call belongs to (read, write, outbound, destructive), then lets a gate enforce the more cautious of the provider label and the review. Reviews are bound to a fingerprint of what the model read.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/omniaura/toolreview) |
| Maintainer | [omniaura](https://github.com/omniaura). Independently curated. |
| Format | Go library (MIT) |
| Requirements | Go toolchain and an OpenRouter key (Jev via OpenRouter decisions; TypeSafe model id pinned). |
| License | [MIT](https://github.com/omniaura/toolreview/blob/990460c76f920d20b3895eedfb316fc5094fe3a7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev/jev.go`](https://github.com/omniaura/toolreview/blob/990460c76f920d20b3895eedfb316fc5094fe3a7/jev/jev.go) at the pinned commit. |

## When to use

- Build an approval gate that does not treat every write the same.
- Review a large tool catalog once and cache fingerprints.
- Mismatch: needs a live decision endpoint; word lists alone are not enough for outbound vs local writes.

## How it works

`jev/jev.go` calls OpenRouter's decisions path with a pinned TypeSafe Jev model and returns calibrated class probabilities; `Verdict.Effective` never lowers a provider's more cautious label. Integration evidence: [`jev/jev.go`](https://github.com/omniaura/toolreview/blob/990460c76f920d20b3895eedfb316fc5094fe3a7/jev/jev.go).

## Get started

Clone the repo, set an OpenRouter key, and review one tool description through the library or CLI shown in the README.

```sh
export OPENROUTER_API_KEY=...
go test ./...
# see README for review-one-tool examples
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/omniaura/toolreview/blob/990460c76f920d20b3895eedfb316fc5094fe3a7/README.md](https://github.com/omniaura/toolreview/blob/990460c76f920d20b3895eedfb316fc5094fe3a7/README.md)

## Limits and data handling

Tool names, titles, descriptions and argument schemas are sent to the decision provider on your key. A review only adds caution; it does not rewrite provider labels downward.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 990460c76f92](https://github.com/omniaura/toolreview/tree/990460c76f920d20b3895eedfb316fc5094fe3a7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
