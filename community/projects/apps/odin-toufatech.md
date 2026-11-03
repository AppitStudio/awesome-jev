# Odin (French-language personal AI agent for terminal, web and Telegram, with an optional Jev judge for its action-severity questions)

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Personal AI agent with a local web UI, terminal, Telegram and HTTP API, built with no runtime dependencies. Before any action that writes, runs or sends, Odin asks itself seven simple questions and classifies the action as routine, important, serious or blocked; a local rules judge answers by default, and a Jev judge can be added to answer only when the local judge hesitates (or on every question). The documentation is in French.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TOUFATECH/Odin) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/TOUFATECH/Odin#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under MIT; you pay your model provider and, if enabled, TypeSafe through your own keys. Checked 2026-11-03. |
| Jev evidence | [`src/mimir/client.ts`](https://github.com/TOUFATECH/Odin/blob/208052946eb3872b51f1a52ccc863f33c1153a80/src/mimir/client.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [TOUFATECH](https://github.com/TOUFATECH). Independently curated. |
| Format | Node.js CLI and local server (installer script, Docker) |
| Platform and availability | macOS, Linux and Windows (installer script or source; Docker). |
| Jev's role | Optional second-opinion judge on action-severity questions when the local judge is unsure. |
| Requirements | Node.js 22.18+; a model provider key for the agent; `TYPESAFE_API_KEY` only for the optional Jev judge. |
| License | [MIT](https://github.com/TOUFATECH/Odin/blob/208052946eb3872b51f1a52ccc863f33c1153a80/LICENSE) |

## When to use

- Run an agent that asks before risky actions and decides routine ones on its own, with decisions logged.
- Mismatch: Jev is optional and off by default (`odin jev use local` is the default), and the docs are in French.

## How it works

`src/mimir/client.ts` is the Mímir adviser: it posts typed noul, choice and score questions to `https://api.typesafe.ai/v1/systemone` and returns probabilities, while the severity-to-action table stays in code (`src/mimir/decisions.ts`). Integration evidence: [`src/mimir/client.ts`](https://github.com/TOUFATECH/Odin/blob/208052946eb3872b51f1a52ccc863f33c1153a80/src/mimir/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/TOUFATECH/Odin.git
cd Odin
npm link
odin jev use local+jev   # optional: consult Jev only when the local judge hesitates
odin jev test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (French) with the decision levels and judges: [github.com/TOUFATECH/Odin#readme](https://github.com/TOUFATECH/Odin#readme)

## Limits and data handling

With `local+jev` or `jev` selected, the question about the pending action goes to TypeSafe on your key (the request passes through Odin's redaction module first); the README's 78 percent accuracy for the local judge is the author's own measurement. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 208052946eb3](https://github.com/TOUFATECH/Odin/tree/208052946eb3872b51f1a52ccc863f33c1153a80). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
