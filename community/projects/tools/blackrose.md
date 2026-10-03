# Blackrose

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeSafe System One decision layer that returns allow/review/block before/after LLM generation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dino-Kupinic/blackrose) |
| Maintainer | [Dino-Kupinic](https://github.com/Dino-Kupinic). Independently curated. |
| Format | Python and JavaScript packages: TypeSafe System One allow/review/block guards for LLM apps. |
| Requirements | Python 3.10+ / Bun 1.1+; TYPESAFE_API_KEY for live calls. |
| License | [MIT](https://github.com/Dino-Kupinic/blackrose/blob/addf5da2627e226dd3364b5d4414834c5124223e/LICENSE). TypeSafe usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. |

## When to use

Use when an LLM app needs an explicit decision gate with confidence thresholds. Prefer thinner clients when you only need a single System One call.

## How it works

Blackrose wraps TypeSafe system_one questions and applies thresholds in your code; generation stays outside the library.

## Get started

```sh
git clone https://github.com/Dino-Kupinic/blackrose.git
cd blackrose
git checkout addf5da2627e226dd3364b5d4414834c5124223e
# cd packages/python && uv sync — see upstream README
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-30** (Europe/Sofia) at [commit addf5da](https://github.com/Dino-Kupinic/blackrose/tree/addf5da2627e226dd3364b5d4414834c5124223e). AI-assisted README and license inspection; install/live paths not executed.
