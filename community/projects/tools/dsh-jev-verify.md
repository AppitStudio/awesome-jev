# dsh-jev-verify

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin that exposes TypeSafe Jev as `jev_decision` (choice/score/noul in one call) plus `jev_verify` (live labeled benchmark). Honest-by-design: no mock fallback; missing keys fail explicitly. Distinct from [dsh-jev](dsh-jev.md) (`jev_ask` only).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xienda/dsh-jev-verify) |
| Maintainer | [xienda](https://github.com/xienda). Independently curated; this page is not an upstream submission or endorsement. Also on npm as `dsh-jev-verify`. |
| Format | DSH plugin package **dsh-jev-verify 0.1.0** (JavaScript; Node ≥ 20; targets dsh ≥ `0.1.5-rc.2`). |
| Requirements | DeepSeek Harness profile; `TYPESAFE_API_KEY` (or plugin credentials / `apiKey` config). Optional `TYPESAFE_BASE_URL` / `TYPESAFE_MODEL`. |
| License | [MIT](https://github.com/xienda/dsh-jev-verify/blob/be731a656dacaf891b079ca9fe1f5fdc0d4af024/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. `npm run check` (syntax) passed; live `jev_verify` / TypeSafe smoke not run. |

## When to use

Use it when a DSH agent should call typed Jev decisions with auditable latency/usage and occasionally self-check the endpoint with a labeled live benchmark. Prefer [dsh-jev](dsh-jev.md) for a narrower `jev_ask` install from a GitHub pin; prefer [ask-jev-skill](ask-jev-skill.md) for Hermes.

## How it works

[`lib/index.js`](https://github.com/xienda/dsh-jev-verify/blob/be731a656dacaf891b079ca9fe1f5fdc0d4af024/lib/index.js) registers Cordis tools. `jev_decision` posts `state` + questions to System One and returns typed answers, confidence, usage, latency, and estimated cost. `jev_verify` runs the bundled labeled cases against the live API and refuses to invent metrics. A dependency-free `bench/bench.mjs` CLI reproduces the benchmark with any key.

## Get started

```sh
git clone https://github.com/xienda/dsh-jev-verify.git
cd dsh-jev-verify
git checkout be731a656dacaf891b079ca9fe1f5fdc0d4af024
npm run check
# In a DSH profile (live key required for tools):
# dsh plugin --profile web add dsh-jev-verify
export TYPESAFE_API_KEY=…
```

Live tools and `jev_verify` call TypeSafe and can incur charges; this listing did not run them.

## Examples and demos

- Upstream `docs/verification.md` and README usage JSON.
- This listing: `npm run check` **passed**. Functional tests that need live API were not run.

## Limits and data handling

`state` and question text reach TypeSafe. No offline mock path by design. Install via DSH plugin market / Cordis patch as documented upstream.

## Review and maintenance

Reviewed on **2026-09-21** at [commit be731a6](https://github.com/xienda/dsh-jev-verify/tree/be731a656dacaf891b079ca9fe1f5fdc0d4af024): MIT; AI-assisted source review of README, LICENSE, `lib/`, and `npm run check`. No live TypeSafe call.

Related: [dsh-jev](dsh-jev.md), [ask-jev-skill](ask-jev-skill.md), [jev-mcp](jev-mcp.md).
