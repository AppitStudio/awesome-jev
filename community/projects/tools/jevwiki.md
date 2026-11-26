# JevWiKi by xingchuan0105 (Rust tool that compiles a folder of documents into a Jev-tagged, quote-checked wiki served over MCP)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Turns a folder of Markdown or text files into a local knowledge base for agents without embeddings: Jev tags each passage on six axes and 34 fixed labels, questions are scored on the same axes, and answers must cite verbatim quotes from the corpus. One Rust binary, one SQLite file, and a stdio MCP server with 11 tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xingchuan0105/JevWiKi) |
| Maintainer | [xingchuan0105](https://github.com/xingchuan0105). Independently curated. |
| Format | Rust CLI and stdio MCP server |
| Requirements | Rust toolchain to build, a folder of `.md`/`.txt` files and a TypeSafe API key (required for tagging and serving). |
| License | [MIT OR Apache-2.0](https://github.com/xingchuan0105/JevWiKi/blob/91bc8e3e8b8169a49198479aace85dc349ea111c/LICENSE-MIT) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.rs`](https://github.com/xingchuan0105/JevWiKi/blob/91bc8e3e8b8169a49198479aace85dc349ea111c/src/jev.rs) at the pinned commit. |

## When to use

- Agents that need evidence-first answers over a personal or team document folder without running a vector database.
- Mismatch: very large corpora on a budget; every passage costs one Jev request at build time.

## How it works

`src/jev.rs` posts each passage to `https://api.typesafe.ai/v1/systemone` (model `jev-latest` by default) with the facet questions; retrieval matches question and passage facet scores by inner product and returns segment coordinates, and a session ledger rejects claims without a quote. Integration evidence: [`src/jev.rs`](https://github.com/xingchuan0105/JevWiKi/blob/91bc8e3e8b8169a49198479aace85dc349ea111c/src/jev.rs).

## Get started

Build the binary, put your TypeSafe key in `.env`, build the wiki and register `jevwiki serve` in your MCP client.

```sh
git clone https://github.com/xingchuan0105/JevWiKi && cd JevWiKi
cargo build --release
echo 'TYPESAFE_API_KEY=...' > /path/to/docs/.env
./target/release/jevwiki build --root /path/to/docs
./target/release/jevwiki serve --root /path/to/docs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Chinese README: [github.com/xingchuan0105/JevWiKi/blob/main/README.zh-CN.md](https://github.com/xingchuan0105/JevWiKi/blob/main/README.zh-CN.md)

## Limits and data handling

Passage text (up to about 2,400 characters each) goes to TypeSafe at build time, about 2.4K input tokens per passage; unchanged passages are not re-tagged. Without a key `build` stops before tagging and `serve` will not start. README in English and Chinese.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 91bc8e3e8b81](https://github.com/xingchuan0105/JevWiKi/tree/91bc8e3e8b8169a49198479aace85dc349ea111c). Inspected the README, both licence files, `Cargo.toml` (`MIT OR Apache-2.0`) and `src/jev.rs` at the pinned commit; nothing was built or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
