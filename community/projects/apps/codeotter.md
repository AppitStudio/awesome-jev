# CodeOtter by Dharmesh Gurnani (self-hosted AI code review where a System One model such as Jev answers the scores and yes/no merge gates)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted pull-request reviewer for GitHub, Bitbucket, Azure DevOps, Forgejo and Gitea. A System One model answers six 0-100 rubric scores and nine yes/no merge gates in one pass, while a language model writes the review text and inline fixes. Runs fully offline with local GGUF models or with your own API keys.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dharmeshgurnani/CodeOtter) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://codeotter.io) |
| Pricing and access | Free AGPL-3.0 self-hosted build; the README says there is no paid tier (GitHub Sponsors only). Jev scoring needs your own TypeSafe key (or OpenRouter key) and is billed to that account; local GGUF models avoid API costs. Checked 2026-11-24. |
| Jev evidence | [`core/models.ts`](https://github.com/dharmeshgurnani/CodeOtter/blob/ff94d3e547a81191d7cd0092dd73c9950713a24c/core/models.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [dharmeshgurnani](https://github.com/dharmeshgurnani). Independently curated. |
| Format | Node.js / TypeScript web app and TUI |
| Platform and availability | Self-hosted Node.js web app (Docker, Render, Railway, Azure templates, or local `pnpm dev`). |
| Jev's role | With the TypeSafe Jev provider selected, Jev answers the score rubrics (five levels mapped to 0-100) and the yes/no merge gates; CodeOtter applies the pass/fail rules. Jev can be swapped for local System One-compatible runtimes or Jev via OpenRouter. |
| Requirements | Node.js 22+ and pnpm (or Docker); a Git provider token; a TypeSafe API key for Jev scoring (optional; local models also work). |
| License | [AGPL-3.0-only](https://github.com/dharmeshgurnani/CodeOtter/blob/ff94d3e547a81191d7cd0092dd73c9950713a24c/LICENSE) |

## When to use

- Add typed scores and merge gates to self-hosted PR review without a per-seat SaaS.
- Mismatch: a hosted, zero-setup reviewer; you run and maintain the server.

## How it works

`core/models.ts` posts `{ model, state, questions }` to `{baseUrl}/v1/systemone` (TypeSafe provider defaults to `https://api.typesafe.ai` with `jev-latest`, key from `TYPESAFE_API_KEY`); `core/engines.ts` defines the rubric and gate questions. Integration evidence: [`core/models.ts`](https://github.com/dharmeshgurnani/CodeOtter/blob/ff94d3e547a81191d7cd0092dd73c9950713a24c/core/models.ts).

## Get started

Run it locally from a checkout, then pick TypeSafe Jev as the System One provider in settings.

```sh
git clone https://github.com/dharmeshgurnani/CodeOtter.git && cd CodeOtter
pnpm dev   # http://localhost:5173
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Product site: [codeotter.io](https://codeotter.io)
- Dual-engine docs: [docs.codeotter.io/docs/dual-engine](https://docs.codeotter.io/docs/dual-engine)
- Engine questions: [github.com/dharmeshgurnani/codeotter/blob/ff94d3e547a81191d7cd0092dd73c9950713a24c/core/engines.ts](https://github.com/dharmeshgurnani/codeotter/blob/ff94d3e547a81191d7cd0092dd73c9950713a24c/core/engines.ts)

## Limits and data handling

With cloud providers, diffs and PR context are sent to TypeSafe (or OpenRouter) and the chosen language-model provider. AGPL-3.0-only, which matters if you offer it as a network service. Version 0.10.0 at review.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit ff94d3e547a8](https://github.com/dharmeshgurnani/CodeOtter/tree/ff94d3e547a81191d7cd0092dd73c9950713a24c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
