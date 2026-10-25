# jeval by osolmaz (framework for decision-model harnesses that look around before they decide)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

TypeScript framework where your program offers a decision model such as Jev a short menu of next steps, runs the chosen one and shows what it found until the model can answer the task's questions; domains are a few small TypeScript pieces, every option probability is kept, and traces can be replayed or forked. Ships a legal-judge domain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/osolmaz/jeval) |
| Maintainer | [osolmaz](https://github.com/osolmaz). Independently curated. |
| Format | TypeScript library and CLI (pnpm) |
| Requirements | Node.js 22.13+ and pnpm; a pi-ai provider key such as `TYPESAFE_API_KEY` for `typesafe/jev-latest`; Poppler, LibreOffice and Netpbm for the legal-judge domain. |
| License | [MIT](https://github.com/osolmaz/jeval/blob/09d87f45d77ac6113b5c4c83d17baaafc3598b3b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models/pi-ai.ts`](https://github.com/osolmaz/jeval/blob/09d87f45d77ac6113b5c4c83d17baaafc3598b3b/src/models/pi-ai.ts) at the pinned commit. |

## When to use

- Build an agent loop where a classifier explores a case (read a log, open a file) before deciding.
- Replay or fork a recorded run to test a different model or prompt.
- Mismatch: not to be confused with the separately listed rlaope/jeval; install pinned to a commit.

## How it works

`src/models/pi-ai.ts` wraps a pi-ai classifier model named `provider/id`; the CLI's `run`, `rejudge`, `replay` and `compare` commands default to `typesafe/jev-latest` and read the key from the provider's environment variable. Integration evidence: [`src/models/pi-ai.ts`](https://github.com/osolmaz/jeval/blob/09d87f45d77ac6113b5c4c83d17baaafc3598b3b/src/models/pi-ai.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/osolmaz/jeval && cd jeval && pnpm install
export TYPESAFE_API_KEY=...
node src/cli/main.ts run cases/case-1 --out results --model typesafe/jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/osolmaz/jeval#readme](https://github.com/osolmaz/jeval#readme)

## Limits and data handling

Each step's state and menu go to the configured model provider. Traces are written locally.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 09d87f45d77a](https://github.com/osolmaz/jeval/tree/09d87f45d77ac6113b5c4c83d17baaafc3598b3b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
