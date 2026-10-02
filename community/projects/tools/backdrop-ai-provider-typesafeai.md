# Backdrop AI Provider TypeSafe AI

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Backdrop CMS AI module provider for TypeSafe System One decisions and moderation checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/backdrop-contrib/ai_provider_typesafeai) |
| Maintainer | [backdrop-contrib](https://github.com/backdrop-contrib). Independently curated. |
| Format | PHP · Backdrop CMS AI module provider (GPL-2.0) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`GPL-2.0`](https://github.com/backdrop-contrib/ai_provider_typesafeai/blob/66a878a39c8c51bb8751cef1e813b9b9b5a0f8f3/LICENSE.txt). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Backdrop CMS AI module provider for TypeSafe System One decisions and moderation checks. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/backdrop-contrib/ai_provider_typesafeai.git
cd ai_provider_typesafeai
git checkout 66a878a39c8c51bb8751cef1e813b9b9b5a0f8f3
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: decide() boolean/choice/score via TypeSafe systemone endpoint (see upstream README). ([upstream evidence](https://github.com/backdrop-contrib/ai_provider_typesafeai/blob/66a878a39c8c51bb8751cef1e813b9b9b5a0f8f3/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 66a878a39c8c](https://github.com/backdrop-contrib/ai_provider_typesafeai/tree/66a878a39c8c51bb8751cef1e813b9b9b5a0f8f3). AI-assisted README and license inspection; install/live paths not executed.
