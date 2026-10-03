# jev-permission-gate (madisonrickert)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code auto-mode PreToolUse gate: TypeSafe Jev answers risk questions to allow/deny/defer to the built-in classifier.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/madisonrickert/jev-permission-gate) |
| Maintainer | [madisonrickert](https://github.com/madisonrickert). Independently curated. |
| Format | Claude Code mod/plugin (MIT) |
| Requirements | See upstream README; provider keys when using live hosted paths. |
| License | [`MIT`](https://github.com/madisonrickert/jev-permission-gate/blob/15ec5f35778c0d102e2c4519f3b8ee2ce8cd69a8/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from weiping/jev-claude-code and RahulBalakavi/claude-code-jev permission gates. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Claude Code auto-mode PreToolUse gate: TypeSafe Jev answers risk questions to allow/deny/defer to the built-in classifier. Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/madisonrickert/jev-permission-gate.git
cd jev-permission-gate
git checkout 15ec5f35778c0d102e2c4519f3b8ee2ce8cd69a8
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README: eight yes/no Jev questions; allow/deny/defer thresholds; TypeSafe API key. ([upstream evidence](https://github.com/madisonrickert/jev-permission-gate/blob/15ec5f35778c0d102e2c4519f3b8ee2ce8cd69a8/README.md)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 15ec5f35778c](https://github.com/madisonrickert/jev-permission-gate/tree/15ec5f35778c0d102e2c4519f3b8ee2ce8cd69a8). AI-assisted README and license inspection; install/live paths not executed.
