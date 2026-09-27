# ZeroAlloc.Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial .NET client for TypeSafe's Jev System One API — source-generated, Native AOT, allocation-conscious.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZeroAlloc-Net/ZeroAlloc.Jev) |
| Maintainer | [ZeroAlloc-Net](https://github.com/ZeroAlloc-Net). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | .NET client library. |
| Requirements | .NET SDK; TypeSafe API key for live calls. |
| License | [MIT](https://github.com/ZeroAlloc-Net/ZeroAlloc.Jev/blob/9f6d9db9762fd533dbaa31330d3d8999a16548ef/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use for allocation-conscious .NET integrations. Prefer official SDKs when available for your stack.

## How it works

Source-generated client targets the System One API; CI badge documented upstream. Unofficial; not affiliated with TypeSafe. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ZeroAlloc-Net/ZeroAlloc.Jev.git
cd ZeroAlloc.Jev
git checkout 9f6d9db9762fd533dbaa31330d3d8999a16548ef
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `9f6d9db9762fd533dbaa31330d3d8999a16548ef` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 9f6d9db9762f](https://github.com/ZeroAlloc-Net/ZeroAlloc.Jev/tree/9f6d9db9762fd533dbaa31330d3d8999a16548ef). AI-assisted README and LICENSE inspection; install/live paths not executed.
