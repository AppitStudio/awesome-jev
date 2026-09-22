# wellposed

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency linter for TypeSafe Jev requests: catches broken state paths, missing Choice escape hatches, bundled judgments, and other structural smells before you call the API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/suraj-phanindra/wellposed) |
| Maintainer | [suraj-phanindra](https://github.com/suraj-phanindra). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm package **`wellposed` 0.4.0** (CLI bin `wellposed`; zero runtime dependencies). |
| Requirements | Node ≥ 18. Structural lint is offline; optional semantic eval scripts may call TypeSafe when configured. |
| License | [MIT](https://github.com/suraj-phanindra/wellposed/blob/86e6f8cb17e464eab33dcf44a0015fdb616b1fc2/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline structural tests and example lint inspected; live TypeSafe semantic evals not run on the review host. Distinct from [riff](riff.md) (prose lint) and [japanese-jev-lint](japanese-jev-lint.md). |

## When to use

Use it when you want to **lint Jev `state`/`questions` payloads** for known failure modes (no escape hatch, broken paths, arithmetic-in-question, bundled judgments) before paying for API calls. Prefer [jev-calibrate](jev-calibrate.md) once you have labelled outcomes to tune gates.

## How it works

The CLI/`structural.mjs` module walks a Jev request JSON and emits error/warn/info findings with TypeSafe docs links. Semantic agreement helpers exist under `skills/wellposed/eval/` for optional live checks; structural rules need no key.

## Get started

```sh
git clone https://github.com/suraj-phanindra/wellposed.git
cd wellposed
git checkout 86e6f8cb17e464eab33dcf44a0015fdb616b1fc2
node --test skills/wellposed/eval/structural.test.mjs
node skills/wellposed/scripts/wellposed.mjs lint skills/wellposed/examples/support-ticket.json
# Or: npx wellposed@0.4.0 lint path/to/request.json
```

Live semantic evals (if used) send requests to TypeSafe and may incur charges. This listing ran structural tests and the example lint only.

## Examples and demos

- Offline on the review host: `node --test skills/wellposed/eval/structural.test.mjs` → **35 passed**; example lint reported 1 error / 4 warn / 1 info on the bundled support-ticket fixture.
- Upstream SKILL.md for agent install paths.

## Limits and data handling

Structural lint is local. Semantic/live agreement paths depend on keys and are out of scope for this listing’s offline evidence. Findings are heuristics aligned with TypeSafe docs—not a guarantee of model correctness.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 86e6f8c](https://github.com/suraj-phanindra/wellposed/tree/86e6f8cb17e464eab33dcf44a0015fdb616b1fc2): **0.4.0**, MIT. AI-assisted source review of README, LICENSE, `skills/wellposed/scripts/`. Offline structural suite 35 passed; example lint OK. No live TypeSafe on the review host.

Related: [jev-calibrate](jev-calibrate.md), [riff](riff.md), [japanese-jev-lint](japanese-jev-lint.md).
