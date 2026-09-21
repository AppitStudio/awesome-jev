# Formanator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI and MCP client for submitting [Forma](https://www.joinforma.com/) benefit claims—optionally letting TypeSafe Jev pick benefit and category when you supply amount, merchant, date, and description yourself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timrogers/formanator) |
| Maintainer | [Tim Rogers](https://github.com/timrogers) / [timrogers/formanator](https://github.com/timrogers/formanator). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Rust CLI **5.4.0** (Homebrew / crates.io / release binaries) with an MCP server for claim workflows. |
| Requirements | Rust **1.94+** to build from source; Forma account (`formanator login`). Optional LLM receipt inference (GitHub Copilot CLI or OpenAI-compatible). Jev category selection needs `TYPESAFE_API_KEY` / `--typesafe-api-key` and `--category-provider jev` (or `FORMANATOR_CATEGORY_PROVIDER=jev`). |
| License | [MIT](https://github.com/timrogers/formanator/blob/548740edef37a4169eef163e4988e64f43a560ec/LICENSE.md). Forma, Copilot/OpenAI, and TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`src/typesafe.rs`, CLI flags, httpmock tests under `tests/typesafe_api.rs`). Offline `cargo test` was **not** run on the review host (rustc 1.85 &lt; required 1.94). Live Forma/TypeSafe/LLM calls were not run. |

## When to use

Use it when you submit Forma claims from the shell or an MCP host and want calibrated Jev choices over valid benefit/category pairs instead of free-form LLM category text. Prefer a plain LLM/`--category-provider` path when you do not have a TypeSafe key. Not a general expense OCR product—receipt image analysis still uses the configured LLM, not Jev.

## How it works

With `--category-provider jev`, [`src/typesafe.rs`](https://github.com/timrogers/formanator/blob/548740edef37a4169eef163e4988e64f43a560ec/src/typesafe.rs) posts a Choice question to `https://api.typesafe.ai` (default model `jev-latest`) over merchant, description, and Forma-returned benefit/category options. Jev does **not** receive receipt images. Confidence below 0.5 or a none-match visibly falls back to the configured OpenAI-compatible provider or Copilot CLI; TypeSafe auth/API errors are surfaced rather than silently ignored.

## Get started

```sh
# Install (pick one): brew tap timrogers/tap && brew install formanator
# or: cargo install formanator   # needs rustc ≥ 1.94
formanator login
export TYPESAFE_API_KEY=...   # do not paste secrets into chat
formanator submit-claim ... --category-provider jev
```

From source on the review host:

```sh
git clone https://github.com/timrogers/formanator.git
cd formanator
git checkout 548740edef37a4169eef163e4988e64f43a560ec
# cargo test   # requires rustc ≥ 1.94; not executed here
```

## Examples and demos

- Upstream README documents Homebrew/Cargo/binary install, MCP usage, CSV bulk submit, and the Jev category path.
- Integration tests in [`tests/typesafe_api.rs`](https://github.com/timrogers/formanator/blob/548740edef37a4169eef163e4988e64f43a560ec/tests/typesafe_api.rs) mock the TypeSafe API with httpmock (not executed on this host).

## Limits and data handling

Merchant, description, and category option labels leave the host on Jev calls; receipt pixels go only to the LLM provider when you use receipt inference. Forma access tokens live in the OS keychain (macOS) or `~/.formanator.toml`. Confirm Forma terms and TypeSafe billing separately. Unofficial community tool—not affiliated with Forma or TypeSafe.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 548740e](https://github.com/timrogers/formanator/tree/548740edef37a4169eef163e4988e64f43a560ec): **5.4.0**, MIT. AI-assisted source review of README, LICENSE.md, `src/typesafe.rs`, and `tests/typesafe_api.rs`. Build/tests skipped (MSRV 1.94). No live provider calls.

Related: [Foreman](foreman.md) (Codex supervision—unrelated name), [Clay JEV People Ranker](clay-jev-people-ranker.md).
