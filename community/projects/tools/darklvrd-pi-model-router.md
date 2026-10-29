# model-router for Pi (Jev sizes each message and routes small jobs to cheaper models, falling back when unsure)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension: before each message, Jev answers three questions in one request (smallest model size that can do the job, is the request clear, is it self-contained) and the session switches to the mapped model only when all three pass; any timeout, error or doubt keeps the default model. Ships switched off; a 2.5 s cap per call and a status command that shows routing and Jev cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DarkLvrd/model-router) |
| Maintainer | [DarkLvrd](https://github.com/DarkLvrd). Independently curated. |
| Format | Pi extension (JavaScript) |
| Requirements | The Pi coding agent and a TypeSafe API key. |
| License | [MIT](https://github.com/DarkLvrd/model-router/blob/a8b9b94e68dd1b4858f90b444c644c7dfbf7f449/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`lib/jev.mjs`](https://github.com/DarkLvrd/model-router/blob/a8b9b94e68dd1b4858f90b444c644c7dfbf7f449/lib/jev.mjs) at the pinned commit. |

## When to use

- Save money on short coding-agent turns without risking hard ones.
- Mismatch: the size-to-model mapping is the author's and has not been benchmarked.

## How it works

`lib/jev.mjs` calls `https://api.typesafe.ai/v1/systemone` (`jev-latest`, set in `lib/config.mjs`) with the size, clarity and standalone questions, and `lib/policy.mjs` applies the thresholds. Integration evidence: [`lib/jev.mjs`](https://github.com/DarkLvrd/model-router/blob/a8b9b94e68dd1b4858f90b444c644c7dfbf7f449/lib/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
pi install /path/to/model-router
node bin/router.mjs on
node bin/router.mjs status
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with live results: [github.com/DarkLvrd/model-router#readme](https://github.com/DarkLvrd/model-router#readme)

## Limits and data handling

Each routed message goes to TypeSafe while the router is on; nothing is sent while it is off.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit a8b9b94e68dd](https://github.com/DarkLvrd/model-router/tree/a8b9b94e68dd1b4858f90b444c644c7dfbf7f449). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
