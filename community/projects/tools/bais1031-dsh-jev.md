# dsh-jev by Bais1031 (DeepSeek Harness plugin that adds Jev decision briefs at critical analysis steps)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DeepSeek Harness (DSH) plugin that calls Jev at critical analysis nodes chosen by deterministic rules and records short probabilistic decision briefs. Shadow mode only records them for later evaluation of decision accuracy and wasted exploration; advisory mode adds briefs that pass protocol and confidence checks to the current request. Neither mode changes the provider, model or reasoning effort.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Bais1031/dsh-jev) |
| Maintainer | [Bais1031](https://github.com/Bais1031). Independently curated. |
| Format | DSH plugin (TypeScript) |
| Requirements | DeepSeek Harness with the Web profile, pnpm, and a Jev (TypeSafe) API key. |
| License | [MIT](https://github.com/Bais1031/dsh-jev/blob/7c878e1d0a39a013cf769dfc0656c1c062422df5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.ts`](https://github.com/Bais1031/dsh-jev/blob/7c878e1d0a39a013cf769dfc0656c1c062422df5/src/client.ts) at the pinned commit. |

## When to use

- Measure whether a decision model would have steered a coding agent better before letting it.
- Mismatch: not on npm; build from source. Distinct from the other dsh-jev plugins in this catalog.

## How it works

`src/client.ts` is an HTTP client for `https://api.typesafe.ai/v1/systemone` (`jev-latest`); `src/dsh-plugin.ts` limits critical nodes, call frequency and input size. Integration evidence: [`src/client.ts`](https://github.com/Bais1031/dsh-jev/blob/7c878e1d0a39a013cf769dfc0656c1c062422df5/src/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Bais1031/dsh-jev && cd dsh-jev
pnpm install && pnpm build
dsh plugin --profile web add "$PWD"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Bais1031/dsh-jev#readme](https://github.com/Bais1031/dsh-jev#readme)

## Limits and data handling

Analysis context at critical nodes goes to TypeSafe, capped by the plugin settings.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 7c878e1d0a39](https://github.com/Bais1031/dsh-jev/tree/7c878e1d0a39a013cf769dfc0656c1c062422df5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
