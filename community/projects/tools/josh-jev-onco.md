# Jev Onco Statistical Hierarchy (JOSH) (Rust research workbench that asks Jev for a cancer-of-unknown-primary origin distribution and gates it locally)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Ratatui TUI and CLI for cancer-of-unknown-primary research: it imports molecular, expression and clinical evidence, sends one request where Jev answers a 22-class primary-site Choice plus evidence-sufficiency, conflict and boundary questions, then checks the answer, applies local abstain/review gates, charts rankings and exports Markdown, with optional Shapley explanations over saved runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy) |
| Maintainer | [SampleBias](https://github.com/SampleBias). Independently curated. |
| Format | Rust workspace: TUI, CLI and loopback API (MIT) |
| Requirements | Cargo with pinned Rust 1.98.1, a C compiler, and a TypeSafe key for live runs (synthetic data only). |
| License | [MIT](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/josh-jev/src/lib.rs`](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/crates/josh-jev/src/lib.rs) at the pinned commit. |

## When to use

- Explore how a typed decision model handles origin-of-cancer evidence on synthetic research data.
- Mismatch: any clinical use; accuracy and clinical calibration are unvalidated and only declared synthetic data is accepted for live calls.

## How it works

`crates/josh-jev/src/lib.rs` posts to `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.13.0`; rate-limit and overload responses retry at most twice. `josh molecular prepare` prints the request without sending it, and saved runs keep the prompt version they were prepared with. Integration evidence: [`crates/josh-jev/src/lib.rs`](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/crates/josh-jev/src/lib.rs).

## Get started

Start the TUI, open a bundled sample, then use Data → Run analysis.

```sh
git clone https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy && cd Jev_Onco_Statistical_Hierarchy
./scripts/start
# offline: josh molecular prepare  (prints the request, sends nothing)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/README.md](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/README.md)
- Quickstart: [github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/docs/QUICKSTART.md](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/docs/QUICKSTART.md)
- Jev workflow: [github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/docs/references/JEV_WORKFLOW.md](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/blob/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe/docs/references/JEV_WORKFLOW.md)

## Limits and data handling

Live calls send the prepared evidence to TypeSafe on your key; the tool accepts declared synthetic data only. Research software, not a diagnostic device; the authors state accuracy and clinical calibration remain unvalidated.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 030cbc8a6a0c](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy/tree/030cbc8a6a0c3bc77da2521b8c969bc900e07cbe). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
