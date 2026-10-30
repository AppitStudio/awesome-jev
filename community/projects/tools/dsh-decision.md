# dsh-decision (DeepSeek Harness plugin that gives the chat model a decision_ask tool backed by Jev or a local Clef)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small DeepSeek Harness plugin that exposes a System One decision model to the chat model as a `decision_ask` tool taking a state and noul, choice or score questions. The provider is hot-reloadable configuration: hosted Jev (`jev-latest` at `api.typesafe.ai`) or a LAN-hosted Clef with the same request shape, switchable per call. The README notes that Jev sends the state to TypeSafe, so egress needs owner sign-off.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tsangkingyiu/dsh-decision) |
| Maintainer | [tsangkingyiu](https://github.com/tsangkingyiu). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript) |
| Requirements | DeepSeek Harness; `TYPESAFE_API_KEY` in the launching environment for the Jev route. |
| License | [MIT](https://github.com/tsangkingyiu/dsh-decision/blob/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/tsangkingyiu/dsh-decision/blob/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d/src/index.ts) at the pinned commit. |

## When to use

- Let an agent ask calibrated typed questions instead of parsing prose judgments, with a local-model option for sensitive data.
- Mismatch: a thin tool wrapper; deciding what to ask is left to the chat model.

## How it works

`index.ts` registers `decision_ask`, picks the provider from config or the per-call `provider` argument, posts state and questions to `/v1/systemone` and returns answers keyed by question id with usage. Integration evidence: [`src/index.ts`](https://github.com/tsangkingyiu/dsh-decision/blob/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd ~/.dsh/profiles/web
npm install /path/to/dsh-decision
dsh plugin --profile web allow-version @tsangkingyiu/dsh-decision@<ver> --dsh-version $(dsh --version) --accept-risk
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tool contract: [github.com/tsangkingyiu/dsh-decision/blob/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d/README.md#tool-contract](https://github.com/tsangkingyiu/dsh-decision/blob/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d/README.md#tool-contract)

## Limits and data handling

On the Jev route the state the model passes is sent to TypeSafe. New repository with no releases. Not affiliated with TypeSafe or DeepSeek.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 7eb0e83f166d](https://github.com/tsangkingyiu/dsh-decision/tree/7eb0e83f166d6b3f8c98ad6045cf417e7f3e587d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
