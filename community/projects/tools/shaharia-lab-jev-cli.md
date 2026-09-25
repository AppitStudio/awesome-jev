# jev-cli (shaharia-lab)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Rust CLI and MCP server for TypeSafe Jev: ask noul/choice/score about any text, get calibrated probabilities, exit codes for shells/CI, and JSON for scripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shaharia-lab/jev-cli) |
| Maintainer | [shaharia-lab](https://github.com/shaharia-lab). Independently curated. Distinct from [jev-cli (tumf)](tumf-jev-cli.md). |
| Format | Rust CLI (`jev`) + MCP; crates.io `jev-cli`. |
| Requirements | Rust toolchain or release binary; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/shaharia-lab/jev-cli/blob/299a2c29580208822eaf67c63cb2feff71bc2554/LICENSE-APACHE) (also MIT per upstream dual licence). |
| Disclosure | Unofficial community project (upstream README). AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe calls not run on the review host. |

## When to use

Use for **shell/CI gates and agent MCP** that need a semantic `if` over content. Prefer tumf's Python `jev-cli` if you want a PyPI workflow instead of Rust.

## How it works

You define the typed question; Jev returns probabilities; the CLI maps thresholds to exit codes and structured output for scripts and agents.

## Get started

```sh
# See upstream install.sh / crates.io jev-cli
git clone https://github.com/shaharia-lab/jev-cli.git
cd jev-cli
git checkout 299a2c29580208822eaf67c63cb2feff71bc2554
```

## Examples and demos

- README terminal demo GIF and docs under `docs/`.
- Example: `jev noul "Is this customer angry?" --state "..."`.

## Limits and data handling

Content and questions go to TypeSafe. Dual-licensed MIT OR Apache-2.0 upstream; this listing links Apache-2.0.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 299a2c2](https://github.com/shaharia-lab/jev-cli/tree/299a2c29580208822eaf67c63cb2feff71bc2554). AI-assisted README and license inspection; live CLI/MCP not executed.
