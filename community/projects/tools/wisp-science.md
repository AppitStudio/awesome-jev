# Wisp Science (local-first AI research workbench with a TypeSafe Jev decision model)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-source desktop research workbench (literature, Python/R, ~80 scientific databases) that can use TypeSafe Jev as its System One decision model for item mapping, row decisions and an optional desktop autopilot.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xuzhougeng/wisp-science) |
| Maintainer | [xuzhougeng](https://github.com/xuzhougeng). Independently curated. |
| Format | Rust core + macOS/desktop app (AGPL-3.0) |
| Requirements | Wisp desktop build, your own LLM, and a TypeSafe API key for Jev decisions. |
| License | [AGPL-3.0](https://github.com/xuzhougeng/wisp-science/blob/7eb4f0bd57c474d42da2691e50be41b023c69c58/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`crates/wisp-llm/src/systemone.rs`](https://github.com/xuzhougeng/wisp-science/blob/7eb4f0bd57c474d42da2691e50be41b023c69c58/crates/wisp-llm/src/systemone.rs) at the pinned commit. |

## When to use

- Screen literature or data rows with calibrated Jev decisions.
- Keep a research trail local with BYO models.
- Mismatch: decision model is optional; defaults use your LLM.

## How it works

`wisp-llm/src/systemone.rs` implements the System One client used by `wisp-core/src/map_items` to attach pass/reject/uncertain Jev decisions; Settings → Models → Decision model accepts TypeSafe Jev or other System One servers. Integration evidence: [`crates/wisp-llm/src/systemone.rs`](https://github.com/xuzhougeng/wisp-science/blob/7eb4f0bd57c474d42da2691e50be41b023c69c58/crates/wisp-llm/src/systemone.rs).

## Get started

Install from the upstream releases, then configure Settings → Models → Decision model with a TypeSafe key.

```sh
git clone https://github.com/xuzhougeng/wisp-science.git && cd wisp-science
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/xuzhougeng/wisp-science/blob/7eb4f0bd57c474d42da2691e50be41b023c69c58/README.md](https://github.com/xuzhougeng/wisp-science/blob/7eb4f0bd57c474d42da2691e50be41b023c69c58/README.md)

## Limits and data handling

Items you map are sent to TypeSafe when Jev is configured as the decision model.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 7eb4f0bd57c4](https://github.com/xuzhougeng/wisp-science/tree/7eb4f0bd57c474d42da2691e50be41b023c69c58). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
