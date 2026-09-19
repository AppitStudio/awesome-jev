# SkillRanker

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rank which agent skills fit the next step from live session context, using TypeSafe Jev for wide comparison and shortlist re-ranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Dicklesworthstone/skillranker) |
| Maintainer | [Dicklesworthstone](https://github.com/Dicklesworthstone) / Jeffrey Emanuel. Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust CLI (`sr`) with Claude Code hook integration, JSON output, and an inline TUI. |
| Requirements | Rust toolchain matching `rust-toolchain.toml` to build. Ranking requires `TYPESAFE_API_KEY`. Offline `sr demo --case …` fixtures need no key. Large skill libraries may use local Quill narrowing before Jev (see upstream docs). |
| License | [MIT with an OpenAI/Anthropic exclusion rider](https://github.com/Dicklesworthstone/skillranker/blob/5d8fd0fdb15859d9d6d149da3356598ef2f82f75/LICENSE). GitHub reports `NOASSERTION` / Other because of the rider. **Restricted parties (OpenAI, Anthropic, affiliates, and agents acting for them) receive no license.** Disclose this before reuse. |

## When to use

Use it when a coding agent has a large skill inventory and you want an inspectable, Jev-backed ranking of which skills fit the current turn—including a real “none of these” option—rather than loading skills from description similarity alone.

It is advisory: the agent and user still decide what to consult. It does not substitute a local model for Jev.

## How it works

The [TypeSafe codec and endpoint helpers](https://github.com/Dicklesworthstone/skillranker/blob/5d8fd0fdb15859d9d6d149da3356598ef2f82f75/src/jev/) target `https://api.typesafe.ai` + `/v1/systemone` with default model `jev-latest`. Wide and re-rank stages compare candidates with structured questions; local feedback and calibration stay on disk. Explicit skill requests can resolve locally before network stages.

## Get started

```sh
git clone https://github.com/Dicklesworthstone/skillranker.git
cd skillranker
git checkout 5d8fd0fdb15859d9d6d149da3356598ef2f82f75
cargo install --locked --path . --bin sr
sr demo --case useful
```

`sr demo` inspects offline fixtures. `sr rank --allow-network` and live hooks need a TypeSafe key and incur charges. This review did not complete a full `cargo test` (git dependency `asupersync` blocked `--offline` builds on the review machine).

## Examples and demos

- Offline demos via `sr demo --case …` (documented in the upstream README).
- Claude Code hook: `sr hook claude`.
- Inline TUI: `sr tui`.

## Limits and data handling

Session context and skill descriptions are sent to TypeSafe when ranking with the network. Retention follows TypeSafe's terms. The OpenAI/Anthropic license rider restricts who may use or redistribute the software. Ranking quality was not independently measured.

## Review and maintenance

Reviewed on **2026-09-19** at [commit 5d8fd0f](https://github.com/Dicklesworthstone/skillranker/tree/5d8fd0fdb15859d9d6d149da3356598ef2f82f75): Cargo package **0.1.0**. AI-assisted source review of README, LICENSE rider, and `src/jev/` (endpoint, codec, wide/rerank). No live TypeSafe calls. Full offline `cargo test` was not run here.

Related: [Skillbox](skillbox.md) hosts a skill library with optional Jev recommendations; SkillRanker focuses on ranking against live session context.
