# jev (stefafafan)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial provider-neutral Go CLI for TypeSafe Jev: Choice, Noul, and Score over TypeSafe, Cloudflare, or Vercel System One endpoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stefafafan/jev) |
| Maintainer | [stefafafan](https://github.com/stefafafan). Independently curated. Not an official TypeSafe product. |
| Format | Go CLI (`jev`). |
| Requirements | Go toolchain for install/build; provider credentials for the chosen backend. |
| License | [MIT](https://github.com/stefafafan/jev/blob/e2ffd61590e7a9a09ac9cf5b363a78324f2cabdc/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Not an official TypeSafe product. |

## When to use

Use for **shell/CI scripts** that need typed Jev answers across multiple System One-compatible providers. Prefer official SDKs for in-process clients.

## How it works

Provider adapters live under [`internal/provider/systemone.go`](https://github.com/stefafafan/jev/blob/e2ffd61590e7a9a09ac9cf5b363a78324f2cabdc/internal/provider/systemone.go) and [`typesafe.go`](https://github.com/stefafafan/jev/blob/e2ffd61590e7a9a09ac9cf5b363a78324f2cabdc/internal/provider/typesafe.go). Companion Action [`stefafafan/setup-jev`](https://github.com/stefafafan/setup-jev); example `pr-risk.yml` workflow.

## Get started

```sh
git clone https://github.com/stefafafan/jev.git
cd jev
git checkout e2ffd61590e7a9a09ac9cf5b363a78324f2cabdc
go build -o jev .
# configure provider credentials per upstream README
```

## Examples and demos

- Upstream README provider list and install paths.
- Example CI workflow labels merge risk from a PR diff (not executed here).

## Limits and data handling

Diffs/state you pass leave the machine for the selected provider. Distinct from `shaharia-lab/jev-cli` and `tumf/jev-cli`.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit e2ffd61](https://github.com/stefafafan/jev/tree/e2ffd61590e7a9a09ac9cf5b363a78324f2cabdc). AI-assisted README and LICENSE inspection of provider adapters; install/live paths not executed.
