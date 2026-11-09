# pi-context-guard-jev (Pi agent extension where Jev trims stale tool output from context)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension: after each run, Jev judges old tool output and off-topic exchanges against the current work, and stale items become one-line notes; README estimates about 25% fewer context tokens.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alandarev/pi-context-guard-jev) |
| Maintainer | [alandarev](https://github.com/alandarev). Independently curated. |
| Format | Pi extension on npm (MIT) |
| Requirements | The Pi agent and an OpenRouter key (`OPENROUTER_API_KEY` or `/login`). |
| License | [MIT](https://github.com/alandarev/pi-context-guard-jev/blob/f865f250d26774505914db764ede007a26de4590/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/alandarev/pi-context-guard-jev/blob/f865f250d26774505914db764ede007a26de4590/src/config.ts) at the pinned commit. |

## When to use

- Cut context tokens in long Pi sessions.
- See which tool outputs a classifier keeps.
- Mismatch: savings are estimated from the author's sessions.

## How it works

`config.ts` sets the classifier to `openrouter/~typesafe/jev-latest`; `index.ts`/`decide.ts` send tool output plus the question and answer to Jev and keep needed lines verbatim. Integration evidence: [`src/config.ts`](https://github.com/alandarev/pi-context-guard-jev/blob/f865f250d26774505914db764ede007a26de4590/src/config.ts).

## Get started

Install with `pi install npm:pi-context-guard-jev` and set an OpenRouter key.

```sh
pi install npm:pi-context-guard-jev
export OPENROUTER_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/alandarev/pi-context-guard-jev/blob/f865f250d26774505914db764ede007a26de4590/README.md](https://github.com/alandarev/pi-context-guard-jev/blob/f865f250d26774505914db764ede007a26de4590/README.md)

## Limits and data handling

Judged tool output is sent to OpenRouter and TypeSafe.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit f865f250d267](https://github.com/alandarev/pi-context-guard-jev/tree/f865f250d26774505914db764ede007a26de4590). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
