# pi-jev-guard by Marc Lefrançois (fail-closed Pi extension where Jev scores every tool call and shell command for danger before it runs)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that sends every tool call and user shell command to Jev as one yes/no danger question before it runs. Calls scoring above 0.60 need your confirmation; if you decline, no UI is available or the classifier fails, the call is blocked.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/marclefrancois/pi-jev-guard) |
| Maintainer | [Marc Lefrançois](https://github.com/marclefrancois). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi with the `typesafe` model provider configured (TypeSafe API key) so `typesafe/jev-latest` is available. |
| License | [MIT](https://github.com/marclefrancois/pi-jev-guard/blob/cce62ad513cabe804830805f368c1b66cc69589d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`index.ts`](https://github.com/marclefrancois/pi-jev-guard/blob/cce62ad513cabe804830805f368c1b66cc69589d/index.ts) at the pinned commit. |

## When to use

- Pi users who want a confirmation step before risky commands without approving every call by hand.
- Mismatch: a sandbox; a low score lets a call run, so it does not replace permissions or backups.

## How it works

`index.ts` hooks Pi's `tool_call` and `user_bash` events, serializes the tool name and input (capped at 12,000 characters) and asks the `typesafe` provider's `jev-latest` a `bool` question about significant harm; a fixed 0.60 threshold decides whether to prompt. Deletion commands are described as destructive in the prompt. Integration evidence: [`index.ts`](https://github.com/marclefrancois/pi-jev-guard/blob/cce62ad513cabe804830805f368c1b66cc69589d/index.ts).

## Get started

Install it into Pi from npm and make sure Pi can reach TypeSafe's Jev.

```sh
pi install npm:@marclefrancois/pi-jev-guard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tests describing the guard's behaviour: [github.com/marclefrancois/pi-jev-guard/tree/main/test](https://github.com/marclefrancois/pi-jev-guard/tree/main/test)

## Limits and data handling

Every tool call and shell command input (up to 12,000 characters) goes to TypeSafe. Fail-closed by design, so a TypeSafe outage blocks tool calls. The npm package name in the README did not resolve on the npm registry on 2026-11-27, so installing from source may be needed.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit cce62ad513ca](https://github.com/marclefrancois/pi-jev-guard/tree/cce62ad513cabe804830805f368c1b66cc69589d). Inspected the README, LICENSE, CHANGELOG and `index.ts` at the pinned commit; the npm package `@marclefrancois/pi-jev-guard` was not found on the public registry on 2026-11-27. Nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
