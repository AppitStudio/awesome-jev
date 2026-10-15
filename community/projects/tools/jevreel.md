# jevreel

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Zero-embedding video search for agents: lays a video out on labelled contact sheets, has Jev judge every sheet in parallel, re-checks the best windows on full frames and returns timed hits over MCP.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DeepAleph/jevreel) |
| Maintainer | [DeepAleph](https://github.com/DeepAleph). Independently curated. |
| Format | Python CLI and MCP server |
| Requirements | Python 3.11+ (or `uv`), ffmpeg-capable host, TypeSafe API key. |
| License | [MIT](https://github.com/DeepAleph/jevreel/blob/6107d4341d4da74856e446aa04eace8a8934280a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jevreel/judge.py`](https://github.com/DeepAleph/jevreel/blob/6107d4341d4da74856e446aa04eace8a8934280a/src/jevreel/judge.py) at the pinned commit. |

## When to use

- Let Claude Code, Codex or Cursor find moments in long videos without building a vector index.
- Search captions in speech mode for when something is said.
- Mismatch: per-query cost and accuracy depend on video length; demo figures are the author's.

## How it works

jevreel samples one frame per second onto contact sheets (sixty frames per image) and sends each sheet to Jev with typed questions using Jev's experimental image input; top windows are verified on full frames and returned as times with probabilities. All Jev calls go through `judge.py`. Integration evidence: [`src/jevreel/judge.py`](https://github.com/DeepAleph/jevreel/blob/6107d4341d4da74856e446aa04eace8a8934280a/src/jevreel/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install "jevreel[all]"
claude mcp add jevreel -e TYPESAFE_API_KEY=your-key -- uvx --from "jevreel[all]" jevreel mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Recorded Claude Code sessions on Blender's *Tears of Steel* in the upstream README.

## Limits and data handling

Video frames are sent to TypeSafe as images and billed to your key; no embeddings are stored.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 6107d4341d4d](https://github.com/DeepAleph/jevreel/tree/6107d4341d4da74856e446aa04eace8a8934280a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
