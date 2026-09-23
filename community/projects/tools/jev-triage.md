# jev-triage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action that labels new/edited issues with TypeSafe Jev (or Cloudflare Workers AI `typesafe/jev`) typed Choice/Score/Noul answers, applying labels only when confidence clears the gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/CMaintz/jev-triage) |
| Maintainer | [CMaintz](https://github.com/CMaintz) (Christoffer Maintz). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Composite/GitHub Action **`cmaintz/jev-triage@v0`** (bundled `dist/`; npm package **jev-triage 0.1.0**). |
| Requirements | Workflow permissions `issues: write`; secrets for Jev (`jev-api-key`) and optionally Cloudflare account id. Repo config `.github/jev-triage.yml`. |
| License | [MIT](https://github.com/CMaintz/jev-triage/blob/4968138cd130f04de377033819a3d5f9dff77441/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `action.yml`, `src/main.ts`, examples). Offline Foundry gate and live issue triage were **not** run on the review host. |

## When to use

Use it for cheap first-pass issue labeling that **defers** uncertain cases (`triage:needs-human`) instead of inventing prose. Prefer [triagedy](triagedy.md) for offline JSONL security-alert triage CLIs. It does not auto-close issues.

## How it works

On `issues` opened/edited/reopened, [`src/main.ts`](https://github.com/CMaintz/jev-triage/blob/4968138cd130f04de377033819a3d5f9dff77441/src/main.ts) builds state from title/body/labels, loads questions from config, calls TypeSafe or Cloudflare provider, and [`decide`](https://github.com/CMaintz/jev-triage/blob/4968138cd130f04de377033819a3d5f9dff77441/src/core/decide.ts) maps confident answers to labels. Dry-run comments a would-apply summary. Screenshots/attachments are ignored; arithmetic stays in code.

## Get started

```yaml
# .github/workflows/triage.yml
on:
  issues: { types: [opened, edited, reopened] }
permissions: { issues: write, contents: read }
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: cmaintz/jev-triage@v0
        with:
          jev-api-key: ${{ secrets.JEV_API_KEY }}
```

See [`examples/jev-triage.yml`](https://github.com/CMaintz/jev-triage/blob/4968138cd130f04de377033819a3d5f9dff77441/examples/jev-triage.yml). Pin reviewed: [commit 4968138](https://github.com/CMaintz/jev-triage/tree/4968138cd130f04de377033819a3d5f9dff77441).

## Examples and demos

- Upstream example workflow + config.
- Author-reported live API validation and unit tests (not re-run here).

## Limits and data handling

Issue title/body go to the configured Jev provider. Low-confidence answers are not applied. ~classification accuracy claims are upstream; treat as a first pass. No live triage in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 4968138](https://github.com/CMaintz/jev-triage/tree/4968138cd130f04de377033819a3d5f9dff77441) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, `action.yml`, `src/main.ts`. No live TypeSafe/Cloudflare spend.

Related: [jev-guard (CMaintz)](cmaintz-jev-guard.md), [triagedy](triagedy.md), [agent-fastpath](agent-fastpath.md).
