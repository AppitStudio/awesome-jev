# pi-Jev-browser

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Pi coding-agent extension: Playwright browser tools where TypeSafe Jev chooses each action over a structured DOM observation in a bounded loop (port of the Cline jev-browser plugin).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/laihenyi/pi-Jev-browser) |
| Maintainer | [laihenyi](https://github.com/laihenyi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package `pi-jev-browser` **0.1.0** — Pi extension (`pi install npm:pi-jev-browser`) with Playwright Chromium and `@typesafe-ai/sdk`. |
| Requirements | Pi coding agent, Node.js as required by the package, `TYPESAFE_API_KEY` (or `typesafe.apiKey` in config). First install may download ~150 MB Chromium. Field text for typed inputs uses the active Pi model. |
| License | [Apache-2.0](https://github.com/laihenyi/pi-Jev-browser/blob/0adf53f6901cf170c75fb616a20693ec6c74d4e1/LICENSE). |

## When to use

Use it when you already run Pi and want a Jev-driven DOM loop instead of screenshot-per-step browser control. Prefer [Jev Ultrafast](jev-ultrafast.md) or [Jev Browser (tontoko)](jev-browser-tontoko.md) for standalone Python/TypeScript agents outside Pi, or a pure-Jev (no helper LLM) browser agent such as buluoray/JevOnly when listed.

## How it works

`jev_run` starts or reuses a browser, observes the page, and posts System One requests (`jev-latest` by default) so Jev selects the next action from enumerated options. Typing helpers can call the session's Pi model for field text. Credential and model defaults are in [`src/credentials.ts`](https://github.com/laihenyi/pi-Jev-browser/blob/0adf53f6901cf170c75fb616a20693ec6c74d4e1/src/credentials.ts); tool surface is registered from [`index.ts`](https://github.com/laihenyi/pi-Jev-browser/blob/0adf53f6901cf170c75fb616a20693ec6c74d4e1/index.ts). Runs stop on uncertainty, limits, policy, or cancellation; `done_unverified` is a claim, not proof.

## Get started

```sh
pi install npm:pi-jev-browser
export TYPESAFE_API_KEY=...
# then use jev_run from a Pi session
```

Or inspect the reviewed commit:

```sh
git clone https://github.com/laihenyi/pi-Jev-browser.git
cd pi-Jev-browser
git checkout 0adf53f6901cf170c75fb616a20693ec6c74d4e1
npm install --ignore-scripts
node --test --experimental-strip-types test/*.test.ts
```

Live `jev_run` drives a real browser and calls TypeSafe (and possibly the Pi text model). This listing did not install into Pi or run live browsing.

## Examples and demos

- [`test/`](https://github.com/laihenyi/pi-Jev-browser/tree/0adf53f6901cf170c75fb616a20693ec6c74d4e1/test): offline loop, policy, observation, and manager coverage.
- [`benchmarks/`](https://github.com/laihenyi/pi-Jev-browser/tree/0adf53f6901cf170c75fb616a20693ec6c74d4e1/benchmarks): upstream capability suite (not re-run here).
- Upstream README documents differences from the Cline plugin.

## Limits and data handling

Page observations and field values are sent to TypeSafe; typed text may also go to the active Pi model. Origin allow/deny policy is local. Chromium and OS library prerequisites remain operator-managed on Linux. Benchmark scores and demo goals are not catalog accuracy claims.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 0adf53f](https://github.com/laihenyi/pi-Jev-browser/tree/0adf53f6901cf170c75fb616a20693ec6c74d4e1): `pi-jev-browser` **0.1.0**, Apache-2.0. AI-assisted source review of credentials/policy/index tooling, README, and license. On Node.js 24.8.0, **`node --test --experimental-strip-types test/*.test.ts`: 83 passed**. No live TypeSafe calls or Pi session installs were performed.

Related: [Jev Ultrafast](jev-ultrafast.md), [Jev Browser (tontoko)](jev-browser-tontoko.md), [pi-jev](pi-jev.md).
