# Ollaya

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

'Ollama for decision models': one Rust binary that pulls open decision models by name (Laya, winnow, decider, NLI, GLiClass), serves them from a local daemon and speaks TypeSafe's `/v1/systemone`, `/v1/decisions` and `/v1/models` wire format, so existing Jev clients and the official SDK work by pointing `TYPESAFE_BASE_URL` at localhost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ollaya-dev/ollaya) |
| Product homepage | [ollaya.dev](https://ollaya.dev) |
| Maintainer | [ollaya-dev](https://github.com/ollaya-dev). Independently curated. |
| Format | Single binary CLI/daemon (`ollaya serve`, `run`, `pull`, `list`, `ps`, `show`, `rm`, `create`) with install script |
| Requirements | macOS or Linux (NVIDIA GPU recommended for 4B-class models; `laya` runs on CPU). No TypeSafe key for local models. |
| License | [Apache-2.0](https://github.com/ollaya-dev/ollaya/blob/e352e0ff7086e85f7f115487f77310c13203a7a6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Develop or test Jev integrations offline against a local, wire-compatible server.
- Keep sensitive decision traffic on your own machine.
- Mismatch: open models score below hosted Jev on the project's own typed-decision benchmark (e.g. winnow:e4b 0.722 vs Jev 0.738, upstream-reported).

## How it works

The daemon ([`crates/ollaya-server`](https://github.com/ollaya-dev/ollaya/tree/e352e0ff7086e85f7f115487f77310c13203a7a6/crates/ollaya-server)) exposes TypeSafe-shaped routes plus a native `/api/decide` with routing and timings; [`crates/ollaya-registry`](https://github.com/ollaya-dev/ollaya/tree/e352e0ff7086e85f7f115487f77310c13203a7a6/crates/ollaya-registry) pulls models and `convert/` exports supported families. The CLI starts the daemon on demand.

## Get started

Install and run a preset (README):

```sh
curl -fsSL https://ollaya.dev/install.sh | sh
ollaya run winnow:e4b --preset triage "Refund it today or I'm cancelling."
# point an existing Jev client at it
export TYPESAFE_BASE_URL=http://localhost:11435
```

No inference charges for local models.

## Examples and demos

- Model catalog with numbers: [ollaya.dev/search](https://ollaya.dev/search).
- README *Features* and model table.

## Limits and data handling

Independent project, not affiliated with Ollama or TypeSafe. Benchmark figures are upstream-reported. The install script is fetched from ollaya.dev; review it before piping to a shell. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit e352e0ff7086](https://github.com/ollaya-dev/ollaya/tree/e352e0ff7086e85f7f115487f77310c13203a7a6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
