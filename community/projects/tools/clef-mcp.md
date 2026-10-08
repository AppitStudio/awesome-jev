# clef-mcp

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MCP server (Japanese docs) that lets Claude Code ask Cloudflare Clef — a Jev / System One API-compatible decision model hosted on Ollama — for typed decisions: one `decide(state, questions, images?)` tool wraps Ollama's `POST /v1/systemone` with `noul` / `choice` / `score` questions (up to 64) and optional local images, plus a `health()` check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kanedayo/clef-mcp) |
| Maintainer | [kanedayo](https://github.com/kanedayo). Independently curated. |
| Format | MCP server (`clef_mcp.py`, `install.sh --register`) |
| Requirements | Python; an Ollama build with decision support (0.35 series tested) serving `clef` or `clef-flash`; Claude Code. |
| License | [Apache-2.0](https://github.com/kanedayo/clef-mcp/blob/91679b66683769b84d17fd063d68dbc640cdc322/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give Claude Code a cheap, local classifier for yes/no, choice and score questions.
- Use image-aware decisions (Clef is multimodal).
- Mismatch: uses Clef via Ollama, not hosted Jev.

## How it works

[`clef_mcp.py`](https://github.com/kanedayo/clef-mcp/blob/91679b66683769b84d17fd063d68dbc640cdc322/clef_mcp.py) validates questions, base64-encodes images and posts to `$CLEF_BASE_URL/v1/systemone`. Use cases: [`USECASES.md`](https://github.com/kanedayo/clef-mcp/blob/91679b66683769b84d17fd063d68dbc640cdc322/USECASES.md).

## Get started

Install and register (README):

```sh
git clone https://github.com/kanedayo/clef-mcp.git && cd clef-mcp
CLEF_BASE_URL=http://<ollama-host>:11434 ./install.sh --register
```

No API charges; runs on your Ollama host.

## Examples and demos

- README tool table and image examples.

## Limits and data handling

State and images go to the configured Ollama server. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 91679b666837](https://github.com/kanedayo/clef-mcp/tree/91679b66683769b84d17fd063d68dbc640cdc322). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
