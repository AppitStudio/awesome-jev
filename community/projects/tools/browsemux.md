# Browsemux (bounded browser loop where Jev proposes typed actions and code validates them)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

A dependency-free Node CLI and library between agent harnesses and browser backends (agent-browser or BSK): it observes the page, asks a decision provider such as Jev for a typed next action, validates it against targets, roles, inputs, URLs, repetition and completion criteria, acts, and stops within a strict budget. Ships a routing skill for Codex, Claude Code, Cursor, OpenCode and Hermes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xenstar/browsemux) |
| Maintainer | [xenstar](https://github.com/xenstar). Independently curated. |
| Format | Node.js CLI + library (npm) |
| Requirements | Node.js 20+, a browser backend (agent-browser or BSK), and a TypeSafe key (or OpenRouter Decisions / an OpenAI-compatible provider). |
| License | [MIT](https://github.com/xenstar/browsemux/blob/c218a16b23ba64f24a1ec2ccc459dbec8602e62a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions/decisions-api.mjs`](https://github.com/xenstar/browsemux/blob/c218a16b23ba64f24a1ec2ccc459dbec8602e62a/src/decisions/decisions-api.mjs) at the pinned commit. |

## When to use

- Give an agent harness short, budgeted browser tasks where a decision model picks the next step and code keeps control.
- Mismatch: open-ended browsing or production automation; the project is pre-release.

## How it works

`src/decisions/decisions-api.mjs` sends the observed page state to `https://api.typesafe.ai/v1/systemone` (or OpenRouter's Decisions API) with the questions built in `questions.mjs`; the model only proposes intent and never gets a browser handle, and outcomes are reported as verified success, unverified completion, limits, blockers or unknown effect. Integration evidence: [`src/decisions/decisions-api.mjs`](https://github.com/xenstar/browsemux/blob/c218a16b23ba64f24a1ec2ccc459dbec8602e62a/src/decisions/decisions-api.mjs).

## Get started

Install from npm, set your key and run a bounded task.

```sh
npm install -g browsemux
export TYPESAFE_API_KEY=...
browsemux run --backend agent-browser --provider typesafe \
  --url https://example.com --goal "Open the Learn more documentation link" \
  --success-url-contains iana.org
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xenstar/browsemux/blob/c218a16b23ba64f24a1ec2ccc459dbec8602e62a/README.md](https://github.com/xenstar/browsemux/blob/c218a16b23ba64f24a1ec2ccc459dbec8602e62a/README.md)

## Limits and data handling

Page observations (text, roles, URLs) are sent to the chosen provider for each step, with per-call cost. Pre-release; benchmark figures in the README were not reproduced.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit c218a16b23ba](https://github.com/xenstar/browsemux/tree/c218a16b23ba64f24a1ec2ccc459dbec8602e62a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
