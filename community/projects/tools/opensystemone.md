# Open System One (independent open specification for System One model APIs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Early-draft open specification (OpenAPI contract, examples, site) for System One model APIs, based on TypeSafe's request/response types; independent of TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/opensystemoneorg/opensystemone) |
| Maintainer | [opensystemoneorg](https://github.com/opensystemoneorg). Independently curated. |
| Format | Specification + OpenAPI + examples (Apache-2.0) |
| Requirements | Nothing to run; read the spec, or validate requests/responses with the provided examples. |
| License | [Apache-2.0](https://github.com/opensystemoneorg/opensystemone/blob/6d887469079c7ddb1a56fd1d1c919cb43884ca1e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`SPEC.md`](https://github.com/opensystemoneorg/opensystemone/blob/6d887469079c7ddb1a56fd1d1c919cb43884ca1e/SPEC.md) at the pinned commit. |

## When to use

- Build a gateway or provider compatible with Jev clients.
- Validate System One payloads against a shared contract.
- Mismatch: early draft; expect breaking changes.

## How it works

`SPEC.md` defines the `SystemOne` POST operation (`noul`, `choice`, `score`, `box` questions) at an implementer-chosen URL; `examples/` include TypeSafe-shaped requests using `jev-latest` and `jev-preview`. Integration evidence: [`SPEC.md`](https://github.com/opensystemoneorg/opensystemone/blob/6d887469079c7ddb1a56fd1d1c919cb43884ca1e/SPEC.md).

## Get started

Read `SPEC.md` and the OpenAPI document; pin a dated release if you depend on it.

```sh
git clone https://github.com/opensystemoneorg/opensystemone.git && cd opensystemone
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/opensystemoneorg/opensystemone/blob/6d887469079c7ddb1a56fd1d1c919cb43884ca1e/README.md](https://github.com/opensystemoneorg/opensystemone/blob/6d887469079c7ddb1a56fd1d1c919cb43884ca1e/README.md)

## Limits and data handling

Specification only; no data is sent anywhere.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 6d887469079c](https://github.com/opensystemoneorg/opensystemone/tree/6d887469079c7ddb1a56fd1d1c919cb43884ca1e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
