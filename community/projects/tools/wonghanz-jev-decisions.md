# jev-decisions (wonghanz)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Typed decision layer for backend engineering (log triage, incident routing, PR triage, deploy risk) with a control-group eval harness via OpenRouter Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wonghanz/jev-decisions) |
| Maintainer | [wonghanz](https://github.com/wonghanz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Library + evaluation harness. |
| Requirements | Node.js; `OPENROUTER_API_KEY` for live Jev via OpenRouter Decisions. |
| License | [MIT](https://github.com/wonghanz/jev-decisions/blob/a6190593d60513ea991947643edbb94d61ce4b69/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when backend ops decisions need typed questions and a harness to compare against a local baseline.

## How it works

Defines choice/noul/score primitives for four production decisions; client talks to OpenRouter's Jev endpoint; policy code cannot emit destructive actions from model answers alone. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/wonghanz/jev-decisions.git
cd jev-decisions
git checkout a6190593d60513ea991947643edbb94d61ce4b69
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `a6190593d60513ea991947643edbb94d61ce4b69` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit a6190593d605](https://github.com/wonghanz/jev-decisions/tree/a6190593d60513ea991947643edbb94d61ce4b69). AI-assisted README and LICENSE inspection; install/live paths not executed.
