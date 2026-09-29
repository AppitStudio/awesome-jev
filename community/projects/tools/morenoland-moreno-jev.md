# Moreno.Jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Cross-platform MCP server and agent skill for TypeSafe Jev structured code review and debugging (review_code / review_diff tools)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MorenoLand/Moreno.Jev) |
| Maintainer | [MorenoLand](https://github.com/MorenoLand). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python MCP server + agent skill. |
| Requirements | Python; TypeSafe key; MCP-capable client (Codex, Pi adapter, etc.). |
| License | [MIT](https://github.com/MorenoLand/Moreno.Jev/blob/3034cc5aed61bab01b48dab702f22f5dbf6d0899/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when Codex or other MCP clients should ask Jev for structured bug triage and diff regression signals. Prefer general evaluate MCP servers for non-review tasks.

## How it works

Six MCP tools wrap typed Jev questions for code/diff review severity and human-review signals. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/MorenoLand/Moreno.Jev.git
cd Moreno.Jev
git checkout 3034cc5aed61bab01b48dab702f22f5dbf6d0899
```

Pin revision `3034cc5aed61bab01b48dab702f22f5dbf6d0899` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 3034cc5](https://github.com/MorenoLand/Moreno.Jev/tree/3034cc5aed61bab01b48dab702f22f5dbf6d0899). AI-assisted README and LICENSE inspection; install/live paths not executed.
