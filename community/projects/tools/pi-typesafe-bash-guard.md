# pi-typesafe-bash-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that classifies every bash tool call and user `!` / `!!` shell command with TypeSafe Jev before execution (`not_harmful` / `may_be_harmful` / `harmful`), with optional 1Password secret references for the API key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gowthamgts/pi-stuff/tree/main/extensions/typesafe-bash-guard) |
| Maintainer | [gowthamgts](https://github.com/gowthamgts) (Gowtham Gopalakrishnan). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension **@gowthamgts/pi-typesafe-bash-guard 0.1.0** (npm; lives under the `gowthamgts/pi-stuff` monorepo). |
| Requirements | Node.js **≥ 20**; Pi coding agent (`@earendil-works/pi-coding-agent` peer). Live reviews need `TYPESAFE_API_KEY` (plaintext or `op://…` 1Password reference). Offline tests mock the TypeSafe client. |
| License | [MIT](https://github.com/gowthamgts/pi-stuff/blob/58ca43d41444b182538d8a158cc1d1588771561c/extensions/typesafe-bash-guard/LICENSE) (extension + monorepo). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live TypeSafe reviews were not run. Discovered via X ([post](https://x.com/gowthamgts/status/2101635898991587785)). |

## When to use

Use it when Pi sessions should gate **bash only**—agent tool calls and interactive `!` shells—with a three-way Jev Choice and UI confirmations. Prefer [pi-jev-sentinel](pi-jev-sentinel.md) for broader tool/output/reply screening across Pi/Claude/Codex. Prefer [toolgate](toolgate.md) / [typesafe-agent-gates](typesafe-agent-gates.md) for non-Pi agent firewalls. Prefer [pi-jev](pi-jev.md) when you want gate + output judge + `jev_ask` rather than bash-only classification.

## How it works

[`index.ts`](https://github.com/gowthamgts/pi-stuff/blob/58ca43d41444b182538d8a158cc1d1588771561c/extensions/typesafe-bash-guard/index.ts) uses `@typesafe-ai/sdk` (`choice`, `TypeSafeClient`) with model `jev-latest` to classify each command plus working directory and source (`agent` / `user`). `harmful` always blocks; `may_be_harmful` (and low-confidence `not_harmful` below 0.65) asks the user; API failures fail open with a warning. Review lines are display-only and do not enter model context. `op://` keys are resolved via `op read` without a shell.

## Get started

```sh
pi install npm:@gowthamgts/pi-typesafe-bash-guard
# or from the reviewed monorepo tip:
git clone https://github.com/gowthamgts/pi-stuff.git
cd pi-stuff/extensions/typesafe-bash-guard
git checkout 58ca43d41444b182538d8a158cc1d1588771561c
npm install
npm test
```

Set `TYPESAFE_API_KEY` before real sessions. Live reviews send the full command, cwd, and source to TypeSafe and can incur charges; this listing ran offline tests only.

## Examples and demos

- Offline `npm test` — 8 tests passed on the review host (allow/block/ask/fail-open paths with a mocked client).
- README footer/status UX description and 1Password setup notes.

## Limits and data handling

Every reviewed command leaves the machine. Fail-open on API errors can allow execution when TypeSafe is down—operators who need fail-closed should choose a different gate. Bash-only scope: other tool types are out of band. Upstream latency/confidence UX claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at monorepo [commit 58ca43d](https://github.com/gowthamgts/pi-stuff/tree/58ca43d41444b182538d8a158cc1d1588771561c) (`extensions/typesafe-bash-guard`): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `index.ts`, and tests. Ran `npm install` and `npm test` (8 pass). No live TypeSafe calls.

Related: [pi-jev-sentinel](pi-jev-sentinel.md), [pi-jev](pi-jev.md), [toolgate](toolgate.md).
