# Jev GitHub Action

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that installs a pinned [model-clis/jev](https://github.com/model-clis/jev) release, runs typed judgments on a workflow event (or JSON request), and exposes the JSON answers to later steps—without mutating issues/PRs itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cachix/jev-action) |
| Maintainer | [cachix](https://github.com/cachix). Independently curated; not an upstream submission or endorsement. |
| Format | Composite/JS GitHub Action (`action.yml`) with Node tests. |
| Requirements | GitHub Actions runner; `api-key` (TypeSafe / Jev); optional `github-token` when fetching repo labels for triage helpers. |
| License | [Apache-2.0](https://github.com/cachix/jev-action/blob/58e66ff259eb209c7a3a775182c3577268613313/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Offline action unit tests not re-run here; live Actions+Jev not executed. |

## When to use

Use it to **gate or label from workflow YAML** with typed Jev answers. The action does not apply labels itself—your workflow consumes `answers` outputs.

## How it works

[`action.yml`](https://github.com/cachix/jev-action/blob/58e66ff259eb209c7a3a775182c3577268613313/action.yml) installs a checksum-verified Jev release tag, builds a request from `questions` + event state (or `request-file`), optional assertion expression (exit 3 on false), and writes the single-line JSON response to outputs.

## Get started

```yaml
- uses: cachix/jev-action@v1
  id: jev
  with:
    api-key: ${{ secrets.JEV_API_KEY }}
    questions: |
      {"needs_review":{"type":"noul","instructions":"Does this PR likely need human review?","criteria":{"true":"Needs review","false":"Clear automated change"}}}
```

Pin the action SHA for production. See upstream README for label-triage and `request-file` modes.

## Examples and demos

- README input table and assertion examples.
- `tests/action.test.mjs` with fake Jev binary.

## Limits and data handling

Event payloads / custom state leave the runner to TypeSafe when a key is set. Action does not hide secrets in logs beyond normal Actions practices—review your `questions`/`state-file`.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 58e66ff](https://github.com/cachix/jev-action/tree/58e66ff259eb209c7a3a775182c3577268613313). AI-assisted README/LICENSE/`action.yml` inspection. No live workflow run.

Related: [agent-evals](agent-evals.md), [Jev Review Action](jev-review-action.md).
