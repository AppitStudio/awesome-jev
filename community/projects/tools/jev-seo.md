# jev-seo

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Agent-oriented SEO/GEO CLI and MCP server: local DuckDuckGo SERP/audit helpers plus optional TypeSafe Jev scoring for intent, gaps, and AI-visibility style judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AkashPriyadarshii/jev-seo) |
| Maintainer | [AkashPriyadarshii](https://github.com/AkashPriyadarshii) (Akash Priyadarshi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust crate / CLI **jev-seo 0.1.0** (`cargo install jev-seo`) with stdio MCP (`src/mcp.rs`). |
| Requirements | Rust toolchain for source builds; live Jev scoring needs `TYPESAFE_API_KEY`. SERP/audit paths scrape public DuckDuckGo HTML endpoints (network required). Local history uses SQLite (`.jev-seo.db`). |
| License | [MIT](https://github.com/AkashPriyadarshii/jev-seo/blob/0b1ab0da90021029ae562ba2b224fbf563292cea/LICENSE). |

## When to use

Use it when an agent or developer wants a local CLI/MCP for directory audits, robots/AI-crawler checks, schema sniffing, and SERP-oriented briefs with optional Jev judgments—without a paid SEO SaaS. Prefer [Testimonial miner](testimonial-miner.md) for email praise mining, or [jegrep](jegrep.md) / [jev-semgrep](jev-semgrep.md) for meaning search over files. Upstream “Semrush alternative” marketing is vendor framing; this listing does not claim feature or quality parity with commercial SEO suites.

## How it works

[`src/engine.rs`](https://github.com/AkashPriyadarshii/jev-seo/blob/0b1ab0da90021029ae562ba2b224fbf563292cea/src/engine.rs) posts to TypeSafe `https://api.typesafe.ai/v1/systemone` (reviewed default model `jev-1.13.0`) when a key is present. Other modules (`serp.rs`, `audit.rs`, `schema.rs`, `robots.rs`, `brief.rs`, `rank.rs`) handle scraping, file audits, and local SQLite rank history. [`src/mcp.rs`](https://github.com/AkashPriyadarshii/jev-seo/blob/0b1ab0da90021029ae562ba2b224fbf563292cea/src/mcp.rs) exposes tools over stdio JSON-RPC for coding agents.

## Get started

```sh
cargo install jev-seo
# or:
git clone https://github.com/AkashPriyadarshii/jev-seo.git
cd jev-seo
git checkout 0b1ab0da90021029ae562ba2b224fbf563292cea
export TYPESAFE_API_KEY=…
# Examples (network / billable as applicable):
# jev-seo audit docs/
# jev-seo robots example.com
# jev-seo query "offline expense tracker android"
```

Scraping and live Jev calls leave the machine. This listing did not run Cargo tests or call TypeSafe.

## Examples and demos

- README quickstart for `query`, `audit`, `schema`, `robots`, and content briefs.
- Unit tests in [`src/tests.rs`](https://github.com/AkashPriyadarshii/jev-seo/blob/0b1ab0da90021029ae562ba2b224fbf563292cea/src/tests.rs).
- Design notes under `docs/`.

## Limits and data handling

SERP/HTML fetches and optional Jev state text leave the host. DuckDuckGo HTML scraping can break if upstream markup changes. Rank history is local SQLite. Treat commercial-suite replacement claims as unverified. Early **0.1.0** crate—confirm `cargo install` availability on crates.io before relying on that path.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 0b1ab0d](https://github.com/AkashPriyadarshii/jev-seo/tree/0b1ab0da90021029ae562ba2b224fbf563292cea): **0.1.0**, MIT. AI-assisted source review of README, `engine.rs`, `mcp.rs`, `Cargo.toml`, and license. No `cargo test`, no live scrape, and no TypeSafe calls on the review host.

Related: [Testimonial miner](testimonial-miner.md), [jev-semgrep](jev-semgrep.md).
