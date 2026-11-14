# Scholar Engine MCP (scientific-literature MCP server that queries arXiv metadata in place and uses Jev yes/no gates to filter papers by questions like "tested on real hardware?")

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

FastMCP server and CLI for coding and research agents: it queries Hugging Face's arXiv metadata Parquet files over HTTP with DuckDB (no bulk download), enriches results with OpenAlex citations, and turns natural-language filters into Jev yes/no predicates with probability thresholds whose answers are cached for reuse. Without a key it falls back to heuristics clearly marked unverified.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wolverin0/scholar-mcp) |
| Maintainer | [wolverin0](https://github.com/wolverin0). Independently curated. |
| Format | Python MCP server and CLI (MIT) |
| Requirements | Python 3.10+; a `TYPESAFE_API_KEY` for Jev gates (otherwise heuristic mode). |
| License | [MIT](https://github.com/wolverin0/scholar-mcp/blob/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scholar/jev/client.py`](https://github.com/wolverin0/scholar-mcp/blob/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793/scholar/jev/client.py) at the pinned commit. |

## When to use

- Let an agent filter arXiv papers on empirical properties that keyword or vector search misses.
- Mismatch: full-text review; it judges paper metadata and abstracts, not PDFs.

## How it works

`scholar/jev/client.py` posts yes/no (Noul) questions to `https://api.typesafe.ai/v1/systemone`; `scholar/jev/gates.py` applies the probability thresholds, and the MCP server labels results as `unverified_heuristic` when no key is set. Integration evidence: [`scholar/jev/client.py`](https://github.com/wolverin0/scholar-mcp/blob/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793/scholar/jev/client.py).

## Get started

Install from a checkout and start the MCP server.

```sh
git clone https://github.com/wolverin0/scholar-mcp.git && cd scholar-mcp
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]" "mcp<2"
export TYPESAFE_API_KEY=...
python -m scholar.mcp.server
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/wolverin0/scholar-mcp/blob/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793/README.md](https://github.com/wolverin0/scholar-mcp/blob/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793/README.md)

## Limits and data handling

Paper titles and abstracts plus your filter questions are sent to TypeSafe on your key; arXiv metadata is read from Hugging Face and citations from OpenAlex.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 06a5062b6c6d](https://github.com/wolverin0/scholar-mcp/tree/06a5062b6c6d26f22f84c9a65dae50ba1dcbf793). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
