# catherd

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Herds coding agents from your Claude Code session: Claude plans and verifies, Codex/opencode write code, TypeSafe Jev picks the model

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/47vigen/catherd) |
| Maintainer | [47vigen](https://github.com/47vigen). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript · agent orchestrator (MIT). |
| Requirements | Claude Code session; TypeSafe credentials for Jev model picks; Codex/opencode as writers. |
| License | [MIT](https://github.com/47vigen/catherd/blob/151087bddcba6daa6e3dfef40ccf06304bbf0fd1/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when coordinating multi-agent coding with a System One model picker.

## How it works

Orchestrator asks Jev which writer model fits each task. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/47vigen/catherd.git
cd catherd
git checkout 151087bddcba6daa6e3dfef40ccf06304bbf0fd1
```

Pin revision `151087bddcba6daa6e3dfef40ccf06304bbf0fd1` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 151087b](https://github.com/47vigen/catherd/tree/151087bddcba6daa6e3dfef40ccf06304bbf0fd1). AI-assisted README and LICENSE inspection; install/live paths not executed.
