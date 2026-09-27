# Jev Bug Hunter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Bounded first-pass bug hunting for source files powered by TypeSafe Jev — a quick sanity check, not a replacement for tests or review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BillNDD/jev-bug-hunter) |
| Maintainer | [BillNDD](https://github.com/BillNDD). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | CLI / developer tool. |
| Requirements | Runtime per upstream README; TypeSafe API key for live hunts. |
| License | [MIT](https://github.com/BillNDD/jev-bug-hunter/blob/fcaacdeedf07561b18721ca3a5f16d528de7e709/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for cheap first-pass bug screens before deeper analysis. Do not treat outputs as complete security audits.

## How it works

Points Jev typed questions at a file (and optional specification) and reports candidate issues; code owns presentation and thresholds. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/BillNDD/jev-bug-hunter.git
cd jev-bug-hunter
git checkout fcaacdeedf07561b18721ca3a5f16d528de7e709
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `fcaacdeedf07561b18721ca3a5f16d528de7e709` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit fcaacdeedf07](https://github.com/BillNDD/jev-bug-hunter/tree/fcaacdeedf07561b18721ca3a5f16d528de7e709). AI-assisted README and LICENSE inspection; install/live paths not executed.
