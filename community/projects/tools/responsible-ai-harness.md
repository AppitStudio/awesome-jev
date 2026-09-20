# Responsible AI Harness

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Model-agnostic assessment harness: deterministic hard rules plus an optional TypeSafe Jev judge for prompt injection, secret/PII leakage, unsafe tool use, and policy bypass—emitting checksummed evidence bundles and a static report UI. Assessment only; never enforces production traffic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/syabdulr/responsible-ai-harness) |
| Maintainer | [syabdulr](https://github.com/syabdulr). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript package (`responsible-ai-harness` **0.1.0**) with CLI scripts, Vitest suite, and static report UI. |
| Requirements | Node.js 22+; offline demo needs no API key. Live Jev is opt-in (`npm run assess:jev-live`) behind an explicit confirmation and a TypeSafe key (env or macOS Keychain). |
| License | [MIT](https://github.com/syabdulr/responsible-ai-harness/blob/b1fb72ab44ecead5700a46b3d49063c352118646/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source, `npm run check`, and offline demo inspected. Live TypeSafe assessment was not run. |

## When to use

Use it to run portable, versioned safety assessments with hard-rule precedence and optional Jev semantic judgment, then verify evidence offline. Prefer [toolgate](toolgate.md) / [pi-jev-sentinel](pi-jev-sentinel.md) for online agent tool gates rather than offline assessment reports. Do not treat fixture StubJudge scores as measured live Jev risk.

## How it works

Fixture cases hit a loopback synthetic target; hard rules always run. When enabled, [`JevJudge`](https://github.com/syabdulr/responsible-ai-harness/blob/b1fb72ab44ecead5700a46b3d49063c352118646/src/judges/jev.ts) posts allowlisted, redacted evidence through the official `@typesafe-ai/sdk` transport ([`jev-transport-typesafe.ts`](https://github.com/syabdulr/responsible-ai-harness/blob/b1fb72ab44ecead5700a46b3d49063c352118646/src/judges/jev-transport-typesafe.ts)). Missing keys, transport errors, and low confidence route to human review (fail-closed for the judge path). Runs write checksummed bundles and self-hashing `report.json`; the UI re-verifies before showing a Live Jev source.

## Get started

```sh
git clone https://github.com/syabdulr/responsible-ai-harness.git
cd responsible-ai-harness
git checkout b1fb72ab44ecead5700a46b3d49063c352118646
npm ci --ignore-scripts
npm run check
npm run demo    # offline fixtures → ./evidence-out/
npm run ui      # http://127.0.0.1:4790/ (zero network)
```

Live Jev (billed, capped): follow upstream `assess:jev-live` only after reading its confirmation gate. This listing did not run it.

## Examples and demos

- Offline screenshots under [`docs/screenshots/`](https://github.com/syabdulr/responsible-ai-harness/tree/b1fb72ab44ecead5700a46b3d49063c352118646/docs/screenshots) (upstream; offline demo path).
- Upstream documents a separate live-run screenshot and TypeSafe usage dash—vendor-reported, not re-run here.
- Vitest covers judges, evidence, report integrity, and MCP connector paths with stubs.

## Limits and data handling

Hard-rule failures cannot be overridden by Jev. Live calls send redacted assessment evidence to TypeSafe; residual high-risk patterns refuse the call. The harness does not block production traffic. Offline StubJudge results are deterministic fixtures, not live probabilities.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b1fb72a](https://github.com/syabdulr/responsible-ai-harness/tree/b1fb72ab44ecead5700a46b3d49063c352118646): **0.1.0**, MIT. AI-assisted source review of Jev judge/transport, README, and LICENSE. On Node.js 22.23.2: **`npm run check`** passed (**395** Vitest tests). **`npm run demo`** wrote an offline evidence bundle. No live TypeSafe calls.

Related: [toolgate](toolgate.md), [pi-jev-sentinel](pi-jev-sentinel.md), [is-malicious](is-malicious.md), [jeval](jeval.md).
