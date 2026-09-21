# pi-jev-permit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that asks TypeSafe Jev whether each `bash` / `write` / `edit` call should run, after local hard-deny, allow/deny rules, and a read-only fast path.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kurihada/pi-jev-permit) |
| Maintainer | [kurihada](https://github.com/kurihada). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript Pi package/extension (`pi-jev-permit` 0.2.0; Node `>=22.19`). |
| Requirements | [Pi](https://github.com/badlogic/pi-mono) agent; TypeSafe API key (or gateway preset) for live judgments. Without a key, non-read-only calls are blocked. |
| License | [MIT](https://github.com/kurihada/pi-jev-permit/blob/e81684763eace2ad5cbd5cd2ed32aacff76b09b8/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Offline `npm test`: **104 passed**. No live TypeSafe or full Pi session. |

## When to use

Use it when Pi should gate mutating tools with one typed allow question and explicit local policy floors. Prefer [pi-jev](pi-jev.md) / [pi-jev-sentinel](pi-jev-sentinel.md) for broader gate+judge+ask surfaces; prefer [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md) for bash-only classification. Distinct focus: permission gate with ranked authorization/credential/irreversibility considerations and `/jev-permit allow` override.

## How it works

Judgment order: hard deny (raw argv) → config allow/deny per shell segment → local read-only fast path → one Jev “should this call be allowed?” question. Secrets in command text are redacted before leaving the machine; write/edit sends paths only. Default allow threshold `0.6`; unclear/no-answer blocks (silence is not consent). Status widget shows verdict, route, and latency.

## Get started

```sh
pi install npm:pi-jev-permit
# restart Pi, then:
# /jev-permit login
```

From source (offline tests):

```sh
git clone https://github.com/kurihada/pi-jev-permit.git
cd pi-jev-permit
git checkout e81684763eace2ad5cbd5cd2ed32aacff76b09b8
npm ci --ignore-scripts
npm test
```

Live judgments send redacted command context to TypeSafe (or your gateway) and may incur charges.

## Examples and demos

- README walkthrough of allow/deny widget lines and config JSONC.
- Unit tests covering chain/policy/config/gate/authorization (`npm test`).

## Limits and data handling

Redacted tool call text still leaves the host on Jev judgments. Hard denies and credential rules are not overridden by `/jev-permit allow`. Gateway misconfiguration can block work; `onUnavailable` modes are documented upstream. Not a full sandbox.

## Review and maintenance

Reviewed on **2026-09-21** at [commit e816847](https://github.com/kurihada/pi-jev-permit/tree/e81684763eace2ad5cbd5cd2ed32aacff76b09b8): **0.2.0**, MIT. AI-assisted review of README, `package.json`, LICENSE, and tests. **`npm test`**: 104 passed. No live TypeSafe / Pi UI session.

Related: [pi-jev](pi-jev.md), [pi-jev-sentinel](pi-jev-sentinel.md), [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md), [jev-guard](jev-guard.md).
