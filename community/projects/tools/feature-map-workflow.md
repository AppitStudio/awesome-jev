# Feature Map workflow (source-first Feature Map XML workflow for Codex with optional TypeSafe Jev decisions)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Codex workflow that keeps a small Feature Map XML per business feature, with Mermaid diagrams, context gates, xquery-mcp validation and optional TypeSafe Jev decisions in its hooks (Japanese and English docs).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nakashima-yoshua/feature-map-workflow) |
| Maintainer | [nakashima-yoshua](https://github.com/nakashima-yoshua). Independently curated. |
| Format | Codex workflow + Python hooks (MIT) |
| Requirements | Codex, Python 3, and optionally a TypeSafe API key. |
| License | [MIT](https://github.com/nakashima-yoshua/feature-map-workflow/blob/0a306d89a06151e1a37bcd74fc4cc18304bb7678/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/decision_provider.py`](https://github.com/nakashima-yoshua/feature-map-workflow/blob/0a306d89a06151e1a37bcd74fc4cc18304bb7678/hooks/decision_provider.py) at the pinned commit. |

## When to use

- Keep Codex grounded in per-feature maps.
- Add optional Jev gates to workflow hooks.
- Mismatch: Jev is opt-in; do not put keys in CI.

## How it works

`hooks/decision_provider.py` calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` only when a Jev mode is explicitly enabled and a key is provided; no SDK is bundled. Integration evidence: [`hooks/decision_provider.py`](https://github.com/nakashima-yoshua/feature-map-workflow/blob/0a306d89a06151e1a37bcd74fc4cc18304bb7678/hooks/decision_provider.py).

## Get started

Install the workflow into a repo per README; enable a Jev mode in hook config if you want typed decisions.

```sh
git clone https://github.com/nakashima-yoshua/feature-map-workflow.git && cd feature-map-workflow
export TYPESAFE_API_KEY=...
ls hooks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nakashima-yoshua/feature-map-workflow/blob/0a306d89a06151e1a37bcd74fc4cc18304bb7678/README.md](https://github.com/nakashima-yoshua/feature-map-workflow/blob/0a306d89a06151e1a37bcd74fc4cc18304bb7678/README.md)

## Limits and data handling

Hook context is sent to TypeSafe on your key only when Jev mode is enabled.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 0a306d89a061](https://github.com/nakashima-yoshua/feature-map-workflow/tree/0a306d89a06151e1a37bcd74fc4cc18304bb7678). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
