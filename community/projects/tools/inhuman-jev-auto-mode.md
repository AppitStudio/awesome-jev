# inhuman (local agent harness with Jev auto-mode tool-call policies)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Background daemon agent workspace with web and terminal clients whose policy packages can ask Jev whether an agent's tool call may run without a prompt, for Pi, OpenCode, OpenClaw, Crush, Aider and Continue.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/here-build/inhuman-harness) |
| Maintainer | [here-build](https://github.com/here-build). Independently curated. |
| Format | Node.js daemon, CLI and policy packages (TypeScript, MIT) |
| Requirements | Node.js 22+ on macOS or Linux, a model provider, and `TYPESAFE_API_KEY` (or `JEV_API_KEY`) for the Jev policies. |
| License | [MIT](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`env-capabilities/env-capability-decision-jev/src/capability.ts`](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/env-capabilities/env-capability-decision-jev/src/capability.ts) at the pinned commit. |

## When to use

- Let an agent run low-risk tool calls unattended while Jev flags the rest for approval.
- Keep agent sessions alive in a daemon you reopen from browser or terminal.
- Mismatch: docs/packages.md says the other-agent Jev/Sage adapters are currently private source packages, not published to npm.

## How it works

`env-capability-decision-jev` wraps the Jev decide call as an environment capability; the `*-jev-auto-mode` packages under `packages-policy/` bind it to each host agent's before-tool-call hook, with Sage variants as an alternative judge. Integration evidence: [`env-capabilities/env-capability-decision-jev/src/capability.ts`](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/env-capabilities/env-capability-decision-jev/src/capability.ts).

## Get started

Start the product with `npx inhuman web`, connect a model, then read the specific `packages-policy/<agent>-jev-auto-mode/README.md` before wiring a Jev policy.

```sh
npx inhuman web
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Package map: [github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/packages.md](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/packages.md)

## Limits and data handling

Tool-call context goes to TypeSafe on your key when a Jev policy is enabled; pending approvals still need you.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 01a9ceafbb17](https://github.com/here-build/inhuman-harness/tree/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
