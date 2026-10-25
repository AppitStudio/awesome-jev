# DecisionTools (DeepSeek Harness tool recommendations and search prefetch from a Jev-style Decision API)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Optional DeepSeek Harness (DSH) plugin: a bounded-answer Decision API such as Jev recommends tools before the main model's first request (per-session DecisionBoost) and can preselect and prefetch search sources, while every tool stays available and the main model keeps control.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/M4rkzzz/dsh-decisiontools) |
| Maintainer | [M4rkzzz](https://github.com/M4rkzzz). Independently curated. |
| Format | DSH plugin (JavaScript, no build step) |
| Requirements | DSH 0.2.1-rc.2+ and Node 22.19+; a Decision API URL and credential, for example TypeSafe Jev. |
| License | [MIT](https://github.com/M4rkzzz/dsh-decisiontools/blob/afe1ee239abc46ae44a490fef8b41594c5539591/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/api.mjs`](https://github.com/M4rkzzz/dsh-decisiontools/blob/afe1ee239abc46ae44a490fef8b41594c5539591/lib/api.mjs) at the pinned commit. |

## When to use

- Give a DSH session a cheap head start on which tools to use.
- Prefetch likely search sources before the main model asks.
- Mismatch: settings UI labels are in Chinese; works with Jev/SystemOne-style APIs, others not guaranteed.

## How it works

`lib/api.mjs` normalises the configured base URL to a `/v1/systemone` (or `/decisions`) endpoint and sends `state + questions` requests with validated `score`, `noul` and `choice` answers; you pick the model yourself after probing. Integration evidence: [`lib/api.mjs`](https://github.com/M4rkzzz/dsh-decisiontools/blob/afe1ee239abc46ae44a490fef8b41594c5539591/lib/api.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
dsh plugin --profile web add 'git+https://github.com/M4rkzzz/dsh-decisiontools.git#v0.1.8'
# then Settings → DecisionTools: enter the Decision API URL and key, probe, select a model, enable
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/M4rkzzz/dsh-decisiontools#readme](https://github.com/M4rkzzz/dsh-decisiontools#readme)
- Releases: [github.com/M4rkzzz/dsh-decisiontools/releases](https://github.com/M4rkzzz/dsh-decisiontools/releases)

## Limits and data handling

When enabled, the Decision service receives the current task plus tool names and short descriptions; search assistance also sends the query and candidate titles, URLs and snippets.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit afe1ee239abc](https://github.com/M4rkzzz/dsh-decisiontools/tree/afe1ee239abc46ae44a490fef8b41594c5539591). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
