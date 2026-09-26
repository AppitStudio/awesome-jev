# Jevlin

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Zig SDK for TypeSafe Jev—typed classification, scoring, and yes/no probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/copyleftdev/jevlin) |
| Maintainer | [copyleftdev](https://github.com/copyleftdev). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Zig package with `zig build check` offline suite and optional `zig build live`. |
| Requirements | Zig 0.16.0; `TYPESAFE_API_KEY` only for live builds. |
| License | [MIT](https://github.com/copyleftdev/jevlin/blob/5d0758ac33dd7ee9d864ddb808f285066a2cc7ac/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when embedding Jev clients in Zig systems that need explicit memory ownership.

## How it works

You own request/response buffers; client evaluates structured questions and returns Zig enums/probabilities. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/copyleftdev/jevlin.git
cd jevlin
git checkout 5d0758ac33dd7ee9d864ddb808f285066a2cc7ac
zig build check
```

Pin revision `5d0758ac33dd7ee9d864ddb808f285066a2cc7ac` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Pre-release; dynamic schemas and pooling not implemented. Live TypeSafe path not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 5d0758a](https://github.com/copyleftdev/jevlin/tree/5d0758ac33dd7ee9d864ddb808f285066a2cc7ac). AI-assisted README and LICENSE inspection; install/live paths not executed.
