# decide (vsekhar)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

CLI to ask TypeSafe Jev typed decisions from the shell, scripts, and agent skills — no application code required (Show HN)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vsekhar/decide) |
| Maintainer | [vsekhar](https://github.com/vsekhar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go · CLI (Apache-2.0). |
| Requirements | brew install vsekhar/tap/decide or Go build; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/vsekhar/decide/blob/a9f85c838b476cc465827586e56dc7afcd3baf79/LICENSE.txt). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when shell scripts or skills need a one-liner System One decision. Prefer SDKs for in-process embedding.

## How it works

CLI wraps Typesafe Jev models with exit-code-friendly answers. Show HN 2026-09-28. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/vsekhar/decide.git
cd decide
git checkout a9f85c838b476cc465827586e56dc7afcd3baf79
```

Pin revision `a9f85c838b476cc465827586e56dc7afcd3baf79` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit a9f85c8](https://github.com/vsekhar/decide/tree/a9f85c838b476cc465827586e56dc7afcd3baf79). AI-assisted README and LICENSE inspection; install/live paths not executed.
