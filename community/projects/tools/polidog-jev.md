# jev (polidog)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Provider-neutral Rust CLI for TypeSafe Jev (TypeSafe, Cloudflare, Vercel).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/polidog/jev) |
| Maintainer | [polidog](https://github.com/polidog). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust command-line client. |
| Requirements | Rust toolchain; provider API key via `TYPESAFE_API_KEY` or provider-specific env per README. |
| License | [MIT](https://github.com/polidog/jev/blob/3bf6c493023bacce4fb72239d4e62b7c06a2987f/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for shell pipelines that need Jev judgments. Prefer language SDKs inside applications.

## How it works

Subcommands map to Noul/Choice/Score; JSON answers go to stdout for jq/thresholds downstream. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
cargo install --git https://github.com/polidog/jev
export TYPESAFE_API_KEY=…
echo "Help! My payouts have been failing for 3 days." | jev noul "Does this convey urgency?"
```

Pin revision `3bf6c493023bacce4fb72239d4e62b7c06a2987f` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Unofficial. Distinct from stefafafan/jev (Go) and feder-cr/jev (jevos server). Live calls not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 3bf6c49](https://github.com/polidog/jev/tree/3bf6c493023bacce4fb72239d4e62b7c06a2987f). AI-assisted README and LICENSE inspection; install/live paths not executed.
