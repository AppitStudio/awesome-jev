# dsh-jev-kit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin: about **23** named typed TypeSafe Jev judgments (privacy scan, change-scope, memory/batch triage, and more) on a budgeted, ledger-backed transport—advisory tools only, no hooks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jackchen13755/dsh-jev-kit) |
| Maintainer | [jackchen13755](https://github.com/jackchen13755). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | DSH plugin npm package **@dsh-external/dsh-jev-kit 0.13.0** (install via `dsh plugin … github:jackchen13755/dsh-jev-kit`). |
| Requirements | DeepSeek Harness (`dsh`) with web profile; `TYPESAFE_API_KEY` (shared credential reference with sibling `dsh-jev-lens` per upstream). |
| License | [BSD-3-Clause](https://github.com/jackchen13755/dsh-jev-kit/blob/64ed0406aaa9a4bcc130f38843dac2ba623d75a5/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `lib/client.js`). DSH install and live Jev calls were **not** executed on the review host. Distinct from catalog [dsh-jev](dsh-jev.md) / [dsh-jev-decide](dsh-jev-decide.md) / [dsh-jev-prune](dsh-jev-prune.md) / [dsh-jev-verify](dsh-jev-verify.md). |

## When to use

Use it when a DeepSeek Harness agent should **call named advisory judgments** (scan private diffs, scope-check hunks, triage logs/bugs, pick with no-match) without registering hooks that block or rewrite. Prefer thinner `jev_ask` / `jev_decide` plugins when you only need a generic question surface.

## How it works

Tools such as `jev_kit_decide`, `jev_kit_scan_private`, `jev_kit_scope_check`, `jev_kit_memory`, and `jev_kit_triage` map channels onto typed System One questions over a hardened HTTP client ([`lib/client.js`](https://github.com/jackchen13755/dsh-jev-kit/blob/64ed0406aaa9a4bcc130f38843dac2ba623d75a5/lib/client.js)). Upstream stresses: no text generation, no interception, no hooks—pure suggestions with a per-channel ledger/report.

## Get started

```sh
dsh plugin --profile web add github:jackchen13755/dsh-jev-kit
# restart dsh web; configure TYPESAFE_API_KEY once (shared with dsh-jev-lens)
```

Pin for review: [commit 64ed040](https://github.com/jackchen13755/dsh-jev-kit/tree/64ed0406aaa9a4bcc130f38843dac2ba623d75a5). Optional HTTP status/report under `/dsh-jev-kit/api/…` per upstream README.

## Examples and demos

- Channel catalog table in the upstream README (privacy, agent, batch, recall groups).
- `jev_kit_bench` fixture comparison tool (upstream; not run here).

## Limits and data handling

Judgment payloads go to TypeSafe; redaction/transport behavior depends on the shared client stack. Chinese-first docs. Live DSH/Jev not run on this host.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 64ed040](https://github.com/jackchen13755/dsh-jev-kit/tree/64ed0406aaa9a4bcc130f38843dac2ba623d75a5) (`@dsh-external/dsh-jev-kit` **0.13.0**, BSD-3-Clause). AI-assisted review of README, LICENSE, client. No live TypeSafe spend.

Related: [dsh-jev](dsh-jev.md), [dsh-jev-decide](dsh-jev-decide.md), [dsh-jev-prune](dsh-jev-prune.md), [dsh-jev-verify](dsh-jev-verify.md).
