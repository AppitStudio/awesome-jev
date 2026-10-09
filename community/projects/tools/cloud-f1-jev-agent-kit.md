# Jev Agent Kit (cloud-f1)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that shortens long `Bash` output before it reaches the model, using a local rules engine with an optional Jev relevance pass; the original output is always kept and recoverable via `/jev readback`. Unofficial community project; the README labels it v0.3.0, measured in pieces, not proven end to end.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cloud-f1/jev-agent-kit) |
| Maintainer | [cloud-f1](https://github.com/cloud-f1). Independently curated. |
| Format | Claude Code plugin (Mod + `/jev` command + skill) and Python CLI |
| Requirements | Claude Code 2.1.287 or later; TypeSafe API key only for `backend: jev`. |
| License | [MIT](https://github.com/cloud-f1/jev-agent-kit/blob/3cb2fb6183a53a51a0c11d5c334110dac2ada3de/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Cut noisy command output in Claude Code sessions while keeping errors and a read-back pointer.
- Mismatch: cost savings are unproven per the README; the Jev pruning path in a real session has not been run by the maintainer.

## How it works

Keeps head, tail, and error/warning blocks; with `backend: jev`, Jev scores the remaining blocks for relevance. Any failure returns the original output. (Summarized from the upstream [README](https://github.com/cloud-f1/jev-agent-kit/blob/3cb2fb6183a53a51a0c11d5c334110dac2ada3de/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `/plugin marketplace add cloud-f1/jev-agent-kit` then `/plugin install jev-agent-kit --marketplace cloud-f1/jev-agent-kit`.

## Limits and data handling

Local rules mode needs no network; Jev mode sends output blocks to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit 3cb2fb6183a5](https://github.com/cloud-f1/jev-agent-kit/tree/3cb2fb6183a53a51a0c11d5c334110dac2ada3de). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
