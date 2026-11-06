# tinysubagent (herdr-native Pi subagents with optional TypeSafe Jev model-profile routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that spawns markdown-defined subagents in a shared herdr column with fire-and-forget and parallel batches. Optional model profiles can route through TypeSafe System One (`jev-latest`) via the bundled systemone client.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tinypi-extension/tinysubagent) |
| Maintainer | [tinypi-extension](https://github.com/tinypi-extension). Independently curated. |
| Format | Pi extension (TypeScript, MIT) |
| Requirements | Pi coding agent, herdr ≥0.8.2, and a TypeSafe key when using System One routing. |
| License | [MIT](https://github.com/tinypi-extension/tinysubagent/blob/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone/client.ts`](https://github.com/tinypi-extension/tinysubagent/blob/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7/src/systemone/client.ts) at the pinned commit. |

## When to use

- Delegate parallel Pi subagents inside herdr.
- Route child model profiles with a System One classifier.
- Mismatch: tool registers only inside herdr; outside it there is no pane to split.

## How it works

`src/systemone/client.ts` posts to `https://api.typesafe.ai` with model `jev-latest` for classifier routing of subagent profiles. Integration evidence: [`src/systemone/client.ts`](https://github.com/tinypi-extension/tinysubagent/blob/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7/src/systemone/client.ts).

## Get started

`pi install git:github.com/tinypi-extension/tinysubagent` then update extensions.

```sh
pi install git:github.com/tinypi-extension/tinysubagent
pi update --extensions
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tinypi-extension/tinysubagent/blob/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7/README.md](https://github.com/tinypi-extension/tinysubagent/blob/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7/README.md)

## Limits and data handling

Classifier inputs are sent to TypeSafe when System One routing is enabled.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 88a62170db6b](https://github.com/tinypi-extension/tinysubagent/tree/88a62170db6bf8843f8ad7f1d1e8a8e942a474f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
