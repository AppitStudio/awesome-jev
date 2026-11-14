# jev-cron-gate (Hermes plugin that skips agent cron runs Jev judges would do nothing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Fills the Hermes cron wake-gate slot: before a scheduled agent run, Jev scores one yes/no question ("would running now do useful work?") over a small snapshot of files, recent changes, localhost URLs or text, and the run is skipped when the answer is no. Fails open on errors and wakes the agent after a set number of consecutive skips; logs runs and skip rates per gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/superlowburn/hermes-jev-cron-gate) |
| Maintainer | [superlowburn](https://github.com/superlowburn). Independently curated. |
| Format | Hermes agent plugin (Python, MIT) |
| Requirements | Hermes agent with plugin support and a `TYPESAFE_API_KEY` (or `JEV_API_KEY`) in the profile `.env`. |
| License | [MIT](https://github.com/superlowburn/hermes-jev-cron-gate/blob/3b2ca30d263be1233e7639108e54e91a74380f8e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gate.py`](https://github.com/superlowburn/hermes-jev-cron-gate/blob/3b2ca30d263be1233e7639108e54e91a74380f8e/gate.py) at the pinned commit. |

## When to use

- Cut the cost of agent cron jobs that mostly wake up to report "still waiting".
- Mismatch: jobs that must run on schedule regardless of state.

## How it works

`gate.py` posts the combined state (capped at 6,000 characters) to `https://api.typesafe.ai/v1/systemone` and prints `{"wakeAgent": false}` when the score is below the gate's cut; `tools.py` exposes setup, test and status actions to the agent. Integration evidence: [`gate.py`](https://github.com/superlowburn/hermes-jev-cron-gate/blob/3b2ca30d263be1233e7639108e54e91a74380f8e/gate.py).

## Get started

Install the plugin, add your key, then create and attach a gate.

```sh
hermes plugins install jev-cron-gate --enable
echo 'TYPESAFE_API_KEY=...' >> ~/.hermes/.env
# then ask the agent: jev_cron_gate(action="setup", name="heartbeat", job_id="...", question="...")
hermes cron edit <job_id> --script jev_gate_heartbeat.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/superlowburn/hermes-jev-cron-gate/blob/3b2ca30d263be1233e7639108e54e91a74380f8e/README.md](https://github.com/superlowburn/hermes-jev-cron-gate/blob/3b2ca30d263be1233e7639108e54e91a74380f8e/README.md)

## Limits and data handling

The gate's source snapshot (files, tails, change lists, localhost responses) is sent to TypeSafe on your key. A wrong 'no' delays work until the consecutive-skip limit forces a run.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 3b2ca30d263b](https://github.com/superlowburn/hermes-jev-cron-gate/tree/3b2ca30d263be1233e7639108e54e91a74380f8e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
