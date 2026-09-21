# triagedy

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

UNIX-filter style security-alert triage: JSONL alerts in, typed dispositions out. Default backend is TypeSafe Jev (Choice / Score / Noul); policy routing stays in ordinary Rust code. Optional OpenAI-compatible backends share the same pipeline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m0rphtail/triagedy) |
| Maintainer | [m0rphtail](https://github.com/m0rphtail). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Rust CLI crate **`triagedy` 0.1.0** (edition 2024). |
| Requirements | Rust toolchain able to build edition 2024 (upstream targets recent rustc). Live Jev path needs `TYPESAFE_API_KEY` (or `triagedy login`). OpenAI-compatible path uses `--backend openai`. |
| License | [MIT](https://github.com/m0rphtail/triagedy/blob/5f8f6380c7c8ebfe47d437e38f6d28dcbfb7ada0/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; `cargo test` not completed here (host rustc 1.85 too old for current transitive crates needing ≥1.88). No live TypeSafe calls. |

## When to use

Use it when SOC Tier-1 style alerts should be screened with calibrated typed questions before humans or heavier tooling. Prefer [Metis](metis.md) for GitHub issue triage, or [jev-guard](jev-guard.md) for coding-agent tool-call gates.

## How it works

For each alert the Jev backend posts five orthogonal System One questions (disposition Choice, severity Score, false-positive Noul, IR-escalation Noul, ATT&CK-category Choice) to `https://api.typesafe.ai/v1/systemone`. Answers are schema-validated; invalid replies become error records. A separate policy layer maps validated answers to actions—the model judges, code decides. Workflow mapping is documented against NIST SP 800-61 Rev. 2 and MITRE ATT&CK in upstream docs.

## Get started

```sh
git clone https://github.com/m0rphtail/triagedy.git
cd triagedy
git checkout 5f8f6380c7c8ebfe47d437e38f6d28dcbfb7ada0
cargo build --release
cat alerts.jsonl | ./target/release/triagedy run | jq '.action'
```

Live runs send alert context to TypeSafe (or your OpenAI-compatible server) and can incur charges.

## Examples and demos

- README five-question table and NIST/ATT&CK mapping.
- Mock backend and wiremock-oriented tests under `tests/` / `src/backends/mock.rs` (not executed in this environment).

## Limits and data handling

Alert payloads leave the host on live backends. OpenAI-compatible confidence is uncalibrated per upstream. This listing did not reproduce accuracy benchmarks in `docs/ACCURACY_BENCHMARKS.md`.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 5f8f638](https://github.com/m0rphtail/triagedy/tree/5f8f6380c7c8ebfe47d437e38f6d28dcbfb7ada0): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `Cargo.toml`, `backends/jev.rs`, questions/policy modules. Cargo tests blocked by rustc 1.85 vs dependency MSRV. No live provider calls.

Related: [Metis](metis.md), [jev-guard](jev-guard.md), [jev-sec-bench](jev-sec-bench.md).
