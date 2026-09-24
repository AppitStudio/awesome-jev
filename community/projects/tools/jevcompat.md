# jevcompat

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Testable spec and conformance suite for Jev-compatible TypeSafe System One API servers—normalising proxy, reference mock, and GitHub Action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mandu5/jevcompat) |
| Maintainer | [mandu5](https://github.com/mandu5) (Youngmin Ko). Independently curated. |
| Format | Python package + `SPEC.md` + GitHub Action (`action.yml`). |
| Requirements | Python 3.x; optional live endpoint under test. |
| License | [MIT](https://github.com/mandu5/jevcompat/blob/983a4a2b2929753a2e9697aadb241b4d93438060/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Spec claims were not independently certified against TypeSafe production beyond reading `SPEC.md`. |

## When to use

Use it when you run a **Jev-compatible `/v1/systemone` server** (or proxy) and need automated conformance. Prefer official TypeSafe docs alone when you only call the hosted API.

## How it works

[`SPEC.md`](https://github.com/mandu5/jevcompat/blob/983a4a2b2929753a2e9697aadb241b4d93438060/SPEC.md) defines the contract for `POST /v1/systemone`. The suite drives typed questions against a target, with a mock and normalising proxy for local CI. The Action wraps the same checks.

## Get started

```sh
git clone https://github.com/mandu5/jevcompat.git
cd jevcompat
git checkout 983a4a2b2929753a2e9697aadb241b4d93438060
# follow README for pip install / pytest / Action usage
```

## Examples and demos

- `SPEC.md`, `DESIGN.md`, `results/REVIEW.md`.
- `tests/test_preflight.py` and related (not executed here).

## Limits and data handling

Pointing the suite at a hosted endpoint sends synthetic (and any configured) payloads there. Do not feed production secrets into fixtures.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 983a4a2](https://github.com/mandu5/jevcompat/tree/983a4a2b2929753a2e9697aadb241b4d93438060). AI-assisted README/SPEC/LICENSE inspection. No live conformance run against TypeSafe.

Related: [Jev GitHub Action](jev-action.md), [TypeSafe Go](typesafe-go.md).
