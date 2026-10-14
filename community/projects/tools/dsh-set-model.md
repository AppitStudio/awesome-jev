# dsh-set-model

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness plugin where TypeSafe Jev auto-switches model presets and thinking depth each turn.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/john-walks-slow/dsh-set-model) |
| Maintainer | [john-walks-slow](https://github.com/john-walks-slow). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript) |
| Requirements | DSH/cordis; TypeSafe API key when jevEnabled. |
| License | [MIT](https://github.com/john-walks-slow/dsh-set-model/blob/754b7ad7ad64e385e4457e9949ec6d3db9d27dce/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/john-walks-slow/dsh-set-model/blob/754b7ad7ad64e385e4457e9949ec6d3db9d27dce/src/jev.ts) at the pinned commit. |

## When to use

- Use when you need: DeepSeek Harness plugin where TypeSafe Jev auto-switches model presets and thinking depth …
- Mismatch: See upstream README for setup limits.

## How it works

See upstream integration at `src/jev.ts`. (Summarized from the upstream README; not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow setup, configure credentials, and run the documented entrypoint.

```sh
# see upstream README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. Not run on the review host.

## Examples and demos

- Evidence path: src/jev.ts.
- Upstream README.

## Limits and data handling

Inputs may go to TypeSafe or the configured provider when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 754b7ad7ad64](https://github.com/john-walks-slow/dsh-set-model/tree/754b7ad7ad64e385e4457e9949ec6d3db9d27dce). Inspected the upstream README, license status, and the Jev integration evidence linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
