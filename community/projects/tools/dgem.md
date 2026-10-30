# dgem (DiffusionGemma as a zero-shot decision model with a /v1/systemone-compatible API)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turns DiffusionGemma 26B-A4B into a decision engine: write a decision as a template of typed questions (boolean, choice, score) and get per-option probabilities and a hesitation score from one pass, with hesitant cases handed to Gemini. Comes as a CLI, an HTTP gateway including `/v1/systemone`, an MCP server and a Decision Studio web app, plus benchmark harnesses and deployment guides for Apple Silicon, NVIDIA, Cloud Run and Vertex AI. Not an officially supported Google product, and not TypeSafe's Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/GoogleCloudPlatform/dgem) |
| Maintainer | [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform). Independently curated. |
| Format | Go CLI, HTTP gateway, MCP server and web app |
| Requirements | Apple Silicon Mac (Metal) or an NVIDIA GPU, or a Google Cloud endpoint; Go to build. |
| License | [Apache-2.0](https://github.com/GoogleCloudPlatform/dgem/blob/c5a9306a9466f4c4c78c7d3cee9edfdd592eb784/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`cmd/systemone_serve.go`](https://github.com/GoogleCloudPlatform/dgem/blob/c5a9306a9466f4c4c78c7d3cee9edfdd592eb784/cmd/systemone_serve.go) at the pinned commit. |

## When to use

- Run a self-hosted model that speaks the same request format as Jev and compare it on your own decisions.
- Mismatch: large model with GPU needs; it is an alternative to Jev, not a Jev client.

## How it works

`cmd/systemone_serve.go` serves `POST /v1/systemone` so clients written for Jev's request shape can call dgem instead. Integration evidence: [`cmd/systemone_serve.go`](https://github.com/GoogleCloudPlatform/dgem/blob/c5a9306a9466f4c4c78c7d3cee9edfdd592eb784/cmd/systemone_serve.go).

## Get started

From the upstream README (not run on the review host):

```sh
make setup && make download && make local-up   # Apple Silicon
make build
./bin/dgem decide -t templates/support_triage.json.tmpl -v 'ticket=I was billed twice' --stats
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs site: [googlecloudplatform.github.io/dgem/](https://googlecloudplatform.github.io/dgem/)

## Limits and data handling

Runs on your hardware or your Google Cloud project; cascade mode sends hesitant cases to Vertex AI Gemini.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit c5a9306a9466](https://github.com/GoogleCloudPlatform/dgem/tree/c5a9306a9466f4c4c78c7d3cee9edfdd592eb784). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
