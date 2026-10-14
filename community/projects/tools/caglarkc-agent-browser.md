# Agent Browser (caglarkc)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Research browser runtime for AI agents: observes pages through Lightpanda DOM controls, lets Jev choose the next action, and verifies outcomes independently, with reproducible benchmarks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/caglarkc/agent-browser) |
| Maintainer | [caglarkc](https://github.com/caglarkc). Independently curated. |
| Format | Node.js research prototype (CLI + lab) |
| Requirements | Node.js, Lightpanda, TypeSafe API key for live runs. |
| License | [MIT](https://github.com/caglarkc/agent-browser/blob/82296f83367c9c26ecf3cdd821f345ec6293f161/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lab/src/policy.mjs`](https://github.com/caglarkc/agent-browser/blob/82296f83367c9c26ecf3cdd821f345ec6293f161/lab/src/policy.mjs) at the pinned commit. |

## When to use

- Experiment with a decision model choosing browser actions from typed DOM candidates.
- Reproduce the matched live benchmarks recorded in the repository.
- Mismatch: research prototype; performance figures are author-reported.

## How it works

The policy builds a Jev request from the goal, page title/text, recent actions and candidate elements; Jev picks the action, Lightpanda executes it, and a separate verifier checks the result. Integration evidence: [`lab/src/policy.mjs`](https://github.com/caglarkc/agent-browser/blob/82296f83367c9c26ecf3cdd821f345ec6293f161/lab/src/policy.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/caglarkc/agent-browser.git
cd agent-browser/lab
npm ci --ignore-scripts
npm run install:lightpanda
npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark traces: `benchmarks/results/`.

## Limits and data handling

Page text and element labels are sent to TypeSafe for each step and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 82296f83367c](https://github.com/caglarkc/agent-browser/tree/82296f83367c9c26ecf3cdd821f345ec6293f161). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
