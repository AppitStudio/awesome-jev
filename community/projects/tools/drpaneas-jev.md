# jev (drpaneas)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Go package for calling TypeSafe Jev System One typed questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/drpaneas/jev) |
| Maintainer | [drpaneas](https://github.com/drpaneas). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Go library. |
| Requirements | Go toolchain; TypeSafe API key for live calls. |
| License | [MIT](https://github.com/drpaneas/jev/blob/d861b9f09608b099aa352ef1fb83a867ee3c0981/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from mattn/go-jev and other Go clients. |

## When to use

Use for lightweight Go integrations. Prefer go-jev or haileyok/typesafe-client when you need a CLI or multi-language clients.

## How it works

Package wraps System One requests for typed Jev answers; see upstream README examples. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/drpaneas/jev.git
cd jev
git checkout d861b9f09608b099aa352ef1fb83a867ee3c0981
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `d861b9f09608b099aa352ef1fb83a867ee3c0981` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Distinct from mattn/go-jev and other Go clients. Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit d861b9f09608](https://github.com/drpaneas/jev/tree/d861b9f09608b099aa352ef1fb83a867ee3c0981). AI-assisted README and LICENSE inspection; install/live paths not executed.
