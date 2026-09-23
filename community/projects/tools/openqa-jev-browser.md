# Jev Browser (openqa-cn)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Indexed Playwright browser automation: the page builds a closed control index; TypeSafe Jev chooses operation and target; Playwright acts. CodexQA skill with replay, generate, explore, and HTML reports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/openqa-cn/jev-browser) |
| Maintainer | [openqa-cn](https://github.com/openqa-cn). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI **`codexqa-jev-browser` 0.1.0** + `SKILL.md` (also listed in CodexQA catalog). |
| Requirements | Node.js ≥ 20; Playwright Chromium; `TYPESAFE_API_KEY` for live auto/generate (OpenAI-compatible chat is fallback planner/decision). Offline `observe` / `run` / `--decisions` need no model. |
| License | [MIT](https://github.com/openqa-cn/jev-browser/blob/ea82bc96597b07f27a386288b196b0bca1cdcb3a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, package). Live browser/Jev runs were **not** executed on the review host. TypeSafe latency/cost comparisons in the upstream README are vendor-reported, not reproduced here. |

## When to use

Use it when you want index-grounded browser steps (no screenshot-to-coordinates planner) with YAML replay after `generate`. Prefer [Jev Ultrafast](jev-ultrafast.md) / [Midscene JEV Runner](midscene-jev-runner.md) for other Playwright+Jev stacks; prefer [Jev Browser Skill](jev-browser-skill.md) for a minimal teaching skill.

## How it works

Observation assigns each visible control an id, role, name, and allowed ops. Live steps ask Jev `/systemone` which op and which index (typing phrases come from the goal). Actions hit `data-codexqa-jev-browser-id`. Knowledge notes bias decisions; `--decisions` scripts skip the model. Reports keep marked screenshots and timing under `reports/`.

## Get started

```sh
git clone https://github.com/openqa-cn/jev-browser.git
cd jev-browser
git checkout ea82bc96597b07f27a386288b196b0bca1cdcb3a
npm install
npx codexqa-jev-browser observe examples/app/index.html
npx codexqa-jev-browser run cases/examples/search-docs.yaml
# Live auto needs .env with TYPESAFE_API_KEY (charges)
```

## Examples and demos

- `cases/examples/`, `cases/scripts/decisions-search.yaml`, `examples/app/` local HTML.
- HTML report preview linked from README; offline `tests/` (vitest) do not call live models.

## Limits and data handling

Live decisions send page index text and goal phrases to TypeSafe or the chat fallback; password field values are omitted from model requests. Knowledge notes are required for site-specific facts. This listing did not run headed Chromium or live Jev.

## Review and maintenance

Reviewed on **2026-09-23** at [commit ea82bc9](https://github.com/openqa-cn/jev-browser/tree/ea82bc96597b07f27a386288b196b0bca1cdcb3a) (**0.1.0**, MIT). AI-assisted source review of README, LICENSE, package metadata. No live TypeSafe spend.

Related: [Midscene JEV Runner](midscene-jev-runner.md), [Jev Browser Skill](jev-browser-skill.md), [Jev Ultrafast](jev-ultrafast.md).
