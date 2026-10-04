# Wingman

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Self-hosted inference hub that exposes a native `POST /v1/systemone` endpoint with a `typesafe` provider alongside chat, embeddings, RAG, and agent APIs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adrianliechti/wingman) |
| Maintainer | [adrianliechti](https://github.com/adrianliechti). Independently curated. |
| Format | Self-hosted AI gateway / inference hub |
| Requirements | Go build or container per upstream README; YAML provider config with a TypeSafe key for the `typesafe` provider. |
| License | [MIT](https://github.com/adrianliechti/wingman/blob/b691c8771973e36e1b32b5c192246dc8256da18e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Put TypeSafe Jev behind the same gateway as your LLM, embedding, and retrieval providers.
- Adapt a completion or embedding model to the System One request shape for comparison.
- Mismatch: if you only call Jev from one app, the official SDK is simpler.

## How it works

Wingman's native API includes `systemone`; the `typesafe` provider forwards to `https://api.typesafe.ai/v1/systemone` by default and returns the native probabilities and token usage, and models under it default to the `decider` role. See upstream [API.md](https://github.com/adrianliechti/wingman/blob/main/API.md#system-one).

## Get started

Configure a provider in `config.yaml` and run the server per the upstream Quick Start:

```sh
git clone https://github.com/adrianliechti/wingman.git
cd wingman
# add a `typesafe` provider to config.yaml (see README: TypeSafe / System One)
# start the server per README, then POST /v1/systemone
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Upstream README Quick Start config and the System One section of API.md.

## Limits and data handling

Requests are forwarded to TypeSafe with your key and billed by TypeSafe. You operate the gateway and its logs.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit b691c8771973](https://github.com/adrianliechti/wingman/tree/b691c8771973e36e1b32b5c192246dc8256da18e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
