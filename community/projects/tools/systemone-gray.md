# systemone (gray plugin)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust sidecar plugin for the gray agent that puts System One decision models (TypeSafe Jev, Laya via Ollaya, any `/v1/systemone` server) behind `judge` and `semantic_find` tools plus a `/s1` chat command.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vstaln/systemone) |
| Maintainer | [vstaln](https://github.com/vstaln). Independently curated. |
| Format | Rust plugin |
| Requirements | Rust toolchain, gray; a `/v1/systemone` backend (local Ollaya by default, or TypeSafe with a key). |
| License | [MIT](https://github.com/vstaln/systemone/blob/9533d330cf34ff24bc51df0b4524486cba029146/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.rs`](https://github.com/vstaln/systemone/blob/9533d330cf34ff24bc51df0b4524486cba029146/src/client.rs) at the pinned commit. |

## When to use

- Give a gray agent typed probabilities instead of prose for checks.
- Search code by meaning when grep is not enough.
- Mismatch: plugin for one specific agent host.

## How it works

`src/client.rs` is a synchronous client for `POST /v1/systemone` with a configurable base URL. `judge` asks typed questions about a state; `semantic_find` scores file chunks against a plain-language query. Set `SYSTEMONE_BASE_URL=https://api.typesafe.ai` and `SYSTEMONE_MODEL=jev-latest` to use Jev. Integration evidence: [`src/client.rs`](https://github.com/vstaln/systemone/blob/9533d330cf34ff24bc51df0b4524486cba029146/src/client.rs).

## Get started

From the upstream README: build the plugin, install it in gray, and set the `SYSTEMONE_*` environment variables.

```sh
export SYSTEMONE_BASE_URL=https://api.typesafe.ai SYSTEMONE_MODEL=jev-latest SYSTEMONE_API_KEY=...
# build and install per README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README backends table (Ollaya, TypeSafe, compatible servers)

## Limits and data handling

State and file chunks go to the configured backend. Local Laya and hosted Jev give different quality.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 9533d330cf34](https://github.com/vstaln/systemone/tree/9533d330cf34ff24bc51df0b4524486cba029146). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
